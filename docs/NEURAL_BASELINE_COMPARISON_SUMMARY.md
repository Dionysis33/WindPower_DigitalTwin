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

The selected test metrics below provide row-level tabular context on parks `00183`, `00198`, `00303`, and `00427`. They are separate from the canonical full-dataset benchmark above and are not directly equivalent to the sequence-window setup used by the GRU, LSTM, TCN, and NB19 audits.

| Evidence space | Model | Test MAE | Test RMSE | Test R2 |
|---|---:|---:|---:|---:|
| Matched four-park row-level baseline | XGBoost | 0.07916488214900315 | 0.13048056280434156 | 0.8733693976256192 |
| Matched four-park row-level baseline | Persistence | 0.08079669733592597 | 0.1474239474217667 | 0.8383472483419506 |
| Matched four-park row-level baseline | Random Forest | 0.08389790455769289 | 0.13389992624988545 | 0.8666454906497136 |
| Matched four-park row-level baseline | MLP | 0.08538023613281545 | 0.13285203467352433 | 0.868724569689501 |
| Matched four-park row-level baseline | Linear Regression | 0.08787732510386184 | 0.13507058489456872 | 0.8643035171583309 |

## Controlled four-park neural and sequence-aligned subset evidence

The following metrics are documented controlled four-park subset evidence only. These rows are not ranked against the canonical baseline rows above.

NB19 adds sequence-aligned evidence for parks `00183`, `00198`, `00303`, and `00427` using target `Power_Output_Normalized`, `LOOKBACK_STEPS=24`, 41 train-inferred numeric features, train-only `StandardScaler`, unscaled target, no `turbine` encoding, gap-safe windows, validation-only selection, and one final test evaluation per selected model family. Both NB19 models use the same input sequence tensor contract: `[n_windows, 24, 41]`.

| Model | Architecture family | Audit source | Evaluation scope | Selected parks | Feature count | Lookback steps | Validation MAE | Validation RMSE | Validation R2 | Test MAE | Test RMSE | Test R2 | test_evaluations | Comparability note |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| PyTorch tabular MLP | Tabular neural network | `docs/NN_SUBSET_EXPERIMENT_AUDIT.md` | Controlled four-park tabular subset | `00183`, `00198`, `00303`, `00427` | 41 | n/a | 0.076672 | 0.122131 | 0.856115 | 0.084520 | 0.131781 | 0.870832 | 1, documented in prose as one-time test evaluation | Supports neural subset readiness; not comparable to canonical full-dataset benchmark rows and not directly equivalent to sequence-window runs |
| PyTorch GRU sequence baseline | Recurrent sequence neural network | `docs/NN_SEQUENCE_SUBSET_AUDIT.md` | Controlled four-park sequence subset | `00183`, `00198`, `00303`, `00427` | 41 | 24 | 0.09467061222417163 | 0.14620384209397685 | 0.7937695238087121 | 0.1013616555108132 | 0.152757068100059 | 0.8269631744779631 | 1 | Comparable to the LSTM controlled sequence subset run; not comparable to canonical full-dataset benchmark rows |
| PyTorch LSTM sequence baseline | Recurrent sequence neural network | `docs/NN_LSTM_SEQUENCE_SUBSET_AUDIT.md` | Controlled four-park sequence subset | `00183`, `00198`, `00303`, `00427` | 41 | 24 | 0.0944957135017893 | 0.14861402980949204 | 0.7869140109636205 | 0.10342178818174555 | 0.15506761498343793 | 0.8216890043240139 | 1 | Comparable to the GRU controlled sequence subset run; not comparable to canonical full-dataset benchmark rows |
| PyTorch TCN sequence baseline | Convolutional sequence neural network | `docs/TCN_SEQUENCE_SUBSET_AUDIT.md` | Controlled four-park sequence subset | `00183`, `00198`, `00303`, `00427` | 41 | 24 | 0.10367857854266052 | 0.157573260059511 | 0.7604477171114871 | 0.11380967093854394 | 0.16218968427658445 | 0.804933645682722 | 1 | Comparable to the GRU/LSTM controlled sequence subset runs; TCN did not outperform the documented GRU test MAE on this same subset |
| Flattened-window XGBoost | Sequence-aligned gradient-boosted tree baseline | `docs/PATCHTST_SEQUENCE_SUBSET_AUDIT.md` | Controlled four-park sequence subset | `00183`, `00198`, `00303`, `00427` | 41 | 24 | 0.087767 | 0.141316 | 0.807329 | 0.096008 | 0.150826 | 0.831309 | 1 | Strong sequence-aligned non-neural baseline under the same NB19 gap-safe `[24, 41]` window protocol; subset evidence only |
| PatchTST-Lite Transformer | Pure PyTorch Transformer-style sequence neural network | `docs/PATCHTST_SEQUENCE_SUBSET_AUDIT.md` | Controlled four-park sequence subset | `00183`, `00198`, `00303`, `00427` | 41 | 24 | 0.110098 | 0.171969 | 0.714678 | 0.117405 | 0.173865 | 0.775838 | 1 | Pure PyTorch Transformer-style sequence baseline under the same NB19 gap-safe `[24, 41]` window protocol; subset evidence only |

