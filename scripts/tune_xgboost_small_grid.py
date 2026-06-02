from __future__ import annotations

import argparse
import itertools
import sys
import time
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    from src import config as cfg
except ImportError:
    cfg = None


def cfg_value(name: str, fallback):
    if cfg is None:
        return fallback
    return getattr(cfg, name, fallback)


DATA_PROCESSED = Path(cfg_value("DATA_PROCESSED", ROOT / "data" / "processed"))

TRAIN_PATH = Path(cfg_value("TRAIN_FINAL_PATH", DATA_PROCESSED / "train_final.csv"))
VAL_PATH = Path(cfg_value("VAL_FINAL_PATH", DATA_PROCESSED / "val_final.csv"))
TEST_PATH = Path(cfg_value("TEST_FINAL_PATH", DATA_PROCESSED / "test_final.csv"))

TARGET_COLUMN = cfg_value("TARGET_COLUMN", "Power_Output_Normalized")
BASELINE_COLUMN = cfg_value("BASELINE_COLUMN", "Baseline_Prediction")
PARK_ID_COLUMN = cfg_value("PARK_ID_COLUMN", "park_id")
TIMESTAMP_COLUMN = cfg_value("TIMESTAMP_COLUMN", "timestamp")
TEST_FLAG_COLUMN = cfg_value("TEST_FLAG_COLUMN", "test_flag")
DEFAULT_SEED = int(cfg_value("RANDOM_SEED", 42))

OUTPUT_DIR = DATA_PROCESSED / "diagnostics" / "baseline_tuning"

SMALL_GRID: dict[str, list[Any]] = {
    "n_estimators": [400, 500],
    "max_depth": [6, 8],
    "learning_rate": [0.03, 0.05],
    "subsample": [0.8],
    "colsample_bytree": [0.8],
}
GRID_KEYS = [
    "n_estimators",
    "max_depth",
    "learning_rate",
    "subsample",
    "colsample_bytree",
]

SMOKE_DEFAULT_MAX_TRAIN_ROWS = 10_000
SMOKE_DEFAULT_MAX_VAL_ROWS = 2_000
SMOKE_DEFAULT_MAX_TEST_ROWS = 2_000


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("row caps must be positive integers")
    return parsed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run a minimal, validation-selected XGBoost small-grid tuning audit."
        )
    )
    parser.add_argument(
        "--smoke",
        action="store_true",
        help=(
            "Run two deterministic configs with deterministic row caps for "
            "code validation only. Smoke outputs are not manuscript evidence."
        ),
    )
    parser.add_argument(
        "--max-train-rows",
        type=positive_int,
        default=None,
        help="Optional deterministic cap on train rows, using file order.",
    )
    parser.add_argument(
        "--max-val-rows",
        type=positive_int,
        default=None,
        help="Optional deterministic cap on validation rows, using file order.",
    )
    parser.add_argument(
        "--max-test-rows",
        type=positive_int,
        default=None,
        help="Optional deterministic cap on test rows, using file order.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=DEFAULT_SEED,
        help=f"Random seed for XGBoost. Default: {DEFAULT_SEED}.",
    )
    return parser.parse_args()


def require_existing_file(path: Path, label: str) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Missing required {label}: {path}")
    if not path.is_file():
        raise FileNotFoundError(f"Required {label} is not a file: {path}")


def read_header(path: Path) -> pd.Index:
    return pd.read_csv(path, nrows=0).columns


def build_parameter_grid() -> list[dict[str, Any]]:
    configs: list[dict[str, Any]] = []
    value_lists = [SMALL_GRID[key] for key in GRID_KEYS]
    for values in itertools.product(*value_lists):
        configs.append(dict(zip(GRID_KEYS, values)))
    return configs


def select_configs_for_run(args: argparse.Namespace) -> list[dict[str, Any]]:
    configs = build_parameter_grid()
    if not args.smoke:
        return configs
    return [configs[0], configs[-1]]


def resolve_row_caps(args: argparse.Namespace) -> tuple[int | None, int | None, int | None]:
    if not args.smoke:
        return args.max_train_rows, args.max_val_rows, args.max_test_rows

    train_cap = args.max_train_rows or SMOKE_DEFAULT_MAX_TRAIN_ROWS
    val_cap = args.max_val_rows or SMOKE_DEFAULT_MAX_VAL_ROWS
    test_cap = args.max_test_rows or SMOKE_DEFAULT_MAX_TEST_ROWS
    return train_cap, val_cap, test_cap


