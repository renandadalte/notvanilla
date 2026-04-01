# Desenvolvimento — manutenção do pack

## Pré-requisitos

- `packwiz` instalado e funcional
- Python 3 para as checagens locais versionadas em `scripts/`
- Minecraft `1.21.1` e Fabric Loader `0.18.4`, conforme `pack.toml`

## Canais do projeto

Hoje o projeto trabalha com dois canais de client e um único canal de servidor:

| Canal | Uso | URL do `pack.toml` |
| --- | --- | --- |
| `main` | produção para jogadores | `https://renandadalte.github.io/notvanilla/main/pack.toml` |
| `dev` | testes antes de merge | `https://renandadalte.github.io/notvanilla/dev/pack.toml` |

O servidor dedicado acompanha apenas `dev` nesta fase. A separação entre servidor `main` e `dev` fica para depois.

## Prism Launcher

### Instância `main`

- Importar pelo ZIP estável:

```text
https://github.com/renandadalte/notvanilla/releases/latest/download/NotVanilla.zip
```

- O `instance.cfg` desse ZIP aponta para:

```text
https://renandadalte.github.io/notvanilla/main/pack.toml
```

### Instância `dev`

- Importar pelo ZIP de testes:

```text
https://github.com/renandadalte/notvanilla/releases/download/dev-latest/NotVanilla-dev.zip
```

- O bootstrap de `dev` aponta para:

```text
https://renandadalte.github.io/notvanilla/dev/pack.toml
```

Também continua válido duplicar a instância principal no Prism e trocar apenas o `PreLaunchCommand`.

## Limites do repositório

Tudo o que está versionado deve cair em um destes grupos:

| Grupo | Exemplos | Vai para o `index.toml`? |
| --- | --- | --- |
| Runtime do pack | `mods/*.pw.toml`, `shaderpacks/*.pw.toml`, `resourcepacks/*.pw.toml`, `config/`, `datapacks/` | Sim |
| Bootstrap e automação | `instance.cfg`, `instance.dev.cfg`, `mmc-pack.json`, `packwiz-installer-bootstrap.jar`, `.github/`, `scripts/` | Não |
| Documentação pública | `README.md`, `CHANGELOG.md`, `docs/` | Não |
| Local / host-only | `.agent/`, `.cursor/`, `logs/`, `.env`, mundo do servidor, auth local | Nunca deve entrar no repo |

Regra prática:

- o repo é a fonte da verdade do pack e da documentação pública;
- o `index.toml` deve conter apenas o que cliente e servidor precisam para rodar;
- segredos, auth, mundo, logs e automação de host ficam fora do repo.

## `.packwizignore` vs `.gitignore`

- `.gitignore` controla o que o Git rastreia.
- `.packwizignore` controla o que o `packwiz refresh` pode colocar no `index.toml`.
- Um arquivo pode continuar no repo e ainda assim **não** fazer parte do canal de atualização do packwiz.

No NotVanilla, o `index.toml` não deve publicar:

- `README.md`
- `CHANGELOG.md`
- `instance.cfg`
- `instance.dev.cfg`
- `mmc-pack.json`
- `packwiz-installer-bootstrap.jar`
- `docs/`
- `scripts/`
- `.agent/`, `.cursor/` e `logs/`

## Mudança no conjunto de mods

1. Altere `mods/*.pw.toml`, `shaderpacks/*.pw.toml` ou `resourcepacks/*.pw.toml`.
2. Atualize `config/` se existir default compartilhado que realmente precisa ser distribuído.
3. Rode:

```bash
packwiz refresh
python3 scripts/check_packwiz_state.py
python3 scripts/audit_repo_surface.py
```

4. Atualize `docs/MODS_INVENTORY.md`.
5. No fluxo rápido do `dev`, atualize docs técnicas e contexto quando necessário, mas deixe `CHANGELOG.md`, `README.md` e versão para as promoções de `main` ou para tarefas explicitamente voltadas à documentação pública.

## Trabalho por módulos

Use [MOD_MODULES.md](./MOD_MODULES.md) para decidir escopo de teste quando a mudança tocar apenas uma parte do pack.

- Se a alteração ficar em um módulo, rode o smoke test desse módulo e, se necessário, o módulo-base do qual ele depende.
- Se a mudança atingir uma biblioteca compartilhada, teste também os módulos consumidores.
- Se a mudança tocar visual, câmera ou combate, revise o módulo vizinho que mais costuma romper junto.
- Se a mudança for só em docs ou contexto, o mapa de módulos serve como referência, mas não exige um teste do client inteiro.

## Política de configs versionadas

Nem toda config versionada deve se comportar como verdade central do pack.

- configs de preferência do jogador devem usar `preserve = true` no `index.toml`, para servir só como default inicial;
- configs de compatibilidade, gameplay compartilhado, benchmark recorrente e comportamento do servidor continuam sem `preserve`, para que updates do pack cheguem de fato à instância;
- `config/spark/activity.json` deve permanecer sanitizado no repo, sem histórico real de profiling.

Regra prática: se uma mudança representa gosto pessoal do jogador, não trate isso como update obrigatório do pack.

## Publicação

### GitHub Pages

O workflow `pages.yml` publica os canais `main` e `dev` de forma atômica. Em vez de expor o branch inteiro, ele monta um artefato mínimo com:

- `pack.toml`
- `index.toml`
- todos os arquivos listados no `index.toml`

Esse passo existe justamente para impedir inconsistência entre `pack.toml` e `index.toml`.

### ZIPs de bootstrap

O workflow `release-bootstrap.yml` publica:

- `latest` com `NotVanilla.zip` para `main`
- `dev-latest` com `NotVanilla-dev.zip` para `dev`

Esses ZIPs não levam mods dentro deles. Eles só preparam o Prism para baixar o conteúdo do canal certo no launch.

### Validação

O workflow `validate.yml` roda as checagens do repositório e faz um dry-run da montagem do artefato do GitHub Pages.

## Servidor `dev`

O servidor dedicado local acompanha `origin/dev`.

Fluxo esperado:

1. um checkout separado busca `origin/dev`;
2. o conteúdo é validado;
3. o servidor usa o canal `dev` publicado no GitHub Pages para sincronizar o que pertence ao pack;
4. depois da sincronização, o serviço do servidor reinicia.

Esses passos devem preservar fora do deploy:

- `.env`
- mundo
- `config/EasyAuth/`
- `ops.json`
- `whitelist.json`
- logs e artefatos locais

## Checagens antes de merge

- [ ] `pack.toml` e `index.toml` estão coerentes.
- [ ] O `index.toml` não publica arquivos de bootstrap, docs ou scripts.
- [ ] `docs/MODS_INVENTORY.md` bate com `mods/*.pw.toml`, `shaderpacks/*.pw.toml` e `resourcepacks/*.pw.toml`.
- [ ] `CHANGELOG.md` e `README.md` continuam coerentes com os canais atuais.
- [ ] Se o destino é `main`, `CHANGELOG.md` foi atualizado para as mudanças promovidas e `README.md` foi revisado quando o fluxo de instalação ou os canais mudaram.
- [ ] O que é local ou sensível continua fora do repositório e fora do `index.toml`.
