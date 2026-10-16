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

## GitHub push and CI fix

Commits: ebcb675..f95d14c

### Changed
- Pushed to github.com/vgainullin/agent_dev; local commits rebased onto the remote's `Initial commit` (3560c62). README conflict resolved in favor of the template README; journal SHAs updated to rebased ones.
- `README.md`: setup step to set Pages source to GitHub Actions; layout rows for the journal.
- `.claude/agents/historian.md`: entries name files in backticks and link only other entries, since only the journal is published.
- `.github/workflows/ci.yml`: `astral-sh/setup-uv` pinned to commit 1c37ad0 (v10.3.0).

### Why
- `setup-uv` has no floating `v10` tag upstream, only full versions (v10.0.0 to v10.3.0). Pinned to the commit SHA rather than a version tag, so the ref is immutable.

### Results
- CI on GitHub passes at f95d14c: ruff, format check, pyright, pytest (run 38851263361, 19 s).

### Negative results
- CI at ebcb675 failed at "Set up job": `Unable to resolve action astral-sh/setup-uv@v10` (run 38851139976).
- Journal workflow at ebcb675 failed at `actions/configure-pages`: Pages site Not Found, because Pages is not enabled on the repo (run 38851140058). Expected until the Pages source is set to GitHub Actions.

### Open
- Enable Pages (Settings → Pages → Source: GitHub Actions), then rerun the journal workflow.
- Mark the repo as a template (Settings → Template repository); manual step.
- Plugin auto-enable through `.claude/settings.json` still untested (unverified).
- Other actions still pinned to major tags, not SHAs.
- Runners warn that `ubuntu-latest` moves to Ubuntu 26 from 2026-10-19.

## Template and Pages enabled

Commits: none since 81dcd18 (repo settings only)

### Changed
- Repo settings on GitHub (set by the user, not in git): template repository on, Pages on.

### Why
- Closes two manual setup steps left open in [GitHub push and CI fix](#github-push-and-ci-fix): the repo can be used as a template, and the journal workflow can publish.

### Results
- Public GitHub API for vgainullin/agent_dev: `is_template=true`, `has_pages=true` (checked by caller, 2026-10-15).
- Pages source set to GitHub Actions (unverified; `has_pages` does not show the build source).

### Negative results
- none

### Open
- Confirm the journal workflow publishes on this commit once it reaches `main`.
