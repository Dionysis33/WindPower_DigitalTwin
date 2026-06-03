from __future__ import annotations

import argparse
import copy
import random
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

OUTPUT_DIR = DATA_PROCESSED / "diagnostics" / "nn_subset"

DEFAULT_N_PARKS = 4
DEFAULT_EPOCHS = 30
DEFAULT_BATCH_SIZE = 1024
DEFAULT_PATIENCE = 5

SMOKE_N_PARKS = 1
SMOKE_EPOCHS = 3
SMOKE_BATCH_SIZE = 512
SMOKE_PATIENCE = 2
SMOKE_MAX_TRAIN_ROWS = 5_000
SMOKE_MAX_VAL_ROWS = 1_000
SMOKE_MAX_TEST_ROWS = 1_000

HIDDEN_DIMS = (64, 32)
LEARNING_RATE = 1e-3
WEIGHT_DECAY = 1e-5
CHUNKSIZE = 100_000


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("value must be a positive integer")
    return parsed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run a deterministic PyTorch tabular MLP subset audit on selected "
            "wind parks."
        )
    )
    parser.add_argument(
        "--smoke",
        action="store_true",
        help=(
            "Use a 1-park, low-epoch, capped run for code validation only. "
            "Smoke outputs are not manuscript evidence."
        ),
    )
    parser.add_argument(
        "--n-parks",
        type=positive_int,
        default=None,
        help=f"Number of deterministic common parks to use. Default: {DEFAULT_N_PARKS}.",
    )
    parser.add_argument(
        "--max-train-rows",
        type=positive_int,
        default=None,
        help="Optional deterministic cap on filtered train rows, using file order.",
    )
    parser.add_argument(
        "--max-val-rows",
        type=positive_int,
        default=None,
        help="Optional deterministic cap on filtered validation rows, using file order.",
    )
    parser.add_argument(
        "--max-test-rows",
        type=positive_int,
        default=None,
        help="Optional deterministic cap on filtered test rows, using file order.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=DEFAULT_SEED,
        help=f"Random seed. Default: {DEFAULT_SEED}.",
    )
    parser.add_argument(
        "--epochs",
        type=positive_int,
        default=None,
        help=f"Maximum training epochs. Default: {DEFAULT_EPOCHS}.",
    )
    parser.add_argument(
        "--batch-size",
        type=positive_int,
        default=None,
        help=f"Training batch size. Default: {DEFAULT_BATCH_SIZE}.",
    )
    return parser.parse_args()


def require_existing_file(path: Path, label: str) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Missing required {label}: {path}")
    if not path.is_file():
        raise FileNotFoundError(f"Required {label} is not a file: {path}")


def read_header(path: Path) -> pd.Index:
    return pd.read_csv(path, nrows=0).columns


def read_park_counts(path: Path) -> dict[str, int]:
    counts: dict[str, int] = {}
    for chunk in pd.read_csv(
        path,
        usecols=[PARK_ID_COLUMN],
        dtype={PARK_ID_COLUMN: "string"},
        chunksize=CHUNKSIZE,
    ):
        park_ids = chunk[PARK_ID_COLUMN].dropna().astype(str)
        for park_id, count in park_ids.value_counts(sort=False).items():
            counts[park_id] = counts.get(park_id, 0) + int(count)
    return counts


def select_common_parks(n_parks: int) -> tuple[list[str], int]:
    train_counts = read_park_counts(TRAIN_PATH)
    val_counts = read_park_counts(VAL_PATH)
    test_counts = read_park_counts(TEST_PATH)

    common_parks = set(train_counts) & set(val_counts) & set(test_counts)
    if not common_parks:
        raise ValueError("No common park_id values found across train/val/test.")
    if n_parks > len(common_parks):
        raise ValueError(
            f"Requested {n_parks} parks, but only {len(common_parks)} are common."
        )

    ranked = sorted(
        ((park_id, train_counts[park_id]) for park_id in common_parks),
        key=lambda item: (-item[1], item[0]),
    )
    return [park_id for park_id, _ in ranked[:n_parks]], len(common_parks)


