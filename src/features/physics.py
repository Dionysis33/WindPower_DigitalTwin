from __future__ import annotations

from typing import Union

import numpy as np
import pandas as pd


NumericLike = Union[float, int, np.ndarray, pd.Series]


# -------------------------------------------------------------------
# Physics constants
# -------------------------------------------------------------------
RHO = 1.225
BETZ_LIMIT = 0.5926


def apply_power_law_scaling(
    v_ref: NumericLike,
    h_ref: float,
    h_hub: float,
    alpha: float = 0.143,
) -> NumericLike:
    """
    Προσαρμόζει την ταχύτητα ανέμου από ύψος αναφοράς `h_ref`
    στο ύψος πλήμνης `h_hub` με χρήση του Power Law.

    Παράμετροι
    ----------
    v_ref:
        Reference wind speed στο ύψος `h_ref`.
    h_ref:
        Ύψος αναφοράς της διαθέσιμης μέτρησης / πρόβλεψης.
    h_hub:
        Στόχος ύψους πλήμνης.
    alpha:
        Power-law exponent. Στο current project χρησιμοποιείται
        ως σταθερή engineering παραδοχή και όχι ως learned parameter.
    """
    if h_ref <= 0:
        raise ValueError("Το h_ref πρέπει να είναι θετικό.")
    if h_hub <= 0:
        raise ValueError("Το h_hub πρέπει να είναι θετικό.")

    return v_ref * (h_hub / h_ref) ** alpha


def calculate_theoretical_max_power(
    wind_speed: NumericLike,
    swept_area: float,
) -> NumericLike:
    """
    Υπολογίζει το θεωρητικό άνω όριο ισχύος με βάση το Betz limit:

        P_max = 0.5 * rho * A * v^3 * Betz_limit
    """
    if swept_area <= 0:
        raise ValueError("Το swept_area πρέπει να είναι θετικό.")

    return 0.5 * RHO * swept_area * (wind_speed ** 3) * BETZ_LIMIT


def get_physics_loss_terms(
    predicted_power: NumericLike,
    wind_speed: NumericLike,
    swept_area: float,
    cut_out_speed: float = 25.0,
) -> tuple[float, float]:
    """
    Υπολογίζει δύο βοηθητικούς physics-informed penalty terms:

    1. L_efficiency:
       Ποινή όταν η προβλεπόμενη ισχύς ξεπερνά το θεωρητικό όριο Betz.

    2. L_cutoff:
       Ποινή όταν προβλέπεται μη μηδενική ισχύς πάνω από το cut-out speed.

    Σημείωση:
    Αυτή η συνάρτηση είναι utility/helper για μελλοντική research extension.
    Δεν συνιστά πλήρως ολοκληρωμένο PHM ή PINN training objective.
    """
    p_max = calculate_theoretical_max_power(wind_speed, swept_area)

    # Παραβίαση φυσικού upper bound
    l_efficiency = np.maximum(0.0, predicted_power - p_max)

    # Παραβίαση cut-out behavior
    l_cutoff = np.where(np.asarray(wind_speed) > cut_out_speed, predicted_power, 0.0)

    return float(np.mean(l_efficiency)), float(np.mean(l_cutoff))