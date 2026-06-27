# Home

This Wiki is a concise navigation layer for reviewers of `WindPower_DigitalTwin`.
It summarizes the repository as a forecasting-first research project and points back to the maintained repository documents.

The project studies spatio-temporal wind power forecasting on the DaKS / Kassel synthetic wind power dataset. The implemented repository should be read as a reproducible forecasting and diagnostics research pipeline, not as a deployed monitoring system, validated PHM system, fault-diagnosis module, Remaining Useful Life estimator, or fully implemented digital twin.

## Suggested Reading Path

1. Start with the research scope and claim boundaries.
2. Review the dataset, artifact, and reproducibility policy.
3. Read the canonical forecasting workflow and benchmark pages.
4. Treat residual diagnostics, graph-aware stages, and neural/sequence subset audits as bounded extensions.
5. Keep `NB15` through `NB21` separate from the canonical `NB02` through `NB14` workflow unless a reviewed document explicitly promotes a new workflow.
6. Use repository hygiene pages to understand contribution and artifact-safety expectations.

## Wiki Pages

- Research Scope and Claim Boundaries
- Dataset Artifacts and Reproducibility
- Leakage Safe Evaluation Protocol
- Canonical Forecasting Workflow
- Canonical Benchmark and Tabular Results
- Residual Diagnostics and PHM-Oriented Interpretation
- Graph-Aware Methodological Extensions
- Controlled Neural and Sequence Subset Evidence
- Local Demo and Artifact Browser
- Repository Evidence Hygiene
- Reviewer FAQ

## Notebook Categories

- `NB01`: historical exploratory context only.
- `NB02` through `NB14`: canonical full-dataset forecasting / graph workflow.
- `NB15`, `NB16`, `NB18`, `NB19`: controlled four-park neural / sequence subset evidence.
- `NB17`: unaudited Mamba sequence scaffold only.
- `NB20`, `NB21`: validation-calibrated residual diagnostic interpretation layers.

## Source Documents

- `README.md`
- `docs/INDEX.md`
- `docs/RESEARCH_SCOPE.md`
- `docs/BASELINE_PROTOCOL.md`
- `docs/DATA.md`
- `docs/PHM_ROADMAP.md`
