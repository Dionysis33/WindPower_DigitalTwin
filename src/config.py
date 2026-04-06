from __future__ import annotations

from pathlib import Path


# -------------------------------------------------------------------
# Core project paths
# -------------------------------------------------------------------
# Το BASE_DIR πρέπει να δείχνει στο repository root.
# Η υπόθεση εδώ είναι ότι το config.py ζει κάτω από το src/.
BASE_DIR = Path(__file__).resolve().parent.parent


# -------------------------------------------------------------------
# Data directories
# -------------------------------------------------------------------
DATA_DIR = BASE_DIR / "data"
DATA_RAW = DATA_DIR / "raw"
DATA_INTERIM = DATA_DIR / "interim"
DATA_PROCESSED = DATA_DIR / "processed"


# -------------------------------------------------------------------
# Canonical DaKS raw directory
# -------------------------------------------------------------------
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
# NB03 | Validated-only master EDA artifacts
# -------------------------------------------------------------------
MASTER_DATASET = DATA_PROCESSED / "master_dataset.csv"
MASTER_SCHEMA_SUMMARY = DATA_PROCESSED / "master_schema_summary.csv"
MASTER_PARK_SUMMARY = DATA_PROCESSED / "master_park_summary.csv"
MASTER_ANOMALY_PROFILE = DATA_PROCESSED / "master_anomaly_profile.csv"
MASTER_PARK_LOAD_SUMMARY = DATA_PROCESSED / "master_park_load_summary.csv"


# -------------------------------------------------------------------
# NB04 | Canonical feature-engineering / graph artifacts
# -------------------------------------------------------------------
FINAL_DATASET = DATA_PROCESSED / "final_feature_engineered_dataset.csv"
ADJACENCY_MATRIX = DATA_PROCESSED / "adjacency_matrix.npy"
GRAPH_NODE_ORDER_PATH = DATA_PROCESSED / "graph_node_order.csv"
GRAPH_EDGE_INDEX_PATH = DATA_PROCESSED / "graph_edge_index.npy"
GRAPH_DISTANCE_MATRIX_PATH = DATA_PROCESSED / "graph_distance_matrix_km.npy"


# -------------------------------------------------------------------
# NB05 | Canonical split artifacts
# -------------------------------------------------------------------
TRAIN_FINAL_PATH = DATA_PROCESSED / "train_final.csv"
VAL_FINAL_PATH = DATA_PROCESSED / "val_final.csv"
TEST_FINAL_PATH = DATA_PROCESSED / "test_final.csv"


# -------------------------------------------------------------------
# NB06 / NB07 | Canonical benchmark / prediction handoff artifacts
# -------------------------------------------------------------------
BASELINE_METRICS_PATH = DATA_PROCESSED / "baseline_metrics.csv"
NB06_TEST_PREDICTIONS_PATH = DATA_PROCESSED / "nb06_test_predictions.csv"
NB07_PREDICTIONS_DIR = DATA_PROCESSED / "predictions"
NB07_ALL_TEST_PREDICTIONS_LONG = NB07_PREDICTIONS_DIR / "nb07_all_test_predictions_long.csv"


# -------------------------------------------------------------------
# NB08 | Diagnostics artifacts
# -------------------------------------------------------------------
DIAGNOSTICS_DIR = DATA_PROCESSED / "diagnostics"

NB08_WIND_REGIME_METRICS = DIAGNOSTICS_DIR / "nb08_wind_regime_metrics.csv"
NB08_POWER_REGIME_METRICS = DIAGNOSTICS_DIR / "nb08_power_regime_metrics.csv"
NB08_TIME_BLOCK_METRICS = DIAGNOSTICS_DIR / "nb08_time_block_metrics.csv"
NB08_BEST_MODEL_BY_WIND_REGIME = DIAGNOSTICS_DIR / "nb08_best_model_by_wind_regime.csv"
NB08_BEST_MODEL_BY_POWER_REGIME = DIAGNOSTICS_DIR / "nb08_best_model_by_power_regime.csv"
NB08_ERROR_DISTRIBUTION_OVERVIEW = DIAGNOSTICS_DIR / "nb08_error_distribution_overview.csv"
NB08_ERROR_PERCENTILES = DIAGNOSTICS_DIR / "nb08_error_percentiles.csv"
NB08_RELATIVE_GAIN_VS_REFERENCES = DIAGNOSTICS_DIR / "nb08_relative_gain_vs_references.csv"
NB08_ROWWISE_BEST_MODEL_FREQUENCY = DIAGNOSTICS_DIR / "nb08_rowwise_best_model_frequency.csv"
NB08_HARD_ROW_REGIME_DISTRIBUTION = DIAGNOSTICS_DIR / "nb08_hard_row_regime_distribution.csv"
NB08_REGIME_SUPPORT_AUDIT = DIAGNOSTICS_DIR / "nb08_regime_support_audit.csv"
NB08_EXPORT_MANIFEST = DIAGNOSTICS_DIR / "nb08_export_manifest.csv"


