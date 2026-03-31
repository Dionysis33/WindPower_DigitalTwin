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
- park-level diagnostics και thesis-oriented consolidation.

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

Οι implemented baselines είναι:

- **Persistence**
- **Linear Regression**
- **Random Forest**
- **XGBoost**
- **MLP**

## Current diagnostics and thesis-consolidation extension

Πάνω στο benchmarked forecasting stack, το project επεκτείνεται πλέον σε ένα **strict downstream diagnostics layer** με δύο implemented stages:

- `NB08` για row-level residual diagnostics και operating-regime-aware inspection
- `NB09` για park-level diagnostics και thesis-oriented consolidation

Αυτό το diagnostics layer:

- χρησιμοποιεί exported baseline predictions και κοινό canonical test-only evaluation space,
- παραμένει forecasting-downstream,
- υποστηρίζει diagnostics-aware / health-aware interpretation,
- αλλά **δεν** ισχυρίζεται ολοκληρωμένο PHM functionality.

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
- production-grade health monitoring.

Η σωστή ακαδημαϊκή θέση του repository είναι ότι τα forecasting residuals και τα park-level diagnostic patterns μπορούν να λειτουργήσουν ως **diagnostic signal candidates**, όχι ως τεκμηριωμένη health-state inference από μόνα τους.

## Κεντρική ερευνητική θέση

Η βασική ερευνητική θέση είναι:

> ένα αυστηρά benchmarked forecasting pipeline μπορεί να αποτελέσει το επιστημονικά ορθό υπόβαθρο για diagnostics-aware, park-level και αργότερα PHM-oriented research extensions, χωρίς να συγχέεται το forecasting diagnostics stage με completed prognostics functionality.

## Ακαδημαϊκή χρήση

Το repository έχει αναπτυχθεί στο πλαίσιο **undergraduate research / thesis-oriented work** και δίνει προτεραιότητα σε:

- μεθοδολογική ορθότητα,
- σαφή πειραματική τεκμηρίωση,
- reproducibility,
- σταδιακή ερευνητική κλιμάκωση από strong baselines προς advanced models.