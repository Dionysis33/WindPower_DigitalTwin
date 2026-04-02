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
- και strict graph data-interface / split-to-graph contract / artifact verification.

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

Οι implemented baselines είναι:

- **Persistence**
- **Linear Regression**
- **Random Forest**
- **XGBoost**
- **MLP**

## Current diagnostics, consolidation, and graph-verification extension

Πάνω στο benchmarked forecasting stack, το project επεκτείνεται πλέον σε τρία strict downstream / supportive stages:

- `NB08` για row-level residual diagnostics και operating-regime-aware inspection
- `NB09` για park-level diagnostics και thesis-oriented consolidation
- `NB10` για strict graph data-interface / split-to-graph contract / artifact verification

Αυτό το extension layer:

- χρησιμοποιεί canonical exported artifacts και benchmark-safe downstream logic,
- παραμένει forecasting-downstream ή forecasting-supportive,
- υποστηρίζει diagnostics-aware / condition-awareness-oriented interpretation,
- σταθεροποιεί το graph-ready handoff προς future graph-based forecasting work,
- αλλά **δεν** ισχυρίζεται ολοκληρωμένο PHM functionality,
- και **δεν** αποτελεί ακόμη graph-model training stage.

## Planned next

Το planned next βήμα δεν είναι ακόμη νέο graph-training issue, αλλά:

- scope-safe planning για το επόμενο graph-based forecasting stage.

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

> ένα αυστηρά benchmarked forecasting pipeline, εμπλουτισμένο με downstream residual diagnostics, park-level diagnostic consolidation και graph-contract verification, μπορεί να αποτελέσει το επιστημονικά ορθό υπόβαθρο για diagnostics-aware, condition-awareness-oriented και αργότερα PHM-oriented research extensions, χωρίς να συγχέεται το forecasting diagnostics stage με completed prognostics functionality.

## Ακαδημαϊκή χρήση

Το repository έχει αναπτυχθεί στο πλαίσιο **undergraduate research / thesis-oriented work** και δίνει προτεραιότητα σε:

- μεθοδολογική ορθότητα,
- σαφή πειραματική τεκμηρίωση,
- reproducibility,
- benchmark validity,
- και σταδιακή ερευνητική κλιμάκωση από strong baselines προς advanced models.