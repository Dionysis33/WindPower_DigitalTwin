# NB19 PatchTST Sequence Subset Audit

## Summary

Το `notebooks/19_patchtst_sequence_subset.ipynb` ορίζει ένα ελεγχόμενο sequence experiment για τέσσερα σταθερά επιλεγμένα αιολικά πάρκα. Το experiment συγκρίνει δύο sequence-aligned μοντέλα πάνω στο ίδιο tensor συμβόλαιο `[n_windows, 24, 41]`:

- Flattened-window XGBoost.
- Pure PyTorch PatchTST-Lite Transformer.

Το audit είναι scaffold-first. Τα προεπιλεγμένα flags δεν εκτελούν training, test evaluation ή exports. Τα αποτελέσματα που θα συμπληρωθούν μετά από χειροκίνητο full local run είναι local-only diagnostics και δεν αντικαθιστούν το canonical full benchmark.

## Purpose And Scope

Σκοπός είναι να προστεθεί ένα δυνατό, reproducible και manuscript-safe sequence experiment μετά τα GRU, LSTM και TCN sequence subset notebooks. Το scope περιορίζεται στο controlled four-park subset με τα ίδια canonical splits, ίδιο lookback και ίδιο feature/scaling contract.

Δεν γίνεται χρήση εξωτερικού PatchTST package ή state-space/CUDA build dependency. Το PatchTST-Lite υλοποιείται μόνο με PyTorch primitives.

## Data Protocol

| Πεδίο | Τιμή |
|---|---|
| Notebook | `notebooks/19_patchtst_sequence_subset.ipynb` |
| Train split | `data/processed/train_final.csv` |
| Validation split | `data/processed/val_final.csv` |
| Test split | `data/processed/test_final.csv` |
| Selected parks | `00183`, `00198`, `00303`, `00427` |
| Target | `Power_Output_Normalized` |
| LOOKBACK_STEPS | `24` |
| Expected input shape | `[batch, 24, 41]` |
| Target horizon | αμέσως επόμενο target timestep |

## Feature/Scaling Contract

- Τα learned features προκύπτουν μόνο από το train subset.
- Χρησιμοποιούνται μόνο numeric feature columns.
- Αναμενόμενο πλήθος learned features: `41`.
- Εξαιρούνται: `Power_Output_Normalized`, `timestamp`, `park_id`, `test_flag`, `Baseline_Prediction`, `turbine`.
- Δεν γίνεται turbine encoding.
- Το `StandardScaler` γίνεται fit μόνο στο train subset.
- Το ίδιο scaler εφαρμόζεται σε validation και test.
- Ο στόχος παραμένει unscaled.

## Gap-Safe Sequence Window Contract

Για κάθε split και κάθε park ανεξάρτητα:

1. Οι γραμμές ταξινομούνται κατά `park_id` και `timestamp`.
2. Η χρονοσειρά σπάει σε segments όταν υπάρχει timestamp gap.
3. Κάθε window χρησιμοποιεί τα προηγούμενα `24` timesteps ως X.
4. Το y είναι το αμέσως επόμενο target timestep.
5. Δεν επιτρέπονται windows που περνούν park boundaries, split boundaries ή timestamp gaps.

Το notebook παράγει window audit table με columns:

| split | park_id | segment_id | segment_start_timestamp | segment_end_timestamp | segment_rows | lookback_steps | windows |
|---|---|---:|---|---|---:|---:|---:|
| pending | pending | pending | pending | pending | pending | 24 | pending |

## Flattened-Window XGBoost

Το XGBoost λαμβάνει το ίδιο sequence tensor `[n_windows, 24, 41]` και το μετατρέπει μόνο στο τελευταίο βήμα σε flattened matrix `[n_windows, 984]`.

Validation-only grid:

| Hyperparameter | Values |
|---|---|
| `n_estimators` | `300`, `500` |
| `max_depth` | `4`, `6` |
| `learning_rate` | `0.03`, `0.05` |
| `subsample` | `0.8` |
| `colsample_bytree` | `0.8` |

Ranking policy:

| Rank key | Direction |
|---|---|
| `MAE` | ascending |
| `RMSE` | ascending |
| `R2` | descending |

## PatchTST-Lite

Το PatchTST-Lite είναι pure PyTorch regression model με input `[batch, 24, 41]` και output `[batch, 1]`.

Αρχική αρχιτεκτονική:

