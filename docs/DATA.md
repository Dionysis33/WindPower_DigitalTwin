# Data

## Dataset source

Το project βασίζεται στο **DaKS / Kassel synthetic wind power dataset**, το οποίο διατίθεται από το Universität Kassel.

Dataset source:
- DaKS dataset portal: https://daks.uni-kassel.de/entities/dataset/57ea0681-d8b2-4e76-b31d-578178961f87

## Important usage note

Τα αρχικά raw δεδομένα **δεν διανέμονται μέσα σε αυτό το repository**.  
Ο χρήστης είναι υπεύθυνος να αποκτήσει πρόσβαση στο dataset από την επίσημη πηγή και να συμμορφώνεται με τους όρους χρήσης, την άδεια και τις ερευνητικές / ακαδημαϊκές προϋποθέσεις που συνοδεύουν το dataset.

Το repository περιλαμβάνει κυρίως:

- τον κώδικα επεξεργασίας,
- τη μεθοδολογία,
- τα notebooks,
- την τεκμηρίωση,
- και επιλεγμένα αρχεία που υποστηρίζουν την αναπαραγωγιμότητα και την τεκμηριωμένη αξιολόγηση.

## Role of the data pipeline

Η pipeline μετασχηματίζει τα raw δεδομένα σε **σύνολα κατάλληλα για forecasting**, με έμφαση σε:

- temporal consistency,
- validated-only downstream processing,
- feature engineering,
- reproducible train / validation / test splitting,
- leakage-aware preprocessing,
- benchmark-ready tabular inputs,
- downstream diagnostics support,
- και graph-ready preparation για επόμενα forecasting stages.

Το project παραμένει **forecasting-first**.  
Τα diagnostics, τα graph-ready exports και τα αρχεία ανάλυσης υποστηρίζουν την forecasting pipeline· από μόνα τους δεν καθορίζουν νέο benchmark αναφοράς.

## Current repository data structure

Τα δεδομένα οργανώνονται ως εξής:

- `data/raw/`  
  Για raw ή αρχικά δεδομένα εισόδου που χρησιμοποιούνται τοπικά.

- `data/interim/`  
  Για ενδιάμεσα αποτελέσματα επεξεργασίας, checks ή transitional exports.

- `data/processed/`  
  Για reproducible processed outputs της pipeline.

Επιπλέον, η ευρύτερη artifact policy του repository συνδέεται και με:

- `models/`  
  Για model-related artifacts.

- `reports/figures/`  
  Για report-facing ή thesis-facing figures.

Η βασική δομή του repository παραμένει σχετικά απλή. Η λεπτομερέστερη οργάνωση που περιγράφεται παρακάτω αποτυπώνεται ήδη στους φακέλους και τα placeholders του repository.

Οι φάκελοι ορίζουν σαφείς προορισμούς εξαγωγής σύμφωνα με την πολιτική αποθήκευσης· τα αποτελέσματα επανεκτέλεσης δεν προστίθενται αυτόματα στο Git.

## Artifact storage policy

Η παρακάτω πολιτική διαχωρίζει τα αρχεία που δημοσιεύονται από εκείνα που διατηρούνται τοπικά, ώστε να υποστηρίζονται η αναπαραγωγιμότητα και η τεκμηρίωση της εργασίας.

### 1. Τοπικό benchmark artifact υπό συμφιλίωση

Το αρχείο του full-dataset tabular benchmark που περιλαμβανόταν στην προηγούμενη δημόσια έκδοση είναι το:

- `data/processed/baseline_metrics.csv`

Το CSV δεν διανέμεται σε αυτή την έκδοση του repository. Το αρχικό ερευνητικό αρχείο διατηρείται τοπικά, ενώ ελέγχονται η προέλευση των πειραματικών αποτελεσμάτων και η αριθμητική συμφωνία με το Author’s Proof του manuscript. Δεν έχει ακόμη εγκριθεί νέο δημόσιο CSV μετρικών αναφοράς. Η απόσυρση δεν αποτελεί εύρημα επιστημονικού σφάλματος στο CSV ή στα αποτελέσματα του manuscript· οι προηγούμενες δημόσιες εκδόσεις του αρχείου παραμένουν στο ιστορικό Git.

Το full-dataset benchmark παραμένει διακριτό από predictions, diagnostics bundles, model binaries, notebook-local exports και supplementary four-park neural / sequence evidence.

### 2. Tracked thesis / report-facing artifacts

Στο δημόσιο repository περιλαμβάνονται μικρά, επιλεγμένα και σταθερά αρχεία για την εργασία ή τις αναφορές, επειδή:

- υποστηρίζουν το thesis narrative,
- είναι κατάλληλα για figures ή documentation,
- και δεν αποτελούν βαριά rerun-dependent dump outputs.

