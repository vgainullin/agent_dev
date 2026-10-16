# Development journal

## Summary

_Updated: 2026-10-15 · through 81dcd18_

- **State:** Template scaffold on GitHub (vgainullin/agent_dev), marked as a template repository, Pages on. CI passes on GitHub: ruff, format check, pyright, pytest. Journal publishing not yet confirmed.
- **Decisions:**
  - Pin third-party actions to commit SHAs when no floating major tag exists (`setup-uv` v10.3.0). [2026-10-15](journal/2026-10-15-bootstrap.md#github-push-and-ci-fix)
  - Only the journal is published to Pages, never the repo. [2026-10-15](journal/2026-10-15-bootstrap.md)
  - Ponytail is loaded as a plugin, not vendored. [2026-10-15](journal/2026-10-15-bootstrap.md)
  - Ruff `S311` ignored for scientific RNG use. [2026-10-15](journal/2026-10-15-bootstrap.md)
- **Results:** none yet.
- **Open:**
  - Confirm the journal workflow publishes on this commit; Pages source = GitHub Actions unverified. [2026-10-15](journal/2026-10-15-bootstrap.md#template-and-pages-enabled)
  - Plugin auto-enable via `.claude/settings.json` untested.
  - Other actions pinned to major versions, not SHAs.

## Entries

- [2026-10-15: Template and Pages enabled](journal/2026-10-15-bootstrap.md#template-and-pages-enabled): repo marked as template and Pages on (settings only, no code).
- [2026-10-15: GitHub push and CI fix](journal/2026-10-15-bootstrap.md#github-push-and-ci-fix): pushed to GitHub, CI green after pinning setup-uv; Pages not yet enabled.
- [2026-10-15: Bootstrap](journal/2026-10-15-bootstrap.md): template scaffold, required Ponytail, journal and historian.
