# XGBoost small-grid tuning audit

Σκοπός: μικρό, reproducible tuning audit για το XGBoost baseline στο τρέχον manuscript-upgrade experiment branch, χωρίς αλλαγή notebooks και χωρίς αντικατάσταση του canonical benchmark artifact.

## Inputs

- Train split: `data/processed/train_final.csv`
- Validation split: `data/processed/val_final.csv`
- Test split: `data/processed/test_final.csv`
- Target column: `Power_Output_Normalized`

## Feature contract

- Αναπαράγεται το NB07 contract.
- Εξαιρούνται: `Power_Output_Normalized`, `park_id`, `timestamp`, `test_flag`, `Baseline_Prediction`.
- Χρησιμοποιούνται μόνο train-inferred numeric feature columns.
- Δεν γίνεται encoding του `turbine` ή άλλων non-numeric columns.
- Δεν γίνεται scaling, επειδή το XGBoost NB07 baseline δεν χρησιμοποιεί scaling.

## Tuning contract

- Train only on `train_final.csv`.
- Hyperparameter selection only on `val_final.csv`.
- Test evaluation μία φορά, μόνο για το selected validation configuration.
- Selection rule: validation MAE ascending, validation RMSE ascending, validation R2 descending.
- Το `data/processed/baseline_metrics.csv` δεν γίνεται overwrite.
- Δεν γράφονται model binaries ή checkpoints.

## Grid

Το full run αξιολογεί 8 configurations:

- `n_estimators`: `400`, `500`
- `max_depth`: `6`, `8`
- `learning_rate`: `0.03`, `0.05`
- `subsample`: `0.8`
- `colsample_bytree`: `0.8`

Base settings: `objective="reg:squarederror"`, `random_state=SEED`, `n_jobs=-1`, `tree_method="hist"`.

## Outputs

Full run outputs:

- `data/processed/diagnostics/baseline_tuning/xgboost_small_grid_validation.csv`
- `data/processed/diagnostics/baseline_tuning/xgboost_small_grid_selected_test_metrics.csv`
- `data/processed/diagnostics/baseline_tuning/xgboost_small_grid_run_manifest.csv`

Smoke/capped runs γράφουν ξεχωριστά prefixed outputs και έχουν `run_mode=smoke` ή `run_mode=capped`. Αυτά είναι μόνο code-validation outputs και δεν αποτελούν manuscript evidence.

Τα generated CSVs μένουν local-only κάτω από `data/processed/**` και δεν αντικαθιστούν το `baseline_metrics.csv`.

## Full-run result summary

Selected validation configuration:

- `config_id`: `3`
- `n_estimators`: `400`
- `max_depth`: `8`
- `learning_rate`: `0.03`
- `subsample`: `0.8`
- `colsample_bytree`: `0.8`

| Model / artifact | Validation MAE | Validation RMSE | Validation R2 | Test MAE | Test RMSE | Test R2 | Χρήση |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Selected tuned XGBoost small-grid run | `0.050490` | `0.093525` | `0.854611` | `0.065765` | `0.113958` | `0.859204` | Reproducible tuning audit |
| Existing canonical XGBoost baseline (`baseline_metrics.csv`) | n/a | n/a | n/a | `0.065750` | `0.113494` | `0.860348` | Benchmark row |

Το small validation-selected XGBoost tuning run δεν βελτίωσε το existing canonical XGBoost baseline στο test split. Η διαφορά είναι μικρή, αλλά τα test metrics του tuned configuration είναι ελαφρώς χειρότερα σε MAE, RMSE και R2 από το tracked `baseline_metrics.csv`. Επομένως το existing XGBoost baseline παραμένει το benchmark row. Το tuning run παραμένει χρήσιμο ως reproducible sensitivity/tuning audit και όχι ως benchmark replacement. Δεν τεκμηριώνεται model-performance improvement, τα full-run CSVs παραμένουν local-only generated outputs κάτω από `data/processed/**` και δεν είναι committed, και το `baseline_metrics.csv` δεν έγινε overwrite.

## Commands

Smoke test:

```powershell
python -B scripts/tune_xgboost_small_grid.py --smoke
```

Full run:

```powershell
python -B scripts/tune_xgboost_small_grid.py
```

## Manuscript boundary

Μόνο το full run χωρίς row caps μπορεί να εξεταστεί ως manuscript-usable evidence, μετά από έλεγχο των outputs. Το smoke mode και τα capped runs επιβεβαιώνουν μόνο ότι ο κώδικας τρέχει. Το audit δεν διεκδικεί model-performance improvement από μόνο του και δεν αλλάζει το canonical benchmark protocol.
