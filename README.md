# WindPower_DigitalTwin
## Συγκριτική Αξιολόγηση Μοντέλων Μηχανικής Μάθησης για Πρόβλεψη και Ανίχνευση Ανωμαλιών

---

### ### Περιγραφή Έργου
Ανάπτυξη ενός **Ψηφιακού Διδύμου (Digital Twin)** για αιολικά συστήματα, με στόχο την ωριαία πρόβλεψη ισχύος και την έγκαιρη ανίχνευση λειτουργικών ανωμαλιών. 

### ### Τεχνολογικό Stack & Εργαλεία
- **Γλώσσα:** `Python 3.12`.
- **Βιβλιοθήκες:** `pandas`, `scikit-learn`, `XGBoost`, `PyTorch/TensorFlow`.
- **Εργαλεία Ανάπτυξης:** - `VS Code`: Τοπική ανάπτυξη, modular coding και feature engineering.
    - `Google Colab`: Εκπαίδευση μοντέλων βαθιάς μάθησης (LSTM/CNN) με χρήση GPU.
    - `MLflow`: Καταγραφή πειραμάτων και σύγκριση metrics.
    - `Streamlit`: Δημιουργία διαδραστικού dashboard για το Digital Twin.

---

### ### Δομή Έργου (Project Structure)
- `data/` : Διαχωρισμός σε `raw/`, `interim/` και `processed/`.
- `notebooks/` : Jupyter Notebooks για τη ροή εργασίας.
- `src/` : Modular κώδικας (`data_loader.py`, `features.py`).
- `models/` : Αποθηκευμένα μοντέλα και logs.

---

### ### Πηγές Δεδομένων (Updated Strategy)
1. **University of Kassel (DaKS):** Κύρια πηγή για το Digital Twin. Περιλαμβάνει δεδομένα από 273 τοποθεσίες με χαρακτηριστικά ανεμογεννητριών Enercon και μετεωρολογικά δεδομένα ICON-EU.
2. **CARE to Compare (Fraunhofer IEE):** Benchmark dataset για την εκπαίδευση του μοντέλου στην ανίχνευση ανωμαλιών (Anomaly Detection).
3. **Renewables.ninja:** Χρησιμοποιείται ως εργαλείο εξωτερικής επαλήθευσης (Validation) για συγκεκριμένα case studies.