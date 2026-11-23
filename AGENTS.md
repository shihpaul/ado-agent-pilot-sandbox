# Codex pilot task boundary (instructions only)

This is a disposable repository intended for **one** explicitly owner-approved Codex Cloud task. A task has not yet been authorized. These instructions do not constitute execution permission.

If separately authorized to implement the task:
- Create or edit **only** `whitespace.py` and `tests/test_whitespace.py`.
- Implement `normalize_whitespace(text: str) -> str`: collapse each run of Unicode whitespace to a single ASCII space, trim leading/trailing whitespace, preserve all non-whitespace characters, and raise `TypeError` for any non-string input.
- Use the Python standard library only. Do not add dependencies, network calls, API usage, scripts, workflow edits, secrets, credentials, telemetry, or deployment configuration.
- Run `python -m unittest discover -s tests -v` and report the command and result.
- Work on a branch; propose a PR. Do not merge. Do not create a second PR or launch repairs without separate owner authorization; total permitted repair rounds, if later authorized, is at most two.

The repository owner independently verifies the PR diff, checks and any review evidence. A passing CI job alone does not grant approval.
