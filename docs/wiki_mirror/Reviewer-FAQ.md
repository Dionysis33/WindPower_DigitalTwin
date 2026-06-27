# Reviewer FAQ

## Is this project a deployed digital twin?

No. The repository is a forecasting-first research pipeline with diagnostics and methodological extensions. It is not a deployed monitoring system or fully implemented digital twin.

## Does the project claim validated PHM or fault diagnosis?

No. Residual diagnostics are candidate screening and interpretation signals. They are not confirmed faults, fault diagnosis, Remaining Useful Life estimation, or validated PHM.

## What is the canonical benchmark?

`data/processed/baseline_metrics.csv` is the canonical full-dataset test-set benchmark artifact for the implemented tabular baseline ladder.

## What can be said about XGBoost?

XGBoost is the lowest-MAE model within the implemented canonical full-dataset tabular benchmark. This should not be generalized to all possible models, all subsets, graph experiments, or future sequence models.

## Are neural and sequence models part of the canonical benchmark?

No. `NB15`, `NB16`, `NB18`, and `NB19` are controlled four-park neural / sequence subset evidence only. They support bounded discussion and future-work motivation, not replacement of the canonical benchmark. `NB17` is an unaudited Mamba sequence scaffold unless a reviewed audit document is added.

## How should NB20 and NB21 be interpreted?

`NB20` and `NB21` are validation-calibrated residual diagnostic interpretation layers over forecasting outputs. They do not establish validated PHM, fault diagnosis, anomaly detection, Remaining Useful Life estimation, or deployed digital twin functionality.

## Do graph-aware stages prove graph superiority?

No. The graph-aware stages are methodological extensions: graph contract verification, graph input packaging, first graph-based forecasting baseline, ablation, and controlled refinement. They are not validated graph superiority.

## Are local outputs public evidence?

Not by default. Local diagnostics, tuning outputs, graph exports, subset outputs, model binaries, and checkpoints remain local-only unless explicitly promoted and reviewed.

## Source Documents

- `README.md`
- `docs/RESEARCH_SCOPE.md`
- `docs/BASELINE_PROTOCOL.md`
- `docs/DATA.md`
- `docs/PHM_ROADMAP.md`
- `docs/NEURAL_BASELINE_COMPARISON_SUMMARY.md`
- `CONTRIBUTING.md`
- `SECURITY.md`
