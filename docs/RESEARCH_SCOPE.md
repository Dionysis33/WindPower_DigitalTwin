# Research Scope

## Σκοπός του έργου

Το παρόν repository υποστηρίζει την ανάπτυξη μιας ερευνητικής pipeline για **spatio-temporal wind power forecasting** πάνω στο **DaKS / Kassel dataset**, με έμφαση στη σωστή προεπεξεργασία δεδομένων, στα ισχυρά **baseline models** και στη μελλοντική επέκταση προς πιο σύνθετες **graph-based** και **sequence-based** αρχιτεκτονικές.

Η εργασία δεν αντιμετωπίζει το forecasting ως ένα απομονωμένο prediction task. Αντίθετα, το προσεγγίζει ως θεμέλιο για μια ευρύτερη κατεύθυνση προς **turbine prognostics and health management (PHM)**, όπου η πρόβλεψη ισχύος, η ανάλυση residuals και η συμπεριφορά του μοντέλου μπορούν αργότερα να αξιοποιηθούν για **anomaly awareness**, **degradation monitoring** και **health-oriented diagnostics**.

## Ερευνητική κατεύθυνση

Το project αυτή τη στιγμή επικεντρώνεται στα εξής:

1. **Data integrity and reproducibility**  
   Κατασκευή καθαρής και επαναλήψιμης ροής επεξεργασίας, από την απόκτηση των δεδομένων μέχρι τα τελικά train / validation / test splits.

2. **Feature engineering for forecasting**  
   Δημιουργία forecasting-ready χαρακτηριστικών, όπως:
   - temporal features,
   - lag features,
   - rolling statistics,
   - wind-related derived variables,
   - graph-ready πληροφορία για μελλοντική αξιοποίηση.

3. **Baseline benchmarking**  
   Αξιολόγηση απλών αλλά επιστημονικά χρήσιμων μοντέλων αναφοράς, ώστε κάθε επόμενο πιο σύνθετο μοντέλο να συγκρίνεται με σαφή και δίκαιο τρόπο.

4. **Future transition to PHM-oriented modeling**  
   Σταδιακή μετατόπιση από το καθαρό forecasting προς ένα πιο ολοκληρωμένο πλαίσιο που συνδέεται με:
   - error behavior,
   - residual patterns,
   - abnormal operating conditions,
   - prognostics / health management.

## Τι περιλαμβάνεται αυτή τη στιγμή

Μέχρι στιγμής, το repository περιλαμβάνει:

- data acquisition and exploration notebooks,
- exploratory data analysis,
- feature engineering and graph construction preparation,
- outlier handling και train-aware temporal splitting,
- baseline modeling με:
  - **Persistence model**
  - **Linear Regression**
- αποθήκευση metrics και βασικά diagnostic plots.

## Τι δεν ισχυρίζεται ακόμη το project

Για λόγους επιστημονικής ακρίβειας, το project **δεν ισχυρίζεται ακόμη** ότι διαθέτει:

- ολοκληρωμένο **Digital Twin deployment**,
- πλήρες **fault diagnosis**,
- πλήρες **remaining useful life (RUL)** framework,
- production-grade online monitoring system,
- τελικά αποτελέσματα από **GNN / Mamba / Transformer** μοντέλα.

Αυτά αποτελούν **μελλοντική ερευνητική κατεύθυνση** και όχι ήδη υλοποιημένη δυνατότητα.

## Κεντρική ερευνητική θέση

Η βασική υπόθεση του έργου είναι ότι ένα σωστά δομημένο forecasting pipeline μπορεί να λειτουργήσει ως το πρώτο βήμα για ένα πιο ώριμο σύστημα **wind turbine prognostics and health management**, όπου:

- το forecasting error δεν είναι απλώς σφάλμα πρόβλεψης,
- αλλά πιθανό diagnostic signal,
- ειδικά όταν αναλύεται σε συνάρτηση με operational conditions, όπως η ταχύτητα ανέμου και η χρονική δυναμική του συστήματος.

## Ακαδημαϊκή χρήση

Το repository έχει αναπτυχθεί στο πλαίσιο **undergraduate research / thesis-oriented work** και δίνει προτεραιότητα σε:

- μεθοδολογική ορθότητα,
- σαφή πειραματική τεκμηρίωση,
- reproducibility,
- σταδιακή ερευνητική κλιμάκωση από simple baselines προς advanced models.