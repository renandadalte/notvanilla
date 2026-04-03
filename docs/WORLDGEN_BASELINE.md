# Baseline de worldgen

Este documento consolida a decisão atual para o Overworld e os perfis de teste que vamos usar para comparar variações sem misturar muitos eixos ao mesmo tempo.

## Baseline recomendado

- `Natural Temperature` como camada de clima e coerência geográfica.
- `Lithostitched` como dependência de suporte obrigatória para `Tectonic`.
- `Tectonic` como camada de macro-terreno: continentes, mares, ilhas e rios em escala maior.
- `WWOO` como camada de biomas, transições e refinamento do mundo.
- `Distant Horizons` como camada de LOD de longo alcance, instalada em cliente e servidor para o multiplayer enxergar além da view distance padrão.
- `Fabric/Quilt Chunk Pregenerator` como ferramenta operacional no servidor para pregenerar a região inicial antes de liberar o mundo.
- `World Preview` para inspecionar seed, biomas, terreno e estruturas antes de gerar um mundo de verdade.
- Neste pack, `Natural Temperature` e `Set World Spawn Point` são distribuídos como `both` para que o client do singleplayer carregue o mesmo stack que o servidor integrado.
- O preset ativo de `Natural Temperature` fica em `config/natural-temperature.json` e é tratado como preferência do jogador, então usa `preserve = true`. Os presets de comparação ficam em `config/natural-temperature-presets/mode5.json` e `config/natural-temperature-presets/mode6.json`.

### Por que essa ordem

- `Natural Temperature` mantém a lógica de faixas climáticas, mas com uma superfície de UI mais simples para o nosso fluxo de teste.
- `Lithostitched` é suporte técnico; não é uma peça de design, mas precisa estar presente para o stack subir.
- `Tectonic` já entrega a sensação de grandes massas continentais e oceanos largos, então `Continents` fica redundante no baseline.
- `WWOO` mantém o overworld mais coerente e ainda abre espaço para variação sem exigir um pacote de fantasia pesado desde o início.
- `World Preview` serve para validar o stack sem depender de exploração manual cega.
- `Distant Horizons` é o caminho DH real para multiplayer; ele fica fora da comparação com `Bobby`, `BetterView` e `Nvidium`, que continuam sendo branches alternativas e não baseline.

## O que fica fora do baseline

- `Terralith` sai da linha principal enquanto `Natural Temperature` estiver ativo, porque a combinação atual não é a trilha mais limpa.
- `Latitude` fica como branch de comparação, mas saiu do baseline porque o teste visual estava parecendo mais uma colcha de retalhos e a UI dele poluía o `World Preview`.
- `Continents` vira perfil de comparação, não peça central.
- `Geophilic` continua como polimento leve do vanilla, mas não como pilar do pack.
- `Biomes O' Plenty` e `Regions Unexplored` entram como alternativas de suíte de biomas quando a prioridade subir de coerência para variedade.
- `Set World Spawn Point` continua sendo a camada de spawn; ele pode fixar o worldspawn em `0,0` sem depender do mod climático.

## Presets de temperatura

- `mode 5` é o preset ativo do pack para este ciclo de teste: ele usa os controles manuais de temperatura e umidade para testar uma distribuição mais customizada sem mudar o resto do stack.
- `mode 6` segue como comparação rápida caso você queira voltar para a leitura banded mais direta.
- Ambos compartilham o mesmo `equatorial_distance`, `equator_offset`, `looping_world`, `wave_magnification` e cobertura geral de bandas para que a comparação fique focada no modo.
- Para alternar no client local, copie o preset desejado para `config/natural-temperature.json` dentro da instância do Prism e reinicie o jogo. O mundo do servidor continua precisando ser criado com seed `0` no host para manter o teste repetível.

## Perfis de teste

| Perfil | Composição | Objetivo |
| --- | --- | --- |
| Controle de terreno | `Lithostitched + Tectonic` | Medir a escala de continentes, mares e rios sem interferência de outras suítes. |
| Coerência climática | `Natural Temperature + Lithostitched + Tectonic` | Validar se as faixas climáticas deixam biomas vizinhos mais lógicos. |
| Baseline | `Natural Temperature + Lithostitched + Tectonic + WWOO` | Validar o stack recomendado para o pack principal. |
| Baseline multiplayer | `Natural Temperature + Lithostitched + Tectonic + WWOO + Distant Horizons + Fabric/Quilt Chunk Pregenerator` | Validar que o starter region chega pregenerado, o cliente recebe LODs no login e o servidor mantém o fluxo DH estável. |
| Branch de fantasia | `Lithostitched + Tectonic + Terralith` | Comparar um branch mais lúdico e visualmente mais exuberante. |
| Branch de biomas grandes | `Natural Temperature + Lithostitched + Tectonic + Biomes O' Plenty` ou `Natural Temperature + Lithostitched + Tectonic + Regions Unexplored` | Trocar a suíte de biomas por uma mais exótica sem perder o eixo de clima/terreno. |
| Comparação marítima | `Continents` | Medir a sensação de ilhas maiores e mares mais vazios antes de qualquer sobreposição. |

## Protocolo de comparação

- Rodar cada perfil em mundo novo, com seed fixo.
- Começar em `16` chunks de view distance, sem Distant Horizons e sem shaders.
- Repetir em `32` chunks com shaders.
- Antes de abrir o mundo para jogadores, rodar `Fabric/Quilt Chunk Pregenerator` no servidor com `/pregen start 128` e depois gerar os LODs com `/dh pregen`.
- Deixar `64` chunks com Distant Horizons por último, porque aí o custo combinado de worldgen, streaming, pregeneration e renderização já domina o teste.
- Observar distância entre massas de terra, largura dos mares, continuidade dos rios, frequência de biomas raros e sensação geral de coerência.

## Fontes

- [Latitude](https://modrinth.com/mod/latitude)
- [Natural Temperature](https://modrinth.com/mod/natural-temperature)
- [Lithostitched](https://modrinth.com/mod/lithostitched)
- [Tectonic](https://modrinth.com/datapack/tectonic)
- [WWOO](https://modrinth.com/mod/wwoo)
- [World Preview](https://modrinth.com/mod/world-preview)
- [Distant Horizons](https://modrinth.com/mod/distanthorizons)
- [Fabric/Quilt Chunk Pregenerator](https://modrinth.com/mod/fabricquilt-chunk-pregenerator)
- [Continents](https://modrinth.com/datapack/continents)
- [Terralith](https://modrinth.com/datapack/terralith)
- [Biomes O' Plenty](https://modrinth.com/mod/biomes-o-plenty)
- [Geophilic](https://modrinth.com/datapack/geophilic)
- [Regions Unexplored](https://modrinth.com/mod/regions-unexplored)
- [Set World Spawn Point](https://modrinth.com/mod/set-world-spawn-point)
