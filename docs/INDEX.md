# Documentation Index

Current canonical workflow:

`NB02 raw validation -> NB03 validated-only EDA -> NB04 feature engineering -> NB05 outlier handling / temporal split -> NB06 baseline modeling -> NB07 advanced tabular baselines -> NB08 downstream residual diagnostics -> NB09 park-level diagnostics / thesis consolidation -> NB10 graph data-interface / split-to-graph contract / artifact verification -> NB11 graph-model input packaging / data object preparation -> NB12 first graph-based forecasting baseline -> NB13 graph ablation / spatial sensitivity analysis`

## Core research documents

- `RESEARCH_SCOPE.md`  
  Περιγράφει το forecasting-first scope του project, το implemented benchmark core, το downstream diagnostics / graph-extension path, και τα future research boundaries με σαφή διάκριση μεταξύ implemented, planned-next και future work.

- `DATA.md`  
  Τεκμηριώνει το **DaKS / Kassel dataset**, τη data-handling λογική και τη διάκριση μεταξύ public tracked artifacts και local rerun outputs.

- `BASELINE_PROTOCOL.md`  
  Ορίζει το baseline evaluation protocol, το canonical benchmark artifact, και τον ρόλο των downstream diagnostics, graph-contract verification, graph-model input packaging και cautious graph-based forecasting comparison stages.

- `PHM_ROADMAP.md`  
  Περιγράφει τη σταδιακή και μη υπερβολική μετάβαση από forecasting benchmark pipeline προς diagnostics-aware, graph-aware και αργότερα PHM-oriented research directions.

## Repository governance

- `README.md`  
  Γενική επισκόπηση του current public repository state και του canonical end-to-end workflow μέχρι το `NB13`, με forecasting-first και benchmark-safe wording.

- `CONTRIBUTING.md`  
  Κανόνες για reproducibility, notebook discipline, benchmark-safe contributions και documentation consistency.

- `LOGS.md`  
  Active canonical methodological log του current public / thesis-ready state.

- `LOGS_ARCHIVE.md`  
  Historical archive παλαιότερων exploratory ή superseded states. Δεν αποτελεί active authority.

## Practical note

Η documentation αυτή υποστηρίζει ένα:

**forecasting-first, benchmark-safe, diagnostics-aware, graph-aware, thesis-facing research workflow**

με σαφή διαχωρισμό ανάμεσα σε:

- **already implemented forecasting, diagnostics, graph-verification, graph-packaging, and cautious graph-forecasting stages**
- **current interpretation boundary without strong graph superiority claims**
- **future work / broader research extension**