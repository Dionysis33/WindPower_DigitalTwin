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

## Matched four-park row-level baseline evidence

The matched four-park baseline audit now documents controlled row-level baseline evidence for the same selected parks used in the neural subset audits: `docs/MATCHED_FOUR_PARK_BASELINE_COMPARISON_AUDIT.md`.

The selected test metrics below provide row-level tabular context on parks `00183`, `00198`, `00303`, and `00427`. They are separate from the canonical full-dataset benchmark above and are not directly equivalent to the sequence-window setup used by the GRU, LSTM, and TCN audits.

| Evidence space | Model | Test MAE | Test RMSE | Test R2 |
|---|---:|---:|---:|---:|
| Matched four-park row-level baseline | XGBoost | 0.07916488214900315 | 0.13048056280434156 | 0.8733693976256192 |
| Matched four-park row-level baseline | Persistence | 0.08079669733592597 | 0.1474239474217667 | 0.8383472483419506 |
| Matched four-park row-level baseline | Random Forest | 0.08389790455769289 | 0.13389992624988545 | 0.8666454906497136 |
| Matched four-park row-level baseline | MLP | 0.08538023613281545 | 0.13285203467352433 | 0.868724569689501 |
| Matched four-park row-level baseline | Linear Regression | 0.08787732510386184 | 0.13507058489456872 | 0.8643035171583309 |

## Controlled four-park neural subset evidence

The following neural metrics are documented controlled four-park subset evidence only. These rows are not ranked against the canonical baseline rows above.

| Model | Architecture family | Audit source | Evaluation scope | Selected parks | Feature count | Lookback steps | Validation MAE | Validation RMSE | Validation R2 | Test MAE | Test RMSE | Test R2 | test_evaluations | Comparability note |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| PyTorch tabular MLP | Tabular neural network | `docs/NN_SUBSET_EXPERIMENT_AUDIT.md` | Controlled four-park tabular subset | `00183`, `00198`, `00303`, `00427` | 41 | n/a | 0.076672 | 0.122131 | 0.856115 | 0.084520 | 0.131781 | 0.870832 | 1, documented in prose as one-time test evaluation | Supports neural subset readiness; not comparable to canonical full-dataset benchmark rows and not directly equivalent to sequence-window runs |
| PyTorch GRU sequence baseline | Recurrent sequence neural network | `docs/NN_SEQUENCE_SUBSET_AUDIT.md` | Controlled four-park sequence subset | `00183`, `00198`, `00303`, `00427` | 41 | 24 | 0.09467061222417163 | 0.14620384209397685 | 0.7937695238087121 | 0.1013616555108132 | 0.152757068100059 | 0.8269631744779631 | 1 | Comparable to the LSTM controlled sequence subset run; not comparable to canonical full-dataset benchmark rows |
| PyTorch LSTM sequence baseline | Recurrent sequence neural network | `docs/NN_LSTM_SEQUENCE_SUBSET_AUDIT.md` | Controlled four-park sequence subset | `00183`, `00198`, `00303`, `00427` | 41 | 24 | 0.0944957135017893 | 0.14861402980949204 | 0.7869140109636205 | 0.10342178818174555 | 0.15506761498343793 | 0.8216890043240139 | 1 | Comparable to the GRU controlled sequence subset run; not comparable to canonical full-dataset benchmark rows |
| PyTorch TCN sequence baseline | Convolutional sequence neural network | `docs/TCN_SEQUENCE_SUBSET_AUDIT.md` | Controlled four-park sequence subset | `00183`, `00198`, `00303`, `00427` | 41 | 24 | 0.10367857854266052 | 0.157573260059511 | 0.7604477171114871 | 0.11380967093854394 | 0.16218968427658445 | 0.804933645682722 | 1 | Comparable to the GRU/LSTM controlled sequence subset runs; TCN did not outperform the documented GRU test MAE on this same subset |

## Comparability matrix

