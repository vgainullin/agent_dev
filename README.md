# agent_dev

Template for scientific Python projects built with coding agents. Agent rules live in [`AGENTS.md`](AGENTS.md); [Ponytail](https://github.com/DietrichGebert/ponytail) is required.

## Use

1. **Use this template** on GitHub, then clone.
2. Rename the package: `git mv src/agent_dev src/<name>`, then replace `agent_dev` / `agent-dev` in `pyproject.toml` and `tests/`.
3. Set up:
   ```bash
   uv sync
   uv run pre-commit install
   uv run pytest
   ```
4. Install Ponytail for your agent (`AGENTS.md` §0). Claude Code picks it up from `.claude/settings.json`.
5. To publish the journal: Settings → Pages → Source: **GitHub Actions**.

## Layout

| Path | Purpose |
|---|---|
| `AGENTS.md` | Rules for all agents. `CLAUDE.md` imports it. |
| `src/agent_dev/` | Package; `seed_everything()` seeds Python, NumPy, PyTorch. |
| `tests/` | pytest + hypothesis. |
| `.pre-commit-config.yaml` | ruff, pyright, fast tests, nbstripout, secret check. |
| `.github/workflows/ci.yml` | Same checks on push and PR. |
| `JOURNAL.md`, `journal/` | Development journal: summary plus dated entries, kept by `.claude/agents/historian.md`. |
| `.github/workflows/journal.yml` | Publishes the journal (only) to GitHub Pages on merge to `main`. |
