# Repository Evidence Hygiene

The repository uses documentation, logs, artifact policy, and contribution rules to keep thesis-facing evidence reviewable.

## Evidence Discipline

Reviewer-safe evidence should be traceable to maintained documentation, canonical artifacts, or explicitly documented audits. Local rerun outputs, diagnostics bundles, model files, and notebook-native exports should remain local-only unless intentionally promoted and reviewed.

`LOGS.md` is the active methodological log. `LOGS_ARCHIVE.md` contains historical or superseded context and should not override current canonical artifacts.

## Contribution and Safety Expectations

Contributions should preserve:

- reproducibility
- temporal leakage prevention
- benchmark-safe reporting
- clear implemented/planned/future distinctions
- careful forecasting-vs-PHM wording
- artifact safety
- local demo non-production wording

Security and governance documents focus on avoiding accidental exposure of secrets, raw data, local paths, large generated artifacts, and unintended public outputs.

## Source Documents

- `CONTRIBUTING.md`
- `SECURITY.md`
- `CODE_OF_CONDUCT.md`
- `LOGS.md`
- `LOGS_ARCHIVE.md`
- `docs/MANUSCRIPT_PROGRESS.md`
