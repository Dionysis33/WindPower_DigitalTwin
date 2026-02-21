from pathlib import Path

# Εντοπισμός του κεντρικού φακέλου του project
BASE_DIR = Path(__file__).resolve().parent.parent

# Μονοπάτια για τα δεδομένα (από το προηγούμενο notebook)
DATA_RAW = BASE_DIR / "data" / "raw"
DATA_PROCESSED = BASE_DIR / "data" / "processed"
FINAL_DATASET = DATA_PROCESSED / "final_feature_engineered_dataset.csv"
ADJACENCY_MATRIX = DATA_PROCESSED / "adjacency_matrix.npy"

# Ρυθμίσεις για το Split (Feedback Καθηγητή)
# Ορίζουμε το 2020 ως την περίοδο ελέγχου (Test/Validation)
TRAIN_END_DATE = "2019-12-31 23:00:00"
VAL_END_DATE = "2020-06-30 23:00:00"

# Παράμετροι για Outliers (Feedback Καθηγητή)
Z_SCORE_THRESHOLD = 3.0 # Τυπικές αποκλίσεις για τον εντοπισμό ακραίων τιμών

# Γενικές Ρυθμίσεις
TARGET_COLUMN = "Power_Output_Normalized"
RANDOM_SEED = 42