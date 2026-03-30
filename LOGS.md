# Active Project Log

Αυτό το αρχείο καταγράφει την ενεργή canonical methodological κατάσταση του τρέχοντος **forecasting-first** pipeline του repository.

Current canonical progression:

`NB02 raw validation -> NB03 validated-only EDA -> NB04 feature engineering -> NB05 outlier handling / temporal split -> NB06 baseline modeling -> NB07 advanced tabular baselines -> NB08 downstream residual diagnostics`

Interpretation bridge:

`forecasting -> residual diagnostics -> health-aware / PHM-oriented interpretation`

Τα παλαιότερα exploratory ή superseded entries έχουν μεταφερθεί στο `LOGS_ARCHIVE.md`.


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


---


## [28/03/2026] - NB02 Coverage-Aware Audit & NB03 Canonical Rewrite Stabilization

### Τεχνικά Επιτεύγματα (Technical Milestones):

1. **Επέκταση του `NB02` από strict raw validation σε coverage-aware downstream contract**
   - Το `02_kassel_exploration.ipynb` παρέμεινε η μοναδική **canonical raw validation authority** του pipeline.
   - Δεν αλλοιώθηκε ο βασικός ρόλος του notebook ως:
     - raw decoding,
     - strict timestamp parsing verification,
     - duplicate / NaT detection,
     - exact input-target alignment audit.
   - Προστέθηκε όμως νέο coverage-aware layer ώστε να διαχωρίζονται:
     - `raw_valid` parks
     - από `NB04-eligible` parks.

2. **Νέα NB02 artifacts για cohort-aware downstream χρήση**
   - Προστέθηκαν τα εξής νέα processed artifacts:
     - `nb02_meta_coverage_audit.csv`
     - `nb02_coverage_class_summary.csv`
     - `nb02_nb04_eligibility_summary.csv`
   - Ο downstream contract δεν βασίζεται πλέον μόνο στο απλό:
     - `status in {"ok", "warning"}`
   - Πλέον γίνεται ρητός διαχωρισμός μεταξύ:
     - strict raw validity
     - coverage class
     - strict downstream eligibility

3. **Κύρια empirical findings από τα exported CSV audits**
   - Το all-pairs raw validation έδειξε ότι το dataset δεν είναι απλώς “ok / failed”.
   - Αναδείχθηκε πραγματική heterogeneity στο validated population:
     - full standard window parks
     - partial mixed window parks
     - partial / nonstandard train-only parks
     - partial / nonstandard test-only parks
     - και ένα raw-failed pair
   - Στο current run προέκυψε ότι:
     - το strict raw-valid population είναι μεγαλύτερο από το τελικό benchmark-ready cohort
     - ενώ το canonical retained cohort για downstream master assembly περιορίζεται στα `NB04-eligible` parks
   - Άρα το βασικό methodological finding ήταν ότι:
     > raw-valid ≠ cohort-equivalent

4. **Σταθεροποίηση του `NB03` ως validated-only και coverage-aware master EDA stage**
   - Το `03_eda_master.ipynb` ξαναγράφηκε ώστε:
     - να μη ξανακάνει raw validation,
     - να μη κάνει loose reparsing raw timestamps,
     - να μη χρησιμοποιεί πλέον hard-coded exclusion logic,
     - και να μην αντιμετωπίζει όλα τα raw-valid parks ως downstream ισοδύναμα.
   - Το actual `master_df` πλέον χτίζεται μόνο από parks με:
     - `nb04_eligible == True`
   - Το notebook εξάγει canonical downstream artifacts:
     - `master_dataset.csv`
     - `master_schema_summary.csv`
     - `master_park_summary.csv`
     - `master_anomaly_profile.csv`
     - `master_park_load_summary.csv`

