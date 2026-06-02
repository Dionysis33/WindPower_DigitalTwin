# Παρακολούθηση προόδου manuscript upgrade

Σκοπός: πρακτική παρακολούθηση του manuscript-upgrade work κατά τη διάρκεια του τρέχοντος experiment branch, με έμφαση σε τεκμηριωμένα αποτελέσματα και καθαρή διαχείριση artifacts.

## Current repository safety state

- Branch: τρέχον manuscript-upgrade experiment branch.
- Το working tree ήταν clean κατά τον έλεγχο.
- Δεν βρέθηκαν tracked `__pycache__` ή `.pyc` files.
- Τα `data/raw`, `data/interim` και `models/local` περιέχουν μόνο `.gitkeep`.
- Το `data/processed/baseline_metrics.csv` είναι tracked.
- Τα μεγάλα tracked files πάνω από 1 MB είναι τα notebooks `06`, `08` και `09`.
- Ο repository provenance / metadata string check δεν έδειξε εμφανή προβληματικά matches.
- Κατά τον έλεγχο δεν έγινε staging, commit, push ή sync.

## Completed work

- Ολοκληρώθηκε repository safety inspection.
- Επιβεβαιώθηκε το experiment branch.
- Ελέγχθηκαν generated/cache files και local artifact paths.
- Ολοκληρώθηκε repository provenance / metadata string check.
- Ολοκληρώθηκε preprocessing correlation audit για leakage-aware feature-correlation review.

## In progress

- Οργάνωση evidence για το manuscript upgrade.
- Διαχωρισμός claims που μπορούν να τεκμηριωθούν από claims που χρειάζονται επιπλέον artifacts.
- Καταγραφή εργασιών που πρέπει να ολοκληρωθούν πριν το τελικό manuscript consolidation.

## Pending experiments

- Επιβεβαίωση των τελικών baseline metrics από committed ή reproducible artifacts.
- Έλεγχος graph-readiness και graph-model inputs πριν από οποιοδήποτε manuscript claim.
- Επανέλεγχος residual diagnostics και PHM-relevant ευρημάτων για tables/figures.
- Απόφαση για το ποια processed outputs πρέπει να μείνουν tracked και ποια να αναπαράγονται.

## Evidence table

| Τεκμήριο | Τρέχουσα πηγή | Κατάσταση | Χρήση στο manuscript |
| --- | --- | --- | --- |
| Baseline metrics | `data/processed/baseline_metrics.csv` | Tracked | Υποψήφια ποσοτική τεκμηρίωση |
| Baseline modeling notebook | `notebooks/06_baseline_modeling.ipynb` | Tracked, large | Να χρησιμοποιηθεί μόνο μετά από verification των outputs |
| Residual diagnostics notebook | `notebooks/08_residual_diagnostics_and_operating_regimes.ipynb` | Tracked, large | Υποψήφια diagnostic τεκμηρίωση |
| Park-level diagnostics notebook | `notebooks/09_park_level_diagnostics_and_thesis_consolidation.ipynb` | Tracked, large | Υποψήφια τεκμηρίωση για consolidation |
| Preprocessing correlation audit | `docs/PREPROCESSING_AUDIT.md`; `scripts/audit_preprocessing_correlations.py`; `reports/figures/diagnostics/preprocessing_target_correlation_top20.png` | Reproducible audit artifact | Supports leakage-aware preprocessing checks and feature-correlation review |
| Raw/interim/local model data | `.gitkeep` placeholders only | Clean | Δεν αποτελεί committed evidence |

## Claims allowed in manuscript

- Το manuscript work γίνεται στο branch `manuscript-upgrade experiment branch`.
- Το working tree ήταν clean κατά τον repository safety inspection.
- Δεν βρέθηκαν tracked Python cache artifacts.
- Τα raw data, interim data και local model directories είναι placeholder-only στο git.
- Το `baseline_metrics.csv` είναι tracked και μπορεί να εξεταστεί ως πηγή evidence.
- Κανένα νέο αποτέλεσμα δεν πρέπει να δηλωθεί στο manuscript αν δεν υποστηρίζεται από committed ή reproducible artifacts.

