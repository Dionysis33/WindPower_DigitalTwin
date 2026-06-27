# Residual Diagnostics and PHM-Oriented Interpretation

Residual diagnostics are downstream interpretation layers over forecasting outputs. They support candidate screening and condition-monitoring-oriented discussion, but they are not confirmed faults and not validated PHM.

## Diagnostic Role

The repository documents residual distributions, operating-regime summaries, park-level diagnostic aggregation, warning-event extraction, directional bias, temporal residual patterns, and residual persistence.

These outputs help identify where forecast behavior is systematically difficult or deviates from expected behavior. They should be interpreted as candidate residual-screening signals.

## Notebook To Audit Map

| Notebook | Evidence status | Audit document |
|---|---|---|
| `NB20` / `20_residual_phm_diagnostics.ipynb` | Validation-calibrated residual diagnostic interpretation layer over forecasting outputs | `docs/RESIDUAL_PHM_DIAGNOSTICS_AUDIT.md` |
| `NB21` / `21_strong_model_residual_phm_diagnostics.ipynb` | Validation-calibrated strong-model residual diagnostic interpretation layer | `docs/STRONG_MODEL_RESIDUAL_PHM_AUDIT.md` |

These notebooks do not replace the canonical benchmark and do not validate PHM, fault diagnosis, anomaly detection, Remaining Useful Life estimation, or deployed digital twin functionality.

## Claim Boundary

Do not present residual diagnostics as:

- confirmed turbine or park faults
- fault diagnosis
- validated anomaly detection
- Remaining Useful Life estimation
- maintenance prescriptions
- deployed monitoring
- completed PHM functionality

Without fault labels, warning flags and diagnostic rankings remain screening and interpretation aids.

## Source Documents

- `docs/PHM_ROADMAP.md`
- `docs/BASELINE_PROTOCOL.md`
- `docs/RESIDUAL_PHM_DIAGNOSTICS_AUDIT.md`
- `docs/STRONG_MODEL_RESIDUAL_PHM_AUDIT.md`
- `README.md`
