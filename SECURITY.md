# Security Policy

## Supported Scope

This repository is an academic/research codebase and is not currently maintained as a production service.

Security issues are still taken seriously, especially if they involve:

- accidental exposure of secrets,
- unsafe handling of credentials,
- supply-chain risks in dependencies,
- unsafe file handling,
- code execution vulnerabilities,
- or leakage of private research artifacts.

---

## Reporting a Vulnerability

Please do **not** open a public issue for sensitive security problems.

Instead, report the issue privately to the maintainer with:

- a clear description of the vulnerability,
- steps to reproduce it,
- the affected file(s) or workflow(s),
- and, if possible, a suggested mitigation.

Please provide enough detail for the issue to be reproduced and verified.

---

## What to Report

Examples of relevant reports include:

- exposed API keys, tokens, or secrets,
- insecure GitHub Actions workflows,
- vulnerable dependency usage,
- unsafe deserialization or code execution patterns,
- path traversal / file overwrite risks,
- accidental publication of non-public research assets,
- leakage of sensitive local environment configuration.

---

## What Is Out of Scope

The following are generally out of scope unless they create a real security risk:

- notebook modeling mistakes,
- metric underperformance,
- scientific limitations of a model,
- documentation typos,
- non-sensitive reproducibility issues.

These should be reported through normal repository issues instead.

---

## Dependency and Workflow Safety

This repository may use GitHub Actions and Python dependencies.

When reporting security issues related to dependencies or CI/CD, please specify:

- the affected package or workflow,
- the impacted version,
- and whether the issue affects:
  - local execution,
  - CI pipelines,
  - or public repository exposure.

---

## Data and Research Asset Safety

This repository uses the **DaKS synthetic wind power dataset** for research purposes.

Security reports may also include cases where:

- repository structure exposes unintended processed artifacts,
- generated files reveal information that should remain private,
- or publication settings unintentionally disclose internal research material.

---

## Response Approach

The maintainer will aim to:

1. acknowledge the report,
2. assess severity,
3. reproduce the issue,
4. apply a fix when appropriate,
5. and document the mitigation if needed.

Because this is a research repository, response times may vary.

---

## Disclosure Policy

Please allow time for the issue to be reviewed and fixed before public disclosure.

Responsible disclosure is appreciated.