def infer_run_mode(
    args: argparse.Namespace,
    train_cap: int | None,
    val_cap: int | None,
    test_cap: int | None,
) -> str:
    if args.smoke:
        return "smoke"
    if any(cap is not None for cap in [train_cap, val_cap, test_cap]):
        return "capped"
    return "full"


def output_paths(run_mode: str) -> dict[str, Path]:
    prefix = "xgboost_small_grid" if run_mode == "full" else f"xgboost_small_grid_{run_mode}"
    return {
        "validation": OUTPUT_DIR / f"{prefix}_validation.csv",
        "selected_test": OUTPUT_DIR / f"{prefix}_selected_test_metrics.csv",
        "manifest": OUTPUT_DIR / f"{prefix}_run_manifest.csv",
    }


def validate_required_columns(headers: dict[str, pd.Index]) -> None:
    blocked_columns = {
        TARGET_COLUMN,
        PARK_ID_COLUMN,
        TIMESTAMP_COLUMN,
        TEST_FLAG_COLUMN,
        BASELINE_COLUMN,
    }

    missing_train = sorted(blocked_columns - set(headers["train"]))
    if missing_train:
        raise KeyError(
            "Missing required columns from train split: " + ", ".join(missing_train)
        )

    for split_name in ["val", "test"]:
        if TARGET_COLUMN not in headers[split_name]:
            raise KeyError(f"Missing target column from {split_name} split.")


def candidate_feature_columns(train_columns: pd.Index) -> list[str]:
    blocked_columns = {
        TARGET_COLUMN,
        PARK_ID_COLUMN,
        TIMESTAMP_COLUMN,
        TEST_FLAG_COLUMN,
        BASELINE_COLUMN,
    }
    return [col for col in train_columns if col not in blocked_columns]


def read_split(
    path: Path,
    columns: list[str],
    max_rows: int | None,
) -> pd.DataFrame:
    return pd.read_csv(path, usecols=columns, nrows=max_rows)


def load_train_split(
    candidate_columns: list[str],
    max_rows: int | None,
) -> tuple[pd.DataFrame, list[str], list[str]]:
    use_columns = [TARGET_COLUMN, *candidate_columns]
    train_df = read_split(TRAIN_PATH, use_columns, max_rows)

    numeric_features = [
        col for col in candidate_columns if pd.api.types.is_numeric_dtype(train_df[col])
    ]
    non_numeric_excluded = sorted(set(candidate_columns) - set(numeric_features))

    if not numeric_features:
        raise ValueError("No numeric learned feature columns were found.")

    return train_df, numeric_features, non_numeric_excluded


def validate_feature_availability(
    headers: dict[str, pd.Index],
    numeric_features: list[str],
) -> None:
    required_columns = {TARGET_COLUMN, *numeric_features}
    for split_name in ["val", "test"]:
        missing = sorted(required_columns - set(headers[split_name]))
        if missing:
            raise KeyError(
                f"Missing selected columns from {split_name} split: "
                + ", ".join(missing)
            )


def validate_no_nulls(df: pd.DataFrame, columns: list[str], split_name: str) -> None:
    null_count = int(df[columns].isnull().sum().sum())
    if null_count:
        raise ValueError(
            f"Found {null_count} null values in selected {split_name} columns."
        )


def split_xy(
    df: pd.DataFrame,
    numeric_features: list[str],
    split_name: str,
) -> tuple[pd.DataFrame, pd.Series]:
    selected_columns = [TARGET_COLUMN, *numeric_features]
    validate_no_nulls(df, selected_columns, split_name)
    return df[numeric_features].copy(), df[TARGET_COLUMN].copy()


def compute_metrics(y_true: pd.Series, y_pred: np.ndarray) -> dict[str, float]:
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

    mse = mean_squared_error(y_true, y_pred)
    return {
        "MAE": float(mean_absolute_error(y_true, y_pred)),
        "RMSE": float(np.sqrt(mse)),
        "R2": float(r2_score(y_true, y_pred)),
    }


