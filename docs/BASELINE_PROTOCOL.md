# Baseline Protocol

## Σκοπός

Το παρόν έγγραφο ορίζει το **baseline evaluation protocol** του project.

Η baseline ladder λειτουργεί ως το κοινό benchmark backbone πάνω στο οποίο στηρίζονται:

- η δίκαιη cross-model comparison,
- η downstream residual diagnostics analysis,
- η park-level diagnostics consolidation,
- οι graph-ready verification και graph-packaging stages,
- και οι cautious συγκρίσεις με implemented graph-based forecasting stages.

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

Τα `NB10`–`NB13` μπορούν να καταναλώνουν canonical split, graph ή benchmark artifacts downstream, αλλά **δεν** επαναορίζουν το `data/processed/baseline_metrics.csv` ως graph benchmark table.

Το benchmark artifact παραμένει canonical authority μόνο για cross-model **test-set baseline reporting** και όχι για graph packaging, graph verification, graph ablation ή graph follow-up exports.

## Role of diagnostics

Η baseline phase δεν τελειώνει στα aggregate metrics.

Το benchmark stack υποστηρίζει downstream:

- residual distribution analysis,
- actual-vs-predicted comparison,
- operating-regime-aware error inspection,
- structured comparison μεταξύ implemented baselines,
- park-level diagnostic aggregation,
- και condition-awareness-oriented interpretation.

## Current downstream and graph-extension path

Μετά την ολοκλήρωση της baseline πεντάδας, το current implemented downstream / graph-extension layer έχει έξι διακριτά notebooks:

- `NB08` -> downstream residual diagnostics and operating regimes
- `NB09` -> park-level diagnostics and thesis consolidation
- `NB10` -> graph data-interface / split-to-graph contract / artifact verification
- `NB11` -> graph-model input packaging / data object preparation
- `NB12` -> first graph-based forecasting baseline
- `NB13` -> graph ablation / spatial sensitivity analysis

Αυτό σημαίνει ότι η canonical ερμηνευτική και graph-extension φάση είναι πλέον:

> benchmarked forecasting -> downstream residual diagnostics -> park-level consolidation -> graph contract verification -> graph-model input packaging -> first graph-based forecasting baseline -> topology-aware graph ablation

και όχι:

> baseline ladder -> άμεσο speculative future graph stage

## Benchmark-safe model-selection and reporting rule

Σε όλο το repository, όπου υπάρχει model fitting, πρέπει να διατηρείται ο εξής κανόνας:

- **validation only for model selection**
- **test only for final reporting**

Αυτό ισχύει:
- για την tabular baseline ladder,
- για το `NB12`,
- και για το `NB13` follow-up comparison framework.

## Graph interpretation boundary

Το `NB12` αποτελεί το πρώτο actual graph-based forecasting baseline του repository.

Το `NB13` αποτελεί strict follow-up sensitivity / ablation stage πάνω σε frozen `NB12`-compatible training configuration.

Όμως:

- το `NB12` δεν τεκμηριώνει graph superiority έναντι του canonical benchmark backbone,
- το `NB13` δείχνει topology sensitivity αλλά μικρό spatial gain,
- και κανένα `NB13` run δεν βελτιώνει το `NB12` reference στο primary benchmark criterion (`test MAE`).

Άρα τα current graph stages πρέπει να αντιμετωπίζονται ως:

- implemented graph-based forecasting evidence,
- cautious topology-aware follow-up evidence,
- αλλά όχι ως validated superiority result.

## PHM-oriented interpretation boundary

Τα diagnostics και τα graph stages μπορούν να συζητηθούν ως βάση για:

- diagnostics-aware interpretation,
- condition-awareness-oriented discussion,
- health-aware framing,
- PHM-oriented future work.

Όμως σε αυτή τη φάση:

- τα diagnostics παραμένουν **forecasting diagnostics** και όχι completed PHM module,
- το `NB10` παραμένει **graph-readiness verification stage**,
- το `NB11` παραμένει **graph-model input packaging stage**,
- το `NB12` παραμένει **first graph forecasting baseline**,
- και το `NB13` παραμένει **graph ablation / spatial sensitivity follow-up**,

χωρίς να μετατρέπεται το repository σε:
- validated PHM system,
- validated anomaly detector,
- ολοκληρωμένο graph-learning benchmark,
- ή validated GNN / Graph-Mamba superiority claim.

## Current status

Η current canonical baseline ladder έχει ολοκληρωθεί και λειτουργεί ως benchmark backbone για:

- `NB06` baseline modeling
- `NB07` advanced tabular baselines
- `NB08` downstream residual diagnostics
- `NB09` park-level diagnostics and thesis consolidation
- `NB10` graph data-interface / split-to-graph contract / artifact verification
- `NB11` graph-model input packaging / data object preparation
- `NB12` first graph-based forecasting baseline
- `NB13` graph ablation / spatial sensitivity analysis

## Planned next vs future modeling step

Το planned next βήμα δεν είναι πλέον ούτε packaging issue ούτε το πρώτο graph-based forecasting stage, επειδή αυτά έχουν ήδη υλοποιηθεί στα `NB11` και `NB12`.

Το planned next είναι:

- scope-safe consolidation του post-NB13 benchmark interpretation boundary
- και στη συνέχεια broader graph refinement μόνο αν αυτό δικαιολογείται από νέα benchmark evidence

Τα παρακάτω παραμένουν future work:

- broader graph redesign,
- stronger graph-based forecasting claims μόνο αν υποστηριχθούν από νέα evidence,
- sequence-based models,
- GNN / Mamba / Graph-Mamba experimentation,
- broader PHM-oriented modeling.

## Final principle

Η baseline ladder πρέπει να αντιμετωπίζεται ως:

> the canonical benchmark backbone of the repository

και όχι ως:

> a stage that can be bypassed or relativized by speculative graph complexity claims χωρίς benchmark-safe evidence.