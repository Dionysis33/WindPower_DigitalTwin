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

> Current focus: πρώτα ένα καθαρό, reproducible forecasting benchmark και μετά προσεκτική επέκταση προς diagnostics-aware και prognostics-aware research directions.

---

## Project Status

Το repository υποστηρίζει ένα **forecasting-first, thesis-ready research pipeline** πάνω στο **DaKS / Kassel synthetic wind power dataset**.

Στην current canonical μορφή του, το pipeline περιλαμβάνει:

- strict raw validation του DaKS dataset,
- validated-only exploratory data analysis,
- feature engineering με temporal και spatial πληροφορία,
- leakage-aware temporal splitting,
- baseline benchmarking,
- και residual diagnostics.

Η current implemented baseline ladder περιλαμβάνει:

- **Persistence**
- **Linear Regression**
- **Random Forest**
- **XGBoost**
- **MLP**

Στο παρόν στάδιο, το **forecasting** αποτελεί τον implemented core άξονα του repository.  
Τα **graph-based**, **sequence-based** και **PHM-oriented** extensions παραμένουν planned / future work πάνω σε αυτό το benchmarked forecasting stack.

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

Διαβάζει τα upstream validation artifacts του `NB02` και συνεχίζει μόνο με validated parks.  
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

### 5. Baseline modeling and diagnostics (`NB06`)
Το `06_baseline_modeling.ipynb` καλύπτει:

- Persistence
- Linear Regression
- baseline comparison
- residual diagnostics
- actual-vs-predicted analysis

### 6. Advanced tabular baselines (`NB07`)
Το `07_advanced_baselines_and_importance.ipynb` καλύπτει:

- Random Forest
- XGBoost
- MLP
- residual plots
- feature-importance analysis
- benchmark artifact update

### Split protocol note

Η active split strategy είναι strict temporal split:

- **Train:** up to `2019-12-31 23:00:00`
- **Validation:** up to `2020-06-30 23:00:00`
- **Test:** from `2020-07-01` onward

Το current cross-model benchmark artifact είναι το:

```text
data/processed/baseline_metrics.csv
```

---

## Canonical Baseline Benchmark Artifact

Το current cross-model benchmark table αποθηκεύεται στο:

```text
data/processed/baseline_metrics.csv
```

Το artifact αυτό πρέπει να αντιμετωπίζεται ως το **canonical final test-set benchmark table** για την implemented baseline ladder.

Για standardized thesis reporting:

- η τελική σύγκριση βασίζεται στο **test split**,
- το primary ranking criterion είναι το **MAE (ascending)**,
- ενώ τα **RMSE** και **R²** διατηρούνται ως complementary evaluation metrics.

Τα validation results χρησιμοποιούνται για model selection όπου χρειάζεται, αλλά **όχι** ως τελική βάση του cross-model ranking.

---

## Repository Structure

```text
WindPower_DigitalTwin/
├── .github/                          # GitHub Actions workflows
├── data/                             # Local datasets (ignored by git)
│   ├── raw/
│   │   └── kassel_dataset/
│   └── processed/
├── docs/                             # Methodology and research documentation
├── models/                           # Saved model artifacts (ignored by git)
├── notebooks/
│   ├── 01_data_acquisition.ipynb
│   ├── 02_kassel_exploration.ipynb
│   ├── 03_eda_master.ipynb
│   ├── 04_feature_engineering_and_graph_construction.ipynb
│   ├── 05_outliers_and_split.ipynb
│   ├── 06_baseline_modeling.ipynb
│   └── 07_advanced_baselines_and_importance.ipynb
├── reports/                          # Figures and exported reports
├── scripts/                          # Auxiliary scripts
├── src/
│   ├── data/
│   │   └── kassel_loader.py
│   └── features/
│       └── physics.py
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── LOGS.md
├── LOGS_ARCHIVE.md
├── README.md
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
Canonical validated-only EDA stage που λειτουργεί πάνω στο upstream validation contract του `NB02`.

### `04_feature_engineering_and_graph_construction.ipynb`
Feature engineering, spatial metadata integration, graph-ready artifacts και export του engineered dataset.

### `05_outliers_and_split.ipynb`
Leakage-aware outlier handling, temporal split και export των canonical train / validation / test artifacts.

### `06_baseline_modeling.ipynb`
Baseline modeling και diagnostics για:

- Persistence
- Linear Regression
- residual analysis
- actual-vs-predicted plots

### `07_advanced_baselines_and_importance.ipynb`
Advanced tabular baselines και diagnostics για:

- Random Forest
- XGBoost
- MLP
- residual plots
- feature-importance analysis
- benchmark artifact update

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

Important execution notes:

- `NB02` is the canonical raw validation authority.
- `NB03` should be executed only after the upstream validation outputs of `NB02` are available.
- Downstream notebooks should follow the validated contract established upstream.
- `01_data_acquisition.ipynb` belongs to the early exploratory phase and is not part of the active canonical forecasting pipeline.

---

## Current Research Direction

Το repository μετακινείται από ένα πιο broad digital-twin framing προς ένα πιο αυστηρά forecasting-centered research question:

**physics-informed, graph-aware wind power forecasting with a pathway to diagnostics-aware and prognostics-aware interpretation.**

Αυτό σημαίνει ότι:

- το forecasting είναι ο current implemented core,
- τα residual και error diagnostics υποστηρίζουν health-oriented interpretation,
- το PHM framing είναι research extension και όχι completed module,
- και τα graph-based / sequence-based models αποτελούν το επόμενο modeling phase μετά τη baseline stabilization.

---

## Known Notes / Limitations

- Το current benchmark core είναι **tabular forecasting**, όχι finalized graph-learning system.
- Η graph-ready pipeline και τα spatial artifacts είναι implemented, αλλά το τελικό GNN / Graph-Mamba modeling stage παραμένει future work.
- Τα current physics utilities είναι implemented, αλλά η πλήρης ενσωμάτωσή τους σε μελλοντικά learning objectives χρειάζεται προσεκτική validation.
- Το `mamba-ssm` μπορεί να είναι δύσκολο να γίνει build σε **Windows**, οπότε **Google Colab ή Linux** είναι λογικό environment για future sequence-model experiments.
- Μεγάλα raw και processed αρχεία εξαιρούνται σκόπιμα από το git μέσω `.gitignore`.

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