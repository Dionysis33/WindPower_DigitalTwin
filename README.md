# WindPower_DigitalTwin

<p align="center">
  <strong>Forecasting-first research repository for spatio-temporal wind power prediction on the DaKS / Kassel synthetic wind power dataset.</strong>
</p>

<p align="center">
  <a href="https://github.com/Dionysis33/WindPower_DigitalTwin/actions/workflows/python-app.yml">
    <img alt="Python application" src="https://github.com/Dionysis33/WindPower_DigitalTwin/actions/workflows/python-app.yml/badge.svg">
  </a>
  <a href="https://github.com/Dionysis33/WindPower_DigitalTwin/actions/workflows/repo-safety-check.yml">
    <img alt="Repo safety check" src="https://github.com/Dionysis33/WindPower_DigitalTwin/actions/workflows/repo-safety-check.yml/badge.svg">
  </a>
  <a href="./LICENSE">
    <img alt="License: AGPL-3.0" src="https://img.shields.io/badge/license-AGPL--3.0-green.svg">
  </a>
  <a href="https://www.python.org/">
    <img alt="Python 3.12" src="https://img.shields.io/badge/python-3.12-blue.svg">
  </a>
  <a href="./requirements.txt">
    <img alt="Dependencies" src="https://img.shields.io/badge/dependencies-requirements.txt-informational.svg">
  </a>
</p>

<p align="center">
  <a href="./docs/INDEX.md"><img alt="Docs" src="https://img.shields.io/badge/Docs-Index-blue"></a>
  <a href="./docs/RESEARCH_SCOPE.md"><img alt="Research Scope" src="https://img.shields.io/badge/Research-Scope-purple"></a>
  <a href="./docs/DATA.md"><img alt="Data" src="https://img.shields.io/badge/Data-DaKS%20%2F%20Kassel-orange"></a>
  <a href="./docs/BASELINE_PROTOCOL.md"><img alt="Baseline Protocol" src="https://img.shields.io/badge/Baseline-Protocol-success"></a>
  <a href="./docs/PHM_ROADMAP.md"><img alt="PHM Roadmap" src="https://img.shields.io/badge/PHM-Roadmap-lightgrey"></a>
  <a href="./notebooks/"><img alt="Notebooks" src="https://img.shields.io/badge/Jupyter-Notebooks-F37626"></a>
  <a href="./src/"><img alt="Python Source" src="https://img.shields.io/badge/Python-Source%20Code-3776AB"></a>
  <a href="./django_demo/"><img alt="Django Demo" src="https://img.shields.io/badge/Django-Local%20Demo-092E20"></a>
  <a href="./LOGS.md"><img alt="Logs" src="https://img.shields.io/badge/Logs-Active%20Methodological%20Log-yellow"></a>
</p>

---

## Overview

**WindPower_DigitalTwin** is a research repository for **spatio-temporal wind power forecasting** on the **DaKS / Kassel synthetic wind power dataset**.

The repository supports a **forecasting-first, reproducible, thesis-ready pipeline** with emphasis on:

- raw data validation,
- validated-only exploratory data analysis,
- leakage-aware feature engineering,
- strict temporal train / validation / test separation,
- baseline benchmarking,
- downstream residual diagnostics,
- park-level diagnostics,
- graph data-interface verification,
- graph-model input packaging,
- cautious graph-based forecasting experimentation,
- and a non-overclaiming transition toward future PHM / digital-twin-oriented research.

The current implementation should be read as a **forecasting and diagnostics research pipeline**, not as a completed production digital twin, PHM system, fault-diagnosis module, anomaly-detection system, or deployed monitoring service.

---

## Quick Navigation

