# Neural-network subset experiment audit

Σκοπός: μικρό, reproducible subset audit για tabular PyTorch MLP σε deterministic subset wind parks. Το audit είναι συμπληρωματικό evidence για neural-network readiness και δεν αντικαθιστά full-dataset benchmark metrics.

## Inputs

- Train split: `data/processed/train_final.csv`
- Validation split: `data/processed/val_final.csv`
- Test split: `data/processed/test_final.csv`
- Target column: `Power_Output_Normalized`

## Feature contract

- Εξαιρούνται: `Power_Output_Normalized`, `park_id`, `timestamp`, `test_flag`, `Baseline_Prediction`.
- Το `turbine` δεν γίνεται encoded και δεν χρησιμοποιείται ως learned feature.
- Χρησιμοποιούνται μόνο train-inferred numeric learned feature columns.
- Δεν χρησιμοποιούνται validation/test statistics για feature selection ή scaling.

## Subset strategy

- Γίνεται intersection των `park_id` values που υπάρχουν σε train, validation και test.
- Τα parks ταξινομούνται με train row count descending και μετά `park_id` ascending.
- Default run: `--n-parks 4`.
- Smoke mode: 1 park, λίγα epochs και deterministic row caps, μόνο για code validation.

## Scaling και training

- `StandardScaler` fit μόνο στα train subset feature rows.
- Το ίδιο scaler εφαρμόζεται σε validation και test subset rows.
- Το target δεν γίνεται scaled.
- Το μοντέλο είναι μόνο tabular PyTorch MLP με δύο hidden layers.
- Χρησιμοποιείται Adam optimizer.
- Το best epoch/model state επιλέγεται μόνο με validation loss.
- Το selected validation state αξιολογείται μία φορά στο test subset.
- Δεν γράφονται model checkpoints ή binaries.

## Outputs

Default subset run outputs:

- `data/processed/diagnostics/nn_subset/nn_subset_mlp_validation_metrics.csv`
- `data/processed/diagnostics/nn_subset/nn_subset_mlp_selected_test_metrics.csv`
- `data/processed/diagnostics/nn_subset/nn_subset_mlp_run_manifest.csv`
- `data/processed/diagnostics/nn_subset/nn_subset_mlp_training_history.csv`

Smoke/capped runs γράφουν ξεχωριστά prefixed outputs και έχουν `run_mode=smoke` ή `run_mode=capped`. Αυτά είναι code-validation outputs και δεν αποτελούν manuscript evidence.

Όλα τα generated CSVs κάτω από `data/processed/**` είναι local-only generated outputs. Το `data/processed/baseline_metrics.csv` δεν γίνεται overwrite.

## Commands

Smoke test:

```powershell
python -B scripts/run_nn_subset_experiments.py --smoke
```

Full subset run:

```powershell
python -B scripts/run_nn_subset_experiments.py
```

## Manuscript boundary

Το audit τεκμηριώνει ότι υπάρχει μικρό, leakage-aware και reproducible path για tabular neural-network subset experiments. Δεν αποτελεί full-dataset benchmark replacement και δεν υποστηρίζει claim model-performance improvement από μόνο του. Οποιαδήποτε manuscript διατύπωση για performance πρέπει να βασίζεται σε completed και reviewed outputs, χωρίς χρήση smoke/capped results ως τελικό evidence.