# -------------------------------------------------------------------
# NB09 | Park-level diagnostics artifacts
# -------------------------------------------------------------------
NB09_PARK_LEVEL_DIR = DIAGNOSTICS_DIR / "nb09_park_level"


# -------------------------------------------------------------------
# NB10 | Graph-readiness verification artifacts
# -------------------------------------------------------------------
NB10_NODE_INDEX_MAP = DATA_PROCESSED / "nb10_node_index_map.csv"
NB10_FEATURE_ROLE_MANIFEST = DATA_PROCESSED / "nb10_feature_role_manifest.csv"
NB10_SPLIT_GRAPH_CONTRACT_SUMMARY = DATA_PROCESSED / "nb10_split_graph_contract_summary.csv"
NB10_ARTIFACT_STATUS_MANIFEST = DATA_PROCESSED / "nb10_artifact_status_manifest.csv"
NB10_GRAPH_ARTIFACT_SUMMARY = DATA_PROCESSED / "nb10_graph_artifact_summary.csv"
NB10_COHORT_CONTRACT_SUMMARY = DATA_PROCESSED / "nb10_cohort_contract_summary.csv"
NB10_DISTANCE_MATRIX_SUMMARY = DATA_PROCESSED / "nb10_distance_matrix_summary.csv"
NB10_UPSTREAM_AUDIT_NOTES = DATA_PROCESSED / "nb10_upstream_audit_notes.csv"


# -------------------------------------------------------------------
# NB11 | Graph-model input packaging exports
# -------------------------------------------------------------------
# Το NB11 είναι packaging-only stage:
# - δεν αλλάζει benchmark reporting
# - δεν κάνει training
# - δεν ξανακάνει raw validation
NB11_EXPORT_DIR = DATA_PROCESSED / "graph_packaging"

NB11_FEATURE_ROLE_MANIFEST = NB11_EXPORT_DIR / "nb11_feature_role_manifest.csv"
NB11_NODE_FEATURE_MANIFEST = NB11_EXPORT_DIR / "nb11_node_feature_manifest.csv"
NB11_SPLIT_GRAPH_PACKAGING_SUMMARY = NB11_EXPORT_DIR / "nb11_split_graph_packaging_summary.csv"
NB11_PACKAGING_STATUS_MANIFEST = NB11_EXPORT_DIR / "nb11_packaging_status_manifest.csv"

NB11_TRAIN_GRAPH_DATASET = NB11_EXPORT_DIR / "train_graph_dataset.pt"
NB11_VAL_GRAPH_DATASET = NB11_EXPORT_DIR / "val_graph_dataset.pt"
NB11_TEST_GRAPH_DATASET = NB11_EXPORT_DIR / "test_graph_dataset.pt"
NB11_PREVIEW_PYG_OBJECTS = NB11_EXPORT_DIR / "nb11_preview_pyg_objects.pt"


# -------------------------------------------------------------------
# Canonical split boundaries
# -------------------------------------------------------------------
# Προσοχή:
# - Το split εδώ παραμένει όπως είναι ήδη στο current repository.
# - Δεν το αλλάζουμε εδώ, γιατί αυτό θα ήταν broader protocol θέμα
#   και όχι απλό config synchronization patch.
TRAIN_END_DATE = "2019-12-31 23:00:00"
VAL_END_DATE = "2020-06-30 23:00:00"


# -------------------------------------------------------------------
# General project settings
# -------------------------------------------------------------------
TARGET_COLUMN = "Power_Output_Normalized"
BASELINE_COLUMN = "Baseline_Prediction"
PARK_ID_COLUMN = "park_id"
TIMESTAMP_COLUMN = "timestamp"
TEST_FLAG_COLUMN = "test_flag"


# -------------------------------------------------------------------
# NB05 | Outlier handling
# -------------------------------------------------------------------
Z_SCORE_THRESHOLD = 3.0


# -------------------------------------------------------------------
# Reproducibility
# -------------------------------------------------------------------
RANDOM_SEED = 42