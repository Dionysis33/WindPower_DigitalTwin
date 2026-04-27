## Summary

Briefly describe what this PR changes.

---

## Type of change

Select all that apply:

- [ ] Bug fix
- [ ] Refactor
- [ ] Documentation update
- [ ] Notebook result update
- [ ] Baseline / modeling change
- [ ] Diagnostics / visualization change
- [ ] Graph verification / graph packaging change
- [ ] Graph baseline / graph ablation / controlled graph refinement change
- [ ] Local demo change
- [ ] Research scope / protocol update

---

## Related issue

Closes #

---

## Related files

List the main files changed by this PR.

- `.github/...`
- `docs/...`
- `notebooks/...`
- `src/...`
- `data/...` only if intentionally changing tracked metadata or tracked outputs
- `django_demo/...` only if changing the local demo helper

---

## Repository scope check

This PR keeps the repository aligned with the current forecasting-first scope.

Confirm where relevant:

- [ ] The change preserves the forecasting-first framing.
- [ ] The change does not present diagnostics as validated PHM, anomaly detection, fault diagnosis, or RUL functionality.
- [ ] The change does not present graph stages as validated graph superiority.
- [ ] The change does not present the local Django demo as a deployed digital twin, production monitoring platform, PHM system, or operational forecasting service.
- [ ] Implemented work, planned next steps, and future work remain clearly separated.

---

## Why this change matters

Explain why this change improves one or more of the following:

- reproducibility
- methodological correctness
- leakage protection
- benchmark clarity
- diagnostics interpretation
- graph-stage clarity
- local demo safety / presentation clarity
- thesis-facing documentation quality
- PHM / digital-twin future-work framing

---

## Validation performed

Select only what applies.

### General checks

- [ ] `git diff --check` passed
- [ ] Only intended files were changed
- [ ] No unintended raw data, local artifacts, model files, or environment files were added

### Documentation-only checks

- [ ] Documentation wording was reviewed for thesis-safe, non-overclaiming framing
- [ ] No code changed
- [ ] No notebooks changed
- [ ] No notebook reruns were performed
- [ ] No benchmark protocol changed
- [ ] No model training was performed
- [ ] No metrics changed
- [ ] No artifacts or results changed

### Notebook / modeling checks

- [ ] Notebook cells rerun successfully
- [ ] No obvious leakage introduced
- [ ] Metrics checked
- [ ] Outputs / plots inspected
- [ ] Logs updated where needed
- [ ] README / docs updated where needed

---

## Benchmark / result impact

Select one:

- [ ] No benchmark, metric, artifact, or result changes
- [ ] Benchmark or metric changes are included and documented below
- [ ] Not applicable

If benchmark or metric changes are included, report them here.

- Validation MAE:
- Validation RMSE:
- Validation R²:
- Test MAE:
- Test RMSE:
- Test R²:

---

## Graph / diagnostics interpretation

If this PR affects diagnostics or graph-related stages, confirm the interpretation boundary.

- [ ] Diagnostics remain forecasting diagnostics, not validated health-state inference
- [ ] Graph verification / packaging remains infrastructure, not graph superiority evidence
- [ ] Graph baseline / ablation / controlled refinement results are interpreted cautiously
- [ ] No validated GNN / Graph-Mamba superiority claim is introduced
- [ ] Not applicable

---

## Local Django demo impact

If this PR affects `django_demo/`, confirm:

- [ ] The demo remains local-only
- [ ] The demo remains read-only
- [ ] The demo remains non-production
- [ ] The demo does not trigger notebook reruns, model training, benchmark rewriting, or artifact mutation
- [ ] Not applicable

---

## Screenshots / Figures

Add screenshots, figures, or workflow status only if useful.

---

## Notes for future work

Describe any future work carefully.

Do not present future work as already implemented.