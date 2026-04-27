---
name: Bug report
about: Αναφορά bug σε notebook, preprocessing, metrics, artifacts, graph stages, local demo ή GitHub workflow
title: "[BUG] "
labels: bug
assignees: ""
---

## Περιγραφή

Σύντομη και καθαρή περιγραφή του προβλήματος.

Τι δεν λειτουργεί σωστά;

---

## Πού εμφανίζεται

Συμπλήρωσε μόνο όσα ισχύουν:

- Notebook / Script:
- Cell / Section:
- File / Path:
- Commit / Branch, αν γνωρίζεις:
- Related issue / PR, αν υπάρχει:

---

## Μέρος του pipeline

Επίλεξε όσα ισχύουν:

- [ ] Raw validation
- [ ] Validated-only EDA
- [ ] Feature engineering
- [ ] Outlier handling / temporal split
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
- [ ] GitHub Actions / repository workflow
- [ ] Documentation / template issue

---

## Βήματα αναπαραγωγής

1.
2.
3.

Αν δεν είναι πλήρως reproducible, γράψε τι γνωρίζεις μέχρι στιγμής.

---

## Αναμενόμενο αποτέλεσμα

Τι θα έπρεπε να συμβαίνει;

---

## Πραγματικό αποτέλεσμα

Τι συνέβη τελικά;

---

## Error message / Traceback

```text
Paste the traceback, terminal output, GitHub Actions output, or notebook error here.
```

---

## Επηρεαζόμενα αρχεία ή artifacts

Συμπλήρωσε μόνο όσα ισχύουν:

- `notebooks/...`
- `src/...`
- `docs/...`
- `.github/...`
- `data/...` μόνο αν αφορά tracked metadata ή tracked outputs
- `django_demo/...` μόνο αν αφορά το local demo helper

Αν το bug αφορά artifact handling, διευκρίνισε αν επηρεάζει:

- [ ] raw data
- [ ] processed outputs
- [ ] canonical benchmark artifact
- [ ] prediction exports
- [ ] diagnostics exports
- [ ] graph exports
- [ ] model artifacts
- [ ] demo bundle
- [ ] not applicable

---

## Leakage / benchmark risk

Υπάρχει πιθανότητα το bug να επηρεάζει:

- [ ] train / validation / test separation
- [ ] train-only preprocessing statistics
- [ ] validation-only model selection
- [ ] test-only final reporting
- [ ] benchmark metrics
- [ ] graph-stage interpretation
- [ ] diagnostics interpretation
- [ ] no obvious leakage or benchmark risk
- [ ] unsure

---

## Scope boundary check

Επιβεβαίωσε όσα ισχύουν:

- [ ] This bug report does not introduce PHM, anomaly detection, fault diagnosis, RUL, or production digital twin claims.
- [ ] Diagnostics remain downstream forecasting diagnostics.
- [ ] Graph stages are not being treated as validated graph superiority.
- [ ] The local Django demo remains local-only, read-only and non-production.
- [ ] Not applicable.

---

## Screenshots / Extra material

Βάλε screenshots, outputs ή snippets αν χρειάζονται.

```text
Paste relevant screenshots description, output snippets, or extra context here.
```

---

## Proposed fix, αν υπάρχει

Αν έχεις ιδέα για πιθανή διόρθωση, γράψε την εδώ.

Αν όχι, γράψε:

- No proposed fix yet.