Τα αρχεία αυτά τοποθετούνται κατά κανόνα στο `reports/figures/` και, όπου χρειάζεται, οργανώνονται σε υποφακέλους ανάλογα με τη χρήση τους στην εργασία.

Το `reports/figures/` **δεν** πρέπει να λειτουργεί ως γενικός φάκελος dump όλων των notebook plots.  
Πρέπει να περιέχει μόνο διαγράμματα που έχουν επιλεγεί ρητά για δημοσίευση.

### 3. Local rerun / diagnostics artifacts

Local rerun / diagnostics artifacts είναι outputs που:

- παράγονται reproducibly από τα notebooks,
- είναι χρήσιμα για inspection, diagnostics και downstream analysis,
- αλλά δεν αποτελούν το δημόσιο benchmark αναφοράς,
- και δεν χρειάζεται να καταγράφονται όλα στο Git.

Τέτοια artifacts περιλαμβάνουν ενδεικτικά:

- `master_dataset.csv`
- `final_feature_engineered_dataset.csv`
- `train_final.csv`
- `val_final.csv`
- `test_final.csv`
- `nb06_test_predictions.csv`
- `predictions/nb07_all_test_predictions_long.csv`
- `diagnostics/nb08_wind_regime_metrics.csv`
- `diagnostics/nb08_power_regime_metrics.csv`
- `diagnostics/nb08_time_block_metrics.csv`
- `diagnostics/nb09_park_level/`
- graph-ready exports,
- graph contract verification outputs,
- graph packaging outputs,
- graph experiment exports,
- και άλλα notebook-native rerun bundles.

Αυτά τα outputs πρέπει να αντιμετωπίζονται ως **reproducible local artifacts by default**, εκτός αν κάποιο συγκεκριμένο artifact προαχθεί ρητά σε canonical ή thesis-facing θέση.

### 4. Local-only model artifacts

Τα model binaries, checkpoints και training-state files πρέπει να παραμένουν local-only by default.

Αυτά ανήκουν εννοιολογικά στο model-artifact space του repository και μπορούν να τοποθετούνται κάτω από local-only substructure όπως:

- `models/local/`

Μπορεί να περιλαμβάνουν:

- `.joblib`
- `.pkl`
- `.pt`
- `.pth`
- `.ckpt`
- training history files
- model-specific manifests για local inspection

Τα αρχεία αυτά **δεν** αποτελούν benchmark αναφοράς και διατηρούνται χωριστά από τα αποτελέσματα που χρησιμοποιούνται σε αναφορές.

## Materialized artifact organization for this cleanup pass

Η ακόλουθη δομή αποτυπώνει τους **υπάρχοντες φακέλους αποθήκευσης** για αρχεία της έρευνας και της τεκμηρίωσης.

Η δομή ορίζει τους προορισμούς εξαγωγής σύμφωνα με την πολιτική αποθήκευσης. Η δημιουργία φακέλου δεν συνεπάγεται προσθήκη των αποτελεσμάτων του στο Git.

### `data/processed/`

Το `data/processed/` παραμένει ο κύριος χώρος για reproducible processed outputs της pipeline.

Προορισμοί αρχείων:

- `data/processed/baseline_metrics.csv`  
  Τοπικά διατηρούμενο αρχείο του full-dataset benchmark· δεν διανέμεται σε αυτή την έκδοση του repository ενόσω εκκρεμεί η συμφιλίωση με το manuscript.

- `data/processed/predictions/`  
  Intended destination για local rerun prediction exports.

- `data/processed/diagnostics/`  
  Intended destination για local rerun diagnostics bundles και case-study exports.

- `data/processed/graph/`  
  Intended destination για graph-ready, graph-verification, graph-packaging και graph-experiment local outputs.

Root-level processed CSVs όπως:

- `master_dataset.csv`
- `final_feature_engineered_dataset.csv`
- `train_final.csv`
- `val_final.csv`
- `test_final.csv`

μπορούν να συνεχίσουν να υπάρχουν ως canonical pipeline output names, αλλά πρέπει να αντιμετωπίζονται ως **local rerun artifacts by default** και όχι ως public tracked benchmark authority.

### `reports/figures/`

Το `reports/figures/` περιέχει επιλεγμένα διαγράμματα για την εργασία και τις αναφορές.

Materialized thesis-facing subfolders:

- `reports/figures/benchmark/`
- `reports/figures/diagnostics/`
- `reports/figures/park_level/`
- `reports/figures/graph/`

Εκεί πρέπει να πηγαίνουν μόνο figures που είναι:

- σταθερές,
- ερμηνεύσιμες,
- χρήσιμες για thesis ή docs,
- και intentionally selected.

Το `reports/figures/` δεν πρέπει να χρησιμοποιείται ως automatic notebook dump directory.

### `models/`

Το `models/` πρέπει να φιλοξενεί μόνο machine artifacts και όχι reporting artifacts.

