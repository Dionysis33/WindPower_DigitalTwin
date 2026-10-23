# Baseline Protocol

## Σκοπός

Το παρόν έγγραφο ορίζει το **πρωτόκολλο αξιολόγησης των baseline μοντέλων** του project.

Τα baseline μοντέλα παρέχουν το κοινό σημείο αναφοράς για:

- τη δίκαιη σύγκριση μοντέλων,
- την ανάλυση residuals,
- τη συγκέντρωση διαγνωστικών αποτελεσμάτων ανά πάρκο,
- τους ελέγχους και την προετοιμασία δεδομένων για graph μοντέλα,
- και την προσεκτική σύγκριση με τα υλοποιημένα graph-based forecasting μοντέλα.

## Baseline philosophy

Η φιλοσοφία του baseline track είναι η εξής:

- ξεκινάμε από απλά και ερμηνεύσιμα μοντέλα,
- καθορίζουμε ένα ισχυρό επίπεδο απόδοσης αναφοράς,
- εξετάζουμε αν τα πιο πολύπλοκα μοντέλα προσθέτουν πραγματική αξία,
- αποφεύγουμε ισχυρισμούς υπεροχής χωρίς κατάλληλη σύγκριση.

## Current implemented baselines

Τα υλοποιημένα tabular baselines είναι:

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
- αναφορά αποτελεσμάτων σύμφωνα με το πρωτόκολλο αξιολόγησης.

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

Το αρχείο του full-dataset tabular benchmark, που περιλαμβανόταν στην προηγούμενη δημόσια έκδοση, διατηρείται τοπικά στο:

`data/processed/baseline_metrics.csv`

Το CSV δεν διανέμεται σε αυτή την έκδοση του repository. Το αρχικό ερευνητικό αρχείο διατηρείται τοπικά, ενώ ελέγχονται η προέλευση των πειραματικών αποτελεσμάτων και η αριθμητική συμφωνία με το Author’s Proof του manuscript. Δεν έχει ακόμη εγκριθεί νέο δημόσιο CSV μετρικών αναφοράς. Η απόσυρση δεν αποτελεί εύρημα επιστημονικού σφάλματος στο CSV ή στα αποτελέσματα του manuscript· οι προηγούμενες δημόσιες εκδόσεις του αρχείου παραμένουν στο ιστορικό Git.

Ο ρόλος του αρχείου στο υπάρχον πρωτόκολλο αξιολόγησης παραμένει:

- **final test-set benchmark table**
- με τις ονομασίες μετρικών:
  - **MAE**
  - **RMSE**
  - **R²**
- και με κύριο κριτήριο κατάταξης το **MAE (ascending)**.

Τα `NB10`–`NB14` μπορούν να χρησιμοποιούν τα αρχεία αναφοράς των splits, των graphs ή του benchmark, αλλά **δεν** μετατρέπουν το `data/processed/baseline_metrics.csv` σε πίνακα αξιολόγησης graph μοντέλων.

Το scope του benchmark artifact περιορίζεται σε cross-model **test-set baseline reporting** και όχι σε graph packaging, graph verification, graph baseline, graph ablation ή controlled graph-refinement exports. Η προσωρινή απόσυρση δεν αλλάζει το evaluation protocol και δεν προάγει supplementary four-park neural / sequence outputs σε replacement public benchmark.

## Role of diagnostics

Η αξιολόγηση των baselines συνεχίζεται πέρα από τις συγκεντρωτικές μετρικές.

Τα αποτελέσματα του benchmark υποστηρίζουν:

- residual distribution analysis,
- actual-vs-predicted comparison,
- operating-regime-aware error inspection,
- structured comparison μεταξύ implemented baselines,
- park-level diagnostic aggregation,
- και condition-awareness-oriented interpretation.

## Current downstream and graph-extension path

Μετά την αξιολόγηση των πέντε baselines, η ανάλυση residuals και οι graph επεκτάσεις υλοποιούνται σε επτά διακριτά notebooks:

- `NB08` -> downstream residual diagnostics and operating regimes
- `NB09` -> park-level diagnostics and thesis consolidation
- `NB10` -> graph data-interface / split-to-graph contract / artifact verification
- `NB11` -> graph-model input packaging / data object preparation
- `NB12` -> first graph-based forecasting baseline
- `NB13` -> graph ablation / spatial sensitivity analysis
- `NB14` -> controlled graph refinement follow-up

Η υλοποιημένη ροή ανάλυσης και graph επεκτάσεων είναι:

> benchmarked forecasting -> downstream residual diagnostics -> park-level consolidation -> graph contract verification -> graph-model input packaging -> first graph-based forecasting baseline -> topology-aware graph ablation -> controlled graph refinement follow-up

