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

## Current diagnostics extension

Το current downstream diagnostics layer δεν είναι νέο modeling stage, αλλά μια **strict forecasting-downstream diagnostics extension** πάνω στα exported baseline predictions.

Σήμερα αυτό περιλαμβάνει δύο implemented notebooks:

- `NB08` για residual diagnostics και operating-regime-aware inspection
- `NB09` για park-level diagnostics και thesis-consolidation layer

Αυτό περιλαμβάνει:

- residual behavior inspection,
- operating-regime-aware slicing,
- comparison των implemented baselines σε diagnostic space,
- park-level diagnostic aggregation,
- representative case-study consolidation,
- και προσεκτική health-aware interpretation.

## Γιατί αυτό συνδέεται με PHM

Στα wind energy systems, τα forecasting residuals μπορεί να σχετίζονται με:

- departures from expected operating behavior,
- shifts across operating regimes,
- performance drift,
- και wider condition-awareness questions.

Αυτό όμως δεν σημαίνει ότι το repository έχει ήδη validated fault diagnosis ή prognostics engine.

## Stage-wise research path

### Stage 1 — Forecasting foundation (implemented)
- raw validation
- EDA
- feature engineering
- temporal split
- reproducible preprocessing

### Stage 2 — Baseline ladder (implemented)
- Persistence
- Linear Regression
- Random Forest
- XGBoost
- MLP

### Stage 3 — Downstream diagnostics extension (implemented current extension)
- row-level residual diagnostics
- operating-regime analysis
- error structure inspection
- park-level diagnostic aggregation
- thesis-oriented case-study consolidation
- diagnostics-aware / health-aware interpretation

### Stage 4 — Stronger PHM-oriented interpretation (future work)
- more systematic residual slicing
- anomaly-awareness hypotheses
- degradation-oriented discussion
- stronger uncertainty-aware diagnostics framing

### Stage 5 — Advanced forecasting models (future work)
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
- deployed digital twin service.

## Προτεινόμενη ακαδημαϊκή διατύπωση

> Το repository αναπτύσσει μια forecasting-first, reproducible pipeline για spatio-temporal wind power forecasting στο DaKS dataset, με current extension προς downstream residual diagnostics και park-level diagnostic consolidation, και μελλοντική δυνατότητα επέκτασης προς health-aware και PHM-oriented research directions.

## Τελικό μήνυμα

Η σωστή εξέλιξη του project είναι:

> forecasting benchmark backbone -> downstream residual diagnostics -> park-level diagnostics consolidation -> future advanced forecasting models -> broader PHM-oriented research extension

και όχι:

> forecasting -> completed PHM / digital twin claims