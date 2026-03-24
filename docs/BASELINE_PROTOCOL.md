# Baseline Protocol

## Σκοπός

Το παρόν έγγραφο περιγράφει το **baseline evaluation protocol** του project.  
Ο ρόλος των baselines είναι να λειτουργούν ως καθαρό σημείο αναφοράς (reference point), ώστε κάθε μελλοντικό πιο σύνθετο μοντέλο να αξιολογείται σε δίκαιη και επιστημονικά συνεπή βάση.

## Baseline philosophy

Η φιλοσοφία του baseline track είναι η εξής:

- ξεκινάμε από απλά και ερμηνεύσιμα μοντέλα,
- καθορίζουμε μια ισχυρή reference performance,
- εξετάζουμε αν τα πιο πολύπλοκα μοντέλα προσθέτουν πραγματική αξία,
- αποφεύγουμε claims υπεροχής χωρίς σωστή σύγκριση.

## Current baselines

Στην παρούσα φάση έχουν υλοποιηθεί τα εξής baseline models:

1. **Persistence**
2. **Linear Regression**

Αυτά αποτελούν το πρώτο benchmark επίπεδο του project.

## Data splitting protocol

Η αξιολόγηση βασίζεται σε **temporal split** και όχι σε random split.

Χρησιμοποιούνται τρία διακριτά σύνολα:

- **Train set**
- **Validation set**
- **Test set**

Η χρονική διάσπαση έχει σχεδιαστεί ώστε:

- το validation να ακολουθεί χρονικά το train,
- το test να ακολουθεί χρονικά το validation,
- να μην υπάρχει overlap μεταξύ των splits.

Αυτό είναι κρίσιμο για time-series forecasting και για αποφυγή **look-ahead bias**.

## Leakage prevention

Ένα από τα βασικά methodological constraints του project είναι η αποφυγή **data leakage**.

Για αυτόν τον λόγο:

- τα split boundaries είναι αυστηρά χρονικά,
- οι έλεγχοι ακεραιότητας γίνονται με explicit assertions,
- τα outlier thresholds / clipping limits υπολογίζονται με βάση **train-only statistics**,
- και στη συνέχεια εφαρμόζονται σε validation / test.

Αυτό σημαίνει ότι το validation και το test δεν επηρεάζουν τον καθορισμό preprocessing thresholds.

## Outlier handling protocol

Στο Notebook 05 εφαρμόστηκε train-aware outlier handling με λογική **Z-score clipping**.

Η διαδικασία έχει ως εξής:

1. Υπολογισμός στατιστικών μόνο στο **train split**
2. Εξαγωγή lower / upper thresholds
3. Εφαρμογή clipping στα:
   - train
   - validation
   - test
4. Export των τελικών datasets

Η προσέγγιση αυτή είναι μεθοδολογικά ισχυρότερη από το να υπολογίζονται thresholds στο συνολικό dataset.

## Persistence baseline

Το **Persistence model** λειτουργεί ως naïve forecast:

- η πρόβλεψη για τη χρονική στιγμή `t+1`
- ισούται με την προηγούμενη διαθέσιμη τιμή.

Στο project, η persistence λογική εφαρμόζεται με τρόπο συμβατό με τη δομή του dataset και τη χρονική ακολουθία των observations.

Ο ρόλος του είναι να απαντά στο ερώτημα:

> «Πόσο καλύτερο είναι το μοντέλο μας από μια πολύ απλή, αλλά ισχυρή, baseline υπόθεση;»

## Linear Regression baseline

Η **Linear Regression** αποτελεί το πρώτο πραγματικό learned model του pipeline.

Χρησιμοποιεί forecasting-ready numerical features, όπως:

- NWP variables,
- temporal encodings,
- lag features,
- rolling statistics,
- selected engineered predictors.

Στόχος της δεν είναι να δώσει το τελικό state-of-the-art αποτέλεσμα, αλλά:

- να ελέγξει αν τα engineered features περιέχουν predictive signal,
- να λειτουργήσει ως interpretable benchmark,
- να δείξει αν υπάρχει σαφές κέρδος σε σχέση με το Persistence baseline.

## Evaluation metrics

Η baseline αξιολόγηση βασίζεται στα εξής metrics:

- **MAE**
- **RMSE**
- **R²**

Αυτά αποθηκεύονται σε structured μορφή ώστε να μπορούν να χρησιμοποιηθούν αργότερα σε συγκρίσεις με πιο σύνθετα μοντέλα.

## Diagnostic analysis

Πέρα από τα aggregate metrics, η baseline φάση περιλαμβάνει και **diagnostic analysis**, όπως:

- residual distribution,
- residual plots,
- comparison plots actual vs predicted,
- error analysis σε σχέση με wind-related features.

Η ανάλυση αυτή είναι σημαντική γιατί δεν μας ενδιαφέρει μόνο το συνολικό error, αλλά και το **πού** και **πότε** αποτυγχάνει το μοντέλο.

## Role of diagnostics for future PHM direction

Η residual behavior analysis μπορεί αργότερα να συνδεθεί με:

- abnormal operating regimes,
- anomaly sensitivity,
- health-oriented monitoring,
- turbine prognostics and health management.

Σε αυτή τη φάση, τα diagnostics χρησιμοποιούνται κυρίως ως forecasting diagnostics και όχι ως πλήρες PHM module.

## Current status

Μέχρι στιγμής, το baseline protocol έχει επιβεβαιώσει ότι:

- η feature-engineered pipeline δίνει καλύτερη απόδοση από το naïve Persistence,
- η Linear Regression συλλαμβάνει μέρος της δυναμικής του target,
- αλλά εξακολουθούν να υπάρχουν non-linear effects που δεν περιγράφονται πλήρως από ένα γραμμικό μοντέλο.

Αυτό δικαιολογεί τη μετάβαση σε ισχυρότερα non-linear baselines στο επόμενο στάδιο.

## Next benchmarking step

Το επόμενο βήμα είναι η επέκταση του baseline benchmark set με μη γραμμικά μοντέλα, όπως:

- **Random Forest**
- **XGBoost**
- **MLP**

ώστε να υπάρχει πιο πλήρης σύγκριση πριν τη μετάβαση σε graph-based ή sequence-based αρχιτεκτονικές.