και όχι:

> baseline ladder -> άμεσο speculative future graph stage

## Benchmark-safe model-selection and reporting rule

Όπου εκπαιδεύεται μοντέλο στο repository, ισχύει ο εξής κανόνας:

- **validation only for model selection**
- **test only for final reporting**

Αυτό ισχύει:
- για την tabular baseline ladder,
- για το `NB12`,
- για το `NB13` follow-up comparison framework,
- και για το `NB14` controlled graph refinement follow-up framework.

## Graph interpretation boundary

Το `NB12` αποτελεί το πρώτο actual graph-based forecasting baseline του repository.

Το `NB13` αποτελεί strict follow-up sensitivity / ablation stage πάνω σε frozen `NB12`-compatible training configuration.

Το `NB14` εξετάζει ελεγχόμενες βελτιώσεις του graph μετά το `NB13`, με αυστηρά περιορισμένο πεδίο σύγκρισης και σύμφωνα με το πρωτόκολλο αξιολόγησης.

Όμως:

- το `NB12` δεν τεκμηριώνει graph superiority έναντι του canonical benchmark backbone,
- το `NB13` δείχνει topology sensitivity αλλά μικρό spatial gain,
- και το `NB14` πρέπει να διαβάζεται ως controlled graph refinement evidence-consolidation stage και όχι ως graph superiority validation stage.

Άρα τα current graph stages πρέπει να αντιμετωπίζονται ως:

- implemented graph-based forecasting evidence,
- cautious topology-aware follow-up evidence,
- controlled graph refinement follow-up evidence,
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
- το `NB13` παραμένει **graph ablation / spatial sensitivity follow-up**,
- και το `NB14` παραμένει **controlled graph refinement follow-up stage**,

χωρίς να μετατρέπεται το repository σε:
- validated PHM system,
- validated anomaly detector,
- ολοκληρωμένο graph-learning benchmark,
- ή validated GNN / Graph-Mamba superiority claim.

## Current status

Η αξιολόγηση των baseline μοντέλων έχει ολοκληρωθεί και αποτελεί το σημείο αναφοράς για:

- `NB06` baseline modeling
- `NB07` advanced tabular baselines
- `NB08` downstream residual diagnostics
- `NB09` park-level diagnostics and thesis consolidation
- `NB10` graph data-interface / split-to-graph contract / artifact verification
- `NB11` graph-model input packaging / data object preparation
- `NB12` first graph-based forecasting baseline
- `NB13` graph ablation / spatial sensitivity analysis
- `NB14` controlled graph refinement follow-up

## Planned next vs future modeling step

Το planned next βήμα δεν είναι πλέον ούτε packaging issue, ούτε το πρώτο graph-based forecasting stage, ούτε controlled graph refinement issue, επειδή αυτά έχουν ήδη υλοποιηθεί στα `NB11`, `NB12` και `NB14`.

Το planned next είναι:

- documentation-consistent consolidation του post-`NB14` benchmark interpretation boundary
- και στη συνέχεια broader graph refinement ή επόμενο graph-related step μόνο αν αυτό δικαιολογείται από νέα benchmark evidence και χωρίς premature superiority claims

Έχουν ήδη ολοκληρωθεί ελεγχόμενα πειράματα σε τέσσερα πάρκα: GRU (`NB15`), LSTM (`NB16`), TCN (`NB18`) και PatchTST-Lite με Flattened-window XGBoost (`NB19`). Πρόκειται για συμπληρωματικά πειράματα υποσυνόλου, όχι για full-dataset sequence benchmarks. Το `NB17` περιέχει Mamba scaffold χωρίς επαληθευμένο ολοκληρωμένο πειραματικό αποτέλεσμα.

Τα παρακάτω παραμένουν future work:

- broader graph redesign,
- stronger graph-based forecasting claims μόνο αν υποστηριχθούν από νέα evidence,
- πιθανή αξιολόγηση sequence-based μοντέλων στο πλήρες dataset, πέρα από τα ελεγχόμενα πειράματα τεσσάρων πάρκων,
- περαιτέρω GNN πειράματα πέρα από τις υλοποιημένες graph-based αξιολογήσεις, καθώς και πειραματική αξιολόγηση των μη επαληθευμένων Mamba / Graph-Mamba επεκτάσεων,
- stronger digital-twin integration,
- deployed PHM / digital twin implementation,
- broader PHM-oriented modeling.

## Final principle

Η baseline ladder πρέπει να αντιμετωπίζεται ως:

> the canonical benchmark backbone of the repository

και όχι ως:

> a stage that can be bypassed or relativized by speculative graph complexity claims χωρίς benchmark-safe evidence.