# Security Policy

## Scope and Repository Context

**WindPower_DigitalTwin** is a **research repository** for **spatio-temporal wind power forecasting** on the **DaKS / Kassel synthetic wind power dataset**.

This repository supports:

- reproducible forecasting research,
- thesis-oriented academic work,
- benchmark-safe experimentation,
- downstream diagnostics analysis,
- and future graph-based, sequence-based, or broader health-aware research extensions.

It is **not** maintained as a production service, deployed platform, or security-hardened operational system.

Even so, security issues are taken seriously, especially when they affect:

- secrets or credentials,
- repository workflows,
- dependency safety,
- unsafe code execution paths,
- accidental disclosure of non-public research material,
- or unintended exposure of local or processed artifacts.

---

## How to Report a Security Issue

Please do **not** open a public issue for sensitive security problems.

Instead, report the issue privately to the maintainer and include:

- a clear description of the issue,
- why it is a security problem,
- steps to reproduce it,
- the affected file(s), notebook(s), script(s), dependency, or workflow(s),
- the potential impact,
- and, if possible, a suggested mitigation.

Please include enough detail for the issue to be reproduced and verified.

---

## What Should Be Reported

Examples of relevant security reports include:

- exposed API keys, tokens, passwords, or secrets,
- accidental commit of `.env`-like local configuration,
- insecure GitHub Actions workflows,
- vulnerable dependency usage,
- unsafe deserialization,
- unsafe shell execution or arbitrary code execution risks,
- path traversal, unsafe overwrite, or unsafe file-loading behavior,
- notebook or script logic that may unintentionally execute untrusted input,
- accidental publication of restricted research assets,
- unintended exposure of local paths, private metadata, or internal outputs,
- or repository artifacts that reveal information that should not be public.

Security-relevant data handling issues may also include cases where:

- raw dataset material is committed when it should not be,
- processed artifacts expose unintended information,
- local rerun outputs reveal private workspace details,
- or repository configuration makes sensitive files too easy to publish by mistake.

---

## What Is Usually Out of Scope

The following are generally **not** security issues unless they create a real and credible security risk:

- notebook modeling mistakes,
- poor benchmark performance,
- metric underperformance,
- forecasting residual structure,
- scientific limitations of a method,
- documentation typos,
- ordinary reproducibility problems,
- disagreement about methodology,
- or the fact that a model is not robust enough for a research claim.

These should normally be reported through standard repository issues, discussions, or documentation updates.

---

## Dependency and Workflow Safety

This repository may use:

- Python dependencies,
- Jupyter notebooks,
- GitHub Actions,
- and local research workflows for reruns and exported artifacts.

When reporting a dependency or CI/CD issue, please specify:

- the affected package, action, or workflow,
- the impacted version,
- the file or job where it appears,
- and whether the issue affects:
  - local execution,
  - CI pipelines,
  - repository integrity,
  - or public exposure.

Useful examples include:

- known vulnerable packages,
- unsafe workflow permissions,
- unpinned or risky action usage,
- secret exposure through workflow logs,
- or notebook execution paths that behave unsafely in automation.

---

## Data and Research Asset Safety

This repository uses the **DaKS synthetic wind power dataset** for research purposes.

The repository is intended to prioritize **reproducibility of the pipeline**, not unrestricted redistribution of all local data artifacts.

Security-relevant reports may include cases where:

- restricted or unintended dataset material is published,
- processed outputs expose information that should remain private,
- generated artifacts reveal local environment details,
- figures, logs, or exports disclose unintended internal information,
- or repository structure makes accidental publication of research assets more likely.

If you report a problem in this area, please describe clearly:

- what artifact is exposed,
- whether it is raw, processed, or derived,
- whether it is already public,
- and what the disclosure risk actually is.

---

## Responsible Disclosure Expectations

Please allow reasonable time for the issue to be reviewed and fixed before public disclosure.

Responsible disclosure is appreciated.

If the issue involves live secrets or exposed credentials, please avoid copying them into public channels.  
If possible, rotate or invalidate exposed credentials immediately after reporting them.

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
- keep dependencies reasonably up to date,
- inspect workflow changes carefully,
- and prefer explicit, reviewable code paths over unsafe convenience shortcuts.

If a contribution touches:

- secrets handling,
- file I/O,
- notebook execution behavior,
- exported artifacts,
- dependency updates,
- or GitHub Actions configuration,

please review it with extra care before opening a PR.

---

## Final Note

This repository is research-facing and thesis-facing, not production-facing.

That does **not** reduce the importance of:

- credential safety,
- workflow integrity,
- dependency hygiene,
- responsible artifact handling,
- and careful disclosure of non-public research material.

If you believe you have found a genuine security issue, please report it privately.