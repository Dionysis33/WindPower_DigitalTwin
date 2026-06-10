# NB20 Residual PHM Diagnostics Audit

## 1. Summary

`notebooks/20_residual_phm_diagnostics.ipynb` defines a controlled forecasting-based residual diagnostics experiment for the WindPower_DigitalTwin manuscript. It uses canonical train/validation/test processed splits and converts forecast residual behavior into condition-monitoring-oriented evidence.

The experiment is a diagnostic interpretation layer on top of forecasting outputs. It does not introduce a new neural architecture, does not replace the canonical benchmark, and does not claim a deployed PHM or production monitoring system.

Full empirical NB20 diagnostics have not yet been executed in this scaffold commit; result tables are generated only during local full-run execution.

## 2. Motivation From Literature

The local literature is used only as conceptual motivation and not as an executable dependency.

- `literature_local/papers/08_Gijon_2025_Hybrid_Explainable_Betz_Limit_Constraint.pdf` motivates residual modeling, explainability, uncertainty, and interpretation of deviations between predicted and observed wind power.
- `literature_local/papers/30_Dhungana_2025_Wind_Power_Forecasting_ML_vs_DL.pdf` motivates the connection between wind-power forecasting, condition monitoring, decision-making, and maintenance planning.
- A local Zou/outlier review PDF, when present, motivates the importance of abnormal or outlier operating data because such observations can bias wind-turbine and wind-farm models.
- `literature_local/papers/18_Vogt_2022_Synthetic_Wind_Dataset_273_Germany.pdf`, when present, motivates the DaKS/Kassel synthetic wind dataset context with many geographically distributed wind plants.
- `literature_local/papers/03_Pessoa_2025_Mamba_Uncertainty_ProbTSF.pdf` is used only to motivate uncertainty-aware forecasting as support for forecast-confidence interpretation. NB20 does not implement Mamba.

## 3. Purpose And PHM Boundary

The purpose is to strengthen the manuscript connection to prognostics and health management by showing how forecast residuals can support condition-monitoring interpretation.

NB20 treats persistent residuals as early-warning indicators and as evidence of persistent deviation from expected forecast behavior. These signals are not labeled faults. No ground-truth fault labels are available. Therefore, the analysis is diagnostic/early-warning evidence, not fault diagnosis.

The word diagnostic in this notebook means forecasting-based residual diagnostics. It does not mean confirmed fault diagnosis, a deployed PHM system, or a production monitoring system.

## 4. Data Inputs

Required canonical inputs:

| Input | Role |
|---|---|
| `data/processed/train_final.csv` | train-only source for optional fallback model fitting |
| `data/processed/val_final.csv` | validation source for prediction audit and threshold derivation |
| `data/processed/test_final.csv` | one-time test evaluation and residual interpretation |

Required columns:

| Column | Role |
|---|---|
| `Power_Output_Normalized` | forecasting target |
| `park_id` | plant identifier, normalized as zero-padded string |
| `timestamp` | time index for rolling and event extraction |

Optional metadata and regime columns include location, turbine metadata, NWP forecast horizon, U/V wind-vector fields, weather variables, and lagged wind/vector columns when available.

## 5. Prediction Source Policy

NB20 resolves predictions in this order:

1. Inspect `val_final.csv` and `test_final.csv` for usable prediction columns: `Baseline_Prediction`, `prediction`, `y_pred`, `predicted`, or `model_prediction`.
2. Reject direct prediction columns if they are constant in validation or test.
3. Reject direct prediction columns if `prediction_equals_target_rate > 0.99` in validation or test.
4. If usable validation and test prediction columns pass these checks, use them directly.
5. If validation predictions are missing or all direct prediction columns fail sanity checks, train a controlled diagnostic fallback model using only `train_final.csv`. The fallback prefers XGBoost if available, otherwise `HistGradientBoostingRegressor`.
6. If validation predictions are missing but test prediction CSVs exist, use those CSVs only for optional model-comparison residual tables. Test residuals are not used to derive thresholds.
7. The fallback model exists only to generate leakage-safe residuals for PHM-oriented interpretation. It is not a new canonical benchmark.

The current repository schema includes `Baseline_Prediction` in the canonical splits, so the default prediction source is expected to be `canonical_split_column:Baseline_Prediction`.

## 5A. Prediction Provenance Audit

NB20 records prediction provenance in `prediction_source_audit_df` using:

