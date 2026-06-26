# Canonical Benchmark and Tabular Results

The canonical benchmark authority is:

```text
data/processed/baseline_metrics.csv
```

This artifact is the repository's full-dataset final test-set benchmark table for the implemented tabular baseline ladder.

## Implemented Benchmark Space

The implemented canonical tabular benchmark includes:

- Persistence
- Linear Regression
- Random Forest
- XGBoost
- MLP

Within this implemented canonical full-dataset tabular benchmark, XGBoost is documented as the lowest-MAE model. That statement should not be generalized beyond this benchmark space.

## Canonical Metrics

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

- `data/processed/baseline_metrics.csv`
- `docs/BASELINE_PROTOCOL.md`
- `docs/XGBOOST_TUNING_AUDIT.md`
- `docs/NEURAL_BASELINE_COMPARISON_SUMMARY.md`
- `README.md`
