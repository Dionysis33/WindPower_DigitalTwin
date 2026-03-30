# Research Scope

## Σκοπός του έργου

Το repository υποστηρίζει μια **forecasting-first, reproducible research pipeline** για **spatio-temporal wind power forecasting** πάνω στο **DaKS / Kassel synthetic wind power dataset**.

Ο πυρήνας της εργασίας είναι η μεθοδολογικά αυστηρή ακολουθία:

- raw validation,
- validated-only EDA,
- feature engineering,
- leakage-aware temporal split,
- baseline benchmarking,
- downstream residual diagnostics.

## Τι είναι ήδη implemented

Μέχρι στιγμής, το implemented public core περιλαμβάνει:

- `NB02` raw validation
- `NB03` validated-only EDA
- `NB04` feature engineering
- `NB05` outlier handling / temporal split
- `NB06` baseline modeling
- `NB07` advanced tabular baselines
- `NB08` downstream residual diagnostics and operating regimes

Οι implemented baselines είναι:

- **Persistence**
- **Linear Regression**
- **Random Forest**
- **XGBoost**
- **MLP**

## Current diagnostics extension

Πάνω στο benchmarked forecasting stack, το project επεκτείνεται σε **strict downstream diagnostics** μέσω residual analysis και operating-regime-aware inspection.

Αυτό το diagnostics layer:

- χρησιμοποιεί exported baseline predictions,
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

Η σωστή ακαδημαϊκή θέση του repository είναι ότι το forecasting residual μπορεί να λειτουργήσει ως **diagnostic signal candidate**, όχι ως τεκμηριωμένη health-state inference από μόνο του.

## Κεντρική ερευνητική θέση

Η βασική ερευνητική θέση είναι:

> ένα αυστηρά benchmarked forecasting pipeline μπορεί να αποτελέσει το επιστημονικά ορθό υπόβαθρο για diagnostics-aware και αργότερα PHM-oriented research extensions, χωρίς να συγχέεται το forecasting diagnostics stage με completed prognostics functionality.

## Ακαδημαϊκή χρήση

Το repository έχει αναπτυχθεί στο πλαίσιο **undergraduate research / thesis-oriented work** και δίνει προτεραιότητα σε:

- μεθοδολογική ορθότητα,
- σαφή πειραματική τεκμηρίωση,
- reproducibility,
- σταδιακή ερευνητική κλιμάκωση από strong baselines προς advanced models.