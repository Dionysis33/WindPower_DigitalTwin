from __future__ import annotations

import csv
import json
from pathlib import Path

from django.conf import settings
from django.shortcuts import render


def _safe_read_csv_rows(path_value: str | None, limit: int | None = None) -> list[dict]:
    """
    Read already exported CSV rows from the local demo bundle.

    This helper is intentionally read-only and defensive:
    - it never triggers notebook execution
    - it never computes new benchmark outputs
    - it only consumes existing exported files
    """
    if not path_value:
        return []

    path = Path(path_value)
    if not path.exists():
        return []

    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        return rows[:limit] if limit is not None else rows
    except Exception:
        return []


def _safe_read_text(path_value: str | None) -> str:
    """Read a small exported text artifact if it exists."""
    if not path_value:
        return ""

    path = Path(path_value)
    if not path.exists():
        return ""

    try:
        return path.read_text(encoding="utf-8").strip()
    except Exception:
        return ""


def _format_metric(value: str | None, decimals: int = 4) -> str:
    """Format numeric-looking values for cleaner UI display."""
    if value in (None, ""):
        return "—"

    try:
        return f"{float(value):.{decimals}f}"
    except (TypeError, ValueError):
        return str(value)


def _humanize_token(value: str | None) -> str:
    """Convert underscore-style tokens into more readable UI text."""
    if value in (None, ""):
        return "—"
    return str(value).replace("_", " ").strip()


def _first_non_empty(*values: str | None) -> str:
    """Return the first non-empty string-like value."""
    for value in values:
        if value not in (None, ""):
            return str(value)
    return ""


def _build_demo_context() -> dict:
    """
    Build shared template context for the local read-only demo interface.

    The interface is intentionally limited to already exported artifacts.
    It does not trigger:
    - retraining
    - notebook execution
    - new diagnostics generation
    - new benchmark-writing workflows
    """

    artifact_dir = Path(settings.DEMO_ARTIFACT_DIR)
    manifest_path = artifact_dir / "demo_manifest.json"

    manifest = {}
    manifest_exists = manifest_path.exists()

    if manifest_exists:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except Exception:
            manifest = {}

    raw_artifact_counts = manifest.get("artifact_counts", {}) or {}
    selected_parks = manifest.get("selected_parks", []) or []
    non_claims = manifest.get("non_claims", []) or []
    exported_files = manifest.get("exported_files", {}) or {}

    metric_label_map = {
        "benchmark_rows": "Benchmark rows",
        "prediction_rows": "Prediction rows",
        "park_rows": "Selected parks",
        "regime_rows": "Regime rows",
    }

    display_artifact_counts = [
        {
            "key": key,
            "label": metric_label_map.get(key, key.replace("_", " ").title()),
            "value": value,
        }
        for key, value in raw_artifact_counts.items()
    ]

    non_claim_label_map = {
        "not_completed_digital_twin": "Not a completed digital twin",
        "not_phm_platform": "Not a PHM platform",
        "not_anomaly_detector": "Not an anomaly detector",
        "not_fault_diagnosis_module": "Not a fault diagnosis module",
        "not_prognostics_or_rul_engine": "Not a prognostics / RUL engine",
        "not_new_benchmark_stage": "Not a new benchmark stage",
        "not_production_deployment": "Not a production deployment",
    }

    display_non_claims = [
        non_claim_label_map.get(item, item.replace("_", " ").strip().title())
        for item in non_claims
    ]

    benchmark_rows_raw = _safe_read_csv_rows(exported_files.get("benchmark_summary"), limit=5)
    park_rows_raw = _safe_read_csv_rows(exported_files.get("park_summary"), limit=12)
    regime_rows_raw = _safe_read_csv_rows(exported_files.get("regime_summary"), limit=8)
    case_rows_raw = _safe_read_csv_rows(exported_files.get("case_study_metadata"), limit=6)
    ui_notes = _safe_read_text(exported_files.get("ui_notes"))

    benchmark_rows = [
        {
            "model": row.get("Model", ""),
            "rank": row.get("demo_rank", ""),
            "mae": _format_metric(row.get("MAE"), 4),
            "rmse": _format_metric(row.get("RMSE"), 4),
            "r2": _format_metric(row.get("R2"), 4),
        }
        for row in benchmark_rows_raw
    ]

    benchmark_leader = benchmark_rows[0] if benchmark_rows else None

    park_rows = [
        {
            "park_id": row.get("park_id", ""),
            "demo_rows": row.get("demo_rows", ""),
            "available_models": row.get("available_models", ""),
            "window_start": row.get("window_start", ""),
            "window_end": row.get("window_end", ""),
        }
        for row in park_rows_raw
    ]

    regime_rows = [
        {
            "source": row.get("demo_regime_source", ""),
            "label": _first_non_empty(
                row.get("wind_regime"),
                row.get("power_regime"),
                row.get("time_block"),
                "Unspecified regime",
            ),
            "model": row.get("model", ""),
            "mae": _format_metric(row.get("mae"), 4),
            "rmse": _format_metric(row.get("rmse"), 4),
        }
        for row in regime_rows_raw
    ]

    case_rows = [
        {
            "park_id": row.get("park_id", ""),
            "case_order": row.get("demo_case_order", ""),
            "selection_reason": _humanize_token(row.get("selection_reason", "")),
            "window_start": row.get("window_start", ""),
            "window_end": row.get("window_end", ""),
            "available_models": row.get("available_models", ""),
        }
        for row in case_rows_raw
    ]

    display_exported_files = [
        {
            "key": key,
            "label": key.replace("_", " ").title(),
            "filename": Path(value).name,
        }
        for key, value in exported_files.items()
        if value
    ]

    return {
        "page_title": "WindPower Forecasting Interface",
        "artifact_dir": artifact_dir,
        "manifest_exists": manifest_exists,
        "artifact_counts": display_artifact_counts,
        "selected_parks": selected_parks,
        "display_non_claims": display_non_claims,
        "benchmark_rows": benchmark_rows,
        "benchmark_leader": benchmark_leader,
        "park_rows": park_rows,
        "regime_rows": regime_rows,
        "case_rows": case_rows,
        "ui_notes": ui_notes,
        "exported_files": display_exported_files,
    }


def home_view(request):
    context = _build_demo_context()
    return render(request, "demo_ui/home.html", context)


def parks_view(request):
    context = _build_demo_context()
    return render(request, "demo_ui/parks.html", context)


def artifacts_view(request):
    context = _build_demo_context()
    return render(request, "demo_ui/artifacts.html", context)


def scope_view(request):
    context = _build_demo_context()
    return render(request, "demo_ui/scope.html", context)