5. **Config synchronization με το νέο upstream contract**
   - Το `src/config.py` ενημερώθηκε ώστε να περιλαμβάνει τα νέα NB02 coverage-aware artifact paths.
   - Έτσι τα downstream notebooks μπορούν να χρησιμοποιούν explicit constants αντί για ad hoc paths.
   - Αυτό βελτιώνει:
     - reproducibility,
     - path consistency,
     - και notebook-to-script synchronization.

6. **Τι κάναμε και τι ΔΕΝ κάναμε στον `KasselLoader`**
   - Επιβεβαιώθηκε ξανά ότι ο `KasselLoader` είναι:
     - operational helper
     - και όχι canonical raw validation authority
   - Δεν μεταφέραμε τη methodological authority από το `NB02` στον loader.
   - Ο loader χρησιμοποιήθηκε downstream μόνο για convenience loading / assembly.
   - Δεν ολοκληρώθηκε ακόμη separate loader hardening patch.

### Scientific Interpretation:
Το κρίσιμο methodological εύρημα αυτής της φάσης ήταν ότι
η raw εγκυρότητα ενός park pair δεν αρκεί από μόνη της για benchmark-ready downstream χρήση.

Με άλλα λόγια:
- ένα park μπορεί να είναι raw-valid,
- αλλά να μην ανήκει στο canonical πλήρες cohort που θέλουμε για feature engineering / benchmark assembly.

Αυτό οδήγησε σε σαφέστερο pipeline contract:

`NB02 raw validation -> NB02 coverage-aware eligibility -> NB03 validated-only / NB04-eligible master assembly`

Η αλλαγή αυτή βελτιώνει:
- cohort clarity,
- reproducibility,
- downstream consistency,
- και benchmark validity.

### CSV-level Findings που χρειάζονται να θυμόμαστε:
1. Το validated population δεν είναι πλήρως ομοιογενές.
2. Υπάρχουν parks με nonstandard temporal coverage που δεν πρέπει να περνούν αυτόματα στο canonical downstream cohort.
3. Τα exported CSV audits είναι πλέον η authority για:
   - raw validity,
   - coverage class,
   - και NB04 eligibility.
4. Τα downstream στάδια πρέπει να βασίζονται σε αυτά τα artifacts και όχι σε implicit assumptions.

### Loader Notes / Future Caution:
1. Ο `KasselLoader` παραμένει operational helper και όχι raw-validation authority.
2. Το current loader implementation χρειάζεται μελλοντικά additional hardening:
   - explicit pre-check πλήρους timestamp-set equality πριν ή γύρω από το merge,
   - ώστε να αποφεύγεται πιθανό silent shrinkage σε mismatch case
   - και καλύτερη ευθυγράμμιση με το canonical NB02 contract.
3. Επίσης καλό είναι να εξεταστεί στο μέλλον:
   - recursive file discovery αντί για μόνο flat `glob("*.csv")`
   - και πιο σαφής handling ειδικών edge cases input files.

### Τι χρειάζεται προσοχή στο μέλλον για αποφυγή methodological regressions:
- Να μην ξαναμπεί λογική `status in {"ok","warning"}` ως μόνο eligibility gate.
- Να μην επιστρέψει hard-coded exclusion λογική τύπου συγκεκριμένου `park_id`.
- Να μην γίνει downstream loose reparsing timestamps μετά το `NB02`.
- Να μην συγχέονται:
  - raw-valid parks
  - με strict benchmark-ready cohort parks.
- Όταν αλλάζει το notebook-stage contract, να ενημερώνονται συντονισμένα:
  - `README.md`
  - `LOGS.md`
  - `docs/INDEX.md`
  - και το σχετικό notebook markdown.
- Να διατηρείται σαφές ότι τα anomaly-like findings στα exported EDA CSVs
  είναι descriptive outputs του `NB03` και όχι automatic cleaning decisions.

