# Matched Four-Park Baseline Comparison Audit

## Purpose and scope

This document records the completed local matched four-park baseline comparison generated under `data/processed/diagnostics/matched_four_park_baseline/`.

The audit covers row-level tabular baseline results for the same selected parks used by the neural subset audits: `00183`, `00198`, `00303`, and `00427`. It is local matched-subset evidence only. It does not replace `data/processed/baseline_metrics.csv`, does not modify the canonical full-dataset benchmark, and must not be merged into the canonical full-dataset benchmark ranking.

## Run manifest summary

| Field | Value |
|---|---|
| Script | `scripts/run_matched_four_park_baseline_comparison.py` |
| Run mode | `matched_four_park` |
| Evidence status | local matched-subset evidence; not benchmark replacement |
| Selected parks | `00183`; `00198`; `00303`; `00427` |
| Train rows used | `31,276` |
| Validation rows used | `2,880` |
| Test rows used | `17,180` |
| Numeric feature count | `41` |
| Excluded columns | `Baseline_Prediction`; `Power_Output_Normalized`; `park_id`; `test_flag`; `timestamp`; `turbine` |
| Feature contract | train-inferred numeric learned columns only; no turbine encoding |
| Models | Persistence; Linear Regression; Random Forest; XGBoost; MLP |
| Selection policy | validation-only model/config selection where applicable |
| Test policy | final selected models evaluated once on the test subset |
| Output policy | local diagnostics only; `data/processed/baseline_metrics.csv` is not read for ranking and is not overwritten |
| Model artifact policy | no model binaries or checkpoints are written |
| Validation output | `data/processed/diagnostics/matched_four_park_baseline/matched_four_park_baseline_validation_metrics.csv` |
| Selected test output | `data/processed/diagnostics/matched_four_park_baseline/matched_four_park_baseline_selected_test_metrics.csv` |
| Manifest output | `data/processed/diagnostics/matched_four_park_baseline/matched_four_park_baseline_run_manifest.csv` |
| Elapsed seconds | `114.554` |

## Method summary

The run evaluates a matched four-park row-level tabular subset using the same selected parks as the neural subset audits. The subset uses rows from the existing `train_final.csv`, `val_final.csv`, and `test_final.csv` split artifacts after zero-padded `park_id` normalization and selected-park filtering.

The learned feature space is inferred from train only. It excludes the target, `park_id`, `timestamp`, `test_flag`, `Baseline_Prediction`, and `turbine`; no `turbine` encoding is used. Random Forest, XGBoost, and MLP use validation-only model/config selection where applicable, and final selected models are evaluated once on the test subset.

## Validation metrics

| Model | Model family | Config ID | MAE | RMSE | R2 | Selection rule |
|---|---|---|---:|---:|---:|---|
| Persistence | naive temporal baseline | fixed | 0.0687021252332015 | 0.12911695615731547 | 0.8391842248050012 | fixed baseline; no model selection |
| Linear Regression | linear tabular baseline | fixed | 0.07852262078444408 | 0.12185872597989066 | 0.8567563573283657 | fixed baseline; no model selection |
| Random Forest | tree ensemble tabular baseline | 1 | 0.08073788525908096 | 0.12711554059640223 | 0.8441311298065655 | validation MAE asc, validation RMSE asc, validation R2 desc |
| Random Forest | tree ensemble tabular baseline | 2 | 0.07850516861221037 | 0.12423260697396153 | 0.851121053294085 | validation MAE asc, validation RMSE asc, validation R2 desc |
| Random Forest | tree ensemble tabular baseline | 3 | 0.07801707033350694 | 0.12423824024011536 | 0.8511075513034794 | validation MAE asc, validation RMSE asc, validation R2 desc |
| XGBoost | gradient-boosted tree tabular baseline | 1 | 0.07308165868558587 | 0.12123304823061623 | 0.8582235361988124 | validation MAE asc, validation RMSE asc, validation R2 desc |
| XGBoost | gradient-boosted tree tabular baseline | 2 | 0.07434081388547913 | 0.1224377988036847 | 0.8553917347184521 | validation MAE asc, validation RMSE asc, validation R2 desc |
| XGBoost | gradient-boosted tree tabular baseline | 3 | 0.07655231580038863 | 0.1244050762888579 | 0.8507073958171921 | validation MAE asc, validation RMSE asc, validation R2 desc |
| MLP | NB07-style PyTorch tabular neural baseline | 1 | 0.07981470749865623 | 0.1247620296161676 | 0.8498494413648559 | best epoch/config by validation MSE loss, then MAE/RMSE/R2 reporting |
| MLP | NB07-style PyTorch tabular neural baseline | 2 | 0.07704863808157447 | 0.12179411036939128 | 0.8569082269857697 | best epoch/config by validation MSE loss, then MAE/RMSE/R2 reporting |
| MLP | NB07-style PyTorch tabular neural baseline | 3 | 0.07989062618957925 | 0.1253557543633297 | 0.8484169506574764 | best epoch/config by validation MSE loss, then MAE/RMSE/R2 reporting |

