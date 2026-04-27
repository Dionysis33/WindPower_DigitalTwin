# Security Policy

## Scope and Repository Context

**WindPower_DigitalTwin** is a **research repository** for **spatio-temporal wind power forecasting** on the **DaKS / Kassel synthetic wind power dataset**.

The repository supports:

- reproducible forecasting research,
- thesis-oriented academic work,
- benchmark-safe experimentation,
- downstream diagnostics analysis,
- graph-aware forecasting research,
- controlled graph refinement follow-up,
- and future health-aware / PHM-oriented research extensions.

It is **not** maintained as:

- a production service,
- a deployed platform,
- a security-hardened operational system,
- a production monitoring platform,
- a completed PHM system,
- a deployed digital twin,
- or an operational forecasting service.

Even so, security and artifact-safety issues are taken seriously, especially when they affect:

- secrets or credentials,
- repository workflows,
- dependency safety,
- unsafe code execution paths,
- unsafe file loading or path handling,
- accidental disclosure of non-public research material,
- accidental publication of raw or restricted dataset material,
- or unintended exposure of local, processed, diagnostic, graph, model, or demo artifacts.

---

## How to Report a Security Issue

Please do **not** open a public issue for sensitive security problems.

Instead, report the issue privately to the maintainer and include:

- a clear description of the issue,
- why it is a security problem,
- steps to reproduce it,
- the affected file(s), notebook(s), script(s), dependency, workflow, or local demo component,
- the potential impact,
- whether any credential, local file, dataset material, artifact, or private path is exposed,
- and, if possible, a suggested mitigation.

Please include enough detail for the issue to be reproduced and verified.

If the issue involves live secrets or exposed credentials, avoid copying them into public channels.

---

## What Should Be Reported

Examples of relevant security reports include:

- exposed API keys, tokens, passwords, credentials, or private keys,
- accidental commit of `.env`-like local configuration,
- insecure GitHub Actions workflow behavior,
- vulnerable dependency usage with credible repository impact,
- unsafe deserialization,
- unsafe shell execution or arbitrary code execution risks,
- unsafe notebook execution paths,
- path traversal,
- unsafe file loading,
- unsafe overwrite behavior,
- accidental publication of restricted research assets,
- accidental exposure of raw dataset material,
- unintended exposure of local paths, private metadata, or internal outputs,
- repository artifacts that reveal information that should not be public,
- local demo behavior that exposes files outside its intended artifact scope,
- or any change that makes sensitive files easier to publish by mistake.

Security-relevant data handling issues may also include cases where:

- raw dataset material is committed when it should remain local-only,
- processed artifacts expose unintended information,
- graph or diagnostics exports reveal private local paths or environment details,
- local rerun outputs reveal private workspace details,
- model artifacts or checkpoints are published unintentionally,
- demo bundles expose local-only files,
- or repository configuration weakens the intended artifact policy.

---

## What Is Usually Out of Scope

The following are generally **not** security issues unless they create a real and credible security risk:

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
- or the fact that a model is not robust enough for a research claim.

These should normally be reported through standard repository issues, discussions, pull requests, or documentation updates.

A methodological problem becomes security-relevant only when it also creates a credible risk such as unsafe execution, credential exposure, unintended artifact disclosure, unsafe file access, or accidental publication of restricted material.

---

## Dependency and Workflow Safety

This repository may use:

- Python dependencies,
- Jupyter notebooks,
- GitHub Actions,
- local research workflows,
- local artifact exports,
- and a local-only Django demo helper.

When reporting a dependency or CI/CD issue, please specify:

- the affected package, action, or workflow,
- the impacted version,
- the file or job where it appears,
- and whether the issue affects:
  - local execution,
  - CI pipelines,
  - repository integrity,
  - artifact safety,
  - or public exposure.

Useful examples include:

- known vulnerable packages with credible repository impact,
- unsafe workflow permissions,
- unpinned or risky action usage,
- secret exposure through workflow logs,
- unsafe dependency update behavior,
- notebook execution paths that behave unsafely in automation,
- or CI checks that accidentally reveal private file paths or local artifact details.

