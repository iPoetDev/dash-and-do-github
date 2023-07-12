## Workflow | Issue

- [ ] CONFIG:
    - [ ]  Build | Integrate | Test | Quality | Config | Deploy
- [ ] GitHub Issue(s) Created?
    - [ ] FLOW: Workflow | Process | Outline
        - [ ] 
          #Issue: [FLOW :: Code Quality Assurance (github.com)](https://github.com/iPoetDev/dash-and-do-github/issues/12)
        - [ ] #Issue:
    - [ ] LINT: Report
        - [ ] #Issue
- [ ] FLOW
    - [x] Config File
    - [ ] Local Script
        - [ ] Bash?
    - [x] IDE Configuration
        - [x] On Save
    - [ ] Pre-Commit
    - [ ] CI Workflow
- [ ] IDE
    - [x] Pycharm
    - [x] WebStorm
        - [ ] Setup: [WebStorm Setup · Prettier](https://prettier.io/docs/en/webstorm.html)
        - [ ] Watch: [Watching For Changes · Prettier](https://prettier.io/docs/en/watching-files.html)

# Package:

**`Intent | Purpose:`**

```ruby
>> Prettier is the only “style guide” that is fully automatic.
>> Prettier intendes to stop all the on-going debates over styles.
>> Building and enforcing a style guide
>> Writing code
>> Easy to adopt
>> Clean up an existing codebas
>> Prettier for formatting
```

- Related Config
    - [[CONFIG - {{}}]]
    - .

## Package | Library Source

- [ ] PIP
- [x] NPM
- [ ] Unpkg
- [ ] JsDeliver

**`ÙRL`**

```bash
https://prettier.io/
```

### Source

- [Install · Prettier](https://prettier.io/docs/en/install.html)

```bash
https://prettier.io/
```

#### Dependencies

- ESLint, install[eslint-config-prettier](https://github.com/prettier/eslint-config-prettier#installation)to make ESLint
  and Prettier play nice
- Stylelint:[stylelint-config-prettier](https://github.com/prettier/stylelint-config-prettier)
  ``

```bash

```

```bash:script


```

### Install

-[Install · Prettier](https://prettier.io/docs/en/install.html)

```bash
npm install --save-dev --save-exact prettier
'Create'
echo {}> .prettierrc.json
echo {}> .prettierignire
```

### Config

[Configuration File · Prettier](https://prettier.io/docs/en/configuration.html)

IGNORE `.prettierignore`[.prettierignore](https://prettier.io/docs/en/ignore.html)

```ini
# Ignore artifacts: 
build
coverage
```

```json
"devDependencies": {
"prettier": "^3.0.0",
}
```

**CONF: `.prettierrc.yaml`**

```yml
# .prettierrc or .prettierrc.yaml  
trailingComma             : "es5"
tabWidth                  : 4
semi                      : false
singleQuote               : true
endOfLine                 : "lf"
embeddedLanguageFormatting: "auto"

# HTML  
bracketSpacing            : true
bracketSameLine           : true
htmlWhitespaceSensitivity : "css"
singleAttributePerLine    : true

# Programming Language  
arrowParens               : "avoid"

# Markdown Configuration  
proseWrap                 : "preserve"
```

#### Local Pre-Commit | ~~Requirements | Proc

EXECUTE `npx | pipx | `

```bash
npx prettier . --write
npx prettier . --write app/
npx prettier . --write {target}/file.js
npx prettier . --write npx prettier . --write #glob

# CI
npx prettier . --check
```

SCRIPT | RUN `Script File`: - File Name: **``  .sh ``**

```bash
#!/bin/bash 
npx prettier . --write
```

CONFIGURATION | RUN `Script File`

- Name:
- Allow Multiple: N | Y
- Store as File: N | Y
- Package.json: `D:\Code\Code Institute\dash-and-do-github\package.json`
- Command:
- Scripts:
- Arguments:
- Node: Node: `C:\Programs Files\node.js\node.exe` 20.3.0
- Node Options:
- Package manager: `C:\Program Files\node.js\node.exe`
- Environments:
- Before Launch:

```
Command: run
Script:
Arguement:
Node Opt: 
Environ:
```

**PYTHON**: **`Requirements | Requirements-dev | Requirements-test`**

```text

```

**OnChange: ``Watch for changes`**

```json
{
  "scripts": {
    "prettier-watch": "onchange \"**/*\" -- prettier --write --ignore-unknown {{changed}}"
  }
}
```

**PRE-COMMIT** **``**

```yml
repos:
  -
    repo: https://github.com/pre-commit/mirrors-prettier
  -
    rev: "" # Use the sha or tag you want to point at 
  -
    hooks:
  -
    id: prettier
```

### Options

[Options · Prettier](https://prettier.io/docs/en/options.html)

- Docs: [Install · Prettier](https://prettier.io/docs/en/install.html)
- Package: [prettier - npm (npmjs.com)](https://www.npmjs.com/package/prettier)
- GitHub: [github.com/prettier/prettier](https://github.com/prettier/prettier)
- Perplexity:

Options that are easier to motivate include:

- `--trailing-comma es5`lets you use trailing commas in most environments without having to transpile (trailing function
  commas were added in ES2017).
- `--prose-wrap`is important to support all quirky Markdown renderers in the wild.
- `--html-whitespace-sensitivity`is needed due to the unfortunate whitespace rules of HTML.
- `--end-of-line`makes it easier for teams to keep CRLFs out of their git repositories.
- `--quote-props`is important for advanced usage of the Google Closure Compiler.
- `--arrow-parens`,
- `--jsx-single-quote`,- `--bracket-same-line`and`--no-bracket-spacing`

## Final

> FLOW

### Steps

- [x] Install an exact version of Prettier locally in your project. This makes sure that everyone in the project gets
  the exact same version of Prettier. Even a patch release of Prettier can result in slightly different formatting, so
  you wouldn’t want different team members using different versions and formatting each other’s changes back and forth.
- [x] Add a`.prettierrc.json`to let your editor know that you are using Prettier.
- [x] Add a`.prettierignore`to let your editor know which files_not_to touch, as well as for being able to
  run`prettier --write .`to format the entire project (without mangling files you don’t want, or choking on generated
  files).
- [ ] Run`prettier --check .`in CI to make sure that your project stays formatted.
- [x] Run Prettier from your editor for the best experience.
- [ ] Use[eslint-config-prettier](https://github.com/prettier/eslint-config-prettier)to make Prettier and ESLint play
  nice together.
- [x] Set up a pre-commit hook to make sure that every commit is formatted.

### Repository

```dirtree

- /dash-and-do-github
	- /.github
		- 🚫/workflows
			- .yml
	- /docs
		- /integration
			- /1-dev
				- prettier.md
	- /scripts
		- /1-dev
			- prettier-write.sh
			- prettier-check.sh
	- .pre-commit-configuration.yml
	- .prettierrc
	- .prettierignore
```



