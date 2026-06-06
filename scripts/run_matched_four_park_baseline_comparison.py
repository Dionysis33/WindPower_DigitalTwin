from __future__ import annotations

"""Matched four-park baseline comparison runner.

This script is for local matched-subset evidence only. It evaluates the
implemented tabular baseline family on the same four parks used by the neural
subset audits and writes local diagnostics outputs under data/processed.

It never updates data/processed/baseline_metrics.csv, never writes model
checkpoints or binaries, and should not be interpreted as replacing the
canonical full-dataset benchmark.
"""

import argparse
import copy
import json
import random
import sys
import time
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Repository path/config resolution
# ---------------------------------------------------------------------------
# Resolve paths through src.config when available, while keeping this script
# runnable as a standalone local audit utility from the repository checkout.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    from src import config as cfg
except ImportError:
    cfg = None


def cfg_value(name: str, fallback):
    """Return a project config value, falling back for standalone execution."""
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

DEFAULT_OUTPUT_DIR = (
    DATA_PROCESSED / "diagnostics" / "matched_four_park_baseline"
)

# ---------------------------------------------------------------------------
# Fixed four-park evidence settings
# ---------------------------------------------------------------------------
# These settings define the matched local evidence space. They must remain
# separate from the canonical full-dataset benchmark in baseline_metrics.csv.
SELECTED_PARKS = ["00183", "00198", "00303", "00427"]
EXPECTED_ROW_COUNTS = {
    "train": 31_276,
    "validation": 2_880,
    "test": 17_180,
}
EXPECTED_NUMERIC_FEATURES = 41

CHUNKSIZE = 100_000
BENCHMARK_COLUMNS = ["Model", "MAE", "RMSE", "R2"]

BLOCKED_FEATURE_COLUMNS = {
    TARGET_COLUMN,
    PARK_ID_COLUMN,
    TIMESTAMP_COLUMN,
    TEST_FLAG_COLUMN,
    BASELINE_COLUMN,
    "turbine",
}

RF_CONFIGS: list[dict[str, Any]] = [
    {"n_estimators": 50, "max_depth": 8, "min_samples_leaf": 1, "max_features": "sqrt"},
    {"n_estimators": 100, "max_depth": 10, "min_samples_leaf": 1, "max_features": "sqrt"},
    {"n_estimators": 100, "max_depth": 12, "min_samples_leaf": 2, "max_features": "sqrt"},
]

XGB_CONFIGS: list[dict[str, Any]] = [
    {
        "n_estimators": 300,
        "max_depth": 6,
        "learning_rate": 0.05,
        "subsample": 0.8,
        "colsample_bytree": 0.8,
    },
    {
        "n_estimators": 500,
        "max_depth": 6,
        "learning_rate": 0.05,
        "subsample": 0.8,
        "colsample_bytree": 0.8,
    },
    {
        "n_estimators": 500,
        "max_depth": 8,
        "learning_rate": 0.05,
        "subsample": 0.8,
        "colsample_bytree": 0.8,
    },
]

MLP_CONFIGS: list[dict[str, Any]] = [
    {"hidden_dims": (64, 32), "dropout": 0.0, "lr": 1e-3, "weight_decay": 1e-5},
    {"hidden_dims": (128, 64), "dropout": 0.0, "lr": 1e-3, "weight_decay": 1e-5},
    {"hidden_dims": (128, 64), "dropout": 0.1, "lr": 5e-4, "weight_decay": 1e-4},
]

MLP_MAX_EPOCHS = 30
MLP_PATIENCE = 5
MLP_TRAIN_BATCH_SIZE = 4096
MLP_EVAL_BATCH_SIZE = 8192