Dependency and workflow reports should focus on practical repository risk rather than theoretical vulnerability lists with no credible impact on this project.

---

## Notebook Execution Safety

The notebooks in this repository are part of a research and thesis-facing workflow.

Security-relevant notebook issues may include:

- execution of untrusted input,
- unsafe shell commands,
- unsafe file writes,
- unsafe overwrite behavior,
- accidental mutation of canonical artifacts,
- accidental exposure of local paths or environment variables,
- output cells that reveal private information,
- or notebook logic that makes restricted files easier to commit by mistake.

Notebook changes should preserve:

- deterministic execution where possible,
- explicit file paths,
- benchmark-safe artifact handling,
- clear separation between raw, processed, diagnostics, graph, model, and demo artifacts,
- and no hidden execution behavior that could expose private local state.

Notebook modeling limitations, weak results, or scientific disagreements should not be treated as security issues unless they also create a concrete safety or disclosure risk.

---

## Data and Research Asset Safety

This repository uses the **DaKS synthetic wind power dataset** for research purposes.

The repository is intended to prioritize **reproducibility of the pipeline**, not unrestricted redistribution of all local data artifacts.

Security-relevant reports may include cases where:

- restricted or unintended dataset material is published,
- raw data files are committed accidentally,
- processed outputs expose information that should remain private,
- generated artifacts reveal local environment details,
- figures, logs, or exports disclose unintended internal information,
- model artifacts or checkpoints are committed unintentionally,
- graph exports expose unintended metadata,
- demo bundles include files outside their intended scope,
- or repository structure makes accidental publication of research assets more likely.

If you report a problem in this area, please describe clearly:

- what artifact is exposed,
- where it appears,
- whether it is raw, processed, derived, diagnostic, graph-related, model-related, or demo-related,
- whether it is already public,
- whether it contains private paths, metadata, credentials, restricted material, or local-only outputs,
- and what the disclosure risk actually is.

---

## Artifact Safety Policy

The repository separates artifacts conceptually into:

- raw / local dataset files,
- processed pipeline outputs,
- canonical benchmark artifacts,
- local prediction exports,
- diagnostics exports,
- graph verification / graph packaging / graph experiment outputs,
- model artifacts,
- thesis / report-facing figures,
- and local demo bundles.

Security and artifact-safety handling should respect the following principles:

- raw dataset files should remain local unless explicitly permitted and documented,
- large rerun outputs should remain local-only by default,
- local prediction, diagnostics, graph, and demo outputs should not be treated as automatic public artifacts,
- model binaries, checkpoints, and training-state files should remain local-only by default,
- `data/processed/baseline_metrics.csv` is a benchmark artifact, not a container for secrets or private metadata,
- report-facing figures should be intentionally selected and reviewed before committing,
- local paths and environment details should not be exposed in committed artifacts,
- and demo bundles should contain only curated, intended, non-sensitive local exports.

Artifact-safety issues should be reported when a file or workflow makes unintended publication, disclosure, or mutation more likely.

---

## Local Django Demo Safety

The optional `django_demo/` directory is intended only as a **local-only, read-only, non-production, thesis-facing helper** for artifact inspection and presentation.

It should be interpreted as:

- a local presentation helper,
- a thesis-facing artifact browser,
- and a read-only interface over curated exported artifacts.

It should **not** be treated as:

- a deployed service,
- a security-hardened platform,
- a production monitoring system,
- a PHM system,
- a deployed digital twin,
- an operational forecasting service,
- a model-training interface,
- or a benchmark-generation system.

Security-relevant issues involving the local demo may include:

- accidental exposure of local artifacts,
- unsafe file loading,
- path traversal or unsafe path handling,
- unintended write access to benchmark or processed artifacts,
- accidental disclosure of private local paths or metadata,
- exposure of raw dataset files through the demo,
- inclusion of unintended files in demo bundles,
- unsafe configuration for public hosting,
- or behavior that exposes local research assets beyond the intended local environment.