- `prediction_provenance_status`,
- `prediction_provenance_note`,
- `rejection_reasons`,
- `constant_prediction_check`,
- `prediction_equals_target_rate`,
- `prediction_equals_target_suspicious_check`.

For canonical split columns, NB20 treats the values as upstream canonical predictions. It does not retrain, overwrite, or alter canonical benchmark files. Optional prediction CSVs remain model-comparison inputs only and are not used to derive residual thresholds.

If all direct prediction columns fail validation/test sanity checks, the selected source becomes the controlled diagnostic fallback model. That fallback is documented as diagnostic-only residual generation and not as a canonical benchmark.

## 5B. Fallback Overfitting And Underfitting Audit

When the controlled diagnostic fallback model is used, NB20 creates a train/validation/test audit for the selected fallback configuration.

The audit reports:

- train MAE/RMSE/R2,
- validation MAE/RMSE/R2,
- test MAE/RMSE/R2,
- `train_validation_gap_MAE`,
- `validation_test_gap_MAE`.

This table is intended only to detect obvious overfitting or underfitting in the diagnostic residual generator. It is not a canonical benchmark table and does not update `baseline_metrics.csv`.

## 6. Leakage-Safe Threshold Policy

All warning thresholds are derived from validation residuals only. The test split is evaluated once after thresholds are fixed.

Thresholds include:

| Threshold Family | Source |
|---|---|
| global residual mean/std | validation residuals |
| global absolute-error quantiles at 0.90, 0.95, 0.99 | validation residuals |
| per-park thresholds where enough validation rows exist | validation residuals |
| global fallback thresholds for sparse parks | validation residuals |
| robust z-score median/MAD parameters | validation residuals |
| rolling MAE-24 q95 threshold | validation rolling residuals |

No test-based threshold derivation is allowed. No test-based model selection is allowed.

## 6A. Threshold Calibration Sanity Checks

NB20 now includes a threshold calibration sanity table that reports, using validation-derived thresholds only:

- validation absolute-error q90/q95/q99 thresholds,
- expected validation exceedance rates for q90/q95/q99,
- actual validation exceedance rates,
- actual test exceedance rates,
- robust z-score warning rates on validation and test,
- rolling MAE warning rates on validation and test,
- combined warning rates on validation and test.

This section exists to make the calibration-transfer boundary visible: validation residuals calibrate warning rules, while test residuals are interpreted after those rules are fixed.

## 7. Residual Definitions

For validation and test predictions, NB20 constructs:

| Field | Definition |
|---|---|
| `y_true` | observed normalized power |
| `y_pred` | selected prediction source |
| `residual` | `y_true - y_pred` |
| `abs_error` | absolute residual |
| `squared_error` | squared residual |
| `residual_sign` | observed above, below, or equal to prediction |
| `residual_z_score` | standard residual score using validation-derived mean/std with epsilon protection |
| `robust_residual_z_score` | robust residual score using validation-derived median/MAD |
| `warning_flag` | manuscript-facing alias for the combined residual warning flag |

Residuals are interpreted as deviations from expected forecast behavior.

## 7A. Residual Column Contract

The enriched NB20 notebook includes a dedicated residual column contract audit for validation and test residual records.

Required manuscript-facing residual columns include:

- `park_id`
- `timestamp`
- `y_true`
- `y_pred`
- `residual`
- `abs_error`
- `squared_error`
- `residual_sign`
- `residual_z_score`
- `robust_residual_z_score`
- `rolling_MAE_24`
- `rolling_MAE_72`
- `rolling_bias_24`
- `rolling_bias_72`
- `warning_abs_q95`
- `warning_robust_z`
- `warning_rolling_mae_24`
- `warning_flag`
- `warning_reason`

The notebook may keep internal aliases such as `robust_z` and `warning_any`, but exported and manuscript-facing residual records expose `robust_residual_z_score` and `warning_flag`.

## 8. Rolling Diagnostic Indicators

Rolling indicators are computed independently per `park_id`, after sorting by timestamp:

- `rolling_MAE_24`
- `rolling_MAE_72`
- `rolling_bias_24`
- `rolling_bias_72`
- `rolling_RMSE_24`
- `rolling_RMSE_72`

The rolling layer supports early-warning indicators by identifying persistent residual elevation or bias, rather than isolated single-row errors.

## 8A. Directional Bias Diagnostics

NB20 adds directional residual summaries by split and by park:

