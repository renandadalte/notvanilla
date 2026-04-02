# Mapa de módulos do pack

Este documento agrupa o modpack em blocos operacionais para teste e ajuste incremental. Ele **não substitui** [MODS_INVENTORY.md](./MODS_INVENTORY.md), que continua sendo o inventário canônico e alfabético do pack.

Use este mapa quando quiser:

- mexer em um conjunto pequeno de features sem tratar o pack inteiro como uma caixa preta;
- montar smoke tests por área funcional;
- entender quais configs, libs e dependências tendem a mudar juntas;
- decidir se uma alteração deve ficar no `dev` por mais tempo antes de ir para `main`.

## Como ler

- Cada mod aparece no seu módulo primário.
- Dependências compartilhadas podem aparecer como suporte em mais de um módulo.
- Se um ajuste tocar um módulo-base, teste também os módulos que dependem dele.

## Módulos

| Módulo | O que cobre | Mods principais | Configs / arquivos associados | Smoke test alvo |
| --- | --- | --- | --- | --- |
| Base e bibliotecas | Camada de suporte para configs, telas e dependências compartilhadas. | Default Options, Fabric API, Architectury API, Balm, Cloth Config API, Collective, Fabric Language Kotlin, Forge Config API Port, JamLib, Paxi, Puzzles Lib, Searchables, TCDCommons API, Text Placeholder API, Yet Another Config Lib, YUNG's API | `config/defaultoptions/*`, `config/paxi/*`, `config/yacl.json5` e, indiretamente, várias telas de configuração | Subir a instância limpa, abrir algumas telas de config, validar os defaults/client packs globais e confirmar que dependentes carregam sem erro. |
| Performance e renderização | Otimizações de client, render pipeline e rede. | Sodium, Indium, Iris Shaders, Entity Culling, ImmediatelyFast, FerriteCore, Lithium, ModernFix, Krypton | `config/sodium-options.json`, `config/sodium-mixins.properties`, `config/iris.properties`, `config/iris-excluded.json`, `config/entityculling.json`, `config/immediatelyfast.json`, `config/ferritecore.mixin.properties`, `config/lithium.properties`, `config/modernfix-mixins.properties` | Abrir mundo novo, trocar shader, comparar FPS e confirmar ausência de conflito de mixins. |
| Camera e perspectiva | F5, câmera em terceira pessoa e corpo em primeira pessoa. | AFK Camera, Client Tweaks, Countered's Smooth F5, Leawind's Third Person, Real Camera | `config/leawind_third_person.json`, `config/realcamera.json` | Testar alternância de câmera, cavalo, agachamento, espaços apertados e visão em primeira pessoa. Se `Client Tweaks` mudar, revalide também atalhos de inventário. |
| Combate e animação | Feels de combate, dodge, animações e sincronização visual. | Better Combat, Combat Roll, Not Enough Animations, Player Animator | `config/bettercombat/client.json5`, `config/bettercombat/fallback_compatibility.json`, `config/bettercombat/server.json5`, `config/bettercombat/weapon_trails.json`, `config/notenoughanimations.json` | Testar swing, roll, sweeping, arma de duas mãos e multiplayer. |
| Interface, inventário e HUD | Fluxo de inventário, leitura de informações e atalhos do cliente. | AppleSkin, Better Advancements, Better Ping Display [Fabric], Better Statistics Screen, BetterF3, Clean Tooltips, Controlling, Crafting Tweaks, Hidden Recipe Book, Inventory Essentials, InvMove, InvMoveCompats, Jade, Just Enough Items (JEI), Mod Menu, Mouse Tweaks, Pick Up Notifier, Screenshot to Clipboard, StartInv, TrashSlot | `config/modmenu.json` | Abrir inventário, buscar receitas, usar JEI, testar InvMove, notar pickup, revisar HUD e atalhos. |
| Interação com o mundo e travessia | Movimentação, blocos, cavalos e ajustes de jogabilidade local. | Call Your Horse, Creative Fly, Easy Anvils, Easy Magic, Easy Shulker Boxes, Horse Expert, Improved Sign Editing, KleeSlabs, Omnidirectional Movement, Simple Homing XP, Wall-Jump TXF | `config/walljump.json` | Testar cavalo, wall-jump, slabs, XP homing, edição de placas e blocos de utilidade. |
| Ferramentas de worldgen | Preview de seed, biomas e terreno antes da geração real. | World Preview | — | Abrir o `Preview` no menu Singleplayer, gerar um seed de teste, alternar biome map/heightmap/structures e conferir que a pré-visualização acompanha o stack de worldgen carregado. |
| Regras do servidor e multiplayer | Serviços e regras que fazem sentido no mundo compartilhado. | Death Backup, Dismount Entity, EasyAuth, Hand Over Your Items, Leaves Be Gone, No Feather Trample, Ready Player Fun, RightClickHarvest, Set World Spawn Point, SimpleAFK, WITS | `config/EasyAuth/*` no host e configs locais do servidor quando aplicável | Validar login, whitelist, AFK, spawn, agricultura, backup, troca de itens e identificação de estruturas. |
| Visuais e assets | Aparência do jogador, shader e resource packs. | Fresh Animations, Fresh Animations: Player Extension, MakeUp - Ultra Fast | `shaderpacks/*.pw.toml`, `resourcepacks/*.pw.toml`, `config/iris.properties`, `config/paxi/resourcepack_load_order.json` | Conferir ordem dos resource packs, ativação do shader e compatibilidade visual com o corpo do player. |
| Diagnóstico e profiling | Medição, inspeção e apoio para investigação de performance. | Observable, spark | `config/observable.json`, `config/spark/config.json`, `config/spark/activity.json` | Rodar perfil Spark, abrir a UI de observabilidade e manter `activity.json` sanitizado no repo. |

## Leituras rápidas por mudança

- Mudou câmera? Comece em `Camera e perspectiva` e depois rode um smoke curto em `Interface, inventário e HUD`.
- Mudou combate? Teste `Combate e animação` e depois um mundo com `Performance e renderização`.
- Mudou worldgen ou biomas? Comece em `Ferramentas de worldgen` e depois valide `Performance e renderização`.
- Mudou libs ou telas de config? Teste `Base e bibliotecas` e os módulos dependentes.
- Mudou uma regra do mundo ou do servidor? Teste `Regras do servidor e multiplayer`.
- Mudou aparência? Teste `Visuais e assets` com `Performance e renderização`.

## Relação com o inventário

Se este mapa e [MODS_INVENTORY.md](./MODS_INVENTORY.md) divergirem, o inventário continua sendo a fonte da verdade para o que está ativo no pack. O mapa de módulos serve para decidir escopo de teste e manutenção.
