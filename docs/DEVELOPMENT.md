# Development — maintaining the pack

## Prerequisites

- [packwiz](https://packwiz.infra.link/) installed (`packwiz refresh`, `packwiz update`, etc.)
- Minecraft version and Fabric loader pinned in `pack.toml` (see `[versions]`)

## Changing the mod set

1. Add, remove, or edit files under `mods/*.pw.toml` (and optional `optional/` / disabled layouts if you adopt them later).
2. Run **`packwiz refresh`** from the repository root so `index.toml` hashes match the tree.
3. Update **`docs/MODS_INVENTORY.md`** in the same change set: **Active** rows ↔ `mods/*.pw.toml`; adjust **Listed** / **Discarded** if the conversation moves mods between backlog and shipped.
4. Update **`CHANGELOG.md`** when the change is user-visible (new mod, removal, fix).
5. Follow deploy rules in `~/.agents/context/NOTVANILLA_MODPACK.md` for dedicated server alignment (never push without explicit confirmation in chat).

## Conventions

- **`side` in `.pw.toml`:** `client`, `server`, or `both` — authoritative for client-only installs vs server.
- **Mod page URL:** Prefer stable project pages (e.g. Modrinth `https://modrinth.com/mod/<slug>`). The `.pw.toml` `[update.modrinth]` block holds the project id for tooling.
- **Discarded mods:** When a mod leaves the pack, remove its `.pw.toml`, add a row under **Discarded mods** (date + reason in **Notes**), and remove it from **Active**. **Listed** is for candidates not yet in packwiz.

## Quality checks before merge

- [ ] `packwiz refresh` run; `index.toml` committed if it changed.
- [ ] `docs/MODS_INVENTORY.md` — **Active** row count matches `mods/*.pw.toml`.
- [ ] `CHANGELOG.md` updated if players care about the change.
