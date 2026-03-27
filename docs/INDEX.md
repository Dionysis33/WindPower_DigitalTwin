# Documentation Index

Current canonical pipeline:
`NB02 raw validation -> NB03 validated-only EDA -> NB04 feature engineering`

## Core research documents
- `RESEARCH_SCOPE.md`  
  Περιγράφει το ακαδημαϊκό scope του project, με το forecasting ως current implemented core και τις PHM / prognostics κατευθύνσεις ως research extension.

- `DATA.md`  
  Τεκμηριώνει το **DaKS / Kassel dataset**, την προέλευση των δεδομένων, τους περιορισμούς χρήσης και τις βασικές data-handling αποφάσεις.

- `BASELINE_PROTOCOL.md`  
  Ορίζει το baseline evaluation protocol, τα train / validation / test splits, τις leakage-aware πρακτικές και τα benchmark comparison standards.

- `PHM_ROADMAP.md`  
  Περιγράφει τη μελλοντική επέκταση του project από forecasting προς prognostics, degradation monitoring, anomaly awareness και health-oriented diagnostics.

## Repository governance
- `README.md`  
  Γενική επισκόπηση του repository, του implemented pipeline και της current project status.

- `CONTRIBUTING.md`  
  Κανόνες για contribution workflow, notebook discipline, documentation consistency και reproducibility requirements.

- `CODE_OF_CONDUCT.md`  
  Βασικές αρχές συμπεριφοράς και συνεργασίας.

- `SECURITY.md`  
  Responsible disclosure policy και οδηγίες για πιθανές security αναφορές.

## Logs and progress tracking
- `LOGS.md`  
  Active canonical log του current forecasting pipeline, με τα recent methodological updates που αντανακλούν την ενεργή repository state.

- `LOGS_ARCHIVE.md`  
  Historical archive παλαιότερων exploratory, superseded ή legacy entries. Δεν αποτελεί active canonical authority για το current pipeline.

## Practical note
Η documentation αυτή υποστηρίζει ένα **forecasting-first, reproducible research workflow** με έμφαση σε:
- raw data integrity,
- methodological correctness,
- leakage prevention,
- benchmark comparability,
- residual diagnostics,
- και καθαρό διαχωρισμό μεταξύ implemented pipeline και future research extensions.