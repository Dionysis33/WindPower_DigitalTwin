# Contributing to WindPower_DigitalTwin

Thank you for your interest in contributing to **WindPower_DigitalTwin**.

This repository is a **research repository** for **spatio-temporal wind power forecasting** on the **DaKS / Kassel synthetic wind power dataset**.

It supports a **forecasting-first, reproducible, thesis-ready pipeline** and broader research development around:

- benchmark-safe wind power forecasting,
- downstream residual diagnostics,
- park-level diagnostic interpretation,
- graph data-interface verification,
- graph-model input packaging,
- cautious graph-based forecasting experimentation,
- controlled graph refinement follow-up,
- and future health-aware / PHM-oriented research extensions.

The current implementation should be understood as a **forecasting and diagnostics research pipeline**, not as a completed PHM system, anomaly-detection system, fault-diagnosis module, RUL estimator, production digital twin, deployed monitoring platform, or operational forecasting service.

At the current stage, the repository is maintained primarily by the author. External contributions are welcome, but they must respect the scientific structure, reproducibility requirements, artifact policy, and scope boundaries of the project.

---

## Contribution Principles

Please make sure that every contribution follows these principles.

### Reproducibility first

Any change must preserve or improve reproducibility of the notebooks, source modules, exported artifacts, documentation, and overall modeling pipeline.

Contributions should avoid hidden state, undocumented local assumptions, and silent behavior that makes the workflow difficult to reproduce.

### No data leakage

Temporal integrity is critical.

Train / validation / test separation must remain strictly correct. Any preprocessing statistics that could leak information downstream must be handled with train-first logic.

In particular:

- validation data should be used for model selection only,
- test data should be used for final reporting only,
- downstream diagnostics should not redefine upstream split logic,
- graph-related stages should consume established canonical artifacts rather than silently changing benchmark assumptions.

### Forecasting-first scope discipline

The implemented core of the repository remains **forecasting-first**.

Diagnostics-aware, condition-awareness-oriented, graph-aware, and PHM-oriented interpretation is welcome only when it is clearly framed as downstream analysis or future research direction.

Contributions must not overstate the current repository as:

- a completed PHM system,
- a validated anomaly detector,
- a fault-diagnosis module,
- a prognostics engine,
- a remaining useful life estimation system,
- a production digital twin,
- a deployed monitoring platform,
- or an operational forecasting service.

### Research consistency

Contributions should align with the repository roadmap and current canonical workflow:

- raw validation,
- validated-only EDA,
- feature engineering,
- leakage-aware temporal split,
- baseline benchmarking,
- advanced tabular baselines,
- downstream residual diagnostics,
- park-level diagnostics / thesis consolidation,
- graph data-interface / split-to-graph contract / artifact verification,
- graph-model input packaging / data object preparation,
- first graph-based forecasting baseline,
- graph ablation / spatial sensitivity analysis,
- controlled graph refinement follow-up,
- local thesis-facing artifact inspection / presentation support,
- and future graph-based, sequence-based, or broader PHM-oriented research extensions only when clearly documented as future work.

### Clear stage distinction

Contributions should clearly distinguish between:

1. **already implemented**
2. **planned next**
3. **future work / research extension**

Do not blur these categories in issues, pull requests, notebook markdown, README text, logs, or thesis-facing documentation.

### Documentation quality

Important changes should be reflected in the relevant documentation when needed.

Depending on the change, this may include:

- notebook markdown explanations,
- `README.md`,
- `LOGS.md`,
- `LOGS_ARCHIVE.md`,
- `docs/INDEX.md`,
- `docs/RESEARCH_SCOPE.md`,
- `docs/BASELINE_PROTOCOL.md`,
- `docs/PHM_ROADMAP.md`,
- and other documentation that defines repository interpretation.

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
- graph-interface or graph-packaging improvements that do not break the current canonical pipeline,
- local demo improvements that preserve read-only, non-production, thesis-facing behavior.

At this phase, please avoid contributions that:

- radically redefine the repository scope,
- break notebook reproducibility,
- introduce hidden leakage,
- add undocumented dependencies,
- bypass canonical stage contracts,
- present diagnostics outputs as validated health-state inference,
- present graph verification or graph packaging outputs as graph-training evidence,
- present graph baseline, graph ablation, or controlled graph-refinement outputs as validated graph superiority,
- present the local Django demo as a deployed digital twin, monitoring platform, PHM system, anomaly-detection system, fault-diagnosis system, or production service,
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
- `docs/align-contributing-with-post-nb14-readme`
- `chore/update-benchmark-artifact-notes`

