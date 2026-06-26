# Local Demo and Artifact Browser

The optional `django_demo/` interface is a local, read-only, thesis-facing artifact browser. It is intended to help inspect already exported local artifacts during presentation or review.

## Intended Role

The demo may be described as:

- local-only
- read-only
- non-production
- thesis-facing
- an artifact inspection helper

It should consume curated local exports only.

## Claim Boundary

Do not describe the demo as:

- a deployed digital twin
- a production monitoring service
- a PHM system
- an anomaly-detection service
- a fault-diagnosis system
- an operational forecasting platform
- a security-hardened public service

The demo should not train models, rerun notebooks, rewrite benchmark results, mutate processed artifacts, or create canonical evidence.

## Source Documents

- `README.md`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `scripts/export_demo_bundle.py`
