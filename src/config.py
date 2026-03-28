from __future__ import annotations

from pathlib import Path


# -------------------------------------------------------------------
# Core project paths
# -------------------------------------------------------------------
# Το BASE_DIR πρέπει να δείχνει στο repository root.
# Η υπόθεση εδώ είναι ότι το αρχείο config.py ζει κάτω από το src/.
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------------------------------------------
# Data directories
# -------------------------------------------------------------------
DATA_DIR = BASE_DIR / "data"
DATA_RAW = DATA_DIR / "raw"
DATA_INTERIM = DATA_DIR / "interim"
DATA_PROCESSED = DATA_DIR / "processed"

# Canonical DaKS raw directory
KASSEL_DATASET_DIR = DATA_RAW / "kassel_dataset"
KASSEL_META_PATH = KASSEL_DATASET_DIR / "meta.csv"

# -------------------------------------------------------------------
# NB02 | Canonical raw-validation artifacts
# -------------------------------------------------------------------
# Αυτά τα artifacts προέρχονται από το 02_kassel_exploration.ipynb
# και αποτελούν την upstream validation contract βάση για τα επόμενα notebooks.
NB02_STRICT_RAW_AUDIT = DATA_PROCESSED / "nb02_strict_raw_audit.csv"
NB02_PAIR_AUDIT = DATA_PROCESSED / "nb02_pair_audit.csv"
NB02_STATUS_COUNTS = DATA_PROCESSED / "nb02_status_counts.csv"
NB02_SEPARATOR_SUMMARY = DATA_PROCESSED / "nb02_separator_summary.csv"
NB02_FAILURE_REASON_SUMMARY = DATA_PROCESSED / "nb02_failure_reason_summary.csv"

# -------------------------------------------------------------------
# NB02 | Coverage-aware downstream eligibility artifacts
# -------------------------------------------------------------------
# Νέα artifacts που ξεχωρίζουν:
# - raw-valid parks
# - coverage classes
# - NB04-eligible parks
#
# Σημαντικό:
# Το NB02 παραμένει canonical raw-validation authority.
# Τα παρακάτω ΔΕΝ αλλάζουν αυτόν τον ρόλο.
# Απλώς επεκτείνουν το downstream contract ώστε το NB03/NB04
# να μην αντιμετωπίζουν όλα τα raw-valid parks ως ισοδύναμα.
NB02_META_COVERAGE_AUDIT = DATA_PROCESSED / "nb02_meta_coverage_audit.csv"
NB02_COVERAGE_CLASS_SUMMARY = DATA_PROCESSED / "nb02_coverage_class_summary.csv"
NB02_NB04_ELIGIBILITY_SUMMARY = DATA_PROCESSED / "nb02_nb04_eligibility_summary.csv"

# -------------------------------------------------------------------
# NB03 / downstream master-EDA artifacts
# -------------------------------------------------------------------
MASTER_DATASET = DATA_PROCESSED / "master_dataset.csv"
MASTER_SCHEMA_SUMMARY = DATA_PROCESSED / "master_schema_summary.csv"
MASTER_PARK_SUMMARY = DATA_PROCESSED / "master_park_summary.csv"
MASTER_ANOMALY_PROFILE = DATA_PROCESSED / "master_anomaly_profile.csv"
MASTER_PARK_LOAD_SUMMARY = DATA_PROCESSED / "master_park_load_summary.csv"

# -------------------------------------------------------------------
# NB04+ downstream feature / graph artifacts
# -------------------------------------------------------------------
FINAL_DATASET = DATA_PROCESSED / "final_feature_engineered_dataset.csv"
ADJACENCY_MATRIX = DATA_PROCESSED / "adjacency_matrix.npy"

# -------------------------------------------------------------------
# Canonical split boundaries
# -------------------------------------------------------------------
# Προσοχή:
# - Το split εδώ παραμένει όπως είναι ήδη στο current repository.
# - Δεν το αλλάζουμε σε αυτό το patch, γιατί αυτό είναι broader protocol θέμα
#   και όχι απλή config synchronization αλλαγή.
# - Οι ημερομηνίες αυτές χρησιμοποιούνται downstream στα NB05+ stages.
TRAIN_END_DATE = "2019-12-31 23:00:00"
VAL_END_DATE = "2020-06-30 23:00:00"

# -------------------------------------------------------------------
# General project settings
# -------------------------------------------------------------------
TARGET_COLUMN = "Power_Output_Normalized"
BASELINE_COLUMN = "Baseline_Prediction"
PARK_ID_COLUMN = "park_id"
TIMESTAMP_COLUMN = "timestamp"

# Threshold για outlier handling στο NB05
Z_SCORE_THRESHOLD = 3.0

# Reproducibility
RANDOM_SEED = 42