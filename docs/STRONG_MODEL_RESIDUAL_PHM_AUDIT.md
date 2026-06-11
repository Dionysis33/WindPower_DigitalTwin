# NB21 Strong-Model Residual PHM Diagnostics Audit

## 1. Summary

`notebooks/21_strong_model_residual_phm_diagnostics.ipynb` defines a controlled scaffold for strong-model residual diagnostics after NB20. The notebook is intended to test whether PHM-oriented residual indicators remain informative and become more selective when residuals are produced by a stronger leakage-safe forecasting model instead of the weaker canonical baseline prediction source.

This is a diagnostic validation scaffold only. It is not a new canonical benchmark, not a neural architecture experiment, and not a replacement for the repository benchmark tables.

The refinement pass hardens the scaffold so smoke-mode setup is derived from train and validation only, feature exclusions are explicit, operating-regime bins are validation-derived, warning events are grouped into contiguous candidate events, and exports use NB21-specific filenames.

## 2. Why NB21 Follows NB20

NB20 established a residual diagnostics layer using the canonical `Baseline_Prediction` source. That layer translated forecasting errors into condition-monitoring-oriented indicators such as absolute-error warnings, robust residual z-scores, rolling residual persistence, park-level summaries, and warning events.

NB21 follows NB20 because the next scientific question is whether the diagnostic signal is robust to a stronger residual source. If a stronger model reduces broad residual noise while preserving persistent deviations for specific parks, the PHM interpretation becomes more selective and more defensible.

## 3. Central Research Question

Does a validation-calibrated residual diagnostics layer remain informative, and become more selective, when residuals are computed from a stronger leakage-safe forecasting model trained only on `train_final.csv`?

The expected interpretation boundary is diagnostic evidence of deviation from expected forecast behavior, not confirmed turbine faults.

## 4. Inputs

Required processed split files:

| Input | Role |
|---|---|
| `data/processed/train_final.csv` | train-only source for model and preprocessing fit |
| `data/processed/val_final.csv` | validation source for threshold calibration |
| `data/processed/test_final.csv` | one-time evaluation after threshold policy is fixed |

Required columns:

| Column | Role |
|---|---|
| `Power_Output_Normalized` | forecasting target |
| `park_id` | plant identifier for grouping and park-level diagnostics |
| `timestamp` | temporal ordering for rolling and event diagnostics |

## 5. Leakage Controls

The scaffold applies the following controls:

- Model fitting uses only `train_final.csv`.
- Imputers and encoders are fit only on the training split through a training-fitted preprocessing pipeline.
- Validation residuals define thresholds and any configuration boundary.
- Test residuals are evaluated once only after the validation threshold policy is fixed.
- Test residuals are not used for threshold derivation.
- Smoke-mode park selection uses train and validation only.
- When full diagnostics are disabled, test data is limited to path, schema, and temporal availability audits.
- Feature selection is based on train and validation schema; test schema is recorded for full-run availability checks but does not select features.
- `data/processed/baseline_metrics.csv` is not updated.
- NB21 is not presented as a canonical benchmark.

## 6. Model And Fallback Policy

The preferred residual model is `XGBRegressor` if XGBoost imports successfully in the current environment.

Fallback order:

1. `XGBRegressor`
2. `HistGradientBoostingRegressor`
3. `RandomForestRegressor` as an emergency fallback

The `HistGradientBoostingRegressor` fallback disables internal early stopping for reproducibility. The scaffold does not install packages, edit `requirements.txt`, run hyperparameter search, or select a model using test data.

## 7. Threshold Policy

All warning thresholds are derived from validation residuals only. The scaffold defines:

- residual mean and standard deviation,
- absolute-error q90, q95, and q99,
- residual median and MAD,
- validation rolling MAE-24 q95,
- per-park thresholds where validation support is sufficient,
- global fallback thresholds for sparse parks.

The test split is evaluated only after these thresholds are fixed.

Operating-regime bins follow the same boundary: the regime source column and bin edges are selected from validation data only, and test records are assigned to those validation-derived bins only during a full run.

