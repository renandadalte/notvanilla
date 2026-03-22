# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
