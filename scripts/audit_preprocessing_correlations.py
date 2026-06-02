from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
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

AUDIT_DIR = DATA_PROCESSED / "diagnostics" / "preprocessing_audit"
AUDIT_CSV_PATH = AUDIT_DIR / "preprocessing_correlation_audit.csv"

FIGURE_DIR = ROOT / "reports" / "figures" / "diagnostics"
FIGURE_PATH = FIGURE_DIR / "preprocessing_target_correlation_top20.png"

MARKDOWN_PATH = ROOT / "docs" / "PREPROCESSING_AUDIT.md"

HIGH_CORR_THRESHOLD = 0.95
TOP_N = 20


def require_existing_file(path: Path, label: str) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Missing required {label}: {path}")
    if not path.is_file():
        raise FileNotFoundError(f"Required {label} is not a file: {path}")


def read_header(path: Path) -> pd.Index:
    return pd.read_csv(path, nrows=0).columns


def validate_split_headers(headers: dict[str, pd.Index]) -> None:
    train_cols = list(headers["train"])
    required_columns = {
        TARGET_COLUMN,
        TIMESTAMP_COLUMN,
        PARK_ID_COLUMN,
        TEST_FLAG_COLUMN,
        BASELINE_COLUMN,
    }

    missing_required = sorted(required_columns - set(train_cols))
    if missing_required:
        raise KeyError(
            "Missing required columns from train split: "
            + ", ".join(missing_required)
        )

    for split_name in ["val", "test"]:
        split_cols = list(headers[split_name])
        if split_cols != train_cols:
            raise ValueError(
                f"Schema mismatch between train and {split_name} split headers."
            )


def candidate_feature_columns(train_columns: pd.Index) -> list[str]:
    blocked_columns = {
        TARGET_COLUMN,
        TIMESTAMP_COLUMN,
        PARK_ID_COLUMN,
        TEST_FLAG_COLUMN,
        BASELINE_COLUMN,
        "turbine",
    }
    return [col for col in train_columns if col not in blocked_columns]


def load_train_audit_frame(
    train_path: Path,
    candidate_columns: list[str],
) -> tuple[pd.DataFrame, list[str], list[str]]:
    use_columns = [TARGET_COLUMN, *candidate_columns]
    train_df = pd.read_csv(train_path, usecols=use_columns)

    if not pd.api.types.is_numeric_dtype(train_df[TARGET_COLUMN]):
        train_df[TARGET_COLUMN] = pd.to_numeric(
            train_df[TARGET_COLUMN],
            errors="raise",
        )

    numeric_features = [
        col
        for col in candidate_columns
        if pd.api.types.is_numeric_dtype(train_df[col])
    ]
    non_numeric_candidates = [
        col
        for col in candidate_columns
        if col not in numeric_features
    ]

    if not numeric_features:
        raise ValueError("No numeric learned feature columns were found.")

    return train_df, numeric_features, non_numeric_candidates


def build_target_correlation_rows(
    train_df: pd.DataFrame,
    numeric_features: list[str],
    n_high_pairs: int,
) -> pd.DataFrame:
    target = train_df[TARGET_COLUMN]
    feature_frame = train_df[numeric_features]

    target_corr = feature_frame.corrwith(target, method="pearson")
    target_df = (
        target_corr
        .rename("pearson_correlation")
        .reset_index()
        .rename(columns={"index": "feature"})
    )
    target_df["absolute_correlation"] = target_df["pearson_correlation"].abs()
    target_df = target_df.sort_values(
        ["absolute_correlation", "feature"],
        ascending=[False, True],
        na_position="last",
    ).reset_index(drop=True)
    target_df["rank"] = np.arange(1, len(target_df) + 1)

    target_df.insert(0, "row_type", "target_correlation")
    target_df["target_column"] = TARGET_COLUMN
    target_df["feature_a"] = pd.NA
    target_df["feature_b"] = pd.NA
    target_df["pair_pearson_correlation"] = np.nan
    target_df["pair_absolute_correlation"] = np.nan
    target_df["high_corr_threshold"] = HIGH_CORR_THRESHOLD
    target_df["n_train_rows"] = len(train_df)
    target_df["n_candidate_features"] = len(numeric_features)
    target_df["n_high_correlation_pairs"] = n_high_pairs

    return target_df


