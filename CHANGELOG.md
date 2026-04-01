# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.11-alpha] - 2026-03-31
### Added
- Large **QoL / utilities** wave: **JEI**, **Jade**, HUD/UX (**Better Advancements**, **Better Statistics Screen** + **TCDCommons API**, **BetterF3**, **Better Ping Display**, **Clean Tooltips**, **Item Pickup Notifier**, **Hidden Recipe Book**), inventory (**Mouse Tweaks**, **Crafting Tweaks**, **Client Tweaks**, **Controlling** + **Searchables**, **Inventory Essentials**, **TrashSlot**, **InvMove** + **InvMoveCompats**, **AppleSkin**, **Screenshot to Clipboard**), **Combat Roll**, farming/world (**RightClickHarvest** + **JamLib**, **Leaves Be Gone**, **No Feather Trample**, **KleeSlabs**, **Easy Shulker / Anvils / Magic**, **Horse Expert**, **Call Your Horse**, **Simple Homing XP**, **WITS**, **Ready Player Fun**), Serilum-style mods on **Collective** (e.g. **Death Backup**, **Dismount Entity**, **Improved Sign Editing**, **Set World Spawn Point**, **Hand Over Your Items**), **AFK Camera**, **SimpleAFK**, **e4mc** (LAN exposure—trusted networks only), **Creative Fly**, **StartInv**, and libraries **Balm**, **Puzzles Lib**, **Forge Config API Port**, **Collective**, **Searchables**, **JamLib**.
### Notes
- **Item Pickup Notifier** uses a Modrinth version whose API `game_versions` list is **1.21.10**—confirm behaviour on **1.21.1** in-game. **Xaero** maps not in this release. **Adaptive Tooltips** omitted (no Fabric **1.21.x** build on Modrinth).

## [0.0.10-alpha] - 2026-03-31
### Changed
- **`config/`:** atualização dos defaults (ex.: **Iris**, **Fabric** indigo, **Wall-Jump**); nova limpeza para **só** ficheiros dos mods listados em `mods/*.pw.toml` (remove lixo de outras instâncias).
### Notes
- Fim da sprint do stack movimento/câmera/combate; **`dev`** alinhado com **`main`** após este release.

## [0.0.9-alpha] - 2026-03-31
### Added
- **Wall-Jump TXF** de volta ao **`main`**: faz parte do stack de **movimento + combate** com o resto do pack (o único mod removido do stack continua a ser **First Person Model**).
- Pasta **`config/`** no repositório: defaults dos **mods ativos** apenas (limpeza de configs de outros modpacks); packwiz passa a sincronizar estes ficheiros com clientes/servidor. Ver `docs/DEVELOPMENT.md`.
### Changed
- **`.packwizignore` / `.gitignore`:** ignorar `config/sodium-fingerprint.json` e pastas temporárias do Spark sob `config/spark/`.

## [0.0.8-alpha] - 2026-03-31
### Added
- **`main` alinhado ao stack movimento/câmera/combate do `dev`** (exceto parkour): Leawind's Third Person, Real Camera, Countered's Smooth F5, Omnidirectional Movement, Not Enough Animations, Player Animator, Cloth Config API, Better Combat; resource packs **Fresh Animations** + **FA Player Extension** em `resourcepacks/`.
### Removed
- **First Person Model**: **Real Camera** cobre o corpo em primeira pessoa com menos conflitos com **Better Combat**; **Not Enough Animations** mantém-se para outras poses. Configs de servidor/cliente a incorporar no repo ficam pendentes (envio separado).
- **Wall-Jump TXF** em **`main`**: nesta versão foi omitido em **`main`** em favor de produção mais leve; **revertido em `0.0.9-alpha`** (Wall-Jump volta ao stack completo em **`main`**).

## [0.0.7-alpha] - 2026-03-31
### Removed
- **Wall-Jump TXF** do branch **`main`** (produção leve); no **`dev`** o mod **mantém-se** para testes de parkour e o servidor de testes segue alinhado ao `dev`.

## [0.0.6-alpha] - 2026-03-31
### Added
- **Cloth Config API** (cliente + servidor): biblioteca de ecrãs de configuração **Cloth**; alinha com **Mod Menu** e **YACL** para cobrir mods que usem qualquer uma das duas stacks de UI.