## 8. Residual And Warning Definitions

Residual records include:

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

Warning rules:

- `abs_error > validation q95`
- `abs(robust_residual_z_score) > 3`
- `rolling_MAE_24 > validation rolling q95`

## 9. Diagnostics Generated

The scaffold defines functions for:

- split and required-column audits,
- feature schema audits,
- train-only preprocessing audits,
- strong-model policy reporting,
- train, validation, and test metric audits,
- train-validation and validation-test MAE gap reporting,
- validation-derived thresholds,
- residual records,
- park-level residual summaries,
- operating-regime summaries when suitable columns exist,
- temporal summaries,
- directional bias summaries,
- warning-event extraction,
- residual persistence and autocorrelation diagnostics,
- metadata and spatial diagnostics when metadata columns exist,
- comparison placeholders against NB20.

Warning-event extraction groups contiguous warning rows by split and park into candidate diagnostic events. Event summaries report start and end timestamps, duration in rows, mean and maximum absolute error, mean residual, maximum rolling MAE-24, and dominant warning reason. These events remain diagnostic candidates, not confirmed faults.

Metadata and spatial summaries use validation metadata under safe defaults. Validation plus test metadata is used only when full diagnostics are enabled and test residuals exist.

## 10. Comparison Boundary Vs NB20

NB20 remains the baseline-residual diagnostic reference. NB21 should be compared to NB20 only after a controlled full run. The comparison should focus on whether stronger-model residuals reduce broad residual noise while preserving interpretable persistent deviations.

The controlled full run on 2026-06-11 records NB21 strong-model residual diagnostics under the NB21 export directory only. The exported `strong_residual_phm_comparison_boundary.csv` remains a boundary table, not a numeric NB20-vs-NB21 comparison table. It explicitly keeps NB20 comparison items in a diagnostic-evidence frame and does not convert warning flags into fault labels.

## 11. Artifact Policy

The scaffold writes no artifacts by default.

When exports are enabled, outputs are limited to:

`data/processed/diagnostics/strong_model_residual_phm/`

Export filenames use the `strong_residual_phm_` prefix. The planned summary exports include run manifest, path audit, split temporal audit, feature audit, preprocessing audit, model policy, model metrics, threshold policy, per-park thresholds, park-level summary, warning-event summary, operating-regime summary, temporal summary, directional-bias summary, residual-persistence summary, metadata/spatial summary, comparison boundary, self-checks, and export audit.

Full residual records are not exported unless `FULL_EXPORT_RESIDUAL_RECORDS=True`. The notebook does not write model binaries, checkpoints, `baseline_metrics.csv`, `requirements.txt`, NB20 notebooks, NB20 audit files, or NB20 diagnostic outputs.

## 12. Scaffold Run Instructions

Committed safe defaults:

```python
SMOKE_MODE = True
RUN_FULL_DIAGNOSTICS = False
EXPORT_RESULTS = False
FULL_EXPORT_RESIDUAL_RECORDS = False
RANDOM_STATE = 42
```

For a controlled full local run:

```python
SMOKE_MODE = False
RUN_FULL_DIAGNOSTICS = True
EXPORT_RESULTS = True
FULL_EXPORT_RESIDUAL_RECORDS = False
```

The full run should be performed only after the scaffold commit, with notebook outputs kept out of version control.

Safe-default execution should not use test data for diagnostic setup beyond path, schema, and temporal availability checks. A full run must be enabled explicitly before test residuals are generated.

## 13. Full-Run Results (2026-06-11)

The controlled full run used:

| Flag | Value |
|---|---:|
| `SMOKE_MODE` | `False` |
| `RUN_FULL_DIAGNOSTICS` | `True` |
| `EXPORT_RESULTS` | `True` |
| `FULL_EXPORT_RESIDUAL_RECORDS` | `False` |
| `RANDOM_STATE` | `42` |

The selected residual source model was `XGBRegressor` with no fallback reason recorded.

### Model Metrics

`strong_residual_phm_model_metrics.csv`:

