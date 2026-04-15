# WindPower_DigitalTwin

[![Build Status](https://github.com/Dionysis33/WindPower_DigitalTwin/actions/workflows/python-app.yml/badge.svg)](https://github.com/Dionysis33/WindPower_DigitalTwin/actions/workflows/python-app.yml)
[![License](https://img.shields.io/badge/license-AGPL--v3-green.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)

Research repository για **spatio-temporal wind power forecasting** πάνω στο **DaKS / Kassel synthetic wind power dataset**, με pipeline που συνδυάζει:

- physics-aware preprocessing,
- leakage-aware baseline benchmarking,
- downstream residual diagnostics,
- park-level diagnostics,
- graph-ready contract verification και graph-model input packaging,
- πρώτο actual graph-based forecasting baseline,
- graph ablation / spatial sensitivity analysis,
- και controlled graph refinement follow-up με benchmark-safe, forecasting-first και non-overclaiming framing.

> Current focus: πρώτα ένα καθαρό, reproducible και benchmark-safe forecasting backbone, μετά diagnostics-aware και condition-awareness-oriented interpretation, στη συνέχεια cautious graph-based forecasting evaluation μέσω baseline, ablation και controlled refinement stages, και αργότερα προσεκτική επέκταση προς broader PHM-oriented και digital-twin-oriented research directions.

---

## Project Status

Το repository υποστηρίζει ένα **forecasting-first, thesis-ready research pipeline** πάνω στο **DaKS / Kassel synthetic wind power dataset**.

### Implemented operational core

Στην current canonical μορφή του, το implemented workflow περιλαμβάνει:

- strict raw validation του DaKS dataset,
- validated-only και coverage-aware downstream EDA,
- feature engineering με temporal, autoregressive και spatial information,
- leakage-aware outlier handling και temporal split,
- baseline benchmarking,
- advanced tabular baseline benchmarking,
- downstream residual diagnostics,
- park-level diagnostics και thesis-consolidation layer,
- graph data-interface / split-to-graph contract / artifact verification,
- graph-model input packaging / data object preparation,
- πρώτο actual graph-based forecasting baseline,
- graph ablation / spatial sensitivity follow-up,
- και controlled graph refinement follow-up πάνω στο post-`NB13` graph evidence.

Η current implemented baseline ladder περιλαμβάνει:

- **Persistence**
- **Linear Regression**
- **Random Forest**
- **XGBoost**
- **MLP**

### Current graph-based extension

Πάνω στο benchmarked forecasting stack, το project έχει πλέον επτά implemented downstream / graph-extension stages:

- `NB08`: row-level residual diagnostics και operating-regime-aware inspection
- `NB09`: park-level diagnostics και thesis-consolidation layer
- `NB10`: strict graph data-interface / split-to-graph contract / artifact-verification layer
- `NB11`: strict graph-model input packaging / data object preparation layer
- `NB12`: first actual graph-based forecasting baseline
- `NB13`: graph ablation / spatial sensitivity analysis as strict follow-up of `NB12`
- `NB14`: controlled graph refinement follow-up as strict post-`NB13` benchmark-safe extension

Αυτά τα stages:

- χρησιμοποιούν canonical exported artifacts και benchmark-safe evaluation logic,
- διατηρούν validation-only model selection και test-only final reporting όπου υπάρχει model fitting,
- επεκτείνουν το repository από graph-readiness σε actual graph-based forecasting experimentation και controlled graph follow-up evaluation,
- αλλά παραμένουν forecasting-first και non-overclaiming,
- και **δεν** τεκμηριώνουν ακόμη validated graph superiority έναντι του current benchmark backbone.

### Current interpretation boundary

Στο παρόν στάδιο, το **forecasting** παραμένει ο implemented core άξονας του repository.

Τα `NB08`–`NB14`:

- **δεν** παρουσιάζουν το repository ως completed PHM system,
- **δεν** συνιστούν validated anomaly detection, fault diagnosis ή RUL module,
- **δεν** τεκμηριώνουν validated GNN / Graph-Mamba superiority,
- **δεν** μετατρέπουν το repository σε completed graph-learning benchmark beyond the current cautious baseline, ablation και controlled refinement evidence,
- και **δεν** συνιστούν completed digital twin implementation.

Το `NB14` πρέπει να διαβάζεται ως:

- controlled graph refinement follow-up,
- narrow-scope post-`NB13` graph-only extension,
- benchmark-safe comparison stage,
- και non-overclaiming evidence consolidation step,

όχι ως νέο broad graph benchmark suite ή graph superiority validation stage.

---

## Main Dataset

### DaKS Dataset (primary source)

Το project βασίζεται στο **DaKS / Kassel synthetic wind power dataset**.

Το current active pipeline χρησιμοποιεί raw per-park CSV pairs της μορφής:

- `data_input_<park_id>.csv` για weather / NWP variables
- `data_target_<park_id>.csv` για power targets
- `meta.csv` για park metadata και spatial information

### Canonical raw validation note

Η **canonical authority** για:

- raw decoding,
- timestamp parsing verification,
- temporal ordering checks,
- duplicate timestamp inspection,
- και input-target alignment

είναι το:

- `02_kassel_exploration.ipynb`

Το notebook αυτό λειτουργεί ως **canonical raw validation gate** του repository.

### Operational helper note

Ο `KasselLoader` χρησιμοποιείται ως **operational helper** για loading / feature-preparation convenience σε downstream στάδια.

Δεν πρέπει να αντιμετωπίζεται ως η **canonical strict raw validation authority** του project.

### Renewables.ninja

Το `Renewables.ninja` ανήκει στην πρώιμη exploratory φάση του project και διατηρείται μόνο ως historical context.

Δεν αποτελεί active primary data source του current canonical forecasting pipeline.

---

## Implemented Pipeline

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

Η active split strategy είναι strict temporal split:

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

## Repository Structure

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
│   └── processed/
│       └── baseline_metrics.csv
├── docs/
├── models/
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
├── reports/
│   └── figures/
├── scripts/
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

### `01_data_acquisition.ipynb`

Early exploratory notebook για external-data experiments.  
Δεν αποτελεί μέρος του current canonical forecasting pipeline.

### `02_kassel_exploration.ipynb`

Canonical raw validation gate του DaKS pipeline.

### `03_eda_master.ipynb`

Canonical validated-only EDA stage που λειτουργεί πάνω στο upstream validation contract του `NB02` και στο canonical validated / `NB04`-eligible cohort.

### `04_feature_engineering_and_graph_construction.ipynb`

Feature engineering, spatial metadata integration, graph-ready artifacts και export του engineered dataset.

### `05_outliers_and_split.ipynb`

Leakage-aware outlier handling, temporal split και export των canonical train / validation / test artifacts.

### `06_baseline_modeling.ipynb`

Baseline modeling και diagnostics για:

- Persistence
- Linear Regression
- test-only benchmark reporting
- forecasting-oriented residual analysis
- actual-vs-predicted plots

### `07_advanced_baselines_and_importance.ipynb`

Advanced tabular baselines και diagnostics για:

- Random Forest
- XGBoost
- MLP
- validation-only model selection
- test-only benchmark update
- residual plots
- feature-importance analysis
- prediction export για downstream diagnostics

### `08_residual_diagnostics_and_operating_regimes.ipynb`

Strict downstream diagnostics notebook που λειτουργεί πάνω στα exported baseline predictions.

Καλύπτει:

- cross-model residual diagnostics
- operating-regime-aware error slicing
- regime-wise benchmark interpretation
- και health-aware / PHM-aware discussion χωρίς overclaiming

Δεν αποτελεί νέο modeling stage.

### `09_park_level_diagnostics_and_thesis_consolidation.ipynb`

Strict downstream park-level diagnostics και thesis-consolidation notebook που λειτουργεί πάνω στο canonical test-only evaluation space.

Καλύπτει:

- per-park diagnostic aggregation
- bias / spread / difficulty inspection across parks
- comparative case-study selection
- thesis-ready consolidation του diagnostics layer
- και cautious health-aware / PHM-aware interpretation χωρίς overclaiming

Δεν αποτελεί νέο modeling stage.

### `10_graph_readiness_and_artifact_verification.ipynb`

Strict graph data-interface / split-to-graph contract / artifact-verification notebook.

Καλύπτει:

- graph-ready data-interface verification
- split-to-graph contract checks
- graph artifact consistency checks
- benchmark-safe readiness for future graph-based forecasting work

Δεν αποτελεί νέο graph-training stage.

### `11_graph_model_input_packaging.ipynb`

Strict graph-model input packaging / data object preparation notebook.

Καλύπτει:

- deterministic loading των canonical split και graph artifacts
- feature-role και node-role manifesting
- coverage-aware graph-model input packaging
- `observed_mask`-aware tensor preparation
- portable serialized graph-ready dataset export
- benchmark-safe handoff προς future graph-based forecasting work

Δεν αποτελεί training notebook.
Δεν αποτελεί benchmarking notebook.
Δεν αλλάζει το `data/processed/baseline_metrics.csv`.
Δεν αποτελεί graph-learning evidence.

### `12_first_graph_based_forecasting_baseline.ipynb`

First actual graph-based forecasting notebook του repository πάνω στα canonical packaged graph artifacts του `NB11`.

Καλύπτει:

- fail-fast integrity checks για τα packaged graph inputs
- snapshot-level graph dataset construction
- benchmark-safe DataLoader materialization
- minimal graph-based forecasting baseline execution
- validation-only model selection
- test-only final reporting
- compact graph-baseline export layer

Το `NB12` αποτελεί implemented graph-based forecasting evidence, αλλά δεν τεκμηριώνει graph superiority έναντι του current tabular benchmark backbone.

### `13_graph_ablation_and_spatial_sensitivity_analysis.ipynb`

Strict follow-up notebook του `NB12` για graph ablation / spatial sensitivity analysis.

Καλύπτει:

- canonical artifact loading και fail-fast integrity checks
- explicit experiment registry με frozen `NB12`-compatible training configuration
- deterministic topology variants
- topology-aware dataset / DataLoader materialization
- controlled GCN execution με validation-only model selection και test-only final reporting
- compact export layer για validation summary, test metrics, training history και reference comparison

Το `NB13` δείχνει sensitivity στην topology choice και μικρό spatial gain, αλλά δεν στηρίζει strong graph superiority claims και δεν βελτιώνει το `NB12` reference στο primary benchmark criterion (`test MAE`).

### `14_controlled_graph_refinement_followup.ipynb`

Strict post-`NB13` controlled graph refinement notebook που λειτουργεί ως narrow-scope benchmark-safe follow-up μέσα στην established `local_pruned_graph` family.

Καλύπτει:

- canonical artifact loading και read-only reference policy
- strict comparison boundary μόνο απέναντι σε `NB12` reference και `NB13` best configuration
- predeclared experiment registry γύρω από controlled pruning-strength refinement
- deterministic refined edge-bundle construction
- validation-only model selection
- test-only final reporting για το validation-selected experiment
- strict reference comparison απέναντι σε `NB12` και `NB13`
- και final sanity test για benchmark-contract integrity

Το `NB14` αποτελεί controlled graph refinement evidence-consolidation stage, αλλά δεν συνιστά broad graph benchmark suite, δεν τεκμηριώνει graph superiority claim, και δεν μετατρέπει το repository σε sequence-model, PHM ή completed digital twin implementation stage.

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

Typical exported artifacts include:

- `final_feature_engineered_dataset.csv`
- `adjacency_matrix.npy`
- `train_final.csv`
- `val_final.csv`
- `test_final.csv`
- `baseline_metrics.csv`

Additional graph-ready and diagnostics artifacts may also be produced locally during reruns, depending on the notebook stage.

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

- `NB02` is the canonical raw validation authority.
- `NB03` should be executed only after the upstream validation outputs of `NB02` are available.
- Downstream notebooks should follow the validated / `NB04`-eligible contract established upstream.
- `NB08` είναι **strict downstream residual diagnostics extension** πάνω στα exported baseline predictions.
- `NB09` είναι **strict downstream park-level diagnostics / thesis-consolidation extension** πάνω στο canonical test-only evaluation space.
- `NB10` είναι **strict graph data-interface / split-to-graph contract / artifact-verification extension** και όχι νέο graph-training notebook.
- `NB11` είναι **strict graph-model input packaging / data object preparation extension** και όχι training / benchmarking notebook.
- Neither `NB08`, `NB09`, `NB10`, nor `NB11` introduces a new predictive model.
- `NB12` είναι το **first actual graph-based forecasting baseline** πάνω στα packaged graph artifacts του `NB11`.
- `NB13` είναι **strict graph ablation / spatial sensitivity follow-up** του `NB12`, με frozen benchmark-safe training configuration.
- Neither `NB12` nor `NB13` should be described as validated graph superiority evidence; they provide cautious graph-based forecasting evidence and topology-sensitivity analysis only.
- `NB14` είναι **strict controlled graph refinement follow-up** του `NB13`, ως narrow-scope benchmark-safe graph-only extension.
- Neither `NB12`, `NB13`, nor `NB14` should be described as validated graph superiority evidence; they provide cautious graph-based forecasting evidence, topology-sensitivity analysis, and controlled refinement follow-up only.

---

## Current Research Direction

Το repository ακολουθεί πλέον την εξής καθαρή ερευνητική γραμμή:

**forecasting-first benchmark pipeline -> downstream residual diagnostics -> park-level diagnostics consolidation -> graph contract verification -> graph-model input packaging -> first graph-based forecasting baseline -> graph ablation / spatial sensitivity follow-up -> controlled graph refinement follow-up -> cautious pathway toward condition-awareness-oriented interpretation and future PHM-oriented research extension**

Αυτό σημαίνει ότι:

- το forecasting είναι ο current implemented core
- τα implemented tabular baselines αποτελούν το benchmark backbone
- το `NB08` λειτουργεί ως row-level / regime-aware diagnostics layer
- το `NB09` λειτουργεί ως park-level diagnostics και thesis-consolidation layer
- το `NB10` λειτουργεί ως graph-readiness / contract-verification layer
- το `NB11` λειτουργεί ως graph-model input packaging / data-object-preparation layer
- το `NB12` λειτουργεί ως πρώτο actual graph-based forecasting baseline
- το `NB13` λειτουργεί ως graph ablation / spatial sensitivity layer για strict post-`NB12` follow-up evaluation
- το `NB14` λειτουργεί ως controlled graph refinement layer για strict post-`NB13` benchmark-safe follow-up evaluation
- το digital twin framing διατηρείται σε research / future-integration επίπεδο
- και broader graph redesign, sequence-based models, Mamba / Graph-Mamba, καθώς και deployed PHM / digital twin implementation παραμένουν future work

---

## Diagnostics and PHM-Oriented Framing

Τα forecasting residuals και τα park-level diagnostic patterns μπορούν να λειτουργήσουν ως diagnostic signal candidates για:

- residual analysis
- condition-awareness-oriented inspection
- diagnostic insights
- και μελλοντική PHM / prognostics discussion

Ωστόσο, στο current repository state αυτό **δεν** ισοδυναμεί με:

- validated fault diagnosis
- completed anomaly detector
- remaining useful life estimation
- completed PHM system
- ή deployed digital twin service

Η σωστή ακαδημαϊκή θέση του repository είναι ότι ένα αυστηρά benchmarked forecasting pipeline, εμπλουτισμένο με downstream residual και park-level diagnostics, graph-contract verification, graph-model input packaging, πρώτο graph-based forecasting baseline, graph ablation / spatial sensitivity analysis και controlled graph refinement follow-up, μπορεί να στηρίξει condition-awareness-oriented interpretation και να αποτελέσει μεθοδολογικά ορθό υπόβαθρο για μελλοντικές prognostics / PHM-oriented επεκτάσεις χωρίς overclaiming.

---

## Planned Next vs Future Work

### Planned next

Το άμεσο επόμενο βήμα μετά το current documentation / framing alignment δεν είναι ούτε νέο packaging stage, ούτε το πρώτο graph-based forecasting stage, ούτε νέο controlled graph refinement stage, επειδή αυτά έχουν ήδη υλοποιηθεί στα `NB11`, `NB12` και `NB14`.

Το planned next είναι:

- documentation-consistent consolidation του post-`NB14` public repository story
- και στη συνέχεια scope-safe planning μόνο για broader graph refinement ή επόμενο graph-related step, εφόσον αυτό δικαιολογείται από το current benchmark evidence και χωρίς premature superiority claims

### Future work

Τα παρακάτω παραμένουν future work / research extension:

- broader graph redesign
- stronger graph-based forecasting claims only if supported by new evidence
- sequence-based forecasting models
- Mamba / Graph-Mamba experimentation
- stronger digital-twin integration
- deployed PHM / digital twin implementation
- broader prognostics / PHM-oriented modeling

---

## Known Notes / Limitations

- Το current benchmark core παραμένει **forecasting-first**, με tabular baselines ως established benchmark backbone.
- Το `NB08` είναι diagnostics stage και όχι νέο forecasting model.
- Το `NB09` είναι park-level diagnostics / thesis-consolidation stage και όχι νέο forecasting model.
- Το `NB10` είναι graph contract verification stage και όχι graph model training stage.
- Το `NB11` είναι graph-model input packaging / data object preparation stage και όχι graph training ή graph benchmarking stage.
- Το `NB12` είναι implemented graph-based forecasting baseline, αλλά δεν τεκμηριώνει graph superiority έναντι του canonical benchmark backbone.
- Το `NB13` είναι topology-aware graph ablation / spatial sensitivity stage, αλλά το observed spatial gain είναι μικρό και δεν αρκεί για strong superiority claims.
- Το `NB13` δεν βελτιώνει το `NB12` reference στο primary benchmark criterion (`test MAE`).
- Το `NB14` είναι strict controlled graph refinement follow-up μέσα στην established post-`NB13` graph evidence line, αλλά δεν συνιστά broad graph benchmark suite και δεν τεκμηριώνει graph superiority claim.
- Το `NB14` επίσης δεν βελτιώνει ούτε το `NB12` reference ούτε το `NB13` best run στο `test MAE`, άρα πρέπει να διαβάζεται ως benchmark-safe evidence consolidation και όχι ως stronger graph validation stage.
- Τα residual diagnostics, τα park-level diagnostics και τα graph follow-up stages υποστηρίζουν diagnostics-aware / health-aware interpretation, αλλά δεν συνιστούν validated anomaly detector, fault diagnosis module ή RUL framework.
- Το `mamba-ssm` μπορεί να είναι δύσκολο να γίνει build σε Windows, οπότε Google Colab ή Linux είναι λογικό environment για future sequence-model experiments.
- Μεγάλα raw και processed αρχεία εξαιρούνται σκόπιμα από το git. Το canonical public benchmark artifact είναι το `data/processed/baseline_metrics.csv`.

---

## Logs and Progress Tracking

Η repository progress tracking διαχωρίζεται πλέον σε:

```text
LOGS.md
LOGS_ARCHIVE.md
```

- `LOGS.md` κρατά το active canonical methodological log του current forecasting pipeline.
- `LOGS_ARCHIVE.md` κρατά historical exploratory, superseded ή legacy entries.

Για current thesis-ready repository state, ως active authority πρέπει να αντιμετωπίζεται το `LOGS.md`.

---

## Contributing

Please read:

```text
CONTRIBUTING.md
```

Important contribution principles include:

- reproducibility first
- no temporal leakage
- research consistency
- clear separation between implemented / planned next / future work
- and documentation updates when results, workflow contracts, or methodological wording change

---

## License

This project is released under the AGPL-3.0 license.

See `LICENSE` for details.