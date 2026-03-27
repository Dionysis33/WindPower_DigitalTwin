# Active Project Log

Αυτό το αρχείο καταγράφει την ενεργή canonical methodological κατάσταση του τρέχοντος forecasting pipeline του repository.

Canonical progression:
`NB02 raw validation -> NB03 validated-only EDA -> NB04 feature engineering`

Τα παλαιότερα exploratory ή superseded entries έχουν μεταφερθεί στο `LOGS_ARCHIVE.md`.


---


## [24/03/2026] - Notebook 05/06 Finalization, CI Validation & Baseline Stabilization

### Τεχνικά Επιτεύγματα (Technical Milestones):

1. **Οριστικοποίηση Notebook 05 - Outlier Handling & Temporal Validation**
   * Αναθεωρήθηκε η μεθοδολογία του outlier handling ώστε τα **Z-score thresholds** να υπολογίζονται αποκλειστικά από το **Train Set** και στη συνέχεια να εφαρμόζονται στα Validation/Test splits.
   * Η αλλαγή αυτή ενίσχυσε τη μεθοδολογική αυστηρότητα του pipeline και εξάλειψε πιθανό **data leakage** από τη φάση preprocessing.
   * Επιβεβαιώθηκε η απουσία χρονικής επικάλυψης μεταξύ Train / Validation / Test μέσω validation protocol με `assert` checks.
   * Ολοκληρώθηκε η εξαγωγή των τελικών split artifacts:
     - `train_final.csv`
     - `val_final.csv`
     - `test_final.csv`

2. **Οριστικοποίηση Notebook 06 - Baseline Benchmarking & Diagnostics**
   * Πραγματοποιήθηκε πλήρης τελική εκτέλεση του Notebook 06 με:
     - **Persistence baseline**
     - **Linear Regression baseline**
     - συγκριτική αξιολόγηση σε Validation και Test set
     - residual diagnostics
     - actual-vs-predicted visualization
     - ανάλυση residuals ως προς wind-related feature
   * Το **Linear Regression** επιβεβαιώθηκε ως σαφώς ανώτερο baseline σε σχέση με το Persistence.
   * Τα τελικά metrics αποθηκεύτηκαν εκ νέου στο αρχείο:
     - `data/processed/baseline_metrics.csv`

3. **Residual Diagnostics & Error Interpretation**
   * Προστέθηκε έλεγχος διαθεσιμότητας wind-related features (`Wind_Speed_100m_ms`, `ws_ref`) πριν από την ανάλυση residuals.
   * Επιλέχθηκε δυναμικά το διαθέσιμο feature για diagnostic plotting, με ρητή σημείωση ότι η μεταβλητή ερμηνεύεται ως **scaled / engineered wind-related feature** και όχι ως ωμή φυσική μέτρηση.
   * Η ανάλυση residuals έδειξε ότι το σφάλμα του γραμμικού baseline παραμένει δομημένο, επιβεβαιώνοντας ότι το πρόβλημα πρόβλεψης περιέχει σημαντική **μη-γραμμικότητα**.

4. **Documentation & Markdown Refinement**
   * Βελτιώθηκε το explanatory markdown στα notebooks, με καθαρότερη επιστημονική τεκμηρίωση για:
     - train-based clipping,
     - leakage-safe preprocessing,
     - validation protocol,
     - baseline interpretation,
     - και diagnostic analysis.
   * Το conclusion του Notebook 06 αναδιατυπώθηκε ώστε να περιγράφει με σαφήνεια:
     - την ανωτερότητα της Linear Regression έναντι του Persistence,
     - τον ρόλο των baselines ως benchmark ladder,
     - και τη μετάβαση στο Notebook 07.

5. **CI/CD & Repository Validation**
   * Επαληθεύτηκε ότι τα πρόσφατα pushes ολοκληρώθηκαν επιτυχώς στο GitHub.
   * Τα workflows του **GitHub Actions** εκτελέστηκαν επιτυχώς (green status), επιβεβαιώνοντας ότι το repository βρίσκεται σε συγχρονισμένη και σταθερή κατάσταση.
   * Ολοκληρώθηκε ο τελικός συγχρονισμός του local environment με το απομακρυσμένο `main` branch.

