# Contributing to WindPower_DigitalTwin

Thank you for your interest in contributing to **WindPower_DigitalTwin**.

This repository is part of an undergraduate research project focused on **spatio-temporal wind power forecasting** using the **DaKS synthetic wind power dataset** and a modeling pipeline that progresses from **data preparation and baseline benchmarking** toward more advanced models such as **XGBoost, MLP, GNN, and Mamba-inspired architectures**.

At the current stage, the repository is maintained primarily by the author. External contributions are welcome, but they should respect the scientific structure, reproducibility requirements, and academic scope of the project.

---

## Contribution Principles

Please make sure that every contribution follows these principles:

- **Reproducibility first**  
  Any change must preserve or improve reproducibility of the notebooks and the modeling pipeline.

- **No data leakage**  
  Temporal integrity is critical. Train / validation / test separation must remain strictly correct.

- **Research consistency**  
  Contributions should align with the repository roadmap:
  - data preprocessing,
  - baseline modeling,
  - advanced ML baselines,
  - graph-based and sequence-based forecasting models.

- **Documentation quality**  
  Important changes should be reflected in:
  - notebook markdown explanations,
  - `README.md`,
  - `LOGS.md`, when relevant.

---

## Types of Contributions

The most useful contributions are:

- bug fixes,
- code cleanup and refactoring,
- better documentation,
- reproducibility improvements,
- evaluation utilities,
- visualization improvements,
- modularization of notebooks into reusable Python code,
- additional benchmark models that fit the repository roadmap.

At this phase, please avoid contributions that:

- radically change the project scope,
- break notebook reproducibility,
- introduce hidden leakage,
- add undocumented dependencies,
- commit large raw/generated artifacts without a strong reason.

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
- `docs/update-notebook06-summary`

### Commit Style
Use concise and meaningful commit messages.

Recommended format:

- `feat: add random forest benchmark`
- `fix: prevent leakage in baseline feature selection`
- `docs: refine notebook 06 conclusion`
- `chore: update baseline metrics csv`

### Coding Style
Please follow these rules:

- prefer readable and explicit code over clever shortcuts,
- keep variable names meaningful,
- use comments where scientific intent matters,
- preserve notebook narrative clarity,
- keep English terminology for technical concepts when appropriate.

### Notebook Policy
When editing notebooks:

- preserve execution order,
- do not leave broken cells,
- avoid hidden assumptions,
- explain major methodological choices in markdown,
- keep outputs informative but not excessively noisy.

If a notebook change affects results, update the relevant interpretation text as well.

---

## Data Policy

This repository uses the **DaKS synthetic wind power dataset** from the University of Kassel research data repository.

Contributors must:

- respect the original dataset attribution requirements,
- avoid misrepresenting the dataset as original raw proprietary data,
- clearly distinguish between:
  - source dataset files,
  - processed artifacts,
  - derived benchmark outputs.

If a contribution depends on dataset access, explain clearly:

- which files are needed,
- where they come from,
- and how they should be prepared.

---

## Before Submitting a Contribution

Please verify that:

- the relevant notebook(s) run successfully,
- no data leakage has been introduced,
- paths remain consistent,
- generated outputs are intentional,
- documentation has been updated where needed,
- `git status` is clean except for intended files.

---

## Pull Requests

If you open a pull request, please include:

1. **What changed**
2. **Why it changed**
3. **Which notebook(s) or module(s) are affected**
4. **Whether metrics changed**
5. **Whether markdown / README / logs were updated**

Good PRs are small, focused, and easy to review.

---

## Academic Note

Because this repository supports an academic thesis workflow, methodological correctness is more important than feature quantity.

A contribution that makes the pipeline more scientifically valid is preferred over one that merely makes it larger.

Thank you for helping improve the project.