### Commit Style

Use concise and meaningful commit messages.

Recommended format:

- `feat: add random forest benchmark`
- `fix: prevent leakage in baseline feature selection`
- `docs: align contributing with post-NB14 README state`
- `chore: update baseline metrics artifact notes`

For documentation-only governance updates, prefer:

```text
docs: align governance docs with post-NB14 README state
```

### Coding Style

Please follow these rules:

- prefer readable and explicit code over clever shortcuts,
- keep variable names meaningful,
- use comments where scientific intent matters,
- preserve notebook narrative clarity,
- keep English terminology for technical concepts when appropriate,
- prefer deterministic behavior where reproducibility matters,
- avoid silent fallbacks that hide methodological problems,
- avoid changing scientific interpretation through code comments alone.

### Notebook Policy

When editing notebooks:

- preserve execution order,
- do not leave broken cells,
- avoid hidden assumptions,
- explain major methodological choices in markdown,
- keep outputs informative but not excessively noisy,
- avoid ad hoc exploratory fragments in canonical notebooks,
- keep exported artifacts consistent with the notebook’s intended role,
- and update relevant interpretation text if a notebook change affects results.

Notebook changes that affect metrics, artifacts, model behavior, split semantics, graph contracts, or diagnostics interpretation should be handled as methodological changes, not as casual cleanup.

---

## Canonical Workflow Contract

For the current public repository state, the canonical workflow is:

```text
NB02 raw validation
-> NB03 validated-only EDA
-> NB04 feature engineering
-> NB05 outlier handling / temporal split
-> NB06 baseline modeling
-> NB07 advanced tabular baselines
-> NB08 downstream residual diagnostics
-> NB09 park-level diagnostics / thesis consolidation
-> NB10 graph data-interface / split-to-graph contract / artifact verification
-> NB11 graph-model input packaging / data object preparation
-> NB12 first graph-based forecasting baseline
-> NB13 graph ablation / spatial sensitivity analysis
-> NB14 controlled graph refinement follow-up
```

This means:

- `02_kassel_exploration.ipynb` is the **canonical raw validation authority**.
- `03_eda_master.ipynb` is the **canonical validated-only EDA stage**.
- `04_feature_engineering_and_graph_construction.ipynb` is the **canonical feature-engineering and graph-ready preparation stage**.
- `05_outliers_and_split.ipynb` is the **canonical leakage-aware split stage**.
- `06_baseline_modeling.ipynb` and `07_advanced_baselines_and_importance.ipynb` define the **implemented tabular baseline ladder**.
- `08_residual_diagnostics_and_operating_regimes.ipynb` is a **strict downstream diagnostics stage**, not a new predictive modeling stage.
- `09_park_level_diagnostics_and_thesis_consolidation.ipynb` is a **strict downstream diagnostics / consolidation stage**, not a new predictive modeling stage.
- `10_graph_readiness_and_artifact_verification.ipynb` is a **strict graph data-interface / split-to-graph contract / artifact verification stage**, not a graph-training stage.
- `11_graph_model_input_packaging.ipynb` is a **strict graph-model input packaging / data object preparation stage**, not a training or benchmark-reporting stage.
- `12_first_graph_based_forecasting_baseline.ipynb` is the **first actual graph-based forecasting baseline** of the repository, but it does not validate graph superiority over the canonical benchmark backbone.
- `13_graph_ablation_and_spatial_sensitivity_analysis.ipynb` is a **strict graph ablation / spatial sensitivity follow-up** and should be interpreted as cautious graph evidence rather than superiority proof.
- `14_controlled_graph_refinement_followup.ipynb` is a **strict controlled graph refinement follow-up** and should be interpreted as narrow-scope graph evidence consolidation, not as validated graph superiority.

### Important downstream rule

After `NB02`, downstream notebooks must not perform **loose reparsing** of raw timestamps or reintroduce raw-validation logic.

Downstream stages should consume validated outputs and canonical exported artifacts rather than silently redefining upstream methodological responsibilities.

---

## Operational Helper Clarification