Materialized local-only subfolder:

- `models/local/`

Εκεί ανήκουν checkpoints, serialized estimators, graph model weights και related local manifests.  
Δεν πρέπει να αποθηκεύονται εκεί benchmark tables, diagnostics CSVs ή thesis figures.

## Current processed outputs and their interpretation

Στην pipeline διακρίνονται οι παρακάτω κατηγορίες αρχείων.

### Τοπικά διατηρούμενο benchmark artifact

- `data/processed/baseline_metrics.csv`

Το αρχείο δεν διανέμεται σε αυτή την έκδοση του repository. Δεν έχει ακόμη εγκριθεί νέο δημόσιο CSV μετρικών αναφοράς.

### Canonical local rerun processed outputs

- `master_dataset.csv`
- `final_feature_engineered_dataset.csv`
- `train_final.csv`
- `val_final.csv`
- `test_final.csv`

### Local prediction exports

- `nb06_test_predictions.csv`
- `predictions/nb07_all_test_predictions_long.csv`

### Local diagnostics exports

- `diagnostics/nb08_wind_regime_metrics.csv`
- `diagnostics/nb08_power_regime_metrics.csv`
- `diagnostics/nb08_time_block_metrics.csv`
- `diagnostics/nb09_park_level/`

Το `diagnostics/nb09_park_level/` μπορεί να περιλαμβάνει:

- park-level summaries,
- selected-park matrices,
- spatial context outputs,
- case-study metadata,
- notebook-local figures,
- και άλλα thesis-supporting diagnostic outputs.

Ο φάκελος διατηρείται κατά κανόνα ως **τοπικό σύνολο αποτελεσμάτων επανεκτέλεσης και diagnostics**, χωρίς να απαιτείται η δημόσια καταγραφή όλου του περιεχομένου του στο Git.

### Local graph-related exports

Graph-related local exports μπορεί να περιλαμβάνουν:

- graph-ready artifacts,
- graph contract verification outputs,
- graph packaging outputs,
- graph baseline outputs,
- graph ablation outputs,
- controlled graph refinement outputs,
- serialized graph datasets,
- graph-model prediction dumps,
- και graph-specific run manifests.

Αυτά πρέπει να αντιμετωπίζονται ως **local rerun artifacts by default**, εκτός αν κάποιο μικρό, επιλεγμένο artifact προαχθεί ρητά σε thesis-facing ή documentation-facing θέση.

## What should remain tracked vs local-only

### Should remain tracked

Κατά κανόνα καταγράφονται στο Git μόνο:

- selected thesis-facing figures στο `reports/figures/`
- μικρά manifests ή policy-facing text files όταν χρειάζονται για reproducibility
- `.gitkeep` placeholders που κάνουν τα intended export destinations repository-visible

### Should remain local-only by default

Το `data/processed/baseline_metrics.csv`, που περιλαμβανόταν σε προηγούμενες δημόσιες εκδόσεις, διατηρείται τοπικά όσο εκκρεμεί ο έλεγχος προέλευσης και αριθμητικής συμφωνίας με το manuscript. Δεν διανέμεται σε αυτή την έκδοση του repository.

Κατά κανόνα πρέπει να μένουν local-only:

- raw dataset files,
- μεγάλα processed datasets,
- train / validation / test rerun CSVs,
- full prediction dumps,
- diagnostics bundles,
- graph intermediate exports,
- graph packaging artifacts,
- graph model outputs,
- notebook-native figure dumps,
- model binaries / checkpoints / weights.

## Target variable

Η βασική μεταβλητή πρόβλεψης είναι η:

- `Power_Output_Normalized`

Η επιλογή normalized target βοηθά σε:

- σταθερότερη εκπαίδευση μοντέλων,
- δικαιότερη σύγκριση baselines,
- πιο καθαρή ερμηνεία residuals και error metrics.

## Indicative feature groups

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

- **Temporal train/validation/test partition isolation**
- **Train-first statistics**
- **Consistent feature space across splits**
- **Reproducible preprocessing**
- **Explicit export of final artifacts**
- **Benchmark-safe reporting**

Ιδιαίτερα σημαντικό είναι ότι ο καθαρισμός outliers και τα thresholds για clipping υπολογίζονται με στατιστικά που προέρχονται από το **train split**, ώστε να αποφεύγεται leakage προς validation / test.

Οι παράμετροι preprocessing που εξαρτώνται από τα δεδομένα υπολογίζονται από το training partition όπου αυτό υλοποιείται. Η επιλογή μοντέλων και hyperparameters χρησιμοποιεί το validation, ενώ η βαθμονόμηση residual-warning thresholds βασίζεται σε validation residuals. Το test partition προορίζεται για την τελική αξιολόγηση, αφού οριστικοποιηθούν οι επιλογές. Η ευθυγράμμιση ως προς το target valid time δεν τεκμηριώνει από μόνη της τη διαθεσιμότητα κάθε feature στο issue time ούτε αυστηρό operational day-ahead forecasting setup. Η διευκρίνιση αφορά το εύρος της επαλήθευσης και δεν αποτελεί εύρημα leakage.