| Area | Link | Purpose |
|---|---|---|
| Documentation index | [`docs/INDEX.md`](./docs/INDEX.md) | Central guide to repository documentation |
| Research scope | [`docs/RESEARCH_SCOPE.md`](./docs/RESEARCH_SCOPE.md) | Defines implemented work, supplementary evidence, planned next steps, and future work |
| Data documentation | [`docs/DATA.md`](./docs/DATA.md) | Explains DaKS data handling and artifact policy |
| Baseline protocol | [`docs/BASELINE_PROTOCOL.md`](./docs/BASELINE_PROTOCOL.md) | Defines benchmark, split, leakage, and reporting rules |
| PHM roadmap | [`docs/PHM_ROADMAP.md`](./docs/PHM_ROADMAP.md) | Explains the cautious transition from forecasting to PHM-oriented research |
| Active log | [`LOGS.md`](./LOGS.md) | Current canonical methodological progress log |
| Historical log archive | [`LOGS_ARCHIVE.md`](./LOGS_ARCHIVE.md) | Superseded or exploratory history |
| Notebooks | [`notebooks/`](./notebooks/) | Canonical workflow plus bounded supplementary extension notebooks |
| Python source | [`src/`](./src/) | Reusable Python modules |
| Python dependencies | [`requirements.txt`](./requirements.txt) | Python environment requirements |
| Python CI workflow | [`.github/workflows/python-app.yml`](./.github/workflows/python-app.yml) | Python linting and dependency-installation workflow |
| Repo safety workflow | [`.github/workflows/repo-safety-check.yml`](./.github/workflows/repo-safety-check.yml) | Repository safety checks |
| Local demo interface | [`django_demo/`](./django_demo/) | Thesis-facing local read-only artifact browser |
| Demo bundle exporter | [`scripts/export_demo_bundle.py`](./scripts/export_demo_bundle.py) | Deterministic local demo-bundle export helper |
| Contributing | [`CONTRIBUTING.md`](./CONTRIBUTING.md) | Contribution and documentation rules |
| Security | [`SECURITY.md`](./SECURITY.md) | Security and artifact-safety policy |
| Code of Conduct | [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md) | Community and academic conduct expectations |
| License | [`LICENSE`](./LICENSE) | AGPL-3.0 license |

---

## Published Wiki and Repository Mirror

The published Wiki mirror in [`docs/wiki_mirror/`](./docs/wiki_mirror/) provides a compact repository-side navigation layer over the maintained repository documentation. Start with [`Home.md`](./docs/wiki_mirror/Home.md), then use the key pages below for claim-safe review.

| Page | Role |
|---|---|
| [`Research-Scope-and-Claim-Boundaries.md`](./docs/wiki_mirror/Research-Scope-and-Claim-Boundaries.md) | Forecasting-first scope and non-claim boundaries |
| [`Canonical-Forecasting-Workflow.md`](./docs/wiki_mirror/Canonical-Forecasting-Workflow.md) | Canonical workflow summary |
| [`Canonical-Benchmark-and-Tabular-Results.md`](./docs/wiki_mirror/Canonical-Benchmark-and-Tabular-Results.md) | Tabular benchmark authority and XGBoost lowest-MAE wording within the implemented canonical benchmark |
| [`Residual-Diagnostics-and-PHM-Oriented-Interpretation.md`](./docs/wiki_mirror/Residual-Diagnostics-and-PHM-Oriented-Interpretation.md) | Residual diagnostics and NB20/NB21 validation-calibrated interpretation layers |
| [`Graph-Aware-Methodological-Extensions.md`](./docs/wiki_mirror/Graph-Aware-Methodological-Extensions.md) | Bounded graph-aware methodology and evidence |
| [`Controlled-Neural-and-Sequence-Subset-Evidence.md`](./docs/wiki_mirror/Controlled-Neural-and-Sequence-Subset-Evidence.md) | Controlled four-park neural and sequence subset evidence |
| [`Local-Demo-and-Artifact-Browser.md`](./docs/wiki_mirror/Local-Demo-and-Artifact-Browser.md) | Local read-only demo and artifact-browser boundaries |
| [`Repository-Evidence-Hygiene.md`](./docs/wiki_mirror/Repository-Evidence-Hygiene.md) | Evidence, artifact, and documentation hygiene |
| [`Reviewer-FAQ.md`](./docs/wiki_mirror/Reviewer-FAQ.md) | Short reviewer-facing claim-boundary answers |

---

## Current Status

The repository currently implements a **forecasting-first benchmark and diagnostics pipeline** with a controlled graph-aware extension and bounded supplementary extension notebooks.

### Implemented operational core

The current implemented workflow includes:

1. strict raw validation,
2. validated-only and coverage-aware downstream EDA,
3. feature engineering,
4. leakage-aware outlier handling and temporal splitting,
5. baseline modeling,
6. advanced tabular baselines,
7. downstream residual diagnostics,
8. park-level diagnostics and thesis consolidation,
9. graph data-interface / split-to-graph contract verification,
10. graph-model input packaging,
11. first graph-based forecasting baseline,
12. graph ablation / spatial sensitivity analysis,
13. controlled graph refinement follow-up,
14. local thesis-facing Django demo interface for read-only artifact inspection.

### Implemented tabular baseline ladder

The current tabular benchmark backbone includes:

