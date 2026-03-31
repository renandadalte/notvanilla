# NotVanilla ⚔️🧭

Um modpack de Minecraft focado em **exploração profunda**, **movimentação fluida**, **combate técnico** e **desafios intensos**. Desenvolvido para transformar a experiência vanilla em uma jornada épica e recompensadora.

## 🚀 Pilares do Projeto
- **Exploração:** Novos biomas, estruturas e segredos (Em breve).
- **Combate & Desafio:** IA de mobs e mecânicas dinâmicas (Em breve).
- **Movimentação:** Agilidade na travessia do mundo (Em breve).
- **Performance & Debugging:** Otimizado com as melhores tecnologias Fabric para a versão 1.21.1, incluindo otimizações de rede e ferramentas para diagnóstico (ex.: **Observable**). **Spark** continua no pack para **investigar lag** quando precisares — não faz parte do fluxo de benchmark rotineiro.
- **Gráficos (cliente):** **Iris** + **Sodium** e o shader base **MakeUp - Ultra Fast** (pacote leve com boa relação qualidade/desempenho). No jogo: **Opções de vídeo → Pacotes de shader** — ativa o pack e, se o FPS cair, reduz perfis/opções *dentro* das definições do shader (o pack é pensado para ser ajustável em máquinas modestas).

## Benchmark padrão (desenvolvimento) — HWiNFO

O datapack **`benchmark`** (`datapacks/benchmark/`) define um cenário **repetível** de **1200 ticks** (~60 s) em **spectator** a partir de **`0 150 0`**: **600 ticks** em **+Z** (~1,5 blocos/tick), **teleporte de volta** ao spawn, **mais 600 ticks** em +Z (segunda passagem com chunks já carregados).

**Fluxo sugerido (simples):**

1. **HWiNFO:** inicia o **log** (CSV) com as colunas que te interessam (CPU, GPU, RAM, FPS, etc.).
2. **Servidor (consola ou RCON):** `function benchmark:start` — entra no mundo antes, se fores tu a voar em spectator.
3. Espera **~60 s**; ao terminar ouves um som e uma mensagem no chat.
4. **Para o log HWiNFO** e guarda o ficheiro com **data + versão do pack** (e notas no teu registo local, ex. `.agent/benchmark-runs.md`).

**Spark (opcional, diagnóstico):** quando houver **lag** ou quiseres **flame graph**, usa **`spark` / `/sparkc`** à parte — [documentação](https://spark.lucko.me/docs/Command-Usage). Não é necessário para comparar runs só com HWiNFO.

**Servidor dedicado:** copia `datapacks/benchmark/` para **`<pasta-do-mundo>/datapacks/benchmark/`** e **`reload`** para aparecer `file/benchmark (world)`.

Notas de operação mais longas (seed fixa, backups de mundo) podem ficar numa skill ou checklist local; o repo mantém só o datapack e este README.

## 🛠️ Instalação e Configuração (Prism Launcher)

Para a melhor experiência e para receber atualizações automáticas via `packwiz`, recomendamos o **Prism Launcher**.

### 1. Instalação do Prism Launcher
1. Acesse [prismlauncher.org](https://prismlauncher.org/download/) e baixe a versão para o seu sistema operacional.
2. Siga as instruções de instalação padrão. O Prism Launcher detectará automaticamente o Java necessário.

### 2. Configuração Global de Memória (RAM)
Antes de baixar o modpack, para garantir que o NotVanilla rode com estabilidade e sem picos de lag (stuttering), configure a alocação de RAM globalmente no launcher:

1. No Prism Launcher, clique em **Settings** (ícone de engrenagem no topo).
2. No menu lateral, selecione **Java**.
3. Na seção **Memory** (Memória), configure os campos de forma idêntica:

#### Opção A: PCs com MAIS de 8GB de RAM total (Recomendado)
- **Minimum memory (Mínimo):** `8192 MiB` (8GB).
- **Maximum memory (Máximo):** `8192 MiB` (8GB).

#### Opção B: PCs com 8GB ou MENOS de RAM total
- **Minimum memory (Mínimo):** `4096 MiB` (4GB).
- **Maximum memory (Máximo):** `4096 MiB` (4GB).

### 3. Adicionando o NotVanilla (Auto-Atualizável)
Este método configura o modpack para se atualizar sozinho toda vez que você clicar em "Play":

1. No Prism Launcher, clique em **Add Instance** (Adicionar Instância).
2. Selecione a aba **Import from zip** (Importar de zip) na barra lateral.
3. Clique no botão **URL** e cole o seguinte link oficial de lançamento:
   `https://github.com/renandadalte/notvanilla/releases/latest/download/NotVanilla.zip`
4. Clique em **OK** para criar a instância.
5. **Pronto!** Ao iniciar o jogo, o `packwiz` fará o download de todos os mods na versão correta e manterá o pack sempre atualizado.

---
*Base 0.0.1: Estrutura oficial, otimização e auto-atualização por GitHub Actions e packwiz.*