NB19 window counts:

| Split | Windows | Segments |
|---|---:|---:|
| train | 30988 | 12 |
| validation | 2784 | 4 |
| test | 16892 | 12 |

NB19 selected model details:

| Model | Selected details |
|---|---|
| Flattened-window XGBoost | `config_id=1`; `n_estimators=300`; `max_depth=4`; `learning_rate=0.03`; `subsample=0.8`; `colsample_bytree=0.8` |
| PatchTST-Lite Transformer | `model_id=patchtst_lite_p4_s2_d64_h4_l2_do0_1`; `best_epoch=23`; `best_val_loss_mse=0.02957333031313858`; `epochs_ran=28` |

## Comparability matrix

| Comparison | Directly comparable? | Reason | Allowed wording | Disallowed wording |
|---|---|---|---|---|
| Canonical baseline model vs canonical baseline model | Yes | Rows share the same canonical final test-set benchmark artifact and metric definitions. | "Within `data/processed/baseline_metrics.csv`, XGBoost has the lowest MAE among the recorded canonical baseline rows." | "XGBoost is superior to all future or non-canonical models." |
| Matched four-park row-level baseline model vs matched four-park row-level baseline model | Yes, within the matched row-level baseline evidence space only | Rows share the same four selected parks and row-level tabular framing documented in `docs/MATCHED_FOUR_PARK_BASELINE_COMPARISON_AUDIT.md`. | "Within the matched four-park row-level baseline table, XGBoost has the lowest selected test MAE." | "The matched four-park row-level table proves model superiority across the canonical and neural sequence evaluation spaces." |
| Matched four-park row-level baseline rows vs canonical full-dataset baseline rows | No | The matched rows are controlled four-park row-level evidence, while `baseline_metrics.csv` remains the canonical full-dataset benchmark artifact for the implemented tabular baseline ladder. | "The matched four-park baseline table provides controlled subset context without changing the canonical benchmark ranking." | "The matched four-park rows replace or revise the canonical full-dataset benchmark." |
| Matched four-park row-level baseline rows vs sequence subsets | Limited | The rows use the same selected parks, but the matched baseline table is row-level tabular evidence while GRU, LSTM, TCN, NB19 Flattened-window XGBoost, and NB19 PatchTST-Lite use 24-step sequence windows. | "The matched row-level baseline table gives controlled context for the same four parks but is not directly equivalent to the sequence-window setup." | "The matched row-level baseline rows and sequence subset rows form one fully equivalent ranking." |
| GRU vs LSTM vs TCN vs NB19 controlled sequence subsets | Yes, within the controlled four-park sequence subset only | These runs use the same four parks, feature count, lookback length, sequence framing, validation-only selection, and one test evaluation, but they remain subset evidence. | "In the controlled four-park sequence subset, Flattened-window XGBoost outperformed PatchTST-Lite under the same leakage-aware sequence-window protocol, and the sequence rows can be discussed as local sequence evidence." | "The sequence subset result changes the canonical benchmark ranking or proves general XGBoost superiority/general Transformer inferiority." |
| NB19 Flattened-window XGBoost vs NB19 PatchTST-Lite | Yes, within NB19 only | Both NB19 models use the same train-only-scaled, gap-safe `[24, 41]` windows, validation-only selection, and one final test evaluation. | "In the controlled four-park subset, Flattened-window XGBoost outperformed PatchTST-Lite on validation and test metrics under the same sequence-window protocol." | "NB19 establishes general XGBoost superiority or general Transformer inferiority." |
| Neural and sequence subset models vs canonical full-dataset baseline rows | No | The subset audits use controlled four-park subset evidence, while `baseline_metrics.csv` is the canonical final test-set benchmark artifact for the implemented tabular baseline ladder. | "The subset audits support neural-pipeline readiness and motivate matched or full-dataset follow-up experiments." | "The subset rows outperform or underperform the canonical baseline rows in the same benchmark." |
| Graph/diagnostic evidence vs canonical benchmark rows | No | Graph and diagnostic outputs are supporting or local rerun evidence unless explicitly promoted; they do not redefine `data/processed/baseline_metrics.csv`. | "Graph and diagnostic evidence can inform interpretation and future work while preserving the canonical benchmark boundary." | "Graph or diagnostic outputs replace the canonical benchmark table or prove graph superiority." |
| Tabular MLP subset vs sequence subsets | Limited | The runs share the selected parks and feature count, but the tabular MLP uses row-level tabular inputs while GRU, LSTM, TCN, NB19 Flattened-window XGBoost, and NB19 PatchTST-Lite use 24-step sequence windows. | "These audits are complementary controlled subset evidence with different input framing." | "The tabular MLP and sequence subset rows form one fully equivalent ranking." |

