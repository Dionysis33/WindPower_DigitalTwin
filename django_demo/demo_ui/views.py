from __future__ import annotations

import json
from pathlib import Path

from django.conf import settings
from django.shortcuts import render


def home_view(request):
    """
    Render the local forecasting artifact interface.

    This view only reads already exported local artifacts.
    It does not trigger model training, forecasting execution,
    diagnostics generation, or benchmark-writing workflows.
    """

    # Resolve the local artifact directory configured in settings.py
    artifact_dir = Path(settings.DEMO_ARTIFACT_DIR)

    # The manifest is the main entry point for the lightweight interface
    manifest_path = artifact_dir / "demo_manifest.json"

    # Default empty state if the manifest is missing or malformed
    manifest = {}
    manifest_exists = manifest_path.exists()

    # Read the manifest only if it exists
    if manifest_exists:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except Exception:
            manifest = {}

    # ------------------------------------------------------------------
    # Raw values loaded from the manifest
    # ------------------------------------------------------------------
    raw_artifact_counts = manifest.get("artifact_counts", {}) or {}
    selected_parks = manifest.get("selected_parks", []) or []
    non_claims = manifest.get("non_claims", []) or []

    # ------------------------------------------------------------------
    # User-facing labels for summary metrics
    # ------------------------------------------------------------------
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

    # ------------------------------------------------------------------
    # Thesis-safe wording for explicit non-claims
    # ------------------------------------------------------------------
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

    # ------------------------------------------------------------------
    # Template context
    # ------------------------------------------------------------------
    context = {
        "page_title": "WindPower Forecasting Interface",
        "artifact_dir": artifact_dir,
        "manifest_exists": manifest_exists,
        "artifact_counts": display_artifact_counts,
        "selected_parks": selected_parks,
        "display_non_claims": display_non_claims,
    }

    return render(request, "demo_ui/home.html", context)