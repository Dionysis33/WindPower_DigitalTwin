# Dataset Artifacts and Reproducibility

The project uses the DaKS / Kassel synthetic wind power dataset. The raw dataset is not redistributed in this repository; users are responsible for obtaining it from the official source and respecting dataset terms.

Official dataset source: `https://daks.uni-kassel.de/entities/dataset/57ea0681-d8b2-4e76-b31d-578178961f87`

## Data Role

The pipeline transforms locally available raw DaKS files into forecasting-ready processed artifacts. The target variable and feature groups are documented in the repository data guide, along with train/validation/test split expectations and leakage-prevention principles.

## Artifact Policy

The repository separates:

- canonical tracked benchmark artifact: `data/processed/baseline_metrics.csv`
- selected thesis/report-facing figures
- local rerun and diagnostics outputs
- local-only model artifacts

Local diagnostics, tuning outputs, graph outputs, subset outputs, model binaries, checkpoints, and large rerun files should not be treated as public benchmark authority.

## Reproducibility Principles

The documented rules emphasize strict temporal separation, train-only preprocessing statistics, consistent feature spaces, explicit artifact roles, and benchmark-safe reporting.

## Source Documents

- `docs/DATA.md`
- `docs/BASELINE_PROTOCOL.md`
- `docs/PREPROCESSING_AUDIT.md`
- `SECURITY.md`
- `CONTRIBUTING.md`
