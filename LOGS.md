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
   - **Connectivity:** `entsoe-py`, `requests`, `sqlalchemy`.
   - **Utilities:** `openpyxl`.
   - **Environment:** Πλήρης εγκατάσταση του `jupyterlab` για χρήση Notebooks.

---

## [31/01/2026] - Φάση 2: Συλλογή Δεδομένων & Βελτιστοποίηση

### Ολοκληρωμένες Ενέργειες:
1. **Διαδικασία API:**
   - Αποστολή αιτήματος για API Token στην πλατφόρμα ENTSO-E (Ticket #9442809) για λήψη δεδομένων από ποικίλες διεθνείς ζώνες.

2. **Version Control & Maintenance:**
   - Βελτιστοποίηση του αρχείου `.gitignore` με αφαίρεση περιττών εγγραφών (redundant venv entry).
   - Επιτυχής συγχρονισμός (Push) των αλλαγών στο GitHub repository.

3. **Έναρξη Ανάπτυξης:**
   - Προετοιμασία του Notebook `01_data_acquisition.ipynb`.

4. **Ασφάλεια & Διαχείριση API Keys:**
   - Δημιουργία αρχείου `.env` για την ασφαλή αποθήκευση των API Tokens.
   - Εγκατάσταση και παραμετροποίηση της βιβλιοθήκης `python-dotenv` για την ασφαλή ανάκτηση των κλειδιών.

---

## [02/02/2026] - Φάση 2: Αναδιάρθρωση & Στρατηγική Δεδομένων

### 1. **Διαδικασία API:**
- **ENTSO-E Approval:** Επιτυχής έγκριση του αιτήματος πρόσβασης (Ticket #9442809) και ενεργοποίηση του Web API Access.
- **Token Management:** Δημιουργία και ασφαλής αποθήκευση του `ENTSOE_API_TOKEN` στο αρχείο `.env`.

### 2. **Τεχνική Αναδιοργάνωση (Refactoring):**
- **Εφαρμογή Προτύπου "Cookiecutter Data Science":** Πραγματοποιήθηκε ριζική αναβάθμιση της οργανωτικής δομής για την υποστήριξη επαγγελματικού workflow:
    - **Υποδιαίρεση Δεδομένων:** Δημιουργία των φακέλων `data/raw/`, `data/interim/` και `data/processed/` για τον έλεγχο της ποιότητας των δεδομένων.
    - **Modular Code Structure:** Δημιουργία του φακέλου `src/` για τη μεταφορά επαναχρησιμοποιήσιμων Python modules όπως το `features.py`.
    - **Documentation & Figures:** Δημιουργία του `reports/figures/` για την αποθήκευση γραφημάτων υψηλής ποιότητας.

### 3. **Στρατηγική Feature Engineering & Δεδομένων:**
- **Σχεδιασμός Προηγμένων Χαρακτηριστικών:** Καθορίστηκε η υλοποίηση των εξής τεχνικών:
    - **Cyclical Encoding:** Μετασχηματισμός ώρας/μήνα σε ημιτονοειδείς συνιστώσες (sin/cos).
    - **Wind Shear Scaling:** Προσαρμογή ταχύτητας ανέμου στο ύψος της πλήμνης (hub height) μέσω του Power Law.
    - **Empirical Mode Decomposition (EMD):** Αποσύνθεση σήματος για μείωση του σφάλματος RMSE.
- **Υβριδική Προσέγγιση Πηγών:**
    - **ENTSO-E Transparency:** Λήψη διεθνών δεδομένων για το σκέλος της πρόβλεψης (Forecasting).
    - **CARE to Compare (Benchmark):** Χρήση του διεθνούς dataset για το σκέλος της ανίχνευσης ανωμαλιών (Anomaly Detection) λόγω των επισημειωμένων πραγματικών βλαβών.

---

## Επόμενα Βήματα:
- [ ] Μετακίνηση των υπαρχόντων CSV αρχείων στον φάκελο `data/raw/`.
- [ ] Δημιουργία του πρώτου module `src/features.py` με τις συναρτήσεις μετασχηματισμού.


---

## [03/02/2026] - Φάση 2: Αναδιοργάνωση, Debugging & Στρατηγική Δεδομένων

### Ολοκληρωμένες Ενέργειες:
1. **Αναδιάρθρωση Φακέλων (Project Refactoring):**
   - Εφαρμογή επαγγελματικής δομής φακέλων: `data/raw/`, `data/interim/`, `data/processed/`, `src/`, και `notebooks/`.
   - Μεταφορά των notebooks και των αρχείων ρυθμίσεων στις σωστές τοποθεσίες για βελτιωμένη διαχειρισιμότητα.

2. **Επίλυση Τεχνικών Σφαλμάτων (Bug Fixing):**
   - Διόρθωση του `NameError: name 'ninja_token' is not defined` στο Renewables.ninja notebook.
   - Επαναφορά της σωστής σειράς εκτέλεσης (cells sequence) για τη φόρτωση των περιβαλλοντικών μεταβλητών από το αρχείο `.env`.

3. **Βελτιστοποίηση Διαδρομών (Path Optimization):**
   - Ενημέρωση των scripts αποθήκευσης δεδομένων. Πλέον όλα τα πρωτογενή αρχεία (Raw Data) αποθηκεύονται αυτόματα στη διαδρομή `../data/raw/` με σωστή ονοματολογία (π.χ. `ninja_evia_2024_raw.csv`).

4. **Επικαιροποίηση Τεκμηρίωσης (Documentation):**
   - Πλήρης αναθεώρηση του `README.md` με την προσθήκη του **Google Colab** στο Tech Stack και την ανάλυση της "Triple Data Strategy".
   - Καθορισμός των τριών πυλώνων δεδομένων:
     - **Renewables.ninja:** Simulated Power (Theoretical Baseline).
     - **ENTSO-E:** Real Grid Generation (Actual Production).
     - **CARE to Compare:** SCADA Fault Data (Anomaly Labels).

5. **Έλεγχος Εκδόσεων (Git Workflow):**
   - Επιτυχής συγχρονισμός (Push) όλων των τοπικών αλλαγών στο GitHub repository.
   - Επίλυση θεμάτων στον Git editor (`COMMIT_EDITMSG`) και ολοκλήρωση του κύκλου commit/sync.

---

## Επόμενα Βήματα:
- [ ] Υλοποίηση του API Script για τη μαζική λήψη δεδομένων **ENTSO-E (2020-2025)**.
- [ ] Χειροκίνητη λήψη και οργάνωση του **CARE to Compare** dataset στο φάκελο `data/raw/`.
- [ ] Έναρξη διαδικασίας συγχρονισμού χρονοσειρών (Time-series Alignment).

---

## [06/02/2026] - Στρατηγική Αναθεώρηση Πηγών Δεδομένων

### ### Αποφάσεις & Ενέργειες:
- **Αντικατάσταση ENTSO-E:** Αποφασίστηκε η απόσυρση των δεδομένων της ENTSO-E από το βασικό pipeline. 
  - **Αιτιολόγηση:** Η έλλειψη χωρικής ανάλυσης (spatial resolution) και τεχνικών προδιαγραφών ανά τουρμπίνα καθιστούσε τα δεδομένα ανεπαρκή για τη δημιουργία ενός ακριβούς Digital Twin.
- **Ενσωμάτωση DaKS Dataset (Uni-Kassel):** Επιλογή του "DAF ICON Synthetic Wind Power" ως κύρια πηγή.
  - **Πλεονεκτήματα:** Υψηλή ανάλυση (273 πάρκα), ενσωματωμένα ICON-EU καιρικά δεδομένα και μοντελοποίηση βασισμένη σε Enercon τουρμπίνες.
- **Εκκαθάριση Φακέλων:** Διαγραφή παλαιών αρχείων ENTSO-E και δημιουργία νέου καταλόγου `data/raw/kassel_dataset/`.

###  Data Loader & Physics Engine 

####  Υλοποιήσεις & Κώδικας:
- **KasselLoader:** Δημιουργία της κλάσης `src/data/kassel_loader.py` για την αυτόματη σάρωση και φόρτωση των δεδομένων.
- **Deduplication Logic:** Προσθήκη φίλτρου `set()` στον Loader, μειώνοντας τα αρχεία από 545 σε **273 μοναδικά πάρκα**.
- **Physics Engine:** Υλοποίηση του νόμου **Power Law Scaling** στο `src/features/physics.py` για την αναγωγή της ταχύτητας ανέμου στο ύψος της πλήμνης.

####  Validation & Testing:
- Επιτυχής φόρτωση δείγματος πάρκου στο Notebook.
- Οπτική επιβεβαίωση της φυσικής μοντελοποίησης (γράφημα Raw vs Hub Height Wind Speed).
- Ολοκλήρωση της δομής του `src` φακέλου για παραγωγικό κώδικα.

---

## [07/02/2026] - Βιβλιογραφική Ανασκόπηση & Μελέτη (State of the Art)

###  Αποφάσεις & Ενέργειες:
- **Στρατηγική Μελέτης:** Πριν την πλήρη υλοποίηση των επόμενων τεχνικών σταδίων, αποφασίστηκε η εμβάθυνση στις σύγχρονες τεχνολογίες Digital Twin μέσω εξειδικευμένης βιβλιογραφίας.
- **Έναρξη Ανάγνωσης:** Ξεκίνησε σήμερα η μελέτη του βιβλίου: *Digital Twin Technology for the Energy Sector: Fundamentals, Advances, Challenges, and Applications* (M. Aghaei et al., 2024).
- **Στόχος:** Η κατανόηση των σύγχρονων μεθοδολογιών υλοποίησης Digital Twins σε αιολικά πάρκα (Κεφάλαιο 8.4) και η βελτίωση των αλγορίθμων πρόβλεψης ενέργειας (Κεφάλαιο 8.3).

---

## [08/02/2026] - Συνέχιση Βιβλιογραφικής Ανασκόπησης & Μελέτης (State of the Art)

###  Πρόοδος Μελέτης:
- **Συνεχιζόμενη Μελέτη:** Περαιτέρω ανάλυση του βιβλίου *Digital Twin Technology for the Energy Sector* (M. Aghaei et al., 2024).
- **Εμβάθυνση:** Εστίαση στις μεθοδολογίες του Κεφαλαίου 8.3 σχετικά με την πρόβλεψη παραγωγής ενέργειας και τη σύνδεσή τους με φυσικά μοντέλα (Physics-Informed approaches).
- **Στόχος:** Η θεωρητική θωράκιση των επόμενων βημάτων της υλοποίησης σύμφωνα με τις τρέχουσες εξελίξεις στον κλάδο.

---

## [09/02/2026] - Βιβλιογραφική Μελέτη & Αναβάθμιση Εργαλείων EDA

###  Πρόοδος Μελέτης:
- **Συνεχιζόμενη Μελέτη:** Περαιτέρω ανάλυση του βιβλίου *Digital Twin Technology for the Energy Sector* (M. Aghaei et al., 2024), με εστίαση στην υλοποίηση Digital Twins ειδικά για αιολικά πάρκα (Κεφάλαιο 8.4).
- **Θεωρητικό Υπόβαθρο:** Κατανόηση των προκλήσεων στη διασύνδεση αισθητήρων και τηλεμετρίας με το ψηφιακό ομοίωμα της τουρμπίνας.

###  Τεχνική Προετοιμασία:
- **Εγκατάσταση Data Wrangler:** Προσθήκη του εργαλείου στο VS Code για την αποτελεσματικότερη διερεύνηση (Exploratory Data Analysis - EDA) των 273 αρχείων CSV του DaKS dataset.
- **Στόχος:** Ο εντοπισμός ανωμαλιών (outliers) και ελλιπών τιμών στα δεδομένα πριν την εκπαίδευση των μοντέλων, σύμφωνα με τις βέλτιστες πρακτικές που περιγράφονται στη βιβλιογραφία.

---

## [10/02/2026] - Βιβλιογραφική Ολοκλήρωση (25 Πηγές) & Στοχοθεσία Δημοσίευσης

### Πρόοδος Μελέτης:
- **Συλλογή SOTA:** Ολοκλήρωση οργάνωσης 25 πηγών (2022-2026) στο NotebookLM με εστίαση σε Energy Prediction και PINNs.
- **Feedback Καθηγητή:** Επικοινωνία με τον κ. Εμεξίδη. Ο στόχος αναβαθμίστηκε σε 35+ πηγές λόγω προοπτικής επιστημονικής δημοσίευσης (publication).
- **Reference Paper:** Επιλογή του *Vogt et al. (2022)* ως βασικού άρθρου αναφοράς για το benchmark των 273 πάρκων στη Γερμανία.

### Τεχνική Προετοιμασία:
- **Στοχοθεσία Baseline:** Στόχος η υπέρβαση του nRMSE (0.125 - 0.196) που επιτεύχθηκε με XGBoost στην αρχική μελέτη.
- **Μοντελοποίηση PINN:** Ανάλυση της υβριδικής Loss Function βάσει των Chinnappan (2025) και Baisthakur (2024).
- **Φυσικοί Περιορισμοί:** Ενσωμάτωση του Power Law Scaling (εκθέτης 0.16-0.22) και του ορίου Betz στη συνάρτηση κόστους.
- **Εξίσωση Loss:** $$L_{total} = L_{data} + \alpha_1L_{efficiency} + \alpha_2L_{cutoff} + \alpha_3L_{sim}$$.


### Επόμενα Βήματα:
- **Επέκταση Βιβλιογραφίας:** Εντοπισμός 10 επιπλέον εξειδικευμένων πηγών για την κάλυψη του στόχου των 35+ άρθρων.
- **Υλοποίηση:** Σχεδιασμός του Physics Engine στο VS Code για την πρόβλεψη ενέργειας (Energy Prediction).

---

## [11/02/2026] - Στρατηγικός Σχεδιασμός & Οριστικοποίηση Ακαδημαϊκής Ταυτότητας

### **Τεχνικός Στόχος:** Σύνθεση της αρχιτεκτονικής Mamba-GNN και ενσωμάτωση των Physics-Informed περιορισμών στο ακαδημαϊκό abstract για υποβολή σε περιοδικό.

### **Πρόοδος Μελέτης:**
* **Source Grounding:** Ολοκληρώθηκε η τροφοδοσία και οργάνωση 39 εξειδικευμένων άρθρων (2022-2026) στο NotebookLM.
* **Αρχιτεκτονική Επιλογή:** Επιβεβαίωση χρήσης **Selective State Space Models (Mamba)** σε συνδυασμό με **Graph Neural Networks (GNN)** για την επίτευξη γραμμικής πολυπλοκότητας $O(L)$ έναντι της τετραγωνικής $O(L^2)$ των Transformers.
* **Οριστικοποίηση Abstract:** Σύνταξη του αγγλικού κειμένου που περιγράφει τη χρήση του **DaKS dataset (273 πάρκα)** και τον στόχο για υπέρβαση του baseline nRMSE (0.125).

### **Τεχνική Προετοιμασία Physics Engine:**
* **Μοντελοποίηση Loss:** Καθορισμός των 5 πυλώνων της υβριδικής συνάρτησης κόστους βάσει των πηγών 08, 09 και 38.
* **Εξίσωση Loss:** $$L_{total} = L_{data} + \alpha_1L_{efficiency} + \alpha_2L_{cutoff} + \alpha_3L_{sim} + \alpha_4L_{dist} + \alpha_5L_{freq}$$

### **Επόμενα Βήματα (Milestones):**
* **Επικοινωνία:** Αποστολή του τίτλου και του abstract στον Καθηγητή κ. Εμεξίδη για έγκριση υποβολής στο περιοδικό.
* **Coding Phase:** Έναρξη υλοποίησης του `physics.py` στην Python (μεταφέρεται λόγω ολοκλήρωσης της θεωρητικής τεκμηρίωσης).
* **Integration:** Σύνδεση του KasselLoader με το Physics Engine για noise-resilient εκπαίδευση.

---

## [12/02/2026] - Υλοποίηση Physics Engine & Προετοιμασία Submission

### **Πρόοδος Submission:**
* **Finalizing Abstract:** Ολοκληρώθηκε η σύνταξη του ακαδημαϊκού abstract και του τίτλου της έρευνας για υποβολή σε περιοδικό.
* **Research Focus:** Επιβεβαίωση της αρχιτεκτονικής **Graph-Mamba PINN** με στόχο την υπέρβαση του baseline nRMSE (0.125).

### **Τεχνική Υλοποίηση Physics Engine:**
* **Physics Module:** Ανάπτυξη του `src/features/physics.py` με ενσωμάτωση των φυσικών περιορισμών.
* **Power Law Scaling:** Υλοποίηση συνάρτησης για την προσαρμογή της ταχύτητας ανέμου στο hub height της τουρμπίνας.
* **Betz Limit Enforcement:** Καθορισμός του $P_{max}$ βάσει του θεωρητικού ορίου απόδοσης (59.3%).
* **Physics Loss Terms:** Προγραμματισμός των όρων $L_{efficiency}$ και $L_{cutoff}$ για την ενίσχυση της ανθεκτικότητας στον θόρυβο (noise resilience).

### **Προετοιμασία Περιβάλλοντος:**
* **Library Setup:** Επιτυχής εγκατάσταση των `torch`, `xgboost`, `lightgbm` και `pyyaml` στο τοπικό περιβάλλον (venv).
* **Environment Note:** Λόγω σφάλματος build-wheel του `mamba-ssm` στα Windows, η εκπαίδευση του χρονικού σκέλους μεταφέρεται στο Google Colab.

### **Εξίσωση Loss Function:**
$$L_{total} = L_{data} + \alpha_1L_{efficiency} + \alpha_2L_{cutoff} + \alpha_3L_{sim} + \alpha_4L_{dist} + \alpha_5L_{freq}$$

---

### **Επόμενα Βήματα (Milestones):**
* **Data Integration:** Σύνδεση του `KasselLoader` με τα raw CSV δεδομένα από τα 273 πάρκα του DaKS dataset.
* **Baseline Execution:** Εκτέλεση και καταγραφή αποτελεσμάτων για τις 5 παραδοσιακές μεθόδους (Linear Regression, Random Forest, XGBoost κ.α.).
* **Commit Reference:** `feat: implement physics engine with power law scaling and Betz limit constraints`.

---

## [13/02/2026] - DaKS Dataset Architecture, Physics Integration & Time-Series Merge

### **Context & Feedback Καθηγητή:**
* **Στόχος:** Διεξοδικός έλεγχος φόρτωσης του DaKS dataset, εντοπισμός outliers και επιβεβαίωση της δομής των δεδομένων.
* **Δράση:** Εκκίνηση Exploratory Data Analysis (EDA) στο `02_kassel_exploration.ipynb`.

### **Τεχνικά Επιτεύγματα (Technical Milestones):**

1. **Αποκρυπτογράφηση Δομής DaKS Dataset:**
   * Επιλύθηκε το ζήτημα των 545 αρχείων: Ανακαλύφθηκε ο διαχωρισμός μεταξύ Μετεωρολογικών Δεδομένων (`data_input_*.csv` με διαχωριστικό `;`) και Μετρήσεων Παραγωγής (`data_target_*.csv` με διαχωριστικό `,`).
   * Αυτοματοποιήθηκε η αντιστοίχιση Inputs/Targets μέσω του μοναδικού Park ID (π.χ., `00011`).

2. **Εφαρμογή Φυσικής Μοντελοποίησης (Physics-Informed Preprocessing):**
   * Υπολογισμός πραγματικής ταχύτητας ανέμου (Wind Magnitude) μέσω των διανυσμάτων U και V ($WS = \sqrt{U^2 + V^2}$).
   * Επιτυχής εφαρμογή του **Power Law Scaling** (`physics.py`) στα raw δεδομένα για την αναγωγή του ανέμου στο ύψος της πλήμνης (Hub Height - 100m). Οπτική επιβεβαίωση (Visual Validation) μέσω διαγραμμάτων.

3. **Ενοποίηση Χρονοσειρών (Time-Series Alignment):**
   * Υλοποίηση `pd.merge()` (Inner Join) για τον απόλυτο χρονικό συγχρονισμό του καιρού (X) με την παραγωγή (y).
   * Επίλυση προβλημάτων μορφοποίησης ημερομηνιών (European Datetime format - `dayfirst=True`) που προκαλούσαν `ValueError`.

4. **Data Insights & Outliers:**
   * Διαπιστώθηκε ότι η παραγωγή ενέργειας (στήλη `pw`) είναι **κανονικοποιημένη [0, 1]**, αντιπροσωπεύοντας το Capacity Factor. Ιδανικό για εκπαίδευση Νευρωνικών Δικτύων.
   * Εντοπίστηκε έτοιμη baseline πρόβλεψη (`icon_eu_daf_pc_baseline`) εντός του dataset, η οποία θα αποτελέσει το benchmark για το μοντέλο.

### **Επόμενα Βήματα (Next Steps):**
* **Refactoring:** Μεταφορά της λογικής φόρτωσης, καθαρισμού και ένωσης (Merge Pipeline) από το Notebook στον αντικειμενοστρεφή `KasselLoader`.
* **Κλιμάκωση (Scaling):** Εφαρμογή του ενοποιημένου Data Pipeline και στα 273 αιολικά πάρκα.

**Commit Reference:** `feat: fix CSV separators, apply Power Law physics, and merge weather inputs with power targets.`

---

## [15/02/2026] - Data Decoding, Unit Scaling & Final Validation

### **Context:**
* **Πρόβλημα:** Κατά τον έλεγχο των ενοποιημένων δεδομένων, παρατηρήθηκαν τιμές ανέμου εκτός φυσικής κλίμακας (π.χ. ~12.000) και κρυπτογραφημένα ονόματα στηλών (π.χ. `ws_hub_100m`).
* **Στόχος:** "Αποκωδικοποίηση" των μονάδων μέτρησης και παραγωγή ενός καθαρού δείγματος για επαλήθευση.

### **Τεχνικά Επιτεύγματα (Technical Milestones):**

1. **Διόρθωση Κλίμακας (Unit Scaling Correction):**
   * Ανακαλύφθηκε ότι το DaKS dataset αποθηκεύει τα δεδομένα πολλαπλασιασμένα επί 1000 (για εξοικονόμηση χώρου/integers).
   * Εφαρμόστηκε διορθωτικός παράγοντας (division by 1000) στις στήλες του ανέμου, επαναφέροντας τις τιμές σε φυσιολογικά επίπεδα (m/s).

2. **Σημασιολογική Μετονομασία (Semantic Renaming):**
   * Μετονομασία των τεχνικών μεταβλητών σε αναγνώσιμη μορφή για ευκολότερη χρήση από το Mamba-GNN:
     * `ws_hub_100m` -> **`Wind_Speed_100m_ms`**
     * `pw` -> **`Power_Output_Normalized`**
     * `icon_eu_daf_pc_baseline` -> **`Baseline_Prediction`**

3. **Εξαγωγή Δείγματος Επαλήθευσης (Validation Artifact):**
   * Δημιουργία και αποθήκευση του αρχείου `park_00011_CLEAN.csv`.
   * **Git Policy:** Το αρχείο `.csv` εξαιρέθηκε από το version control (μέσω `.gitignore`) για να διατηρηθεί το αποθετήριο ελαφρύ, καθώς μπορεί να αναπαραχθεί ανά πάσα στιγμή από τον κώδικα.

### **Επόμενα Βήματα (Next Steps):**
* Ενσωμάτωση της λογικής scaling και renaming στο script `kassel_loader.py`.
* Έναρξη της φάσης εκπαίδευσης (Training Phase) με το καθαρό dataset.

**Commit Reference:** `feat: add data decoding logic (units scaling) and export clean sample for validation`

---

## [16/02/2026] - Robust Loader & Master Dataset EDA

### **Τεχνικά Επιτεύγματα (Technical Milestones):**
1. **Αναβάθμιση KasselLoader (Robustness):**
   * Υλοποίηση **Smart Indexing** για άμεσο εντοπισμό ζευγών αρχείων (Input/Target).
   * Επίλυση του προβλήματος `list index out of range`: Ο Loader πλέον ανιχνεύει αυτόματα τον διαχωριστή (separator) του CSV (είτε `;` είτε `,`).
   * **Αποτέλεσμα:** Επιτυχής φόρτωση για **271 από τα 272 πάρκα (99.6%)**.

2. **Δημιουργία Master Dataset (Big Data):**
   * Μαζική φόρτωση και ενοποίηση όλων των πάρκων σε ένα ενιαίο DataFrame.
   * Συνολικός όγκος δεδομένων: **3.355.233 εγγραφές**.

3. **Εξερευνητική Ανάλυση (EDA) & Καθαρισμός:**
   * **Power Curve Analysis:** Εντοπισμός και αφαίρεση θορύβου (Negative Power, "Magical Power" σε άπνοια).
   * **Time Series Inspection:** Επιβεβαίωση χρονικού συγχρονισμού μεταξύ Μετεωρολογικών Δεδομένων (Input) και Πραγματικής Παραγωγής (Target).
   * Διαπίστωση ότι η διασπορά στο Power Curve οφείλεται στη μεταβλητότητα του πραγματικού ανέμου vs την ομαλότητα του μοντέλου πρόβλεψης.

### **Επόμενα Βήματα (Next Steps):**
* **Feature Engineering:** Δημιουργία νέων μεταβλητών για να βοηθήσουμε το μοντέλο να μάθει τη συμπεριφορά του ανέμου.
* Προετοιμασία Dataset για εκπαίδευση (Train/Test Split).

**Commit Reference:** `docs: completed EDA and power curve analysis`

---

## [17/02/2026] - Επιστημονική Θεμελίωση & Massive Literature Review

### **Βιβλιογραφική Υποδομή (Scientific Haul):**
* **Συγκρότηση Βιβλιοθήκης:** Ολοκλήρωση συλλογής και οργάνωσης 39+ εξειδικευμένων επιστημονικών άρθρων (State-of-the-Art 2022-2026).
* **Κατηγοριοποίηση Πηγών:** Συστηματική ταξινόμηση βάσει έτους, συγγραφέα και τεχνικού αντικειμένου (Scaling, Turbulence, ML Architectures).
* **Θεματολογία Αιχμής:** Η βιβλιογραφία καλύπτει πλέον όλο το φάσμα της έρευνας:
    * **Physics-Guided AI:** Χρήση PINNs και Physics-Constrained μοντέλων.
    * **Advanced Architectures:** Μελέτη Graph Neural Networks (GNN), Transformers και Mamba για πρόβλεψη χρονοσειρών.
    * **Domain Specifics:** Τεκμηρίωση για Wind Shear Exponents, Turbulence Impact και SCADA Anomaly Detection.

### **Τεχνική Ετοιμότητα (Technical Readiness):**
* **Ευθυγράμμιση Κώδικα-Θεωρίας:** Η υλοποιημένη λογική του KasselLoader (Power Law Scaling) είναι πλήρως εναρμονισμένη με τις βέλτιστες πρακτικές της σύγχρονης βιβλιογραφίας.
* **Feature Strategy:** Ο σχεδιασμός των επόμενων βημάτων (Feature Engineering) βασίζεται πλέον σε αποδεδειγμένα μοντέλα χρονικών υστερήσεων (Lags) και ατμοσφαιρικής ευστάθειας.

**Commit Reference:** `docs: finalize massive literature review (39+ papers organized)`

---

### ## [19/02/2026] - Finalizing CI/CD & Documentation
**Εργασίες:**
* **CI/CD Optimization:** Επίλυση του "Exit code 5" στο GitHub Actions μέσω αφαίρεσης του pytest step και καθαρισμού του `requirements.txt` για συμβατότητα με Linux.
* **README Upgrade:** Πλήρης ανασχεδιασμός της τεκμηρίωσης με προσθήκη Build Status Badges, πίνακα τεχνικών προδιαγραφών και οπτικής δομής αποθετηρίου (src-layout).
* **Data Strategy:** Επικαιροποίηση των πηγών δεδομένων με εστίαση στο DaKS dataset και την πλατφόρμα Renewables.ninja.
* **Toolchain Integration:** Σύνδεση του VS Code με το GitHub Actions για άμεσο έλεγχο των workflows.

### ### **Επόμενα Βήματα (Next Steps):**
1.  **Data Acquisition (Renewables.ninja):** Υλοποίηση του script στο notebook `01_data_acquisition.ipynb` για την αυτόματη λήψη ωριαίων δεδομένων αιολικής παραγωγής μέσω API.
2.  **Exploratory Data Analysis (EDA):** Ανάλυση συσχέτισης μεταξύ των δεδομένων ταχύτητας ανέμου του DaKS dataset και της παραγωγής από το Renewables.ninja.
3.  **Feature Engineering:** Δημιουργία χρονικών υστερήσεων (time-lags) και ενσωμάτωση μετεωρολογικών παραμέτρων για την ενίσχυση της προγνωστικής ικανότητας του μοντέλου.
4.  **Baseline Modeling:** Εκπαίδευση ενός απλού μοντέλου (π.χ. Random Forest ή LSTM) για τη δημιουργία ενός μέτρου σύγκρισης πριν την υλοποίηση του Mamba.

**Commit Reference:** `docs: finalized README with structure and data sources`

---

## [20/02/2026] - Feature Engineering Completion & Graph Construction

**Ολοκλήρωση του Notebook 04 με επιτυχή δημιουργία χαρακτηριστικών και κατασκευή χωρικού γράφου για τα 269 αιολικά πάρκα.**

* **Temporal Encoding:** Υλοποίηση κυκλικής κωδικοποίησης (sin/cos) για την ώρα και τον μήνα, επιτρέποντας στο μοντέλο να αντιλαμβάνεται την περιοδικότητα του χρόνου.
* **Lag & Rolling Engineering:** Δημιουργία χρονικών υστερήσεων (1h, 3h, 6h) και κινητών στατιστικών δεικτών (rolling mean/std) για την παροχή «μνήμης» στις Sequential αρχιτεκτονικές (Mamba, Transformers).
* **Spatial Metadata Integration:** Επιτυχής αναζήτηση και ενσωμάτωση πραγματικών γεωγραφικών συντεταγμένων από το αρχείο `meta.csv` μετά από επίλυση προβλημάτων σε separators και mapping.
* **Graph Construction:** Κατασκευή του Adjacency Matrix (269x269) βάσει Ευκλείδειας απόστασης (threshold: 0.5°) και οπτική επαλήθευση της συνδεσιμότητας του δικτύου.
* **Data Export:** Εξαγωγή του τελικού επεξεργασμένου dataset με **1.655.885 δείγματα** και **41 χαρακτηριστικά**, έτοιμο για την εκπαιδευτική διαδικασία.

**Επόμενα Βήματα (Next Steps):**
1. **Notebook 05 - Baseline Modeling:** Διαχωρισμός δεδομένων σε Train/Test (Temporal Split) και εκπαίδευση παραδοσιακών μοντέλων (XGBoost, Random Forest) ως μέτρο σύγκρισης για το Mamba.

**Commit Reference:** `feat: complete feature engineering with 1.6M samples and verified spatial graph (269 nodes)`

---

## ## [21/02/2026] - Statistical Outlier Mitigation & Temporal Data Splitting

* **Z-Score Outlier Detection:** Εφαρμογή στατιστικού ελέγχου Z-score (threshold=3.0) στη στήλη `Power_Output_Normalized`. Εντοπίστηκαν **3.111 ακραίες τιμές** (0.1879% του συνόλου των 1.655.885 δειγμάτων).
* **Outlier Clipping:** Αντικατάσταση των ακραίων τιμών (clipping) στα όρια **[-0.0467, 0.0721]** για τη διατήρηση της συνέχειας της χρονοσειράς χωρίς απώλεια δειγμάτων.
* **Temporal Splitting Strategy:** Αυστηρός χρονικός διαχωρισμός του dataset σε τρία ανεξάρτητα σύνολα:
    * **Train:** 1.244.004 δείγματα (έως 2019-12-31).
    * **Validation:** 329.084 δείγματα (έως 2020-06-30).
    * **Test:** 82.797 δείγματα (από 2020-07-01).
* **Data Integrity Verification:** Επιτυχής έλεγχος για **μηδενικές null τιμές** και στα τρία σύνολα. Επιβεβαίωση απουσίας temporal leakage μέσω `assert` statements.
* **Data Export:** Εξαγωγή των τελικών αρχείων `train_final.csv`, `val_final.csv` και `test_final.csv` στο φάκελο `data/processed/`.

**Επόμενα Βήματα (Next Steps):**
1. **Notebook 06 - Baseline Modeling:** Ανάπτυξη του Persistence Model και Linear Regression ως μέτρα σύγκρισης για την απόδοση του Digital Twin.

**Commit Reference:** `feat: complete phase 05 with professional split and clipping`