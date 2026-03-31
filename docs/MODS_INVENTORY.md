# Mod inventory (reference)

**Canonical technical list** for the NotVanilla pack. **Truth for binaries and versions** lives in `pack.toml`, `index.toml`, `mods/*.pw.toml`, and `shaderpacks/*.pw.toml`. The **Active mods** table is **reconciled** with those manifests whenever the mod or shader set changes.

| Pack version | Minecraft | Fabric loader | Active rows (mods + shader packs) | Listed | Discarded |
| --- | --- | --- | --- | --- | --- |
| `0.0.5-alpha` (see `pack.toml`) | `1.21.1` | `0.18.4` | 19 (18 + 1) | 0 | 0 |

## Three tables

| Table | Meaning |
| --- | --- |
| **Active mods** | Shipped in the repo: one row per `mods/*.pw.toml` **and** `shaderpacks/*.pw.toml`. |
| **Listed mods** | Under evaluation or planned; **not** in packwiz yet (watchlist / backlog). |
| **Discarded mods** | Explicitly rejected or removed from the pack; kept for audit (include date and reason in **Notes**). |

## Column definitions

Same columns in all three tables (no **Status** column — the section implies state).

| Column | Meaning |
| --- | --- |
| **Mod** | Display name (matches `name` in `.pw.toml` for active rows when possible). |
| **Page** | Primary project page (Modrinth `https://modrinth.com/mod/<slug>` or `https://modrinth.com/shader/<slug>`). |
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
| Architectury API | [modrinth.com/mod/architectury-api](https://modrinth.com/mod/architectury-api) | Library | both | high | — | Observable | — | Cross-loader abstraction; keep if any dependent mod remains. |
| Entity Culling | [modrinth.com/mod/entityculling](https://modrinth.com/mod/entityculling) | Optimization, Rendering | client | high | — | — | — | Reduces entity render work client-side. |
| Fabric API | [modrinth.com/mod/fabric-api](https://modrinth.com/mod/fabric-api) | Library, Core | both | very high | — | (Fabric ecosystem) | — | Required baseline for almost all Fabric mods. |
| Fabric Language Kotlin | [modrinth.com/mod/fabric-language-kotlin](https://modrinth.com/mod/fabric-language-kotlin) | Library | both | high | — | Observable | — | Kotlin language adapter; needed by Kotlin mods. |
| FerriteCore | [modrinth.com/mod/ferrite-core](https://modrinth.com/mod/ferrite-core) | Optimization | both | high | — | — | — | Memory footprint reductions for models/collections. |
| ImmediatelyFast | [modrinth.com/mod/immediatelyfast](https://modrinth.com/mod/immediatelyfast) | Optimization, Rendering | client | high | — | — | — | Client-side immediate-mode rendering optimizations. |
| Indium | [modrinth.com/mod/indium](https://modrinth.com/mod/indium) | Library, Rendering | client | high | Sodium | — | — | Compatibility layer when using Sodium with Fabric Rendering API consumers. |
| Iris Shaders | [modrinth.com/mod/iris](https://modrinth.com/mod/iris) | Rendering, Shaders | client | high | Sodium | — | — | Shader loader paired with Sodium; enable packs under **Video Settings → Shader Packs**. |
| Krypton | [modrinth.com/mod/krypton](https://modrinth.com/mod/krypton) | Optimization, Networking | both | medium | — | — | Rare proxy/pipeline interactions | Micro-optimizes Minecraft networking; validate on your host if using unusual proxies. |
| Lithium | [modrinth.com/mod/lithium](https://modrinth.com/mod/lithium) | Optimization | both | very high | — | — | — | Server/game logic optimizations without changing vanilla mechanics. |
| MakeUp - Ultra Fast | [modrinth.com/shader/makeup-ultra-fast-shaders](https://modrinth.com/shader/makeup-ultra-fast-shaders) | Shaders | client | high | Iris Shaders | — | — | Baseline **lightweight** shader (v9.4c); strong quality/perf ratio—lower settings inside the shader if FPS dips. Ships as `shaderpacks/*.pw.toml`. |
| Mod Menu | [modrinth.com/mod/modmenu](https://modrinth.com/mod/modmenu) | QoL, UI | client | high | Fabric API, Text Placeholder API | — | — | In-game mod list; entry points to config screens where mods register them. |
| ModernFix | [modrinth.com/mod/modernfix](https://modrinth.com/mod/modernfix) | Optimization | both | very high | — | — | — | Broad startup/memory/perf improvements. |
| Observable | [modrinth.com/mod/observable](https://modrinth.com/mod/observable) | Diagnostics | both | medium | Architectury API, Fabric Language Kotlin | — | — | Profiling/inspection tooling; align with pack debugging goals. |
| Text Placeholder API | [modrinth.com/mod/placeholder-api](https://modrinth.com/mod/placeholder-api) | Library | both | high | — | Mod Menu | — | Required by **Mod Menu**; useful for mods that expose placeholder-driven text. |
| Sodium | [modrinth.com/mod/sodium](https://modrinth.com/mod/sodium) | Optimization, Rendering | client | very high | — | Indium, Iris Shaders | — | Client rendering engine; pair with Indium when mods need FRAPI; required by Iris. |
| spark | [modrinth.com/mod/spark](https://modrinth.com/mod/spark) | Diagnostics | both | medium | — | — | — | Profiling (`/spark`, `/sparkc`); diagnostic, not part of routine benchmark flow per README. |
| Wall-Jump TXF | [modrinth.com/mod/wall-jump-txf](https://modrinth.com/mod/wall-jump-txf) | Movement, Gameplay | both | medium | — | — | — | Wall jump, double jump, fence jump; **client + server** for multiplayer. |
| Yet Another Config Lib | [modrinth.com/mod/yacl](https://modrinth.com/mod/yacl) | Library, UI | both | high | Fabric API | — | — | Config GUI library for mods that use YACL (complements **Cloth Config** when present on other branches). |

## Listed mods

Candidates or planned additions **without** a `mods/*.pw.toml` or `shaderpacks/*.pw.toml` yet. When one ships, move the row to **Active mods** and remove it from here.

| Mod | Page | Categories | Environment | Priority | Dependencies | Dependents | Incompatibilities | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| — | — | — | — | — | — | — | — | *No entries yet. Remove this row when adding the first listed mod.* |

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
Architectury API ──┐
Fabric Language Kotlin ──┴──► Observable
Text Placeholder API ──► Mod Menu
```

## Reconciliation

- **Last reconciled:** 2026-03-31 — **Active** rows vs `mods/*.pw.toml` (18) + `shaderpacks/*.pw.toml` (1), `pack.toml` `0.0.5-alpha`; **Listed** / **Discarded** counts updated manually.
- After every manifest change, bump **Last reconciled** and verify **Active** row count vs `mods/*.pw.toml` and `shaderpacks/*.pw.toml`.