def build_model(params: dict[str, Any], seed: int) -> Any:
    from xgboost import XGBRegressor

    return XGBRegressor(
        objective="reg:squarederror",
        random_state=seed,
        n_jobs=-1,
        tree_method="hist",
        **params,
    )


def tune_on_validation(
    configs: list[dict[str, Any]],
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_val: pd.DataFrame,
    y_val: pd.Series,
    seed: int,
    run_mode: str,
) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for config_id, params in enumerate(configs, start=1):
        fit_start = time.perf_counter()
        model = build_model(params, seed)
        model.fit(X_train, y_train)
        val_pred = model.predict(X_val)
        metrics = compute_metrics(y_val, val_pred)
        fit_seconds = time.perf_counter() - fit_start

        rows.append(
            {
                "run_mode": run_mode,
                "config_id": config_id,
                **params,
                **metrics,
                "fit_seconds": round(fit_seconds, 3),
                "selection_split": "validation",
                "selection_rule": "MAE asc, RMSE asc, R2 desc",
            }
        )

    validation_df = pd.DataFrame(rows)
    validation_df = validation_df.sort_values(
        ["MAE", "RMSE", "R2"],
        ascending=[True, True, False],
        kind="mergesort",
    ).reset_index(drop=True)
    validation_df.insert(2, "validation_rank", np.arange(1, len(validation_df) + 1))
    return validation_df


def selected_params_from_validation(validation_df: pd.DataFrame) -> dict[str, Any]:
    best = validation_df.iloc[0]
    return {
        key: best[key].item() if hasattr(best[key], "item") else best[key]
        for key in GRID_KEYS
    }


def evaluate_selected_on_test(
    selected_params: dict[str, Any],
    validation_df: pd.DataFrame,
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    seed: int,
    run_mode: str,
) -> pd.DataFrame:
    fit_start = time.perf_counter()
    model = build_model(selected_params, seed)
    model.fit(X_train, y_train)
    test_pred = model.predict(X_test)
    metrics = compute_metrics(y_test, test_pred)
    fit_seconds = time.perf_counter() - fit_start

    best_validation = validation_df.iloc[0]
    evidence_status = (
        "full-run manuscript candidate" if run_mode == "full" else "code-validation only"
    )

    return pd.DataFrame(
        [
            {
                "run_mode": run_mode,
                "evidence_status": evidence_status,
                "model": "XGBoost",
                "selected_config_id": int(best_validation["config_id"]),
                **selected_params,
                "validation_MAE": float(best_validation["MAE"]),
                "validation_RMSE": float(best_validation["RMSE"]),
                "validation_R2": float(best_validation["R2"]),
                **metrics,
                "test_evaluations": 1,
                "test_fit_seconds": round(fit_seconds, 3),
                "selection_split": "validation",
                "selection_rule": "MAE asc, RMSE asc, R2 desc",
            }
        ]
    )


