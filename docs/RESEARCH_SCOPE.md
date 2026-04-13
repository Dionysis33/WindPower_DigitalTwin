# Research Scope

## Σκοπός του έργου

Το repository υποστηρίζει μια **forecasting-first, reproducible research pipeline** για **spatio-temporal wind power forecasting** πάνω στο **DaKS / Kassel synthetic wind power dataset**.

Ο πυρήνας της εργασίας είναι η μεθοδολογικά αυστηρή ακολουθία:

- raw validation,
- validated-only EDA,
- feature engineering,
- leakage-aware temporal split,
- baseline benchmarking,
- downstream residual diagnostics,
- park-level diagnostics και thesis-oriented consolidation,
- strict graph data-interface / split-to-graph contract / artifact verification,
- strict graph-model input packaging / data object preparation,
- πρώτο actual graph-based forecasting baseline,
- και strict graph ablation / spatial sensitivity follow-up.

## Τι είναι ήδη implemented

Μέχρι στιγμής, το implemented public core περιλαμβάνει:

- `NB02` raw validation
- `NB03` validated-only EDA
- `NB04` feature engineering
- `NB05` outlier handling / temporal split
- `NB06` baseline modeling
- `NB07` advanced tabular baselines
- `NB08` downstream residual diagnostics and operating regimes
- `NB09` park-level diagnostics and thesis consolidation
- `NB10` graph data-interface / split-to-graph contract / artifact verification
- `NB11` graph-model input packaging / data object preparation
- `NB12` first graph-based forecasting baseline
- `NB13` graph ablation / spatial sensitivity analysis

Οι implemented baselines είναι:

- **Persistence**
- **Linear Regression**
- **Random Forest**
- **XGBoost**
- **MLP**

## Current diagnostics, graph, and cautious forecasting extension

Πάνω στο benchmarked forecasting stack, το project επεκτείνεται πλέον σε έξι strict downstream / graph-extension stages:

- `NB08` για row-level residual diagnostics και operating-regime-aware inspection
- `NB09` για park-level diagnostics και thesis-oriented consolidation
- `NB10` για strict graph data-interface / split-to-graph contract / artifact verification
- `NB11` για strict graph-model input packaging / data object preparation
- `NB12` για first actual graph-based forecasting baseline
- `NB13` για graph ablation / spatial sensitivity analysis ως strict follow-up του `NB12`

Αυτό το extension layer:

- χρησιμοποιεί canonical exported artifacts και benchmark-safe evaluation logic,
- παραμένει forecasting-first και non-overclaiming,
- διατηρεί validation-only model selection και test-only final reporting όπου υπάρχει model fitting,
- επεκτείνει το repository από graph-readiness σε actual graph-based forecasting experimentation,
- αλλά **δεν** τεκμηριώνει ακόμη validated graph superiority,
- **δεν** ισχυρίζεται ολοκληρωμένο PHM functionality,
- και **δεν** αποτελεί completed graph-learning benchmark beyond the current cautious baseline and ablation evidence.

## Planned next

Το planned next βήμα δεν είναι πλέον ούτε graph-model input packaging issue ούτε το πρώτο actual graph-based forecasting stage, επειδή αυτά έχουν ήδη υλοποιηθεί στα `NB11` και `NB12`.

Το άμεσο planned next είναι:

- scope-safe planning για broader graph refinement μόνο αν δικαιολογείται από το current benchmark evidence
- και, μόνο εφόσον υπάρξει νέα τεκμηριωμένη ανάγκη, future experiment planning χωρίς premature superiority claims

## Future work

Τα παρακάτω παραμένουν future work / research extension:

- broader graph redesign,
- stronger graph-based forecasting claims μόνο αν υποστηριχθούν από νέα evidence,
- sequence-based forecasting models,
- GNN / Mamba / Graph-Mamba experimentation,
- stronger digital-twin integration,
- broader PHM-oriented modeling.

## Scope boundary

Το project **δεν** ισχυρίζεται σήμερα ότι διαθέτει:

- completed PHM system,
- validated anomaly detector,
- fault classification,
- remaining useful life estimation,
- production-grade health monitoring,
- validated GNN / Graph-Mamba superiority,
- ολοκληρωμένο graph-learning benchmark,
- ή deployed digital twin service.

Η σωστή ακαδημαϊκή θέση του repository είναι ότι τα forecasting residuals, τα park-level diagnostic patterns, το graph contract verification, το graph-model input packaging, το πρώτο graph-based baseline και το topology-aware graph ablation layer μπορούν να λειτουργήσουν ως **diagnostic signal candidates**, ως **benchmark-safe graph evidence**, και ως **methodological infrastructure** για μελλοντική condition-awareness-oriented και PHM-oriented έρευνα, όχι ως τεκμηριωμένη health-state inference ή validated graph superiority από μόνα τους.

## Κεντρική ερευνητική θέση

Η βασική ερευνητική θέση είναι:

> ένα αυστηρά benchmarked forecasting pipeline, εμπλουτισμένο με downstream residual diagnostics, park-level diagnostic consolidation, graph-contract verification, graph-model input packaging, πρώτο graph-based forecasting baseline και topology-aware graph ablation, μπορεί να αποτελέσει το επιστημονικά ορθό υπόβαθρο για diagnostics-aware, condition-awareness-oriented και αργότερα PHM-oriented research extensions, χωρίς να συγχέεται το forecasting diagnostics stage ή το current graph stage με completed prognostics functionality ή validated graph superiority.

## Ακαδημαϊκή χρήση

Το repository έχει αναπτυχθεί στο πλαίσιο **undergraduate research / thesis-oriented work** και δίνει προτεραιότητα σε:

- μεθοδολογική ορθότητα,
- σαφή πειραματική τεκμηρίωση,
- reproducibility,
- benchmark validity,
- non-overclaiming interpretation,
- και σταδιακή ερευνητική κλιμάκωση από strong baselines προς advanced models.