## Manuscript-safe interpretation

"The tracked `data/processed/baseline_metrics.csv` artifact is the repository's canonical final test-set benchmark table for the implemented baseline ladder. Within that comparable benchmark space, XGBoost has the lowest MAE among the recorded rows."

"The MLP, GRU, LSTM, TCN, and PatchTST-Lite audits provide controlled four-park neural evidence on parks `00183`, `00198`, `00303`, and `00427`, using train-only preprocessing and validation-selected model states followed by one test evaluation. NB19 also adds a sequence-aligned Flattened-window XGBoost baseline under the same leakage-aware `[24, 41]` sequence-window protocol."

"The matched four-park row-level baseline audit provides controlled tabular baseline context on the same selected parks, while remaining separate from both the canonical full-dataset benchmark and the sequence-window evidence."

"In the controlled four-park sequence subset, Flattened-window XGBoost outperformed PatchTST-Lite under the same leakage-aware sequence-window protocol. This is subset-level evidence only; it does not replace the canonical full benchmark and does not establish general XGBoost superiority or general Transformer inferiority."

"These subset metrics should not be merged into the canonical full benchmark ranking or used to claim superiority over XGBoost, MLP, or other baseline rows in a different evaluation space. They support neural-pipeline readiness, add a strong sequence-aligned non-neural baseline and a pure PyTorch Transformer-style sequence baseline after GRU, LSTM, and TCN, and motivate future comparable full-benchmark or matched-subset experiments."

## Limitations and next steps

Current limitations:

- The neural evidence is controlled four-park subset evidence, not a full-dataset benchmark replacement.
- The matched four-park baseline evidence is controlled row-level subset evidence, not a full-dataset benchmark replacement.
- The tabular MLP subset row and the sequence subset rows use different input framing.
- The matched row-level baseline table and the sequence subset rows use different input framing.
- NB19 is controlled four-park sequence evidence only and should not be generalized to full-dataset or architecture-wide superiority claims.
- Graph and diagnostic evidence remain outside the canonical tabular benchmark ranking unless a future artifact is explicitly promoted and reviewed.

Next steps:

- Use the matched four-park baseline audit as controlled row-level context for manuscript discussion.
- Optional full-dataset neural scaling for the best feasible neural model.
- Manuscript table integration after comparability review.
