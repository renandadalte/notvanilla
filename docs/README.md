# NotVanilla — documentação técnica

Esta pasta segue a lógica do [Diátaxis](https://diataxis.fr/): cada documento deve ter um papel claro e não virar um depósito genérico de notas.

## Mapa

| Documento | Papel | Uso |
| --- | --- | --- |
| [MODS_INVENTORY.md](./MODS_INVENTORY.md) | Referência | Inventário do que está ativo no pack, backlog e itens descartados |
| [MOD_MODULES.md](./MOD_MODULES.md) | Referência | Agrupamento operacional dos mods em módulos de teste e ajuste |
| [WORLDGEN_BASELINE.md](./WORLDGEN_BASELINE.md) | Referência | Baseline de worldgen, perfis de teste e critérios de comparação |
| [NOTION_API.md](./NOTION_API.md) | How-to | Integração oficial da database de mods via API da Notion |
| [DEVELOPMENT.md](./DEVELOPMENT.md) | How-to | Manutenção do pack, packwiz, canais `main`/`dev`, publicação e deploy |
| Este arquivo | Explicação | Limites do que fica documentado aqui |

## Fonte da verdade

No NotVanilla, a ordem de autoridade é esta:

1. `pack.toml`, `index.toml`, `mods/*.pw.toml`, `shaderpacks/*.pw.toml` e `resourcepacks/*.pw.toml`
2. `docs/MODS_INVENTORY.md`
3. `CHANGELOG.md`

O repositório guarda o pack e a documentação pública. Contexto de host, segredos, auth, mundo, caches locais e anotações temporárias ficam fora dele.

## O que não entra no pack

Nem tudo o que está no repo precisa ser distribuído pelo packwiz.

- `README.md`, `CHANGELOG.md` e `docs/` continuam públicos, mas não entram no `index.toml`.
- `instance.cfg`, `instance.dev.cfg`, `mmc-pack.json` e `packwiz-installer-bootstrap.jar` continuam no repo para bootstrap/importação, mas também ficam fora do `index.toml`.
- `scripts/` e automação de CI servem ao repositório, não ao runtime do jogo.

Se um documento aqui ficar desatualizado em relação aos manifests, o manifesto continua sendo a fonte da verdade e a doc precisa ser reconciliada.
