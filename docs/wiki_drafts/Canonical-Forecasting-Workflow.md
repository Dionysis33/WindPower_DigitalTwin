# Canonical Forecasting Workflow

The canonical workflow is the reviewer-safe backbone of the repository. It runs from raw validation through forecasting baselines, residual diagnostics, park-level diagnostics, and bounded graph-aware extensions.

## Workflow Summary

The documented canonical path is:

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
-> NB11 graph-model input packaging
-> NB12 first graph-based forecasting baseline
-> NB13 graph ablation / spatial sensitivity analysis
-> NB14 controlled graph refinement follow-up
```

`NB01` is preserved as historical exploratory context and is not part of the current canonical DaKS forecasting pipeline.

## Interpretation

The workflow should be presented as forecasting-first. Diagnostics and graph-aware notebooks extend interpretation and methodology, but they do not replace the canonical full-dataset tabular benchmark and do not validate PHM, fault diagnosis, or graph superiority.

## Source Documents

- `README.md`
- `docs/INDEX.md`
- `docs/RESEARCH_SCOPE.md`
- `docs/BASELINE_PROTOCOL.md`
- `CONTRIBUTING.md`