- underprediction rate, defined as `residual > 0`,
- overprediction rate, defined as `residual < 0`,
- near-zero residual rate using `abs(residual) <= 0.01`,
- mean residual,
- median residual,
- warning rate.

This allows manuscript text to distinguish systematic directional bias from high absolute error. When exports are enabled, the table is written as `residual_phm_directional_bias_summary.csv`.

## 8B. Temporal Residual Diagnostics

NB20 derives temporal fields from `timestamp` when available:

- hour,
- day of week,
- month,
- quarter,
- season.

Residual metrics are summarized by hour, month, quarter, and season, including row count, MAE, RMSE, mean residual, p95 absolute error, and warning rate. These diagnostics support cautious discussion of temporal residual stress without changing threshold policy.

When exports are enabled, the temporal summary is written as `residual_phm_temporal_summary.csv`. Optional exported figures are:

- `temporal_warning_rate_by_hour.png`
- `temporal_abs_error_by_month.png`

## 8C. Residual Persistence And Autocorrelation Diagnostics

NB20 adds test-set persistence diagnostics per park:

- lag-1 residual autocorrelation,
- lag-24 residual autocorrelation when enough rows exist,
- lag-72 residual autocorrelation when enough rows exist,
- longest same-sign residual run,
- longest warning run,
- warning-event count,
- warning rate.

This strengthens the PHM early-warning argument because persistent deviations are more diagnostically meaningful than isolated residual spikes. When exports are enabled, the table is written as `residual_phm_residual_persistence_summary.csv`.

## 9. Warning-Event Extraction

Warning rows are created when at least one validation-calibrated condition is met:

- `abs_error > validation q95`
- `abs(robust_z) > 3`
- `rolling_MAE_24 > validation rolling q95`

Contiguous warning rows are grouped into warning events per park. NB20 now infers the common per-park timestamp interval when possible and breaks events when timestamp gaps exceed an inferred interval tolerance. This prevents separated warning clusters from being merged across missing-time gaps.

Event summaries include start/end timestamps, row duration, inferred-hour duration when possible, whether timestamp-gap breaks were used, maximum and mean absolute error, maximum rolling MAE-24, mean residual, dominant warning reason, target mean, prediction mean, and available regime information.

Timestamp-aware event fields include:

- `event_start`,
- `event_end`,
- `duration_rows`,
- `duration_hours_if_inferable`,
- `timestamp_gap_breaks_used`.

Warning events indicate persistent deviation from expected forecast behavior. They are not labeled faults.

## 9A. Warning Event Severity Ranking

NB20 adds a candidate-event severity score:

`severity_score = duration_rows * mean_abs_error * (1 + abs(mean_residual))`

Warning events are ranked by severity score, duration, maximum absolute error, and maximum rolling MAE-24. The ranking is intended to prioritize candidate diagnostic events for manuscript interpretation. It does not label or confirm faults.

When exports are enabled, the top event table is written as `residual_phm_top_warning_events.csv`.

## 10. Park-Level Diagnostic Summary

NB20 creates a test-set park-level summary with:

- row count,
- MAE, RMSE, R2,
- mean and median residual,
- median and p95 absolute error,
- residual standard deviation,
- warning count and warning rate,
- event count and longest event duration,
- mean target and mean prediction,
- available latitude, longitude, hub height, rotor diameter, and nominal power.

Parks are ranked by descending MAE, descending warning rate, and descending absolute mean residual. This ranking supports manuscript discussion of difficult parks and residual stress concentration.

## 10A. Park Metadata Relationship Diagnostics

When park metadata are available, NB20 computes descriptive correlations between metadata and park-level residual metrics.

Metadata considered:

- latitude,
- longitude,
- hub height,
- rotor diameter,
- nominal power or capacity.

Residual metrics considered:

- MAE,
- warning rate,
- absolute mean residual,
- event count,
- longest event duration.

These correlations are descriptive only and make no causal claim. When exports are enabled, the table is written as `residual_phm_metadata_correlation_summary.csv`. If enough metadata are available, `metadata_vs_warning_rate.png` can also be exported.

## 11. Operating-Regime Diagnostic Summary

The operating-regime analysis bins residuals by available operating context:

- target power bin,
- predicted power bin,
- NWP forecast horizon bin,
- wind-speed bin,
- temperature bin.

For each regime, NB20 computes row count, MAE, RMSE, mean residual, p95 absolute error, and warning rate. This supports manuscript language such as: residual stress was concentrated in high-output or transition operating regimes.

The analysis is descriptive. It does not make causal claims.

