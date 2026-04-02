# Mod inventory (reference)

**Canonical technical list** for the NotVanilla pack. **Truth for binaries and versions** lives in `pack.toml`, `index.toml`, `mods/*.pw.toml`, `shaderpacks/*.pw.toml`, and `resourcepacks/*.pw.toml`. The **Active mods** table is **reconciled** with those manifests whenever the mod or shader set changes.

For a test-oriented grouping of the same pack into operational bundles, see [MOD_MODULES.md](./MOD_MODULES.md). This file stays alphabetical and canonical; the module map is for scoped testing and maintenance.

| Pack version | Minecraft | Fabric loader | Active rows (mods + shader packs + resource packs) | Listed | Discarded |
| --- | --- | --- | --- | --- | --- |
| `0.0.11-alpha` (see `pack.toml`) | `1.21.1` | `0.18.4` | 86 (83 + 1 + 2) | 6 | 2 |

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
| AFK Camera | [modrinth.com/mod/afk-camera](https://modrinth.com/mod/afk-camera) | QoL, Camera | client | medium | Fabric API | — | — | AFK third-person camera. |
| AppleSkin | [modrinth.com/mod/appleskin](https://modrinth.com/mod/appleskin) | QoL, UI | both | medium | Fabric API | — | — | Food/saturation preview. |
| Architectury API | [modrinth.com/mod/architectury-api](https://modrinth.com/mod/architectury-api) | Library | both | high | — | Leawind's Third Person, Observable, RightClickHarvest | — | Cross-loader abstraction. |
| Balm | [modrinth.com/mod/balm](https://modrinth.com/mod/balm) | Library | both | high | Fabric API | Crafting Tweaks, Client Tweaks, TrashSlot, KleeSlabs, Inventory Essentials | — | BlayTheNinth shared library. |
| Better Advancements | [modrinth.com/mod/better-advancements](https://modrinth.com/mod/better-advancements) | QoL, UI | client | medium | — | — | — | Advancements screen overhaul. |
| Better Combat | [modrinth.com/mod/better-combat](https://modrinth.com/mod/better-combat) | Combat, Animation | both | medium | Fabric API, Cloth Config API, Player Animator | — | — | Animated melee; server + client for MP. |
| Better Ping Display [Fabric] | [modrinth.com/mod/better-ping-display-fabric](https://modrinth.com/mod/better-ping-display-fabric) | QoL, UI | client | medium | — | — | — | Tab list ping display. |
| Better Statistics Screen | [modrinth.com/mod/better-stats](https://modrinth.com/mod/better-stats) | QoL, UI | both | medium | Fabric API, TCDCommons API | — | — | Statistics UI improvements. |
| BetterF3 | [modrinth.com/mod/betterf3](https://modrinth.com/mod/betterf3) | QoL, Diagnostics | client | low | Cloth Config API | — | — | F3 overlay tweaks. |
| Call Your Horse | [modrinth.com/mod/call-your-horse](https://modrinth.com/mod/call-your-horse) | Gameplay, QoL | both | medium | — | — | — | Summon owned horse. |
| Clean Tooltips | [modrinth.com/mod/clean-tooltips](https://modrinth.com/mod/clean-tooltips) | QoL, UI | client | medium | Forge Config API Port | — | — | Tooltip layout; client-side. |
| Client Tweaks | [modrinth.com/mod/client-tweaks](https://modrinth.com/mod/client-tweaks) | QoL, Client | client | medium | Fabric API, Balm | — | — | May overlap **Countered's Smooth F5**—review config. |
| Cloth Config API | [modrinth.com/mod/cloth-config](https://modrinth.com/mod/cloth-config) | Library, UI | both | high | — | Better Combat, Combat Roll, InvMove, BetterF3, Creative Fly, StartInv | — | Config screens. |
| Collective | [modrinth.com/mod/collective](https://modrinth.com/mod/collective) | Library | both | high | — | Serilum-style mods in-pack | — | Shared library for Collective-fork ports. |
| Combat Roll | [modrinth.com/mod/combat-roll](https://modrinth.com/mod/combat-roll) | Combat, Movement | both | medium | Fabric API, Player Animator, Cloth Config API | — | — | Dodge roll; test with **Better Combat** / camera stack. |
| Controlling | [modrinth.com/mod/controlling](https://modrinth.com/mod/controlling) | QoL, UI | client | high | Fabric API, Searchables | — | — | Keybind search UI. |
| Countered's Smooth F5 | [modrinth.com/mod/countereds-smooth-f5](https://modrinth.com/mod/countereds-smooth-f5) | Camera, QoL | client | medium | — | — | — | Smooth third-person toggle. |
| Crafting Tweaks | [modrinth.com/mod/crafting-tweaks](https://modrinth.com/mod/crafting-tweaks) | QoL, UI | both | medium | Fabric API, Balm | — | — | Crafting grid shortcuts. |
| Creative Fly | [modrinth.com/mod/creative-fly](https://modrinth.com/mod/creative-fly) | QoL, Creative | client | low | Fabric API, Cloth Config API | — | — | Creative flight tweaks; creative only. |
| Death Backup | [modrinth.com/mod/death-backup](https://modrinth.com/mod/death-backup) | Gameplay, Utility | server | medium | Collective | — | — | Backup gear on death (server). |
| Default Options | [modrinth.com/mod/default-options](https://modrinth.com/mod/default-options) | QoL, Configuration | client | high | Balm, Fabric API | — | — | Ships the vanilla keybind/video default layer; capture `config/defaultoptions/*` with `/defaultoptions saveAll`, `/defaultoptions saveOptions`, or `/defaultoptions saveKeys` when the baseline is decided. |
| Dismount Entity | [modrinth.com/mod/dismount-entity](https://modrinth.com/mod/dismount-entity) | Gameplay, Utility | server | low | Collective | — | — | Dismount riders (server). |
| EasyAuth | [modrinth.com/mod/easyauth](https://modrinth.com/mod/easyauth) | Security, Utility | server | high | Fabric API | — | — | Offline-mode auth gate for the dedicated server; invite secret for registration, then per-player `/login`. |
| Easy Anvils | [modrinth.com/mod/easy-anvils](https://modrinth.com/mod/easy-anvils) | QoL, Gameplay | both | medium | Fabric API, Puzzles Lib, Forge Config API Port | — | — | Anvil UX tweaks. |
| Easy Magic | [modrinth.com/mod/easy-magic](https://modrinth.com/mod/easy-magic) | QoL, Gameplay | both | medium | Fabric API, Puzzles Lib, Forge Config API Port | — | — | Enchanting table UX. |
| Easy Shulker Boxes | [modrinth.com/mod/easy-shulker-boxes](https://modrinth.com/mod/easy-shulker-boxes) | QoL, Storage | both | medium | Fabric API, Puzzles Lib, Forge Config API Port | — | — | Shulker interaction QoL. |
| Entity Culling | [modrinth.com/mod/entityculling](https://modrinth.com/mod/entityculling) | Optimization, Rendering | client | high | — | — | — | Client entity culling. |
| Fabric API | [modrinth.com/mod/fabric-api](https://modrinth.com/mod/fabric-api) | Library, Core | both | very high | — | (ecosystem) | — | Fabric baseline. |
| Fabric Language Kotlin | [modrinth.com/mod/fabric-language-kotlin](https://modrinth.com/mod/fabric-language-kotlin) | Library | both | high | — | Observable | — | Kotlin adapter. |
| FerriteCore | [modrinth.com/mod/ferrite-core](https://modrinth.com/mod/ferrite-core) | Optimization | both | high | — | — | — | Memory reductions. |
| Forge Config API Port | [modrinth.com/mod/forge-config-api-port](https://modrinth.com/mod/forge-config-api-port) | Library | both | high | Fabric API | Puzzles Lib, Clean Tooltips, SimpleAFK, … | — | Config API port. |
| Hand Over Your Items | [modrinth.com/mod/hand-over-your-items](https://modrinth.com/mod/hand-over-your-items) | Gameplay, Multiplayer | both | low | Collective | — | — | Hand-off items; server for MP. |
| Hidden Recipe Book | [modrinth.com/mod/hidden-recipe-book](https://modrinth.com/mod/hidden-recipe-book) | QoL, UI | client | medium | Collective | — | — | Hides vanilla recipe book; pair with **JEI**. |
| Horse Expert | [modrinth.com/mod/horse-expert](https://modrinth.com/mod/horse-expert) | QoL, UI | both | medium | Fabric API, Puzzles Lib, Forge Config API Port | — | — | Horse stats in UI. |
| ImmediatelyFast | [modrinth.com/mod/immediatelyfast](https://modrinth.com/mod/immediatelyfast) | Optimization, Rendering | client | high | — | — | — | Immediate-mode rendering. |
| Improved Sign Editing | [modrinth.com/mod/improved-sign-editing](https://modrinth.com/mod/improved-sign-editing) | QoL, UI | client | medium | Collective | — | — | Better sign editing. |
| Indium | [modrinth.com/mod/indium](https://modrinth.com/mod/indium) | Library, Rendering | client | high | Sodium | — | — | FRAPI + Sodium bridge. |
| Inventory Essentials | [modrinth.com/mod/inventory-essentials](https://modrinth.com/mod/inventory-essentials) | QoL, UI | both | medium | Fabric API, Balm | — | — | Inventory shortcuts. |
| InvMove | [modrinth.com/mod/invmove](https://modrinth.com/mod/invmove) | QoL, Movement | client | medium | Cloth Config API | — | — | Move with inventories open; test with **JEI**. |
| InvMoveCompats | [modrinth.com/mod/invmovecompats](https://modrinth.com/mod/invmovecompats) | QoL, Compatibility | client | medium | InvMove, Cloth Config API | — | — | Extra InvMove compat. |
| Iris Shaders | [modrinth.com/mod/iris](https://modrinth.com/mod/iris) | Rendering, Shaders | client | high | Sodium | — | — | Shader loader. |
| Jade 🔍 | [modrinth.com/mod/jade](https://modrinth.com/mod/jade) | QoL, UI | both | high | — | — | — | Block/entity overlay info. |
| JamLib | [modrinth.com/mod/jamlib](https://modrinth.com/mod/jamlib) | Library | both | high | Fabric API, Architectury API | RightClickHarvest | — | Jared library. |
| Just Enough Items (JEI) | [modrinth.com/mod/jei](https://modrinth.com/mod/jei) | QoL, UI | both | very high | — | — | — | Recipe lookup. |
| KleeSlabs | [modrinth.com/mod/kleeslabs](https://modrinth.com/mod/kleeslabs) | QoL, Building | both | medium | Fabric API, Balm | — | — | Break individual slab halves. |
| Krypton | [modrinth.com/mod/krypton](https://modrinth.com/mod/krypton) | Optimization, Networking | both | medium | — | — | Rare proxy issues | Net micro-opts. |
| Leaves Be Gone | [modrinth.com/mod/leaves-be-gone](https://modrinth.com/mod/leaves-be-gone) | Performance, World | server | medium | Fabric API, Puzzles Lib, Forge Config API Port | — | — | Faster leaf decay (server). |
| Leawind's Third Person | [modrinth.com/mod/leawind-third-person](https://modrinth.com/mod/leawind-third-person) | Camera, Utility | client | medium | Fabric API, Architectury API | — | Overlaps camera mods | Third-person rig. |
| Lithium | [modrinth.com/mod/lithium](https://modrinth.com/mod/lithium) | Optimization | both | very high | — | — | — | Server/game logic optimizations. |
| Lithostitched | [modrinth.com/mod/lithostitched](https://modrinth.com/mod/lithostitched) | Library, World Gen | both | high | — | Tectonic | — | Support library required by **Tectonic** 3.0.21+ so the worldgen stack loads in singleplayer, server and `World Preview`. |
| Mod Menu | [modrinth.com/mod/modmenu](https://modrinth.com/mod/modmenu) | QoL, UI | client | high | Fabric API, Text Placeholder API | — | — | Mod list. |
| Natural Temperature | [modrinth.com/mod/natural-temperature](https://modrinth.com/mod/natural-temperature) | World Gen, Climate | server | high | Fabric API | — | Latitude | Climate bands for a more Earth-like overworld; server-side only, but works in singleplayer and is lighter on the preview UI than Latitude. |
| ModernFix | [modrinth.com/mod/modernfix](https://modrinth.com/mod/modernfix) | Optimization | both | very high | — | — | — | Broad perf fixes. |
| Mouse Tweaks | [modrinth.com/mod/mouse-tweaks](https://modrinth.com/mod/mouse-tweaks) | QoL, UI | client | high | Fabric API | — | — | Inventory mouse shortcuts. |
| No Feather Trample | [modrinth.com/mod/no-feather-trample](https://modrinth.com/mod/no-feather-trample) | Gameplay, Farming | server | low | Collective | — | — | Crop trample tweak (server). |
| Not Enough Animations | [modrinth.com/mod/not-enough-animations](https://modrinth.com/mod/not-enough-animations) | Animation | client | medium | — | — | — | Extra animations. |
| Observable | [modrinth.com/mod/observable](https://modrinth.com/mod/observable) | Diagnostics | both | medium | Architectury API, Fabric Language Kotlin | — | — | Profiling UI. |
| Omnidirectional Movement | [modrinth.com/mod/omnidirectional-movement](https://modrinth.com/mod/omnidirectional-movement) | Movement | both | medium | — | — | — | Strafe movement; both sides MP. |
| Paxi | [modrinth.com/mod/paxi](https://modrinth.com/mod/paxi) | Utility, Resource Loading | both | high | Fabric API, Cloth Config API, YUNG's API | — | — | Global datapack/resourcepack loader. Paxi uses the base `.minecraft/datapacks` directory plus `config/paxi/{datapacks,resourcepacks}` and the load-order JSON files. |
| Pick Up Notifier | [modrinth.com/mod/pick-up-notifier](https://modrinth.com/mod/pick-up-notifier) | QoL, UI | both | medium | — | — | — | Replaces the incompatible `ItemPickupNotifier` build; compatible with `1.21.1`. |
| Player Animator | [modrinth.com/mod/playeranimator](https://modrinth.com/mod/playeranimator) | Library, Animation | both | high | — | Better Combat, Combat Roll | — | Animation library. |
| Puzzles Lib | [modrinth.com/mod/puzzles-lib](https://modrinth.com/mod/puzzles-lib) | Library | both | high | Fabric API, Forge Config API Port | Leaves Be Gone, Easy Anvils, Easy Magic, Horse Expert, Easy Shulker Boxes | — | Fuzs library. |
| Ready Player Fun | [modrinth.com/mod/ready-player-fun](https://modrinth.com/mod/ready-player-fun) | Gameplay, Server | server | low | Fabric API | — | — | Server-side player fun features. |
| Real Camera | [modrinth.com/mod/real-camera](https://modrinth.com/mod/real-camera) | Camera | client | medium | Fabric API | — | Overlaps camera mods | First-person body. |
| RightClickHarvest | [modrinth.com/mod/rightclickharvest](https://modrinth.com/mod/rightclickharvest) | Gameplay, Farming | server | medium | Fabric API, Architectury API, JamLib | — | — | Right-click harvest (server). |
| Screenshot to Clipboard | [modrinth.com/mod/screenshot-to-clipboard](https://modrinth.com/mod/screenshot-to-clipboard) | QoL, Utility | client | low | — | — | — | Copy screenshots. |
| Searchables | [modrinth.com/mod/searchables](https://modrinth.com/mod/searchables) | Library | client | high | Fabric API | Controlling | — | Search UI library. |
| Set World Spawn Point | [modrinth.com/mod/set-world-spawn-point](https://modrinth.com/mod/set-world-spawn-point) | Utility, Server | server | low | Collective | — | — | Exact custom spawn point and spawn tweaks; pin new worlds to `0,0` with `forceExactSpawn`. |
| Simple Homing XP | [modrinth.com/mod/simple-homing-xp](https://modrinth.com/mod/simple-homing-xp) | QoL, Gameplay | both | low | — | — | — | XP orb attraction. |
| SimpleAFK | [modrinth.com/mod/simpleafk](https://modrinth.com/mod/simpleafk) | Gameplay, Server | server | low | Fabric API, Forge Config API Port | — | — | AFK detection/rules (server). |
| Sodium | [modrinth.com/mod/sodium](https://modrinth.com/mod/sodium) | Optimization, Rendering | client | very high | — | Indium, Iris | — | Client renderer. |
| spark | [modrinth.com/mod/spark](https://modrinth.com/mod/spark) | Diagnostics | both | medium | — | — | — | Profiler. |
| StartInv | [modrinth.com/mod/startinv](https://modrinth.com/mod/startinv) | Gameplay, Utility | both | low | Cloth Config API | — | — | Starting inventory. |
| TCDCommons API | [modrinth.com/mod/tcdcommons](https://modrinth.com/mod/tcdcommons) | Library | both | high | Fabric API | Better Statistics Screen | — | TCD Commons. |
| Tectonic | [modrinth.com/datapack/tectonic](https://modrinth.com/datapack/tectonic) | World Gen, Terrain | both | high | Lithostitched | — | Continents | Macro-terrain layer: continents, deep oceans and rivers; shipped as `both` here so singleplayer and `World Preview` see the same terrain stack. |
| Text Placeholder API | [modrinth.com/mod/placeholder-api](https://modrinth.com/mod/placeholder-api) | Library | both | high | — | Mod Menu | — | Placeholders. |
| TrashSlot | [modrinth.com/mod/trashslot](https://modrinth.com/mod/trashslot) | QoL, UI | both | medium | Fabric API, Balm | — | — | Trash slot in inventory. |
| Wall-Jump TXF | [modrinth.com/mod/wall-jump-txf](https://modrinth.com/mod/wall-jump-txf) | Movement, Gameplay | both | medium | — | — | — | Wall/double jump. |
| William Wythers' Overhauled Overworld | [modrinth.com/mod/wwoo](https://modrinth.com/mod/wwoo) | World Gen, Biomes, Terrain | both | high | — | — | Terralith | Biome/transitions layer; includes Navigable Rivers, Cliffs and Coves and Towering Tepuis via config. |
| WITS (What Is This Structure?) | [modrinth.com/mod/wits](https://modrinth.com/mod/wits) | Utility, World | server | medium | Fabric API | — | — | Structure identification (server). |
| World Preview | [modrinth.com/mod/world-preview](https://modrinth.com/mod/world-preview) | World Gen, Utility | client | low | Fabric API | — | — | Adds a `Preview` tab to Singleplayer for seed, biome and terrain scouting before committing a world. |
| Yet Another Config Lib | [modrinth.com/mod/yacl](https://modrinth.com/mod/yacl) | Library, UI | both | high | Fabric API | — | — | YACL configs. |
| YUNG's API | [modrinth.com/mod/yungs-api](https://modrinth.com/mod/yungs-api) | Library | both | high | — | Paxi | — | Support library pulled in for Paxi. |
| Fresh Animations | [modrinth.com/resourcepack/fresh-animations](https://modrinth.com/resourcepack/fresh-animations) | Resource pack, Animation | client | medium | — | Fresh Animations: Player Extension | — | Ships as `resourcepacks/*.pw.toml`; Paxi loads it globally, with Player Extension above the base pack. |
| Fresh Animations: Player Extension | [modrinth.com/resourcepack/fa-player-extension](https://modrinth.com/resourcepack/fa-player-extension) | Resource pack, Animation | client | medium | Fresh Animations (in-pack) | — | — | FA player layer. |
| MakeUp - Ultra Fast | [modrinth.com/shader/makeup-ultra-fast-shaders](https://modrinth.com/shader/makeup-ultra-fast-shaders) | Shaders | client | high | Iris Shaders | — | — | Ships as `shaderpacks/*.pw.toml`. |

## Listed mods

Candidates or planned additions **without** a `mods/*.pw.toml`, `shaderpacks/*.pw.toml`, or `resourcepacks/*.pw.toml` yet. When one ships, move the row to **Active mods** and remove it from here.

| Mod | Page | Categories | Environment | Priority | Dependencies | Dependents | Incompatibilities | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Biomes O' Plenty | [modrinth.com/mod/biomes-o-plenty](https://modrinth.com/mod/biomes-o-plenty) | World Gen, Biomes, Content | both | medium | Fabric API, GlitchCore, TerraBlender | — | WWOO / Terralith as primary biome suite | Classic fantasy-biome branch with vanilla-esque flair; good if we trade coherence for more variety. |
| Continents | [modrinth.com/datapack/continents](https://modrinth.com/datapack/continents) | World Gen, Terrain | server | medium | — | — | Tectonic baseline | Comparison branch for larger oceans and more separated landmasses. |
| Latitude | [modrinth.com/mod/latitude](https://modrinth.com/mod/latitude) | World Gen, Climate, Utility | both | high | Fabric API | — | Terralith | Comparison branch for climate bands; shelved from the active baseline after the `World Preview` UI got cluttered and the world still read as patchy. |
| ParCool! | [modrinth.com/mod/parcool](https://modrinth.com/mod/parcool) | Movement | both | low | — | — | — | Planned for movement stack; **no Fabric 1.21.1** file on Modrinth as of 2026-03-31 (NeoForge/Forge only for recent 1.21.1 builds). Re-evaluate if Fabric returns. |
| Regions Unexplored | [modrinth.com/mod/regions-unexplored](https://modrinth.com/mod/regions-unexplored) | World Gen, Biomes, Content | both | medium | Fabric API, Biolith, Lithostitched | — | WWOO as primary biome suite | 70+ biome branch for a more exotic overworld; use instead of WWOO if fantasy variety wins. |
| Terralith | [modrinth.com/datapack/terralith](https://modrinth.com/datapack/terralith) | World Gen, Biomes, Terrain | server | medium | — | — | Latitude baseline | Realism + light fantasy branch with many biomes; do not keep it in the same baseline as Latitude. |

## Discarded mods

Removed from the pack or rejected after evaluation. Do not delete rows casually; use **Notes** for decision date and rationale.

| Mod | Page | Categories | Environment | Priority | Dependencies | Dependents | Incompatibilities | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| e4mc | [modrinth.com/mod/e4mc](https://modrinth.com/mod/e4mc) | Networking, Utility | client | medium | Fabric API | — | Krypton, integrated server login | Removed **2026-04-01**: caused singleplayer / LAN disconnects in the standard pack via login-pipeline mixin conflicts with **Krypton**. Keep only as a local optional mod if you really need ad-hoc tunnels. |
| First Person Model | [modrinth.com/mod/first-person-model](https://modrinth.com/mod/first-person-model) | Animation, Rendering | client | medium | Fabric API, Not Enough Animations | — | — | Removed **2026-03-31**: redundant with **Real Camera** (better FP stack); fewer glitches with **Better Combat**. **NEA** kept for other animations. |

## Dependency sketch (in-pack)

```text
Fabric API ─────────────────────────► (most Fabric mods)
Sodium ──► Indium
Sodium ──► Iris Shaders ──► shader packs (e.g. MakeUp - Ultra Fast)
Architectury API ──┬──► Leawind's Third Person, Observable, RightClickHarvest
Fabric Language Kotlin ──┴──► Observable
Forge Config API Port ──► Puzzles Lib ──► Leaves Be Gone, Easy Anvils/Magic/Shulker, Horse Expert
Forge Config API Port ──► SimpleAFK, Clean Tooltips
Collective ──► Serilum-style mods (Death Backup, Dismount Entity, …)
Balm ──► Crafting Tweaks, Client Tweaks, TrashSlot, KleeSlabs, Inventory Essentials, Default Options
JamLib + Architectury API ──► RightClickHarvest
Searchables ──► Controlling
TCDCommons API ──► Better Statistics Screen
Cloth Config API ──┬──► Better Combat, Combat Roll, InvMove, BetterF3, Creative Fly, StartInv
Player Animator ───┴──► Better Combat, Combat Roll
YUNG's API ──► Paxi
Fresh Animations ──► Fresh Animations: Player Extension
Text Placeholder API ──► Mod Menu
```

## Reconciliation

- **Last reconciled:** 2026-04-02 — **Active** rows vs `mods/*.pw.toml` (83) + `shaderpacks/*.pw.toml` (1) + `resourcepacks/*.pw.toml` (2), `pack.toml` `0.0.11-alpha`; **Listed** 6 (**Biomes O' Plenty**, **Continents**, **Latitude**, **ParCool!**, **Regions Unexplored**, **Terralith**); **Discarded** 2 (**e4mc**, **First Person Model**). **EasyAuth** remains **server-only** for offline-mode auth on the dedicated server. **Default Options** now covers the vanilla keybind/video baseline, and **Paxi** auto-loads the benchmark datapack from the base `datapacks/` directory plus the ordered global resource packs in `config/paxi/*`. **Pick Up Notifier** replaced the incompatible `ItemPickupNotifier` Modrinth build that declared `minecraft 1.21.10`; this line is aligned with `1.21.1`. **Natural Temperature + Lithostitched + Tectonic + WWOO** is now the recommended overworld baseline; `World Preview` is still the client-side entry point for comparing seeds and terrain before generation. **e4mc** was removed from the shipped pack because it conflicted with **Krypton** during integrated-server login and broke standard singleplayer/LAN startup. **Manual smoke (host):** create a fresh singleplayer world; check `Options`/`Controls` for default baseline behavior; verify `benchmark:*` is available without manual world injection; open **JEI** while **InvMove** walking; try **Combat Roll** with **Better Combat**; review **Client Tweaks** vs **Smooth F5**; for worldgen, open `Preview` and compare `Lithostitched + Tectonic`, `Natural Temperature + Lithostitched + Tectonic`, and the fantasy branches listed above.
- After every manifest change, bump **Last reconciled** and verify **Active** row count vs `mods/*.pw.toml`, `shaderpacks/*.pw.toml`, and `resourcepacks/*.pw.toml`.
