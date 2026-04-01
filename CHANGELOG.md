# Changelog

Todas as mudanças relevantes do NotVanilla ficam registradas aqui.

O formato segue a ideia do [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) e as versões continuam compatíveis com [Semantic Versioning](https://semver.org/spec/v2.0.0.html), adaptadas ao ritmo atual do pack.

## [Não lançado]

### Alterado
- O fluxo de atualização automática dos clientes passa a usar **GitHub Pages** como origem dos canais `main` e `dev`, em vez de depender de `raw.githubusercontent.com` ou `jsDelivr` apontando para branch viva.
- O `index.toml` deixa de publicar arquivos de bootstrap, documentação e automação que não fazem parte do runtime do pack.

### Adicionado
- Workflow para publicar os canais `main` e `dev` de forma atômica no GitHub Pages.
- Workflow de validação do repositório para checar coerência de `pack.toml` e `index.toml`, além de uma auditoria básica de exposição do repositório.
- ZIP rotativo de bootstrap para o canal `dev`, separado do ZIP estável de produção.
- Scripts versionados para validar o estado do packwiz, auditar a superfície do repositório e montar o artefato do GitHub Pages.

### Corrigido
- O canal `dev` deixa de depender de alias de CDN em branch, que podia servir `pack.toml` e `index.toml` fora de sincronia e causar erro de hash no Prism.

## [0.0.11-alpha] - 2026-03-31

### Adicionado
- Grande leva de mods de qualidade de vida, utilidades, HUD, inventário, movimento e apoio ao combate.
- **EasyAuth** como mod **server-only** para proteger o servidor dedicado em `online-mode=false`, com senha global de convite para o primeiro cadastro e senha individual depois disso.

### Alterado
- `instance.dev.cfg` passou a usar `jsDelivr` no lugar de `raw.githubusercontent.com` para reduzir o atraso de cache que estava afetando o branch `dev`.
- **e4mc** virou mod **client-only**: continua útil para sessões improvisadas entre clientes, mas sai do fluxo do servidor público dedicado.

### Corrigido
- Ajustes no `.packwizignore` e na coerência entre `pack.toml` e `index.toml` para reduzir erros do instalador packwiz.

### Notas
- **ItemPickupNotifier** continua pedindo validação manual em `1.21.1`, porque o metadata exposto na API do Modrinth não está alinhado com a versão real usada no pack.

## [0.0.10-alpha] - 2026-03-31

### Alterado
- Limpeza e atualização dos defaults em `config/`, mantendo no repositório apenas arquivos que pertencem aos mods realmente enviados no pack.

### Notas
- Esse release fechou a rodada de alinhamento entre câmera, movimento e combate antes da próxima leva de mudanças.

## [0.0.9-alpha] - 2026-03-31

### Adicionado
- **Wall-Jump TXF** voltou ao `main`.
- A pasta `config/` passou a fazer parte do repositório de forma controlada, para sincronizar defaults entre clientes e servidor.

### Alterado
- `.gitignore` e `.packwizignore` passaram a ignorar o `sodium-fingerprint` e diretórios temporários do Spark.

## [0.0.8-alpha] - 2026-03-31

### Adicionado
- Stack de movimento, câmera e combate no `main`: Leawind's Third Person, Real Camera, Countered's Smooth F5, Omnidirectional Movement, Not Enough Animations, Player Animator e Better Combat.
- Resource packs **Fresh Animations** e **Fresh Animations: Player Extension**.

### Removido
- **First Person Model**, substituído por uma combinação mais estável com **Real Camera**.
- **Wall-Jump TXF** saiu temporariamente do `main` nessa linha e voltou no release seguinte.

## [0.0.7-alpha] - 2026-03-31

### Removido
- **Wall-Jump TXF** do `main`, mantendo o mod apenas na linha de testes naquele momento.

## [0.0.6-alpha] - 2026-03-31

### Adicionado
- **Cloth Config API**, para ampliar a compatibilidade do pack com telas de configuração.

## [0.0.5-alpha] - 2026-03-31

### Adicionado
- **Mod Menu**, **Text Placeholder API** e **YACL**.
- **Wall-Jump TXF** no `dev`.
- Primeira rodada mais forte do stack de movimento, câmera e combate no branch `dev`.
- Resource packs **Fresh Animations** e **Fresh Animations: Player Extension** no fluxo do pack.

### Notas
- **ParCool!** ficou fora por falta de build Fabric adequada para `1.21.1`.

## [0.0.4] - 2026-03-31

### Adicionado
- **Iris Shaders**.
- **MakeUp - Ultra Fast** como shader base enviado pelo pack.
- `instance.dev.cfg` como modelo de instância Prism para o branch `dev`.

### Corrigido
- Ajustes em `.packwizignore` para impedir que caminhos locais e documentação gerassem 404 no instalador.

## [0.0.3] - 2026-03-29

### Adicionado
- Datapack `benchmark` com cenário repetível de voo em spectator para medições comparáveis.

### Alterado
- O fluxo de benchmark passou a priorizar **HWiNFO** como baseline, deixando o Spark como ferramenta de diagnóstico mais pontual.

## [0.0.2] - 2026-03-22

### Adicionado
- **ImmediatelyFast** e **Krypton** para reforçar a linha de performance.
- **Spark** e **Observable** como ferramentas de profiling.
- Dependências obrigatórias como **Architectury API** e **Fabric Language Kotlin**.

## [0.0.1] - 2026-03-22

### Adicionado
- Estrutura inicial do modpack com `packwiz` para Minecraft `1.21.1`.
- Base de performance com **Entity Culling**, **FerriteCore**, **Indium**, **Lithium**, **ModernFix** e **Sodium**.
- Integração inicial com **Fabric API**.
- Automação de release para gerar o ZIP de bootstrap do Prism.

### Alterado
- Ajustes iniciais de `.gitignore` e `.packwizignore` para manter o repositório e o pack mais limpos.
