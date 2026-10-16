# 2026-10-15: Bootstrap

Commits: 7e7f298..311b0f6

## Changed
- Agent rules in `AGENTS.md`; `CLAUDE.md` imports them.
- Ponytail required; Claude Code enables it via `.claude/settings.json`.
- uv + lockfile, ruff, strict pyright on `src/`, pytest + hypothesis, pre-commit, CI workflow.
- `seed_everything()` seeds Python, NumPy, PyTorch from one value, with a property-based test.
- Development journal: `historian` agent, this file format, Pages publishing via `journal.yml`.

## Why
- Ponytail loaded as a plugin, not vendored: avoids double-loading and drift, keeps its review/audit/debt commands. Rejected: copying its rules into AGENTS.md.
- Ruff rule `S311` ignored: non-crypto RNGs are standard in scientific code.
- Only the journal is published, not the repo, so private code and data never reach Pages.

## Results
- Local: ruff, pyright (0 errors), pytest (1 passed), all pre-commit hooks pass.

## Negative results
- none

## Open
- CI and journal workflows not yet run on GitHub (unverified).
- Plugin auto-enable through `.claude/settings.json` not tested (unverified).
- Actions pinned to major versions, not commit SHAs.