def candidate_feature_columns(train_columns: pd.Index) -> list[str]:
    blocked_columns = {
        TARGET_COLUMN,
        PARK_ID_COLUMN,
        TIMESTAMP_COLUMN,
        TEST_FLAG_COLUMN,
        BASELINE_COLUMN,
        "turbine",
    }
    return [col for col in train_columns if col not in blocked_columns]


def validate_required_columns(headers: dict[str, pd.Index]) -> None:
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


def validate_feature_availability(
    headers: dict[str, pd.Index],
    numeric_features: list[str],
) -> None:
    required_columns = {TARGET_COLUMN, PARK_ID_COLUMN, *numeric_features}
    for split_name in ["val", "test"]:
        missing = sorted(required_columns - set(headers[split_name]))
        if missing:
            raise KeyError(
                f"Missing selected columns from {split_name} split: "
                + ", ".join(missing)
            )


def read_filtered_split(
    path: Path,
    columns: list[str],
    selected_parks: list[str],
    max_rows: int | None,
) -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    rows_collected = 0
    selected = set(selected_parks)

    for chunk in pd.read_csv(
        path,
        usecols=columns,
        dtype={PARK_ID_COLUMN: "string"},
        chunksize=CHUNKSIZE,
    ):
        filtered = chunk.loc[chunk[PARK_ID_COLUMN].astype(str).isin(selected)].copy()
        if filtered.empty:
            continue

        if max_rows is not None:
            remaining = max_rows - rows_collected
            if remaining <= 0:
                break
            filtered = filtered.head(remaining)

        frames.append(filtered)
        rows_collected += len(filtered)

        if max_rows is not None and rows_collected >= max_rows:
            break

    if not frames:
        raise ValueError(f"No rows found in {path} for selected parks.")

    return pd.concat(frames, ignore_index=True)


def load_train_subset(
    candidate_columns: list[str],
    selected_parks: list[str],
    max_rows: int | None,
) -> tuple[pd.DataFrame, list[str], list[str]]:
    columns = [PARK_ID_COLUMN, TARGET_COLUMN, *candidate_columns]
    train_df = read_filtered_split(TRAIN_PATH, columns, selected_parks, max_rows)

    numeric_features = [
        col for col in candidate_columns if pd.api.types.is_numeric_dtype(train_df[col])
    ]
    non_numeric_excluded = sorted(set(candidate_columns) - set(numeric_features))

    if not numeric_features:
        raise ValueError("No numeric learned feature columns were found.")

    return train_df, numeric_features, non_numeric_excluded


def validate_no_null_or_nonfinite(
    df: pd.DataFrame,
    numeric_features: list[str],
    split_name: str,
) -> None:
    selected_columns = [TARGET_COLUMN, *numeric_features]
    null_count = int(df[selected_columns].isnull().sum().sum())
    if null_count:
        raise ValueError(
            f"Found {null_count} null values in selected {split_name} columns."
        )

    numeric_values = df[selected_columns].to_numpy(dtype=np.float64)
    if not np.isfinite(numeric_values).all():
        raise ValueError(f"Found non-finite values in selected {split_name} columns.")


def split_xy(
    df: pd.DataFrame,
    numeric_features: list[str],
    split_name: str,
) -> tuple[pd.DataFrame, np.ndarray]:
    validate_no_null_or_nonfinite(df, numeric_features, split_name)
    X = df[numeric_features].copy()
    y = df[TARGET_COLUMN].to_numpy(dtype=np.float32)
    return X, y


def scale_features(
    X_train: pd.DataFrame,
    X_val: pd.DataFrame,
    X_test: pd.DataFrame,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    from sklearn.preprocessing import StandardScaler

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train).astype(np.float32)
    X_val_scaled = scaler.transform(X_val).astype(np.float32)
    X_test_scaled = scaler.transform(X_test).astype(np.float32)
    return X_train_scaled, X_val_scaled, X_test_scaled


