# Documentation Index

Current canonical workflow:

`NB02 raw validation -> NB03 validated-only EDA -> NB04 feature engineering -> NB05 outlier handling / temporal split -> NB06 baseline modeling -> NB07 advanced tabular baselines -> NB08 downstream residual diagnostics`

## Core research documents

- `RESEARCH_SCOPE.md`  
  Περιγράφει το forecasting-first scope του project, τον implemented benchmark core, το current diagnostics extension και τα future research boundaries.

- `DATA.md`  
  Τεκμηριώνει το **DaKS / Kassel dataset**, τη data-handling λογική και τη διάκριση μεταξύ public tracked artifacts και local rerun outputs.

- `BASELINE_PROTOCOL.md`  
  Ορίζει το baseline evaluation protocol, το canonical benchmark artifact και τον ρόλο του downstream diagnostics stage.

- `PHM_ROADMAP.md`  
  Περιγράφει τη σταδιακή και μη υπερβολική μετάβαση από forecasting benchmark pipeline προς diagnostics-aware και αργότερα PHM-oriented research directions.

## Repository governance

- `README.md`  
  Γενική επισκόπηση του current public repository state.

- `CONTRIBUTING.md`  
  Κανόνες για reproducibility, notebook discipline και documentation consistency.

- `LOGS.md`  
  Active canonical methodological log του current public / thesis-ready state.

- `LOGS_ARCHIVE.md`  
  Historical archive παλαιότερων exploratory ή superseded states. Δεν αποτελεί active authority.

## Practical note

Η documentation αυτή υποστηρίζει ένα:

**forecasting-first, benchmark-safe, diagnostics-aware research workflow**

με σαφή διαχωρισμό ανάμεσα σε:

- **already implemented**
- **current diagnostics extension**
- **future work**