| Split | Rows | MAE | RMSE | R2 | Status |
|---|---:|---:|---:|---:|---|
| train | 1,982,736 | 0.056222 | 0.101874 | 0.857458 | evaluated |
| validation | 182,998 | 0.050777 | 0.093881 | 0.853504 | evaluated |
| test | 1,086,336 | 0.066216 | 0.114639 | 0.857516 | evaluated |

The metric export records `train_validation_MAE_gap = -0.005445` and `validation_test_MAE_gap = 0.015440`. No separate `strong_residual_phm_overfit_audit.csv` or model-fit-audit CSV is present in the output directory; model-fit review is therefore limited to the gap fields in `strong_residual_phm_model_metrics.csv`.

### Validation-Derived Thresholds

`strong_residual_phm_threshold_policy.csv`:

| residual_mean | residual_std | abs_error_q90 | abs_error_q95 | abs_error_q99 | residual_median | residual_mad | rolling_MAE_24_q95 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| -0.001814 | 0.093863 | 0.139009 | 0.210602 | 0.383183 | -0.004240 | 0.018691 | 0.143057 |

`strong_residual_phm_threshold_per_park.csv` contains 256 parks. Validation support ranges from 191 to 720 rows per park. Across parks, `abs_error_q95` has mean 0.191660, min 0.029381 at park 1550, and max 0.395608 at park 2985. `rolling_MAE_24_q95` has mean 0.122974, min 0.028470 at park 7341, and max 0.233049 at park 1490.

### Park-Level Diagnostics

`strong_residual_phm_park_level_summary.csv` contains 512 rows: 256 validation park summaries and 256 test park summaries.

| Split | Parks | Rows | Mean park MAE | Min park MAE | Max park MAE | Mean park warning rate | Min warning rate | Max warning rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| validation | 256 | 182,998 | 0.050747 | 0.007697 | 0.128171 | 0.210831 | 0.081944 | 0.552778 |
| test | 256 | 1,086,336 | 0.066163 | 0.023573 | 0.120913 | 0.326094 | 0.145285 | 0.543190 |

Highest validation MAE parks were 183, 5792, 2985, 5426, and 1832. Highest test MAE parks were 5792, 5078, 2985, 891, and 4271. Highest test warning-rate parks were 4024, 4271, 3987, 5792, and 5078. These are residual diagnostic rankings only.

### Warning Events

`strong_residual_phm_warning_event_summary.csv` contains 112,651 contiguous candidate warning events.

| Split | Events | Parks | Total duration rows | Mean duration rows | Max duration rows | Mean event abs error | Max abs error |
|---|---:|---:|---:|---:|---:|---:|---:|
| validation | 15,095 | 256 | 38,621 | 2.558529 | 48 | 0.157485 | 0.985002 |
| test | 97,556 | 256 | 354,467 | 3.633472 | 285 | 0.160725 | 0.976800 |

Dominant warning reasons:

| Split | `robust_z_gt_3` | `abs_q95` | `rolling_mae_24_q95` |
|---|---:|---:|---:|
| validation | 12,546 | 1,995 | 554 |
| test | 76,645 | 15,176 | 5,735 |

The longest test event was park 13901 from 2020-02-15 16:00:00 to 2020-02-27 12:00:00 with 285 rows and dominant reason `rolling_mae_24_q95`. This is a candidate residual-warning episode, not a confirmed fault.

### Operating Regimes

`strong_residual_phm_operating_regime_summary.csv` uses validation-derived bins from `Wind_Speed_100m_ms`.