### Τρέχουσα Κατάσταση Έργου:
* Το pipeline έως και το **Notebook 06** θεωρείται πλέον **σταθεροποιημένο και αναπαραγώγιμο**.
* Υπάρχει πλέον:
  - καθαρό preprocessing pipeline,
  - leakage-safe split strategy,
  - βασική baseline ladder,
  - exportable benchmark metrics,
  - και ώριμη τεκμηρίωση για τη μετάβαση στα advanced baselines.

### Επόμενα Βήματα (Next Steps):
1. **Notebook 07 - Advanced Baselines & Feature Importance**
   - Random Forest
   - XGBoost
   - MLP
2. Συγκριτική αξιολόγηση όλων των baselines σε κοινό benchmark framework.
3. Οριστικοποίηση της baseline πεντάδας πριν τη μετάβαση σε **GNN / Graph-Mamba** αρχιτεκτονικές.

**Commit References:**
- `fix: finalize train-based clipping and validation protocol in notebook 05`
- `feat: finalize notebook 06 baseline benchmarking and diagnostics`
- `chore: update baseline metrics after notebook 06 rerun`


---

## [25/03/2026] - Notebook 07 Random Forest Baseline with Train / Validation / Test Protocol

### Ολοκληρωμένες Ενέργειες:
1. Υλοποιήθηκε ο πρώτος καθαρός `Random Forest` baseline στο `07_advanced_baselines_and_importance.ipynb`.
2. Χρησιμοποιήθηκε strict `train / validation / test` protocol.
3. Πραγματοποιήθηκε explicit feature audit πριν από την εκπαίδευση.
4. Εξαιρέθηκαν από το πρώτο clean baseline τα:
   - `test_flag`
   - `park_id`
   - `Baseline_Prediction`
5. Έγινε validation-based επιλογή υπερπαραμέτρων.
6. Το τελικό test αποτέλεσμα του `Random Forest` ήταν:
   - **MAE:** 0.007260
   - **RMSE:** 0.009845
   - **R²:** 0.526639
7. Ενημερώθηκε το κοινό benchmark artifact `data/processed/baseline_metrics.csv`.

### Μεθοδολογική Σημείωση:
Η παρούσα υλοποίηση αποφεύγει τη χρήση helper / identifier columns και διατηρεί το test split αποκλειστικά για final reporting.


---


## [25/03/2026] - Notebook 07 XGBoost Baseline with Train / Validation / Test Protocol

### Ολοκληρωμένες Ενέργειες:
1. Υλοποιήθηκε `XGBoost` baseline στο `07_advanced_baselines_and_importance.ipynb`.
2. Χρησιμοποιήθηκε το ίδιο clean feature space με το `Random Forest` baseline.
3. Διατηρήθηκε strict `train / validation / test` protocol.
4. Η επιλογή υπερπαραμέτρων έγινε μόνο με χρήση του validation split.
5. Το test split χρησιμοποιήθηκε αποκλειστικά για final reporting.
6. Υπολογίστηκαν τα τελικά test metrics:
   - **MAE:** 0.006178
   - **RMSE:** 0.008952
   - **R²:** 0.608583
7. Ενημερώθηκε το κοινό benchmark artifact `data/processed/baseline_metrics.csv`.
8. Προστέθηκαν:
   - residual diagnostics,
   - XGBoost feature-importance analysis.

### Validation-best configuration:
- `n_estimators = 500`
- `max_depth = 8`
- `learning_rate = 0.05`
- `subsample = 0.8`
- `colsample_bytree = 0.8`

### Scientific Interpretation:
Το `XGBoost` αποτελεί πλέον το ισχυρότερο current tabular baseline του Notebook 07 και υπερτερεί του `Random Forest`, της `Linear Regression` και του `Persistence` στο current exported benchmark.

### Note on benchmark provenance:
Το `baseline_metrics.csv` αντιμετωπίζεται πλέον ως το current benchmark artifact αναφοράς. Αν historical τιμές σε παλαιότερα log entries διαφέρουν, αυτές πρέπει να θεωρούνται παλαιότερα notebook outputs και όχι κατ’ ανάγκη το τελικό standardized benchmark state.


---

## [25/03/2026] - Notebook 07 MLP Baseline as Bridge to Deep Learning Models

