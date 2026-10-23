# Canonical Benchmark and Tabular Results

The previously tracked full-dataset tabular benchmark artifact is retained locally at:

```text
data/processed/baseline_metrics.csv
```

The previously tracked baseline metrics CSV has been withdrawn from the current repository snapshot pending reconciliation of its experimental provenance and numerical consistency with the manuscript. The research artifact is retained locally, and no replacement public canonical metrics CSV has yet been approved. This withdrawal does not establish that the CSV or manuscript results are scientifically incorrect.

## Implemented Benchmark Space

The implemented canonical tabular benchmark includes:

- Persistence
- Linear Regression
- Random Forest
- XGBoost
- MLP

Within the previously recorded full-dataset tabular benchmark, XGBoost was documented as the lowest-MAE model. This preserved result context is subject to the provenance reconciliation above and should not be generalized beyond that benchmark space.

## Canonical Metrics

The values below preserve the previously documented research record. They are unchanged and do not constitute an approved replacement public canonical metrics artifact.

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| XGBoost | 0.0657 | 0.1135 | 0.860 |
| MLP | 0.0680 | 0.1153 | 0.856 |
| Persistence | 0.0698 | 0.1304 | 0.816 |
| Random Forest | 0.0710 | 0.1188 | 0.847 |
| Linear Regression | 0.0727 | 0.1203 | 0.843 |

## What Does Not Replace The Benchmark

The following do not replace `data/processed/baseline_metrics.csv`:

- XGBoost tuning audits
- residual diagnostics outputs
- graph verification, packaging, baseline, ablation, or refinement outputs
- matched four-park baseline outputs
- neural or sequence subset outputs
- local diagnostics CSVs
- model binaries or checkpoints

## Source Documents

- `data/processed/baseline_metrics.csv` (retained locally; withdrawn from the current repository snapshot)
- `docs/BASELINE_PROTOCOL.md`
- `docs/XGBOOST_TUNING_AUDIT.md`
- `docs/NEURAL_BASELINE_COMPARISON_SUMMARY.md`
- `README.md`
