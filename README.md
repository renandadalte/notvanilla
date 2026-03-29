# NotVanilla ⚔️🧭

Um modpack de Minecraft focado em **exploração profunda**, **movimentação fluida**, **combate técnico** e **desafios intensos**. Desenvolvido para transformar a experiência vanilla em uma jornada épica e recompensadora.

## 🚀 Pilares do Projeto
- **Exploração:** Novos biomas, estruturas e segredos (Em breve).
- **Combate & Desafio:** IA de mobs e mecânicas dinâmicas (Em breve).
- **Movimentação:** Agilidade na travessia do mundo (Em breve).
- **Performance & Debugging:** Otimizado com as melhores tecnologias Fabric para a versão 1.21.1, incluindo otimizações de rede e ferramentas para diagnóstico de performance (Spark e Observable).

## Benchmark padrão (desenvolvimento)

O pack inclui o datapack **`benchmark`** (`datapacks/benchmark/`): cenário fixo de **~60 s** em **spectator** (teleporte em linha a partir de `0 150 0`) para alinhar perfis **Spark** no servidor e no cliente.

- **Servidor (consola):** `function benchmark:start` — inicia o cenário; termina sozinho com mensagem no chat.
- **Spark no cliente (Fabric):** usar **`/sparkc`** (não `/spark`) — ex.: `/sparkc profiler start` / `/sparkc profiler stop` ([documentação](https://spark.lucko.me/docs/Command-Usage)).
- **Spark no servidor (consola):** `spark profiler start` / `spark profiler stop` (sem `/` na consola dedicada).
- **Servidor dedicado:** copie `datapacks/benchmark/` para **`<pasta-do-mundo>/datapacks/benchmark/`** (ex.: `world/datapacks/benchmark/`), não basta deixar só na raiz do servidor; depois execute **`reload`** na consola para o pack aparecer como `file/benchmark (world)`.

Fluxo operacional detalhado (reset com seed `0`, HWiNFO, registo de resultados) está na skill local **`notvanilla-spark-benchmark`** em `~/.agents/skills/notvanilla-spark-benchmark/` (não versionada no repo).

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