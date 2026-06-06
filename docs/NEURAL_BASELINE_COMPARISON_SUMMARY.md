# Neural Baseline Comparison Summary

## Purpose and scope

This document consolidates the manuscript-facing comparison boundary between the repository's canonical tabular baseline benchmark and the controlled neural-network subset audits.

It is a comparison summary, not a new experiment report. It does not merge metrics from incompatible evaluation spaces into one ranking, and it does not promote local diagnostic or neural subset outputs into canonical benchmark artifacts.

## Canonical baseline benchmark

The tracked `data/processed/baseline_metrics.csv` artifact is the repository's canonical final test-set benchmark artifact for the implemented tabular baseline ladder. The rows below are ranked only within that canonical comparable tabular benchmark space by MAE ascending.

| Rank | Model | MAE | RMSE | R2 | Evidence source | Evaluation scope | Manuscript use |
|---:|---|---:|---:|---:|---|---|---|
| 1 | XGBoost | 0.06574968136344334 | 0.1134941263311143 | 0.8603478411144265 | `data/processed/baseline_metrics.csv` | Canonical final test-set benchmark for the implemented tabular baseline ladder | Primary comparable benchmark row; lowest MAE within this table |
| 2 | MLP | 0.0680078041111079 | 0.11534326087238028 | 0.8557601267189187 | `data/processed/baseline_metrics.csv` | Canonical final test-set benchmark for the implemented tabular baseline ladder | Comparable canonical benchmark row |
| 3 | Persistence | 0.0698321887215004 | 0.1304087445718935 | 0.8156197880627447 | `data/processed/baseline_metrics.csv` | Canonical final test-set benchmark for the implemented tabular baseline ladder | Comparable canonical benchmark row |
| 4 | Random Forest | 0.07096254721460128 | 0.118826019905796 | 0.8469180509688362 | `data/processed/baseline_metrics.csv` | Canonical final test-set benchmark for the implemented tabular baseline ladder | Comparable canonical benchmark row |
| 5 | Linear Regression | 0.0727208735022708 | 0.120307498871806 | 0.8430771171338876 | `data/processed/baseline_metrics.csv` | Canonical final test-set benchmark for the implemented tabular baseline ladder | Comparable canonical benchmark row |

XGBoost has the lowest MAE only within this canonical comparable tabular benchmark space.

## Controlled four-park neural subset evidence

The following neural metrics are documented controlled four-park subset evidence only. These rows are not ranked against the canonical baseline rows above.

| Model | Architecture family | Audit source | Evaluation scope | Selected parks | Feature count | Lookback steps | Validation MAE | Validation RMSE | Validation R2 | Test MAE | Test RMSE | Test R2 | test_evaluations | Comparability note |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| PyTorch tabular MLP | Tabular neural network | `docs/NN_SUBSET_EXPERIMENT_AUDIT.md` | Controlled four-park tabular subset | `00183`, `00198`, `00303`, `00427` | 41 | n/a | 0.076672 | 0.122131 | 0.856115 | 0.084520 | 0.131781 | 0.870832 | 1, documented in prose as one-time test evaluation | Supports neural subset readiness; not comparable to canonical full-dataset benchmark rows and not directly equivalent to sequence-window runs |
| PyTorch GRU sequence baseline | Recurrent sequence neural network | `docs/NN_SEQUENCE_SUBSET_AUDIT.md` | Controlled four-park sequence subset | `00183`, `00198`, `00303`, `00427` | 41 | 24 | 0.09467061222417163 | 0.14620384209397685 | 0.7937695238087121 | 0.1013616555108132 | 0.152757068100059 | 0.8269631744779631 | 1 | Comparable to the LSTM controlled sequence subset run; not comparable to canonical full-dataset benchmark rows |
| PyTorch LSTM sequence baseline | Recurrent sequence neural network | `docs/NN_LSTM_SEQUENCE_SUBSET_AUDIT.md` | Controlled four-park sequence subset | `00183`, `00198`, `00303`, `00427` | 41 | 24 | 0.0944957135017893 | 0.14861402980949204 | 0.7869140109636205 | 0.10342178818174555 | 0.15506761498343793 | 0.8216890043240139 | 1 | Comparable to the GRU controlled sequence subset run; not comparable to canonical full-dataset benchmark rows |

## Comparability matrix

| Comparison | Directly comparable? | Reason | Allowed wording | Disallowed wording |
|---|---|---|---|---|
| Canonical baseline model vs canonical baseline model | Yes | Rows share the same canonical final test-set benchmark artifact and metric definitions. | "Within `data/processed/baseline_metrics.csv`, XGBoost has the lowest MAE among the recorded canonical baseline rows." | "XGBoost is superior to all future or non-canonical models." |
| GRU vs LSTM controlled sequence subset | Yes, within the controlled sequence subset only | Both runs use the same four parks, feature count, lookback length, sequence framing, validation-selected state, and one test evaluation. | "In the controlled four-park sequence subset, GRU and LSTM can be compared as local sequence evidence." | "The GRU or LSTM result changes the canonical benchmark ranking." |
| Neural subset models vs canonical full-dataset baseline rows | No | The neural audits use controlled four-park subset evidence, while `baseline_metrics.csv` is the canonical final test-set benchmark artifact for the implemented tabular baseline ladder. | "The neural subset audits support neural-pipeline readiness and motivate matched or full-dataset follow-up experiments." | "The neural subset rows outperform or underperform the canonical baseline rows in the same benchmark." |
| Graph/diagnostic evidence vs canonical benchmark rows | No | Graph and diagnostic outputs are supporting or local rerun evidence unless explicitly promoted; they do not redefine `data/processed/baseline_metrics.csv`. | "Graph and diagnostic evidence can inform interpretation and future work while preserving the canonical benchmark boundary." | "Graph or diagnostic outputs replace the canonical benchmark table or prove graph superiority." |
| Tabular MLP subset vs GRU/LSTM sequence subsets | Limited | The runs share the selected parks and feature count, but the tabular MLP uses row-level tabular inputs while GRU/LSTM use 24-step sequence windows. | "These audits are complementary controlled neural subset evidence with different input framing." | "The tabular MLP, GRU, and LSTM rows form one fully equivalent neural ranking." |

## Manuscript-safe interpretation

"The tracked `data/processed/baseline_metrics.csv` artifact is the repository's canonical final test-set benchmark table for the implemented baseline ladder. Within that comparable benchmark space, XGBoost has the lowest MAE among the recorded rows."

"The MLP, GRU, and LSTM audits provide controlled four-park neural evidence on parks `00183`, `00198`, `00303`, and `00427`, using train-only preprocessing and validation-selected model states followed by one test evaluation."

"These neural subset metrics should not be merged into the canonical full benchmark ranking or used to claim superiority over XGBoost, MLP, or other baseline rows. They support neural-pipeline readiness and motivate future comparable full-benchmark or matched-subset experiments."

## Limitations and next steps

Current limitations:

- The neural evidence is controlled four-park subset evidence, not a full-dataset benchmark replacement.
- The tabular MLP subset row and the GRU/LSTM sequence subset rows use different input framing.
- Graph and diagnostic evidence remain outside the canonical tabular benchmark ranking unless a future artifact is explicitly promoted and reviewed.

Next steps:

- Matched four-park baseline comparison.
- Optional full-dataset neural scaling for the best feasible neural model.
- Manuscript table integration after comparability review.
