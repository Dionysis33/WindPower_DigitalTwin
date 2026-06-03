# NB15 GRU Sequence Subset Audit

## Summary

This document records the completed local controlled GRU subset run from `notebooks/15_nn_sequence_baseline_subset.ipynb`.

The run is controlled four-park subset evidence only. It is not a full-dataset benchmark replacement, does not update `data/processed/baseline_metrics.csv`, and should not be used to claim model superiority or performance improvement.

## Run Configuration

| Field | Value |
|---|---:|
| model | PyTorch GRU sequence baseline |
| selected parks | 00183, 00198, 00303, 00427 |
| seed | 42 |
| device | cpu |
| lookback_steps | 24 |
| hidden_size | 64 |
| GRU layers | 1 |
| dropout | 0.0 |
| learning_rate | 0.001 |
| weight_decay | 1e-5 |
| batch_size | 512 |
| epochs requested | 30 |
| early stopping patience | 5 |
| best_epoch | 7 |
| best_val_loss_mse | 0.021375563306113083 |
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
| validation | 0.09467061222417163 | 0.14620384209397685 | 0.7937695238087121 |
| test | 0.1013616555108132 | 0.152757068100059 | 0.8269631744779631 |

The test set was evaluated once after validation-selected state selection (`test_evaluations = 1`).

## Local-Only Outputs

The following CSVs were written under `data/processed/diagnostics/nn_sequence_subset/`:

- `data/processed/diagnostics/nn_sequence_subset/nn_sequence_subset_gru_run_manifest.csv`
- `data/processed/diagnostics/nn_sequence_subset/nn_sequence_subset_gru_window_audit.csv`
- `data/processed/diagnostics/nn_sequence_subset/nn_sequence_subset_gru_training_history.csv`
- `data/processed/diagnostics/nn_sequence_subset/nn_sequence_subset_gru_validation_metrics.csv`
- `data/processed/diagnostics/nn_sequence_subset/nn_sequence_subset_gru_selected_test_metrics.csv`

These CSVs are ignored/local-only and should not be committed.

No checkpoints or model binaries were written.
