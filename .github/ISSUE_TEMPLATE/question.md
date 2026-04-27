---
name: Research / implementation question
about: Ερώτηση για methodology, notebooks, metrics, leakage, graph stages, dataset handling, local demo ή research direction
title: "[QUESTION] "
labels: question
assignees: ""
---

## Ερώτηση

Γράψε καθαρά το ερώτημα.

Παράδειγμα:

- Ποια είναι η σωστή benchmark-safe ερμηνεία;
- Χρειάζεται notebook rerun ή είναι documentation-only αλλαγή;
- Πρέπει αυτό να θεωρηθεί implemented, planned next ή future work;
- Πώς αποφεύγεται leakage σε αυτό το στάδιο;
- Πώς πρέπει να διατυπωθεί ένα graph-related ή PHM-oriented claim χωρίς overclaiming;

---

## Context

Σε ποιο σημείο του project αφορά;

- Notebook:
- Section:
- File / Path:
- Related experiment / issue:
- Related PR:
- Related artifact, αν υπάρχει:

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
- [ ] Documentation / thesis-facing wording
- [ ] Repository governance / templates
- [ ] Future research planning

---

## Τι έχεις ήδη δοκιμάσει

1.
2.
3.

Αν δεν έχει γίνει ακόμα τεχνική δοκιμή, γράψε:

- Not tested yet / conceptual question only.

---

## Τι ακριβώς σε μπλοκάρει

Περιέγραψε το ambiguity ή το technical blocker.

Παραδείγματα:

- methodological ambiguity
- leakage concern
- benchmark interpretation concern
- graph-stage interpretation concern
- artifact handling concern
- local demo scope concern
- wording / thesis framing concern
- future-work vs implemented-work boundary

---

## Πιθανές επιλογές

- Επιλογή A:
- Επιλογή B:
- Επιλογή C:

Αν δεν υπάρχουν ακόμη επιλογές, γράψε:

- Need guidance before defining options.

---

## Research relevance

Αφορά:

- [ ] forecasting correctness
- [ ] reproducibility
- [ ] leakage prevention
- [ ] benchmark clarity
- [ ] diagnostics interpretation
- [ ] graph-aware forecasting
- [ ] graph-stage boundary
- [ ] local demo boundary
- [ ] thesis-facing documentation
- [ ] PHM / prognostics future direction
- [ ] digital-twin future framing

---

## Scope boundary check

Επιβεβαίωσε όσα ισχύουν:

- [ ] Forecasting remains the implemented core.
- [ ] Diagnostics are not being presented as validated health-state inference.
- [ ] Graph stages are not being presented as validated graph superiority.
- [ ] The local Django demo is not being presented as a deployed service or production platform.
- [ ] PHM / digital twin wording remains future-oriented unless explicitly implemented and evaluated.
- [ ] Implemented work, planned next steps and future work are clearly separated.

---

## Expected answer type

Τι είδους απάντηση χρειάζεται;

- [ ] Methodological decision
- [ ] Documentation wording
- [ ] Code / implementation direction
- [ ] Notebook interpretation
- [ ] Benchmark interpretation
- [ ] Artifact policy decision
- [ ] Thesis-facing explanation
- [ ] Future-work planning

---

## Extra material

Βάλε screenshots, outputs, snippets ή links αν χρειάζονται.

```text
Paste relevant terminal output, notebook output, metric table, or markdown snippet here.
```