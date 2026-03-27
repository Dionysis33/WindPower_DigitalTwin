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

---

## [22/02/2026] - Baseline Modeling & Performance Benchmarking

* **Persistence Model (Naive Forecast):** Υλοποίηση του μοντέλου αναφοράς με την παραδοχή ότι η ισχύς τη στιγμή t+1 θα είναι ίδια με τη στιγμή t. Χρησιμοποιήθηκε ως το ελάχιστο κριτήριο αποδοχής για την αξιολόγηση των επόμενων μοντέλων.
* **Linear Regression Training:** Εκπαίδευση γραμμικού μοντέλου παλινδρόμησης χρησιμοποιώντας αριθμητικά χαρακτηριστικά: NWP forecasts, lag features (1h, 3h, 6h), και rolling statistics.
* **Feature Engineering & Robustness:** Επιτυχής διαχείριση σφαλμάτων τύπου ValueError μέσω αυτόματου φιλτραρίσματος των μη-αριθμητικών στηλών (timestamps) κατά τη διαδικασία της εκπαίδευσης.
* **Comparative Performance Evaluation:** Αξιολόγηση των μοντέλων στο Test Set (82.796 δείγματα):
    * **Persistence:** MAE = 0.013840, RMSE = 0.019180, R-squared = -0.7967.
    * **Linear Regression:** MAE = 0.008278, RMSE = 0.010841, R-squared = 0.4259.
* **Performance Insight:** Το Linear Regression πέτυχε μείωση σφάλματος (MAE) κατά περίπου **40%** σε σχέση με το Persistence, επιβεβαιώνοντας την προγνωστική ισχύ των καιρικών δεδομένων.
* **Data Export:** Αποθήκευση των τελικών metrics στο αρχείο `baseline_metrics.csv` για τη σύγκριση με τα επερχόμενα μοντέλα Deep Learning.

**Επόμενα Βήματα (Next Steps - Notebook 06):**
1. **Residual Analysis:** Ανάλυση των σφαλμάτων του Linear Regression για τον εντοπισμό μοτίβων (π.χ. μεγαλύτερα σφάλματα σε υψηλές ταχύτητες ανέμου).
2. **Visualization:** Δημιουργία συγκριτικών γραφημάτων (Actual vs Predicted) για επιλεγμένα χρονικά παράθυρα του Test Set.

**Commit Reference:** `feat: implement persistence and linear regression baselines`

---

## [23/02/2026] - Finalizing Notebook 06 & Error Diagnostics

### Ολοκληρωμένες Ενέργειες:
1. **Residual Analysis & Diagnostics:**
   - Πραγματοποιήθηκε αναλυτικός έλεγχος των καταλοίπων (residuals) του Linear Regression.
   - Δημιουργήθηκε γράφημα συσχέτισης σφάλματος και ταχύτητας ανέμου (Residuals vs Wind Speed).
   - **Εύρημα:** Το σφάλμα (MAE) παρουσιάζει κορύφωση στις μεσαίες ταχύτητες ανέμου (8-12 m/s), επιβεβαιώνοντας τη μη-γραμμική φύση της καμπύλης ισχύος.

2. **Προηγμένη Οπτικοποίηση:**
   - Υλοποίηση Distribution Plot για τα σφάλματα (Normal Distribution check).
   - Δημιουργία Actual vs Predicted Scatter Plot με γραμμή ταυτότητας (identity line) για τον εντοπισμό αποκλίσεων.

3. **Στρατηγική Κλιμάκωσης (Baselines):**
   - Επαναπροσδιορισμός της στρατηγικής για το Notebook 07. Αντί για άμεση μετάβαση σε SOTA μοντέλα, αποφασίστηκε η συμπλήρωση μιας **"ισχυρής πεντάδας" (5 Baselines)**:
     - *Persistence* (Ολοκληρώθηκε)
     - *Linear Regression* (Ολοκληρώθηκε)
     - *Random Forest* (Εκκρεμεί)
     - *XGBoost* (Εκκρεμεί)
     - *Simple MLP* (Εκκρεμεί)

### Τελικά Metrics (Notebook 06):
- **Linear Regression:** MAE: 0.008278, R²: 0.4259.
- **Βελτίωση:** ~40% έναντι του Persistence (MAE: 0.013840).

**Commit Reference:** `feat: complete notebook 06 with error analysis and 5-baseline strategy`


---

## [24/02/2026] - CI/CD Optimization & Environment Harmonization

### **Τεχνικά Επιτεύγματα (Technical Milestones):**

