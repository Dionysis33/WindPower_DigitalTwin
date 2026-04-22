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
- τη documentation,
- και επιλεγμένα artifacts που υποστηρίζουν reproducibility και benchmark-safe reporting.

## Role of the data pipeline

Η data pipeline έχει σχεδιαστεί ώστε να μετασχηματίζει τα raw δεδομένα σε **forecasting-ready** σύνολα, με έμφαση σε:

- temporal consistency,
- validated-only downstream processing,
- feature engineering,
- reproducible train / validation / test splitting,
- leakage-aware preprocessing,
- benchmark-ready tabular inputs,
- downstream diagnostics support,
- και graph-ready preparation για επόμενα forecasting stages.

Το project παραμένει **forecasting-first**.  
Τα diagnostics, τα graph-ready exports και τα downstream analysis artifacts πρέπει να διαβάζονται ως υποστηρικτικά layers του forecasting pipeline και όχι ως νέο benchmark authority από μόνα τους.

## Current repository data structure

Η current βασική λογική οργάνωσης είναι η εξής:

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

Η current public repository structure παραμένει σχετικά απλή στα top-level paths.  
Η πιο λεπτομερής artifact organization που περιγράφεται παρακάτω αποτελεί **proposed thesis-safe organization** στο πλαίσιο του current cleanup / organization pass και όχι πλήρως εγκατεστημένη current structure σε κάθε subfolder.

## Artifact storage policy

Για να παραμένει το repository καθαρό, reproducible και thesis-safe, χρησιμοποιείται ο παρακάτω διαχωρισμός.

### 1. Canonical tracked benchmark artifact

Canonical tracked benchmark artifact είναι ένα μικρό, stable, public-facing artifact που λειτουργεί ως authority για benchmark reporting.

Στο current repository state, αυτό είναι το:

- `data/processed/baseline_metrics.csv`

Το συγκεκριμένο αρχείο είναι η canonical authority για final test-set benchmark reporting της implemented baseline ladder.  
Δεν πρέπει να συγχέεται με predictions, diagnostics bundles, model binaries ή notebook-local exports.

### 2. Tracked thesis / report-facing artifacts

Tracked thesis-facing ή report-facing artifacts είναι μικρά, επιλεγμένα, σταθερά outputs που αξίζει να εμφανίζονται στο public repository επειδή:

- υποστηρίζουν το thesis narrative,
- είναι κατάλληλα για figures ή documentation,
- και δεν αποτελούν βαριά rerun-dependent dump outputs.

Αυτά πρέπει να τοποθετούνται κατά κανόνα στο `reports/figures/` και, όπου χρειάζεται πιο καθαρή οργάνωση, μπορούν να promoted σε επιλεγμένα subfolders με thesis-facing λογική.

Το `reports/figures/` **δεν** πρέπει να λειτουργεί ως γενικός φάκελος dump όλων των notebook plots.  
Πρέπει να περιέχει μόνο selected, intentionally promoted figures.

### 3. Local rerun / diagnostics artifacts

Local rerun / diagnostics artifacts είναι outputs που:

- παράγονται reproducibly από τα notebooks,
- είναι χρήσιμα για inspection, diagnostics και downstream analysis,
- αλλά δεν αποτελούν public benchmark authority,
- και δεν χρειάζεται να tracked όλα στο repository.

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
- και άλλα notebook-native rerun bundles.

Αυτά τα outputs πρέπει να αντιμετωπίζονται ως **reproducible local artifacts by default**, εκτός αν κάποιο συγκεκριμένο artifact προαχθεί ρητά σε canonical ή thesis-facing θέση.

### 4. Local-only model artifacts

Τα model binaries, checkpoints και training-state files πρέπει να παραμένουν local-only by default.

Αυτά ανήκουν εννοιολογικά στο model-artifact space του repository και σε πιο καθαρή organization μπορούν να τοποθετούνται κάτω από local-only substructure όπως:

- `models/local/`

Μπορεί να περιλαμβάνουν:

- `.joblib`
- `.pkl`
- `.pt`
- `.pth`
- training history files
- model-specific manifests για local inspection

Τα artifacts αυτά **δεν** αποτελούν benchmark authority και **δεν** πρέπει να συγχέονται με report-facing outputs.

## Proposed artifact organization for this cleanup pass

Η ακόλουθη δομή είναι η **proposed thesis-safe organization** των artifacts στο πλαίσιο του current cleanup pass.

### `data/processed/`

Το `data/processed/` παραμένει ο κύριος χώρος για reproducible processed outputs της pipeline.

Προτεινόμενη λογική:

- `data/processed/baseline_metrics.csv`  
  Canonical tracked benchmark artifact

- `data/processed/predictions/`  
  Local rerun prediction exports