| Split | Regime bin | Rows | MAE | Mean residual | Warning rate |
|---|---|---:|---:|---:|---:|
| validation | `(-inf, 2.656]` | 45,750 | 0.020334 | -0.001146 | 0.062492 |
| validation | `(2.656, 5.225]` | 45,749 | 0.034417 | -0.000401 | 0.116112 |
| validation | `(5.225, 8.228]` | 45,749 | 0.054426 | -0.002726 | 0.217273 |
| validation | `(8.228, inf]` | 45,750 | 0.093930 | -0.002983 | 0.448306 |
| test | `(-inf, 2.656]` | 205,112 | 0.020754 | -0.000790 | 0.072190 |
| test | `(2.656, 5.225]` | 229,088 | 0.037860 | 0.000647 | 0.153723 |
| test | `(5.225, 8.228]` | 255,026 | 0.062969 | 0.000426 | 0.305090 |
| test | `(8.228, inf]` | 397,110 | 0.108142 | 0.000126 | 0.570718 |

### Temporal Diagnostics

`strong_residual_phm_temporal_summary.csv` contains 193 month-hour groups. Test has 168 groups and validation has 25 groups. Test group-level MAE ranges up to 0.106833 and warning rate ranges up to 0.584605. The highest test warning rates occur in February midday and afternoon groups, with the top group at month 2, hour 11: MAE 0.102637 and warning rate 0.584605.

### Directional Bias

`strong_residual_phm_directional_bias_summary.csv` contains 512 park-split rows.

| Split | Parks | Mean of park mean residuals | Min park mean residual | Max park mean residual | Mean positive residual rate |
|---|---:|---:|---:|---:|---:|
| validation | 256 | -0.001868 | -0.020391 | 0.020145 | 0.374533 |
| test | 256 | 0.000085 | -0.017678 | 0.028904 | 0.404930 |

The largest positive test mean residual is park 7374 at 0.028904. The most negative test mean residual is park 891 at -0.017678.

### Residual Persistence

`strong_residual_phm_residual_persistence_summary.csv` contains 512 park-split rows.

| Split | Parks | Mean residual lag-1 autocorr | Min residual lag-1 autocorr | Max residual lag-1 autocorr | Mean abs-error lag-1 autocorr | Mean rolling MAE-24 | Max rolling MAE-72 |
|---|---:|---:|---:|---:|---:|---:|---:|
| validation | 256 | -0.073634 | -0.383709 | 0.320956 | 0.446195 | 0.050887 | 0.410507 |
| test | 256 | -0.072004 | -0.213625 | 0.176110 | 0.434354 | 0.066121 | 0.463569 |

### Metadata And Spatial Summary

`strong_residual_phm_metadata_spatial_summary.csv` contains 256 parks. Across parks, mean MAE is 0.058455, min MAE is 0.017048, max MAE is 0.121133, mean warning rate is 0.268462, min warning rate is 0.132979, and max warning rate is 0.472436. The top metadata/spatial MAE parks are 5792, 2985, 5426, 183, and 5078. The coordinate coverage spans latitude 47.375 to 55.000 and longitude 6.000 to 14.9375.

### Self-Checks And Export Audit

`strong_residual_phm_self_checks.csv` records 10 checks, all passed:

- `smoke_requires_no_full_run`
- `no_full_residual_export_by_default`
- `test_not_used_in_default_work_subset`
- `no_split_provenance_features`
- `no_model_checkpoint_target`
- `baseline_metrics_not_planned`
- `requirements_not_planned`
- `export_dir_is_nb21_only`
- `all_planned_exports_use_nb21_prefix`
- `exactly_one_test_evaluation_path_when_full`

`strong_residual_phm_export_audit.csv` records 19 planned paths, all with `will_write=True`, and zero full residual record exports. The output directory therefore contains only summary/audit CSVs and no residual-row dump.

## 14. Manuscript-Safe Interpretation Boundary

NB21 may support the manuscript by showing whether forecast residual diagnostics remain useful under a stronger residual source. The safe claim is that validation-calibrated residual indicators identify systematic deviations from expected forecast behavior.

Without fault labels, warning flags are not confirmed failures, not fault diagnoses, and not maintenance prescriptions.

## 15. What This Does Not Claim

NB21 does not claim:

- a deployed PHM system,
- confirmed turbine faults,
- a new canonical forecasting benchmark,
- superiority selected from test data,
- a neural architecture contribution,
- package or dependency changes,
- replacement of NB20 artifacts.
