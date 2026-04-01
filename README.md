# NotVanilla

NotVanilla é um modpack Fabric para Minecraft `1.21.1` focado em três frentes: movimentação mais gostosa, combate mais interessante e uma base leve o bastante para continuar prática no dia a dia. A ideia não é fugir totalmente da identidade vanilla, mas empurrá-la para uma versão mais confortável, expressiva e estável.

## Canais do projeto

- `main`: canal de produção, pensado para a instância principal dos jogadores.
- `dev`: canal de testes, usado para validar mudanças antes de promover para `main`.

Hoje a separação vale principalmente para o client. O servidor dedicado acompanha a linha `dev` enquanto o pack ainda está em iteração mais rápida.

## Como instalar a instância `main`

1. Abra o Prism Launcher.
2. Clique em **Add Instance**.
3. Escolha **Import from zip**.
4. Use a URL:

```text
https://github.com/renandadalte/notvanilla/releases/latest/download/NotVanilla.zip
```

Essa instância já vem preparada para rodar o `packwiz-installer-bootstrap` no lançamento e seguir o canal estável publicado em:

```text
https://renandadalte.github.io/notvanilla/main/pack.toml
```

## Como instalar a instância `dev`

Você pode importar uma instância separada de testes diretamente pelo ZIP:

```text
https://github.com/renandadalte/notvanilla/releases/download/dev-latest/NotVanilla-dev.zip
```

Ela aponta para o canal de testes publicado em:

```text
https://renandadalte.github.io/notvanilla/dev/pack.toml
```

Se preferir, também dá para duplicar a instância principal no Prism e trocar apenas o `PreLaunchCommand` para o URL do canal `dev`.

## Onde ficam os detalhes técnicos

- [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md): manutenção do pack, fluxo `main`/`dev`, packwiz, publicação e deploy.
- [docs/MODS_INVENTORY.md](docs/MODS_INVENTORY.md): inventário do que está no pack, backlog e mods descartados.
- [CHANGELOG.md](CHANGELOG.md): histórico voltado para mudanças visíveis para quem joga.

## Requisitos rápidos

- Minecraft `1.21.1`
- Fabric Loader `0.18.4`
- Prism Launcher

Se você só quer jogar, use o ZIP do canal desejado. Se vai mexer no pack, a documentação técnica em [`docs/`](docs/) é a fonte mais útil.

## Comandos de pre-launch

Se você duplicar a instância manualmente no Prism Launcher ou precisar corrigir o `PreLaunchCommand`, use estes valores:

`main`

```text
"$INST_JAVA" -jar packwiz-installer-bootstrap.jar https://renandadalte.github.io/notvanilla/main/pack.toml
```

`dev`

```text
"$INST_JAVA" -jar packwiz-installer-bootstrap.jar https://renandadalte.github.io/notvanilla/dev/pack.toml
```