### Practical Note:
Με την ολοκλήρωση αυτής της φάσης:
- το `NB02` θεωρείται κλειστό ως canonical raw validation + coverage-aware audit stage
- το `NB03` θεωρείται κλειστό ως validated-only / NB04-eligible master EDA stage
- και το επόμενο λογικό methodological βήμα είναι το:
  - `04_feature_engineering_and_graph_construction.ipynb`

### Commit References:
- `config: add NB02 coverage-aware artifact paths`
- `feat(nb02): add coverage-aware downstream eligibility audit`
- `refactor(nb03): rewrite validated-only master EDA with NB04 eligibility gate`


---


## [28/03/2026] - NB04 Canonical Rewrite, Leakage-Safe Feature Engineering & Graph Export Stabilization

### Τεχνικά Επιτεύγματα (Technical Milestones):
1. **Complete rewrite του `04_feature_engineering_and_graph_construction.ipynb`**
   - Το `NB04` επανασχεδιάστηκε ως καθαρό **validated-only downstream feature engineering stage**.
   - Αφαιρέθηκε raw rediscovery λογική, loose reparsing timestamps και ad hoc metadata hunting.
   - Το notebook πλέον χρησιμοποιεί μόνο τα canonical downstream artifacts που έχουν ήδη παραχθεί upstream.

2. **Leakage-safe temporal feature construction**
   - Τα lag features κατασκευάζονται αυστηρά ανά `park_id` μετά από deterministic sorting στο canonical `timestamp` backbone.
   - Τα rolling features έγιναν **causal-by-construction** με `shift(1)` πριν από rolling mean / std.
   - Έτσι αποφεύγεται direct ή indirect χρήση της current-step target τιμής στη στιγμή `t`.

3. **Σταθεροποίηση feature-space definition**
   - Το τελικό exported dataset διαχωρίζει καθαρότερα:
     - backbone / control columns
     - static / spatial metadata
     - exogenous meteorological features
     - engineered temporal / autoregressive features
   - Provenance / audit columns δεν αντιμετωπίζονται πλέον ως candidate modeling inputs στο canonical export.

4. **Strict spatial validation και graph-ready artifact construction**
   - Εφαρμόστηκε deterministic node ordering πάνω στο strict `NB04-eligible` cohort.
   - Ο spatial graph κατασκευάστηκε με μία μόνο authoritative export path.
   - Ο exported adjacency matrix είναι binary, συμμετρικός και consistent με το graph node order.

5. **Επανεκτέλεση και επιβεβαίωση των NB04 exports**
   - Το notebook ολοκληρώθηκε επιτυχώς χωρίς execution error.
   - Παράχθηκαν εκ νέου τα canonical downstream artifacts:
     - `final_feature_engineered_dataset.csv`
     - `adjacency_matrix.npy`
     - `graph_node_order.csv`
     - `graph_edge_index.npy`
     - `graph_distance_matrix_km.npy`

### Current rerun outputs:
- **Parks:** 256
- **Final dataset rows:** 3,252,070
- **Final dataset columns:** 47
- **Graph nodes:** 256
- **Undirected edges:** 534

### Scientific Interpretation:
Το βασικό methodological concern του `NB04` για πιθανό leakage σε rolling target-derived features θεωρείται πλέον resolved.
Το notebook λειτουργεί πλέον ως καθαρό, leakage-aware και graph-ready feature engineering stage για τα downstream benchmark και diagnostics notebooks.

### Next Step:
Επόμενο βήμα είναι ο downstream rerun / verification έλεγχος στα:
- `05_outliers_and_split.ipynb`
- `06_baseline_modeling.ipynb`
- `07_advanced_baselines_and_importance.ipynb`

ώστε να επιβεβαιωθεί πλήρως η consistency του stabilized artifact chain πριν από το `NB08`.

### Commit References:
- `fix(nb04): rewrite feature engineering with leakage-safe rolling and graph-ready exports`

---

### Verification update after clean rerun

