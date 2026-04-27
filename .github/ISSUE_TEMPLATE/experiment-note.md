---
name: Experiment note
about: Καταγραφή πειράματος ή ερευνητικής αλλαγής σε forecasting, diagnostics, graph stages ή thesis-safe documentation
title: "[EXPERIMENT] "
labels: experiment
assignees: ""
---

## Στόχος πειράματος

Τι ακριβώς θέλεις να ελέγξεις;

Γράψε το scope με σαφήνεια, π.χ.:

- baseline improvement
- leakage-safe preprocessing check
- residual diagnostics analysis
- graph-model input packaging check
- graph-based forecasting comparison
- graph ablation / spatial sensitivity analysis
- controlled graph refinement follow-up
- documentation-only research framing check

---

## Ερευνητικό motivation

Γιατί έχει νόημα αυτό το experiment για το project;

Σύνδεσέ το με ένα ή περισσότερα από τα παρακάτω:

- forecasting correctness
- reproducibility
- leakage control
- stronger benchmark clarity
- residual diagnostics
- park-level diagnostics
- graph-aware forecasting
- graph-stage interpretation
- thesis-facing consolidation
- PHM-oriented future direction

Μην παρουσιάσεις future PHM, anomaly detection, fault diagnosis, RUL ή digital twin functionality ως ήδη implemented.

---

## Μέρος του pipeline

Επίλεξε όσα ισχύουν:

- [ ] Raw validation
- [ ] Validated-only EDA
- [ ] Feature engineering
- [ ] Outlier handling / temporal splitting
- [ ] Baseline modeling
- [ ] Advanced tabular baselines
- [ ] Residual diagnostics / operating regimes
- [ ] Park-level diagnostics / thesis consolidation
- [ ] Graph data-interface / split-to-graph contract verification
- [ ] Graph-model input packaging
- [ ] First graph-based forecasting baseline
- [ ] Graph ablation / spatial sensitivity analysis
- [ ] Controlled graph refinement follow-up
- [ ] Local Django demo helper
- [ ] Documentation-only research framing

---

## Προτεινόμενη αλλαγή

Περιέγραψε καθαρά τι αλλάζει.

Αν είναι documentation-only αλλαγή, γράψε ρητά ότι δεν αλλάζουν:

- code
- notebooks
- benchmark protocol
- model training
- metrics
- artifacts
- results
- scientific scope

---

## Επηρεαζόμενα αρχεία

Συμπλήρωσε μόνο όσα ισχύουν:

- `.github/...`
- `docs/...`
- `notebooks/...`
- `src/...`
- `data/...` μόνο αν αλλάζει tracked metadata ή tracked output
- `django_demo/...` μόνο αν αλλάζει το local demo helper

---

## Πρωτόκολλο αξιολόγησης

Πώς θα κρίνεις αν πέτυχε;

Για modeling / benchmark experiments:

- Metric(s): MAE / RMSE / R² / άλλο
- Split: Validation ή Test
- Comparison against:
  - Persistence
  - Linear Regression
  - Random Forest
  - XGBoost
  - MLP
  - NB12 graph reference
  - NB13 best configuration
  - άλλο baseline

Για documentation-only experiments:

- consistency with README / docs
- thesis-safe wording
- no overclaiming
- clear implemented / planned / future distinction
- no notebook rerun required
- no benchmark or result change

---

## Αναμενόμενο αποτέλεσμα

Τι περιμένεις να βελτιωθεί ή να αποκαλυφθεί;

Παραδείγματα:

- clearer benchmark interpretation
- improved validation performance
- safer leakage handling
- clearer residual diagnostic interpretation
- clearer graph-stage boundary
- better thesis-facing documentation
- better local demo boundary

Απέφυγε claims τύπου “validated graph superiority”, “completed PHM”, “production digital twin” ή “fault diagnosis” αν δεν υπάρχει τεκμηριωμένη υλοποίηση.

---

## Risks / Leakage checks

Υπάρχει πιθανότητα για:

- [ ] data leakage
- [ ] inconsistent feature space
- [ ] train / validation / test contamination
- [ ] validation used as final reporting
- [ ] test data used for model selection
- [ ] misleading diagnostics due to scaled variables
- [ ] graph artifact mismatch
- [ ] graph-stage overclaiming
- [ ] local demo interpreted as production system
- [ ] PHM / anomaly detection / digital twin overclaiming
- [ ] not applicable because this is documentation-only

---

## Scope boundary

Επιβεβαίωσε όσα ισχύουν:

- [ ] Forecasting remains the implemented core.
- [ ] Diagnostics are treated as downstream forecasting diagnostics, not validated health-state inference.
- [ ] Graph stages are treated as cautious graph-aware forecasting evidence, not validated graph superiority.
- [ ] The local Django demo remains local-only, read-only and non-production.
- [ ] PHM / digital twin wording remains future-oriented.
- [ ] Implemented work, planned next steps and future work are clearly separated.

---

## Αποτελέσματα

Συμπληρώνεται μετά το run ή μετά την ολοκλήρωση του documentation pass.

Για modeling / benchmark experiments:

- Validation MAE:
- Validation RMSE:
- Validation R²:
- Test MAE:
- Test RMSE:
- Test R²:

Για documentation-only work:

- Files changed:
- Consistency checked against:
- Notebook reruns performed: No
- Benchmark changes introduced: No
- Artifact changes introduced: No

Παρατηρήσεις:

Συμπέρασμα:

---

## Next step

Ποιο είναι το επόμενο λογικό βήμα;

Ξεχώρισε καθαρά:

- implemented outcome
- planned next
- future work / research extension