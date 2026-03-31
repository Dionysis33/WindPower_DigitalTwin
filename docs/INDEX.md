# Documentation Index

Current canonical workflow:

`NB02 raw validation -> NB03 validated-only EDA -> NB04 feature engineering -> NB05 outlier handling / temporal split -> NB06 baseline modeling -> NB07 advanced tabular baselines -> NB08 downstream residual diagnostics -> NB09 park-level diagnostics / thesis consolidation`

## Core research documents

- `RESEARCH_SCOPE.md`  
  Περιγράφει το forecasting-first scope του project, το implemented benchmark core, το current downstream diagnostics layer και τα future research boundaries.

- `DATA.md`  
  Τεκμηριώνει το **DaKS / Kassel dataset**, τη data-handling λογική και τη διάκριση μεταξύ public tracked artifacts και local rerun outputs.

- `BASELINE_PROTOCOL.md`  
  Ορίζει το baseline evaluation protocol, το canonical benchmark artifact και τον ρόλο των downstream diagnostics / consolidation stages.

- `PHM_ROADMAP.md`  
  Περιγράφει τη σταδιακή και μη υπερβολική μετάβαση από forecasting benchmark pipeline προς diagnostics-aware και αργότερα PHM-oriented research directions.

## Repository governance

- `README.md`  
  Γενική επισκόπηση του current public repository state και του canonical end-to-end workflow μέχρι το `NB09`.

- `CONTRIBUTING.md`  
  Κανόνες για reproducibility, notebook discipline και documentation consistency.

- `LOGS.md`  
  Active canonical methodological log του current public / thesis-ready state.

- `LOGS_ARCHIVE.md`  
  Historical archive παλαιότερων exploratory ή superseded states. Δεν αποτελεί active authority.

## Practical note

Η documentation αυτή υποστηρίζει ένα:

**forecasting-first, benchmark-safe, diagnostics-aware, thesis-facing research workflow**

με σαφή διαχωρισμό ανάμεσα σε:

- **already implemented forecasting and diagnostics stages**
- **current park-level consolidation / interpretation layer**
- **future work**