Μετά την ολοκλήρωση του rewrite και του καθαρού rerun του `05_outliers_and_split.ipynb`, πραγματοποιήθηκε επιπλέον **post-export file-level verification** στα canonical split artifacts που παράγονται από το notebook.

Ο στόχος αυτού του δεύτερου ελέγχου ήταν να επιβεβαιωθεί ότι:

- τα exported CSV αρχεία γράφτηκαν σωστά,
- δεν υπάρχει truncated ή corrupted artifact,
- τα row counts συμφωνούν ακριβώς με το current in-memory split state,
- το schema παραμένει identical στα `train / val / test`,
- και το `test_flag` contract τηρείται όπως ορίζεται από το current flag-aware split protocol.

#### Επιβεβαιωμένα canonical outputs

Το verification επιβεβαίωσε ότι το current rerun state του `NB05` παράγει τα εξής canonical artifacts:

- `train_final.csv` → **1,982,736 rows**, **47 columns**
- `val_final.csv` → **182,998 rows**, **47 columns**
- `test_final.csv` → **1,086,336 rows**, **47 columns**

#### Τι επιβεβαιώθηκε στο file-level verification

Πέρα από το απλό row-count check, επιβεβαιώθηκαν και τα εξής:

- σωστή ανάγνωση header χωρίς schema corruption
- σωστό πλήθος στηλών σε όλα τα exported files
- επιτυχές sample parse μετά το export
- παρουσία των required backbone columns:
  - `park_id`
  - `timestamp`
  - `test_flag`
  - `Power_Output_Normalized`
  - `Baseline_Prediction`
- σωστό `test_flag` contract ανά split:
  - `train_final.csv` → μόνο `test_flag == 0`
  - `val_final.csv` → μόνο `test_flag == 0`
  - `test_final.csv` → μόνο `test_flag == 1`

Το τελικό verification cell του notebook επέστρεψε:

- **QUICK VERIFICATION PASSED**

#### Methodological clarification

Η τελική verification φάση βοήθησε επίσης να αποσαφηνιστεί η σωστή διατύπωση του split semantics στο active documentation.

Πιο συγκεκριμένα, το `val_df` πρέπει να περιγράφεται ως:

- **το τελικό χρονικό tail του pre-test window**

και όχι ως stronger claim τύπου:

- **τελευταίο contiguous χρονικό block**

Η νέα διατύπωση είναι πιο ακριβής, επειδή το notebook ορίζει το validation split μέσω χρονικού cutoff μέσα στο pre-test window και όχι μέσω πρόσθετης εγγύησης πλήρους per-park contiguity.

#### Practical implication

Με αυτή την επιβεβαίωση, το `NB05` θεωρείται πλέον πλήρως επαληθευμένο ως canonical downstream stage για:

- leakage-safe outlier handling,
- flag-aware temporal split,
- deterministic export,
- και stable handoff προς τα `NB06` και `NB07`.

Άρα, από τη σκοπιά του artifact chain, το τμήμα:

- `NB04 -> NB05`

θεωρείται πλέον σταθεροποιημένο και αναπαραγώγιμο στο current local rerun state.


---


## [30/03/2026] - NB06 Canonical Rewrite, Test-Only Benchmark Export & Diagnostic Handoff Stabilization

### Τεχνικά Επιτεύγματα (Technical Milestones):
1. **Complete rewrite του `06_baseline_modeling.ipynb`**
   - Το `NB06` επανασχεδιάστηκε ως καθαρό downstream baseline notebook πάνω στα canonical split artifacts:
     - `train_final.csv`
     - `val_final.csv`
     - `test_final.csv`
   - Αφαιρέθηκε ambiguity ανάμεσα σε intermediate validation reporting και final benchmark export.
   - Το notebook παραμένει αυστηρά στο forecasting scope:
     - `Persistence`
     - `Linear Regression`
     - baseline comparison
     - residual diagnostics
     - actual-vs-predicted analysis