### Ολοκληρωμένες Ενέργειες:
1. Υλοποιήθηκε `MLP` baseline στο `07_advanced_baselines_and_importance.ipynb` με χρήση `PyTorch`.
2. Χρησιμοποιήθηκε το ίδιο clean feature space με τα `Random Forest` και `XGBoost` baselines.
3. Εφαρμόστηκε `StandardScaler` fitted μόνο στο `train` split και transform στα `validation` / `test` splits.
4. Πραγματοποιήθηκε explicit validation-based επιλογή βασικών hyperparameters.
5. Το test split χρησιμοποιήθηκε αποκλειστικά για final reporting.
6. Τα τελικά test metrics του `MLP` ήταν:
   - **MAE:** 0.006917
   - **RMSE:** 0.009870
   - **R²:** 0.524226
7. Ενημερώθηκε το κοινό benchmark artifact `data/processed/baseline_metrics.csv`.
8. Προστέθηκε residual diagnostic plot για το `MLP`.

### Best validation configuration:
- `hidden_dims = (128, 64)`
- `dropout = 0.0`
- `lr = 0.001`
- `weight_decay = 1e-5`

### Scientific Interpretation:
Το `MLP` λειτουργεί επιτυχώς ως bridge baseline ανάμεσα στα classical tabular ML models και στα επόμενα deep-learning-oriented στάδια. Στο current benchmark βελτιώνει το `Random Forest` ως προς το **MAE**, αλλά το `Random Forest` παραμένει οριακά καλύτερο σε **RMSE** και **R²**. Το `XGBoost` συνεχίζει να αποτελεί το ισχυρότερο current tabular baseline αναφοράς.


---

## [25/03/2026] - Unified Baseline Benchmark Table Standardization

### Ολοκληρωμένες Ενέργειες:
1. Ορίστηκε το `data/processed/baseline_metrics.csv` ως το **canonical baseline benchmark artifact** του project.
2. Ενοποιήθηκαν σε κοινό benchmark table τα αποτελέσματα των:
   - Persistence
   - Linear Regression
   - Random Forest
   - XGBoost
   - MLP
3. Καθορίστηκε ότι ο τελικός benchmark ranking πίνακας αφορά αποκλειστικά το **test split**.
4. Καθορίστηκε ότι το **primary ranking criterion** είναι το **MAE (ascending)**, ενώ τα **RMSE** και **R²** παραμένουν συμπληρωματικά metrics ερμηνείας.
5. Συγχρονίστηκαν το `README.md`, το `BASELINE_PROTOCOL.md` και το `LOGS.md` ώστε να αντανακλούν την πλήρως υλοποιημένη baseline ladder.

### Scientific Interpretation:
Η baseline πεντάδα θεωρείται πλέον ολοκληρωμένη και λειτουργεί ως κοινό σημείο αναφοράς για τα επόμενα forecasting experiments. Το `XGBoost` αποτελεί το ισχυρότερο current tabular baseline, ενώ το `MLP` και το `Random Forest` προσφέρουν ισχυρές non-linear συγκρίσεις απέναντι στα απλούστερα baselines.

### Clarification:
Historical metric values σε παλαιότερα log entries πρέπει να ερμηνεύονται ως notebook-run history. Για thesis reporting, canonical σημείο αναφοράς είναι το τρέχον `data/processed/baseline_metrics.csv`.


---

## [27/03/2026] - NB02 Raw Timestamp Validation Stabilization

### Τεχνικά Επιτεύγματα (Technical Milestones):
1. **Μεθοδολογικός καθαρισμός του `02_kassel_exploration.ipynb`:**
   - Το notebook επαναδιατυπώθηκε ως καθαρό raw decoding / timestamp integrity validation στάδιο.
   - Αφαιρέθηκαν legacy debug sections, monkey-patching λογική και ad hoc exploratory fragments που δεν ανήκαν στο canonical forecasting pipeline.

2. **Ρητός χειρισμός raw input / target αρχείων του DaKS dataset:**
   - Εφαρμόστηκε strict input-target pairing ανά `park_id`.
   - Προστέθηκε explicit CSV separator handling με fallback ανά αρχείο.
   - Προστέθηκε explicit timestamp-column detection για input και target files.

3. **Σταθεροποίηση timestamp parsing:**
   - Αντικαταστάθηκε το ambiguous datetime parsing με explicit allowed timestamp formats ανά file type.
   - Το parsing πλέον δεν βασίζεται σε `format='mixed'` ή άλλες χαλαρές heuristics.
   - Η χρονική σειρά ελέγχεται ρητά πριν από το merge.

