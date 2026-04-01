# Contributing to WindPower_DigitalTwin

Thank you for your interest in contributing to **WindPower_DigitalTwin**.

This repository is a **research repository** for **spatio-temporal wind power forecasting** on the **DaKS / Kassel synthetic wind power dataset**. It supports a **forecasting-first, reproducible pipeline** and also serves **thesis-oriented academic work** and broader research development around benchmark-safe forecasting, downstream diagnostics, and future health-aware / PHM-oriented extensions.

At the current stage, the repository is maintained primarily by the author. External contributions are welcome, but they must respect the scientific structure, reproducibility requirements, and scope boundaries of the project.

---

## Contribution Principles

Please make sure that every contribution follows these principles:

- **Reproducibility first**  
  Any change must preserve or improve reproducibility of the notebooks, exported artifacts, and the overall modeling pipeline.

- **No data leakage**  
  Temporal integrity is critical. Train / validation / test separation must remain strictly correct.  
  Any preprocessing statistics that could leak information downstream must be handled with train-first logic.

- **Forecasting-first scope discipline**  
  The implemented core of the repository remains forecasting-first.  
  Diagnostics-aware interpretation is welcome, but contributions must not overstate the current repository as a completed PHM, fault-diagnosis, anomaly-detection, or RUL system.

- **Research consistency**  
  Contributions should align with the repository roadmap and current canonical workflow:
  - raw validation,
  - validated-only EDA,
  - feature engineering,
  - leakage-aware temporal split,
  - baseline benchmarking,
  - downstream residual diagnostics,
  - park-level diagnostics / thesis consolidation,
  - and future graph-based or sequence-based forecasting work.

- **Clear stage distinction**  
  Contributions should clearly distinguish between:
  1. **already implemented**
  2. **planned next**
  3. **future work / research extension**

- **Documentation quality**  
  Important changes should be reflected in:
  - notebook markdown explanations,
  - `README.md`,
  - `LOGS.md`,
  - `docs/INDEX.md`,
  - and other relevant documentation when needed.

---

## What Kinds of Contributions Are Most Useful

The most useful contributions are:

- bug fixes,
- code cleanup and refactoring,
- reproducibility improvements,
- documentation improvements,
- evaluation utilities,
- notebook-to-module modularization,
- diagnostics utilities,
- visualization improvements,
- benchmark-safe exported artifact checks,
- additional baseline models that fit the repository roadmap,
- graph-readiness or interface-contract improvements that do not break the current canonical pipeline.

At this phase, please avoid contributions that:

- radically redefine the repository scope,
- break notebook reproducibility,
- introduce hidden leakage,
- add undocumented dependencies,
- bypass canonical stage contracts,
- present diagnostics outputs as validated health-state inference,
- commit large raw or generated artifacts without a strong reason,
- or mix implemented results with speculative future claims.

---

## Development Guidelines

### Branch Naming

Use clear branch names such as:

- `fix/...`
- `feat/...`
- `docs/...`
- `chore/...`

Examples:

- `feat/add-random-forest-baseline`
- `fix/temporal-split-validation`
- `docs/realign-contributing-scope`
- `chore/update-benchmark-artifact-notes`

### Commit Style

Use concise and meaningful commit messages.

Recommended format:

- `feat: add random forest benchmark`
- `fix: prevent leakage in baseline feature selection`
- `docs: realign contributing guide with research scope`
- `chore: update baseline metrics artifact notes`

### Coding Style

Please follow these rules:

- prefer readable and explicit code over clever shortcuts,
- keep variable names meaningful,
- use comments where scientific intent matters,
- preserve notebook narrative clarity,
- keep English terminology for technical concepts when appropriate,
- prefer deterministic behavior where reproducibility matters,
- and avoid silent fallbacks that hide methodological problems.

### Notebook Policy

When editing notebooks:

- preserve execution order,
- do not leave broken cells,
- avoid hidden assumptions,
- explain major methodological choices in markdown,
- keep outputs informative but not excessively noisy,
- avoid ad hoc exploratory fragments in canonical notebooks,
- and keep exported artifacts consistent with the notebook’s intended role.

If a notebook change affects results, update the relevant interpretation text as well.

---

## Canonical Workflow Contract

For the current public repository state, the canonical workflow is:

`NB02 raw validation -> NB03 validated-only EDA -> NB04 feature engineering -> NB05 outlier handling / temporal split -> NB06 baseline modeling -> NB07 advanced tabular baselines -> NB08 downstream residual diagnostics -> NB09 park-level diagnostics / thesis consolidation`

This means:

- `02_kassel_exploration.ipynb` is the **canonical raw validation authority**.
- `03_eda_master.ipynb` is the **canonical validated-only EDA stage**.
- `04_feature_engineering_and_graph_construction.ipynb` is the **canonical feature-engineering and graph-ready preparation stage**.
- `05_outliers_and_split.ipynb` is the **canonical leakage-aware split stage**.
- `06_baseline_modeling.ipynb` and `07_advanced_baselines_and_importance.ipynb` define the **implemented baseline ladder**.
- `08_residual_diagnostics_and_operating_regimes.ipynb` is a **strict downstream diagnostics stage**, not a new predictive modeling stage.
- `09_park_level_diagnostics_and_thesis_consolidation.ipynb` is a **strict downstream diagnostics / consolidation stage**, not a new predictive modeling stage.

