#  WindPower_DigitalTwin

![Build Status](https://github.com/Dionysis33/WindPower_DigitalTwin/actions/workflows/python-app.yml/badge.svg)
![License](https://img.shields.io/badge/license-AGPL--v3-green.svg)
![Python](https://img.shields.io/badge/python-3.12-blue.svg)

**Industrial-Grade Digital Twin for Wind Energy Forecasting & Anomaly Detection**

---

##  Σύνοψη Τεχνικών Προδιαγραφών

| Κατηγορία | Περιγραφή |
| :--- | :--- |
| **Engine** | Python 3.12 |
| **Architecture** | Modular src-layout |
| **Patterns** | Factory Design Pattern & Pydantic Data Contracts |
| **CI/CD** | GitHub Actions (Automated Testing & Linting) |
| **License** | AGPL-v3 / Open Source |

---

##  Πηγές Δεδομένων

Το Digital Twin τροφοδοτείται από συνδυασμό ιστορικών και προσομοιωμένων δεδομένων υψηλής πιστότητας:

* **DaKS Dataset:** Χρήση δεδομένων υψηλής ανάλυσης για την κίνηση του ανέμου και την απόδοση ανεμογεννητριών (High-fidelity wind speed & SCADA data).
* **Renewables.ninja:** Χρήση της πλατφόρμας για την παραγωγή ωριαίων χρονοσειρών αιολικής ενέργειας, βασισμένων σε δορυφορικά δεδομένα (MERRA-2) και τεχνικά χαρακτηριστικά ανεμογεννητριών.

---

##  Μεθοδολογία & Εργαλεία

1. **Data Acquisition:** Σύνδεση με το API του Renewables.ninja για λήψη δεδομένων παραγωγής.
2. **Preprocessing:** Καθαρισμός και ευθυγράμμιση των δεδομένων DaKS.
3. **Forecasting:** Ανάπτυξη μοντέλου βασισμένου στην αρχιτεκτονική **Mamba (Selective State Spaces)** για πρόβλεψη παραγωγής σε μεγάλο χρονικό ορίζοντα.

---

##  Δομή Αποθετηρίου

```text
├── data/               # Τοπικά δεδομένα (DaKS, Renewables.ninja exports)
├── notebooks/          # Jupyter Notebooks για EDA & πειραματισμό
├── src/                # Ο βασικός κώδικας του Digital Twin
│   ├── data_loaders/   # Modules για σύνδεση με API (Renewables.ninja)
│   ├── models/         # Υλοποίηση αρχιτεκτονικής Mamba
│   └── utils/          # Βοηθητικές συναρτήσεις
├── .github/workflows/  # CI/CD automation (GitHub Actions)
├── requirements.txt    # Λίστα βιβλιοθηκών
└── LOGS.md             # Ημερολόγιο προόδου

---

##  Εγκατάσταση & Χρήση (Για νέους χρήστες)

1. **Κλωνοποίηση του αποθετηρίου:**
 git clone https://github.com/Dionysis33/WindPower_DigitalTwin.git

---

##  Daily Logs
Η καθημερινή πρόοδος και οι τεχνικές αποφάσεις καταγράφονται αναλυτικά στο: 
 [LOGS.md](./LOGS.md)