| Πεδίο | Τιμή |
|---|---:|
| `PATCH_LEN` | 4 |
| `PATCH_STRIDE` | 2 |
| `D_MODEL` | 64 |
| `N_HEADS` | 4 |
| `N_LAYERS` | 2 |
| `DROPOUT` | 0.1 |
| `BATCH_SIZE` | 512 |
| `LEARNING_RATE` | 0.001 |
| `WEIGHT_DECAY` | 1e-5 |
| `EPOCHS_REQUESTED` | 30 |
| `EARLY_STOPPING_PATIENCE` | 5 |

Η υλοποίηση περιλαμβάνει patchify στο time dimension, linear patch projection, positional embedding, `nn.TransformerEncoder` και regression head.

## Validation-Only Selection Policy

Η επιλογή configuration/model state γίνεται μόνο στο validation split. Η σειρά ranking είναι:

1. MAE ascending.
2. RMSE ascending.
3. R2 descending.

Το test split δεν χρησιμοποιείται για επιλογή υπερπαραμέτρων, early stopping ή model state.

## One-Time Test Evaluation Policy

Το test evaluation εκτελείται μόνο αν `RUN_TEST_EVALUATION=True` και υπάρχει validation-selected configuration/state στη μνήμη.

Για κάθε μοντέλο, το selected validation αποτέλεσμα αξιολογείται ακριβώς μία φορά στο test subset. Δεν γίνεται test-driven model selection.

## Local-Only Output Policy

Τα exports είναι απενεργοποιημένα από προεπιλογή. Αν `EXPORT_RESULTS=True`, τα CSVs γράφονται μόνο κάτω από:

`data/processed/diagnostics/nn_sequence_subset_patchtst/`

Αναμενόμενα local-only CSV exports:

- `nn_sequence_subset_patchtst_run_manifest.csv`
- `nn_sequence_subset_patchtst_window_audit.csv`
- `nn_sequence_subset_patchtst_xgboost_validation_metrics.csv`
- `nn_sequence_subset_patchtst_xgboost_selected_test_metrics.csv`
- `nn_sequence_subset_patchtst_training_history.csv`
- `nn_sequence_subset_patchtst_validation_metrics.csv`
- `nn_sequence_subset_patchtst_selected_test_metrics.csv`

Το `data/processed/baseline_metrics.csv` δεν ενημερώνεται. Δεν γράφονται checkpoints ή binary model files. Τα generated CSVs παραμένουν local-only και δεν πρέπει να γίνουν commit.

## Window Counts

| Split | Windows | Notes |
|---|---:|---|
| train | pending | fill after full local run |
| validation | pending | fill after full local run |
| test | pending | fill after full local run |

## XGBoost Validation Metrics

| validation_rank | config_id | n_estimators | max_depth | learning_rate | subsample | colsample_bytree | MAE | RMSE | R2 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |

## XGBoost Selected Test Metrics

| model | config_id | test_evaluations | MAE | RMSE | R2 |
|---|---:|---:|---:|---:|---:|
| Flattened-window XGBoost | pending | pending | pending | pending | pending |

## PatchTST Training History Summary

| model_id | best_epoch | best_val_loss_mse | epochs_ran | train_windows_used | val_windows_used |
|---|---:|---:|---:|---:|---:|
| pending | pending | pending | pending | pending | pending |

## PatchTST Validation Metrics

| validation_rank | model | model_id | best_epoch | MAE | RMSE | R2 |
|---:|---|---|---:|---:|---:|---:|
| pending | PatchTST-Lite Transformer | pending | pending | pending | pending | pending |

## PatchTST Selected Test Metrics

| model | model_id | test_evaluations | MAE | RMSE | R2 |
|---|---|---:|---:|---:|---:|
| PatchTST-Lite Transformer | pending | pending | pending | pending | pending |

## Manuscript Interpretation Boundary

Το NB19 παρέχει controlled four-park subset evidence μόνο για τα parks `00183`, `00198`, `00303` και `00427`. Δεν αποτελεί αντικατάσταση του canonical full benchmark και δεν πρέπει να συγχωνευθεί στο `data/processed/baseline_metrics.csv`.

Πριν υπολογιστούν και ελεγχθούν πραγματικά metrics, δεν τεκμηριώνεται ισχυρισμός υπεροχής για το XGBoost, το PatchTST-Lite ή οποιαδήποτε άλλη sequence architecture. Το πείραμα είναι χρήσιμο ως reproducible matched-subset sequence evidence και ως βάση για μελλοντικό full benchmark follow-up.
