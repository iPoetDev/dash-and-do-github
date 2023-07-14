### Badge: [![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)

# Source

-   Pre-Commit Repo [URL]: [github.com/pre-commit/mirrors-prettier](https://github.com/pre-commit/mirrors-prettier)
-   Hook ID
    -   `prettier`
-   Category | Intent: Code Formatting | Code Quality | Code Style Consistency
-   Description:
    -   Prettier is an opinionated code formatter.
    -   It enforces
        -   a consistent style by parsing your code and
        -   re-printing it with its own rules that take the maximum line length into account, wrapping code when
            necessary.
-   Languages: \* \*_JavaScript · TypeScript · Flow · JSX · JSON_ · _CSS · SCSS · Less_ · _HTML · Vue · Angular_ · _GraphQL · Markdown ·
    YAML_\*\*

## Fetch: npm

```bash
npm install --save-dev --save-exact prettier
# Create
.prettierrc.json | .yml | .yaml
# Add
```

## Library

-   [ ] IDE
        Plugin: [Prettier - IntelliJ IDEs Plugin | Marketplace (jetbrains.com)](https://plugins.jetbrains.com/plugin/10456-prettier)
-   [ ]
    Repo: [pre-commit/mirrors-prettier: mirror of the `prettier` npm package for pre-commit (github.com)](https://github.com/pre-commit/mirrors-prettier)
-   [ ] Source: https://github.com/prettier/prettier
-   [ ] Hook: [Pre-commit Hook · Prettier](https://prettier.io/docs/en/precommit.html)

#### Config

-   [ ] [Webstorm](https://www.jetbrains.com/help/webstorm/prettier.html))
    -   [ ] **Reformat with Prettier**action (\_Alt+Shift+Ctrl+P_on Windows and Linux)
    -   [ ] Open*Preferences / Settings | Languages & Frameworks | JavaScript | Prettier* : **On save**and/or**On
            ‘Reformat Code’**
    -   [ ] apply formatting to all*.js, .ts, .jsx*, and\_.tsx_files | [glob patterns](https://github.com/isaacs/node-glob)

#### Option

-   [ ] API

```bash
# Print Width
printWidth: <int>  # True | False
# Whitespace
proseWrap: "<always|never|preserve>"
htmlWhitespaceSensitivity: "<css|strict|ignore>"
endOfLine: "<lf|crlf|cr|auto>"
# Tab Width:
tabWidth: <int>  # True | False
useTabs: <bool>  # True | False
# Semi-Colon
semi: <bool>  # True | False
trailingComma: "<all|es5|none>"
# Single Quote
singleQuote: <bool>  # True | False
quoteProps: "<as-needed|consistent|preserve>"
# Brackes & Attributes
bracketSpacing: <bool>  # True | False
bracketSameLine: <bool>  # True | False
singleAttributePerLine: <bool> # True | False
# Programming
arrowParens: "<always|avoid>"
# Format N Parsing
rangeStart: <int>  # True | False
rangeEnd: <int>  # True | False
# Pragm
requirePragma: <bool> # True | False
insertPragma: <bool> # True | False
# Lang
embeddedLanguageFormatting: "<off|auto>" # "auto" "off"

```

### Config `.prettier.yaml`

-   [ ] Project Level
-   [ ] Node Module: `D:\Code\node_modules`
-   [ ] Package: `D:\Code\node_modules\prettier`

```yaml
# .prettierrc or .prettierrc.yaml
trailingComma: 'es5'
tabWidth: 4
semi: false
singleQuote: true
endOfLine: 'lf'
embeddedLanguageFormatting: 'auto'

# HTML
bracketSpacing: true
bracketSameLine: true
htmlWhitespaceSensitivity: 'css'
singleAttributePerLine: true

# Programming Language
arrowParens: 'avoid'

# Markdown Configuration
proseWrap: 'preserve'
```

## IDE

-   [ ] Configuration
    -   [ ] Automatic: Prettier (from closest node_modules) + closest **`.prettiterrc.*`**
    -   [ ] Manual: Target **`.prettiterrc.*`** for all modules by linking to specific prettier packages.
-   [ ] Run files: **` {**/_,_}.{html,css,js,ts,jsx,tsx,vue,astro} `\*\*
-   [ ] Run on
    -   [ ] Save
    -   [ ] **`CTRL + ALT + SHIFT + P`**
    -   [ ] Context Menu
    -   [ ] Specific Files [default]: **`CTRL + ALT + L`**

<details><summary>Screenshots</summary>
![[Pasted image 20230709091314.png]]

</details>

## Config

-   [ ] Create a` .pre-commit-config.yaml` in root of repository.
-   [ ] Commit `yaml` repository.
-   [ ] Prepare for run by adding hook's
    -   [ ]
        Repository: `- repo: https://github.com/pre-commit/mirrors-prettier`: [pre-commit/mirrors-prettier: mirror of the `prettier` npm package for pre-commit (github.com)](https://github.com/pre-commit/mirrors-prettier)
    -   [ ]
        Revision: `rev` : `3.0.0` [pre-commit/mirrors-prettier: mirror of the `prettier` npm package for pre-commit (github.com)](https://github.com/pre-commit/mirrors-prettier/tags)
        -   [ ] 3.0.0
        -   Select/Use the ref you want to point at
    -   [ ] Hooks:
        -   [ ] Id: `id prettier`
        -   [ ] `additional_dependencies`:
            -   `prettier@2.1.2`
            -   ` '@prettier/plugin-xml@0.12.0'
        -   [ ] types_or: `[html, css, javascript]`
        -   [ ] types:
        -   [ ] files:

```yaml
- repo: https://github.com/pre-commit/mirrors-prettier
  rev: '3.0.0' # Use the sha / tag you want to point at
  hooks:
      - id: prettier
```

## Install

```bash
npm install --save-dev --save-exact prettier
# Create
.prettierrc.json
```

## Run

```bash
# Formats everything
npx prettier . --write
# Formta a target
prettier --write app/
# Format a File
prettier --write "app/**/*.test.js"
# Checks already formated
npx prettier . --check
```