Operational helper modules may be used for loading, feature preparation, artifact reading, or downstream convenience, but they must not be documented as canonical methodological authorities unless the pipeline is explicitly redesigned.

In particular, `KasselLoader` should be treated as an **operational helper** and not as the **canonical strict raw validation layer** of the project.

The canonical raw validation authority remains `NB02`.

---

## Local Demo Helper Clarification

The optional `django_demo/` interface should be treated as a **local-only, read-only, non-production, thesis-facing artifact inspection and presentation helper**.

It may be used to support local review of already exported artifacts, but it must not be documented or presented as:

- a deployed digital twin,
- a production monitoring platform,
- a PHM system,
- an anomaly-detection service,
- a fault-diagnosis system,
- an operational forecasting platform,
- or a security-hardened deployed service.

The local demo should not trigger model training, rerun notebooks, write benchmark results, mutate processed artifacts, or modify canonical outputs.

A contribution to the local demo should preserve:

- local-only execution,
- read-only artifact inspection,
- deterministic artifact-bundle consumption,
- thesis-facing presentation support,
- and non-production wording.

---

## Research Framing Rules

Because this repository is both research-facing and thesis-facing, contribution wording must remain scientifically disciplined.

### 1. Implemented vs planned vs future

When describing contributions, issues, PRs, markdown cells, README updates, logs, or thesis-facing text, clearly separate:

- **Implemented now**
- **Planned next**
- **Future work / research extension**

Do not blur these categories.

### 2. Diagnostics boundary

Residual diagnostics, operating-regime analysis, and park-level diagnostics may support:

- diagnostics-aware interpretation,
- condition-awareness-oriented discussion,
- health-aware discussion,
- PHM-oriented future thinking,
- thesis-facing interpretation of forecasting behavior.

However, they must not be presented as:

- completed PHM functionality,
- validated anomaly detection,
- fault diagnosis,
- prognostics engine,
- RUL estimation,
- production health monitoring,
- or deployed digital twin service.

### 3. Graph verification, packaging, and graph-experiment boundary

Graph data-interface checks, split-to-graph contract validation, artifact-consistency verification, and graph-model input packaging may support:

- graph-readiness claims,
- benchmark-safe graph handoff,
- graph-based forecasting experimentation,
- topology-aware sensitivity analysis,
- and controlled follow-up analysis.

The implemented `NB12`–`NB14` stages may be described as:

- cautious graph-based forecasting evidence,
- topology-aware graph ablation / spatial sensitivity analysis,
- controlled graph refinement follow-up,
- and narrow-scope graph evidence consolidation.

However, they must not be presented as:

- validated graph superiority over the canonical benchmark backbone,
- validated GNN / Graph-Mamba superiority,
- completed graph-learning benchmark beyond the current bounded evidence,
- production-grade graph forecasting functionality,
- or a completed digital twin graph intelligence layer.

### 4. Forecasting remains the implemented core

The repository currently supports:

- benchmark-safe forecasting,
- advanced tabular baseline comparison,
- diagnostics-aware downstream analysis,
- park-level diagnostic consolidation,
- graph data-interface verification,
- graph-model input packaging,
- first graph-based forecasting baseline evidence,
- topology-aware graph ablation / spatial sensitivity follow-up,
- controlled graph refinement follow-up,
- and local thesis-facing artifact inspection through a read-only demo helper.

Broader graph redesign, sequence-based modeling, Mamba / Graph-Mamba experimentation, stronger graph-based forecasting claims, deployed PHM, and deployed digital-twin functionality remain **future work** unless explicitly implemented, evaluated, documented, and justified by evidence.

---

## Benchmark and Reporting Rules

The repository uses a benchmark-safe reporting structure.

### Canonical benchmark artifact

For cross-model reporting, the canonical benchmark artifact is:

```text
data/processed/baseline_metrics.csv
```

Use this artifact as the reporting authority for final test-set benchmark comparisons of the implemented tabular baseline ladder.

### Test-only benchmark interpretation

When reporting final benchmark performance:

- validation should be used for model selection only,
- test should be used for final reporting only,
- benchmark summaries should remain consistent with the canonical exported artifact,
- and final reporting should not mix validation metrics with test-set benchmark claims.

### Graph and diagnostics artifacts are not automatic benchmark authority

