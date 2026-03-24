# PHM Roadmap

## Γιατί χρειάζεται αυτό το roadmap

Το project ξεκίνησε με βασικό άξονα το **wind power forecasting**, αλλά η ερευνητική του κατεύθυνση μπορεί να επεκταθεί φυσικά προς **turbine prognostics and health management (PHM)**.

Αυτό δεν σημαίνει ότι το repository σήμερα είναι ήδη πλήρες PHM system.  
Σημαίνει όμως ότι η παρούσα forecasting pipeline μπορεί να λειτουργήσει ως η επιστημονική βάση για μια πιο health-aware προσέγγιση.

## Current stage

Αυτή τη στιγμή το project βρίσκεται στο στάδιο:

- clean preprocessing,
- feature engineering,
- leakage-aware splitting,
- baseline benchmarking,
- residual diagnostics.

Αυτό είναι το σωστό πρώτο βήμα, γιατί χωρίς αξιόπιστο forecasting backbone δεν μπορεί να στηριχθεί ένα σοβαρό PHM framework.

## Γιατί το forecasting συνδέεται με PHM

Στα wind energy systems, το forecasting error δεν είναι πάντα “τυχαίο”.  
Σε αρκετές περιπτώσεις μπορεί να αντανακλά:

- μεταβολές στη λειτουργική κατάσταση του συστήματος,
- μη αναμενόμενη απόκλιση από τη φυσιολογική power curve,
- αισθητηριακές ή λειτουργικές ανωμαλίες,
- αλλαγές που σχετίζονται με degradation ή abnormal operating regimes.

Άρα, ένα καλά μελετημένο forecasting pipeline μπορεί να προσφέρει:

- **prediction layer**
- και στη συνέχεια **diagnostic / prognostic signal extraction**

## Σταδιακή μετάβαση που ταιριάζει στο παρόν project

### Stage 1 — Forecasting foundation
Τι υπάρχει ήδη:

- καθαρό data pipeline,
- temporal splitting,
- outlier handling,
- baseline models,
- residual analysis.

### Stage 2 — Stronger predictive baselines
Τι ακολουθεί λογικά:

- **Random Forest**
- **XGBoost**
- **MLP**

Ο στόχος εδώ είναι να βελτιωθεί η predictive performance και να χαρτογραφηθεί καλύτερα η non-linear behavior των δεδομένων.

### Stage 3 — Error-aware diagnostics
Μετά τα stronger baselines, μπορεί να προστεθεί συστηματικότερη ανάλυση:

- residuals by wind regime,
- residuals by time-of-day / season,
- extreme error slices,
- uncertainty-aware inspection,
- systematic underprediction / overprediction patterns.

Αυτό είναι το πρώτο ουσιαστικό βήμα προς **diagnostics-oriented forecasting**.

### Stage 4 — Health-oriented interpretation
Σε αυτό το στάδιο, τα residual patterns μπορούν να αντιμετωπιστούν ως πιθανά indicators για:

- anomalous behavior,
- operational drift,
- performance degradation,
- turbine condition awareness.

Εδώ αρχίζει η σύνδεση με **health management**.

### Stage 5 — Advanced models with PHM perspective
Αφού πρώτα χτιστεί σωστό benchmark stack, μπορούν να προστεθούν:

- graph-based models,
- spatio-temporal architectures,
- sequence models,
- ενδεχομένως **Graph Neural Networks**, **Transformers**, ή **Mamba-style** models,

όχι μόνο για καλύτερο forecasting, αλλά και για πλουσιότερη αναπαράσταση λειτουργικής συμπεριφοράς.

## Τι θα άρεσε σε μια ακαδημαϊκή εξέλιξη της πτυχιακής

Για μια πιο ώριμη και επαγγελματική διπλωματική / πτυχιακή πορεία, η πιο ισχυρή αφήγηση είναι:

1. **Ξεκινώ από reproducible forecasting pipeline**
2. **Χτίζω ισχυρά baselines**
3. **Αναλύω residuals και failure modes**
4. **Δείχνω γιατί αυτά σχετίζονται με operational awareness**
5. **Επεκτείνω τη μεθοδολογία προς prognostics / health management**

Αυτή η πορεία είναι πιο πειστική από το να παρουσιαστεί εξαρχής ένα “Digital Twin” χωρίς αρκετή experimental βάση.

## Τι δεν πρέπει να υποσχεθεί το repository ακόμη

Για λόγους ακαδημαϊκής και τεχνικής ακρίβειας, δεν πρέπει ακόμη να διατυπώνεται ότι το project έχει:

- πλήρες PHM engine,
- online fault detection,
- fault classification,
- RUL estimation,
- validated health-state inference.

Αυτά μπορούν να εμφανιστούν ως **future work** ή **research roadmap**, όχι ως ήδη υπάρχον functionality.

## Προτεινόμενη ακαδημαϊκή διατύπωση

Η πιο σωστή διατύπωση για το project σήμερα είναι:

> Το repository αναπτύσσει μια reproducible pipeline για spatio-temporal wind power forecasting στο DaKS dataset, με σχεδιασμό που μπορεί να επεκταθεί προς turbine prognostics and health management μέσω residual analysis, stronger baselines και advanced spatio-temporal modeling.

## Practical next steps

Τα επόμενα ρεαλιστικά βήματα που ταιριάζουν με όσα υπάρχουν ήδη στο repo είναι:

1. Ολοκλήρωση του baseline suite:
   - Random Forest
   - XGBoost
   - MLP

2. Standardized benchmark table για όλα τα models

3. Residual slicing:
   - by wind feature,
   - by hour,
   - by month / season,
   - by target range

4. Σύγκριση linear vs non-linear error structure

5. Προετοιμασία της αφήγησης από forecasting προς PHM / turbine health awareness

## Τελικό μήνυμα

Η σωστή εξέλιξη του project δεν είναι:

> forecasting -> κατευθείαν “έτοιμο Digital Twin”

Η σωστή εξέλιξη είναι:

> reproducible forecasting pipeline -> strong baselines -> residual diagnostics -> anomaly / degradation awareness -> PHM-oriented research direction

Αυτό είναι και πιο επιστημονικά σωστό, και πιο πειστικό για ακαδημαϊκή αξιολόγηση.