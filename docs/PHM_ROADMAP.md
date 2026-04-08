# PHM Roadmap

## Γιατί χρειάζεται αυτό το roadmap

Το project ξεκίνησε και παραμένει **forecasting-first**.  
Η σύνδεση προς **turbine prognostics and health management (PHM)** είναι πραγματική ως ερευνητική κατεύθυνση, αλλά πρέπει να διατυπώνεται χωρίς overclaiming.

## Current implemented backbone

Σήμερα το repository έχει ήδη ολοκληρώσει:

- clean preprocessing,
- validated-only downstream data assembly,
- feature engineering,
- leakage-aware split strategy,
- baseline benchmarking,
- advanced tabular baselines.

## Current diagnostics, graph-verification, and packaging extension

Το current downstream extension layer δεν είναι νέο deployed modeling stage, αλλά μια **strict forecasting-downstream and forecasting-supportive extension** πάνω στα canonical exported artifacts.

Σήμερα αυτό περιλαμβάνει τέσσερα implemented notebooks:

- `NB08` για residual diagnostics και operating-regime-aware inspection
- `NB09` για park-level diagnostics και thesis-consolidation layer
- `NB10` για strict graph data-interface / split-to-graph contract / artifact verification
- `NB11` για strict graph-model input packaging / data object preparation

Αυτό περιλαμβάνει:

- residual behavior inspection,
- operating-regime-aware slicing,
- comparison των implemented baselines σε diagnostic space,
- park-level diagnostic aggregation,
- representative case-study consolidation,
- cautious health-aware interpretation,
- graph-ready contract verification,
- και graph-model input packaging πριν από future graph-based forecasting experiments.

## Γιατί αυτό συνδέεται με PHM

Στα wind energy systems, τα forecasting residuals και τα park-level patterns μπορεί να σχετίζονται με:

- departures from expected operating behavior,
- shifts across operating regimes,
- performance drift,
- condition-awareness questions,
- και wider diagnostic hypotheses.

Παράλληλα, ένα strict graph data-interface / artifact-verification stage μαζί με ένα strict graph-model input packaging stage είναι χρήσιμα γιατί επιτρέπουν future graph-based forecasting work πάνω σε benchmark-safe, contract-safe και μεθοδολογικά καθαρό υπόβαθρο.

Αυτό όμως **δεν** σημαίνει ότι το repository έχει ήδη validated fault diagnosis ή prognostics engine.

## Stage-wise research path

### Stage 1 — Forecasting foundation (implemented)
- raw validation
- validated-only EDA
- feature engineering
- temporal split
- reproducible preprocessing

### Stage 2 — Baseline ladder (implemented)
- Persistence
- Linear Regression
- Random Forest
- XGBoost
- MLP

### Stage 3 — Downstream diagnostics extension (implemented)
- row-level residual diagnostics
- operating-regime analysis
- error structure inspection
- park-level diagnostic aggregation
- thesis-oriented case-study consolidation
- diagnostics-aware / health-aware interpretation

### Stage 4 — Graph-readiness verification (implemented)
- graph data-interface checks
- split-to-graph contract verification
- artifact-consistency verification
- benchmark-safe graph-ready handoff

### Stage 5 — Graph-model input packaging (implemented)
- deterministic loading of canonical split / graph artifacts
- feature-role and node-role manifesting
- coverage-aware graph-model input packaging
- observed-mask-aware tensor preparation
- portable serialized graph-ready dataset export
- benchmark-safe handoff to future graph-based forecasting experiments

### Stage 6 — Advanced forecasting models (future work)
- graph-based models
- spatio-temporal learning
- sequence models
- GNN / Mamba / Graph-Mamba experimentation

## Τι δεν πρέπει να ισχυρίζεται ακόμη το repository

Το project δεν πρέπει να παρουσιάζεται ως:

- completed PHM system,
- online fault diagnosis platform,
- validated anomaly detector,
- RUL estimation framework,
- deployed digital twin service,
- graph-model input packaging as graph-learning evidence,
- ολοκληρωμένο graph-learning benchmark.

## Προτεινόμενη ακαδημαϊκή διατύπωση

> Το repository αναπτύσσει μια forecasting-first, reproducible pipeline για spatio-temporal wind power forecasting στο DaKS dataset, με current extension προς downstream residual diagnostics, park-level diagnostic consolidation, graph-contract verification και graph-model input packaging, και μελλοντική δυνατότητα επέκτασης προς condition-awareness-oriented και PHM-oriented research directions.

## Τελικό μήνυμα

Η σωστή εξέλιξη του project είναι:

> forecasting benchmark backbone -> downstream residual diagnostics -> park-level diagnostics consolidation -> graph contract verification -> graph-model input packaging -> future advanced forecasting models -> broader PHM-oriented research extension

και όχι:

> forecasting -> completed PHM / digital twin claims