Graph-verification, graph-packaging, graph-experiment, diagnostics, prediction, and local demo artifacts must not be confused with the canonical tabular benchmark authority unless explicitly promoted and documented.

The graph stages may have their own bounded exports and interpretation, but they do not redefine `data/processed/baseline_metrics.csv` as a graph benchmark table.

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
- avoid redistributing raw dataset files through this repository unless explicitly permitted,
- clearly distinguish between:
  - source dataset files,
  - local raw files,
  - processed artifacts,
  - derived benchmark outputs,
  - diagnostics outputs,
  - graph-ready verification artifacts,
  - graph-model packaging artifacts,
  - graph experiment outputs,
  - local demo bundles,
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
- do not treat demo bundles as benchmark authority,
- do not commit model binaries or checkpoints unless there is a documented reason,
- and document any exported file that becomes part of the stable workflow.

---

## Documentation Consistency

When a change affects pipeline meaning, notebook roles, benchmark reporting, diagnostics interpretation, graph positioning, local demo interpretation, or forecasting-vs-PHM wording, documentation must be updated in a coordinated way where relevant.

Relevant documentation may include:

- `README.md`
- `LOGS.md`
- `LOGS_ARCHIVE.md`
- `docs/INDEX.md`
- `docs/RESEARCH_SCOPE.md`
- `docs/BASELINE_PROTOCOL.md`
- `docs/PHM_ROADMAP.md`
- notebook markdown cells that describe methodological role or pipeline order
- local demo documentation if the change affects `django_demo/`

### Additional review requirement

If a change affects any of the following, it should be reviewed explicitly for documentation realignment and scope consistency:

- raw validation,
- timestamp parsing,
- coverage / eligibility rules,
- split semantics,
- feature-space definition,
- benchmark interpretation,
- diagnostics positioning,
- graph-ready contracts,
- graph-model input packaging,
- graph-based forecasting evidence,
- graph ablation or controlled graph refinement interpretation,
- local Django demo behavior or wording,
- artifact policy,
- or forecasting vs PHM / digital-twin framing.

---

## Before Submitting a Contribution

Please verify that:

- the relevant notebook(s), script(s), or documentation files are internally consistent,
- no data leakage has been introduced,
- paths remain consistent,
- required exported artifacts are intentional,
- documentation has been updated where needed,
- canonical benchmark or diagnostics wording remains consistent,
- graph-stage wording remains bounded and precise,
- local demo wording remains local-only, read-only, and non-production,
- scope wording does not overclaim repository functionality,
- and `git status` is clean except for intended files.

If your change affects results, please also verify:

- whether metrics changed,
- whether benchmark ranking changed,
- whether residual or park-level diagnostics interpretation changed,
- whether graph-contract interpretation changed,
- whether graph-experiment interpretation changed,
- whether local demo outputs changed,
- and whether those changes should be reflected in logs or docs.

For documentation-only changes, make clear in the PR that no code, notebook execution, benchmark, model, artifact, or result change is introduced.

---

## Pull Requests

If you open a pull request, please include:

1. **What changed**
2. **Why it changed**
3. **Which notebook(s), module(s), scripts, or docs are affected**
4. **Whether metrics changed**
5. **Whether exported artifacts changed**
6. **Whether markdown / README / logs / docs were updated**
7. **Whether the change is implemented work, planned-next scaffolding, or future-facing preparation**
8. **Whether the change affects forecasting, diagnostics, graph stages, local demo behavior, or PHM / digital-twin framing**

Good PRs are:

- small,
- focused,
- easy to review,
- benchmark-safe,
- artifact-safe,
- and explicit about methodological impact.

For documentation-only PRs, state explicitly that the PR does not change:

- code,
- notebooks,
- benchmark protocol,
- model training,
- metrics,
- artifacts,
- results,
- repository structure,
- or scientific scope.

---

## Academic and Research Note

Because this repository supports both **academic thesis work** and a broader **research-oriented forecasting workflow**, methodological correctness is more important than feature quantity.

A contribution that makes the pipeline more scientifically valid, more reproducible, more transparent, or more clearly documented is preferred over one that merely makes it larger.

Academic and research-facing contributions should preserve:

- fair attribution,
- honest reporting of results,
- clear citation of datasets and prior work,
- reproducible methodology,
- transparent use of software tools,
- and careful separation between evidence, interpretation, and future claims.

Thank you for helping improve the project.