## Claims not yet supported

- Βελτιώσεις τελικής απόδοσης πέρα από verified baseline metrics.
- Claims που βασίζονται σε uncommitted local data, raw files, interim artifacts ή local model outputs.
- Claims που εξαρτώνται από notebook outputs χωρίς επανέλεγχο των σχετικών results.
- Claims αναπαραγωγιμότητας πριν επιβεβαιωθούν scripts, data assumptions και outputs.

## Άμεσο πλάνο εργασίας

### 1. Preprocessing checks

- Στόχος: Να επιβεβαιωθεί ότι τα preprocessing assumptions, splits και feature inputs είναι σαφή και αναπαράξιμα.
- Output: Σύντομο checklist ή σημείωση με verified inputs, assumptions και τυχόν gaps.
- Προτεραιότητα: Υψηλή.
- Μπορεί να μείνει εκτός αν δεν προλάβω: Εκτεταμένη ανάλυση εναλλακτικών preprocessing variants.

### 2. Baseline tuning

- Στόχος: Να ελεγχθεί αν τα baseline settings είναι επαρκώς τεκμηριωμένα και αν χρειάζεται μικρό tuning πριν το manuscript.
- Output: Verified baseline metrics και σαφής αναφορά στο artifact που τα υποστηρίζει.
- Προτεραιότητα: Υψηλή.
- Μπορεί να μείνει εκτός αν δεν προλάβω: Μεγάλο hyperparameter sweep χωρίς άμεση manuscript αξία.

### 3. Neural-network experiments

- Στόχος: Να αξιολογηθούν μόνο όσα neural-network experiments μπορούν να τεκμηριωθούν καθαρά και να αναπαραχθούν.
- Output: Minimal results table ή decision note για inclusion/exclusion.
- Προτεραιότητα: Μεσαία.
- Μπορεί να μείνει εκτός αν δεν προλάβω: Νέα architectures χωρίς σταθερό evaluation path.

### 4. Graph-model audit

- Στόχος: Να ελεγχθεί η ετοιμότητα των graph inputs, adjacency assumptions και graph baseline claims.
- Output: Audit note με verified graph artifacts, missing pieces και safe wording για το manuscript.
- Προτεραιότητα: Υψηλή.
- Μπορεί να μείνει εκτός αν δεν προλάβω: Πλήρης επέκταση graph experiments πέρα από το ήδη τεκμηριωμένο scope.

### 5. Residual / PHM diagnostics

- Στόχος: Να εντοπιστούν diagnostic findings που μπορούν να στηρίξουν προσεκτικά PHM-oriented discussion.
- Output: Verified residual/operating-regime evidence και λίστα επιτρεπτών manuscript claims.
- Προτεραιότητα: Μεσαία προς υψηλή.
- Μπορεί να μείνει εκτός αν δεν προλάβω: Πρόσθετα exploratory plots χωρίς καθαρή σύνδεση με claims.

### 6. Manuscript updates

- Στόχος: Να περαστούν στο manuscript μόνο claims που έχουν καθαρή πηγή evidence.
- Output: Updated manuscript sections ή change notes με links σε committed/reproducible artifacts.
- Προτεραιότητα: Υψηλή.
- Μπορεί να μείνει εκτός αν δεν προλάβω: Style polishing που δεν επηρεάζει τεχνική ακρίβεια.

## Files/artifacts to avoid committing

- `__pycache__/` directories και `*.pyc` files.
- Raw datasets κάτω από `data/raw/`.
- Interim working data κάτω από `data/interim/`.
- Local model checkpoints ή binaries κάτω από `models/local/`.
- Μεγάλα generated figures, predictions, diagnostics ή model outputs χωρίς ρητή αξιολόγηση.
- Environment-specific files, local credentials, logs και temporary exports.
