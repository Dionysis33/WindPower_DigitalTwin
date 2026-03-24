---
name: Experiment note
about: Καταγραφή πειράματος / ερευνητικής αλλαγής σε baseline, preprocessing ή diagnostics
title: "[EXPERIMENT] "
labels: experiment
assignees: ""
---

## Στόχος πειράματος
Τι ακριβώς θέλεις να ελέγξεις;

## Ερευνητικό motivation
Γιατί έχει νόημα αυτό το experiment για το project;
Π.χ.:
- leakage control
- stronger baseline
- residual diagnostics
- PHM-oriented direction
- health-aware interpretability

## Μέρος του pipeline
- [ ] Data acquisition
- [ ] Preprocessing
- [ ] Feature engineering
- [ ] Temporal splitting
- [ ] Baseline modeling
- [ ] Diagnostics / residual analysis
- [ ] Documentation

## Προτεινόμενη αλλαγή
Περιέγραψε καθαρά τι αλλάζει.

## Επηρεαζόμενα αρχεία
- `notebooks/...`
- `src/...`
- `data/...`
- `docs/...`

## Πρωτόκολλο αξιολόγησης
Πώς θα κρίνεις αν πέτυχε;
- Metric(s): MAE / RMSE / R² / άλλο
- Split: Validation ή Test
- Comparison against:
  - Persistence
  - Linear Regression
  - άλλο baseline

## Αναμενόμενο αποτέλεσμα
Τι περιμένεις να βελτιωθεί ή να αποκαλυφθεί;

## Risks / Leakage checks
Υπάρχει πιθανότητα:
- data leakage;
- inconsistent feature space;
- train/test contamination;
- misleading diagnostics λόγω scaled variables;

## Αποτελέσματα
Συμπληρώνεται μετά το run:
- MAE:
- RMSE:
- R²:
- Παρατηρήσεις:
- Συμπέρασμα:

## Next step
Ποιο είναι το επόμενο λογικό βήμα αν το experiment πετύχει;