from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd


# -------------------------------------------------------------------
# Ensure repository root is importable
# -------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


from src.config import (  # noqa: E402
    BASELINE_METRICS_PATH,
    NB06_TEST_PREDICTIONS_PATH,
    NB07_ALL_TEST_PREDICTIONS_LONG,
    NB08_POWER_REGIME_METRICS,
    NB08_TIME_BLOCK_METRICS,
    NB08_WIND_REGIME_METRICS,
    DEMO_BENCHMARK_SUMMARY,
    DEMO_CASE_STUDY_METADATA,
    DEMO_DIR,
    DEMO_MANIFEST_PATH,
    DEMO_PARK_SUMMARY,
    DEMO_PREDICTIONS_LONG,
    DEMO_REGIME_SUMMARY,
    DEMO_UI_NOTES_PATH,
    PARK_ID_COLUMN,
    TIMESTAMP_COLUMN,
)


# -------------------------------------------------------------------
# Demo export settings
# -------------------------------------------------------------------
MAX_DEMO_PARKS = 12


# -------------------------------------------------------------------
# Small helpers
# -------------------------------------------------------------------
def find_column(df: pd.DataFrame, candidates: list[str]) -> str | None:
    """
    Επιστρέφει το πρώτο matching column name με case-insensitive λογική.
    """
    lower_map = {str(col).strip().lower(): col for col in df.columns}

    for candidate in candidates:
        hit = lower_map.get(candidate.lower())
        if hit is not None:
            return hit

    return None


def read_csv_optional(path: Path) -> pd.DataFrame | None:
    """
    Διαβάζει CSV μόνο αν υπάρχει.
    """
    if path.exists():
        return pd.read_csv(path)
    return None


def ensure_demo_dir() -> None:
    DEMO_DIR.mkdir(parents=True, exist_ok=True)


# -------------------------------------------------------------------
# Benchmark export
# -------------------------------------------------------------------
def export_benchmark_summary() -> pd.DataFrame:
    if not BASELINE_METRICS_PATH.exists():
        raise FileNotFoundError(
            f"Δεν βρέθηκε το canonical benchmark artifact: {BASELINE_METRICS_PATH}"
        )

    df = pd.read_csv(BASELINE_METRICS_PATH).copy()

    mae_col = find_column(df, ["MAE", "mae"])
    model_col = find_column(df, ["model", "Model", "method", "name", "baseline"])

    if mae_col is not None:
        df = df.sort_values(by=mae_col, ascending=True).reset_index(drop=True)
        df["demo_rank"] = range(1, len(df) + 1)

    if model_col is not None and "demo_rank" in df.columns:
        ordered_cols = ["demo_rank", model_col] + [
            col for col in df.columns if col not in {"demo_rank", model_col}
        ]
        df = df[ordered_cols]

    df.to_csv(DEMO_BENCHMARK_SUMMARY, index=False)
    return df


# -------------------------------------------------------------------
# Prediction export
# -------------------------------------------------------------------
def load_prediction_source() -> tuple[pd.DataFrame, str]:
    """
    Προτιμάμε το NB07 long predictions artifact.
    Αν λείπει, κάνουμε fallback στο NB06 predictions artifact.
    """
    if NB07_ALL_TEST_PREDICTIONS_LONG.exists():
        return pd.read_csv(NB07_ALL_TEST_PREDICTIONS_LONG), "NB07_ALL_TEST_PREDICTIONS_LONG"

    if NB06_TEST_PREDICTIONS_PATH.exists():
        return pd.read_csv(NB06_TEST_PREDICTIONS_PATH), "NB06_TEST_PREDICTIONS_PATH"

    raise FileNotFoundError(
        "Δεν βρέθηκε prediction artifact ούτε στο NB07 ούτε στο NB06."
    )


