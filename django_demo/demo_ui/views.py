from __future__ import annotations

import json
from pathlib import Path

from django.conf import settings
from django.shortcuts import render


def home_view(request):
    demo_dir = Path(settings.DEMO_ARTIFACT_DIR)
    manifest_path = demo_dir / "demo_manifest.json"

    manifest = {}
    manifest_exists = manifest_path.exists()

    if manifest_exists:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except Exception:
            manifest = {"error": "Failed to parse demo_manifest.json"}

    context = {
        "page_title": "WindPower Digital Twin Demo",
        "demo_dir": str(demo_dir),
        "manifest_exists": manifest_exists,
        "manifest": manifest,
        "selected_parks": manifest.get("selected_parks", []),
        "artifact_counts": manifest.get("artifact_counts", {}),
        "non_claims": manifest.get("non_claims", []),
    }

    return render(request, "demo_ui/home.html", context)