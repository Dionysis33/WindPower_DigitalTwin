# Data

## Dataset source

Το project βασίζεται στο **DaKS / Kassel dataset**, το οποίο διατίθεται από το Universität Kassel.

Dataset source:
- DaKS dataset portal: https://daks.uni-kassel.de/entities/dataset/57ea0681-d8b2-4e76-b31d-578178961f87

## Σημαντική σημείωση χρήσης

Τα αρχικά δεδομένα **δεν διανέμονται μέσα σε αυτό το repository**.  
Ο χρήστης είναι υπεύθυνος να αποκτήσει πρόσβαση στο dataset από την επίσημη πηγή και να συμμορφώνεται με τους όρους χρήσης, την άδεια και τις ερευνητικές / ακαδημαϊκές προϋποθέσεις που συνοδεύουν το dataset.

Το repository περιλαμβάνει μόνο:

- τον κώδικα επεξεργασίας,
- τη μεθοδολογία,
- τα notebooks,
- και τα παραγόμενα artifacts που είναι απαραίτητα για την ερευνητική pipeline.

## Στόχος της data pipeline

Η data pipeline έχει σχεδιαστεί ώστε να μετασχηματίζει τα raw δεδομένα σε forecasting-ready σύνολα, με έμφαση σε:

- temporal consistency,
- καθαρή διαχείριση missing / anomalous values,
- feature engineering,
- reproducible train / validation / test splitting,
- baseline-ready tabular inputs,
- graph-ready preparation για μελλοντικά μοντέλα.

## Δομή δεδομένων στο repository

Η τρέχουσα λογική οργάνωση ακολουθεί την παρακάτω μορφή:

- `data/raw/`  
  Για raw ή αρχικά δεδομένα εισόδου.

- `data/interim/`  
  Για ενδιάμεσα αποτελέσματα επεξεργασίας.

- `data/processed/`  
  Για τελικά processed αρχεία, όπως:
  - feature-engineered datasets,
  - train / validation / test splits,
  - baseline metrics.

## Τρέχοντα processed artifacts

Με βάση την παρούσα κατάσταση του project, έχουν δημιουργηθεί processed artifacts όπως:

- `master_dataset.csv`
- `final_feature_engineered_dataset.csv`
- `train_final.csv`
- `val_final.csv`
- `test_final.csv`
- `baseline_metrics.csv`

Τα παραπάνω αποτελούν outputs της pipeline και μπορούν να επαναδημιουργηθούν μέσω των notebooks.

## Target variable

Η βασική μεταβλητή πρόβλεψης είναι η:

- `Power_Output_Normalized`

Η επιλογή normalized target βοηθά σε:

- σταθερότερη εκπαίδευση μοντέλων,
- δικαιότερη σύγκριση baselines,
- πιο καθαρή ερμηνεία residuals και error metrics.

## Ενδεικτικά feature groups

Ανάλογα με το στάδιο της pipeline, χρησιμοποιούνται χαρακτηριστικά όπως:

1. **Meteorological / NWP features**
   - θερμοκρασία,
   - σχετική υγρασία,
   - πίεση,
   - wind-related fields.

2. **Derived wind features**
   - wind speed variables,
   - ref wind features,
   - μετασχηματισμένα wind inputs.

3. **Temporal features**
   - hour,
   - month,
   - cyclical encodings (`sin/cos`).

4. **Lag and rolling features**
   - lagged target values,
   - lagged wind values,
   - rolling mean / rolling std.

## Data integrity principles

Η pipeline ακολουθεί τις παρακάτω αρχές:

- **No temporal leakage**
- **Train-first statistics**
- **Consistent feature space across splits**
- **Reproducible preprocessing**
- **Explicit export of final artifacts**

Ιδιαίτερα σημαντικό είναι ότι ο καθαρισμός outliers και τα thresholds για clipping υπολογίζονται με στατιστικά που προέρχονται από το **train split**, ώστε να αποφεύγεται leakage προς validation / test.

## Τι να προσέξει ένας νέος χρήστης

Αν θέλεις να τρέξεις το project από την αρχή:

1. Απόκτησε το dataset από την επίσημη πηγή.
2. Τοποθέτησε τα αρχεία στα κατάλληλα data paths.
3. Έλεγξε το configuration στο `src/config`.
4. Τρέξε τα notebooks με τη σωστή σειρά.
5. Επιβεβαίωσε ότι δημιουργούνται ξανά τα processed outputs.

## Data governance / reproducibility note

Το repository δίνει μεγαλύτερη έμφαση στη **μεθοδολογική αναπαραγωγιμότητα (reproducibility)** παρά στη διανομή έτοιμων δεδομένων.  
Ο στόχος είναι να μπορεί οποιοσδήποτε ερευνητής με νόμιμη πρόσβαση στο dataset να αναπαράγει τα βήματα της pipeline και να επιβεβαιώσει τα αποτελέσματα.