4. **Validation του input-target synchronization:**
   - Υλοποιήθηκε deterministic single-park validation.
   - Υλοποιήθηκε all-parks raw audit με interpretable failure logging.
   - Επιβεβαιώθηκε explicit merge validation πάνω στο timestamp backbone πριν από τα downstream notebooks.

### Scientific Interpretation:
Το NB02 θεωρείται πλέον methodologically acceptable ως canonical raw validation στάδιο του forecasting pipeline.
Ο ρόλος του περιορίζεται σε:
- raw decoding,
- timestamp parsing verification,
- temporal ordering checks,
- και input-target timestamp alignment.

Άρα το notebook παραμένει επιστημονικά καθαρό:
- χωρίς modeling,
- χωρίς splitting,
- χωρίς feature engineering,
- και χωρίς claims πέρα από raw data integrity validation.

### Practical Note:
Το τρέχον local raw directory αποδίδει 272 πλήρως ζευγοποιημένα input-target park pairs.
Η λεπτομέρεια αυτή καταγράφεται ως local-data note και μπορεί να ελεγχθεί αργότερα έναντι της ευρύτερης DaKS documentation, όπου η δημοσίευση αναφέρει 273 wind plants.

### Next Step:
Επόμενο βήμα είναι το methodological audit του `04_feature_engineering_and_graph_construction.ipynb` με έμφαση σε:
- leakage-safe rolling / lag feature construction,
- consistency του engineered feature space,
- και readiness για τα downstream split / benchmark notebooks.

**Commit Reference:** `fix(nb02): stabilize DaKS timestamp parsing and raw validation flow`


---


## [27/03/2026] - Canonicalization of NB02 and NB03, Documentation Realignment

### Ολοκληρωμένες Ενέργειες:
1. **Οριστικοποίηση του `02_kassel_exploration.ipynb` ως canonical raw validation gate**
   - Το NB02 σταθεροποιήθηκε ως strict raw validation / timestamp integrity notebook.
   - Εφαρμόζεται strict input-target pairing ανά `park_id`.
   - Υπάρχει explicit separator handling, strict timestamp parsing, duplicate timestamp detection και exact input-target timestamp alignment.
   - Το notebook παράγει τα canonical raw audit artifacts του NB02.

2. **Οριστικοποίηση του `03_eda_master.ipynb` ως validated-only EDA stage**
   - Το NB03 διαβάζει τα `nb02_*.csv` ως upstream validation contract.
   - Συνεχίζει μόνο με parks όπου `status in {"ok", "warning"}`.
   - Το failed park `06238` αποκλείεται ρητά από downstream processing.
   - Το notebook λειτουργεί ως validated-only master EDA stage και όχι ως raw validation / cleaning notebook.

3. **Καθαρός downstream contract ορισμός**
   - Το canonical progression του pipeline είναι πλέον:
     `NB02 raw validation -> NB03 validated-only EDA -> NB04 feature engineering`.
   - Το `park_id` αντιμετωπίζεται ως string στα downstream notebooks.
   - Δεν επιτρέπεται loose reparsing raw timestamps μετά το NB02.

4. **Documentation realignment**
   - Επιβεβαιώθηκε ότι το active repository scope είναι το DaKS / Kassel forecasting pipeline.
   - Τα legacy exploratory directions (π.χ. ENTSO-E / Renewables.ninja / older triple-source framing) πρέπει να αντιμετωπίζονται ως historical context και όχι ως current canonical pipeline.
   - Προτείνεται διάκριση μεταξύ active log και archive log για να μειωθεί η documentation ambiguity.

### Scientific Interpretation:
Το forecasting pipeline είναι πλέον σαφέστερα οργανωμένο σε validation-first μορφή.
Το NB02 αποτελεί τη μοναδική canonical authority για raw integrity,
ενώ το NB03 αποτελεί το canonical validated-only EDA layer.
Η αρχιτεκτονική αυτή βελτιώνει reproducibility, leakage control και downstream benchmark clarity.

### Practical Note:
Ο `KasselLoader` παραμένει operational helper για loading / feature preparation,
αλλά όχι canonical strict validation authority.
Η canonical raw integrity authority του project είναι πλέον το NB02.

### Next Step:
Methodological audit και rewrite planning για το
`04_feature_engineering_and_graph_construction.ipynb`
με έμφαση σε:
- leakage-safe lag / rolling construction,
- stable feature-space definition,
- spatial metadata integration,
- graph artifact consistency.