# Baseline Protocol

## Σκοπός

Το παρόν έγγραφο ορίζει το **baseline evaluation protocol** του project.

Η baseline ladder λειτουργεί ως το κοινό benchmark backbone πάνω στο οποίο στηρίζονται:

- η δίκαιη cross-model comparison,
- η downstream residual diagnostics analysis,
- και οι μελλοντικές συγκρίσεις με graph-based ή sequence-based models.

## Baseline philosophy

Η φιλοσοφία του baseline track είναι η εξής:

- ξεκινάμε από απλά και ερμηνεύσιμα μοντέλα,
- καθορίζουμε μια ισχυρή reference performance,
- εξετάζουμε αν τα πιο πολύπλοκα μοντέλα προσθέτουν πραγματική αξία,
- αποφεύγουμε claims υπεροχής χωρίς σωστή σύγκριση.

## Current implemented baselines

Στην current canonical baseline ladder περιλαμβάνονται:

1. **Persistence**
2. **Linear Regression**
3. **Random Forest**
4. **XGBoost**
5. **MLP**

## Data splitting protocol

Η αξιολόγηση βασίζεται σε **strict temporal split** και όχι σε random split.

Χρησιμοποιούνται:

- **Train**
- **Validation**
- **Test**

Το validation χρησιμοποιείται μόνο για model selection όπου απαιτείται.  
Το test χρησιμοποιείται μόνο για final reporting.

## Leakage prevention

Το protocol επιβάλλει:

- χρονικά απομονωμένα splits,
- consistent feature space across splits,
- train-only preprocessing statistics,
- benchmark-safe reporting.

Τα outlier thresholds / clipping limits υπολογίζονται με βάση **train-only statistics** και εφαρμόζονται downstream χωρίς leakage προς validation ή test.

## Outlier handling protocol

Στο `NB05` εφαρμόστηκε train-aware outlier handling με λογική **Z-score clipping**.

Η διαδικασία έχει ως εξής:

1. Υπολογισμός στατιστικών μόνο στο **train split**
2. Εξαγωγή lower / upper thresholds
3. Εφαρμογή clipping στα:
   - train
   - validation
   - test
4. Export των τελικών datasets

## Canonical benchmark artifact

Για cross-model reporting, canonical artifact είναι το:

`data/processed/baseline_metrics.csv`

Το artifact αυτό ερμηνεύεται ως:

- **final test-set benchmark table**
- με canonical metric naming:
  - **MAE**
  - **RMSE**
  - **R²**
- και με primary ranking criterion το **MAE (ascending)**.

## Role of diagnostics

Η baseline phase δεν τελειώνει στα aggregate metrics.

Το benchmark stack υποστηρίζει downstream:

- residual distribution analysis,
- actual-vs-predicted comparison,
- operating-regime-aware error inspection,
- structured comparison μεταξύ implemented baselines,
- και park-level diagnostic aggregation.

## Current diagnostics extension

Μετά την ολοκλήρωση της baseline πεντάδας, το current implemented downstream layer έχει δύο διακριτά notebooks:

- `NB08` -> downstream residual diagnostics and operating regimes
- `NB09` -> park-level diagnostics and thesis consolidation

Αυτό σημαίνει ότι η αμέσως επόμενη canonical ερμηνευτική φάση είναι:

> benchmarked forecasting -> downstream residual diagnostics -> park-level consolidation

και όχι:

> baseline ladder -> άμεσο νέο modeling stage

## PHM-oriented interpretation boundary

Τα diagnostics μπορούν να συζητηθούν ως βάση για:

- diagnostics-aware interpretation,
- health-aware discussion,
- PHM-oriented future work.

Όμως σε αυτή τη φάση τα diagnostics παραμένουν **forecasting diagnostics** και όχι completed PHM module.

## Current status

Η current canonical baseline ladder έχει ολοκληρωθεί και λειτουργεί ως benchmark backbone για:

- `NB06` baseline modeling
- `NB07` advanced tabular baselines
- `NB08` downstream residual diagnostics
- `NB09` park-level diagnostics and thesis consolidation

## Next benchmarking / modeling step

Αφού σταθεροποιηθεί και το downstream diagnostics / consolidation layer, το επόμενο modeling step παραμένει future work:

- graph-based forecasting models,
- sequence-based models,
- GNN / Mamba / Graph-Mamba experimentation.

Άρα η baseline ladder πρέπει να αντιμετωπίζεται ως:

> canonical benchmark backbone for diagnostics today, park-level consolidation now, and advanced modeling tomorrow