- **Persistence**
- **Linear Regression**
- **Random Forest**
- **XGBoost**
- **MLP**

### Implemented graph-aware extension

The graph-aware extension currently includes:

- `NB10` graph data-interface / split-to-graph contract / artifact verification,
- `NB11` graph-model input packaging / data object preparation,
- `NB12` first graph-based forecasting baseline,
- `NB13` graph ablation / spatial sensitivity follow-up,
- `NB14` controlled graph refinement follow-up.

These stages provide **cautious graph-based forecasting evidence**, but they do **not** establish validated graph superiority over the canonical benchmark backbone.

### Supplementary extension evidence

Post-`NB14` notebooks are supplementary extensions. They are not replacements for the canonical full-dataset workflow or for `data/processed/baseline_metrics.csv`.

The documented supplementary evidence currently includes:

- `NB15`, `NB16`, `NB18`, and `NB19` as controlled four-park neural / sequence subset evidence,
- `NB20` and `NB21` as validation-calibrated residual diagnostic interpretation layers.

`NB17` is present as an unaudited Mamba sequence scaffold. Without a completed reviewed audit document, it should not be promoted as manuscript or reviewer-facing evidence.

---

## Dataset

The project uses the **DaKS / Kassel synthetic wind power dataset** as the primary research dataset.

The DaKS publication describes a synthetic renewable power forecasting dataset containing:

- synthetic but realistic power measurements,
- numerical weather prediction input features,
- timestamps,
- geographic information,
- static power-plant metadata,
- and 273 wind power plants across Germany.

The current repository focuses on the **wind power forecasting** part of the dataset.

### Expected raw data layout

The canonical pipeline expects per-park file pairs in the following style:

```text
data_input_<park_id>.csv
data_target_<park_id>.csv
meta.csv
```

Conceptually:

- `data_input_<park_id>.csv` contains weather / NWP input variables,
- `data_target_<park_id>.csv` contains power target values,
- `meta.csv` contains static metadata and spatial information.

### Data access note

The raw DaKS dataset is **not redistributed inside this repository**.

Users are responsible for obtaining the dataset from the official source and complying with the dataset terms, attribution requirements, license conditions, and academic usage constraints.

See:

- [`docs/DATA.md`](./docs/DATA.md)

---

## Canonical Workflow

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

`NB01` is preserved as historical exploratory context and is not part of the current canonical DaKS forecasting pipeline.

`NB15` through `NB21` are supplementary extensions. They do not replace the canonical `NB02` through `NB14` full-dataset workflow unless a future document explicitly changes that status.

---

## Notebook Guide

| Notebook | Role | Current interpretation |
|---|---|---|
| `01_data_acquisition.ipynb` | Historical exploratory notebook | Not part of the current canonical forecasting pipeline |
| `02_kassel_exploration.ipynb` | Canonical raw validation | Raw decoding, timestamp validation, temporal ordering, duplicate inspection, input-target alignment |
| `03_eda_master.ipynb` | Validated-only EDA | Operates only on the validated / downstream-eligible cohort |
| `04_feature_engineering_and_graph_construction.ipynb` | Feature engineering and graph-ready artifact construction | Builds temporal, cyclic, lag/rolling, spatial, and graph-ready features |
| `05_outliers_and_split.ipynb` | Outlier handling and temporal split | Applies leakage-aware preprocessing and exports train / validation / test splits |
| `06_baseline_modeling.ipynb` | Initial baseline modeling | Persistence and Linear Regression benchmark reporting |
| `07_advanced_baselines_and_importance.ipynb` | Advanced tabular baselines | Random Forest, XGBoost, MLP, feature importance, prediction exports |
| `08_residual_diagnostics_and_operating_regimes.ipynb` | Downstream residual diagnostics | Test-only residual and operating-regime analysis; not a new model |
| `09_park_level_diagnostics_and_thesis_consolidation.ipynb` | Park-level diagnostics | Park-level diagnostic aggregation and thesis-facing consolidation; not a new model |
| `10_graph_readiness_and_artifact_verification.ipynb` | Graph contract verification | Verifies graph/split/artifact consistency; not graph training |
| `11_graph_model_input_packaging.ipynb` | Graph-model input packaging | Prepares graph-ready tensors/data objects; not training or benchmarking |
| `12_first_graph_based_forecasting_baseline.ipynb` | First graph-based forecasting baseline | First actual graph-based forecasting experiment |
| `13_graph_ablation_and_spatial_sensitivity_analysis.ipynb` | Graph ablation and spatial sensitivity | Topology-aware follow-up; cautious graph evidence only |
| `14_controlled_graph_refinement_followup.ipynb` | Controlled graph refinement follow-up | Narrow-scope graph-only follow-up; evidence consolidation, not superiority validation |
| `15_nn_sequence_baseline_subset.ipynb` | Controlled GRU sequence subset extension | Audited controlled four-park sequence subset evidence only; not a full-dataset benchmark replacement |
| `16_nn_lstm_sequence_subset.ipynb` | Controlled LSTM sequence subset extension | Audited controlled four-park sequence subset evidence only; not a full-dataset benchmark replacement |
| `17_mamba_sequence_baseline_subset.ipynb` | Mamba sequence scaffold | Unaudited supplementary scaffold only; not completed reviewer-facing evidence |
| `18_tcn_sequence_baseline_subset.ipynb` | Controlled TCN sequence subset extension | Audited controlled four-park sequence subset evidence only; not a full-dataset benchmark replacement |
| `19_patchtst_sequence_subset.ipynb` | Controlled sequence-aligned subset extension | Audited PatchTST-Lite and flattened-window XGBoost sequence subset evidence only |
| `20_residual_phm_diagnostics.ipynb` | Residual diagnostic interpretation extension | Validation-calibrated residual diagnostics over forecasting outputs; not validated PHM or fault diagnosis |
| `21_strong_model_residual_phm_diagnostics.ipynb` | Strong-model residual diagnostic extension | Validation-calibrated residual diagnostics with a stronger residual source; not a canonical benchmark replacement |

