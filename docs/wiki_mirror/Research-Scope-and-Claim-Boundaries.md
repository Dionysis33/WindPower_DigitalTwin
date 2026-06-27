# Research Scope and Claim Boundaries

The repository is forecasting-first. Its implemented core is a reproducible wind power forecasting pipeline with downstream diagnostics, graph-aware methodological extensions, and controlled subset experiments.

## Implemented Scope

The documented canonical workflow covers raw validation, validated-only EDA, feature engineering, leakage-aware temporal splitting, tabular forecasting baselines, residual diagnostics, park-level diagnostics, graph contract verification, graph input packaging, first graph-based forecasting experimentation, graph ablation, and controlled graph refinement.

Supplementary notebooks after `NB14` are bounded extensions: `NB15`, `NB16`, `NB18`, and `NB19` provide controlled four-park neural / sequence subset evidence; `NB20` and `NB21` provide validation-calibrated residual diagnostic interpretation layers; `NB17` is an unaudited Mamba sequence scaffold only.

These stages support thesis-facing discussion of forecasting behavior and methodological extensions. They do not establish validated health-state inference or production deployment.

## Boundary Language

Safe wording:

- forecasting-first research repository
- reproducible benchmark and diagnostics pipeline
- residual diagnostics as candidate screening signals
- graph-aware methodological extensions
- controlled four-park neural and sequence subset evidence
- validation-calibrated residual diagnostic interpretation layers
- unaudited scaffold wording for `NB17`

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
