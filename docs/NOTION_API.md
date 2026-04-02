# Notion API

Este documento descreve o caminho para manipulação precisa da database `Mods`
via a API oficial da Notion. Use este fluxo quando a base ficar grande demais
para manutenção confortável via MCP interativo.

## Quando usar

- auditoria completa da database;
- listagem de rows por título, status ou campos vazios;
- atualizações em lote com controle explícito de página;
- exportação da tabela inteira para análise local.

## O que é necessário

- uma integração interna na workspace da Notion;
- a chave `NOTION_API_KEY` dessa integração, copiada exatamente como a Notion
  fornecer;
- o ID da database `Mods` a partir do link da página;
- acesso explícito da integração à database via `Add connections`.

## Limites importantes

- a API oficial da Notion é gratuita para uso normal no workspace;
- a API é limitada a uma média de 3 requests por segundo por integração;
- a integração só enxerga páginas e databases compartilhadas com ela;
- o token do MCP não serve como token da API pública.

## Variáveis de ambiente

```bash
NOTION_API_KEY=ntn_xxx
NOTION_DATABASE_ID=2d36f4dba5f281139f41f86a64b38df6
NOTION_API_VERSION=2022-06-28
```

Coloque a chave no `.env` local exatamente no formato que a Notion fornecer.
Tokens novos costumam começar com `ntn_`; tokens antigos podem começar com
`secret_`. Não adicione prefixos extras como `secret_ntn_`.
O ID da database vem da URL da página da database no Notion. No caso do
NotVanilla, esse é o identificador `2d36f4dba5f281139f41f86a64b38df6` sem
hífens.

## Fluxo recomendado

1. Criar uma integração interna na Notion.
2. Compartilhar a database `Mods` com essa integração.
3. Copiar a chave para o `.env` local.
4. Rodar `python3 scripts/notion_api_sync.py audit` para validar acesso.
5. Usar `python3 scripts/notion_api_sync.py sync-inventory` para reconciliar a
   database inteira com `docs/MODS_INVENTORY.md` e `docs/MOD_MODULES.md`; o
   comando cria rows ativas ausentes, preenche campos faltantes e normaliza
   títulos com sufixos de plataforma como `- Minecraft Mod`,
   `- Minecraft Shader` e `- Minecraft Resource Pack`. Quando a row já tem
   `Página`, o comando também liga o título diretamente para essa URL.
6. Usar `python3 scripts/notion_api_sync.py find ...` e `update ...` para
   ajustes cirúrgicos.
7. Usar `python3 scripts/notion_api_sync.py bulk-mark-listed` quando o objetivo
   for apenas preencher `Status` vazio com `Listed`.

## Exemplos

```bash
python3 scripts/notion_api_sync.py audit
python3 scripts/notion_api_sync.py sync-inventory
python3 scripts/notion_api_sync.py find --title Sodium
python3 scripts/notion_api_sync.py update --page-id <page-id> --set Status=Listed
python3 scripts/notion_api_sync.py update --page-id <page-id> --set Ambiente=client --set "Prioridade=4 - Alta"
```
