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