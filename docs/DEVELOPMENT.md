# Development — maintaining the pack

## Prerequisites

- [packwiz](https://packwiz.infra.link/) installed (`packwiz refresh`, `packwiz update`, etc.)
- Minecraft version and Fabric loader pinned in `pack.toml` (see `[versions]`)

## Prism Launcher — produção (`main`) vs desenvolvimento (`dev`)

Sim: podes ter **duas instâncias** no Prism, ambas com o mesmo fluxo packwiz (bootstrap + `pack.toml` no GitHub), mas cada uma segue um **branch** diferente. Os jogadores em produção continuam só a puxar **`main`**; tu testas em **`dev`** sem alterar o URL que eles usam.

### Ideia

| Instância | Branch no URL | Uso |
| --- | --- | --- |
| **NotVanilla** (produção) | `main` | Alinhado ao que releases / README apontam; mesmo que a maioria dos clientes. |
| **NotVanilla Dev** | `dev` | Mods experimentais, pins novos, quebras temporárias — `packwiz refresh` + push para `dev`. |

O instalador packwiz resolve `index.toml` e o resto dos ficheiros relativamente ao URL do `pack.toml`. Com **raw GitHub** basta trocar o segmento do branch.

**Produção (atual padrão do repo):**

```text
https://raw.githubusercontent.com/renandadalte/notvanilla/main/pack.toml
```

**Desenvolvimento:**

```text
https://raw.githubusercontent.com/renandadalte/notvanilla/dev/pack.toml
```

### Ficheiros de referência no repo

| Ficheiro | Branch no URL packwiz |
| --- | --- |
| [`instance.cfg`](../instance.cfg) | `main` (produção / mesma linha que a maioria dos jogadores) |
| [`instance.dev.cfg`](../instance.dev.cfg) | `dev` (testes no teu PC de jogo ou noutra máquina na rede) |

No PC onde está o Prism (pode ser diferente do servidor de git): para a instância **Dev**, usa o conteúdo de **`instance.dev.cfg`** — ou copia o ficheiro para a pasta dessa instância **com o nome `instance.cfg`**, ou cola só a linha **`PreLaunchCommand`** nas definições da instância (**Edit instance → Custom commands**). O fluxo é o **mesmo** que com `main`: cada **Play** corre o bootstrap e sincroniza com o `pack.toml` desse branch no GitHub.

**Raw (outro PC na rede, sem clonar o repo):**

- `https://raw.githubusercontent.com/renandadalte/notvanilla/main/instance.cfg`
- `https://raw.githubusercontent.com/renandadalte/notvanilla/dev/instance.dev.cfg` — requer o branch **`dev`** no GitHub; o mesmo ficheiro costuma existir em `main` também para referência.

### Passos no Prism (resumo)

1. **Produção:** mantém [`instance.cfg`](../instance.cfg) (URL `.../main/pack.toml`).
2. **Dev:** duplica a instância (**Copy Instance**), abre **Edit instance → Custom commands** e define o **Pre-launch command** igual ao de [`instance.dev.cfg`](../instance.dev.cfg) (URL `.../dev/pack.toml`). Ajusta **nome** da instância para `NotVanilla Dev` (opcional, só organização).
3. Garante que o branch **`dev`** existe no GitHub (`git push -u origin dev` a partir de `main` quando ainda não existir); sem isso o URL `.../dev/pack.toml` devolve **404**.
4. Cada instância tem a **sua pasta** → mundos e configs **isolados**.

### Fluxo de git sugerido

- Trabalho arriscado ou WIP: commits em **`dev`**; abre só a instância Dev no Prism.
- Quando estiver estável: **merge** `dev` → `main` (ou PR), atualiza **CHANGELOG** / versão em `pack.toml` se for release visível.
- Quem usa só `main` (zip de release ou URL fixo) **nunca** vê o `dev` até merges.

### Alternativas (quando faz sentido)

- **Um só branch + instância local sem URL remota:** clona o repo, corre `packwiz` na pasta e aponta o Prism para essa instância manualmente — bom para quem edita o pack o dia todo, **mau** para “igual ao jogador” porque deixa de espelhar o download HTTP.
- **`packwiz serve` em localhost:** útil para testar o índice antes de push; para jogar no dia a dia, as **duas instâncias + raw `main`/`dev`** costumam ser mais simples.

## `.packwizignore` vs `.gitignore`

**`packwiz refresh`** adds every file under the pack root to **`index.toml`**, except paths matched by **`.packwizignore`**. The packwiz installer then downloads **each indexed file** from your hosted pack URL (e.g. GitHub Pages).

- **`.gitignore`** only affects git — it does **not** stop packwiz from indexing those paths.
- Local folders like **`.agent/`** and **`logs/`** must appear in **`.packwizignore`** too, or clients will get **404** (those files are never pushed to GitHub).
- Dev-only trees such as **`docs/`** can be ignored in the pack index if you do not want them copied into every player instance; they remain in the repo for GitHub.

## Default mod configs (`config/`)

From **`0.0.9-alpha`**, the repo ships a **`config/`** tree so packwiz can **sync the same defaults** to Prism instances and to the dedicated server (only files for **mods that are actually in the pack**).

- When you paste configs from another modpack or instance, **prune** anything that does not belong to a mod listed in `mods/*.pw.toml` before committing (avoids noise and wrong assumptions).
- **`config/sodium-fingerprint.json`** is **per machine** — it is **gitignored** and listed in **`.packwizignore`** so it is not indexed for clients.
- **`config/spark/tmp/`** and **`config/spark/tmp-client/`** are runtime profiler noise — keep them out of git (`.packwizignore` covers them if they appear locally).

## Changing the mod set

1. Add, remove, or edit files under `mods/*.pw.toml` and `shaderpacks/*.pw.toml` (and optional `optional/` / disabled layouts if you adopt them later).
2. Run **`packwiz refresh`** from the repository root so `index.toml` hashes match the tree.
3. Update **`docs/MODS_INVENTORY.md`** in the same change set: **Active** rows ↔ `mods/*.pw.toml` and `shaderpacks/*.pw.toml`; adjust **Listed** / **Discarded** if the conversation moves entries between backlog and shipped.
4. Update **`CHANGELOG.md`** when the change is user-visible (new mod, removal, fix).
5. If a shipped mod writes defaults you want everyone to share, add or update the matching paths under **`config/`** and re-run **`packwiz refresh`**.
6. Follow deploy rules in `~/.agents/context/NOTVANILLA_MODPACK.md` for dedicated server alignment (never push without explicit confirmation in chat).

## Conventions

- **`side` in `.pw.toml`:** `client`, `server`, or `both` — authoritative for client-only installs vs server.
- **Mod page URL:** Prefer stable project pages (e.g. Modrinth `https://modrinth.com/mod/<slug>`). The `.pw.toml` `[update.modrinth]` block holds the project id for tooling.
- **Discarded mods:** When a mod leaves the pack, remove its `.pw.toml`, add a row under **Discarded mods** (date + reason in **Notes**), and remove it from **Active**. **Listed** is for candidates not yet in packwiz.

## Quality checks before merge

- [ ] `packwiz refresh` run; `index.toml` committed if it changed.
- [ ] `docs/MODS_INVENTORY.md` — **Active** row count matches `mods/*.pw.toml` plus `shaderpacks/*.pw.toml`.
- [ ] `CHANGELOG.md` updated if players care about the change.
- [ ] If **`config/`** changed: only mods **in the pack**; no `sodium-fingerprint.json` or Spark `tmp*` trees in git; **`grep`** `index.toml` for stray paths (e.g. old mod names) after refresh.