# ---------------------------------------------------------------------------
# CLI entrypoint configuration
# ---------------------------------------------------------------------------
def parse_args() -> argparse.Namespace:
    """Parse CLI flags without reading data, fitting models, or writing files."""
    parser = argparse.ArgumentParser(
        description=(
            "Run local matched four-park baseline metrics for the same parks "
            "used by the neural subset audits. This does not update "
            "data/processed/baseline_metrics.csv."
        )
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=(
            "Directory for local generated CSVs. Defaults to "
            "data/processed/diagnostics/matched_four_park_baseline/."
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help=(
            "Load and validate the selected four-park subset, then print the "
            "model/output plan without fitting models or writing CSVs."
        ),
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=DEFAULT_SEED,
        help=f"Random seed for stochastic models. Default: {DEFAULT_SEED}.",
    )
    return parser.parse_args()


def resolve_output_dir(path: Path) -> Path:
    """Resolve the local diagnostics output directory without creating it."""
    if path.is_absolute():
        return path
    return ROOT / path


def output_paths(output_dir: Path) -> dict[str, Path]:
    """Format the three local CSV output paths; this does not write files."""
    return {
        "validation": output_dir / "matched_four_park_baseline_validation_metrics.csv",
        "selected_test": output_dir / "matched_four_park_baseline_selected_test_metrics.csv",
        "manifest": output_dir / "matched_four_park_baseline_run_manifest.csv",
    }


def require_existing_file(path: Path, label: str) -> None:
    """Validate that a required input artifact exists before reading it."""
    if not path.exists():
        raise FileNotFoundError(f"Missing required {label}: {path}")
    if not path.is_file():
        raise FileNotFoundError(f"Required {label} is not a file: {path}")


def normalize_park_id(series: pd.Series) -> pd.Series:
    """Normalize park identifiers to the zero-padded string contract."""
    return series.astype(str).str.replace(".0", "", regex=False).str.zfill(5)


def read_header(path: Path) -> pd.Index:
    """Read only a CSV header for schema validation; no data rows are loaded."""
    return pd.read_csv(path, nrows=0).columns


# ---------------------------------------------------------------------------
# Safety/leakage checks
# ---------------------------------------------------------------------------
def validate_headers(headers: dict[str, pd.Index]) -> None:
    """Check required split columns and identical schemas across splits."""
    required = {
        TARGET_COLUMN,
        PARK_ID_COLUMN,
        TIMESTAMP_COLUMN,
        TEST_FLAG_COLUMN,
        BASELINE_COLUMN,
    }

    for split_name, columns in headers.items():
        missing = sorted(required - set(columns))
        if missing:
            raise KeyError(
                f"Missing required columns from {split_name} split: "
                + ", ".join(missing)
            )

    train_columns = list(headers["train"])
    for split_name in ["validation", "test"]:
        if train_columns != list(headers[split_name]):
            raise ValueError(
                "Canonical split schemas are not identical. "
                f"Mismatch found in {split_name}."
            )


def read_filtered_split(
    path: Path,
    split_name: str,
    selected_parks: list[str],
) -> pd.DataFrame:
    """Read one split and filter it to the fixed selected parks.

    This function reads processed split data, normalizes park IDs, parses
    timestamps, and returns deterministic row order. It does not fit models or
    write outputs.
    """
    selected = set(selected_parks)
    frames: list[pd.DataFrame] = []

    for chunk in pd.read_csv(
        path,
        dtype={PARK_ID_COLUMN: "string"},
        chunksize=CHUNKSIZE,
    ):
        chunk[PARK_ID_COLUMN] = normalize_park_id(chunk[PARK_ID_COLUMN])
        filtered = chunk.loc[chunk[PARK_ID_COLUMN].isin(selected)].copy()
        if not filtered.empty:
            frames.append(filtered)

    if not frames:
        raise ValueError(f"No selected-park rows found in {split_name} split.")

    df = pd.concat(frames, ignore_index=True)
    df[PARK_ID_COLUMN] = normalize_park_id(df[PARK_ID_COLUMN])
    df[TIMESTAMP_COLUMN] = pd.to_datetime(df[TIMESTAMP_COLUMN], errors="raise")
    return (
        df.sort_values([PARK_ID_COLUMN, TIMESTAMP_COLUMN], kind="mergesort")
        .reset_index(drop=True)
        .copy()
    )


def validate_selected_split(
    df: pd.DataFrame,
    split_name: str,
    expected_flag_values: set[int],
) -> None:
    """Validate the selected split support and temporal backbone.

    The checks preserve the existing temporal split contract: exact row counts,
    exact selected parks, no duplicate `(park_id, timestamp)` keys, expected
    `test_flag` values, and monotonic timestamps within each park.
    """
    if df.empty:
        raise ValueError(f"The selected {split_name} split is empty.")

    expected_rows = EXPECTED_ROW_COUNTS[split_name]
    if len(df) != expected_rows:
        raise ValueError(
            f"Unexpected {split_name} row count. "
            f"Expected={expected_rows:,}, observed={len(df):,}."
        )

    observed_parks = sorted(df[PARK_ID_COLUMN].astype(str).unique().tolist())
    if observed_parks != SELECTED_PARKS:
        raise ValueError(
            f"Unexpected selected parks in {split_name}. "
            f"Expected={SELECTED_PARKS}, observed={observed_parks}."
        )

    duplicate_count = int(
        df.duplicated(subset=[PARK_ID_COLUMN, TIMESTAMP_COLUMN]).sum()
    )
    if duplicate_count:
        raise ValueError(
            f"Found {duplicate_count} duplicate (park_id, timestamp) rows "
            f"in {split_name}."
        )

    core_columns = [PARK_ID_COLUMN, TIMESTAMP_COLUMN, TEST_FLAG_COLUMN, TARGET_COLUMN]
    core_nulls = int(df[core_columns].isnull().sum().sum())
    if core_nulls:
        raise ValueError(f"Found {core_nulls} null core values in {split_name}.")

    observed_flags = set(df[TEST_FLAG_COLUMN].dropna().astype(int).unique().tolist())
    if observed_flags != expected_flag_values:
        raise ValueError(
            f"Unexpected {TEST_FLAG_COLUMN} values in {split_name}. "
            f"Expected={expected_flag_values}, observed={observed_flags}."
        )

    if not df[PARK_ID_COLUMN].astype(str).str.len().eq(5).all():
        raise ValueError(f"{split_name} park_id values are not zero-padded strings.")

    monotonic_ok = (
        df.groupby(PARK_ID_COLUMN, sort=False)[TIMESTAMP_COLUMN]
        .apply(lambda values: values.is_monotonic_increasing)
        .all()
    )
    if not monotonic_ok:
        raise ValueError(f"{split_name} timestamps are not monotonic within park.")


def validate_no_cross_split_overlap(split_frames: dict[str, pd.DataFrame]) -> None:
    """Ensure train, validation, and test have disjoint park-time keys."""
    keys = {
        split_name: df[[PARK_ID_COLUMN, TIMESTAMP_COLUMN]].drop_duplicates()
        for split_name, df in split_frames.items()
    }
    pairs = [
        ("train", "validation"),
        ("train", "test"),
        ("validation", "test"),
    ]
    for left_name, right_name in pairs:
        overlap = keys[left_name].merge(
            keys[right_name],
            on=[PARK_ID_COLUMN, TIMESTAMP_COLUMN],
            how="inner",
        )
        if not overlap.empty:
            raise ValueError(
                f"Found {len(overlap):,} overlapping keys between "
                f"{left_name} and {right_name}."
            )


# ---------------------------------------------------------------------------
# Feature contract
# ---------------------------------------------------------------------------
def infer_numeric_features(train_df: pd.DataFrame) -> tuple[list[str], list[str]]:
    """Infer learned numeric feature columns from train only.

    Target, identifiers, split flags, baseline prediction, and `turbine` are
    excluded before numeric feature inference to avoid leakage and preserve the
    NB06/NB07 feature contract.
    """
    candidate_features = [
        column for column in train_df.columns if column not in BLOCKED_FEATURE_COLUMNS
    ]
    numeric_features = [
        column
        for column in candidate_features
        if pd.api.types.is_numeric_dtype(train_df[column])
    ]
    non_numeric_excluded = sorted(set(candidate_features) - set(numeric_features))

    if not numeric_features:
        raise ValueError("No numeric learned feature columns were found.")

    if len(numeric_features) != EXPECTED_NUMERIC_FEATURES:
        raise ValueError(
            f"Unexpected numeric feature count. "
            f"Expected={EXPECTED_NUMERIC_FEATURES}, observed={len(numeric_features)}."
        )

    illegal_features = sorted(set(numeric_features) & BLOCKED_FEATURE_COLUMNS)
    if illegal_features:
        raise ValueError(f"Blocked columns entered feature space: {illegal_features}")

    return numeric_features, non_numeric_excluded


def validate_feature_contract(
    split_frames: dict[str, pd.DataFrame],
    numeric_features: list[str],
) -> None:
    """Validate train-inferred numeric features across all three splits.

    This checks availability, numeric dtype, nulls, and finite values without
    using validation or test statistics to choose features.
    """
    required = {TARGET_COLUMN, *numeric_features}
    for split_name, df in split_frames.items():
        missing = sorted(required - set(df.columns))
        if missing:
            raise KeyError(
                f"Missing selected columns from {split_name}: " + ", ".join(missing)
            )

        non_numeric = [
            column
            for column in numeric_features
            if not pd.api.types.is_numeric_dtype(df[column])
        ]
        if non_numeric:
            raise TypeError(
                f"Non-numeric learned features in {split_name}: {non_numeric}"
            )

        selected_columns = [TARGET_COLUMN, *numeric_features]
        null_count = int(df[selected_columns].isnull().sum().sum())
        if null_count:
            raise ValueError(
                f"Found {null_count} null target/feature values in {split_name}."
            )

        values = df[selected_columns].to_numpy(dtype=np.float64)
        if not np.isfinite(values).all():
            raise ValueError(f"Found non-finite target/feature values in {split_name}.")


def load_and_validate_subset() -> tuple[dict[str, pd.DataFrame], list[str], list[str]]:
    """Load processed splits and run all non-model validation checks.

    The returned feature list is inferred from train only. No models are fit and
    no output files are written by this function.
    """
    for label, path in [
        ("train split", TRAIN_PATH),
        ("validation split", VAL_PATH),
        ("test split", TEST_PATH),
    ]:
        require_existing_file(path, label)

    headers = {
        "train": read_header(TRAIN_PATH),
        "validation": read_header(VAL_PATH),
        "test": read_header(TEST_PATH),
    }
    validate_headers(headers)

    split_frames = {
        "train": read_filtered_split(TRAIN_PATH, "train", SELECTED_PARKS),
        "validation": read_filtered_split(VAL_PATH, "validation", SELECTED_PARKS),
        "test": read_filtered_split(TEST_PATH, "test", SELECTED_PARKS),
    }

    validate_selected_split(split_frames["train"], "train", {0})
    validate_selected_split(split_frames["validation"], "validation", {0})
    validate_selected_split(split_frames["test"], "test", {1})
    validate_no_cross_split_overlap(split_frames)

    numeric_features, non_numeric_excluded = infer_numeric_features(
        split_frames["train"]
    )
    validate_feature_contract(split_frames, numeric_features)
    return split_frames, numeric_features, non_numeric_excluded


def split_xy(
    df: pd.DataFrame,
    numeric_features: list[str],
) -> tuple[pd.DataFrame, pd.Series]:
    """Split a validated dataframe into feature matrix and target vector."""
    return df[numeric_features].copy(), df[TARGET_COLUMN].copy()


def compute_metrics(y_true: pd.Series | np.ndarray, y_pred: np.ndarray) -> dict[str, float]:
    """Compute the shared MAE, RMSE, and R2 metric set."""
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

    y_true_array = np.asarray(y_true, dtype=np.float64)
    y_pred_array = np.asarray(y_pred, dtype=np.float64)
    mse = mean_squared_error(y_true_array, y_pred_array)
    return {
        "MAE": float(mean_absolute_error(y_true_array, y_pred_array)),
        "RMSE": float(np.sqrt(mse)),
        "R2": float(r2_score(y_true_array, y_pred_array)),
    }


def config_to_json(config: dict[str, Any] | None) -> str:
    """Format a model configuration for CSV output without changing it."""
    if config is None:
        return "fixed"
    return json.dumps(config, sort_keys=True)


# ---------------------------------------------------------------------------
# Persistence baseline logic
# ---------------------------------------------------------------------------
def build_seeded_persistence(
    previous_split_df: pd.DataFrame,
    current_split_df: pd.DataFrame,
    pred_col: str = "Persistence_Pred",
) -> pd.DataFrame:
    """Build full-support persistence predictions for one evaluation split.

    The first row for each park is seeded from the previous split's last target
    value, matching NB06 behavior and avoiding row trimming in validation/test.
    """
    prev_sorted = (
        previous_split_df.sort_values(
            [PARK_ID_COLUMN, TIMESTAMP_COLUMN],
            kind="mergesort",
        )
        .reset_index(drop=True)
        .copy()
    )
    curr_sorted = (
        current_split_df.sort_values(
            [PARK_ID_COLUMN, TIMESTAMP_COLUMN],
            kind="mergesort",
        )
        .reset_index(drop=True)
        .copy()
    )

    previous_last_actual = prev_sorted.groupby(PARK_ID_COLUMN, sort=False)[
        TARGET_COLUMN
    ].last()
    curr_sorted[pred_col] = curr_sorted.groupby(PARK_ID_COLUMN, sort=False)[
        TARGET_COLUMN
    ].shift(1)

    first_row_mask = curr_sorted.groupby(PARK_ID_COLUMN, sort=False).cumcount().eq(0)
    curr_sorted.loc[first_row_mask, pred_col] = curr_sorted.loc[
        first_row_mask, PARK_ID_COLUMN
    ].map(previous_last_actual)

    if curr_sorted[pred_col].isnull().any():
        missing = curr_sorted.loc[curr_sorted[pred_col].isnull(), PARK_ID_COLUMN]
        raise ValueError(
            "Persistence produced null predictions for parks: "
            + ", ".join(sorted(missing.astype(str).unique().tolist()))
        )

    if not np.isfinite(curr_sorted[pred_col].to_numpy(dtype=np.float64)).all():
        raise ValueError("Persistence produced non-finite predictions.")

    return curr_sorted


def validation_row(
    model: str,
    model_family: str,
    config_id: str,
    config: dict[str, Any] | None,
    metrics: dict[str, float],
    selection_rule: str,
) -> dict[str, Any]:
    """Format one validation metrics row for local diagnostics CSV output."""
    return {
        "run_mode": "matched_four_park",
        "evidence_status": "local matched-subset evidence; not benchmark replacement",
        "model": model,
        "model_family": model_family,
        "config_id": config_id,
        "config": config_to_json(config),
        **metrics,
        "selection_split": "validation",
        "selection_rule": selection_rule,
    }


def selected_test_row(
    model: str,
    model_family: str,
    selected_config_id: str,
    selected_config: dict[str, Any] | None,
    validation_metrics: dict[str, float],
    test_metrics: dict[str, float],
    numeric_feature_count: int,
    row_counts: dict[str, int],
    selection_rule: str,
    comparability_note: str,
) -> dict[str, Any]:
    """Format one selected-test row after final one-time test evaluation."""
    return {
        "run_mode": "matched_four_park",
        "evidence_status": "local matched-subset evidence; not benchmark replacement",
        "model": model,
        "model_family": model_family,
        "selected_config_id": selected_config_id,
        "selected_config": config_to_json(selected_config),
        "selected_parks": ";".join(SELECTED_PARKS),
        "n_parks": len(SELECTED_PARKS),
        "n_numeric_features": numeric_feature_count,
        "train_rows_used": row_counts["train"],
        "val_rows_used": row_counts["validation"],
        "test_rows_used": row_counts["test"],
        "validation_MAE": validation_metrics["MAE"],
        "validation_RMSE": validation_metrics["RMSE"],
        "validation_R2": validation_metrics["R2"],
        "MAE": test_metrics["MAE"],
        "RMSE": test_metrics["RMSE"],
        "R2": test_metrics["R2"],
        "test_evaluations": 1,
        "selection_split": "validation",
        "selection_rule": selection_rule,
        "evaluation_granularity": "row-level four-park tabular subset",
        "comparability_note": comparability_note,
    }


def select_best_validation_row(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """Select a validation row by the NB07 metric ordering."""
    return (
        pd.DataFrame(rows)
        .sort_values(["MAE", "RMSE", "R2"], ascending=[True, True, False], kind="mergesort")
        .iloc[0]
        .to_dict()
    )


def evaluate_persistence(
    split_frames: dict[str, pd.DataFrame],
    numeric_features: list[str],
    row_counts: dict[str, int],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Evaluate the fixed persistence baseline.

    This fits no learned model. It reports validation metrics and one final
    test evaluation using the seeded persistence logic.
    """
    val_eval = build_seeded_persistence(split_frames["train"], split_frames["validation"])
    test_eval = build_seeded_persistence(split_frames["validation"], split_frames["test"])

    val_metrics = compute_metrics(
        val_eval[TARGET_COLUMN],
        val_eval["Persistence_Pred"].to_numpy(dtype=np.float64),
    )
    test_metrics = compute_metrics(
        test_eval[TARGET_COLUMN],
        test_eval["Persistence_Pred"].to_numpy(dtype=np.float64),
    )
    selection_rule = "fixed baseline; no model selection"
    validation_rows = [
        validation_row(
            "Persistence",
            "naive temporal baseline",
            "fixed",
            None,
            val_metrics,
            selection_rule,
        )
    ]
    test_row = selected_test_row(
        "Persistence",
        "naive temporal baseline",
        "fixed",
        None,
        val_metrics,
        test_metrics,
        len(numeric_features),
        row_counts,
        selection_rule,
        "Matched row-level four-park baseline evidence; not a canonical benchmark row.",
    )
    return validation_rows, test_row


# ---------------------------------------------------------------------------
# Learned baseline evaluation
# ---------------------------------------------------------------------------
def evaluate_linear_regression(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_val: pd.DataFrame,
    y_val: pd.Series,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    numeric_features: list[str],
    row_counts: dict[str, int],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Fit and evaluate the fixed Linear Regression baseline.

    The model is fit on the matched train subset, reported on validation, and
    evaluated once on the matched test subset.
    """
    from sklearn.linear_model import LinearRegression

    model = LinearRegression()
    model.fit(X_train, y_train)
    val_pred = model.predict(X_val)
    test_pred = model.predict(X_test)

    val_metrics = compute_metrics(y_val, val_pred)
    test_metrics = compute_metrics(y_test, test_pred)
    selection_rule = "fixed baseline; no model selection"
    validation_rows = [
        validation_row(
            "Linear Regression",
            "linear tabular baseline",
            "fixed",
            None,
            val_metrics,
            selection_rule,
        )
    ]
    test_row = selected_test_row(
        "Linear Regression",
        "linear tabular baseline",
        "fixed",
        None,
        val_metrics,
        test_metrics,
        len(numeric_features),
        row_counts,
        selection_rule,
        "Matched row-level four-park baseline evidence; not a canonical benchmark row.",
    )
    return validation_rows, test_row


def evaluate_random_forest(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_val: pd.DataFrame,
    y_val: pd.Series,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    numeric_features: list[str],
    row_counts: dict[str, int],
    seed: int,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Evaluate Random Forest with validation-only config selection.

    Each candidate is fit on train and scored on validation. The selected
    configuration is refit on train and evaluated once on test.
    """
    from sklearn.ensemble import RandomForestRegressor

    selection_rule = "validation MAE asc, validation RMSE asc, validation R2 desc"
    rows: list[dict[str, Any]] = []
    for config_id, config in enumerate(RF_CONFIGS, start=1):
        model = RandomForestRegressor(random_state=seed, n_jobs=-1, **config)
        model.fit(X_train, y_train)
        metrics = compute_metrics(y_val, model.predict(X_val))
        rows.append(
            validation_row(
                "Random Forest",
                "tree ensemble tabular baseline",
                str(config_id),
                config,
                metrics,
                selection_rule,
            )
        )

    best = select_best_validation_row(rows)
    selected_config_id = str(best["config_id"])
    selected_config = RF_CONFIGS[int(selected_config_id) - 1]
    model = RandomForestRegressor(random_state=seed, n_jobs=-1, **selected_config)
    model.fit(X_train, y_train)
    test_metrics = compute_metrics(y_test, model.predict(X_test))
    validation_metrics = {
        "MAE": float(best["MAE"]),
        "RMSE": float(best["RMSE"]),
        "R2": float(best["R2"]),
    }
    test_row = selected_test_row(
        "Random Forest",
        "tree ensemble tabular baseline",
        selected_config_id,
        selected_config,
        validation_metrics,
        test_metrics,
        len(numeric_features),
        row_counts,
        selection_rule,
        "Matched row-level four-park baseline evidence; not a canonical benchmark row.",
    )
    return rows, test_row


def evaluate_xgboost(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_val: pd.DataFrame,
    y_val: pd.Series,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    numeric_features: list[str],
    row_counts: dict[str, int],
    seed: int,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Evaluate XGBoost with validation-only config selection.

    The canonical benchmark is not read or updated; this function only returns
    local validation rows and the one-time selected test row.
    """
    from xgboost import XGBRegressor

    selection_rule = "validation MAE asc, validation RMSE asc, validation R2 desc"
    rows: list[dict[str, Any]] = []
    for config_id, config in enumerate(XGB_CONFIGS, start=1):
        model = XGBRegressor(
            objective="reg:squarederror",
            random_state=seed,
            n_jobs=-1,
            tree_method="hist",
            **config,
        )
        model.fit(X_train, y_train)
        metrics = compute_metrics(y_val, model.predict(X_val))
        rows.append(
            validation_row(
                "XGBoost",
                "gradient-boosted tree tabular baseline",
                str(config_id),
                config,
                metrics,
                selection_rule,
            )
        )

    best = select_best_validation_row(rows)
    selected_config_id = str(best["config_id"])
    selected_config = XGB_CONFIGS[int(selected_config_id) - 1]
    model = XGBRegressor(
        objective="reg:squarederror",
        random_state=seed,
        n_jobs=-1,
        tree_method="hist",
        **selected_config,
    )
    model.fit(X_train, y_train)
    test_metrics = compute_metrics(y_test, model.predict(X_test))
    validation_metrics = {
        "MAE": float(best["MAE"]),
        "RMSE": float(best["RMSE"]),
        "R2": float(best["R2"]),
    }
    test_row = selected_test_row(
        "XGBoost",
        "gradient-boosted tree tabular baseline",
        selected_config_id,
        selected_config,
        validation_metrics,
        test_metrics,
        len(numeric_features),
        row_counts,
        selection_rule,
        "Matched row-level four-park baseline evidence; not a canonical benchmark row.",
    )
    return rows, test_row


# ---------------------------------------------------------------------------
# MLP training/selection
# ---------------------------------------------------------------------------
def set_mlp_reproducibility(seed: int) -> None:
    """Set PyTorch and NumPy seeds for reproducible local MLP fitting."""
    import torch

    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    if hasattr(torch.backends, "cudnn"):
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False


def build_mlp_model(input_dim: int, hidden_dims: tuple[int, ...], dropout: float):
    """Construct the NB07-style tabular MLP architecture."""
    import torch.nn as nn

    layers: list[Any] = []
    previous_dim = input_dim
    for hidden_dim in hidden_dims:
        layers.extend([nn.Linear(previous_dim, hidden_dim), nn.ReLU()])
        if dropout > 0:
            layers.append(nn.Dropout(dropout))
        previous_dim = hidden_dim
    layers.append(nn.Linear(previous_dim, 1))
    return nn.Sequential(*layers)


def make_loader(
    X: np.ndarray,
    y: np.ndarray,
    batch_size: int,
    shuffle: bool,
    seed: int,
):
    """Create a PyTorch DataLoader without writing artifacts."""
    import torch
    from torch.utils.data import DataLoader, TensorDataset

    dataset = TensorDataset(
        torch.from_numpy(X.astype(np.float32)),
        torch.from_numpy(y.astype(np.float32).reshape(-1, 1)),
    )
    generator = None
    if shuffle:
        generator = torch.Generator()
        generator.manual_seed(seed)
    return DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        generator=generator,
    )


def run_mlp_epoch(model, loader, criterion, device, optimizer=None) -> float:
    """Run one MLP train or evaluation epoch and return average MSE loss."""
    is_train = optimizer is not None
    model.train(mode=is_train)
    total_loss = 0.0
    total_count = 0

    for xb, yb in loader:
        xb = xb.to(device)
        yb = yb.to(device)
        if is_train:
            optimizer.zero_grad()
        pred = model(xb)
        loss = criterion(pred, yb)
        if is_train:
            loss.backward()
            optimizer.step()
        batch_size = xb.shape[0]
        total_loss += float(loss.detach().cpu().item()) * batch_size
        total_count += batch_size

    if total_count == 0:
        raise ValueError("Cannot evaluate an empty MLP loader.")
    return total_loss / total_count


def predict_mlp(model, loader, device) -> np.ndarray:
    """Generate MLP predictions for an existing loader without fitting."""
    import torch

    model.eval()
    preds: list[np.ndarray] = []
    with torch.no_grad():
        for xb, _ in loader:
            xb = xb.to(device)
            pred = model(xb).detach().cpu().numpy().reshape(-1)
            preds.append(pred)
    if not preds:
        raise ValueError("Cannot predict from an empty MLP loader.")
    return np.concatenate(preds).astype(float)


def train_mlp_with_early_stopping(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_val: np.ndarray,
    y_val: np.ndarray,
    config: dict[str, Any],
    seed: int,
) -> tuple[Any, float, int, Any]:
    """Fit one MLP config using validation-only early stopping.

    The selected state is held in memory only. No checkpoint, model binary, or
    canonical benchmark artifact is written.
    """
    import torch
    import torch.nn as nn

    set_mlp_reproducibility(seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    train_loader = make_loader(
        X_train,
        y_train,
        MLP_TRAIN_BATCH_SIZE,
        shuffle=True,
        seed=seed,
    )
    val_loader = make_loader(
        X_val,
        y_val,
        MLP_EVAL_BATCH_SIZE,
        shuffle=False,
        seed=seed,
    )

    model = build_mlp_model(
        X_train.shape[1],
        tuple(config["hidden_dims"]),
        float(config["dropout"]),
    ).to(device)
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=float(config["lr"]),
        weight_decay=float(config["weight_decay"]),
    )

    best_state = None
    best_val_loss = float("inf")
    best_epoch = 0
    epochs_without_improvement = 0

    for epoch in range(1, MLP_MAX_EPOCHS + 1):
        run_mlp_epoch(model, train_loader, criterion, device, optimizer=optimizer)
        val_loss = run_mlp_epoch(model, val_loader, criterion, device, optimizer=None)
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            best_epoch = epoch
            best_state = copy.deepcopy(model.state_dict())
            epochs_without_improvement = 0
        else:
            epochs_without_improvement += 1
        if epochs_without_improvement >= MLP_PATIENCE:
            break

    if best_state is None:
        raise RuntimeError("No best validation state was selected for the MLP.")

    model.load_state_dict(best_state)
    return model, float(best_val_loss), best_epoch, device


def evaluate_mlp(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_val: pd.DataFrame,
    y_val: pd.Series,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    numeric_features: list[str],
    row_counts: dict[str, int],
    seed: int,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Evaluate the NB07-style MLP with train-only scaling.

    StandardScaler is fit only on the matched train subset and applied to
    validation/test. Config/epoch selection uses validation loss, and the final
    selected model is evaluated once on the matched test subset.
    """
    from sklearn.preprocessing import StandardScaler

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train).astype(np.float32)
    X_val_scaled = scaler.transform(X_val).astype(np.float32)
    X_test_scaled = scaler.transform(X_test).astype(np.float32)

    y_train_np = y_train.to_numpy(dtype=np.float32)
    y_val_np = y_val.to_numpy(dtype=np.float32)
    y_test_np = y_test.to_numpy(dtype=np.float32)

    selection_rule = "best epoch/config by validation MSE loss, then MAE/RMSE/R2 reporting"
    rows: list[dict[str, Any]] = []
    trained_metadata: dict[str, tuple[float, int]] = {}
    for config_id, config in enumerate(MLP_CONFIGS, start=1):
        model, best_val_loss, best_epoch, device = train_mlp_with_early_stopping(
            X_train_scaled,
            y_train_np,
            X_val_scaled,
            y_val_np,
            config,
            seed,
        )
        val_loader = make_loader(
            X_val_scaled,
            y_val_np,
            MLP_EVAL_BATCH_SIZE,
            shuffle=False,
            seed=seed,
        )
        val_pred = predict_mlp(model, val_loader, device)
        metrics = compute_metrics(y_val, val_pred)
        row = validation_row(
            "MLP",
            "NB07-style PyTorch tabular neural baseline",
            str(config_id),
            config,
            metrics,
            selection_rule,
        )
        row["best_val_loss_mse"] = best_val_loss
        row["best_epoch"] = best_epoch
        rows.append(row)
        trained_metadata[str(config_id)] = (best_val_loss, best_epoch)

    best = (
        pd.DataFrame(rows)
        .sort_values(
            ["best_val_loss_mse", "MAE", "RMSE", "R2"],
            ascending=[True, True, True, False],
            kind="mergesort",
        )
        .iloc[0]
        .to_dict()
    )
    selected_config_id = str(best["config_id"])
    selected_config = MLP_CONFIGS[int(selected_config_id) - 1]
    model, _, _, device = train_mlp_with_early_stopping(
        X_train_scaled,
        y_train_np,
        X_val_scaled,
        y_val_np,
        selected_config,
        seed,
    )
    test_loader = make_loader(
        X_test_scaled,
        y_test_np,
        MLP_EVAL_BATCH_SIZE,
        shuffle=False,
        seed=seed,
    )
    test_pred = predict_mlp(model, test_loader, device)
    test_metrics = compute_metrics(y_test, test_pred)
    validation_metrics = {
        "MAE": float(best["MAE"]),
        "RMSE": float(best["RMSE"]),
        "R2": float(best["R2"]),
    }
    test_row = selected_test_row(
        "MLP",
        "NB07-style PyTorch tabular neural baseline",
        selected_config_id,
        selected_config,
        validation_metrics,
        test_metrics,
        len(numeric_features),
        row_counts,
        selection_rule,
        "Matched row-level four-park baseline evidence; comparable to row-level neural subset framing, not canonical full benchmark.",
    )
    best_val_loss, best_epoch = trained_metadata[selected_config_id]
    test_row["best_val_loss_mse"] = best_val_loss
    test_row["best_epoch"] = best_epoch
    return rows, test_row


def run_models(
    split_frames: dict[str, pd.DataFrame],
    numeric_features: list[str],
    seed: int,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Run all five baseline families and collect local metrics tables.

    This is the only function that fits models across the full baseline set.
    It returns dataframes for output writing and does not touch canonical
    benchmark artifacts.
    """
    X_train, y_train = split_xy(split_frames["train"], numeric_features)
    X_val, y_val = split_xy(split_frames["validation"], numeric_features)
    X_test, y_test = split_xy(split_frames["test"], numeric_features)
    row_counts = {name: len(df) for name, df in split_frames.items()}

    validation_rows: list[dict[str, Any]] = []
    test_rows: list[dict[str, Any]] = []

    model_runners = [
        lambda: evaluate_persistence(split_frames, numeric_features, row_counts),
        lambda: evaluate_linear_regression(
            X_train,
            y_train,
            X_val,
            y_val,
            X_test,
            y_test,
            numeric_features,
            row_counts,
        ),
        lambda: evaluate_random_forest(
            X_train,
            y_train,
            X_val,
            y_val,
            X_test,
            y_test,
            numeric_features,
            row_counts,
            seed,
        ),
        lambda: evaluate_xgboost(
            X_train,
            y_train,
            X_val,
            y_val,
            X_test,
            y_test,
            numeric_features,
            row_counts,
            seed,
        ),
        lambda: evaluate_mlp(
            X_train,
            y_train,
            X_val,
            y_val,
            X_test,
            y_test,
            numeric_features,
            row_counts,
            seed,
        ),
    ]

    for runner in model_runners:
        rows, test_row = runner()
        validation_rows.extend(rows)
        test_rows.append(test_row)

    validation_df = pd.DataFrame(validation_rows)
    selected_test_df = (
        pd.DataFrame(test_rows)
        .sort_values(["MAE", "RMSE", "R2"], ascending=[True, True, False], kind="mergesort")
        .reset_index(drop=True)
    )
    return validation_df, selected_test_df


# ---------------------------------------------------------------------------
# Output writing and manifest policy
# ---------------------------------------------------------------------------
def build_manifest(
    args: argparse.Namespace,
    output_files: dict[str, Path],
    split_frames: dict[str, pd.DataFrame],
    numeric_features: list[str],
    non_numeric_excluded: list[str],
    elapsed_seconds: float,
    dry_run: bool,
) -> pd.DataFrame:
    """Build the local run manifest dataframe.

    The manifest records selected parks, row counts, feature policy, output
    paths, and the rule that baseline_metrics.csv is not overwritten.
    """
    rows = {
        "script": "scripts/run_matched_four_park_baseline_comparison.py",
        "run_mode": "dry_run" if dry_run else "matched_four_park",
        "evidence_status": "local matched-subset evidence; not benchmark replacement",
        "seed": args.seed,
        "train_path": TRAIN_PATH.relative_to(ROOT),
        "validation_path": VAL_PATH.relative_to(ROOT),
        "test_path": TEST_PATH.relative_to(ROOT),
        "target_column": TARGET_COLUMN,
        "selected_parks": ";".join(SELECTED_PARKS),
        "excluded_columns": ";".join(sorted(BLOCKED_FEATURE_COLUMNS)),
        "feature_contract": "train-inferred numeric learned columns only; no turbine encoding",
        "numeric_feature_count": len(numeric_features),
        "non_numeric_excluded": ";".join(non_numeric_excluded) or "none",
        "train_rows_used": len(split_frames["train"]),
        "validation_rows_used": len(split_frames["validation"]),
        "test_rows_used": len(split_frames["test"]),
        "models": "Persistence;Linear Regression;Random Forest;XGBoost;MLP",
        "selection_policy": "validation-only model/config selection where applicable",
        "test_policy": "final selected models evaluated once on the test subset",
        "baseline_metrics_policy": "data/processed/baseline_metrics.csv is not read for ranking and is not overwritten",
        "model_artifact_policy": "no model binaries or checkpoints are written",
        "validation_output": output_files["validation"].relative_to(ROOT)
        if output_files["validation"].is_relative_to(ROOT)
        else output_files["validation"],
        "selected_test_output": output_files["selected_test"].relative_to(ROOT)
        if output_files["selected_test"].is_relative_to(ROOT)
        else output_files["selected_test"],
        "manifest_output": output_files["manifest"].relative_to(ROOT)
        if output_files["manifest"].is_relative_to(ROOT)
        else output_files["manifest"],
        "elapsed_seconds": round(elapsed_seconds, 3),
    }
    return pd.DataFrame(
        [{"field": field, "value": value} for field, value in rows.items()]
    )


def print_dry_run_report(
    output_files: dict[str, Path],
    split_frames: dict[str, pd.DataFrame],
    numeric_features: list[str],
    non_numeric_excluded: list[str],
) -> None:
    """Print the validated model/output plan without fitting or writing CSVs."""
    print("Dry run complete. No models were fitted and no CSVs were written.")
    print(f"Selected parks: {', '.join(SELECTED_PARKS)}")
    for split_name in ["train", "validation", "test"]:
        print(f"{split_name} rows: {len(split_frames[split_name]):,}")
    print(f"Numeric learned features: {len(numeric_features)}")
    print(
        "Non-numeric excluded features: "
        + (", ".join(non_numeric_excluded) if non_numeric_excluded else "none")
    )
    print("Planned models:")
    print("- Persistence")
    print("- Linear Regression")
    print(f"- Random Forest ({len(RF_CONFIGS)} validation configs)")
    print(f"- XGBoost ({len(XGB_CONFIGS)} validation configs)")
    print(f"- MLP ({len(MLP_CONFIGS)} validation configs)")
    print("Planned outputs:")
    for label, path in output_files.items():
        print(f"- {label}: {path}")


def write_outputs(
    output_files: dict[str, Path],
    validation_df: pd.DataFrame,
    selected_test_df: pd.DataFrame,
    manifest_df: pd.DataFrame,
) -> None:
    """Write local diagnostics CSVs only under the configured output directory."""
    output_files["validation"].parent.mkdir(parents=True, exist_ok=True)
    validation_df.to_csv(output_files["validation"], index=False)
    selected_test_df.to_csv(output_files["selected_test"], index=False)
    manifest_df.to_csv(output_files["manifest"], index=False)


# ---------------------------------------------------------------------------
# CLI entrypoint
# ---------------------------------------------------------------------------
def main() -> None:
    """Coordinate CLI execution, preserving dry-run and local-output boundaries."""
    args = parse_args()
    run_start = time.perf_counter()
    output_dir = resolve_output_dir(args.output_dir)
    files = output_paths(output_dir)

    split_frames, numeric_features, non_numeric_excluded = load_and_validate_subset()

    if args.dry_run:
        print_dry_run_report(files, split_frames, numeric_features, non_numeric_excluded)
        return

    validation_df, selected_test_df = run_models(
        split_frames,
        numeric_features,
        seed=args.seed,
    )
    elapsed_seconds = time.perf_counter() - run_start
    manifest_df = build_manifest(
        args,
        files,
        split_frames,
        numeric_features,
        non_numeric_excluded,
        elapsed_seconds,
        dry_run=False,
    )
    write_outputs(files, validation_df, selected_test_df, manifest_df)

    print("Matched four-park baseline comparison completed.")
    print("Evidence status: local matched-subset evidence; not benchmark replacement.")
    print("data/processed/baseline_metrics.csv was not modified.")
    print(f"Validation metrics: {files['validation']}")
    print(f"Selected test metrics: {files['selected_test']}")
    print(f"Run manifest: {files['manifest']}")


if __name__ == "__main__":
    main()