def build_high_pair_rows(
    train_df: pd.DataFrame,
    numeric_features: list[str],
) -> pd.DataFrame:
    feature_corr = train_df[numeric_features].corr(method="pearson")
    upper_mask = np.triu(np.ones(feature_corr.shape, dtype=bool), k=1)

    pair_df = (
        feature_corr
        .where(upper_mask)
        .stack()
        .rename("pair_pearson_correlation")
        .reset_index()
        .rename(columns={"level_0": "feature_a", "level_1": "feature_b"})
    )
    pair_df["pair_absolute_correlation"] = (
        pair_df["pair_pearson_correlation"].abs()
    )
    pair_df = pair_df.loc[
        pair_df["pair_absolute_correlation"] >= HIGH_CORR_THRESHOLD
    ].copy()
    pair_df = pair_df.sort_values(
        ["pair_absolute_correlation", "feature_a", "feature_b"],
        ascending=[False, True, True],
    ).reset_index(drop=True)

    pair_df.insert(0, "row_type", "high_feature_pair")
    pair_df["feature"] = pd.NA
    pair_df["rank"] = pd.NA
    pair_df["target_column"] = TARGET_COLUMN
    pair_df["pearson_correlation"] = np.nan
    pair_df["absolute_correlation"] = np.nan
    pair_df["high_corr_threshold"] = HIGH_CORR_THRESHOLD
    pair_df["n_train_rows"] = len(train_df)
    pair_df["n_candidate_features"] = len(numeric_features)
    pair_df["n_high_correlation_pairs"] = len(pair_df)

    return pair_df


def combine_audit_rows(
    target_rows: pd.DataFrame,
    pair_rows: pd.DataFrame,
) -> pd.DataFrame:
    output_columns = [
        "row_type",
        "feature",
        "rank",
        "target_column",
        "pearson_correlation",
        "absolute_correlation",
        "feature_a",
        "feature_b",
        "pair_pearson_correlation",
        "pair_absolute_correlation",
        "high_corr_threshold",
        "n_train_rows",
        "n_candidate_features",
        "n_high_correlation_pairs",
    ]
    return pd.concat(
        [
            target_rows.reindex(columns=output_columns),
            pair_rows.reindex(columns=output_columns),
        ],
        ignore_index=True,
    )


def save_top_target_correlation_figure(target_rows: pd.DataFrame) -> None:
    plot_df = (
        target_rows
        .dropna(subset=["absolute_correlation"])
        .head(TOP_N)
        .sort_values("absolute_correlation", ascending=True)
    )

    if plot_df.empty:
        raise ValueError("No target correlations available for plotting.")

    FIGURE_DIR.mkdir(parents=True, exist_ok=True)

    fig_height = max(6.0, 0.35 * len(plot_df))
    fig, ax = plt.subplots(figsize=(10, fig_height))
    ax.barh(plot_df["feature"], plot_df["absolute_correlation"], color="#2f6f9f")
    ax.set_xlabel(f"Absolute Pearson correlation with {TARGET_COLUMN}")
    ax.set_ylabel("Feature")
    ax.set_title("Top train-only target correlations")
    ax.grid(axis="x", linestyle="--", alpha=0.3)

    max_value = float(plot_df["absolute_correlation"].max())
    ax.set_xlim(0, min(1.0, max_value * 1.1 if max_value > 0 else 1.0))

    fig.tight_layout()
    fig.savefig(FIGURE_PATH, dpi=150)
    plt.close(fig)


