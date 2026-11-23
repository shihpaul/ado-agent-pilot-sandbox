# ADO agent pilot sandbox

**Disposable, public, non-sensitive test repository.** Not part of Agent Development Orchestrator's production repository. No user data, credentials, service connections, environment secrets, paid APIs, deployment, or autonomous dispatch.

This repository is only for a single, separately authorized Codex Cloud task: implement `normalize_whitespace(text: str) -> str` with comprehensive standard-library tests.

## Base repository

- `.github/workflows/ci.yml` is the read-only GitHub Actions check (`python-tests`).
- `tests/test_baseline.py` confirms the initial test runner works before the agent starts.
- `AGENTS.md` explains the proposed task restrictions. Instructions are **not** a substitute for GitHub permissions or protected branch rules.
- **Codex may create or modify only:** `whitespace.py` and `tests/test_whitespace.py`. The CI job checks this path allowlist on PRs.

The starting branch is `main`. The proposed agent branch is `codex/whitespace-pilot`. Never let the agent merge into `main`. Require the `python-tests` status on the latest PR head and a separately verified human exact-SHA acceptance before merging.

The owner must configure branch protection and inspect the Codex GitHub authorization screen before authorizing any coding task. No automatic Codex tasks are enabled by this starter.
