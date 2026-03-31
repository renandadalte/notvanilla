# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
- **Branch `dev` — movimento/câmera/combate:** Leawind's Third Person, Real Camera, Countered's Smooth F5, Omnidirectional Movement, Not Enough Animations, First Person Model, Player Animator, Cloth Config API, Better Combat (mods `both` no servidor).
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