### Important downstream rule

After `NB02`, downstream notebooks must not perform **loose reparsing** of raw timestamps or reintroduce raw-validation logic.

Downstream stages should consume validated outputs and canonical exported artifacts rather than silently redefining upstream methodological responsibilities.

---

## Operational Helper Clarification

Operational helper modules may be used for loading, feature preparation, or downstream convenience, but they must not be documented as canonical methodological authorities unless the pipeline is explicitly redesigned.

In particular, `KasselLoader` should be treated as an **operational helper** and not as the **canonical strict raw validation layer** of the project.

---

## Research Framing Rules

Because this repository is both research-facing and thesis-facing, contribution wording must remain scientifically disciplined.

### 1. Implemented vs planned vs future

When describing contributions, issues, PRs, markdown cells, or docs updates, clearly separate:

- **Implemented now**
- **Planned next**
- **Future work / research extension**

Do not blur these categories.

### 2. Diagnostics boundary

Residual diagnostics, operating-regime analysis, and park-level diagnostics may support:

- diagnostics-aware interpretation,
- health-aware discussion,
- PHM-oriented future thinking.

However, they must not be presented as:

- completed PHM functionality,
- validated anomaly detection,
- fault diagnosis,
- prognostics engine,
- RUL estimation,
- or deployed digital twin service.

### 3. Forecasting remains the implemented core

The repository currently supports:

- benchmark-safe forecasting,
- diagnostics-aware downstream analysis,
- and cautious thesis-oriented interpretation.

Graph-based, sequence-based, and broader PHM-oriented modeling remain **future work** unless explicitly implemented and documented.

---

## Benchmark and Reporting Rules

The repository uses a benchmark-safe reporting structure.

### Canonical benchmark artifact

For cross-model reporting, the canonical benchmark artifact is:

`data/processed/baseline_metrics.csv`

Use this artifact as the reporting authority for benchmark comparisons.

### Test-only benchmark interpretation

When reporting final benchmark performance:

- validation should be used for model selection only,
- test should be used for final reporting only,
- and benchmark summaries should remain consistent with the canonical exported artifact.

### Historical logs are not active benchmark authority

- `LOGS.md` is the **active canonical methodological log**.
- `LOGS_ARCHIVE.md` contains historical, exploratory, or superseded states.

Do not treat archived notebook outputs or old log entries as the active benchmark authority when current canonical artifacts already exist.

---

## Data Policy

This repository uses the **DaKS synthetic wind power dataset** from the University of Kassel research data repository.

Contributors must:

- respect the original dataset attribution requirements,
- avoid misrepresenting the dataset as original proprietary raw data,
- clearly distinguish between:
  - source dataset files,
  - processed artifacts,
  - derived benchmark outputs,
  - and thesis/report figures derived from reruns.

If a contribution depends on dataset access, explain clearly:

- which files are needed,
- where they come from,
- how they should be placed,
- and how they should be prepared before execution.

### Artifact discipline

Please be careful with generated outputs.

In general:

- do not commit large raw files,
- do not commit large rerun artifacts unless they are intentionally tracked,
- do not assume local outputs are canonical public artifacts,
- and document any exported file that becomes part of the stable workflow.

---

## Documentation Consistency

When a change affects pipeline meaning, notebook roles, benchmark reporting, or diagnostics interpretation, documentation must be updated in a coordinated way where relevant:

- `README.md`
- `LOGS.md`
- `LOGS_ARCHIVE.md`
- `docs/INDEX.md`
- `docs/RESEARCH_SCOPE.md`
- `docs/BASELINE_PROTOCOL.md`
- `docs/PHM_ROADMAP.md`
- notebook markdown cells that describe methodological role or pipeline order

### Additional review requirement

If a change affects:

- raw validation,
- timestamp parsing,
- coverage / eligibility rules,
- split semantics,
- feature-space definition,
- benchmark interpretation,
- diagnostics positioning,
- or forecasting vs PHM wording,

then it should be reviewed explicitly for documentation realignment and scope consistency.

---

## Before Submitting a Contribution

Please verify that:

- the relevant notebook(s) run successfully,
- no data leakage has been introduced,
- paths remain consistent,
- required exported artifacts are intentional,
- documentation has been updated where needed,
- canonical benchmark or diagnostics wording remains consistent,
- scope wording does not overclaim repository functionality,
- and `git status` is clean except for intended files.

If your change affects results, please also verify:

- whether metrics changed,
- whether benchmark ranking changed,
- whether residual or park-level diagnostics interpretation changed,
- and whether those changes should be reflected in logs or docs.

---

## Pull Requests

If you open a pull request, please include:

1. **What changed**
2. **Why it changed**
3. **Which notebook(s), module(s), or docs are affected**
4. **Whether metrics changed**
5. **Whether exported artifacts changed**
6. **Whether markdown / README / logs / docs were updated**
7. **Whether the change is implemented work, planned-next scaffolding, or future-facing preparation**

Good PRs are:

- small,
- focused,
- easy to review,
- benchmark-safe,
- and explicit about methodological impact.

---

## Academic and Research Note

Because this repository supports both **academic thesis work** and a broader **research-oriented forecasting workflow**, methodological correctness is more important than feature quantity.

A contribution that makes the pipeline more scientifically valid, more reproducible, or more clearly documented is preferred over one that merely makes it larger.

Thank you for helping improve the project.