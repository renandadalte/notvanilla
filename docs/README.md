# NotVanilla — technical documentation

This folder follows [Diátaxis](https://diataxis.fr/): separate **tutorial** intent (learning), **how-to** (tasks), **explanation** (understanding), and **reference** (facts). For a Fabric packwiz repository, we keep a thin, practical slice so the **GitHub repo remains the single source of truth** for manifests, client/server installs, and documentation.

## Map

| Doc | Diátaxis role | Purpose |
| --- | --- | --- |
| [MODS_INVENTORY.md](./MODS_INVENTORY.md) | **Reference** | Three tables: **active** (packwiz), **listed** (backlog), **discarded** (audit); same columns, no status column |
| [DEVELOPMENT.md](./DEVELOPMENT.md) | **How-to** | Day-to-day pack maintenance: packwiz, index, changelog, server sync |
| This file | **Explanation** | Why we document this way; pointers for future modpacks |

## Single source of truth

1. **Pack manifests:** `pack.toml`, `index.toml`, `mods/*.pw.toml` define what is actually shipped.
2. **Human-readable inventory:** `docs/MODS_INVENTORY.md` — **Active** table must match `mods/*.pw.toml` after any ship change; **Listed** / **Discarded** are maintained in prose.
3. **Player-facing history:** root `CHANGELOG.md` for visible release notes.

Reusing this layout on **other packwiz modpacks**: copy `docs/README.md`, `docs/MODS_INVENTORY.md` (reset the table), and `docs/DEVELOPMENT.md` (adjust paths and server layout). Keep the same column schema in `MODS_INVENTORY.md`.

## Agent workflow

Cursor agents should read `~/.cursor/skills/packwiz-modpack-documentation/SKILL.md` when editing mods or documentation so the inventory table stays aligned with the repository without the author having to repeat the request each time.