## Naming guidance for exported artifacts

Για να είναι σαφής η προέλευσή τους, τα exports που δεν αποτελούν αρχεία αναφοράς πρέπει να ακολουθούν σταθερούς κανόνες ονοματοδοσίας.

### Figures

Προτιμάται μορφή όπως:

- `nb07_benchmark_test_metrics_comparison.png`
- `nb08_diagnostics_residual_distribution_test.png`
- `nb09_park_level_selected_case_study_01_park_00011.png`

### CSV exports

Προτιμάται μορφή όπως:

- `nb06_test_predictions.csv`
- `nb07_all_test_predictions_long.csv`
- `nb08_wind_regime_metrics.csv`
- `nb09_park_model_metrics.csv`

### Model files

Προτιμάται μορφή όπως:

- `nb07_random_forest_best.joblib`
- `nb07_xgboost_best.joblib`
- `nb12_gcn_reference_best.pt`

Τα canonical filenames όπως:

- `baseline_metrics.csv`
- `train_final.csv`
- `val_final.csv`
- `test_final.csv`

μπορούν να παραμείνουν ως έχουν.

## Guidance for notebook exports

Η default συμπεριφορά των notebooks πρέπει να είναι η εξής:

- να γράφουν rerun datasets, predictions και diagnostics outputs στο `data/processed/...`
- να κρατούν notebook-local figures στο local diagnostic / export context
- να προάγουν μόνο επιλεγμένες figures στο `reports/figures/...`
- και να κρατούν model binaries / checkpoints κάτω από `models/local/` όταν χρειάζονται για local inspection

Με άλλα λόγια:

- **default = local rerun export**
- **selected only = thesis/report-facing promotion**
- **model binaries = local-only model artifact space**

Αυτό βοηθά να μη μετατραπεί το repository σε dump όλων των notebook outputs.

## What a new user should keep in mind

Αν θέλεις να τρέξεις το project από την αρχή:

1. Απόκτησε το dataset από την επίσημη πηγή.
2. Τοποθέτησε τα αρχεία στα κατάλληλα data paths.
3. Έλεγξε το configuration στο `src/config.py`.
4. Τρέξε τα notebooks με τη σωστή σειρά.
5. Επιβεβαίωσε ότι δημιουργούνται ξανά τα canonical processed outputs.
6. Το `data/processed/baseline_metrics.csv` μπορεί να παραχθεί τοπικά από τα `NB06` / `NB07`, αλλά δεν διανέμεται σε αυτή την έκδοση του repository. Τα επόμενα στάδια που το απαιτούν χρειάζονται τοπικό αρχείο· η αναπαραγωγή του δεν αποτελεί έγκριση δημοσίευσης ως benchmark αναφοράς όσο εκκρεμεί η συμφιλίωση.
7. Αν χρειάζεσαι thesis-facing figures, επίλεξε και προώθησε μόνο τις κατάλληλες figures στο `reports/figures/`.

## Data governance / reproducibility note

Το repository δίνει μεγαλύτερη έμφαση στη **μεθοδολογική αναπαραγωγιμότητα (reproducibility)** παρά στη μαζική διανομή έτοιμων outputs.

Ο στόχος είναι να μπορεί οποιοσδήποτε ερευνητής με νόμιμη πρόσβαση στο dataset να:

- αναπαράγει τα βήματα της pipeline,
- επιβεβαιώσει τα benchmark outputs,
- ελέγξει τα diagnostics artifacts όπου χρειάζεται,
- και διατηρήσει καθαρό διαχωρισμό ανάμεσα σε:
  - αρχεία του benchmark αναφοράς,
  - thesis-facing selected artifacts,
  - local rerun outputs,
  - local graph / diagnostics exports,
  - και local-only model artifacts.

## Scope boundary for this artifact-organization pass

Η οργάνωση των αρχείων αφορά τη δομή του repository και την πολιτική τεκμηρίωσης.

Δεν εισάγει:

- notebook rerun,
- νέο benchmark,
- νέο model training,
- αλλαγή στο canonical benchmark protocol,
- αλλαγή στο `data/processed/baseline_metrics.csv`,
- νέο diagnostics claim,
- νέο graph superiority claim,
- ή νέο PHM / digital twin claim.

Η αλλαγή διευκρινίζει τους φακέλους αποθήκευσης και τη χρήση των αρχείων στην εργασία, διατηρώντας την επιστημονική ερμηνεία των υπαρχόντων αποτελεσμάτων.