The `NB15` through `NB21` rows are supplementary categories. They should remain separated from the canonical full-dataset benchmark unless a future reviewed document explicitly promotes a new workflow.

---

## Split and Evaluation Protocol

The repository follows a **strict temporal split** rather than a random split.

The evaluation protocol follows these principles:

- validation is used for model selection,
- test data is used only for final reporting,
- preprocessing statistics must not leak information from validation or test into training,
- benchmark comparisons must use consistent feature space and consistent evaluation keys,
- final benchmark reporting is test-only.

The canonical benchmark artifact is:

```text
data/processed/baseline_metrics.csv
```

This file is the public benchmark authority for the implemented tabular baseline ladder.

Graph-verification, graph-packaging, diagnostics, and graph-experiment outputs must not be confused with the canonical tabular benchmark authority unless explicitly promoted and documented.

See:

- [`docs/BASELINE_PROTOCOL.md`](./docs/BASELINE_PROTOCOL.md)

---

## Repository Structure

The current public repository structure is summarized below; the current `notebooks/` inventory is listed separately after the compact tree.

```text
WindPower_DigitalTwin/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/
│   │   ├── python-app.yml
│   │   └── repo-safety-check.yml
│   ├── dependabot.yml
│   └── pull_request_template.md
├── data/
├── django_demo/
├── docs/
│   ├── BASELINE_PROTOCOL.md
│   ├── DATA.md
│   ├── INDEX.md
│   ├── PHM_ROADMAP.md
│   └── RESEARCH_SCOPE.md
├── notebooks/
│   ├── 01_data_acquisition.ipynb
│   ├── 02_kassel_exploration.ipynb
│   ├── 03_eda_master.ipynb
│   ├── 04_feature_engineering_and_graph_construction.ipynb
│   ├── 05_outliers_and_split.ipynb
│   ├── 06_baseline_modeling.ipynb
│   ├── 07_advanced_baselines_and_importance.ipynb
│   ├── 08_residual_diagnostics_and_operating_regimes.ipynb
│   ├── 09_park_level_diagnostics_and_thesis_consolidation.ipynb
│   ├── 10_graph_readiness_and_artifact_verification.ipynb
│   ├── 11_graph_model_input_packaging.ipynb
│   ├── 12_first_graph_based_forecasting_baseline.ipynb
│   ├── 13_graph_ablation_and_spatial_sensitivity_analysis.ipynb
│   └── 14_controlled_graph_refinement_followup.ipynb
├── scripts/
│   └── export_demo_bundle.py
├── src/
│   ├── data/
│   ├── features/
│   ├── __init__.py
│   └── config.py
├── .gitattributes
├── .gitignore
├── CITATION.cff
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── LOGS.md
├── LOGS_ARCHIVE.md
├── README.md
├── requirements.txt
└── SECURITY.md
```

Current `notebooks/` inventory:

