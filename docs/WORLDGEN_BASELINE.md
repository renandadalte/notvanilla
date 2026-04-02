# Baseline de worldgen

Este documento consolida a decisão atual para o Overworld e os perfis de teste que vamos usar para comparar variações sem misturar muitos eixos ao mesmo tempo.

## Baseline recomendado

- `Latitude` como camada de clima e coerência geográfica.
- `Lithostitched` como dependência de suporte obrigatória para `Tectonic`.
- `Tectonic` como camada de macro-terreno: continentes, mares, ilhas e rios em escala maior.
- `WWOO` como camada de biomas, transições e refinamento do mundo.
- `World Preview` para inspecionar seed, biomas, terreno e estruturas antes de gerar um mundo de verdade.

### Por que essa ordem

- `Latitude` é o que mais diretamente empurra biomas para faixas climáticas que fazem sentido.
- `Lithostitched` é suporte técnico; não é uma peça de design, mas precisa estar presente para o stack subir.
- `Tectonic` já entrega a sensação de grandes massas continentais e oceanos largos, então `Continents` fica redundante no baseline.
- `WWOO` mantém o overworld mais coerente e ainda abre espaço para variação sem exigir um pacote de fantasia pesado desde o início.
- `World Preview` serve para validar o stack sem depender de exploração manual cega.

## O que fica fora do baseline

- `Terralith` sai da linha principal enquanto `Latitude` estiver ativo, porque a combinação atual não é a trilha mais limpa.
- `Continents` vira perfil de comparação, não peça central.
- `Geophilic` continua como polimento leve do vanilla, mas não como pilar do pack.
- `Biomes O' Plenty` e `Regions Unexplored` entram como alternativas de suíte de biomas quando a prioridade subir de coerência para variedade.

## Perfis de teste

| Perfil | Composição | Objetivo |
| --- | --- | --- |
| Controle de terreno | `Lithostitched + Tectonic` | Medir a escala de continentes, mares e rios sem interferência de outras suítes. |
| Coerência climática | `Latitude + Lithostitched + Tectonic` | Validar se as faixas latitudinais deixam biomas vizinhos mais lógicos. |
| Baseline | `Latitude + Lithostitched + Tectonic + WWOO` | Validar o stack recomendado para o pack principal. |
| Branch de fantasia | `Lithostitched + Tectonic + Terralith` | Comparar um branch mais lúdico e visualmente mais exuberante. |
| Branch de biomas grandes | `Latitude + Lithostitched + Tectonic + Biomes O' Plenty` ou `Latitude + Lithostitched + Tectonic + Regions Unexplored` | Trocar a suíte de biomas por uma mais exótica sem perder o eixo de clima/terreno. |
| Comparação marítima | `Continents` | Medir a sensação de ilhas maiores e mares mais vazios antes de qualquer sobreposição. |

## Protocolo de comparação

- Rodar cada perfil em mundo novo, com seed fixo.
- Começar em `16` chunks de view distance, sem Distant Horizons e sem shaders.
- Repetir em `32` chunks com shaders.
- Deixar `64` chunks com Distant Horizons por último, porque aí o custo combinado de worldgen, streaming e renderização já domina o teste.
- Observar distância entre massas de terra, largura dos mares, continuidade dos rios, frequência de biomas raros e sensação geral de coerência.

## Fontes

- [Latitude](https://modrinth.com/mod/latitude)
- [Lithostitched](https://modrinth.com/mod/lithostitched)
- [Tectonic](https://modrinth.com/datapack/tectonic)
- [WWOO](https://modrinth.com/mod/wwoo)
- [World Preview](https://modrinth.com/mod/world-preview)
- [Continents](https://modrinth.com/datapack/continents)
- [Terralith](https://modrinth.com/datapack/terralith)
- [Biomes O' Plenty](https://modrinth.com/mod/biomes-o-plenty)
- [Geophilic](https://modrinth.com/datapack/geophilic)
- [Regions Unexplored](https://modrinth.com/mod/regions-unexplored)