## 12. Optional Model-Comparison Residual Summary

If compatible NB06/NB07 prediction CSVs are available, NB20 computes model-level residual summaries for existing prediction files, including XGBoost, Random Forest, MLP, and any available baseline rows.

This section is optional and fail-safe. It does not use test predictions to derive thresholds, select models, or update canonical metrics.

## 13. Generated Local-Only Artifacts

When `EXPORT_RESULTS=True`, outputs are written under:

`data/processed/diagnostics/residual_phm_diagnostics/`

Expected CSV outputs:

- `residual_phm_run_manifest.csv`
- `residual_phm_path_audit.csv`
- `residual_phm_prediction_source_audit.csv`
- `residual_phm_threshold_policy.csv`
- `residual_phm_overall_metrics.csv`
- `residual_phm_park_level_summary.csv`
- `residual_phm_top_diagnostic_parks.csv`
- `residual_phm_warning_event_summary.csv`
- `residual_phm_operating_regime_summary.csv`
- `residual_phm_directional_bias_summary.csv`
- `residual_phm_temporal_summary.csv`
- `residual_phm_residual_persistence_summary.csv`
- `residual_phm_top_warning_events.csv`
- `residual_phm_metadata_correlation_summary.csv`
- `residual_phm_model_comparison.csv`, when compatible prediction CSVs are available
- `residual_phm_test_residual_records_sample.csv`

Expected figure directory:

`data/processed/diagnostics/residual_phm_diagnostics/figures/`

Expected figures:

- `residual_distribution_validation_test.png`
- `park_level_mae_top20.png`
- `park_level_warning_rate_top20.png`
- `rolling_residual_top3_parks.png`
- `warning_event_timeline_top3_parks.png`
- `operating_regime_abs_error.png`
- `residual_vs_predicted_power.png`
- `spatial_residual_map_if_latlong.png`, when latitude/longitude are available
- `temporal_warning_rate_by_hour.png`, when exports are enabled and temporal summaries are available
- `temporal_abs_error_by_month.png`, when exports are enabled and temporal summaries are available
- `metadata_vs_warning_rate.png`, when enough metadata are available

The notebook does not write model binaries, checkpoints, `requirements.txt`, or `data/processed/baseline_metrics.csv`.

## 13A. Manuscript Table And Figure Readiness

NB20 now includes a manuscript table builder that creates compact table objects during execution:

- Table A: overall validation/test residual metrics,
- Table B: top diagnostic parks by MAE,
- Table C: top diagnostic parks by warning rate,
- Table D: top warning events by severity,
- Table E: high-error operating-regime summary.

The notebook also includes figure caption drafts for residual distributions, park rankings, rolling residuals, warning-event timelines, operating-regime residuals, residual-vs-predicted-power plots, spatial diagnostics, temporal diagnostics, and metadata relationship diagnostics.

These table and caption sections are scaffolded for manuscript writing. They are populated with empirical values only when the notebook is executed locally.

## 14. Manuscript Interpretation

NB20 supports PHM-oriented interpretation through residual behavior. Persistent residuals are treated as condition-monitoring indicators and early-warning indicators.

Manuscript-safe wording:

- forecasting-based residual diagnostics,
- condition-monitoring-oriented evidence,
- early-warning indicators,
- operating-regime mismatch,
- persistent deviation from expected forecast behavior.

The results can support a paper section on residual analysis, park-level diagnostic ranking, regime-dependent residual stress, rolling warning indicators, warning-event extraction, and optional model-comparison residual interpretation.

## 15. Limitations

The analysis has no ground-truth fault labels. It cannot validate whether a warning event corresponds to a physical turbine or park fault.

Thresholds are empirical and validation-derived. They are useful for controlled manuscript diagnostics but are not a certified monitoring rule.

Residuals may reflect weather-regime mismatch, forecast horizon effects, sensor or data quality issues, model bias, underrepresented operating states, or other unobserved factors. NB20 does not distinguish these causes without additional evidence.

## 16. What This Does Not Claim

NB20 does not claim confirmed faults.

NB20 does not claim fault diagnosis.

NB20 does not claim a deployed PHM system or production monitoring system.

NB20 does not claim state-of-the-art superiority.

NB20 does not replace the canonical benchmark or `baseline_metrics.csv`.

NB20 does not create a canonical benchmark replacement.

NB20 does not treat residual events as labeled failures. Results are local-only until specific figures or tables are selected for the manuscript.