## [0.0.5-alpha] - 2026-03-31
### Added
- **Mod Menu** + **Text Placeholder API** (dependência): lista de mods no jogo e atalhos para ecrãs de configuração quando os mods os expõem.
- **Yet Another Config Lib (YACL)**: biblioteca de UIs de configuração para mods que usam YACL (complementa **Cloth Config** no pack).
- **Wall-Jump TXF** (**só `dev`**): salto em parede / double jump / salto em fences; **cliente e servidor**.
- **Branch `dev` — movimento/câmera/combate:** Leawind's Third Person, Real Camera, Countered's Smooth F5, Omnidirectional Movement, Not Enough Animations, Player Animator, Cloth Config API, Better Combat (mods `both` no servidor). *First Person Model foi removido em `0.0.8-alpha`.*
- **Resource packs** em `resourcepacks/`: [Fresh Animations](https://modrinth.com/resourcepack/fresh-animations) (base v1.10.4) e [Fresh Animations: Player Extension](https://modrinth.com/resourcepack/fa-player-extension) — na lista do jogo, ativar **ambos** com a **extensão acima** da base (maior prioridade).
### Notes
- **ParCool!** não entrou: no Modrinth não há release **Fabric** para `1.21.1` (apenas NeoForge/Forge nas versões recentes). Permanece em **Listed** em `docs/MODS_INVENTORY.md` para reavaliação futura.

## [0.0.4] - 2026-03-31
### Added
- **Iris Shaders** (cliente): carregador de shaders sobre **Sodium** para Minecraft 1.21.1.
- **MakeUp - Ultra Fast** v9.4c como shader **base** do pack (leve, boa qualidade visual, perfis ajustáveis para poupar FPS). Entregue via `shaderpacks/` no packwiz.
### Fixed
- **`.packwizignore`:** `.agent/`, `logs/`, `docs/` e `README.md` deixam de entrar no `index.toml`. O instalador packwiz já não tenta baixar ficheiros que não existem no GitHub Pages (evita **404** em `.agent/*`, logs de benchmark, etc.). *`.gitignore` não afeta o índice — só o `.packwizignore`.*
### Added
- **`instance.dev.cfg`:** modelo Prism com **Pre-launch** para `https://raw.githubusercontent.com/renandadalte/notvanilla/dev/pack.toml` — mesma lógica que `instance.cfg`/`main`, para instância de testes noutro PC; documentado em `docs/DEVELOPMENT.md` e README.

## [0.0.3] - 2026-03-29
### Added
- Datapack **`benchmark`**: cenário spectator **1200 ticks** (~60s), percurso ida → spawn → ida (warm chunks); **`function benchmark:start`** na consola/RCON. Baseline principal com **HWiNFO** (CSV); Spark fica só para diagnóstico de lag quando precisares.
### Changed
- Removido fluxo `benchmark:sync_start` (Spark dentro do datapack); README alinhado ao benchmark **HWiNFO-first**.
- `.gitignore`: `.cursor/` e `.agent/` permanecem só no ambiente local (repo = modpack + docs).

## [0.0.2] - 2026-03-22
### Added
- Adição de mods para otimização em ambientes com muitos mods: ImmediatelyFast (renderização 2D/UI) e Krypton (rede).
- Adição de ferramentas profissionais para depuração e benchmark: Spark (profiling técnico) e Observable (profiling visual de entidades).
- Adição de dependências obrigatórias: Architectury API e Fabric Language Kotlin.

## [0.0.1] - 2026-03-22
### Added
- Setup inicial da arquitetura do modpack via `packwiz` para a versão Minecraft 1.21.1.
- Adição dos mods base de performance: Entity Culling, FerriteCore, Indium, Lithium, ModernFix e Sodium.
- Integração da API do Fabric (v0.18.4).
- Automação robusta via GitHub Actions para geração do `NotVanilla.zip` nos Releases sem erro de cache.
- Regras estritas de `.gitignore` e `.packwizignore` para não poluir o repositório nem o cliente.

### Changed
- Configuração oficial do `instance.cfg` do Prism Launcher para auto-atualização sem flags descontinuadas (`-d`).
- Arquitetura limpa: o repositório não rastreia mais os binários compilados (`.zip` ou `.mrpack`).
