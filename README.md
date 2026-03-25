# WindPower_DigitalTwin

[![Build Status](https://github.com/Dionysis33/WindPower_DigitalTwin/actions/workflows/python-app.yml/badge.svg)](https://github.com/Dionysis33/WindPower_DigitalTwin/actions/workflows/python-app.yml)
[![License](https://img.shields.io/badge/license-AGPL--v3-green.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)

Research repository for **spatio-temporal wind power forecasting** on the **DaKS / Kassel synthetic wind power dataset**, with a pipeline that combines:

- physics-aware preprocessing,
- graph-ready feature engineering,
- leakage-aware baseline benchmarking,
- residual diagnostics,
- and a roadmap toward **graph-based** and **sequence-based** forecasting models.

> Current focus: build a clean, reproducible forecasting benchmark first, then extend it toward diagnostics-aware and prognostics-aware research directions.

---

## Project Status

The repository currently contains a working forecasting pipeline for:

- loading and validating raw DaKS CSV files,
- merging weather inputs with power targets,
- reconstructing wind magnitude from U/V components,
- scaling wind speed to hub height via **Power Law scaling**,
- engineering temporal and spatial features,
- building graph-ready spatial artifacts,
- creating strict temporal **train / validation / test** splits,
- and benchmarking both simple and advanced tabular baselines.

The current implemented baseline ladder includes:

- **Persistence**
- **Linear Regression**
- **Random Forest**
- **XGBoost**
- **MLP**

At the current stage, forecasting is the implemented core of the repository.  
Graph-based, sequence-based, and PHM-oriented extensions remain future work built on top of this benchmarked forecasting stack.

---

## Main Dataset

### DaKS Dataset (primary source)

This project is centered on the **DaKS / Kassel wind power dataset**.

The active forecasting pipeline uses raw per-park CSV pairs of the form:

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

`Renewables.ninja` appears only in the early exploratory stage of the project.  
It is **not** the main active data source of the current forecasting benchmark pipeline.

---

## Implemented Pipeline

### 1. Raw data loading

The repository includes a `KasselLoader` that:

- scans the raw CSV directory,
- matches `input` and `target` files by park ID,
- loads files with automatic separator fallback,
- merges them on timestamp,
- and returns park-level time series aligned in time.

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

The preprocessing notebooks also include z-score-based outlier handling and train-first preprocessing logic to preserve temporal integrity and avoid leakage.

### 5. Baseline benchmarking

The current tabular benchmark suite includes:

- Persistence
- Linear Regression
- Random Forest
- XGBoost
- MLP

This baseline ladder provides the current reference point for all future graph-based, sequence-based, and deeper forecasting models.

---

## Canonical Baseline Benchmark Artifact

The current cross-model benchmark table is stored in:

```text
data/processed/baseline_metrics.csv
```

This artifact should be interpreted as the **canonical final test-set benchmark table** for the implemented baseline ladder.

For standardized thesis reporting:

- the final comparison is based on the **test split**,
- the primary ranking criterion is **MAE (ascending)**,
- while **RMSE** and **R²** are retained as complementary evaluation metrics.

Validation results are used for model selection where applicable, but they are **not** used as the final cross-model ranking basis.

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
Advanced tabular baselines and diagnostics for:

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

The repository is evolving from a broad digital-twin framing toward a more precise forecasting-centered research question:

**physics-informed, graph-aware wind power forecasting with a pathway to diagnostics-aware and prognostics-aware interpretation.**

This means:

- forecasting is the current implemented core,
- residual and error diagnostics support health-oriented interpretation,
- PHM framing is a research extension rather than a completed module,
- and graph-based / sequence-based models are the next modeling phase after baseline stabilization.

---

## Known Notes / Limitations

- The current benchmark core is **tabular forecasting**, not a finalized graph-learning system.
- The graph-ready pipeline and spatial artifacts are implemented, but the final GNN / Graph-Mamba modeling stage is still future work.
- The current physics utilities are implemented, but their full integration into future learning objectives still requires careful validation.
- `mamba-ssm` may be difficult to build on **Windows**, so **Google Colab or Linux** is a reasonable environment for future sequence-model experiments.
- Large raw and processed files are intentionally excluded from git through `.gitignore`.

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
- benchmark consolidation,
- CI/CD fixes,
- graph alignment,
- and the next planned research steps.

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