```text
01_data_acquisition.ipynb
02_kassel_exploration.ipynb
03_eda_master.ipynb
04_feature_engineering_and_graph_construction.ipynb
05_outliers_and_split.ipynb
06_baseline_modeling.ipynb
07_advanced_baselines_and_importance.ipynb
08_residual_diagnostics_and_operating_regimes.ipynb
09_park_level_diagnostics_and_thesis_consolidation.ipynb
10_graph_readiness_and_artifact_verification.ipynb
11_graph_model_input_packaging.ipynb
12_first_graph_based_forecasting_baseline.ipynb
13_graph_ablation_and_spatial_sensitivity_analysis.ipynb
14_controlled_graph_refinement_followup.ipynb
15_nn_sequence_baseline_subset.ipynb
16_nn_lstm_sequence_subset.ipynb
17_mamba_sequence_baseline_subset.ipynb
18_tcn_sequence_baseline_subset.ipynb
19_patchtst_sequence_subset.ipynb
20_residual_phm_diagnostics.ipynb
21_strong_model_residual_phm_diagnostics.ipynb
```

---

## Artifact Policy

The repository separates artifacts into four categories.

### 1. Canonical tracked benchmark artifact

```text
data/processed/baseline_metrics.csv
```

This is the canonical public benchmark artifact for final test-set reporting of the implemented tabular baseline ladder.

### 2. Selected thesis / report-facing artifacts

Selected figures or small outputs may be tracked only when they are intentionally promoted for documentation, reporting, or thesis narrative.

Typical location:

```text
reports/figures/
```

This directory should not be used as a general notebook plot dump.

### 3. Local rerun / diagnostics artifacts

Large rerun outputs, predictions, diagnostics bundles, graph exports, and notebook-native exports should generally remain local-only unless explicitly documented otherwise.

Examples include:

```text
data/processed/predictions/
data/processed/diagnostics/
data/processed/graph/
```

### 4. Local-only model artifacts

Model binaries, checkpoints, serialized estimators, and training-state files should remain local-only by default.

Typical location:

```text
models/local/
```

These artifacts are not benchmark authority and should not be confused with report-facing outputs.

---

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/Dionysis33/WindPower_DigitalTwin.git
cd WindPower_DigitalTwin
```

### 2. Create a Python environment

```bash
python -m venv venv
```

Activate it:

```powershell
# Windows PowerShell
.\venv\Scripts\Activate.ps1
```

```bash
# Linux / macOS
source venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Start JupyterLab

```bash
jupyter lab
```

### 5. Place the raw dataset locally

Place the DaKS / Kassel raw files under:

```text
data/raw/kassel_dataset/
```

Expected contents include:

```text
data_input_<park_id>.csv
data_target_<park_id>.csv
meta.csv
```

The raw dataset is intentionally not redistributed through this repository.

---

## Quick Start

Recommended canonical execution order:

1. Run `02_kassel_exploration.ipynb`
2. Run `03_eda_master.ipynb`
3. Run `04_feature_engineering_and_graph_construction.ipynb`
4. Run `05_outliers_and_split.ipynb`
5. Run `06_baseline_modeling.ipynb`
6. Run `07_advanced_baselines_and_importance.ipynb`
7. Run `08_residual_diagnostics_and_operating_regimes.ipynb`
8. Run `09_park_level_diagnostics_and_thesis_consolidation.ipynb`
9. Run `10_graph_readiness_and_artifact_verification.ipynb`
10. Run `11_graph_model_input_packaging.ipynb`
11. Run `12_first_graph_based_forecasting_baseline.ipynb`
12. Run `13_graph_ablation_and_spatial_sensitivity_analysis.ipynb`
13. Run `14_controlled_graph_refinement_followup.ipynb`

Important execution notes:

- `NB02` is the canonical raw validation authority of the repository.
- `NB03` should run only after the upstream validation outputs of `NB02` are available.
- Downstream notebooks should preserve the established validation, split, and artifact contracts.
- Graph-related notebooks should not overwrite the canonical tabular benchmark authority unless explicitly documented.
- `NB15` through `NB21` are supplementary extensions and are not part of the recommended canonical execution order.
- `NB17` should be treated as an unaudited scaffold unless a reviewed audit document is added.

---

## Optional Local Django Demo

The repository includes a lightweight local Django demo under:

```text
django_demo/
```

This interface is intended as a **read-only thesis-facing artifact browser** over already exported local artifacts.

It should be interpreted as:

- a local presentation helper,
- a thesis/demo support interface,
- and a non-production artifact browser.

It should **not** be interpreted as:

