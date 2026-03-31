# WindPower_DigitalTwin

[![Build Status](https://github.com/Dionysis33/WindPower_DigitalTwin/actions/workflows/python-app.yml/badge.svg)](https://github.com/Dionysis33/WindPower_DigitalTwin/actions/workflows/python-app.yml)
[![License](https://img.shields.io/badge/license-AGPL--v3-green.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)

Research repository για **spatio-temporal wind power forecasting** πάνω στο **DaKS / Kassel synthetic wind power dataset**, με pipeline που συνδυάζει:

- physics-aware preprocessing,
- graph-ready feature engineering,
- leakage-aware baseline benchmarking,
- residual diagnostics,
- και roadmap προς **graph-based** και **sequence-based** forecasting models.

> Current focus: πρώτα ένα καθαρό, reproducible forecasting benchmark και μετά προσεκτική επέκταση προς diagnostics-aware και health-aware / PHM-oriented research directions.

---

## Project Status

Το repository υποστηρίζει ένα **forecasting-first, thesis-ready research pipeline** πάνω στο **DaKS / Kassel synthetic wind power dataset**.

### Implemented operational core

Στην current canonical μορφή του, το implemented workflow περιλαμβάνει:

- strict raw validation του DaKS dataset
- validated-only και coverage-aware downstream EDA
- feature engineering με temporal, autoregressive και spatial information
- leakage-aware outlier handling και temporal split
- baseline benchmarking
- advanced tabular baseline benchmarking
- downstream residual diagnostics
- park-level diagnostics και thesis-consolidation layer

Η current implemented baseline ladder περιλαμβάνει:

- **Persistence**
- **Linear Regression**
- **Random Forest**
- **XGBoost**
- **MLP**

### Current diagnostics and thesis-consolidation extension

Πάνω στο benchmarked forecasting stack, το project έχει πλέον δύο implemented downstream diagnostic layers:

- `NB08`: row-level residual diagnostics και operating-regime-aware inspection
- `NB09`: park-level diagnostics και thesis-consolidation layer

Αυτά τα stages:

- χρησιμοποιούν canonical exported predictions και κοινό test-only evaluation space,
- παραμένουν forecasting-downstream,
- ενισχύουν diagnostics-aware / health-aware interpretation,
- αλλά **δεν** αποτελούν νέο modeling stage.

### Scope boundary

Στο παρόν στάδιο, το **forecasting** παραμένει ο implemented core άξονας του repository.

Τα `NB08` και `NB09`:

- **δεν** εισάγουν νέο forecasting model,
- **δεν** παρουσιάζουν το repository ως completed PHM system,
- **δεν** συνιστούν validated anomaly detection, fault diagnosis ή RUL module.

Τα **graph-based**, **sequence-based** και broader **PHM-oriented** extensions παραμένουν planned / future work πάνω σε αυτό το benchmarked forecasting stack.

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
- και health-aware interpretation χωρίς PHM overclaiming.

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

---

## Repository Structure

```text
WindPower_DigitalTwin/
├── .github/
├── data/
│   └── processed/
│       └── baseline_metrics.csv
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
│   └── 09_park_level_diagnostics_and_thesis_consolidation.ipynb
├── src/
├── .gitattributes
├── .gitignore
├── CITATION.cff
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── LOGS.md
├── LOGS_ARCHIVE.md
├── README.md
├── SECURITY.md
└── requirements.txt
```

---

## Notebook Guide

### `01_data_acquisition.ipynb`

Early exploratory notebook για external-data experiments.  
Δεν αποτελεί μέρος του current canonical forecasting pipeline.

### `02_kassel_exploration.ipynb`

Canonical raw validation gate του DaKS pipeline.

### `03_eda_master.ipynb`

Canonical validated-only EDA stage που λειτουργεί πάνω στο upstream validation contract του `NB02` και στο canonical validated / NB04-eligible cohort.

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

- cross-model residual diagnostics,
- operating-regime-aware error slicing,
- regime-wise benchmark interpretation,
- και health-aware / PHM-aware discussion χωρίς overclaiming.

Δεν αποτελεί νέο modeling stage.

### `09_park_level_diagnostics_and_thesis_consolidation.ipynb`

Strict downstream park-level diagnostics και thesis-consolidation notebook που λειτουργεί πάνω στο canonical test-only evaluation space.

Καλύπτει:

- per-park diagnostic aggregation,
- bias / spread / difficulty inspection across parks,
- comparative case-study selection,
- thesis-ready consolidation του diagnostics layer,
- και cautious health-aware / PHM-aware interpretation χωρίς overclaiming.

Δεν αποτελεί νέο modeling stage.

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

Important execution notes:

- `NB02` is the canonical raw validation authority.
- `NB03` should be executed only after the upstream validation outputs of `NB02` are available.
- Downstream notebooks should follow the validated / NB04-eligible contract established upstream.
- `NB08` είναι **strict downstream residual diagnostics extension** πάνω στα exported baseline predictions.
- `NB09` είναι **strict downstream park-level diagnostics / thesis-consolidation extension** πάνω στο canonical test-only evaluation space.
- Neither `NB08` nor `NB09` introduces a new predictive model.
- `01_data_acquisition.ipynb` belongs to the early exploratory phase and is not part of the active canonical forecasting pipeline.

---

## Current Research Direction

Το repository ακολουθεί πλέον την εξής καθαρή ερευνητική γραμμή:

**forecasting-first benchmark pipeline -> downstream residual diagnostics -> park-level diagnostics consolidation -> cautious pathway toward health-aware / PHM-oriented interpretation**

Αυτό σημαίνει ότι:

- το forecasting είναι ο current implemented core,
- τα implemented baselines αποτελούν το benchmark backbone,
- το `NB08` λειτουργεί ως row-level / regime-aware diagnostics layer,
- το `NB09` λειτουργεί ως park-level diagnostics και thesis-consolidation layer,
- το digital twin framing διατηρείται σε research level,
- και τα graph-based / sequence-based models παραμένουν future modeling work.

---

## Known Notes / Limitations

- Το current benchmark core είναι **tabular forecasting**, όχι finalized graph-learning system.
- Το `NB08` είναι **diagnostics stage** και όχι νέο forecasting model.
- Το `NB09` είναι **park-level diagnostics / thesis-consolidation stage** και όχι νέο forecasting model.
- Τα residual diagnostics και τα park-level diagnostics υποστηρίζουν **diagnostics-aware / health-aware interpretation**, αλλά **δεν** συνιστούν validated anomaly detector, fault diagnosis module ή RUL framework.
- Η graph-ready pipeline και τα spatial artifacts είναι implemented, αλλά το τελικό GNN / Graph-Mamba / sequence-modeling stage παραμένει future work.
- Το `mamba-ssm` μπορεί να είναι δύσκολο να γίνει build σε **Windows**, οπότε **Google Colab ή Linux** είναι λογικό environment για future sequence-model experiments.
- Μεγάλα raw και processed αρχεία εξαιρούνται σκόπιμα από το git. Το canonical public benchmark artifact είναι το `data/processed/baseline_metrics.csv`.

---

## Logs and Progress Tracking

Η repository progress tracking διαχωρίζεται πλέον σε:

```text
LOGS.md
LOGS_ARCHIVE.md
```

- `LOGS.md` κρατά το **active canonical methodological log** του current forecasting pipeline.
- `LOGS_ARCHIVE.md` κρατά historical exploratory, superseded ή legacy entries.

Για current thesis-ready repository state, ως active authority πρέπει να αντιμετωπίζεται το `LOGS.md`.

---

## Contributing

Please read:

```text
CONTRIBUTING.md
```

Important contribution principles include:

- reproducibility first,
- no temporal leakage,
- research consistency,
- and documentation updates when results or methodology change.

---

## License

This project is released under the **AGPL-3.0** license.

See `LICENSE` for details.