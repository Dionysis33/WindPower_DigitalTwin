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