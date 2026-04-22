# WindPower_DigitalTwin

[![Build Status](https://github.com/Dionysis33/WindPower_DigitalTwin/actions/workflows/python-app.yml/badge.svg)](https://github.com/Dionysis33/WindPower_DigitalTwin/actions/workflows/python-app.yml)
[![License](https://img.shields.io/badge/license-AGPL--v3-green.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)

Research repository για **spatio-temporal wind power forecasting** πάνω στο **DaKS / Kassel synthetic wind power dataset**.

Υποστηρίζει ένα **forecasting-first, reproducible και thesis-ready pipeline** με έμφαση σε:

- raw validation,
- validated-only downstream EDA,
- feature engineering,
- leakage-aware temporal splitting,
- baseline benchmarking,
- downstream residual and park-level diagnostics,
- και cautious graph-aware extension με benchmark-safe και non-overclaiming framing.

> Current focus: ένα καθαρό και repository-consistent forecasting backbone, σαφής διάκριση ανάμεσα σε canonical benchmark artifacts, thesis-facing figures και local rerun outputs, και προσεκτική επέκταση από downstream diagnostics και graph-aware forecasting evaluation προς broader PHM-oriented και digital-twin-oriented future research directions.

---

## Project Status

Το repository υποστηρίζει ένα **forecasting-first, thesis-ready research pipeline** πάνω στο **DaKS / Kassel synthetic wind power dataset**.

### Implemented operational core

Στην current canonical μορφή του, το implemented workflow περιλαμβάνει:

- strict raw validation,
- validated-only and coverage-aware downstream EDA,
- feature engineering,
- leakage-aware outlier handling and temporal split,
- baseline benchmarking,
- advanced tabular baselines,
- downstream residual diagnostics,
- park-level diagnostics and thesis-oriented consolidation,
- graph data-interface / split-to-graph contract / artifact verification,
- graph-model input packaging / data object preparation,
- first graph-based forecasting baseline,
- graph ablation / spatial sensitivity follow-up,
- και controlled graph refinement follow-up.

Η current implemented baseline ladder περιλαμβάνει:

- **Persistence**
- **Linear Regression**
- **Random Forest**
- **XGBoost**
- **MLP**

### Current graph-aware extension

Πάνω στο benchmarked forecasting stack, το repository περιλαμβάνει πλέον ένα implemented downstream / graph-aware extension path που εκτείνεται από:

- `NB08` residual diagnostics
- `NB09` park-level diagnostics and thesis consolidation
- `NB10` graph data-interface / split-to-graph contract / artifact verification
- `NB11` graph-model input packaging / data object preparation
- `NB12` first graph-based forecasting baseline
- `NB13` graph ablation / spatial sensitivity follow-up
- `NB14` controlled graph refinement follow-up

Αυτό το extension path:

- χρησιμοποιεί canonical exported artifacts και benchmark-safe evaluation logic,
- διατηρεί validation-only model selection και test-only final reporting όπου υπάρχει model fitting,
- επεκτείνει το repository από downstream diagnostics και graph-readiness σε cautious graph-based forecasting evaluation,
- αλλά παραμένει forecasting-first και non-overclaiming,
- και **δεν** τεκμηριώνει ακόμη validated graph superiority έναντι του canonical benchmark backbone.

### Current interpretation boundary

Στο παρόν στάδιο, το **forecasting** παραμένει ο implemented core άξονας του repository.

Τα downstream diagnostics και τα graph-aware stages του current workflow πρέπει να διαβάζονται ως:

- benchmark-safe extensions του forecasting pipeline,
- cautious diagnostics-aware και condition-awareness-oriented interpretation layers,
- και methodological infrastructure για επόμενη research extension,

όχι ως completed PHM system, validated anomaly-detection or fault-diagnosis module, validated graph superiority result, ή completed digital twin implementation.

Ειδικά το `NB14` πρέπει να διαβάζεται ως:

- controlled graph refinement follow-up,
- narrow-scope post-`NB13` graph-only extension,
- benchmark-safe evidence-consolidation step,

και όχι ως broad graph benchmark suite ή graph superiority validation stage.

---

## Main Dataset

### DaKS Dataset (primary source)

Το project βασίζεται στο **DaKS / Kassel synthetic wind power dataset**.

Το current canonical pipeline χρησιμοποιεί raw per-park CSV pairs της μορφής:

- `data_input_<park_id>.csv` για weather / NWP variables
- `data_target_<park_id>.csv` για power targets
- `meta.csv` για park metadata και spatial information

### Canonical raw validation authority

Η canonical authority για:

- raw decoding,
- timestamp parsing verification,
- temporal ordering checks,
- duplicate timestamp inspection,
- και input-target alignment

είναι το `02_kassel_exploration.ipynb`, το οποίο λειτουργεί ως **canonical raw validation gate** του repository.

### Operational helper clarification

Ο `KasselLoader` χρησιμοποιείται ως **operational helper** για loading και downstream feature-preparation convenience.

Δεν πρέπει να αντιμετωπίζεται ως canonical methodological authority του project.

### Historical exploratory context

Το `Renewables.ninja` ανήκει στην πρώιμη exploratory φάση του repository και διατηρείται μόνο ως historical context.

Δεν αποτελεί active primary data source του current canonical forecasting pipeline.

---

## Canonical Implemented Pipeline

### 1. Canonical raw validation (`NB02`)

Το `02_kassel_exploration.ipynb` αποτελεί το **canonical raw validation stage** του pipeline.

Ο ρόλος του περιορίζεται σε:

- raw decoding,
- timestamp parsing verification,
- temporal ordering checks,
- duplicate timestamp inspection,
- και strict input-target alignment ανά `park_id`.

### 2. Canonical validated-only EDA (`NB03`)

Το `03_eda_master.ipynb` αποτελεί το **canonical validated-only EDA stage**.

Διαβάζει τα upstream validation artifacts του `NB02` και συνεχίζει μόνο με το **validated / NB04-eligible downstream cohort**.  
Δεν λειτουργεί ως raw validation / cleaning notebook.

### 3. Feature engineering (`NB04`)

Το `04_feature_engineering_and_graph_construction.ipynb` καλύπτει:

- temporal feature engineering,
- cyclical time encoding,
- lag / rolling features,
- spatial metadata integration,
- graph-ready artifact construction,
- και export του engineered dataset.

### 4. Outlier handling and temporal splitting (`NB05`)

Το `05_outliers_and_split.ipynb` εφαρμόζει:

- leakage-aware outlier handling,
- strict temporal split,
- και export των:
  - `train_final.csv`
  - `val_final.csv`
  - `test_final.csv`

### 5. Baseline modeling (`NB06`)

Το `06_baseline_modeling.ipynb` καλύπτει:

- Persistence
- Linear Regression
- baseline comparison
- test-only benchmark reporting
- forecasting-oriented residual diagnostics
- actual-vs-predicted analysis

### 6. Advanced tabular baselines (`NB07`)

Το `07_advanced_baselines_and_importance.ipynb` καλύπτει:

- Random Forest
- XGBoost
- MLP
- validation-only model selection
- test-only benchmark update
- residual plots
- feature-importance analysis
- benchmark-safe prediction export για downstream diagnostics

### 7. Downstream residual diagnostics and operating regimes (`NB08`)

Το `08_residual_diagnostics_and_operating_regimes.ipynb` αποτελεί **strict downstream diagnostics notebook** πάνω στα exported baseline predictions.

Ο ρόλος του περιορίζεται σε:

- residual-distribution analysis,
- operating-regime slicing,
- underprediction / overprediction inspection,
- diagnostics-aware comparison των implemented baselines,
- και health-aware / condition-awareness-oriented interpretation χωρίς PHM overclaiming.

Το `NB08` **δεν** είναι νέο modeling stage.

### 8. Park-level diagnostics and thesis consolidation (`NB09`)

Το `09_park_level_diagnostics_and_thesis_consolidation.ipynb` αποτελεί **strict downstream diagnostics and consolidation notebook** πάνω στο canonical test-only evaluation space.

Ο ρόλος του περιορίζεται σε:

- per-park diagnostic aggregation across implemented baselines,
- park-level bias / spread / difficulty analysis,
- comparative park-space summaries και representative case studies,
- thesis-ready consolidation του diagnostics layer,
- και cautious health-aware / PHM-oriented interpretation χωρίς overclaiming.

Το `NB09` **δεν** είναι νέο modeling stage.

### 9. Graph data-interface / split-to-graph contract / artifact verification (`NB10`)

Το `10_graph_readiness_and_artifact_verification.ipynb` αποτελεί **strict graph-readiness verification notebook** πάνω στα canonical upstream artifacts του forecasting pipeline.

Ο ρόλος του περιορίζεται σε:

- verification του graph data-interface,
- split-to-graph contract checks,
- artifact-consistency verification,
- benchmark-safe handoff προς future graph-based forecasting stages,
- και repository-safe confirmation ότι η graph-ready pipeline δεν σπάει το established forecasting contract.

Το `NB10` **δεν** είναι graph model training stage.  
Δεν υλοποιεί ακόμη GNN benchmarking, Graph-Mamba experimentation ή νέο predictive model.

### 10. Graph-model input packaging / data object preparation (`NB11`)

Το `11_graph_model_input_packaging.ipynb` αποτελεί **strict graph-model input packaging / data object preparation notebook** πάνω στα canonical split και graph artifacts του forecasting pipeline.

Ο ρόλος του περιορίζεται σε:

- deterministic loading των canonical split artifacts,
- feature-role και node-role manifesting,
- coverage-aware graph-model input packaging,
- `observed_mask`-aware tensor preparation,
- portable serialized graph-ready dataset export,
- και benchmark-safe handoff προς future graph-based forecasting stages.

Το `NB11` **δεν** είναι training notebook.  
Δεν κάνει benchmarking.  
Δεν αλλάζει το `data/processed/baseline_metrics.csv`.  
Δεν παρέχει ακόμη graph-learning evidence ή νέο predictive result.

### Split protocol note

Η active split strategy παραμένει **strict temporal split**:

- **Train:** up to `2019-12-31 23:00:00`
- **Validation:** up to `2020-06-30 23:00:00`
- **Test:** from `2020-07-01` onward

Για methodological wording consistency, το validation πρέπει να περιγράφεται ως **το τελικό χρονικό tail του pre-test window** και όχι ως stronger claim τύπου **τελευταίο contiguous χρονικό block**.

---

## Canonical Baseline Benchmark Artifact

Το current cross-model benchmark table αποθηκεύεται στο:

```text
data/processed/baseline_metrics.csv
```

Το artifact αυτό παραμένει η **canonical authority** για final test-set benchmark reporting σε όλη την implemented baseline ladder.

---

## Current Public Repository Structure

The following tree reflects the **current public repository structure**.

It should be read as the **currently tracked public tree** of the repository, not as the full local workspace layout.  
Proposed artifact subfolders discussed in `docs/DATA.md` belong to the current cleanup pass and should not be interpreted as already created unless they are explicitly added in a later step.

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

---

## Notebook Guide

Το παρακάτω guide συνοψίζει τον ρόλο κάθε notebook μέσα στο **current canonical workflow** του repository.

### `01_data_acquisition.ipynb`

Historical exploratory notebook για external-data experiments.

Δεν αποτελεί μέρος του current canonical forecasting pipeline.

### `02_kassel_exploration.ipynb`

Canonical raw validation authority του DaKS pipeline.

Καλύπτει:

- raw decoding,
- timestamp parsing verification,
- temporal ordering checks,
- duplicate timestamp inspection,
- και strict input-target alignment ανά `park_id`.

### `03_eda_master.ipynb`

Canonical validated-only EDA stage που λειτουργεί πάνω στο upstream validation contract του `NB02` και στο canonical validated / `NB04`-eligible cohort.

Δεν αποτελεί raw validation ή cleaning notebook.

### `04_feature_engineering_and_graph_construction.ipynb`

Canonical feature-engineering stage του workflow.

Καλύπτει:

- temporal feature engineering,
- cyclical time encoding,
- lag / rolling features,
- spatial metadata integration,
- graph-ready artifact construction,
- και export του engineered dataset.

### `05_outliers_and_split.ipynb`

Canonical leakage-aware split stage του workflow.

Καλύπτει:

- leakage-aware outlier handling,
- strict temporal split,
- και export των canonical:
  - `train_final.csv`
  - `val_final.csv`
  - `test_final.csv`

### `06_baseline_modeling.ipynb`

Baseline modeling notebook για τα πρώτα implemented reference models.

Καλύπτει:

- Persistence,
- Linear Regression,
- baseline comparison,
- test-only benchmark reporting,
- forecasting-oriented residual analysis,
- και actual-vs-predicted plots.

### `07_advanced_baselines_and_importance.ipynb`

Advanced tabular baseline notebook του implemented benchmark stack.

Καλύπτει:

- Random Forest,
- XGBoost,
- MLP,
- validation-only model selection,
- test-only benchmark update,
- residual plots,
- feature-importance analysis,
- και prediction export για downstream diagnostics.

### `08_residual_diagnostics_and_operating_regimes.ipynb`

Strict downstream residual diagnostics notebook πάνω στα exported baseline predictions.

Καλύπτει:

- cross-model residual diagnostics,
- operating-regime-aware error slicing,
- regime-wise benchmark interpretation,
- και cautious health-aware / PHM-aware discussion χωρίς overclaiming.

Δεν αποτελεί νέο modeling stage.

### `09_park_level_diagnostics_and_thesis_consolidation.ipynb`

Strict downstream park-level diagnostics και thesis-consolidation notebook πάνω στο canonical test-only evaluation space.

Καλύπτει:

- per-park diagnostic aggregation,
- bias / spread / difficulty inspection across parks,
- comparative case-study selection,
- thesis-ready consolidation του diagnostics layer,
- και cautious health-aware / PHM-aware interpretation χωρίς overclaiming.

Δεν αποτελεί νέο modeling stage.

### `10_graph_readiness_and_artifact_verification.ipynb`

Strict graph data-interface / split-to-graph contract / artifact-verification notebook.

Καλύπτει:

- graph-ready data-interface verification,
- split-to-graph contract checks,
- graph artifact consistency checks,
- και benchmark-safe readiness for future graph-based forecasting work.

Δεν αποτελεί νέο graph-training stage.

### `11_graph_model_input_packaging.ipynb`

Strict graph-model input packaging / data object preparation notebook.

Καλύπτει:

- deterministic loading των canonical split και graph artifacts,
- feature-role και node-role manifesting,
- coverage-aware graph-model input packaging,
- `observed_mask`-aware tensor preparation,
- portable serialized graph-ready dataset export,
- και benchmark-safe handoff προς future graph-based forecasting work.

Δεν αποτελεί training notebook.
Δεν αποτελεί benchmarking notebook.
Δεν αλλάζει το `data/processed/baseline_metrics.csv`.
Δεν αποτελεί graph-learning evidence.

### `12_first_graph_based_forecasting_baseline.ipynb`

First actual graph-based forecasting baseline του repository πάνω στα canonical packaged graph artifacts του `NB11`.

Καλύπτει:

- fail-fast integrity checks για τα packaged graph inputs,
- snapshot-level graph dataset construction,
- benchmark-safe DataLoader materialization,
- minimal graph-based forecasting baseline execution,
- validation-only model selection,
- test-only final reporting,
- και compact graph-baseline export layer.

Αποτελεί implemented graph-based forecasting evidence, αλλά δεν τεκμηριώνει validated graph superiority έναντι του canonical tabular benchmark backbone.

### `13_graph_ablation_and_spatial_sensitivity_analysis.ipynb`

Strict follow-up notebook του `NB12` για graph ablation / spatial sensitivity analysis.

Καλύπτει:

- canonical artifact loading και fail-fast integrity checks,
- explicit experiment registry με frozen `NB12`-compatible training configuration,
- deterministic topology variants,
- topology-aware dataset / DataLoader materialization,
- controlled GCN execution με validation-only model selection και test-only final reporting,
- και compact export layer για validation summary, test metrics, training history και reference comparison.

Αποτελεί topology-aware follow-up evidence, αλλά δεν στηρίζει strong graph superiority claims.

### `14_controlled_graph_refinement_followup.ipynb`

Strict post-`NB13` controlled graph refinement notebook που λειτουργεί ως narrow-scope benchmark-safe follow-up.

Καλύπτει:

- canonical artifact loading και read-only reference policy,
- strict comparison boundary μόνο απέναντι σε `NB12` reference και `NB13` best configuration,
- predeclared experiment registry γύρω από controlled pruning-strength refinement,
- deterministic refined edge-bundle construction,
- validation-only model selection,
- test-only final reporting για το validation-selected experiment,
- strict reference comparison απέναντι σε `NB12` και `NB13`,
- και final sanity test για benchmark-contract integrity.

Αποτελεί controlled graph refinement follow-up evidence-consolidation stage, αλλά δεν συνιστά broad graph benchmark suite, validated graph superiority result, PHM stage, ή completed digital twin implementation stage.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Dionysis33/WindPower_DigitalTwin.git
cd WindPower_DigitalTwin
```

### 2. Create and activate a virtual environment

**Windows (PowerShell)**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux / macOS**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Launch Jupyter Lab

```bash
jupyter lab
```

---

## Data Setup

Place the raw DaKS files under:

```text
data/raw/kassel_dataset/
```

Expected contents include:

- multiple `data_input_*.csv` files
- multiple `data_target_*.csv` files
- `meta.csv`

Processed outputs generated by the notebooks are stored under:

```text
data/processed/
```

At the current public repository state:

- `data/processed/baseline_metrics.csv` is the **canonical tracked benchmark artifact**
- canonical pipeline outputs such as
  - `final_feature_engineered_dataset.csv`
  - `train_final.csv`
  - `val_final.csv`
  - `test_final.csv`
  may be produced reproducibly during notebook reruns
- additional prediction, diagnostics, graph-ready, verification, packaging, and graph-experiment artifacts may also be produced locally depending on the notebook stage

For thesis-safe artifact handling, it is important to distinguish between:

- the **public tracked benchmark authority**
- **selected thesis / report-facing figures**
- **local rerun / diagnostics artifacts**
- and **local-only model artifacts**

A more detailed artifact policy and proposed organization for this cleanup pass are documented in `docs/DATA.md`.

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
- `NB03` should run only after the upstream validation outputs of `NB02` are available and should continue only with the validated / `NB04`-eligible cohort.
- Downstream notebooks should preserve the established validation, split, and artifact contracts of the canonical workflow.
- `NB08` is a **strict downstream residual-diagnostics extension** on top of the exported baseline predictions and does not introduce a new predictive model.
- `NB09` is a **strict downstream park-level diagnostics / thesis-consolidation extension** on top of the canonical test-only evaluation space and does not introduce a new predictive model.
- `NB10` is a **strict graph data-interface / split-to-graph contract / artifact-verification stage** and not a graph-training notebook.
- `NB11` is a **strict graph-model input packaging / data object preparation stage** and not a training or benchmarking notebook.
- `NB12` is the **first actual graph-based forecasting baseline** of the repository on top of the packaged graph artifacts of `NB11`.
- `NB13` is a **strict graph ablation / spatial sensitivity follow-up** of `NB12`, with frozen benchmark-safe training configuration.
- `NB14` is a **strict controlled graph refinement follow-up** of `NB13`, as a narrow-scope benchmark-safe graph-only extension.
- `NB12`, `NB13`, and `NB14` should be described as **cautious graph-based forecasting evidence** and not as validated graph superiority evidence.

---

## Current Research Direction

The repository currently follows a **forecasting-first research direction** with a staged extension path from benchmarked forecasting toward diagnostics-aware, graph-aware, and later PHM-oriented research.

Current implemented direction:

- forecasting remains the implemented operational core
- the implemented tabular baselines define the benchmark backbone
- `NB08` extends the benchmark stack with row-level and operating-regime-aware residual diagnostics
- `NB09` extends the diagnostics layer with park-level consolidation and thesis-oriented interpretation
- `NB10` provides graph data-interface / split-to-graph contract / artifact verification
- `NB11` provides graph-model input packaging / data object preparation
- `NB12` provides the first actual graph-based forecasting baseline
- `NB13` provides graph ablation / spatial sensitivity follow-up
- `NB14` provides controlled graph refinement follow-up within a benchmark-safe and narrow-scope comparison setting

Interpretation boundary:

- the digital-twin framing currently remains at the level of research direction and future integration
- the implemented graph stages should be read as cautious graph-based forecasting evidence, not as validated graph superiority
- broader graph redesign, sequence-based models, Mamba / Graph-Mamba, and deployed PHM / digital twin implementation remain future work

---

## Diagnostics and PHM-Oriented Framing

The current repository supports a **forecasting-first benchmark pipeline** enriched with downstream residual diagnostics, park-level diagnostics, graph-contract verification, graph-model input packaging, a first graph-based forecasting baseline, graph ablation / spatial sensitivity follow-up, and controlled graph refinement follow-up.

Within this framing:

- forecasting residuals and park-level diagnostic patterns may be interpreted as **diagnostic signal candidates**
- the current diagnostics layer may support **condition-awareness-oriented inspection**
- and the implemented workflow may serve as a **methodologically sound foundation** for future prognostics / PHM-oriented research extension

However, in the current repository state, this should **not** be interpreted as:

- validated fault diagnosis
- completed anomaly detection
- remaining useful life estimation
- completed PHM functionality
- or deployed digital twin implementation

The correct academic interpretation is that the implemented forecasting, diagnostics, and graph-aware stages provide a cautious and non-overclaiming bridge from benchmarked forecasting toward condition-awareness-oriented interpretation and future PHM-oriented research.

---

## Planned Next vs Future Work

### Planned next

After the current documentation and framing alignment pass, the immediate planned next step is **not** a new graph-packaging stage, a first graph-based forecasting stage, or a new controlled graph-refinement stage, because these have already been implemented in `NB11`, `NB12`, and `NB14`.

The planned next direction is:

- documentation-consistent consolidation of the post-`NB14` public repository story
- repository-safe artifact organization and thesis-facing cleanup
- and only then scope-safe planning for a broader graph-related next step, if justified by the current benchmark evidence and without premature superiority claims

### Future work

The following remain **future work / research extension**:

- broader graph redesign
- stronger graph-based forecasting claims only if supported by new evidence
- sequence-based forecasting models
- Mamba / Graph-Mamba experimentation
- stronger digital-twin integration
- broader prognostics / PHM-oriented modeling
- and deployed PHM / digital twin implementation

---

## Known Notes / Limitations

- The current benchmark core remains **forecasting-first**, with the implemented tabular baselines serving as the established benchmark backbone.
- `NB08` is a downstream residual-diagnostics stage and not a new forecasting model.
- `NB09` is a park-level diagnostics / thesis-consolidation stage and not a new forecasting model.
- `NB10` is a graph data-interface / split-to-graph contract / artifact-verification stage and not a graph-training stage.
- `NB11` is a graph-model input packaging / data object preparation stage and not a graph-training or graph-benchmarking stage.
- `NB12` is an implemented graph-based forecasting baseline, but it does **not** establish validated graph superiority over the canonical benchmark backbone.
- `NB13` is a topology-aware graph ablation / spatial sensitivity follow-up stage; the observed spatial gain remains limited and does not support strong superiority claims.
- `NB13` does not improve the `NB12` reference on the primary benchmark criterion (`test MAE`).
- `NB14` is a strict controlled graph-refinement follow-up within the established post-`NB13` evidence line, but it does **not** constitute a broad graph benchmark suite or a validated graph-superiority result.
- `NB14` also does not improve either the `NB12` reference or the `NB13` best run on `test MAE`, so it should be read as benchmark-safe evidence consolidation rather than stronger graph validation.
- Residual diagnostics, park-level diagnostics, and graph follow-up stages may support diagnostics-aware / health-aware interpretation, but they do **not** constitute a validated anomaly detector, fault-diagnosis module, RUL framework, or completed PHM system.
- `mamba-ssm` may be difficult to build on Windows, so Google Colab or Linux is a more practical environment for future sequence-model experiments.
- Large raw files, rerun-dependent processed outputs, prediction dumps, diagnostics bundles, graph exports, and model binaries should generally remain local-only; the canonical public benchmark artifact is `data/processed/baseline_metrics.csv`.

---

## Logs and Progress Tracking

Repository progress tracking is organized into:

```text
LOGS.md
LOGS_ARCHIVE.md
```

- `LOGS.md` is the **active canonical methodological log** of the current forecasting-first pipeline.
- `LOGS_ARCHIVE.md` stores **historical, exploratory, superseded, or legacy entries** that should not be treated as the active repository authority.

For the current thesis-ready repository state, `LOGS.md` should be treated as the active reference point for methodological progress and pipeline status.

---

## Contributing

[![Contributing](https://img.shields.io/badge/Contributing-Guide-blue.svg)](./CONTRIBUTING.md)

Please read [`CONTRIBUTING.md`](./CONTRIBUTING.md).

Important contribution principles include:

- reproducibility first
- no temporal leakage
- research consistency
- clear separation between implemented / planned next / future work
- and documentation updates when results, workflow contracts, or methodological wording change

---

## License

[![License](https://img.shields.io/badge/License-AGPL--3.0-green.svg)](./LICENSE)

This repository is released under the AGPL-3.0 license.

See [`LICENSE`](./LICENSE) for the full license text.