# Security Policy

## Overview

**WindPower_DigitalTwin** is a **forecasting-first research repository** for **spatio-temporal wind power forecasting** on the **DaKS / Kassel synthetic wind power dataset**.

It supports reproducible forecasting research, benchmark-safe experimentation, downstream residual diagnostics, graph-aware methodological extensions, controlled subset evidence, local artifact inspection, and future PHM / digital-twin-oriented research.

It is not maintained as a production service, deployed platform, security-hardened operational system, production monitoring platform, completed PHM system, deployed digital twin, anomaly-detection service, fault-diagnosis system, RUL estimator, or operational forecasting service.

Security and artifact-safety issues still matter, especially when they affect secrets, workflows, dependency safety, file loading, notebook execution, local demo behavior, or accidental publication of raw data, local outputs, diagnostics, graph exports, subset outputs, model artifacts, or private research material.

---

## Quick Navigation

| Area | Purpose |
|---|---|
| [Report Privately](#report-privately) | How to report sensitive issues |
| [What To Report](#what-to-report) | Security and artifact-safety issues in scope |
| [Usually Out Of Scope](#usually-out-of-scope) | Methodological issues that are not security reports |
| [Data and Artifact Safety](#data-and-artifact-safety) | Raw data, generated artifacts, and local outputs |
| [Workflow and Notebook Safety](#workflow-and-notebook-safety) | Dependencies, CI, notebooks, and file I/O |
| [Local Demo Safety](#local-demo-safety) | Boundaries for `django_demo/` |
| [Secrets and Disclosure](#secrets-and-disclosure) | Credential handling and responsible disclosure |

---

## Report Privately

Please do **not** open a public issue for sensitive security problems.

Report the issue privately to the maintainer and include:

- a clear description of the issue,
- why it is a security problem,
- steps to reproduce it,
- affected files, notebooks, scripts, dependencies, workflows, or local demo components,
- the potential impact,
- whether credentials, local files, dataset material, artifacts, or private paths are exposed,
- and any suggested mitigation.

If live secrets or exposed credentials are involved, do not copy them into public channels.

---

## What To Report

Relevant reports include:

- exposed API keys, tokens, passwords, credentials, or private keys,
- accidental commit of `.env`-style local configuration,
- insecure GitHub Actions workflow behavior,
- vulnerable dependency usage with credible repository impact,
- unsafe deserialization,
- unsafe shell execution or arbitrary code execution risk,
- unsafe notebook execution paths,
- path traversal,
- unsafe file loading or overwrite behavior,
- accidental publication of restricted research assets,
- accidental exposure of raw dataset material,
- unintended exposure of local paths, private metadata, notebook outputs, or internal files,
- repository artifacts that reveal information that should not be public,
- local demo behavior that exposes files outside its intended artifact scope,
- or any change that makes sensitive files easier to publish by mistake.

Security-relevant data handling issues may include accidental publication of raw files, processed outputs with unintended metadata, graph or diagnostics exports with private paths, local rerun outputs, model artifacts, checkpoints, demo bundles, or controlled subset outputs that should remain local-only.

---

## Usually Out Of Scope

The following are usually **not** security issues unless they create a concrete safety, disclosure, or unsafe-execution risk:

- notebook modeling mistakes,
- poor benchmark performance,
- metric underperformance,
- forecasting residual structure,
- graph experiment underperformance,
- scientific limitations of a method,
- documentation typos,
- ordinary reproducibility problems,
- disagreement about methodology,
- disagreement about graph interpretation,
- or the fact that a model is not strong enough for a research claim.

These should normally be handled through standard issues, discussions, pull requests, or documentation updates.

---

## Data and Artifact Safety

The repository prioritizes reproducibility of the pipeline, not unrestricted redistribution of all local data artifacts.

Security and artifact-safety handling should respect these roles:

- raw DaKS dataset files should remain local unless explicitly permitted and documented,
- `data/processed/baseline_metrics.csv` is the canonical benchmark artifact, not a place for secrets or private metadata,
- selected thesis / report-facing figures should be intentionally reviewed before committing,
- local predictions, diagnostics, graph exports, controlled subset outputs, rerun outputs, and demo bundles should not be treated as automatic public artifacts,
- model binaries, checkpoints, serialized estimators, and training-state files should remain local-only by default,
- local paths and environment details should not be exposed in committed artifacts,
- demo bundles should contain only curated, intended, non-sensitive local exports.

When reporting an artifact-safety issue, describe what is exposed, where it appears, whether it is raw, processed, derived, diagnostic, graph-related, subset-related, model-related, or demo-related, and what the disclosure risk is.

---

## Workflow and Notebook Safety

This repository may use Python dependencies, Jupyter notebooks, GitHub Actions, local artifact exports, and a local-only Django demo helper.

When reporting a dependency or CI issue, specify:

- the affected package, action, or workflow,
- the impacted version,
- the file or job where it appears,
- and whether the issue affects local execution, CI, repository integrity, artifact safety, or public exposure.

Security-relevant notebook issues may include:

- execution of untrusted input,
- unsafe shell commands,
- unsafe file writes,
- accidental mutation of canonical artifacts,
- accidental exposure of local paths or environment variables,
- output cells that reveal private information,
- or notebook logic that makes restricted files easier to commit by mistake.

Notebook and workflow changes should preserve explicit paths, benchmark-safe artifact handling, clear separation between raw, processed, diagnostics, graph, subset, model, and demo artifacts, and no hidden execution behavior that could expose private local state.

---

## Local Demo Safety

The optional `django_demo/` directory is a **local-only, read-only, non-production, thesis-facing artifact inspection helper**.

It should be interpreted as:

- a local presentation helper,
- a thesis-facing artifact browser,
- and a read-only interface over curated exported artifacts.

It should not be treated as:

- a deployed service,
- a security-hardened platform,
- a production monitoring system,
- a PHM system,
- a deployed digital twin,
- an anomaly-detection service,
- a fault-diagnosis system,
- an operational forecasting service,
- a model-training interface,
- or a benchmark-generation system.

Report local demo issues when behavior may expose local artifacts, allow unsafe file loading, permit path traversal, write to benchmark or processed artifacts, disclose private paths or metadata, expose raw dataset files, include unintended files in demo bundles, encourage public hosting, or behave like deployed monitoring.

The demo should not trigger notebook reruns, train models, rewrite benchmark results, mutate processed artifacts, modify canonical outputs, expose raw dataset files, or act as a public service.

---

## Secrets and Disclosure

Contributors should not commit:

- `.env` files,
- API tokens,
- passwords,
- private keys,
- access credentials,
- private local database files,
- sensitive local machine paths,
- or private configuration files.

If a secret is accidentally committed:

1. remove it from the repository,
2. rotate or invalidate the exposed credential,
3. check whether it appeared in logs, artifacts, notebook outputs, or workflow output,
4. and report the issue privately if exposure may have occurred.

Please allow reasonable time for review and mitigation before public disclosure. If the issue involves local data, local artifacts, or research material, avoid making that material public while the issue is being reviewed.

---

## Repository Checks

The repository may use lightweight CI and repository-safety checks for issues such as merge conflict markers, accidentally tracked `.env`-style files, private key material, dependency installation failures, or basic linting problems.

These checks are useful safeguards for a research-facing repository, but they are not full production-grade security scanning.

Contributors should still manually review workflow permissions, dependency changes, notebook outputs, artifact changes, local demo behavior, and any file that may expose private paths, secrets, or local-only research material.

Repository security should not rely solely on built-in GitHub alerts or lightweight repository checks.

---

## Response Approach

The maintainer will aim to:

1. acknowledge the report,
2. assess whether it is security-relevant,
3. reproduce the issue when possible,
4. evaluate severity and repository impact,
5. apply a fix or mitigation when appropriate,
6. and document the mitigation if needed.

Because this is a research repository and not a staffed production service, response times may vary.

---

## Practical Security Hygiene

Before opening a contribution, review especially carefully if it touches:

- secrets handling,
- file I/O,
- notebook execution behavior,
- exported artifacts,
- graph exports,
- controlled subset outputs,
- demo bundles,
- model artifacts,
- dependency updates,
- GitHub Actions configuration,
- or the local Django demo.

Good security hygiene includes reviewing notebook outputs before committing, avoiding broad file-glob loading when explicit paths are safer, keeping dependencies reasonably up to date, inspecting generated CSVs and figures before committing, and preferring explicit, reviewable code paths over unsafe convenience shortcuts.

If you believe you have found a genuine security issue, please report it privately.
