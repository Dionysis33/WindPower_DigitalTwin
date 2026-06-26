# Contributing to WindPower_DigitalTwin

Thank you for your interest in contributing to **WindPower_DigitalTwin**.

This repository is a **forecasting-first research repository** for **spatio-temporal wind power forecasting** on the **DaKS / Kassel synthetic wind power dataset**. It supports a reproducible, thesis-ready workflow with downstream residual diagnostics, graph-aware methodological extensions, controlled subset evidence, and cautious future PHM / digital-twin-oriented research.

The current implementation should be read as a **forecasting and diagnostics research pipeline**, not as a completed PHM system, anomaly detector, fault-diagnosis module, RUL estimator, production digital twin, deployed monitoring platform, or operational forecasting service.

At the current stage, the repository is maintained primarily by the author. External contributions are welcome when they preserve the scientific structure, reproducibility requirements, artifact policy, and scope boundaries of the project.

---

## Quick Navigation

| Area | Purpose |
|---|---|
| [Contribution Principles](#contribution-principles) | Core rules for reproducible and claim-safe changes |
| [Useful Contributions](#useful-contributions) | Changes that fit the repository's current direction |
| [Workflow and Evidence Rules](#workflow-and-evidence-rules) | Canonical notebook order, benchmark authority, and evidence boundaries |
| [Development Guidelines](#development-guidelines) | Branches, commits, code style, and notebook discipline |
| [Data and Artifact Policy](#data-and-artifact-policy) | Dataset, generated artifact, and local-output expectations |
| [Documentation and PR Checklist](#documentation-and-pr-checklist) | Required review points before opening a pull request |

---

## Contribution Principles

Every contribution should preserve or improve:

- reproducibility,
- temporal leakage prevention,
- benchmark-safe reporting,
- clear implemented / planned / future distinctions,
- artifact safety,
- local demo non-production wording,
- and careful forecasting-vs-PHM / digital-twin framing.

### Reproducibility first

Contributions should avoid hidden state, undocumented local assumptions, and silent behavior that makes notebooks, scripts, exported artifacts, or documentation difficult to reproduce.

Prefer deterministic behavior where reproducibility matters. If a change depends on local data or generated artifacts, document the required inputs and expected outputs.

### No data leakage

Train / validation / test separation must remain strict.

- Training data is used for model fitting and train-only preprocessing statistics.
- Validation data is used for model or configuration selection.
- Test data is used only for final reporting after selection is fixed.
- Downstream diagnostics must not redefine upstream split logic.
- Graph-aware and subset stages should consume established artifacts rather than silently changing benchmark assumptions.

### Forecasting-first scope discipline

Diagnostics-aware, condition-awareness-oriented, graph-aware, and PHM-oriented interpretation is welcome only when clearly framed as downstream analysis, bounded evidence, or future research.

Do not present the current repository as:

- a completed PHM system,
- a validated anomaly detector,
- a fault-diagnosis module,
- a prognostics engine,
- a remaining useful life estimation system,
- a production digital twin,
- a deployed monitoring platform,
- or an operational forecasting service.

### Evidence separation

Keep these evidence spaces distinct:

- canonical full-dataset tabular benchmark evidence,
- downstream residual diagnostics and park-level diagnostic signals,
- graph-aware forecasting extensions,
- controlled four-park neural and sequence subset evidence,
- local demo and artifact-browser outputs,
- and future work.

XGBoost may be described as the **lowest-MAE model within the implemented canonical full-dataset tabular benchmark space**. Do not generalize that wording into a state-of-the-art claim or a claim about all possible models, graph experiments, subsets, or future sequence work.

---

## Useful Contributions

Useful contributions include:

- bug fixes,
- code cleanup and refactoring,
- reproducibility improvements,
- documentation improvements,
- evaluation utilities,
- notebook-to-module modularization,
- diagnostics utilities,
- visualization improvements,
- benchmark-safe artifact checks,
- additional baseline models that fit the documented roadmap,
- graph-interface or graph-packaging improvements that preserve the canonical pipeline,
- local demo improvements that remain read-only, local-only, non-production, and thesis-facing.

Please avoid contributions that:

- radically redefine the repository scope,
- break notebook reproducibility,
- introduce hidden leakage,
- add undocumented dependencies,
- bypass canonical stage contracts,
- present residual diagnostics as validated health-state inference or confirmed faults,
- present graph stages as validated graph superiority,
- present controlled neural or sequence subset evidence as a replacement for the canonical benchmark,
- present the local Django demo as a deployed digital twin, monitoring platform, PHM system, anomaly-detection system, fault-diagnosis system, or production service,
- commit large raw or generated artifacts without a documented reason,
- or mix implemented results with speculative future claims.

---

## Workflow and Evidence Rules

The current canonical workflow is:

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

`NB01` is historical exploratory context and is not part of the current canonical forecasting pipeline.

### Notebook roles

- `NB02` is the canonical raw validation authority.
- `NB03` is the validated-only EDA stage.
- `NB04` builds feature-engineering and graph-ready preparation artifacts.
- `NB05` defines leakage-aware outlier handling and temporal split artifacts.
- `NB06` and `NB07` define the implemented tabular baseline ladder.
- `NB08` and `NB09` are downstream diagnostics and consolidation stages, not new predictive modeling stages.
- `NB10` and `NB11` verify graph contracts and package graph-model inputs, not graph training or benchmark reporting.
- `NB12` through `NB14` provide cautious graph-based forecasting evidence, ablation, and controlled refinement, not validated graph superiority.

After `NB02`, downstream notebooks should consume validated outputs and canonical artifacts. They should not loosely reparse raw timestamps or reintroduce raw-validation responsibilities.

### Benchmark authority

The canonical benchmark artifact is:

```text
data/processed/baseline_metrics.csv
```

Use this artifact as the reporting authority for final test-set comparisons within the implemented tabular baseline ladder.

Graph outputs, diagnostics outputs, tuning outputs, controlled subset outputs, local demo bundles, model binaries, and checkpoints do not replace this benchmark artifact unless explicitly promoted and documented.

### Diagnostics boundary

Residual diagnostics, operating-regime analysis, and park-level diagnostics may support:

- candidate screening signals,
- diagnostics-aware interpretation,
- condition-awareness-oriented discussion,
- health-aware discussion,
- and PHM-oriented future research framing.

They must not be presented as confirmed faults, validated anomaly detection, fault diagnosis, maintenance prescriptions, RUL estimation, production health monitoring, or deployed PHM functionality.

### Graph and subset boundaries

Graph-aware stages may be described as graph-readiness, graph input packaging, graph-based forecasting experimentation, topology-aware sensitivity analysis, and controlled refinement evidence. They must not be presented as validated graph superiority, validated GNN / Graph-Mamba superiority, production graph forecasting, or a completed digital-twin graph layer.

Controlled neural and sequence experiments are four-park subset evidence only. They can support discussion of experimental readiness and future full-benchmark motivation, but they do not replace `data/processed/baseline_metrics.csv` and should not be merged into the canonical full-dataset benchmark ranking.

### Local demo boundary

The optional `django_demo/` interface is a local-only, read-only, non-production, thesis-facing artifact inspection helper.

It should not train models, rerun notebooks, rewrite benchmark results, mutate processed artifacts, modify canonical outputs, expose raw dataset files, or be described as a deployed digital twin, monitoring system, PHM system, anomaly-detection service, fault-diagnosis system, operational forecasting platform, or public service.

---

## Development Guidelines

### Branches and commits

Use clear branch names such as:

- `fix/...`
- `feat/...`
- `docs/...`
- `chore/...`

Use concise commit messages such as:

- `fix: prevent leakage in baseline feature selection`
- `docs: align governance docs with current README state`
- `chore: update benchmark artifact notes`

For documentation-only governance updates, a good default is:

```text
docs: align governance docs with current repository scope
```

### Code style

Please:

- prefer readable and explicit code over clever shortcuts,
- keep variable names meaningful,
- use comments where scientific intent matters,
- preserve notebook narrative clarity,
- keep technical terminology consistent,
- avoid silent fallbacks that hide methodological problems,
- and avoid changing scientific interpretation through comments alone.

### Notebook policy

When editing notebooks:

- preserve execution order,
- do not leave broken cells,
- avoid hidden assumptions,
- explain major methodological choices in markdown,
- keep outputs informative but not excessively noisy,
- avoid ad hoc exploratory fragments in canonical notebooks,
- keep exported artifacts consistent with the notebook's intended role,
- and update relevant interpretation text if notebook meaning changes.

Notebook changes that affect metrics, artifacts, model behavior, split semantics, graph contracts, or diagnostics interpretation should be handled as methodological changes, not casual cleanup.

Operational helper modules may support loading, feature preparation, artifact reading, or downstream convenience, but they should not be documented as canonical methodological authorities unless the pipeline is explicitly redesigned. In particular, `KasselLoader` is an operational helper; `NB02` remains the canonical raw validation authority.

---

## Data and Artifact Policy

This repository uses the **DaKS synthetic wind power dataset** from the University of Kassel research data repository. Contributors must respect dataset terms, attribution requirements, and redistribution limits.

Do not commit raw dataset files unless explicitly permitted and documented.

Generated outputs should be handled according to their role:

- `data/processed/baseline_metrics.csv` is the canonical tracked benchmark artifact.
- Selected thesis / report-facing figures may be tracked when intentionally promoted.
- Local predictions, diagnostics, graph outputs, subset outputs, rerun exports, and demo bundles should remain local-only unless explicitly reviewed.
- Model binaries, checkpoints, serialized estimators, and training-state files should remain local-only by default.

If a contribution depends on dataset access, explain which files are needed, where they come from, how they should be placed, and how they should be prepared before execution.

---

## Documentation and PR Checklist

When a change affects pipeline meaning, notebook roles, benchmark reporting, diagnostics interpretation, graph positioning, local demo behavior, artifact policy, or forecasting-vs-PHM wording, update the relevant documentation.

Relevant documentation may include:

- `README.md`
- `LOGS.md`
- `LOGS_ARCHIVE.md`
- `docs/INDEX.md`
- `docs/RESEARCH_SCOPE.md`
- `docs/BASELINE_PROTOCOL.md`
- `docs/PHM_ROADMAP.md`
- `docs/wiki_drafts/`
- notebook markdown cells
- local demo documentation

Before submitting a contribution, verify that:

- the relevant files are internally consistent,
- no data leakage has been introduced,
- paths remain explicit and reviewable,
- required exported artifacts are intentional,
- documentation has been updated where needed,
- canonical benchmark wording remains bounded,
- residual diagnostics remain candidate screening / diagnostic signals,
- graph-stage wording remains bounded and precise,
- controlled subset evidence is not promoted into the canonical benchmark,
- local demo wording remains local-only, read-only, and non-production,
- scope wording does not overclaim repository functionality,
- and `git status` is clean except for intended files.

If opening a pull request, include:

1. what changed,
2. why it changed,
3. which files are affected,
4. whether metrics changed,
5. whether exported artifacts changed,
6. whether documentation was updated,
7. whether the change is implemented work, planned-next scaffolding, or future-facing preparation,
8. whether the change affects forecasting, diagnostics, graph stages, controlled subset evidence, local demo behavior, or PHM / digital-twin framing.

For documentation-only PRs, state explicitly that the PR does not change code, notebooks, benchmark protocol, model training, metrics, artifacts, results, repository structure, or scientific scope.

---

## Academic and Research Note

Because this repository supports academic thesis work and a broader research-oriented forecasting workflow, methodological correctness is more important than feature quantity.

Contributions should preserve:

- fair attribution,
- honest reporting of results,
- clear citation of datasets and prior work,
- reproducible methodology,
- transparent use of software tools,
- and careful separation between evidence, interpretation, and future claims.

Thank you for helping improve the project.