- `data/processed/diagnostics/`  
  Local rerun diagnostics bundles και case-study exports

- `data/processed/graph/`  
  Graph-ready, graph-verification, packaging και graph-experiment local outputs

Root-level processed CSVs όπως:

- `master_dataset.csv`
- `final_feature_engineered_dataset.csv`
- `train_final.csv`
- `val_final.csv`
- `test_final.csv`

μπορούν να συνεχίσουν να υπάρχουν ως canonical pipeline output names, αλλά πρέπει να αντιμετωπίζονται ως **local rerun artifacts by default** και όχι ως public tracked benchmark authority.

### `reports/figures/`

Το `reports/figures/` είναι ο curated χώρος για thesis-facing / report-facing figures.

Προτεινόμενη λογική subfolders:

- `reports/figures/benchmark/`
- `reports/figures/diagnostics/`
- `reports/figures/park_level/`
- `reports/figures/graph/`

Εκεί πρέπει να πηγαίνουν μόνο figures που είναι:

- σταθερές,
- ερμηνεύσιμες,
- χρήσιμες για thesis ή docs,
- και intentionally selected.

### `models/`

Το `models/` πρέπει να φιλοξενεί μόνο machine artifacts και όχι reporting artifacts.

Προτεινόμενη λογική subfolder:

- `models/local/`

Εκεί ανήκουν checkpoints, serialized estimators, graph model weights και related local manifests.  
Δεν πρέπει να αποθηκεύονται εκεί benchmark tables, diagnostics CSVs ή thesis figures.

## Current processed outputs and their interpretation

Στο current pipeline, είναι σημαντικό να ξεχωρίζονται οι παρακάτω κατηγορίες.

### Public tracked benchmark authority

- `data/processed/baseline_metrics.csv`

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

Αυτό δεν σημαίνει ότι όλο το directory πρέπει να versioned/tracked δημόσια.  
Η default αντιμετώπιση του είναι **local rerun / diagnostics bundle**.

## What should remain tracked vs local-only

### Should remain tracked

Κατά κανόνα πρέπει να tracked μόνο:

- `data/processed/baseline_metrics.csv`
- selected thesis-facing figures στο `reports/figures/`
- μικρά manifests ή policy-facing text files όταν χρειάζονται για reproducibility

### Should remain local-only by default

Κατά κανόνα πρέπει να μένουν local-only:

- μεγάλα processed datasets,
- train / validation / test rerun CSVs,
- full prediction dumps,
- diagnostics bundles,
- graph intermediate exports,
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

- **No temporal leakage**
- **Train-first statistics**
- **Consistent feature space across splits**
- **Reproducible preprocessing**
- **Explicit export of final artifacts**

Ιδιαίτερα σημαντικό είναι ότι ο καθαρισμός outliers και τα thresholds για clipping υπολογίζονται με στατιστικά που προέρχονται από το **train split**, ώστε να αποφεύγεται leakage προς validation / test.

## Naming guidance for exported artifacts

Για να διατηρείται καθαρό artifact provenance, τα non-canonical exports πρέπει να έχουν deterministic naming.

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
- να κρατούν notebook-local figures στο local diagnostic/export context
- και να προάγουν μόνο επιλεγμένες figures στο `reports/figures/...`

Με άλλα λόγια:

- **default = local rerun export**
- **selected only = thesis/report-facing promotion**

Αυτό βοηθά να μη μετατραπεί το repository σε dump όλων των notebook outputs.

## What a new user should keep in mind

Αν θέλεις να τρέξεις το project από την αρχή:

1. Απόκτησε το dataset από την επίσημη πηγή.
2. Τοποθέτησε τα αρχεία στα κατάλληλα data paths.
3. Έλεγξε το configuration στο `src/config.py`.
4. Τρέξε τα notebooks με τη σωστή σειρά.
5. Επιβεβαίωσε ότι δημιουργούνται ξανά τα canonical processed outputs.
6. Αν χρειάζεσαι thesis-facing figures, επίλεξε και προώθησε μόνο τις κατάλληλες figures στο `reports/figures/`.

## Data governance / reproducibility note

Το repository δίνει μεγαλύτερη έμφαση στη **μεθοδολογική αναπαραγωγιμότητα (reproducibility)** παρά στη μαζική διανομή έτοιμων outputs.

Ο στόχος είναι να μπορεί οποιοσδήποτε ερευνητής με νόμιμη πρόσβαση στο dataset να:

- αναπαράγει τα βήματα της pipeline,
- επιβεβαιώσει τα benchmark outputs,
- ελέγξει τα diagnostics artifacts όπου χρειάζεται,
- και διατηρήσει καθαρό διαχωρισμό ανάμεσα σε:
  - canonical benchmark authority,
  - thesis-facing selected artifacts,
  - local rerun outputs,
  - και local-only model artifacts.