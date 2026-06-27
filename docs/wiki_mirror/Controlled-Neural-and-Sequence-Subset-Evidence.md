# Controlled Neural and Sequence Subset Evidence

Neural and sequence experiments are controlled four-park subset evidence only. They should not be merged into the canonical full-dataset benchmark ranking.

## Evidence Spaces

The repository separates:

- canonical full-dataset tabular benchmark evidence
- matched four-park row-level baseline evidence
- four-park tabular neural subset evidence
- four-park sequence-window evidence

These evidence spaces have different scopes and comparability rules.

## Notebook To Audit Map

| Notebook | Evidence status | Audit document |
|---|---|---|
| `NB15` / `15_nn_sequence_baseline_subset.ipynb` | Audited controlled GRU sequence subset evidence | `docs/NN_SEQUENCE_SUBSET_AUDIT.md` |
| `NB16` / `16_nn_lstm_sequence_subset.ipynb` | Audited controlled LSTM sequence subset evidence | `docs/NN_LSTM_SEQUENCE_SUBSET_AUDIT.md` |
| `NB17` / `17_mamba_sequence_baseline_subset.ipynb` | Unaudited Mamba sequence scaffold only | No completed `NB17` audit document found |
| `NB18` / `18_tcn_sequence_baseline_subset.ipynb` | Audited controlled TCN sequence subset evidence | `docs/TCN_SEQUENCE_SUBSET_AUDIT.md` |
| `NB19` / `19_patchtst_sequence_subset.ipynb` | Audited sequence-aligned PatchTST-Lite and flattened-window XGBoost subset evidence | `docs/PATCHTST_SEQUENCE_SUBSET_AUDIT.md` |

The tabular neural subset and matched four-park baseline context are documented separately in `docs/NN_SUBSET_EXPERIMENT_AUDIT.md`, `docs/MATCHED_FOUR_PARK_BASELINE_COMPARISON_AUDIT.md`, and `docs/NEURAL_BASELINE_COMPARISON_SUMMARY.md`.

## Safe Interpretation

The neural and sequence audits can support discussion of experimental readiness, leakage-aware subset protocols, matched-subset comparisons, and future full-benchmark motivation.

They do not prove general model superiority, do not replace `data/processed/baseline_metrics.csv`, and should not be used to claim that subset models outperform or underperform canonical full-dataset rows in the same benchmark.

## Special Note

Only audited and documented subset evidence should be given reviewer-facing weight. Notebook files without matching reviewed audit documentation should not be promoted as manuscript evidence.

## Source Documents

- `docs/NEURAL_BASELINE_COMPARISON_SUMMARY.md`
- `docs/MATCHED_FOUR_PARK_BASELINE_COMPARISON_AUDIT.md`
- `docs/NN_SUBSET_EXPERIMENT_AUDIT.md`
- `docs/NN_SEQUENCE_SUBSET_AUDIT.md`
- `docs/NN_LSTM_SEQUENCE_SUBSET_AUDIT.md`
- `docs/TCN_SEQUENCE_SUBSET_AUDIT.md`
- `docs/PATCHTST_SEQUENCE_SUBSET_AUDIT.md`
