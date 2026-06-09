# NB18 TCN Sequence Subset Audit

## Σύνοψη

Το παρόν αρχείο καταγράφει το ολοκληρωμένο τοπικό run του `notebooks/18_tcn_sequence_baseline_subset.ipynb` για το TCN sequence baseline σε ελεγχόμενο υποσύνολο τεσσάρων αιολικών πάρκων.

Το αποτέλεσμα πρέπει να χρησιμοποιείται ως τεκμήριο για το συγκεκριμένο controlled four-park sequence subset μόνο. Δεν αντικαθιστά το πλήρες benchmark, δεν τροποποιεί το `data/processed/baseline_metrics.csv` και δεν τεκμηριώνει ισχυρισμό υπεροχής έναντι GRU, LSTM, XGBoost ή Vogt-style baselines χωρίς άμεσα συγκρίσιμα, ήδη τεκμηριωμένα matched metrics.

## Πρωτόκολλο

| Πεδίο | Τιμή |
|---|---:|
| Notebook | `notebooks/18_tcn_sequence_baseline_subset.ipynb` |
| Model | PyTorch TCN sequence baseline |
| model_id | `tcn_c64_k3_d1_2_4_8_do0_1` |
| selected parks | `00183`, `00198`, `00303`, `00427` |
| n_parks | 4 |
| seed | 42 |
| device | cpu |
| LOOKBACK_STEPS | 24 |
| n_numeric_features | 41 |
| channels | 64 |
| kernel_size | 3 |
| dilations | 1, 2, 4, 8 |
| dropout | 0.1 |
| learning_rate | 0.001 |
| weight_decay | 1e-05 |
| batch_size | 512 |
| epochs_requested | 30 |
| validation selection policy | MAE primary, then RMSE, then R2 |

## Έλεγχοι Δεδομένων Και Εκτέλεσης

- Τα features προκύπτουν μόνο από το train split.
- Το `StandardScaler` εφαρμόζεται με fit μόνο στο train.
- Ο στόχος παραμένει unscaled.
- Τα sequence windows είναι gap-safe.
- Δεν δημιουργούνται windows που περνούν όρια park, split ή timestamp gap.
- Πραγματοποιήθηκε ακριβώς μία τελική αξιολόγηση στο test split.
- Το `data/processed/baseline_metrics.csv` δεν τροποποιήθηκε.
- Δεν γράφτηκαν checkpoints ή model binaries.

## Πλήθος Windows

| Split | Windows |
|---|---:|
| train | 30988 |
| validation | 2784 |
| test | 16892 |

## Εκπαίδευση Και Επιλογή

| Πεδίο | Τιμή |
|---|---:|
| best_epoch | 25 |
| best_val_loss_mse | 0.024829332042357016 |
| elapsed_seconds | 431.964 |

## Metrics

| Split | MAE | RMSE | R2 |
|---|---:|---:|---:|
| validation | 0.10367857854266052 | 0.157573260059511 | 0.7604477171114871 |
| selected test | 0.11380967093854394 | 0.16218968427658445 | 0.804933645682722 |

`test_evaluations = 1`: το validation-selected TCN state αξιολογήθηκε μία φορά στο test subset.

## Local-Only CSV Exports

Τα παρακάτω CSV αρχεία αποτελούν τοπικά diagnostics κάτω από `data/processed/diagnostics/nn_sequence_subset_tcn/` και δεν πρέπει να προστεθούν σε commit:

- `data/processed/diagnostics/nn_sequence_subset_tcn/nn_sequence_subset_tcn_run_manifest.csv`
- `data/processed/diagnostics/nn_sequence_subset_tcn/nn_sequence_subset_tcn_window_audit.csv`
- `data/processed/diagnostics/nn_sequence_subset_tcn/nn_sequence_subset_tcn_training_history.csv`
- `data/processed/diagnostics/nn_sequence_subset_tcn/nn_sequence_subset_tcn_validation_metrics.csv`
- `data/processed/diagnostics/nn_sequence_subset_tcn/nn_sequence_subset_tcn_selected_test_metrics.csv`

## Manuscript-Safe Ερμηνεία

Το TCN run προσθέτει ένα convolutional neural baseline στην ίδια ελεγχόμενη τετραπλή επιλογή πάρκων και δείχνει ότι το πειραματικό πρωτόκολλο μπορεί να υποστηρίξει μη αναδρομικές sequence architectures.

Σε άμεση σύγκριση μόνο με το ήδη τεκμηριωμένο GRU run στο ίδιο four-park sequence subset, το TCN δεν υπερέβη το GRU ως προς test MAE: το TCN έχει test MAE 0.11381, ενώ το προηγουμένως τεκμηριωμένο GRU έχει test MAE περίπου 0.10136.

Το αποτέλεσμα δεν πρέπει να παρουσιαστεί ως αντικατάσταση του πλήρους benchmark ούτε ως ισχυρισμός βελτίωσης έναντι GRU, LSTM, XGBoost ή Vogt-style baselines χωρίς αντίστοιχο matched comparison context.