def build_manifest(
    run_mode: str,
    args: argparse.Namespace,
    train_cap: int | None,
    val_cap: int | None,
    test_cap: int | None,
    configs: list[dict[str, Any]],
    numeric_features: list[str],
    non_numeric_excluded: list[str],
    row_counts: dict[str, int],
    output_files: dict[str, Path],
    elapsed_seconds: float,
) -> pd.DataFrame:
    evidence_status = (
        "full-run manuscript candidate" if run_mode == "full" else "code-validation only"
    )
    rows = {
        "script": "scripts/tune_xgboost_small_grid.py",
        "run_mode": run_mode,
        "evidence_status": evidence_status,
        "seed": args.seed,
        "train_path": TRAIN_PATH.relative_to(ROOT),
        "val_path": VAL_PATH.relative_to(ROOT),
        "test_path": TEST_PATH.relative_to(ROOT),
        "target_column": TARGET_COLUMN,
        "excluded_columns": ", ".join(
            [
                TARGET_COLUMN,
                PARK_ID_COLUMN,
                TIMESTAMP_COLUMN,
                TEST_FLAG_COLUMN,
                BASELINE_COLUMN,
            ]
        ),
        "feature_contract": "NB07 blocked columns plus train-inferred numeric columns only; no turbine encoding",
        "numeric_feature_count": len(numeric_features),
        "non_numeric_excluded": ", ".join(non_numeric_excluded) or "none",
        "full_grid_combinations": len(build_parameter_grid()),
        "evaluated_configurations": len(configs),
        "selection_rule": "validation MAE asc, validation RMSE asc, validation R2 desc",
        "test_policy": "selected configuration evaluated once on test split",
        "baseline_metrics_policy": "data/processed/baseline_metrics.csv is not overwritten",
        "model_artifact_policy": "no model binaries or checkpoints are written",
        "train_rows_used": row_counts["train"],
        "val_rows_used": row_counts["val"],
        "test_rows_used": row_counts["test"],
        "max_train_rows": train_cap if train_cap is not None else "none",
        "max_val_rows": val_cap if val_cap is not None else "none",
        "max_test_rows": test_cap if test_cap is not None else "none",
        "validation_output": output_files["validation"].relative_to(ROOT),
        "selected_test_output": output_files["selected_test"].relative_to(ROOT),
        "manifest_output": output_files["manifest"].relative_to(ROOT),
        "elapsed_seconds": round(elapsed_seconds, 3),
    }
    return pd.DataFrame(
        [
            {"run_mode": run_mode, "field": key, "value": value}
            for key, value in rows.items()
        ]
    )


def main() -> None:
    args = parse_args()
    run_start = time.perf_counter()

    for label, path in [
        ("train split", TRAIN_PATH),
        ("validation split", VAL_PATH),
        ("test split", TEST_PATH),
    ]:
        require_existing_file(path, label)

    train_cap, val_cap, test_cap = resolve_row_caps(args)
    run_mode = infer_run_mode(args, train_cap, val_cap, test_cap)
    configs = select_configs_for_run(args)
    output_files = output_paths(run_mode)

    headers = {
        "train": read_header(TRAIN_PATH),
        "val": read_header(VAL_PATH),
        "test": read_header(TEST_PATH),
    }
    validate_required_columns(headers)

    candidates = candidate_feature_columns(headers["train"])
    train_df, numeric_features, non_numeric_excluded = load_train_split(
        candidates,
        train_cap,
    )
    validate_feature_availability(headers, numeric_features)

    split_columns = [TARGET_COLUMN, *numeric_features]
    val_df = read_split(VAL_PATH, split_columns, val_cap)

    X_train, y_train = split_xy(train_df, numeric_features, "train")
    X_val, y_val = split_xy(val_df, numeric_features, "validation")

    validation_df = tune_on_validation(
        configs,
        X_train,
        y_train,
        X_val,
        y_val,
        seed=args.seed,
        run_mode=run_mode,
    )
    selected_params = selected_params_from_validation(validation_df)

    test_df = read_split(TEST_PATH, split_columns, test_cap)
    X_test, y_test = split_xy(test_df, numeric_features, "test")
    selected_test_df = evaluate_selected_on_test(
        selected_params,
        validation_df,
        X_train,
        y_train,
        X_test,
        y_test,
        seed=args.seed,
        run_mode=run_mode,
    )

    elapsed_seconds = time.perf_counter() - run_start
    row_counts = {
        "train": len(train_df),
        "val": len(val_df),
        "test": len(test_df),
    }
    manifest_df = build_manifest(
        run_mode,
        args,
        train_cap,
        val_cap,
        test_cap,
        configs,
        numeric_features,
        non_numeric_excluded,
        row_counts,
        output_files,
        elapsed_seconds,
    )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    validation_df.to_csv(output_files["validation"], index=False)
    selected_test_df.to_csv(output_files["selected_test"], index=False)
    manifest_df.to_csv(output_files["manifest"], index=False)

    print("XGBoost small-grid tuning audit completed.")
    print(f"Run mode: {run_mode}")
    if run_mode != "full":
        print("Evidence status: code-validation only; not manuscript evidence.")
    print(f"Evaluated configurations: {len(configs)}")
    print(f"Numeric learned features: {len(numeric_features)}")
    print(f"Validation output: {output_files['validation']}")
    print(f"Selected test output: {output_files['selected_test']}")
    print(f"Run manifest: {output_files['manifest']}")


if __name__ == "__main__":
    main()
