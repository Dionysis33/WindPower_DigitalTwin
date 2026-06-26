# Research Scope and Claim Boundaries

The repository is forecasting-first. Its implemented core is a reproducible wind power forecasting pipeline with downstream diagnostics, graph-aware methodological extensions, and controlled subset experiments.

## Implemented Scope

The documented workflow covers raw validation, validated-only EDA, feature engineering, leakage-aware temporal splitting, tabular forecasting baselines, residual diagnostics, park-level diagnostics, graph contract verification, graph input packaging, first graph-based forecasting experimentation, graph ablation, and controlled graph refinement.

These stages support thesis-facing discussion of forecasting behavior and methodological extensions. They do not establish validated health-state inference or production deployment.

## Boundary Language

Safe wording:

- forecasting-first research repository
- reproducible benchmark and diagnostics pipeline
- residual diagnostics as candidate screening signals
- graph-aware methodological extensions
- controlled four-park neural and sequence subset evidence

Avoid wording:

- validated PHM system
- confirmed fault diagnosis
- Remaining Useful Life estimation
- deployed monitoring platform
- fully implemented digital twin
- validated graph superiority

## Source Documents

- `docs/RESEARCH_SCOPE.md`
- `docs/PHM_ROADMAP.md`
- `docs/BASELINE_PROTOCOL.md`
- `CONTRIBUTING.md`