def write_markdown_note(
    train_df: pd.DataFrame,
    numeric_features: list[str],
    non_numeric_candidates: list[str],
    pair_rows: pd.DataFrame,
) -> None:
    target_rows_count = len(numeric_features)
    high_pair_count = len(pair_rows)
    non_numeric_text = (
        ", ".join(f"`{col}`" for col in non_numeric_candidates)
        if non_numeric_candidates
        else "κανένα"
    )

    note = f"""# Έλεγχος preprocessing correlations

Σκοπός: leakage-aware έλεγχος συσχετίσεων για το preprocessing / feature-space contract του manuscript, χωρίς model training και χωρίς αλλαγή στα upstream artifacts.

## Inputs που χρησιμοποιούνται

- Train statistics: `data/processed/train_final.csv`
- Validation schema/header check only: `data/processed/val_final.csv`
- Test schema/header check only: `data/processed/test_final.csv`
- Target column: `{TARGET_COLUMN}`
- Excluded columns: `{TARGET_COLUMN}`, `{TIMESTAMP_COLUMN}`, `{PARK_ID_COLUMN}`, `{TEST_FLAG_COLUMN}`, `{BASELINE_COLUMN}`, `turbine`

## Κανόνες leakage-safety

- Όλες οι συσχετίσεις υπολογίζονται αποκλειστικά στο train split.
- Τα validation/test splits χρησιμοποιούνται μόνο για schema/header consistency checks.
- Δεν χρησιμοποιούνται validation ή test statistics για feature-selection decisions.
- Δεν γίνεται model training, hyperparameter tuning ή αλλαγή preprocessing policy.
- Τα high-correlation ευρήματα είναι review candidates και όχι automatic removals.

## Train-only statistics

- Train rows used: `{len(train_df):,}`
- Number of candidate numeric learned features: `{target_rows_count}`
- Number of high-correlation feature pairs with `abs(Pearson r) >= {HIGH_CORR_THRESHOLD}`: `{high_pair_count}`
- Non-numeric candidate columns excluded by the numeric feature contract: {non_numeric_text}

## Σύντομη ερμηνεία ευρημάτων

- Οι strongest target correlations κυριαρχούνται από autoregressive power/target lag features και wind-speed-related features.
- Αυτό είναι αναμενόμενο για forecasting setup και δεν υποδηλώνει από μόνο του leakage, εφόσον τα lag/rolling features έχουν παραχθεί causally από past observations.
- Τα `{high_pair_count}` high-correlation feature pairs είναι review candidates για redundancy/complexity checks και όχι automatic feature removals.
- Το audit δεν διεκδικεί model-performance improvement ή feature-removal decision.

## Outputs

- Figure: tracked manuscript-facing figure, `reports/figures/diagnostics/preprocessing_target_correlation_top20.png`
- CSV: reproducible local audit output, `data/processed/diagnostics/preprocessing_audit/preprocessing_correlation_audit.csv`
  - Το CSV αγνοείται από το repository data policy επειδή βρίσκεται κάτω από `data/processed/**`.
  - Αναπαράγεται με `python -B scripts/audit_preprocessing_correlations.py`.

## Όριο ερμηνείας

Το audit επιτρέπεται να στηρίξει προσεκτική manuscript διατύπωση για leakage-aware preprocessing checks και feature-correlation review. Δεν τεκμηριώνει από μόνο του feature removal, model-performance improvement ή αλλαγή στο canonical benchmark protocol.
"""

    MARKDOWN_PATH.write_text(note, encoding="utf-8")


def main() -> None:
    for label, path in [
        ("train split", TRAIN_PATH),
        ("validation split", VAL_PATH),
        ("test split", TEST_PATH),
    ]:
        require_existing_file(path, label)

    headers = {
        "train": read_header(TRAIN_PATH),
        "val": read_header(VAL_PATH),
        "test": read_header(TEST_PATH),
    }
    validate_split_headers(headers)

    candidates = candidate_feature_columns(headers["train"])
    train_df, numeric_features, non_numeric_candidates = load_train_audit_frame(
        TRAIN_PATH,
        candidates,
    )

    pair_rows = build_high_pair_rows(train_df, numeric_features)
    target_rows = build_target_correlation_rows(
        train_df,
        numeric_features,
        n_high_pairs=len(pair_rows),
    )
    audit_df = combine_audit_rows(target_rows, pair_rows)

    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    audit_df.to_csv(AUDIT_CSV_PATH, index=False)
    save_top_target_correlation_figure(target_rows)
    write_markdown_note(
        train_df,
        numeric_features,
        non_numeric_candidates,
        pair_rows,
    )

    print("Preprocessing correlation audit completed.")
    print(f"Candidate numeric learned features: {len(numeric_features)}")
    print(f"High-correlation pairs: {len(pair_rows)}")
    print(f"CSV: {AUDIT_CSV_PATH}")
    print(f"Figure: {FIGURE_PATH}")
    print(f"Markdown note: {MARKDOWN_PATH}")


if __name__ == "__main__":
    main()
