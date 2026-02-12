import numpy as np
import pandas as pd
from typing import Union

def apply_power_law_scaling(
    v_ref: Union[float, pd.Series], 
    h_ref: float, 
    h_hub: float, 
    alpha: float = 0.143
) -> Union[float, pd.Series]:
    """
    Προσαρμογή της ταχύτητας ανέμου στο ύψος της πλήμνης (Power Law Scaling).
    """
    if h_ref <= 0:
        raise ValueError("Το ύψος αναφοράς πρέπει να είναι θετικό.")
        
    return v_ref * (h_hub / h_ref) ** alpha

# Σταθερές Φυσικής (Physics Constants)
RHO = 1.225  # Πυκνότητα αέρα στο επίπεδο της θάλασσας (kg/m^3)
BETZ_LIMIT = 0.5926  # Το θεωρητικό μέγιστο όριο απόδοσης (59.3%)

def calculate_theoretical_max_power(wind_speed: Union[float, pd.Series], swept_area: float) -> Union[float, pd.Series]:
    """
    Υπολογίζει το θεωρητικό μέγιστο όριο ενέργειας βάσει του ορίου Betz: 
    P_max = 0.5 * rho * Area * v^3 * Betz_Limit
    """
    #
    return 0.5 * RHO * swept_area * (wind_speed ** 3) * BETZ_LIMIT

def get_physics_loss_terms(predicted_power, wind_speed, swept_area, cut_out_speed=25.0):
    """
    Υπολογίζει τους όρους του Physics Loss (L_efficiency και L_cutoff).
    Αυτοί οι όροι θα προστεθούν στην L_total για να μειώσουν τον θόρυβο.
    """
    # 1. Έλεγχος Παραβίασης Ορίου Betz (L_efficiency)
    # Η ενέργεια δεν μπορεί να ξεπερνά το θεωρητικό μέγιστο
    p_max = calculate_theoretical_max_power(wind_speed, swept_area)
    #
    l_efficiency = np.maximum(0, predicted_power - p_max)
    
    # 2. Έλεγχος Cut-off Speed (L_cutoff)
    # Αν ο άνεμος είναι πάνω από το όριο ασφαλείας, η ισχύς πρέπει να είναι μηδέν
    #
    l_cutoff = np.where(wind_speed > cut_out_speed, predicted_power, 0.0)
    
    return np.mean(l_efficiency), np.mean(l_cutoff)