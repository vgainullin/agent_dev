# Development journal

## Summary

_Updated: 2026-10-15 · through 311b0f6_

- **State:** Template scaffold complete and passing locally: agent rules, required Ponytail, uv/ruff/pyright/pytest, pre-commit, CI, journal publishing. Not yet run on GitHub.
- **Decisions:**
  - Only the journal is published to Pages, never the repo. [2026-10-15](journal/2026-10-15-bootstrap.md)
  - Ponytail is loaded as a plugin, not vendored. [2026-10-15](journal/2026-10-15-bootstrap.md)
  - Ruff `S311` ignored for scientific RNG use. [2026-10-15](journal/2026-10-15-bootstrap.md)
- **Results:** none yet.
- **Open:**
  - First CI and journal workflow runs on GitHub.
  - Plugin auto-enable via `.claude/settings.json` untested.
  - Actions pinned to major versions, not SHAs.

## Entries

- [2026-10-15: Bootstrap](journal/2026-10-15-bootstrap.md): template scaffold, required Ponytail, journal and historian.