- a deployed digital twin,
- a production monitoring service,
- a PHM system,
- a new forecasting benchmark stage,
- or an operational forecasting platform.

A typical local flow is:

```bash
python scripts/export_demo_bundle.py
cd django_demo
python manage.py runserver
```

The demo should read curated local exports only. It should not trigger training, rerun notebooks, write benchmark results, or modify canonical artifacts.

---

## Research Framing

The repository follows a staged research framing:

```text
forecasting benchmark backbone
-> downstream residual diagnostics
-> park-level diagnostic consolidation
-> graph contract verification
-> graph-model input packaging
-> first graph-based forecasting baseline
-> topology-aware graph ablation
-> controlled graph refinement follow-up
-> supplementary controlled neural / sequence subset evidence
-> supplementary residual diagnostic interpretation layers
-> future condition-awareness / PHM-oriented research
```

### What is already implemented

- DaKS raw validation and validated-only downstream processing
- leakage-aware feature engineering
- temporal splitting
- tabular baseline ladder
- advanced tabular baselines
- residual diagnostics
- park-level diagnostics
- graph contract verification
- graph-model input packaging
- first graph-based forecasting baseline
- graph ablation / spatial sensitivity analysis
- controlled graph refinement follow-up
- controlled four-park neural / sequence subset evidence for `NB15`, `NB16`, `NB18`, and `NB19`
- validation-calibrated residual diagnostic interpretation layers for `NB20` and `NB21`
- an unaudited supplementary Mamba sequence scaffold in `NB17`
- local read-only Django demo interface

### Planned next

The immediate planned direction is:

- repository-safe artifact organization,
- thesis-facing cleanup,
- maintenance of the canonical-vs-supplementary documentation boundary,
- and scope-safe planning for broader graph, neural, sequence, or residual-diagnostic work only if justified by reviewed evidence.

### Future work

The following remain future work / research extensions:

- broader graph redesign,
- stronger graph-based forecasting claims only if supported by new evidence,
- broader neural / sequence forecasting beyond the controlled four-park subset evidence,
- completed and audited Mamba / Graph-Mamba evidence beyond the unaudited `NB17` scaffold,
- stronger digital-twin integration,
- broader prognostics / PHM-oriented modeling,
- deployed PHM implementation,
- and deployed digital twin implementation.

---

## Scientific Boundaries

The current repository does **not** claim to provide:

- a completed PHM system,
- a validated anomaly detector,
- a fault-diagnosis module,
- remaining useful life estimation,
- production-grade health monitoring,
- validated neural / sequence model superiority,
- validated GNN / Graph-Mamba superiority,
- a deployed digital twin service,
- or a production forecasting platform.

The implemented diagnostics, graph-aware stages, and bounded supplementary extensions should be interpreted as:

- benchmark-safe extensions of the forecasting pipeline,
- diagnostic signal candidates,
- cautious graph-based forecasting evidence,
- controlled four-park neural / sequence subset evidence,
- validation-calibrated residual diagnostic interpretation layers,
- and methodological infrastructure for future condition-awareness and PHM-oriented research.

---

## Development and Contribution Rules

Please read:

- [`CONTRIBUTING.md`](./CONTRIBUTING.md)
- [`SECURITY.md`](./SECURITY.md)
- [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md)

Core contribution principles:

- reproducibility first,
- no temporal leakage,
- benchmark-safe reporting,
- clear separation between implemented work, planned next steps, and future research,
- documentation updates when workflow meaning changes,
- no overclaiming of diagnostics, graph, PHM, or digital-twin functionality.

---

## Logs and Progress Tracking

Repository progress is tracked in:

```text
LOGS.md
LOGS_ARCHIVE.md
```

- [`LOGS.md`](./LOGS.md) is the active canonical methodological log.
- [`LOGS_ARCHIVE.md`](./LOGS_ARCHIVE.md) stores historical, exploratory, or superseded entries.

For current thesis-ready status, treat [`LOGS.md`](./LOGS.md) as the active reference.

---

## Citation and Attribution

This repository is built around the DaKS / Kassel synthetic renewable power forecasting dataset.

Primary dataset reference:

```text
Vogt, S., Schreiber, J. and Sick, B. (2022).
Synthetic Photovoltaic and Wind Power Forecasting Data.
arXiv:2204.00411.
```

Please also see the repository citation metadata when available:

```text
CITATION.cff
```

---

## License

This repository is released under the **AGPL-3.0** license.

See:

- [`LICENSE`](./LICENSE)