def curate_predictions_for_demo(
    df: pd.DataFrame,
    max_demo_parks: int = MAX_DEMO_PARKS,
) -> tuple[pd.DataFrame, list[str], str | None, str | None, str | None]:
    """
    Κρατάμε μόνο λίγα parks για να μείνει το demo ελαφρύ.
    Η επιλογή είναι deterministic:
    - top parks by row coverage
    - tie-break by park_id ascending
    """
    park_col = find_column(df, [PARK_ID_COLUMN, "park_id", "park"])
    timestamp_col = find_column(df, [TIMESTAMP_COLUMN, "timestamp", "time", "datetime"])
    model_col = find_column(df, ["model", "Model", "method", "baseline"])

    if park_col is None:
        raise KeyError(
            f"Δεν βρέθηκε column park_id στο prediction artifact. Columns={df.columns.tolist()}"
        )

    work = df.copy()
    work[park_col] = work[park_col].astype(str).str.zfill(5)

    if timestamp_col is not None:
        work[timestamp_col] = pd.to_datetime(work[timestamp_col], errors="coerce")

    park_counts = (
        work.groupby(park_col)
        .size()
        .rename("row_count")
        .reset_index()
        .sort_values(by=["row_count", park_col], ascending=[False, True])
        .reset_index(drop=True)
    )

    selected_parks = park_counts.head(max_demo_parks)[park_col].tolist()

    filtered = work[work[park_col].isin(selected_parks)].copy()

    sort_cols = [park_col]
    if model_col is not None:
        sort_cols.append(model_col)
    if timestamp_col is not None:
        sort_cols.append(timestamp_col)

    filtered = filtered.sort_values(by=sort_cols).reset_index(drop=True)

    # Κρατάμε essential columns αν υπάρχουν, αλλιώς όλο το filtered dataframe
    actual_col = find_column(
        filtered,
        ["actual", "y_true", "target", "Power_Output_Normalized"],
    )
    pred_col = find_column(
        filtered,
        ["prediction", "pred", "y_pred", "Predicted"],
    )
    residual_col = find_column(filtered, ["residual", "error"])
    abs_error_col = find_column(filtered, ["abs_error", "absolute_error"])

    keep_candidates = [
        park_col,
        timestamp_col,
        model_col,
        actual_col,
        pred_col,
        residual_col,
        abs_error_col,
    ]
    keep_cols = [col for col in keep_candidates if col is not None]

    if len(keep_cols) >= 3:
        filtered = filtered[keep_cols].copy()

    if timestamp_col is not None and timestamp_col in filtered.columns:
        filtered[timestamp_col] = pd.to_datetime(
            filtered[timestamp_col], errors="coerce"
        ).dt.strftime("%Y-%m-%d %H:%M:%S")

    filtered.to_csv(DEMO_PREDICTIONS_LONG, index=False)

    return filtered, selected_parks, park_col, timestamp_col, model_col


# -------------------------------------------------------------------
# Park summary export
# -------------------------------------------------------------------
def build_park_summary(
    filtered_predictions: pd.DataFrame,
    park_col: str,
    timestamp_col: str | None,
    model_col: str | None,
) -> pd.DataFrame:
    park_summary = (
        filtered_predictions.groupby(park_col)
        .size()
        .rename("demo_rows")
        .reset_index()
        .sort_values(by=[park_col])
        .reset_index(drop=True)
    )

    if model_col is not None and model_col in filtered_predictions.columns:
        model_counts = (
            filtered_predictions.groupby(park_col)[model_col]
            .nunique()
            .rename("available_models")
            .reset_index()
        )
        park_summary = park_summary.merge(model_counts, on=park_col, how="left")

    if timestamp_col is not None and timestamp_col in filtered_predictions.columns:
        temp = filtered_predictions.copy()
        temp[timestamp_col] = pd.to_datetime(temp[timestamp_col], errors="coerce")

        time_window = (
            temp.groupby(park_col)[timestamp_col]
            .agg(["min", "max"])
            .reset_index()
            .rename(columns={"min": "window_start", "max": "window_end"})
        )

        for col in ["window_start", "window_end"]:
            time_window[col] = pd.to_datetime(time_window[col], errors="coerce").dt.strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        park_summary = park_summary.merge(time_window, on=park_col, how="left")

    park_summary.to_csv(DEMO_PARK_SUMMARY, index=False)
    return park_summary


# -------------------------------------------------------------------
# Regime summary export
# -------------------------------------------------------------------
def export_regime_summary() -> pd.DataFrame:
    pieces: list[pd.DataFrame] = []

    for path, source_name in [
        (NB08_WIND_REGIME_METRICS, "wind_regime"),
        (NB08_POWER_REGIME_METRICS, "power_regime"),
        (NB08_TIME_BLOCK_METRICS, "time_block"),
    ]:
        df = read_csv_optional(path)
        if df is not None:
            temp = df.copy()
            temp["demo_regime_source"] = source_name
            pieces.append(temp)

    if pieces:
        regime_summary = pd.concat(pieces, ignore_index=True)
    else:
        regime_summary = pd.DataFrame(columns=["demo_regime_source"])

    regime_summary.to_csv(DEMO_REGIME_SUMMARY, index=False)
    return regime_summary