1.  **Επίλυση Συγκρούσεων GitHub Actions (CI/CD Debugging):**
    * Εντοπισμός και διόρθωση του σφάλματος **"Checks have failed"** που οφειλόταν σε αναντιστοιχία εκδόσεων Python (3.10 στον server έναντι 3.12 τοπικά).
    * Αναβάθμιση του αρχείου ρυθμίσεων `.github/workflows/python-app.yml` στην έκδοση **Python 3.12** για πλήρη συμβατότητα με τις σύγχρονες βιβλιοθήκες του project.

2.  **Εξορθολογισμός Εξαρτήσεων (Requirements Cleanup):**
    * Εντοπισμός ασυμβατότητας της βιβλιοθήκης `pywinpty` με το περιβάλλον Linux των GitHub Runners.
    * Αφαίρεση του πακέτου `pywinpty` από το `requirements.txt`, καθώς αποτελεί εξάρτηση αποκλειστικά για Windows και δεν επηρεάζει τη λειτουργία του μοντέλου.
    * **Αποτέλεσμα:** Επιτυχής ολοκλήρωση του build (**Green Checkmark**) στο GitHub για το commit `48d9947`.

3.  **Ετοιμότητα Deep Learning Stack:**
    * Επιβεβαίωση εγκατάστασης του **`torch-geometric==2.7.0`** στο τοπικό περιβάλλον και συγχρονισμός με το απομακρυσμένο repository.
    * Προετοιμασία του workflow για την εισαγωγή των **Graph Neural Networks (GNN)** και της αρχιτεκτονικής **Mamba** βάσει της βιβλιογραφίας (Martin 2024, Hong 2025).

### **Επόμενα Βήματα (Next Steps):**
* **Notebook 08 - Graph Construction:** Μετατροπή του Adjacency Matrix σε μορφή `edge_index` (Sparse format).
* **Data Preparation:** Κατασκευή των Graph Data Objects (Nodes, Edges, Features) για τα 271 αιολικά πάρκα.

**Commit Reference:** `fix: remove windows-specific package pywinpty from requirements`

---

## [10/03/2026] - Data Synchronization & Baseline Consolidation

### **Τεχνικά Επιτεύγματα (Technical Milestones):**

1. **Οριστική Ευθυγράμμιση Γράφου & Δεδομένων (Notebook 04):**
    * **Node Alignment:** Επίλυση του κρίσιμου προβλήματος αναντιστοιχίας (mismatch) μεταξύ του Adjacency Matrix και του Master Dataset.
    * **Categorical Sorting:** Εφαρμογή εξαναγκασμένης ταξινόμησης στα **269 αιολικά πάρκα**. Διασφαλίστηκε ότι η σειρά των κόμβων στον γράφο ταυτίζεται απόλυτα με τη σειρά των δειγμάτων στον πίνακα χαρακτηριστικών $X \in \mathbb{R}^{N \times F}$.
    * **Verification:** Επιτυχής έλεγχος (Success Flag) που επιβεβαιώνει τον συγχρονισμό των IDs πριν την παραγωγή του `.npy` αρχείου.


2. **Ολοκλήρωση Advanced Baselines & UI Fixes (Notebook 07):**
    * **Benchmarking:** Εκπαίδευση μοντέλων **XGBoost** και **MLP**, θέτοντας το State-of-the-Art benchmark στο **$R^2 \approx 0.61$**.
    * **Optimization:** Εφαρμογή **Random Sampling (20%)** για τη σταθεροποίηση της εκτέλεσης και την αποφυγή Memory Overflow (RAM usage optimization).
    * **Visualization Clean-up:** Διόρθωση των `Seaborn FutureWarnings` μέσω ορθού ορισμού των παραμέτρων `hue` και `palette`, εξασφαλίζοντας "καθαρό" output στο GitHub.

3. **Διαχείριση Version Control:**
    * Επιτυχές Push των κρίσιμων διορθώσεων (Commit: `9351bdf`).
    * Πλήρης συγχρονισμός του τοπικού περιβάλλοντος με το απομακρυσμένο repository για τα Notebooks 04 έως 07.

---

### **Επόμενα Βήματα (Next Steps):**
* **Notebook 08 - GNN Implementation:** Εκκίνηση της αρχιτεκτονικής **Graph Convolutional Network (GCN)** χρησιμοποιώντας τη βιβλιοθήκη `PyTorch Geometric`.
* **Sparse Matrix Conversion:** Μετατροπή του Adjacency Matrix σε μορφή `edge_index` (COO format).
* **Graph Data Loader:** Κατασκευή του custom Dataset object που θα τροφοδοτεί το μοντέλο με την πληροφορία των 269 κόμβων ανά χρονική στιγμή.

**Commit Reference:** `fix: ensure strict park ID alignment and graph consistency in NB04`


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