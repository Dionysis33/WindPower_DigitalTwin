# Leakage Safe Evaluation Protocol

The repository uses leakage-safe evaluation rules to keep forecasting results reviewer-safe and comparable.

## Core Rules

- Splits are temporal, not random.
- Training data is used for model fitting.
- Validation data is used for model or configuration selection.
- Test data is used only for final reporting after selection is fixed.
- Preprocessing statistics that could leak information are derived from training data only.
- Feature spaces should remain consistent across train, validation, and test.

## Benchmark Authority

The canonical full-dataset tabular benchmark authority is:

```text
data/processed/baseline_metrics.csv
```

Local diagnostics, tuning outputs, graph outputs, and controlled subset outputs do not replace this benchmark artifact.

## Extension Boundaries

Residual diagnostics may use fixed validation-derived thresholds for candidate screening signals. Graph-aware and subset experiments may have their own bounded protocols, but they must not be presented as validated graph superiority or full-dataset benchmark replacements.

## Source Documents

- `docs/BASELINE_PROTOCOL.md`
- `docs/DATA.md`
- `docs/PREPROCESSING_AUDIT.md`
- `docs/XGBOOST_TUNING_AUDIT.md`
- `docs/NEURAL_BASELINE_COMPARISON_SUMMARY.md`
- `docs/RESIDUAL_PHM_DIAGNOSTICS_AUDIT.md`
