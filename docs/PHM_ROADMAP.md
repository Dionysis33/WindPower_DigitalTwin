# PHM Roadmap

## Γιατί χρειάζεται αυτό το roadmap

Το project ξεκίνησε και παραμένει **forecasting-first**.  
Η σύνδεση προς **turbine prognostics and health management (PHM)** είναι πραγματική ως ερευνητική κατεύθυνση, αλλά πρέπει να διατυπώνεται με αυστηρό scientific correctness και χωρίς overclaiming.

## Current implemented backbone

Σήμερα το repository έχει ήδη ολοκληρώσει ένα forecasting-first benchmark pipeline που περιλαμβάνει:

- raw validation,
- validated-only EDA,
- feature engineering,
- leakage-aware temporal split,
- baseline benchmarking,
- advanced tabular baselines,
- downstream residual diagnostics,
- park-level diagnostics / thesis consolidation,
- graph data-interface / split-to-graph contract / artifact verification,
- graph-model input packaging / data object preparation,
- πρώτο actual graph-based forecasting baseline,
- και graph ablation / spatial sensitivity follow-up.

## Current diagnostics and graph-extension layer

Το current downstream / graph-extension layer δεν αποτελεί deployed PHM stage, αλλά μια **strict forecasting-downstream and graph-aware research extension** πάνω στα canonical exported artifacts.

Σήμερα αυτό περιλαμβάνει έξι implemented notebooks:

- `NB08` για residual diagnostics και operating-regime-aware inspection
- `NB09` για park-level diagnostics και thesis-consolidation layer
- `NB10` για strict graph data-interface / split-to-graph contract / artifact verification
- `NB11` για strict graph-model input packaging / data object preparation
- `NB12` για first actual graph-based forecasting baseline
- `NB13` για graph ablation / spatial sensitivity analysis ως strict follow-up του `NB12`

Αυτό το extension layer περιλαμβάνει:

- residual behavior inspection,
- operating-regime-aware slicing,
- comparison των implemented baselines σε diagnostic space,
- park-level diagnostic aggregation,
- representative case-study consolidation,
- cautious health-aware interpretation,
- graph-ready contract verification,
- graph-model input packaging,
- first graph-based forecasting evidence,
- και topology-aware graph follow-up analysis.

## Γιατί αυτό συνδέεται με PHM

Στα wind energy systems, τα forecasting residuals, τα operating-regime patterns, τα park-level differences και οι topology-aware graph comparisons μπορεί να σχετίζονται με:

- departures from expected operating behavior,
- shifts across operating regimes,
- performance drift,
- condition-awareness questions,
- spatially structured forecasting difficulty,
- και wider diagnostic hypotheses.

Παράλληλα, ένα strict graph data-interface / artifact-verification stage, ένα strict graph-model input packaging stage, ένα first graph-based forecasting baseline και ένα topology-aware graph ablation stage είναι χρήσιμα γιατί επιτρέπουν future graph-aware forecasting and diagnostics research πάνω σε benchmark-safe, contract-safe και μεθοδολογικά καθαρό υπόβαθρο.

Αυτό όμως **δεν** σημαίνει ότι το repository έχει ήδη:

- validated fault diagnosis,
- anomaly detection module,
- prognostics engine,
- RUL estimation,
- ή completed PHM functionality.

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
- benchmark-safe handoff to graph-based forecasting experiments

### Stage 6 — First graph-based forecasting baseline (implemented)
- canonical packaged graph artifact loading
- fail-fast integrity checks
- snapshot-level graph dataset construction
- benchmark-safe DataLoader materialization
- validation-only model selection
- test-only final reporting
- compact graph-baseline export layer

### Stage 7 — Graph ablation / spatial sensitivity follow-up (implemented)
- frozen `NB12`-compatible training configuration
- deterministic topology variants
- controlled sensitivity analysis
- benchmark-safe reference comparison
- topology-aware interpretation without superiority claims

### Stage 8 — Broader graph and sequence research (future work)
- broader graph redesign
- richer spatio-temporal graph formulations
- sequence models
- GNN / Mamba / Graph-Mamba experimentation
- stronger graph claims only if supported by new evidence

### Stage 9 — Broader PHM-oriented research extension (future work)
- anomaly-aware analysis
- fault-oriented diagnostics
- degradation monitoring
- prognostics-oriented modeling
- stronger digital-twin integration

## Current graph interpretation boundary

Το `NB12` και το `NB13` επεκτείνουν πράγματι το repository από graph-readiness σε actual graph-based forecasting experimentation.

Όμως:

- το `NB12` δεν τεκμηριώνει graph superiority έναντι του canonical benchmark backbone,
- το `NB13` δείχνει sensitivity στην topology choice αλλά μικρό spatial gain,
- και κανένα `NB13` run δεν βελτιώνει το `NB12` reference στο primary benchmark criterion (`test MAE`).

Άρα το current graph layer πρέπει να αντιμετωπίζεται ως:

- implemented graph-based forecasting evidence,
- topology-aware follow-up evidence,
- αλλά όχι ως validated superiority result.

## Τι δεν πρέπει να ισχυρίζεται ακόμη το repository

Το project δεν πρέπει να παρουσιάζεται ως:

- completed PHM system,
- online fault diagnosis platform,
- validated anomaly detector,
- fault classification system,
- RUL estimation framework,
- deployed digital twin service,
- validated GNN / Graph-Mamba superiority,
- ή ολοκληρωμένο graph-learning benchmark.

Επίσης, δεν πρέπει να συγχέονται:

- residual diagnostics,
- park-level diagnostics,
- graph contract verification,
- graph-model input packaging,
- graph baseline evidence,
- και graph ablation evidence

με validated health-state inference ή completed prognostics functionality.

## Προτεινόμενη ακαδημαϊκή διατύπωση

> Το repository αναπτύσσει μια forecasting-first, reproducible pipeline για spatio-temporal wind power forecasting στο DaKS dataset, με implemented extension προς downstream residual diagnostics, park-level diagnostic consolidation, graph-contract verification, graph-model input packaging, πρώτο graph-based forecasting baseline και topology-aware graph ablation, και μελλοντική δυνατότητα επέκτασης προς condition-awareness-oriented και PHM-oriented research directions χωρίς overclaiming ως προς current health-state inference ή graph superiority.

## Τελικό μήνυμα

Η σωστή εξέλιξη του project είναι:

> forecasting benchmark backbone -> downstream residual diagnostics -> park-level diagnostics consolidation -> graph contract verification -> graph-model input packaging -> first graph-based forecasting baseline -> topology-aware graph ablation -> broader graph / sequence research if justified -> broader PHM-oriented research extension

και όχι:

> forecasting -> completed PHM / digital twin / graph-superiority claims