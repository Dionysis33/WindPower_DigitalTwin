# WindPower_DigitalTwin

[![Build Status](https://github.com/Dionysis33/WindPower_DigitalTwin/actions/workflows/python-app.yml/badge.svg)](https://github.com/Dionysis33/WindPower_DigitalTwin/actions/workflows/python-app.yml)

[![License](https://img.shields.io/badge/license-AGPL--v3-green.svg)](./LICENSE)

[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)

Research repository for **spatio-temporal wind power forecasting** on the **DaKS dataset**, with a pipeline that combines:
- physics-aware preprocessing,
- graph-ready feature engineering,
- strong tabular baselines,
- and a roadmap toward **GNN / Graph-Mamba** models.

> Current focus: build a clean, reproducible forecasting pipeline first, then extend it toward **prognostics-aware / anomaly-sensitive** digital twin experimentation.

---

## Project Status

The repository currently contains a working research pipeline for:
- loading and validating raw DaKS CSV files,
- merging weather inputs with power targets,
- computing hub-height wind speed via **Power Law scaling**,
- engineering temporal and spatial features,
- building an adjacency matrix for aligned wind parks,
- creating strict temporal train/validation/test splits,
- and benchmarking classical and advanced baseline models.

Implemented results so far include:
- **Persistence** and **Linear Regression** baselines,
- advanced baselines in Notebook 07,
- graph/data alignment for **269 valid and aligned parks**,
- and a best logged advanced-baseline performance around **R² ≈ 0.61**.

The **deep graph stage is not finalized yet**. GNN and Graph-Mamba experiments are the next research phase, not a completed production module.

---

## Main Dataset

### DaKS Dataset (primary source)
This project is centered on the **DaKS / Kassel wind power dataset**.

The current pipeline uses raw per-park CSV pairs of the form:
- `data_input_<park_id>.csv` for weather / NWP variables
- `data_target_<park_id>.csv` for power targets
- `meta.csv` for park metadata and spatial information

During loading:
- input and target files are matched by **park ID**,
- separators are detected automatically,
- wind speed is reconstructed from **U/V components**,
- wind speed is scaled to **100 m hub height**,
- target power is mapped to `Power_Output_Normalized`,
- and the built-in dataset forecast is mapped to `Baseline_Prediction`.

### Renewables.ninja
`Renewables.ninja` appears in the early exploratory phase of the project, but it is **not the main active data source of the current forecasting pipeline**.

---

## Implemented Pipeline

### 1. Raw data loading
The repository includes a `KasselLoader` that:
- scans the raw CSV directory,
- matches `input` and `target` files by park ID,
- loads files with automatic separator fallback,
- merges them on timestamp,
- and returns a park-level time series indexed by time.

### 2. Physics-aware preprocessing
The current preprocessing includes:
- wind magnitude reconstruction from U/V wind components,
- **Power Law scaling** to hub height,
- a theoretical power upper-bound utility based on the **Betz limit**,
- and helper functions for physics-loss experimentation.

### 3. Feature engineering
The feature pipeline includes:
- cyclical time encoding,
- lag features,
- rolling statistics,
- spatial metadata integration,
- and graph construction from park coordinates.

### 4. Dataset splitting and quality control
The active split strategy is a **strict temporal split**:
- **Train:** up to `2019-12-31 23:00:00`
- **Validation:** up to `2020-06-30 23:00:00`
- **Test:** from `2020-07-01` onward

A z-score based outlier handling stage is also included in the preprocessing notebooks.

### 5. Baseline benchmarking
The current baseline ladder includes:
- Persistence
- Linear Regression
- Random Forest / XGBoost / MLP experimentation in the advanced baseline notebook

This stage is used to establish a solid benchmark before moving to graph neural architectures.

---

## Repository Structure

```text
WindPower_DigitalTwin/
├── .github/                          # GitHub Actions workflow
├── data/                             # Local datasets (ignored by git)
│   ├── raw/
│   │   └── kassel_dataset/
│   └── processed/
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
├── LICENSE
├── LOGS.md
├── README.md
└── requirements.txt
```

---

## Notebook Guide

### `01_data_acquisition.ipynb`
Early exploratory notebook for external data acquisition experiments.

### `02_kassel_exploration.ipynb`
Initial decoding and inspection of the DaKS raw files.

### `03_eda_master.ipynb`
Master exploratory data analysis across the merged dataset.

### `04_feature_engineering_and_graph_construction.ipynb`
Core notebook for:
- temporal feature engineering,
- spatial metadata integration,
- graph construction,
- and export of the engineered master dataset.

### `05_outliers_and_split.ipynb`
Outlier handling, temporal split, and export of:
- `train_final.csv`
- `val_final.csv`
- `test_final.csv`

### `06_baseline_modeling.ipynb`
Baseline training and diagnostics for:
- Persistence
- Linear Regression
- residual analysis
- actual-vs-predicted plots

### `07_advanced_baselines_and_importance.ipynb`
Advanced tabular baselines and feature-importance analysis.

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

Recommended execution order:

1. Run `02_kassel_exploration.ipynb`
2. Run `03_eda_master.ipynb`
3. Run `04_feature_engineering_and_graph_construction.ipynb`
4. Run `05_outliers_and_split.ipynb`
5. Run `06_baseline_modeling.ipynb`
6. Run `07_advanced_baselines_and_importance.ipynb`

Use `01_data_acquisition.ipynb` only if you want to revisit earlier exploratory external-data steps.

---

## Current Research Direction

The repository is evolving from a broad digital-twin concept toward a more precise research question:

**physics-informed, graph-aware wind power forecasting with a pathway to prognostics-aware and anomaly-sensitive analysis.**

That means:
- forecasting is the current implemented core,
- anomaly / PHM framing is an active research extension,
- and Graph-Mamba is the planned next modeling stage after baseline stabilization.

---

## Known Notes / Limitations

- The deep graph pipeline is **under active development**.
- The current physics utilities are implemented, but their integration into the final learning objective still needs careful unit-consistent validation.
- `mamba-ssm` may be difficult to build on **Windows**, so **Google Colab or Linux** is a reasonable option for future Graph-Mamba experiments.
- Large raw and processed data files are intentionally ignored by git through `.gitignore`.

---

## Logs and Progress Tracking

Daily technical progress is tracked in:

```text
LOGS.md
```

This includes milestone notes for:
- data strategy changes,
- notebook completion,
- baseline results,
- CI/CD fixes,
- graph alignment,
- and the next planned research steps.

---

## License

This project is released under the **AGPL-3.0** license.

See `LICENSE` for details.