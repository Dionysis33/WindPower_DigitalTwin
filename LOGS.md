# Ημερολόγιο Προόδου Πτυχιακής Εργασίας
**Project:** WindPower_DigitalTwin

---

## [30/01/2026] - Φάση 1: Προετοιμασία & Στήσιμο Περιβάλλοντος

### Ολοκληρωμένες Ενέργειες:
1. **Διαχείριση Έκδοσης (Git & GitHub):**
   - Αρχικοποίηση τοπικού Git repository.
   - Σύνδεση με το GitHub (Repository: `Dionysis33/WindPower_DigitalTwin`).
   - Πραγματοποίηση των πρώτων commits ("Initial commit", "Exclude venv folder").

2. **Αρχιτεκτονική Έργου:**
   - Δημιουργία βασικής δομής φακέλων:
     - `data/`: Για αποθήκευση συνόλων δεδομένων.
     - `models/`: Για τα αρχεία των μοντέλων (π.χ. .h5, .pkl).
     - `notebooks/`: Για πειραματική ανάλυση δεδομένων.
     - `scripts/`: Για τον τελικό κώδικα Python.

3. **Ρυθμίσεις Git (Security & Optimization):**
   - Παραμετροποίηση του αρχείου `.gitignore`.
   - Εξαίρεση του εικονικού περιβάλλοντος (`venv/`), των προσωρινών αρχείων (`.ipynb_checkpoints/`), των ρυθμίσεων του VS Code (`.vscode/`) και των φακέλων δεδομένων/μοντέλων από τον συγχρονισμό στο GitHub.

4. **Εικονικό Περιβάλλον (Python Virtual Environment):**
   - Δημιουργία και ενεργοποίηση του `venv` (Python 3.12).
   - Αναβάθμιση του `pip` στην τελευταία έκδοση.

5. **Εγκατάσταση Τεχνολογικού Stack:**
   - **Data Science:** `pandas`, `numpy`, `scikit-learn`.
   - **Visualization:** `matplotlib`, `seaborn`.
   - **Connectivity:** `entsoe-py`, `requests`, `sqlalchemy` (για MySQL).
   - **Utilities:** `openpyxl` (για Excel αρχεία).
   - **Environment:** Πλήρης εγκατάσταση του `jupyterlab` για χρήση Notebooks.

---

## Επόμενα Βήματα:
- [ ] Δημιουργία του πρώτου Notebook (`01_data_acquisition.ipynb`).
- [ ] Αίτηση για API Key στην πλατφόρμα ENTSO-E Transparency.
- [ ] Έρευνα για εναλλακτικές open-source πηγές δεδομένων αιολικής ενέργειας.
- [ ] Σχεδιασμός της αρχιτεκτονικής του Digital Twin στο draw.io.


## [31/01/2026] - Φάση 2: Συλλογή Δεδομένων & Βελτιστοποίηση

### Ολοκληρωμένες Ενέργειες:

1. **Διαδικασία API:**
   - Αποστολή αιτήματος για API Token στην πλατφόρμα ENTSO-E (Ticket #9442809) για λήψη δεδομένων από ποικίλες ευρωπαϊκές ζώνες.

2. **Version Control & Maintenance:**
   - Βελτιστοποίηση του αρχείου `.gitignore` με αφαίρεση περιττών εγγραφών (redundant venv entry).
   - Επιτυχής συγχρονισμός (Push) των αλλαγών στο GitHub repository.

3. **Έναρξη Ανάπτυξης:**
   - Προετοιμασία του Notebook `01_data_acquisition.ipynb`.

4. **Ασφάλεια & Διαχείριση API Keys:**
   - Δημιουργία αρχείου `.env` για την ασφαλή αποθήκευση των API Tokens.
   - Εγκατάσταση και παραμετροποίηση της βιβλιοθήκης `python-dotenv` για την ασφαλή ανάκτηση των κλειδιών.

5. **Υλοποίηση Data Pipeline (`01_data_acquisition.ipynb`):**
   - Ανάπτυξη κώδικα για την επικοινωνία με το REST API του Renewables.ninja.
   - **Επίλυση Σφάλματος:** Αντιμετώπιση του `OverflowError` στον index των ημερομηνιών με χρήση της συνάρτησης `pd.to_numeric` και μετατροπή σε milliseconds (`unit='ms'`).
   - **Data Extraction:** Επιτυχής λήψη και κανονικοποίηση (normalization) ωριαίων δεδομένων αιολικής ισχύος για την περιοχή της **Εύβοιας** για το 2024.
   - **Αποθήκευση:** Εξαγωγή των δεδομένων σε αρχείο `data/wind_evia_2024_raw.csv`.

---

## Επόμενα Βήματα:
- [ ] Λήψη αντίστοιχου dataset για περιοχή της Γερμανίας για τη διεξαγωγή συγκριτικής ανάλυσης.
- [ ] Έναρξη του Notebook `02_exploratory_data_analysis.ipynb` για τον εντοπισμό outliers.
- [ ] Οπτικοποίηση των χρονοσειρών (Time-series Visualization).