Changes to the local demo should preserve its local-only and read-only role.

The demo should not, by default:

- trigger notebook reruns,
- train models,
- rewrite benchmark results,
- mutate processed artifacts,
- modify canonical outputs,
- expose raw dataset files,
- or behave like a deployed monitoring platform.

If the demo is run locally, it should be treated as a development / presentation helper and not as a public service.

---

## Secrets and Local Configuration

Contributors should not commit:

- `.env` files,
- API tokens,
- passwords,
- private keys,
- access credentials,
- local database files containing private data,
- local machine paths that reveal sensitive information,
- or private configuration files.

If a secret is accidentally committed:

1. remove it from the repository,
2. rotate or invalidate the exposed credential,
3. check whether it appeared in logs, artifacts, notebook outputs, or workflow output,
4. and report the issue privately if exposure may have occurred.

Do not paste live credentials into public issues, pull requests, comments, notebook outputs, screenshots, or logs.

---

## GitHub Actions and Repository Checks

The repository may use lightweight CI and repository-safety checks.

These checks can help detect obvious issues such as:

- merge conflict markers,
- accidentally tracked `.env`-style files,
- private key material,
- dependency installation failures,
- or basic Python linting problems.

These checks are useful safeguards for a research-facing repository, but they should not be interpreted as full production-grade security scanning.

Contributors should still manually review:

- workflow permissions,
- dependency changes,
- notebook outputs,
- artifact changes,
- local demo behavior,
- and any file that may expose private paths, secrets, or local-only research material.

---

## Responsible Disclosure Expectations

Please allow reasonable time for the issue to be reviewed and fixed before public disclosure.

Responsible disclosure is appreciated.

If the issue involves live secrets or exposed credentials:

- do not copy them into public channels,
- rotate or invalidate them as soon as possible,
- and report the exposure privately.

If the issue involves local data, local artifacts, or research material, please avoid making the material public while the issue is being reviewed.

---

## Response Approach

The maintainer will aim to:

1. acknowledge the report,
2. assess whether it is genuinely security-relevant,
3. reproduce the issue when possible,
4. evaluate severity and repository impact,
5. apply a fix or mitigation when appropriate,
6. and document the mitigation if needed.

Because this is a research repository and not a staffed production service, response times may vary.

---

## Practical Security Hygiene for Contributors

Contributors are encouraged to follow these basic practices:

- do not commit secrets, tokens, or credentials,
- do not publish local `.env` files,
- review notebook outputs before committing them,
- avoid committing large raw or private artifacts by accident,
- review generated CSVs, figures, manifests, and demo bundles before committing,
- keep dependencies reasonably up to date,
- inspect workflow changes carefully,
- avoid unsafe shell execution,
- avoid broad file-glob loading when a narrower explicit path is safer,
- and prefer explicit, reviewable code paths over unsafe convenience shortcuts.

If a contribution touches:

- secrets handling,
- file I/O,
- notebook execution behavior,
- exported artifacts,
- graph exports,
- demo bundles,
- model artifacts,
- dependency updates,
- GitHub Actions configuration,
- or the local Django demo,

please review it with extra care before opening a PR.

---

## Current Code Scanning Note

At the current repository setup, built-in GitHub code scanning alerts are not relied upon as an active security layer.

For this reason, the repository may use lightweight repository-level substitute checks focused on obvious security hygiene risks, such as accidental secret exposure, unsafe merge remnants, or CI-detectable regressions.

These checks are intended as minimal safeguards for a research-facing repository and should not be interpreted as equivalent to full production-grade security scanning.

---

## Final Note

This repository is research-facing and thesis-facing, not production-facing.

That does **not** reduce the importance of:

- credential safety,
- workflow integrity,
- dependency hygiene,
- responsible artifact handling,
- local demo safety,
- and careful disclosure of non-public research material.

If you believe you have found a genuine security issue, please report it privately.