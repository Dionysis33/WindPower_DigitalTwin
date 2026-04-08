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
- και strict graph-model input packaging / data object preparation.

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

Οι implemented baselines είναι:

- **Persistence**
- **Linear Regression**
- **Random Forest**
- **XGBoost**
- **MLP**

## Current diagnostics, consolidation, graph-verification, and packaging extension

Πάνω στο benchmarked forecasting stack, το project επεκτείνεται πλέον σε τέσσερα strict downstream / supportive stages:

- `NB08` για row-level residual diagnostics και operating-regime-aware inspection
- `NB09` για park-level diagnostics και thesis-oriented consolidation
- `NB10` για strict graph data-interface / split-to-graph contract / artifact verification
- `NB11` για strict graph-model input packaging / data object preparation

Αυτό το extension layer:

- χρησιμοποιεί canonical exported artifacts και benchmark-safe downstream logic,
- παραμένει forecasting-downstream ή forecasting-supportive,
- υποστηρίζει diagnostics-aware / condition-awareness-oriented interpretation,
- σταθεροποιεί τόσο το graph-ready contract όσο και το graph-model-ready handoff προς future graph-based forecasting work,
- αλλά **δεν** ισχυρίζεται ολοκληρωμένο PHM functionality,
- **δεν** αποτελεί graph-model training stage,
- και **δεν** αποτελεί graph-benchmarking evidence.

## Planned next

Το planned next βήμα δεν είναι πλέον graph-model input packaging issue, γιατί αυτό έχει ήδη υλοποιηθεί στο `NB11`.

Το planned next είναι:

- scope-safe planning για το πρώτο actual graph-based forecasting stage μετά το packaging layer.

## Future work

Τα παρακάτω παραμένουν future work / research extension:

- graph-based forecasting models,
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
- ολοκληρωμένο GNN training benchmark,
- ή deployed digital twin service.

Η σωστή ακαδημαϊκή θέση του repository είναι ότι τα forecasting residuals, τα park-level diagnostic patterns και η graph-ready verification pipeline μπορούν να λειτουργήσουν ως **diagnostic signal candidates** και ως **methodological infrastructure** για μελλοντική condition-awareness-oriented και PHM-oriented έρευνα, όχι ως τεκμηριωμένη health-state inference από μόνα τους.

## Κεντρική ερευνητική θέση

Η βασική ερευνητική θέση είναι:

> ένα αυστηρά benchmarked forecasting pipeline, εμπλουτισμένο με downstream residual diagnostics, park-level diagnostic consolidation, graph-contract verification και graph-model input packaging, μπορεί να αποτελέσει το επιστημονικά ορθό υπόβαθρο για diagnostics-aware, condition-awareness-oriented και αργότερα PHM-oriented research extensions, χωρίς να συγχέεται το forecasting diagnostics stage ή το packaging stage με completed prognostics functionality.

## Ακαδημαϊκή χρήση

Το repository έχει αναπτυχθεί στο πλαίσιο **undergraduate research / thesis-oriented work** και δίνει προτεραιότητα σε:

- μεθοδολογική ορθότητα,
- σαφή πειραματική τεκμηρίωση,
- reproducibility,
- benchmark validity,
- και σταδιακή ερευνητική κλιμάκωση από strong baselines προς advanced models.