2. **Split integrity και feature-space contract checks**
   - Προστέθηκαν explicit checks για:
     - required input files
     - required columns
     - split/schema consistency
     - blocked columns εκτός learned-model feature space
   - Διατηρήθηκε καθαρός feature / target contract για τα baselines του NB06.
   - Το notebook λειτουργεί πλέον πιο fail-fast και reproducibly πάνω στο stabilized upstream stack.

3. **Canonical benchmark export cleanup**
   - Το benchmark export logic καθαρίστηκε ώστε να μην υπάρχει contamination του
     `data/processed/baseline_metrics.csv`
     από intermediate validation outputs.
   - Τα validation metrics διατηρούνται μόνο για notebook-level interpretation.
   - Το `baseline_metrics.csv` ενημερώνεται πλέον μόνο με canonical **test-set** rows του NB06.

4. **Diagnostic handoff artifact**
   - Προστέθηκε export του:
     - `data/processed/nb06_test_predictions.csv`
   - Το artifact αυτό προορίζεται για downstream residual diagnostics και benchmark-aligned error inspection.
   - Το export βασίζεται σε καθαρό evaluation key space και είναι κατάλληλο ως handoff προς το NB08.

### Scientific Interpretation:
Το βασικό methodological concern του NB06 για benchmark export contamination θεωρείται πλέον resolved.

Το `NB06` είναι τώρα:
- methodologically acceptable
- benchmark-safe στο current scope
- reproducible ως downstream stage μετά το `NB05`
- κατάλληλο για diagnostics-oriented handoff

### Important Note:
Το current `baseline_metrics.csv` μετά το rerun του `NB06` πρέπει να αντιμετωπίζεται ως **transitional benchmark artifact** του NB06 stage και όχι ακόμη ως το τελικό thesis-ready cross-model benchmark table, μέχρι να ολοκληρωθεί και το canonical cleanup / rerun του `NB07`.

### Next Step:
Επόμενο βήμα είναι το canonical rewrite / rerun του:
- `07_advanced_baselines_and_importance.ipynb`

με έμφαση σε:
- κοινό canonical evaluation key space
- benchmark update consistency
- πλήρη επανασυγκρότηση του `baseline_metrics.csv` ως final **test-only** benchmark table για όλη την baseline ladder

### Commit References:
- `fix(nb06): stabilize canonical benchmark export and test-only reporting`


---


## [30/03/2026] - NB07 Benchmark Reconciliation & Active Log Finalization

### Ολοκληρωμένες Ενέργειες:
1. Ολοκληρώθηκε το methodological reconciliation του `07_advanced_baselines_and_importance.ipynb` ως strict downstream stage πάνω στα canonical artifacts του `NB05`.
2. Επιβεβαιώθηκε ότι το `NB07` παραμένει συνεπές με το established benchmark contract του pipeline:
   - κοινό leakage-safe feature space,
   - validation μόνο για model selection,
   - test μόνο για final reporting.
3. Ορίστηκε ρητά ότι το `data/processed/baseline_metrics.csv` αποτελεί το current **canonical final test-set benchmark table** για όλη την implemented baseline ladder.
4. Τα historical NB07 benchmark values και παλαιότερα notebook-run states διατηρούνται μόνο στο `LOGS_ARCHIVE.md` ως history και όχι ως active canonical authority.
5. Το active documentation realigned ώστε το `README.md`, το `LOGS.md` και το benchmark interpretation να χρησιμοποιούν το ίδιο canonical reporting rule.

### Scientific Interpretation:
Μετά το παρόν reconciliation pass, το forecasting pipeline θεωρείται documentation-consistent ως προς:
- split semantics,
- leakage-safe benchmark reporting,
- validation-vs-test role separation,
- και benchmark provenance.

Για thesis-ready reporting, authority για cross-model comparison είναι το τρέχον `data/processed/baseline_metrics.csv` και όχι historical metric mentions σε archived log entries.