## Selected test metrics

| Model | Model family | Selected config ID | Validation MAE | Validation RMSE | Validation R2 | Test MAE | Test RMSE | Test R2 | test_evaluations |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| XGBoost | gradient-boosted tree tabular baseline | 1 | 0.07308165868558587 | 0.12123304823061623 | 0.8582235361988124 | 0.07916488214900315 | 0.13048056280434156 | 0.8733693976256192 | 1 |
| Persistence | naive temporal baseline | fixed | 0.0687021252332015 | 0.12911695615731547 | 0.8391842248050012 | 0.08079669733592597 | 0.1474239474217667 | 0.8383472483419506 | 1 |
| Random Forest | tree ensemble tabular baseline | 3 | 0.07801707033350694 | 0.12423824024011536 | 0.8511075513034794 | 0.08389790455769289 | 0.13389992624988545 | 0.8666454906497136 | 1 |
| MLP | NB07-style PyTorch tabular neural baseline | 2 | 0.07704863808157447 | 0.12179411036939128 | 0.8569082269857697 | 0.08538023613281545 | 0.13285203467352433 | 0.868724569689501 | 1 |
| Linear Regression | linear tabular baseline | fixed | 0.07852262078444408 | 0.12185872597989066 | 0.8567563573283657 | 0.08787732510386184 | 0.13507058489456872 | 0.8643035171583309 | 1 |

## Comparison boundary

These are matched four-park row-level baseline results. They are more directly comparable to the row-level tabular MLP subset audit than to GRU/LSTM sequence-window evidence, because the GRU and LSTM audits use 24-step sequence windows rather than row-level tabular evaluation.

These results do not replace `data/processed/baseline_metrics.csv`. They must not be merged into the canonical full-dataset benchmark ranking and must not be used to claim model superiority outside this matched subset evaluation space.

## Manuscript-safe wording

"Within the matched four-park row-level baseline run, XGBoost produced the lowest test MAE among the evaluated baseline rows. This finding is local matched-subset evidence and does not alter the repository's canonical full-dataset benchmark table."

"The matched four-park baseline comparison provides a row-level tabular reference for the same selected parks used in the neural subset audits. It can support cautious matched-subset discussion, especially against row-level tabular neural evidence, but it is not a replacement for the canonical full-dataset benchmark."

"The controlled GRU and LSTM sequence audits should remain separated from the row-level tabular comparison unless a sequence-aligned baseline evaluation is added."

## Limitations and next steps

- The run is limited to four selected parks and should not be generalized to the full dataset benchmark.
- The comparison is row-level and tabular; it is not sequence-window aligned with GRU or LSTM evidence.
- The local diagnostics CSVs remain generated outputs under `data/processed/diagnostics/` and are not benchmark authority.
- Next step: integrate this audit into the neural baseline comparison summary only after explicit comparability review.
- Future work: add sequence-aligned baseline evidence if direct GRU/LSTM comparison becomes necessary.

