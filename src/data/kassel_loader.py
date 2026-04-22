from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd

from src.features.physics import apply_power_law_scaling


class KasselLoader:
    """
    Operational loader για downstream χρήση του DaKS / Kassel dataset.

    Σημαντική μεθοδολογική σημείωση:
    - Το NB02 παραμένει η canonical raw validation authority.
    - Ο παρών loader λειτουργεί μόνο ως operational helper.
    - Δεν πρέπει να χρησιμοποιείται ως υποκατάστατο του NB02 για raw integrity validation.
    """

    # Επιτρεπτό filename pattern για per-park raw files.
    PAIR_PATTERN = re.compile(r"^data_(input|target)_(\d+)\.csv$", re.IGNORECASE)

    # Strict input-side observed formats από τα raw samples.
    INPUT_TS_FORMATS = [
        "%d/%m/%Y %H:%M",      # π.χ. 8/12/2018 0:00
        "%Y-%m-%d %H:%M:%S",   # π.χ. 2018-12-08 00:00:00
    ]

    # Strict target-side canonical ISO format.
    TARGET_TS_FORMATS = [
        "%Y-%m-%d %H:%M:%S",
    ]

    def __init__(self, raw_data_path: str | Path):
        self.raw_data_path = Path(raw_data_path).resolve()

        if not self.raw_data_path.exists():
            raise FileNotFoundError(f"Δεν βρέθηκε raw data directory: {self.raw_data_path}")

        self.all_csv_files = sorted(self.raw_data_path.glob("*.csv"))
        self.meta_path = self.raw_data_path / "meta.csv"
        self.park_index = self._build_park_index()

        print(
            "KasselLoader initialized: "
            f"{len(self.park_index)} πλήρως ή μερικώς καταλογογραφημένα park IDs."
        )

    # ------------------------------------------------------------------
    # File discovery / indexing
    # ------------------------------------------------------------------
    def _build_park_index(self) -> dict[str, dict[str, Path | None]]:
        """
        Δημιουργεί strict input-target index ανά park_id.

        Κρίσιμη λεπτομέρεια:
        - το meta.csv εξαιρείται ρητά
        - μόνο αρχεία που ταιριάζουν στο pair pattern συμμετέχουν στο index
        """
        park_index: dict[str, dict[str, Path | None]] = {}

        for file_path in self.all_csv_files:
            file_name = file_path.name

            # Το meta.csv είναι auxiliary metadata file και όχι park pair file.
            if file_name.lower() == "meta.csv":
                continue

            match = self.PAIR_PATTERN.match(file_name)
            if not match:
                continue

            file_type, park_id = match.groups()
            park_id = str(park_id).zfill(5)

            if park_id not in park_index:
                park_index[park_id] = {"input": None, "target": None}

            if file_type.lower() == "input":
                park_index[park_id]["input"] = file_path
            else:
                park_index[park_id]["target"] = file_path

        return park_index

    def get_available_parks(self) -> list[str]:
        """
        Επιστρέφει μόνο parks που έχουν και input και target file.
        """
        valid_parks = []
        for park_id, files in self.park_index.items():
            if files["input"] is not None and files["target"] is not None:
                valid_parks.append(park_id)

        return sorted(valid_parks)

    # ------------------------------------------------------------------
    # CSV decoding helpers
    # ------------------------------------------------------------------
    def _choose_separator(self, file_path: Path, file_type: str) -> tuple[pd.DataFrame, str]:
        """
        Επιλέγει separator με deterministic scoring.

        Δεν χρησιμοποιούμε αδιαφανές auto-sniffing.
        Θέλουμε reproducible και ελεγχόμενη συμπεριφορά.
        """
        separator_candidates = [";", ","]
        time_candidates = {"fcst_time", "time", "timestamp"}

        if file_type == "input":
            value_candidates = {"nwp_fcst_horiz_hours", "U_GVL_58_HL", "U_GVL_60_HL"}
            expected_sep = ";"
        else:
            value_candidates = {"pw", "icon_eu_daf_pc_baseline", "test_flag"}
            expected_sep = ","

        scored_reads = []

        for sep in separator_candidates:
            df = pd.read_csv(file_path, sep=sep)
            df.columns = [str(col).strip() for col in df.columns]

            score = 0
            score += len(df.columns)
            score += 50 if any(col in df.columns for col in time_candidates) else 0
            score += 10 if any(col in df.columns for col in value_candidates) else 0
            score += 1 if sep == expected_sep else 0

            # Μία μόνο στήλη σημαίνει σχεδόν σίγουρα λάθος separator.
            if len(df.columns) == 1:
                score -= 100

            scored_reads.append((score, sep, df))

        scored_reads.sort(key=lambda x: x[0], reverse=True)
        _, best_sep, best_df = scored_reads[0]

        if len(best_df.columns) == 1:
            raise ValueError(
                f"Separator detection failed for {file_path.name}. "
                "All candidate parses remained degenerate."
            )

        return best_df, best_sep

    def _get_time_column(self, df: pd.DataFrame, file_type: str, file_name: str) -> str:
        """
        Εντοπίζει temporal column με explicit candidate order.
        """
        if file_type == "input":
            candidates = ["fcst_time", "time", "timestamp"]
        else:
            candidates = ["time", "timestamp", "fcst_time"]

        for col in candidates:
            if col in df.columns:
                return col

        raise KeyError(
            f"No timestamp column found in {file_name}. "
            f"Available columns={df.columns.tolist()}"
        )

    def _parse_timestamp_strict(
        self,
        series: pd.Series,
        allowed_formats: Iterable[str],
        field_name: str,
    ) -> tuple[pd.Series, str]:
        """
        Κάνει strict datetime parsing χωρίς:
        - errors='coerce'
        - dayfirst heuristics
        - format='mixed'

        Αν ένα format δεν ταιριάζει σε όλη τη σειρά, απορρίπτεται.
        """
        raw_str = series.astype("string").str.strip()
        empty_mask = raw_str.isna() | (raw_str == "")

        last_error = None

        for fmt in allowed_formats:
            try:
                parsed = pd.to_datetime(
                    raw_str.mask(empty_mask),
                    format=fmt,
                    errors="raise",
                )
                return parsed, fmt
            except Exception as exc:
                last_error = exc

        sample_value = raw_str[~empty_mask].iloc[0] if (~empty_mask).any() else "<empty>"

        raise ValueError(
            f"Strict timestamp parsing failed for {field_name}. "
            f"Sample='{sample_value}' | Allowed formats={list(allowed_formats)} | Last error={last_error}"
        )

    # ------------------------------------------------------------------
    # Unit normalization / wind helpers
    # ------------------------------------------------------------------
    def _requires_divide_by_1000(self, df_in: pd.DataFrame) -> bool:
        """
        Εντοπίζει αν το input file φαίνεται να είναι αποθηκευμένο σε milli-style scale.

        Παρατήρηση από τα raw samples:
        - κάποια parks έχουν φυσικές τιμές π.χ. 9.682 m/s, 278.698 K
        - άλλα έχουν integer-like τιμές π.χ. 11219, 277105
        """
        probe_cols = [
            col for col in [
                "T_HAG_2_M",
                "RELHUM_HAG_2_M",
                "PS_SFC_0_M",
                "U_GVL_58_HL",
                "V_GVL_58_HL",
                "U_GVL_60_HL",
                "V_GVL_60_HL",
            ]
            if col in df_in.columns
        ]

        if not probe_cols:
            return False

        median_abs_values = {}
        for col in probe_cols:
            numeric = pd.to_numeric(df_in[col], errors="coerce")
            if numeric.notna().any():
                median_abs_values[col] = float(np.nanmedian(np.abs(numeric.to_numpy())))

        if not median_abs_values:
            return False

        return (
            median_abs_values.get("U_GVL_58_HL", 0.0) > 100
            or median_abs_values.get("V_GVL_58_HL", 0.0) > 100
            or median_abs_values.get("U_GVL_60_HL", 0.0) > 100
            or median_abs_values.get("V_GVL_60_HL", 0.0) > 100
            or median_abs_values.get("T_HAG_2_M", 0.0) > 1000
            or median_abs_values.get("RELHUM_HAG_2_M", 0.0) > 1000
            or median_abs_values.get("PS_SFC_0_M", 0.0) > 1_000_000
        )

    def _normalize_input_units(self, df_in: pd.DataFrame) -> tuple[pd.DataFrame, bool]:
        """
        Κανονικοποιεί meteorological input units όταν ανιχνεύεται milli-style storage.

        Δεν πειράζουμε:
        - το nwp_fcst_horiz_hours
        - τις raw string timestamp στήλες
        """
        out = df_in.copy()
        divide_by_1000 = self._requires_divide_by_1000(out)

        if not divide_by_1000:
            return out, False

        numeric_cols = out.select_dtypes(include=[np.number]).columns.tolist()
        cols_to_skip = {"nwp_fcst_horiz_hours"}
        cols_to_scale = [col for col in numeric_cols if col not in cols_to_skip]

        out[cols_to_scale] = out[cols_to_scale] / 1000.0
        return out, True

    def _build_wind_features(self, df_in: pd.DataFrame) -> pd.DataFrame:
        """
        Ανακατασκευάζει wind magnitude από U/V components και εφαρμόζει Power Law scaling.

        Προτιμάμε το 58_HL ως πιο κοντινό 100m-level field.
        Αν δεν υπάρχει, πέφτουμε στο 60_HL.
        """
        out = df_in.copy()

        candidate_pairs = [
            ("U_GVL_58_HL", "V_GVL_58_HL", 58),
            ("U_GVL_60_HL", "V_GVL_60_HL", 60),
        ]

        selected_pair = None
        for u_col, v_col, h_ref in candidate_pairs:
            if u_col in out.columns and v_col in out.columns:
                selected_pair = (u_col, v_col, h_ref)
                break

        if selected_pair is None:
            raise KeyError(
                "Could not locate a valid U/V wind component pair in the input dataframe."
            )

        u_col, v_col, h_ref = selected_pair

        out["ws_ref"] = np.sqrt(out[u_col] ** 2 + out[v_col] ** 2)
        out["Wind_Speed_100m_ms"] = apply_power_law_scaling(
            v_ref=out["ws_ref"],
            h_ref=h_ref,
            h_hub=100,
            alpha=0.143,
        )

        return out

    # ------------------------------------------------------------------
    # Main public API
    # ------------------------------------------------------------------
    def load_park_data(self, park_id: str) -> pd.DataFrame | None:
        """
        Φορτώνει ένα πλήρες park-level dataframe.

        Κρίσιμες αρχές:
        - strict separator handling
        - strict timestamp parsing
        - target-side ISO timestamp ως canonical downstream backbone
        - no loose pd.to_datetime(..., format='mixed', dayfirst=True)
        """
        park_id = str(park_id).zfill(5)

        if park_id not in self.park_index:
            return None

        files = self.park_index[park_id]
        if files["input"] is None or files["target"] is None:
            return None

        # --------------------------------------------------------------
        # 1. Decode INPUT / TARGET
        # --------------------------------------------------------------
        df_in, input_sep = self._choose_separator(files["input"], file_type="input")
        df_out, target_sep = self._choose_separator(files["target"], file_type="target")

        input_time_col = self._get_time_column(df_in, file_type="input", file_name=files["input"].name)
        target_time_col = self._get_time_column(df_out, file_type="target", file_name=files["target"].name)

        # --------------------------------------------------------------
        # 2. Strict timestamp parsing
        # --------------------------------------------------------------
        parsed_input_ts, input_ts_format = self._parse_timestamp_strict(
            df_in[input_time_col],
            self.INPUT_TS_FORMATS,
            field_name=f"{files['input'].name}:{input_time_col}",
        )
        parsed_target_ts, target_ts_format = self._parse_timestamp_strict(
            df_out[target_time_col],
            self.TARGET_TS_FORMATS,
            field_name=f"{files['target'].name}:{target_time_col}",
        )

        df_in = df_in.copy()
        df_out = df_out.copy()

        # Κρατάμε τις parsed merge keys χωριστά από τις raw display columns.
        df_in["_input_timestamp"] = parsed_input_ts
        df_out["_target_timestamp"] = parsed_target_ts

        # --------------------------------------------------------------
        # 3. Unit normalization και wind features
        # --------------------------------------------------------------
        df_in, scaled_by_1000 = self._normalize_input_units(df_in)
        df_in = self._build_wind_features(df_in)

        # --------------------------------------------------------------
        # 4. Fail-fast integrity checks πριν το merge
        # --------------------------------------------------------------
        if df_in["_input_timestamp"].isna().any():
            raise ValueError(f"Park {park_id}: NaT timestamps detected in input dataframe.")

        if df_out["_target_timestamp"].isna().any():
            raise ValueError(f"Park {park_id}: NaT timestamps detected in target dataframe.")

        if df_in.duplicated(subset=["_input_timestamp"]).any():
            dup_count = int(df_in.duplicated(subset=["_input_timestamp"]).sum())
            raise ValueError(f"Park {park_id}: duplicate input timestamps detected ({dup_count}).")

        if df_out.duplicated(subset=["_target_timestamp"]).any():
            dup_count = int(df_out.duplicated(subset=["_target_timestamp"]).sum())
            raise ValueError(f"Park {park_id}: duplicate target timestamps detected ({dup_count}).")

        # --------------------------------------------------------------
        # 5. Merge using strict parsed keys
        # --------------------------------------------------------------
        merged = df_in.merge(
            df_out,
            left_on="_input_timestamp",
            right_on="_target_timestamp",
            how="inner",
            validate="one_to_one",
        )

        # --------------------------------------------------------------
        # 6. Canonical downstream timestamp
        # --------------------------------------------------------------
        # Το authoritative downstream backbone είναι το target-side ISO timestamp.
        merged["timestamp"] = merged["_target_timestamp"]

        # --------------------------------------------------------------
        # 7. Canonical column naming
        # --------------------------------------------------------------
        merged = merged.rename(
            columns={
                "pw": "Power_Output_Normalized",
                "icon_eu_daf_pc_baseline": "Baseline_Prediction",
            }
        )

        # --------------------------------------------------------------
        # 8. Loader-level diagnostics
        # --------------------------------------------------------------
        merged["loader_input_sep_used"] = input_sep
        merged["loader_target_sep_used"] = target_sep
        merged["loader_input_ts_format"] = input_ts_format
        merged["loader_target_ts_format"] = target_ts_format
        merged["loader_scaled_input_by_1000"] = scaled_by_1000

        # --------------------------------------------------------------
        # 9. Cleanup και final checks
        # --------------------------------------------------------------
        cols_to_drop = [col for col in ["_input_timestamp", "_target_timestamp"] if col in merged.columns]
        merged = merged.drop(columns=cols_to_drop)
        merged = merged.sort_values("timestamp").reset_index(drop=True)

        if merged["timestamp"].isna().any():
            raise ValueError(f"Park {park_id}: NaT timestamps detected after merge.")

        if merged.duplicated(subset=["timestamp"]).any():
            dup_count = int(merged.duplicated(subset=["timestamp"]).sum())
            raise ValueError(f"Park {park_id}: duplicate timestamps detected after merge ({dup_count}).")

        if not merged["timestamp"].is_monotonic_increasing:
            raise ValueError(f"Park {park_id}: non-monotonic timestamps detected after merge.")

        return merged