# Έλεγχος preprocessing correlations

Σκοπός: leakage-aware έλεγχος συσχετίσεων για το preprocessing / feature-space contract του manuscript, χωρίς model training και χωρίς αλλαγή στα upstream artifacts.

## Inputs που χρησιμοποιούνται

- Train statistics: `data/processed/train_final.csv`
- Validation schema/header check only: `data/processed/val_final.csv`
- Test schema/header check only: `data/processed/test_final.csv`
- Target column: `Power_Output_Normalized`
- Excluded columns: `Power_Output_Normalized`, `timestamp`, `park_id`, `test_flag`, `Baseline_Prediction`, `turbine`

## Κανόνες leakage-safety

- Όλες οι συσχετίσεις υπολογίζονται αποκλειστικά στο train split.
- Τα validation/test splits χρησιμοποιούνται μόνο για schema/header consistency checks.
- Δεν χρησιμοποιούνται validation ή test statistics για feature-selection decisions.
- Δεν γίνεται model training, hyperparameter tuning ή αλλαγή preprocessing policy.
- Τα high-correlation ευρήματα είναι review candidates και όχι automatic removals.

## Train-only statistics

- Train rows used: `1,982,736`
- Number of candidate numeric learned features: `41`
- Number of high-correlation feature pairs with `abs(Pearson r) >= 0.95`: `25`
- Non-numeric candidate columns excluded by the numeric feature contract: κανένα

## Σύντομη ερμηνεία ευρημάτων

- Οι strongest target correlations κυριαρχούνται από autoregressive power/target lag features και wind-speed-related features.
- Αυτό είναι αναμενόμενο για forecasting setup και δεν υποδηλώνει από μόνο του leakage, εφόσον τα lag/rolling features έχουν παραχθεί causally από past observations.
- Τα `25` high-correlation feature pairs είναι review candidates για redundancy/complexity checks και όχι automatic feature removals.
- Το audit δεν διεκδικεί model-performance improvement ή feature-removal decision.

## Outputs

- Figure: tracked manuscript-facing figure, `reports/figures/diagnostics/preprocessing_target_correlation_top20.png`
- CSV: reproducible local audit output, `data/processed/diagnostics/preprocessing_audit/preprocessing_correlation_audit.csv`
  - Το CSV αγνοείται από το repository data policy επειδή βρίσκεται κάτω από `data/processed/**`.
  - Αναπαράγεται με `python -B scripts/audit_preprocessing_correlations.py`.

## Όριο ερμηνείας

Το audit επιτρέπεται να στηρίξει προσεκτική manuscript διατύπωση για leakage-aware preprocessing checks και feature-correlation review. Δεν τεκμηριώνει από μόνο του feature removal, model-performance improvement ή αλλαγή στο canonical benchmark protocol.