| Comparison | Directly comparable? | Reason | Allowed wording | Disallowed wording |
|---|---|---|---|---|
| Canonical baseline model vs canonical baseline model | Yes | Rows share the same canonical final test-set benchmark artifact and metric definitions. | "Within `data/processed/baseline_metrics.csv`, XGBoost has the lowest MAE among the recorded canonical baseline rows." | "XGBoost is superior to all future or non-canonical models." |
| Matched four-park row-level baseline model vs matched four-park row-level baseline model | Yes, within the matched row-level baseline evidence space only | Rows share the same four selected parks and row-level tabular framing documented in `docs/MATCHED_FOUR_PARK_BASELINE_COMPARISON_AUDIT.md`. | "Within the matched four-park row-level baseline table, XGBoost has the lowest selected test MAE." | "The matched four-park row-level table proves model superiority across the canonical and neural sequence evaluation spaces." |
| Matched four-park row-level baseline rows vs canonical full-dataset baseline rows | No | The matched rows are controlled four-park row-level evidence, while `baseline_metrics.csv` remains the canonical full-dataset benchmark artifact for the implemented tabular baseline ladder. | "The matched four-park baseline table provides controlled subset context without changing the canonical benchmark ranking." | "The matched four-park rows replace or revise the canonical full-dataset benchmark." |
| Matched four-park row-level baseline rows vs GRU/LSTM/TCN sequence subsets | Limited | The rows use the same selected parks, but the matched baseline table is row-level tabular evidence while GRU, LSTM, and TCN use 24-step sequence windows. | "The matched row-level baseline table gives controlled context for the same four parks but is not directly equivalent to the sequence-window setup." | "The matched row-level baseline rows and sequence subset rows form one fully equivalent ranking." |
| GRU vs LSTM vs TCN controlled sequence subset | Yes, within the controlled sequence subset only | These runs use the same four parks, feature count, lookback length, sequence framing, validation-selected state, and one test evaluation. | "In the controlled four-park sequence subset, GRU, LSTM, and TCN can be compared as local sequence evidence; TCN did not outperform the documented GRU test MAE in this matched setting." | "The GRU, LSTM, or TCN result changes the canonical benchmark ranking." |
| Neural subset models vs canonical full-dataset baseline rows | No | The neural audits use controlled four-park subset evidence, while `baseline_metrics.csv` is the canonical final test-set benchmark artifact for the implemented tabular baseline ladder. | "The neural subset audits support neural-pipeline readiness and motivate matched or full-dataset follow-up experiments." | "The neural subset rows outperform or underperform the canonical baseline rows in the same benchmark." |
| Graph/diagnostic evidence vs canonical benchmark rows | No | Graph and diagnostic outputs are supporting or local rerun evidence unless explicitly promoted; they do not redefine `data/processed/baseline_metrics.csv`. | "Graph and diagnostic evidence can inform interpretation and future work while preserving the canonical benchmark boundary." | "Graph or diagnostic outputs replace the canonical benchmark table or prove graph superiority." |
| Tabular MLP subset vs GRU/LSTM/TCN sequence subsets | Limited | The runs share the selected parks and feature count, but the tabular MLP uses row-level tabular inputs while GRU, LSTM, and TCN use 24-step sequence windows. | "These audits are complementary controlled neural subset evidence with different input framing." | "The tabular MLP, GRU, LSTM, and TCN rows form one fully equivalent neural ranking." |

## Manuscript-safe interpretation

"The tracked `data/processed/baseline_metrics.csv` artifact is the repository's canonical final test-set benchmark table for the implemented baseline ladder. Within that comparable benchmark space, XGBoost has the lowest MAE among the recorded rows."

"The MLP, GRU, LSTM, and TCN audits provide controlled four-park neural evidence on parks `00183`, `00198`, `00303`, and `00427`, using train-only preprocessing and validation-selected model states followed by one test evaluation."

"The matched four-park row-level baseline audit provides controlled tabular baseline context on the same selected parks, while remaining separate from both the canonical full-dataset benchmark and the GRU/LSTM/TCN sequence-window evidence."

"These neural subset metrics should not be merged into the canonical full benchmark ranking or used to claim superiority over XGBoost, MLP, or other baseline rows. They support neural-pipeline readiness and motivate future comparable full-benchmark or matched-subset experiments."

## Limitations and next steps

Current limitations:

- The neural evidence is controlled four-park subset evidence, not a full-dataset benchmark replacement.
- The matched four-park baseline evidence is controlled row-level subset evidence, not a full-dataset benchmark replacement.
- The tabular MLP subset row and the GRU/LSTM/TCN sequence subset rows use different input framing.
- The matched row-level baseline table and the GRU/LSTM/TCN sequence subset rows use different input framing.
- Graph and diagnostic evidence remain outside the canonical tabular benchmark ranking unless a future artifact is explicitly promoted and reviewed.

Next steps:

- Use the matched four-park baseline audit as controlled row-level context for manuscript discussion.
- Optional full-dataset neural scaling for the best feasible neural model.
- Manuscript table integration after comparability review.