def compute_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> dict[str, float]:
    y_true = np.asarray(y_true, dtype=np.float64)
    y_pred = np.asarray(y_pred, dtype=np.float64)
    residual = y_true - y_pred
    mae = float(np.mean(np.abs(residual)))
    rmse = float(np.sqrt(np.mean(residual**2)))
    ss_res = float(np.sum(residual**2))
    ss_tot = float(np.sum((y_true - np.mean(y_true)) ** 2))
    r2 = float(1.0 - ss_res / ss_tot) if ss_tot > 0 else np.nan
    return {"MAE": mae, "RMSE": rmse, "R2": r2}


def set_reproducibility(seed: int) -> None:
    import torch

    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    if hasattr(torch.backends, "cudnn"):
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False


def build_model(input_dim: int) -> Any:
    import torch.nn as nn

    return nn.Sequential(
        nn.Linear(input_dim, HIDDEN_DIMS[0]),
        nn.ReLU(),
        nn.Linear(HIDDEN_DIMS[0], HIDDEN_DIMS[1]),
        nn.ReLU(),
        nn.Linear(HIDDEN_DIMS[1], 1),
    )


def make_loader(
    X: np.ndarray,
    y: np.ndarray,
    batch_size: int,
    shuffle: bool,
    seed: int,
) -> Any:
    import torch
    from torch.utils.data import DataLoader, TensorDataset

    dataset = TensorDataset(
        torch.from_numpy(X),
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


def evaluate_loss(model: Any, loader: Any, criterion: Any, device: Any) -> float:
    import torch

    model.eval()
    total_loss = 0.0
    total_count = 0
    with torch.no_grad():
        for xb, yb in loader:
            xb = xb.to(device)
            yb = yb.to(device)
            pred = model(xb)
            loss = criterion(pred, yb)
            batch_size = xb.shape[0]
            total_loss += float(loss.detach().cpu().item()) * batch_size
            total_count += batch_size
    if total_count == 0:
        raise ValueError("Cannot evaluate an empty loader.")
    return total_loss / total_count


def predict(model: Any, loader: Any, device: Any) -> np.ndarray:
    import torch

    model.eval()
    preds: list[np.ndarray] = []
    with torch.no_grad():
        for xb, _ in loader:
            xb = xb.to(device)
            pred = model(xb).detach().cpu().numpy().reshape(-1)
            preds.append(pred)
    if not preds:
        raise ValueError("Cannot predict from an empty loader.")
    return np.concatenate(preds)


def train_mlp(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_val: np.ndarray,
    y_val: np.ndarray,
    seed: int,
    epochs: int,
    batch_size: int,
    patience: int,
) -> tuple[Any, pd.DataFrame, int, float, str]:
    import torch
    import torch.nn as nn

    set_reproducibility(seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    train_loader = make_loader(X_train, y_train, batch_size, shuffle=True, seed=seed)
    val_loader = make_loader(X_val, y_val, batch_size, shuffle=False, seed=seed)

    model = build_model(X_train.shape[1]).to(device)
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=LEARNING_RATE,
        weight_decay=WEIGHT_DECAY,
    )

    best_val_loss = float("inf")
    best_epoch = 0
    best_state = None
    epochs_without_improvement = 0
    history: list[dict[str, Any]] = []

    for epoch in range(1, epochs + 1):
        model.train()
        total_loss = 0.0
        total_count = 0

        for xb, yb in train_loader:
            xb = xb.to(device)
            yb = yb.to(device)
            optimizer.zero_grad()
            pred = model(xb)
            loss = criterion(pred, yb)
            loss.backward()
            optimizer.step()

            batch_size_current = xb.shape[0]
            total_loss += float(loss.detach().cpu().item()) * batch_size_current
            total_count += batch_size_current

        train_loss = total_loss / total_count
        val_loss = evaluate_loss(model, val_loader, criterion, device)
        improved = val_loss < best_val_loss - 1e-8

        if improved:
            best_val_loss = val_loss
            best_epoch = epoch
            best_state = copy.deepcopy(model.state_dict())
            epochs_without_improvement = 0
        else:
            epochs_without_improvement += 1

        history.append(
            {
                "epoch": epoch,
                "train_loss_mse": train_loss,
                "val_loss_mse": val_loss,
                "is_best_epoch": improved,
            }
        )

        if epochs_without_improvement >= patience:
            break

    if best_state is None:
        raise RuntimeError("No best validation state was selected for the MLP.")

    model.load_state_dict(best_state)
    return model, pd.DataFrame(history), best_epoch, best_val_loss, str(device)


def resolve_effective_args(
    args: argparse.Namespace,
) -> tuple[str, int, int, int, int | None, int | None, int | None, int]:
    n_parks = args.n_parks
    epochs = args.epochs
    batch_size = args.batch_size
    train_cap = args.max_train_rows
    val_cap = args.max_val_rows
    test_cap = args.max_test_rows

    if args.smoke:
        n_parks = n_parks or SMOKE_N_PARKS
        epochs = epochs or SMOKE_EPOCHS
        batch_size = batch_size or SMOKE_BATCH_SIZE
        train_cap = train_cap or SMOKE_MAX_TRAIN_ROWS
        val_cap = val_cap or SMOKE_MAX_VAL_ROWS
        test_cap = test_cap or SMOKE_MAX_TEST_ROWS
        return "smoke", n_parks, epochs, batch_size, train_cap, val_cap, test_cap, SMOKE_PATIENCE

    n_parks = n_parks or DEFAULT_N_PARKS
    epochs = epochs or DEFAULT_EPOCHS
    batch_size = batch_size or DEFAULT_BATCH_SIZE
    patience = DEFAULT_PATIENCE
    run_mode = (
        "capped"
        if any(cap is not None for cap in [train_cap, val_cap, test_cap])
        else "subset"
    )
    return run_mode, n_parks, epochs, batch_size, train_cap, val_cap, test_cap, patience


def output_paths(run_mode: str) -> dict[str, Path]:
    prefix = "nn_subset_mlp" if run_mode == "subset" else f"nn_subset_mlp_{run_mode}"
    return {
        "validation": OUTPUT_DIR / f"{prefix}_validation_metrics.csv",
        "selected_test": OUTPUT_DIR / f"{prefix}_selected_test_metrics.csv",
        "manifest": OUTPUT_DIR / f"{prefix}_run_manifest.csv",
        "history": OUTPUT_DIR / f"{prefix}_training_history.csv",
    }


def evidence_status(run_mode: str) -> str:
    if run_mode == "subset":
        return "subset audit only; not benchmark replacement"
    return "code-validation only; not manuscript evidence"


def build_validation_metrics_row(
    run_mode: str,
    selected_parks: list[str],
    numeric_features: list[str],
    row_counts: dict[str, int],
    args: argparse.Namespace,
    effective_epochs: int,
    batch_size: int,
    best_epoch: int,
    best_val_loss: float,
    device: str,
    val_metrics: dict[str, float],
) -> dict[str, Any]:
    return {
        "run_mode": run_mode,
        "evidence_status": evidence_status(run_mode),
        "model": "PyTorch tabular MLP",
        "selected_parks": ";".join(selected_parks),
        "n_parks": len(selected_parks),
        "seed": args.seed,
        "device": device,
        "hidden_dims": ",".join(str(dim) for dim in HIDDEN_DIMS),
        "learning_rate": LEARNING_RATE,
        "weight_decay": WEIGHT_DECAY,
        "batch_size": batch_size,
        "epochs_requested": effective_epochs,
        "best_epoch": best_epoch,
        "best_val_loss_mse": best_val_loss,
        "n_numeric_features": len(numeric_features),
        "train_rows_used": row_counts["train"],
        "val_rows_used": row_counts["val"],
        "test_rows_used": row_counts["test"],
        "MAE": val_metrics["MAE"],
        "RMSE": val_metrics["RMSE"],
        "R2": val_metrics["R2"],
        "selection_split": "validation",
        "selection_policy": "best epoch by validation MSE loss",
    }


def build_test_metrics_row(
    validation_row: dict[str, Any],
    test_metrics: dict[str, float],
) -> dict[str, Any]:
    return {
        "run_mode": validation_row["run_mode"],
        "evidence_status": validation_row["evidence_status"],
        "model": validation_row["model"],
        "selected_parks": validation_row["selected_parks"],
        "n_parks": validation_row["n_parks"],
        "seed": validation_row["seed"],
        "device": validation_row["device"],
        "hidden_dims": validation_row["hidden_dims"],
        "learning_rate": validation_row["learning_rate"],
        "weight_decay": validation_row["weight_decay"],
        "batch_size": validation_row["batch_size"],
        "epochs_requested": validation_row["epochs_requested"],
        "best_epoch": validation_row["best_epoch"],
        "best_val_loss_mse": validation_row["best_val_loss_mse"],
        "n_numeric_features": validation_row["n_numeric_features"],
        "train_rows_used": validation_row["train_rows_used"],
        "val_rows_used": validation_row["val_rows_used"],
        "test_rows_used": validation_row["test_rows_used"],
        "validation_MAE": validation_row["MAE"],
        "validation_RMSE": validation_row["RMSE"],
        "validation_R2": validation_row["R2"],
        "MAE": test_metrics["MAE"],
        "RMSE": test_metrics["RMSE"],
        "R2": test_metrics["R2"],
        "test_evaluations": 1,
        "test_policy": "selected validation state evaluated once on test subset",
    }


def build_manifest(
    run_mode: str,
    args: argparse.Namespace,
    selected_parks: list[str],
    common_park_count: int,
    numeric_features: list[str],
    non_numeric_excluded: list[str],
    row_counts: dict[str, int],
    caps: tuple[int | None, int | None, int | None],
    effective_epochs: int,
    batch_size: int,
    patience: int,
    output_files: dict[str, Path],
    elapsed_seconds: float,
) -> pd.DataFrame:
    train_cap, val_cap, test_cap = caps
    rows = {
        "script": "scripts/run_nn_subset_experiments.py",
        "run_mode": run_mode,
        "evidence_status": evidence_status(run_mode),
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
                "turbine",
            ]
        ),
        "feature_contract": "numeric learned train columns only; no turbine encoding; no validation/test statistics for feature selection",
        "scaling_policy": "StandardScaler fit on train subset feature rows only; applied to validation/test; target not scaled",
        "selection_policy": "best epoch selected by validation MSE loss",
        "test_policy": "selected validation state evaluated once on test subset",
        "baseline_metrics_policy": "data/processed/baseline_metrics.csv is not overwritten",
        "model_artifact_policy": "no model binaries or checkpoints are written",
        "common_park_count": common_park_count,
        "selected_parks": ";".join(selected_parks),
        "n_parks": len(selected_parks),
        "seed": args.seed,
        "hidden_dims": ",".join(str(dim) for dim in HIDDEN_DIMS),
        "learning_rate": LEARNING_RATE,
        "weight_decay": WEIGHT_DECAY,
        "epochs_requested": effective_epochs,
        "batch_size": batch_size,
        "patience": patience,
        "numeric_feature_count": len(numeric_features),
        "non_numeric_excluded": ", ".join(non_numeric_excluded) or "none",
        "train_rows_used": row_counts["train"],
        "val_rows_used": row_counts["val"],
        "test_rows_used": row_counts["test"],
        "max_train_rows": train_cap if train_cap is not None else "none",
        "max_val_rows": val_cap if val_cap is not None else "none",
        "max_test_rows": test_cap if test_cap is not None else "none",
        "validation_output": output_files["validation"].relative_to(ROOT),
        "selected_test_output": output_files["selected_test"].relative_to(ROOT),
        "manifest_output": output_files["manifest"].relative_to(ROOT),
        "training_history_output": output_files["history"].relative_to(ROOT),
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

    (
        run_mode,
        n_parks,
        epochs,
        batch_size,
        train_cap,
        val_cap,
        test_cap,
        patience,
    ) = resolve_effective_args(args)
    output_files = output_paths(run_mode)

    headers = {
        "train": read_header(TRAIN_PATH),
        "val": read_header(VAL_PATH),
        "test": read_header(TEST_PATH),
    }
    validate_required_columns(headers)

    selected_parks, common_park_count = select_common_parks(n_parks)
    candidate_columns = candidate_feature_columns(headers["train"])
    train_df, numeric_features, non_numeric_excluded = load_train_subset(
        candidate_columns,
        selected_parks,
        train_cap,
    )
    validate_feature_availability(headers, numeric_features)

    split_columns = [PARK_ID_COLUMN, TARGET_COLUMN, *numeric_features]
    val_df = read_filtered_split(VAL_PATH, split_columns, selected_parks, val_cap)
    test_df = read_filtered_split(TEST_PATH, split_columns, selected_parks, test_cap)

    X_train, y_train = split_xy(train_df, numeric_features, "train")
    X_val, y_val = split_xy(val_df, numeric_features, "validation")
    X_test, y_test = split_xy(test_df, numeric_features, "test")

    X_train_scaled, X_val_scaled, X_test_scaled = scale_features(
        X_train,
        X_val,
        X_test,
    )

    model, history_df, best_epoch, best_val_loss, device = train_mlp(
        X_train_scaled,
        y_train,
        X_val_scaled,
        y_val,
        seed=args.seed,
        epochs=epochs,
        batch_size=batch_size,
        patience=patience,
    )

    val_loader = make_loader(X_val_scaled, y_val, batch_size, shuffle=False, seed=args.seed)
    test_loader = make_loader(
        X_test_scaled,
        y_test,
        batch_size,
        shuffle=False,
        seed=args.seed,
    )
    import torch

    device_obj = torch.device(device)
    val_pred = predict(model, val_loader, device_obj)
    val_metrics = compute_metrics(y_val, val_pred)
    test_pred = predict(model, test_loader, device_obj)
    test_metrics = compute_metrics(y_test, test_pred)

    row_counts = {
        "train": len(train_df),
        "val": len(val_df),
        "test": len(test_df),
    }
    validation_row = build_validation_metrics_row(
        run_mode,
        selected_parks,
        numeric_features,
        row_counts,
        args,
        epochs,
        batch_size,
        best_epoch,
        best_val_loss,
        device,
        val_metrics,
    )
    test_row = build_test_metrics_row(validation_row, test_metrics)

    elapsed_seconds = time.perf_counter() - run_start
    manifest_df = build_manifest(
        run_mode,
        args,
        selected_parks,
        common_park_count,
        numeric_features,
        non_numeric_excluded,
        row_counts,
        (train_cap, val_cap, test_cap),
        epochs,
        batch_size,
        patience,
        output_files,
        elapsed_seconds,
    )

    history_df.insert(0, "run_mode", run_mode)
    history_df.insert(1, "evidence_status", evidence_status(run_mode))

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([validation_row]).to_csv(output_files["validation"], index=False)
    pd.DataFrame([test_row]).to_csv(output_files["selected_test"], index=False)
    manifest_df.to_csv(output_files["manifest"], index=False)
    history_df.to_csv(output_files["history"], index=False)

    print("NN subset MLP audit completed.")
    print(f"Run mode: {run_mode}")
    if run_mode != "subset":
        print("Evidence status: code-validation only; not manuscript evidence.")
    print(f"Selected parks: {', '.join(selected_parks)}")
    print(f"Numeric learned features: {len(numeric_features)}")
    print(f"Best epoch: {best_epoch}")
    print(f"Validation output: {output_files['validation']}")
    print(f"Selected test output: {output_files['selected_test']}")
    print(f"Run manifest: {output_files['manifest']}")
    print(f"Training history: {output_files['history']}")


if __name__ == "__main__":
    main()