# -------------------------------------------------------------------
# Case-study metadata export
# -------------------------------------------------------------------
def export_case_study_metadata(park_summary: pd.DataFrame, park_col: str) -> pd.DataFrame:
    """
    Απλό deterministic case-study scaffold για το πρώτο demo pass.
    Δεν αποτελεί scientific ranking ή thesis claim.
    """
    case_df = park_summary.copy()
    case_df["demo_case_order"] = range(1, len(case_df) + 1)
    case_df["selection_reason"] = "auto_selected_for_local_demo_bundle"

    ordered_cols = ["demo_case_order", park_col] + [
        col for col in case_df.columns if col not in {"demo_case_order", park_col}
    ]
    case_df = case_df[ordered_cols]

    case_df.to_csv(DEMO_CASE_STUDY_METADATA, index=False)
    return case_df


# -------------------------------------------------------------------
# UI notes / non-claims
# -------------------------------------------------------------------
def write_ui_notes() -> None:
    ui_text = """This local Django demo is a lightweight, read-only interface layer.
It visualizes already generated forecasting, diagnostics, and selected artifact summaries.
It is not a completed digital twin, PHM platform, anomaly detector, fault diagnosis module,
prognostics engine, RUL estimator, production deployment, or new benchmark stage.
"""

    DEMO_UI_NOTES_PATH.write_text(ui_text, encoding="utf-8")


# -------------------------------------------------------------------
# Manifest export
# -------------------------------------------------------------------
def write_manifest(
    benchmark_df: pd.DataFrame,
    predictions_df: pd.DataFrame,
    park_summary_df: pd.DataFrame,
    regime_df: pd.DataFrame,
    selected_parks: list[str],
    prediction_source_name: str,
) -> None:
    manifest = {
        "demo_version": "v1",
        "bundle_type": "local_read_only_django_demo",
        "prediction_source": prediction_source_name,
        "max_demo_parks": MAX_DEMO_PARKS,
        "selected_parks": selected_parks,
        "artifact_counts": {
            "benchmark_rows": int(len(benchmark_df)),
            "prediction_rows": int(len(predictions_df)),
            "park_rows": int(len(park_summary_df)),
            "regime_rows": int(len(regime_df)),
        },
        "exported_files": {
            "benchmark_summary": str(DEMO_BENCHMARK_SUMMARY),
            "park_summary": str(DEMO_PARK_SUMMARY),
            "predictions_long": str(DEMO_PREDICTIONS_LONG),
            "regime_summary": str(DEMO_REGIME_SUMMARY),
            "case_study_metadata": str(DEMO_CASE_STUDY_METADATA),
            "ui_notes": str(DEMO_UI_NOTES_PATH),
        },
        "non_claims": [
            "not_completed_digital_twin",
            "not_phm_platform",
            "not_anomaly_detector",
            "not_fault_diagnosis_module",
            "not_prognostics_or_rul_engine",
            "not_new_benchmark_stage",
            "not_production_deployment",
        ],
    }

    DEMO_MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


# -------------------------------------------------------------------
# Main
# -------------------------------------------------------------------
def main() -> None:
    ensure_demo_dir()

    print("Exporting demo benchmark summary...")
    benchmark_df = export_benchmark_summary()

    print("Loading canonical prediction source...")
    prediction_df, prediction_source_name = load_prediction_source()

    print("Curating predictions for demo parks...")
    curated_predictions, selected_parks, park_col, timestamp_col, model_col = curate_predictions_for_demo(
        prediction_df
    )

    print("Building demo park summary...")
    park_summary_df = build_park_summary(
        curated_predictions,
        park_col=park_col,
        timestamp_col=timestamp_col,
        model_col=model_col,
    )

    print("Exporting regime summary...")
    regime_df = export_regime_summary()

    print("Exporting case-study metadata...")
    export_case_study_metadata(park_summary_df, park_col=park_col)

    print("Writing UI notes...")
    write_ui_notes()

    print("Writing manifest...")
    write_manifest(
        benchmark_df=benchmark_df,
        predictions_df=curated_predictions,
        park_summary_df=park_summary_df,
        regime_df=regime_df,
        selected_parks=selected_parks,
        prediction_source_name=prediction_source_name,
    )

    print("\nDemo bundle export completed successfully.")
    print(f"Selected demo parks: {selected_parks}")
    print(f"Output directory: {DEMO_DIR}")


if __name__ == "__main__":
    main()