### Practical Note:
Όπου χρειάζεται αριθμητική αναφορά benchmark αποτελεσμάτων, οι τιμές πρέπει να αντιγράφονται από το current `baseline_metrics.csv` και όχι από παλαιότερα notebook outputs ή archived log text.

### Next Step:
Επόμενο βήμα είναι downstream diagnostics / interpretation work πάνω στο stabilized forecasting benchmark stack, χωρίς αλλαγή του canonical baseline reporting contract.


---


## [30/03/2026] - NB08 Operating-Regime Residual Diagnostics & Health-Oriented Interpretation Bridge

### Τεχνικά Επιτεύγματα (Technical Milestones):
1. **Ολοκλήρωση του `08_residual_diagnostics_and_operating_regimes.ipynb`**
   - Το `NB08` υλοποιήθηκε ως **strict downstream diagnostics notebook** πάνω στα canonical exported test artifacts.
   - Το notebook δεν εισάγει νέο training, δεν αλλάζει splits και δεν επηρεάζει το upstream benchmark protocol.

2. **Canonical downstream evaluation space**
   - Χρησιμοποιήθηκαν τα εξής canonical inputs:
     - `data/processed/test_final.csv`
     - `data/processed/baseline_metrics.csv`
     - `data/processed/nb06_test_predictions.csv`
     - `data/processed/predictions/nb07_all_test_predictions_long.csv` ή τα αντίστοιχα fallback exports
   - Επιβεβαιώθηκε κοινό **test-only row-level evaluation space** για όλα τα implemented baselines.

3. **Residual diagnostics across implemented baselines**
   - Πραγματοποιήθηκε residual analysis για:
     - `Persistence`
     - `Linear Regression`
     - `Random Forest`
     - `XGBoost`
     - `MLP`
   - Υλοποιήθηκε cross-model residual / absolute-error structure analysis.

4. **Operating-regime slicing**
   - Ορίστηκαν και αναλύθηκαν:
     - wind-related regimes
     - power-related regimes
     - secondary temporal blocks
   - Παράχθηκαν regime-wise summaries και diagnostic plots για να φανεί αν η error structure μεταβάλλεται συστηματικά ανά operating condition.

5. **Compact diagnostics exports**
   - Εξήχθησαν τα εξής summary artifacts:
     - `nb08_wind_regime_metrics.csv`
     - `nb08_power_regime_metrics.csv`
     - `nb08_time_block_metrics.csv`
     - `nb08_best_model_by_wind_regime.csv`
     - `nb08_best_model_by_power_regime.csv`

### Scientific Interpretation:
Το `NB08` έδειξε ότι τα forecasting residuals δεν περιγράφονται επαρκώς μόνο από aggregate metrics όπως MAE / RMSE / R².

Αντίθετα, η residual structure εμφανίζει **structured dependence across operating regimes**, κάτι που ενισχύει τη diagnostics-aware ανάγνωση του benchmark stack.

Αυτό δεν ισοδυναμεί με:
- fault diagnosis,
- anomaly detection ως completed module,
- health-state inference,
- ή RUL estimation.

Αποτελεί όμως ένα καθαρό και μεθοδολογικά defensible βήμα από:

`forecasting -> residual diagnostics -> health-aware / PHM-oriented interpretation`

### Methodological Note:
Το notebook παραμένει:
- **test-only**
- **benchmark-safe**
- **non-overclaiming**
- και πλήρως ευθυγραμμισμένο με το forecasting-first positioning του repository.

Το digital-twin framing διατηρείται, αλλά πλέον υποστηρίζεται από πιο explicit σύνδεση με prognostics / health-management direction μέσω structured residual analysis.

### Practical Outcome:
Το issue για το operating-regime diagnostics experiment θεωρείται πλέον ολοκληρωμένο σε notebook-level scope και το σχετικό PR merged στο `main`.
---