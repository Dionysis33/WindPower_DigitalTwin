# NB16 LSTM Sequence Subset Audit

## Summary

This document records the completed local controlled LSTM subset run from `notebooks/16_nn_lstm_sequence_subset.ipynb`.

The run is completed local controlled four-park LSTM subset evidence only. It is not a full-dataset benchmark replacement, does not update `data/processed/baseline_metrics.csv`, and should not be used alone to claim model superiority or performance improvement.

## Run Configuration

| Field | Value |
|---|---:|
| model | PyTorch LSTM sequence baseline |
| selected parks | 00183, 00198, 00303, 00427 |
| seed | 42 |
| device | cpu |
| lookback_steps | 24 |
| hidden_size | 64 |
| LSTM layers | 1 |
| dropout | 0.0 |
| learning_rate | 0.001 |
| weight_decay | 1e-5 |
| batch_size | 512 |
| epochs requested | 30 |
| early stopping patience | 5 |
| best_epoch | 6 |
| best_val_loss_mse | 0.02208613018751487 |
| numeric features | 41 |

## Window Counts

| Split | Windows | Segments |
|---|---:|---:|
| train | 30988 | 12 |
| validation | 2784 | 4 |
| test | 16892 | 12 |

## Metrics

| Split | MAE | RMSE | R2 |
|---|---:|---:|---:|
| validation | 0.0944957135017893 | 0.14861402980949204 | 0.7869140109636205 |
| test | 0.10342178818174555 | 0.15506761498343793 | 0.8216890043240139 |

The test set was evaluated once after validation-selected state selection (`test_evaluations = 1`).

## Local-Only Outputs

The following CSVs were written under `data/processed/diagnostics/nn_lstm_sequence_subset/`:

- `data/processed/diagnostics/nn_lstm_sequence_subset/nn_lstm_sequence_subset_lstm_run_manifest.csv`
- `data/processed/diagnostics/nn_lstm_sequence_subset/nn_lstm_sequence_subset_lstm_selected_test_metrics.csv`
- `data/processed/diagnostics/nn_lstm_sequence_subset/nn_lstm_sequence_subset_lstm_training_history.csv`
- `data/processed/diagnostics/nn_lstm_sequence_subset/nn_lstm_sequence_subset_lstm_validation_metrics.csv`
- `data/processed/diagnostics/nn_lstm_sequence_subset/nn_lstm_sequence_subset_lstm_window_audit.csv`

These CSVs are ignored/local-only and should not be committed.

## Safety/Reproducibility Notes

- Feature columns are inferred from the train split only.
- `StandardScaler` is fit only on train subset feature rows and then applied to validation and test.
- The target `Power_Output_Normalized` remains unscaled.
- The `turbine` column is not encoded and is not used as a learned feature.
- Sequence windows are gap-safe and do not cross park, split, or timestamp-gap boundaries.
- The selected model state is chosen by validation loss only.
- The test split is evaluated once after validation-selected state selection.
- No checkpoints or model binaries were written.
- Generated CSV outputs are ignored/local-only under `data/processed/diagnostics/nn_lstm_sequence_subset/`.

## Manuscript Boundary

This run can be cited as controlled subset neural evidence for the LSTM sequence scaffold.

It cannot replace the canonical full-dataset benchmark metrics, and no superiority claim should be made without reviewed comparison context.
