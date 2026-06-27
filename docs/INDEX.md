# Documentation Index

Current canonical workflow:

`NB02 raw validation -> NB03 validated-only EDA -> NB04 feature engineering -> NB05 outlier handling / temporal split -> NB06 baseline modeling -> NB07 advanced tabular baselines -> NB08 downstream residual diagnostics -> NB09 park-level diagnostics / thesis consolidation -> NB10 graph data-interface / split-to-graph contract / artifact verification -> NB11 graph-model input packaging / data object preparation -> NB12 first graph-based forecasting baseline -> NB13 graph ablation / spatial sensitivity analysis -> NB14 controlled graph refinement follow-up`

Later notebooks are supplementary extensions unless explicitly promoted by a future reviewed document. `NB15`, `NB16`, `NB18`, and `NB19` are controlled neural / sequence subset evidence; `NB20` and `NB21` are validation-calibrated residual diagnostic interpretation layers; `NB17` is an unaudited Mamba sequence scaffold.

## Core research documents

- `RESEARCH_SCOPE.md`  
  Περιγράφει το forecasting-first scope του project, το implemented benchmark core, το downstream diagnostics / graph-extension path, και τα future research boundaries με σαφή διάκριση μεταξύ implemented, planned-next και future work.

- `DATA.md`  
  Τεκμηριώνει το **DaKS / Kassel dataset**, τη data-handling λογική και τη διάκριση μεταξύ public tracked artifacts και local rerun outputs.

- `BASELINE_PROTOCOL.md`  
  Ορίζει το baseline evaluation protocol, το canonical benchmark artifact, και τον ρόλο των downstream diagnostics, graph-contract verification, graph-model input packaging, cautious graph-based forecasting comparison και controlled graph refinement follow-up stages.

- `PHM_ROADMAP.md`  
  Περιγράφει τη σταδιακή και μη υπερβολική μετάβαση από forecasting benchmark pipeline προς diagnostics-aware, graph-aware και αργότερα PHM-oriented research directions.

## Supplementary extension evidence

- `NEURAL_BASELINE_COMPARISON_SUMMARY.md`
  Consolidates controlled neural / sequence subset evidence and keeps it separate from the canonical full-dataset benchmark.

- `MATCHED_FOUR_PARK_BASELINE_COMPARISON_AUDIT.md`
  Documents matched four-park row-level baseline context for the neural subset evidence space.

- `NN_SUBSET_EXPERIMENT_AUDIT.md`
  Documents controlled four-park tabular neural subset evidence.

- `NN_SEQUENCE_SUBSET_AUDIT.md`
  Documents `NB15` controlled GRU sequence subset evidence.

- `NN_LSTM_SEQUENCE_SUBSET_AUDIT.md`
  Documents `NB16` controlled LSTM sequence subset evidence.

- `TCN_SEQUENCE_SUBSET_AUDIT.md`
  Documents `NB18` controlled TCN sequence subset evidence.

- `PATCHTST_SEQUENCE_SUBSET_AUDIT.md`
  Documents `NB19` sequence-aligned PatchTST-Lite and flattened-window XGBoost subset evidence.

- `RESIDUAL_PHM_DIAGNOSTICS_AUDIT.md`
  Documents `NB20` validation-calibrated residual diagnostic interpretation evidence.

- `STRONG_MODEL_RESIDUAL_PHM_AUDIT.md`
  Documents `NB21` strong-model residual diagnostic interpretation evidence.

No completed `NB17` / Mamba audit document is present in this index. Treat `NB17` as an unaudited scaffold only.

## Repository governance

- `README.md`  
  Public overview of the current repository state, the canonical end-to-end workflow through `NB14`, and the bounded supplementary post-`NB14` notebook extensions.

- `CONTRIBUTING.md`  
  Κανόνες για reproducibility, notebook discipline, benchmark-safe contributions και documentation consistency.

- `LOGS.md`  
  Active canonical methodological log του current public / thesis-ready state.

- `LOGS_ARCHIVE.md`  
  Historical archive παλαιότερων exploratory ή superseded states. Δεν αποτελεί active authority.

## Published Wiki and Repository Mirror

- `wiki_mirror/Home.md`
  Reviewer navigation over canonical workflow, benchmark evidence, and bounded supplementary extensions.

- `wiki_mirror/Canonical-Forecasting-Workflow.md`
  Mirror page for the canonical `NB02` through `NB14` workflow and its supplementary-extension boundary.

- `wiki_mirror/Controlled-Neural-and-Sequence-Subset-Evidence.md`
  Mirror page for controlled four-park neural / sequence subset evidence.

- `wiki_mirror/Residual-Diagnostics-and-PHM-Oriented-Interpretation.md`
  Mirror page for residual diagnostic interpretation layers and PHM-oriented claim limits.

## Practical note

Η documentation αυτή υποστηρίζει ένα:

**forecasting-first, benchmark-safe, diagnostics-aware, graph-aware, thesis-facing research workflow**

με σαφή διαχωρισμό ανάμεσα σε:

- **already implemented forecasting, diagnostics, graph-verification, graph-packaging, graph-baseline, graph-ablation, controlled graph-refinement stages, and bounded supplementary extension evidence**
- **current interpretation boundary without strong graph superiority claims**
- **future work / broader research extension**
