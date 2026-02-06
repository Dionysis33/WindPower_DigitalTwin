# 🌬️ WindPower_DigitalTwin
> **Industrial-Grade Digital Twin for Wind Energy Forecasting & Anomaly Detection**

---

### 📊 Σύνοψη Τεχνικών Προδιαγραφών
| Κατηγορία | Περιγραφή |
| :--- | :--- |
| **Engine** | Python 3.12 |
| **Architecture** | Modular src-layout (Standard Industry Practice) |
| **Patterns** | Factory Design Pattern & Pydantic Data Contracts |
| **License** | AGPL-v3 / Open Source |

---

## 📝 Περιγραφή Έργου
[cite_start]Το **WindPower_DigitalTwin** αποτελεί μια ολοκληρωμένη προσέγγιση για τη μετάβαση ακαδημαϊκών ερευνών σε λογισμικό επιπέδου παραγωγής[cite: 3, 293]. Το σύστημα έχει σχεδιαστεί για να εκτελεί:
* **Ωριαία Πρόβλεψη Ισχύος** με υψηλή πιστότητα χρησιμοποιώντας το DaKS dataset.
* [cite_start]**Έγκαιρη Ανίχνευση Ανωμαλιών** βασισμένη σε πραγματικά δεδομένα SCADA από το CARE to Compare[cite: 74, 313].

---

## 🏗️ Αρχιτεκτονική Συστήματος
[cite_start]Για τη διασφάλιση της μακροπρόθεσμης συντηρησιμότητας, το έργο υιοθετεί τη δομή **src-layout**, απομονώνοντας τη βασική λογική από τα σενάρια χρήστη.

### ⚙️ Σχεδιαστικά Πρότυπα
* **Factory Design Pattern:** Επιτρέπει τη δυναμική εισαγωγή δεδομένων από πολλαπλές πηγές (Multi-source Strategy) χωρίς αλλαγές στον κεντρικό κώδικα[cite: 16, 305].
* [cite_start]**Pydantic Validation:** Χρήση δηλωτικών σχημάτων για την επιβολή αυστηρών φυσικών περιορισμών (Data Quality Gates)[cite: 47, 340].

### 📊 Διάγραμμα Ροής Δεδομένων
```mermaid
graph LR
    A[Data Sources] --> B{Factory Loader}
    B --> C[Validation Layer]
    C --> D[Digital Twin Core]
    
    style B fill:#f4f4f4,stroke:#333
    style C fill:#e1f5fe,stroke:#01579b