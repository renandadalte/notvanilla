# Mod inventory (reference)

**Canonical technical list** for the NotVanilla pack. **Truth for binaries and versions** lives in `pack.toml`, `index.toml`, `mods/*.pw.toml`, `shaderpacks/*.pw.toml`, and `resourcepacks/*.pw.toml`. The **Active mods** table is **reconciled** with those manifests whenever the mod or shader set changes.

| Pack version | Minecraft | Fabric loader | Active rows (mods + shader packs + resource packs) | Listed | Discarded |
| --- | --- | --- | --- | --- | --- |
| `0.0.5-alpha` (see `pack.toml`) | `1.21.1` | `0.18.4` | 30 (27 + 1 + 2) | 1 | 0 |

## Three tables

| Table | Meaning |
| --- | --- |
| **Active mods** | Shipped in the repo: one row per `mods/*.pw.toml`, `shaderpacks/*.pw.toml`, and `resourcepacks/*.pw.toml`. |
| **Listed mods** | Under evaluation or planned; **not** in packwiz yet (watchlist / backlog). |
| **Discarded mods** | Explicitly rejected or removed from the pack; kept for audit (include date and reason in **Notes**). |

## Column definitions

Same columns in all three tables (no **Status** column — the section implies state).

| Column | Meaning |
| --- | --- |
| **Mod** | Display name (matches `name` in `.pw.toml` for active rows when possible). |
| **Page** | Primary project page (Modrinth `mod`, `shader`, or `resourcepack` URL). |
| **Categories** | Functional tags: Optimization, Rendering, Library, Networking, Diagnostics, QoL, World Gen, Content, etc. |
| **Environment** | For **active**: from packwiz `side` (`client`, `server`, `both`). For **listed**/**discarded**: intended or last-known side. |
| **Priority** | Pack policy: `very high` → `very low`. |
| **Dependencies** | Other mods/libs the entry **requires** at runtime. |
| **Dependents** | Other mods **in this pack** (or common extensions) that rely on this entry; use `—` if none in-pack. |
| **Incompatibilities** | Known bad pairs or caveats. |
| **Notes** | Operational or design notes (for **discarded**, include removal/decision date and reason). |

## Active mods

<!-- TABLE_SCHEMA: Mod | Page | Categories | Environment | Priority | Dependencies | Dependents | Incompatibilities | Notes; sort A–Z by Mod. -->

| Mod | Page | Categories | Environment | Priority | Dependencies | Dependents | Incompatibilities | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Architectury API | [modrinth.com/mod/architectury-api](https://modrinth.com/mod/architectury-api) | Library | both | high | — | Leawind's Third Person, Observable | — | Cross-loader abstraction; required by Leawind's Third Person. |
| Better Combat | [modrinth.com/mod/better-combat](https://modrinth.com/mod/better-combat) | Combat, Animation | both | medium | Fabric API, Cloth Config API, Player Animator | — | — | Animated melee; **dev** test stack; server needs same JAR for multiplayer. |
| Cloth Config API | [modrinth.com/mod/cloth-config](https://modrinth.com/mod/cloth-config) | Library | both | high | — | Better Combat | — | Config API for mods that expose Cloth screens. |
| Countered's Smooth F5 | [modrinth.com/mod/countereds-smooth-f5](https://modrinth.com/mod/countereds-smooth-f5) | Camera, QoL | client | medium | — | — | — | Smooth camera transition when toggling third person. |
| Entity Culling | [modrinth.com/mod/entityculling](https://modrinth.com/mod/entityculling) | Optimization, Rendering | client | high | — | — | — | Reduces entity render work client-side. |
| Fabric API | [modrinth.com/mod/fabric-api](https://modrinth.com/mod/fabric-api) | Library, Core | both | very high | — | (Fabric ecosystem) | — | Required baseline for almost all Fabric mods. |
| Fabric Language Kotlin | [modrinth.com/mod/fabric-language-kotlin](https://modrinth.com/mod/fabric-language-kotlin) | Library | both | high | — | Observable | — | Kotlin language adapter; needed by Kotlin mods. |
| FerriteCore | [modrinth.com/mod/ferrite-core](https://modrinth.com/mod/ferrite-core) | Optimization | both | high | — | — | — | Memory footprint reductions for models/collections. |
| First Person Model | [modrinth.com/mod/first-person-model](https://modrinth.com/mod/first-person-model) | Animation, Rendering | client | medium | Fabric API, Not Enough Animations | — | — | Shows player body in first person; pair order with NEA on client. |
| Fresh Animations | [modrinth.com/resourcepack/fresh-animations](https://modrinth.com/resourcepack/fresh-animations) | Resource pack, Animation | client | medium | — | Fresh Animations: Player Extension | — | Base FA pack (v1.10.4 in manifest); ships as `resourcepacks/*.pw.toml`. In **Resource Packs**, place **Fresh Animations: Player Extension** **above** this entry (higher = wins overrides). |
| Fresh Animations: Player Extension | [modrinth.com/resourcepack/fa-player-extension](https://modrinth.com/resourcepack/fa-player-extension) | Resource pack, Animation | client | medium | Fresh Animations (in-pack) | — | — | Player animations in FA style; depends on **Fresh Animations** base in this pack. Ships as `resourcepacks/*.pw.toml`. |
| ImmediatelyFast | [modrinth.com/mod/immediatelyfast](https://modrinth.com/mod/immediatelyfast) | Optimization, Rendering | client | high | — | — | — | Client-side immediate-mode rendering optimizations. |
| Indium | [modrinth.com/mod/indium](https://modrinth.com/mod/indium) | Library, Rendering | client | high | Sodium | — | — | Compatibility layer when using Sodium with Fabric Rendering API consumers. |
| Iris Shaders | [modrinth.com/mod/iris](https://modrinth.com/mod/iris) | Rendering, Shaders | client | high | Sodium | — | — | Shader loader paired with Sodium; enable packs under **Video Settings → Shader Packs**. |
| Krypton | [modrinth.com/mod/krypton](https://modrinth.com/mod/krypton) | Optimization, Networking | both | medium | — | — | Rare proxy/pipeline interactions | Micro-optimizes Minecraft networking; validate on your host if using unusual proxies. |
| Leawind's Third Person | [modrinth.com/mod/leawind-third-person](https://modrinth.com/mod/leawind-third-person) | Camera, Utility | client | medium | Fabric API, Architectury API | — | Overlaps other camera mods | Chosen **third-person** stack for **dev**; tune crosshair offset vs Real Camera. |
| Lithium | [modrinth.com/mod/lithium](https://modrinth.com/mod/lithium) | Optimization | both | very high | — | — | — | Server/game logic optimizations without changing vanilla mechanics. |
| MakeUp - Ultra Fast | [modrinth.com/shader/makeup-ultra-fast-shaders](https://modrinth.com/shader/makeup-ultra-fast-shaders) | Shaders | client | high | Iris Shaders | — | — | Baseline **lightweight** shader (v9.4c); strong quality/perf ratio—lower settings inside the shader if FPS dips. Ships as `shaderpacks/*.pw.toml`. |
| Mod Menu | [modrinth.com/mod/modmenu](https://modrinth.com/mod/modmenu) | QoL, UI | client | high | Fabric API, Text Placeholder API | — | — | In-game mod list; entry points to config screens where mods register them. |
| ModernFix | [modrinth.com/mod/modernfix](https://modrinth.com/mod/modernfix) | Optimization | both | very high | — | — | — | Broad startup/memory/perf improvements. |
| Not Enough Animations | [modrinth.com/mod/not-enough-animations](https://modrinth.com/mod/not-enough-animations) | Animation | client | medium | — | First Person Model | — | Extra player/item animations; **required** by First Person Model. |
| Observable | [modrinth.com/mod/observable](https://modrinth.com/mod/observable) | Diagnostics | both | medium | Architectury API, Fabric Language Kotlin | — | — | Profiling/inspection tooling; align with pack debugging goals. |
| Omnidirectional Movement | [modrinth.com/mod/omnidirectional-movement](https://modrinth.com/mod/omnidirectional-movement) | Movement | both | medium | — | — | — | Strafe-style movement; **server + client** for multiplayer. |
| Player Animator | [modrinth.com/mod/playeranimator](https://modrinth.com/mod/playeranimator) | Library, Animation | both | high | — | Better Combat | — | Animation library for Better Combat and similar mods. |
| Real Camera | [modrinth.com/mod/real-camera](https://modrinth.com/mod/real-camera) | Camera | client | medium | Fabric API | — | Overlaps Leawind / Smooth F5 | Inertia-style camera; **dev** pairing with Leawind—reduce duplicate effects in config if needed. |
| Text Placeholder API | [modrinth.com/mod/placeholder-api](https://modrinth.com/mod/placeholder-api) | Library | both | high | — | Mod Menu | — | Required by **Mod Menu**; useful for mods that expose placeholder-driven text. |
| Sodium | [modrinth.com/mod/sodium](https://modrinth.com/mod/sodium) | Optimization, Rendering | client | very high | — | Indium, Iris Shaders | — | Client rendering engine; pair with Indium when mods need FRAPI; required by Iris. |
| spark | [modrinth.com/mod/spark](https://modrinth.com/mod/spark) | Diagnostics | both | medium | — | — | — | Profiling (`/spark`, `/sparkc`); diagnostic, not part of routine benchmark flow per README. |
| Wall-Jump TXF | [modrinth.com/mod/wall-jump-txf](https://modrinth.com/mod/wall-jump-txf) | Movement, Gameplay | both | medium | — | — | — | Wall jump, double jump, fence jump; **client + server** for multiplayer. |
| Yet Another Config Lib | [modrinth.com/mod/yacl](https://modrinth.com/mod/yacl) | Library, UI | both | high | Fabric API | — | — | Config GUI library for mods that use YACL; complements **Cloth Config API** in this pack. |

## Listed mods

Candidates or planned additions **without** a `mods/*.pw.toml`, `shaderpacks/*.pw.toml`, or `resourcepacks/*.pw.toml` yet. When one ships, move the row to **Active mods** and remove it from here.

| Mod | Page | Categories | Environment | Priority | Dependencies | Dependents | Incompatibilities | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ParCool! | [modrinth.com/mod/parcool](https://modrinth.com/mod/parcool) | Movement | both | low | — | — | — | Planned for movement stack; **no Fabric 1.21.1** file on Modrinth as of 2026-03-31 (NeoForge/Forge only for recent 1.21.1 builds). Re-evaluate if Fabric returns. |

## Discarded mods

Removed from the pack or rejected after evaluation. Do not delete rows casually; use **Notes** for decision date and rationale.

| Mod | Page | Categories | Environment | Priority | Dependencies | Dependents | Incompatibilities | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| — | — | — | — | — | — | — | — | *No entries yet. Remove this row when recording the first discarded mod.* |

## Dependency sketch (in-pack)

```text
Fabric API ─────────────────────────► (all Fabric mods)
Sodium ──► Indium
Sodium ──► Iris Shaders ──► shader packs (e.g. MakeUp - Ultra Fast)
Architectury API ──┬──► Leawind's Third Person
Fabric Language Kotlin ──┴──► Observable
Not Enough Animations ──► First Person Model
Cloth Config API ──┐
Player Animator ───┴──► Better Combat
Fresh Animations ──► Fresh Animations: Player Extension
Text Placeholder API ──► Mod Menu
```

## Reconciliation

- **Last reconciled:** 2026-03-31 — **Active** rows vs `mods/*.pw.toml` (27) + `shaderpacks/*.pw.toml` (1) + `resourcepacks/*.pw.toml` (2), `pack.toml` `0.0.5-alpha`; **Listed** 1 (ParCool!); **Discarded** 0.
- After every manifest change, bump **Last reconciled** and verify **Active** row count vs `mods/*.pw.toml`, `shaderpacks/*.pw.toml`, and `resourcepacks/*.pw.toml`.
