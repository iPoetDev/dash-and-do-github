**META**: 23-07-12.21:35 | Last Edited By:

## Workflow | Issue
> .

- [x] CONFIG:
    - [x] Build | Integrate | Test | Quality | Security | Config 
- [ ] GitHub Issue(s) Created?
    - [ ] FLOW: Workflow | Process | Outline
        - [ ] #Issue #12 [FLOW :: Code Quality Assurance](https://github.com/iPoetDev/dash-and-do-github/issues/12)
        - [ ] #Flow: Commit-Flow (pre-commits)
    - [ ] LINT: Report
        - [ ] #Issue
- [ ] FLOW
    - [x] Config .dotfile
        - [x] ` .eslintrc.js`
        - [x] Only Add Shareabe Configs
        - [x] Keep to a minimum, lowest maintence
    - [x] Local Script
        - [x] Bash?
    - [x] IDE Configuration
        - [ ] Run Configuration?
    - [x] Pre-Commit
        - [ ] Installed?
        - [ ] Use as a local runner?
    - [ ] CI Workflow
        - [ ] YML
        - [ ] Runner

# Package:

**`Intent | Purpose:`**

```ruby
>> Statically analsyses code and is built in to the IDEs that author uses
>> Write high quality consistent JavaScript
>> Catch common issues early and often
>> Fix problems automatically
>> High level of configuration
>> High level of extensibility so to enforce custom conventions
```

- Related Config
    - Template [[CONFIG - {{}}]]:
    - Associated Package: [[StandardJS]]

## Package | Library Source
> .

- [x] NPM
- [ ] **Link:** **[`URL`](https://eslint.org/)**: [Find and fix problems in your JavaScript code - ESLint - Pluggable JavaScript Linter](https://eslint.org/)

```bash
[Find and fix problems in your JavaScript code - ESLint - Pluggable JavaScript Linter](https://eslint.org/)

https://eslint.org/

```

### Source

```bash
https://github.com/eslint/eslint
```

#### Dependencies

Only focus on 
- [ ] Sharable Configs
- [ ] Plugins as strictly necessary, as they emerge

-  See below **Depends on:** ``
    - Sharable Configs
        - *eslint-Config-Defaults: [eslint-config-defaults - npm (npmjs.com)](https://www.npmjs.com/package/eslint-config-defaults)
        - *eslint-Config-Prettier: [- eslint-config-prettier - npm (npmjs.com)](https://www.npmjs.com/package/eslint-config-prettier)
        - *eslint-Config-SemiStandard: - [eslint-config-semistandard - npm (npmjs.com)](https://www.npmjs.com/package/eslint-config-semistandard)
        - *eslint-Config-Standard: - [eslint-config-standard - npm (npmjs.com)](https://www.npmjs.com/package/eslint-config-standard)

### Install

#### Currently
```dirtree

- /node_modules
    - /...
    - /@eslint
    - /@eslint-community
    - /eslint-config-defaults
    - /eslint-config-prettier
    - /eslint-config-semistandard
    - /eslint-config-standard
    - /eslint-import-resolver-mode
    - /eslint-module-utils
    - /eslint-plugin-es
    - /eslint-plugin-import
    - /eslint-plugin-promise
    - /eslint-plugin-react
    - /eslint-plugin-security
    - /eslint-plugin-unicorn
    - /eslint-scope
    - /eslint-utils
    - /eslint-visitor-keys
```

```bash

```

### Config

- [ ] Use only Sharable Confits
- [ ] Properties
    - [ ] `root`: Scope to checks to root of project
    - [ ] `extends`: include sharable configs, inc plugin dependencies
    - [ ] `files`
    - [ ] `ignores`
    - [ ] `langauageOptions`
        - [ ] `ecmaVersion`
        - [ ] `sourceType`
        - [ ] `globals`
        - [ ] `parser`
        - [ ] `parserOptions`
    - [ ] `linterOptions` .
        - [ ] ` noInlineConfig` 
        - [ ] ` reportUnusedDisableDirecttives` 
    - [ ] `processor` 
    - [ ] `plugins` .
    - [ ] `rules` .
    - [ ] `settings` .
    - [ ] Rules
    - [ ] Formatters Reference

```shell

```

```js
module.exports = {  
    root: true,  
    extends: ['standard', 'prettier'],  
}
```

#### Command Line
[Command Line Interface Reference - ESLint - Pluggable JavaScript Linter](https://eslint.org/docs/latest/use/command-line-interface)
```json
🦄  eslint -h
eslint [options] file.js [file.js] [dir]

Basic configuration:
  --no-eslintrc                   Disable use of configuration from .eslintrc.*
  -c, --config path::String       Use this configuration, overriding .eslintrc.* config options if present
  --env [String]                  Specify environments
  --ext [String]                  Specify JavaScript file extensions
  --global [String]               Define global variables
  --parser String                 Specify the parser to be used
  --parser-options Object         Specify parser options
  --resolve-plugins-relative-to path::String  A folder where plugins should be resolved from, CWD by default

Specify Rules and Plugins:
  --plugin [String]               Specify plugins
  --rule Object                   Specify rules
  --rulesdir [path::String]       Load additional rules from this directory. Deprecated: Use rules from plugins

Fix Problems:
  --fix                           Automatically fix problems
  --fix-dry-run                   Automatically fix problems without saving the changes to the file system
  --fix-type Array                Specify the types of fixes to apply (directive, problem, suggestion, layout)

Ignore Files:
  --ignore-path path::String      Specify path of ignore file
  --no-ignore                     Disable use of ignore files and patterns
  --ignore-pattern [String]       Pattern of files to ignore (in addition to those in .eslintignore)

Use stdin:
  --stdin                         Lint code provided on <STDIN> - default: false
  --stdin-filename String         Specify filename to process STDIN as

Handle Warnings:
  --quiet                         Report errors only - default: false
  --max-warnings Int              Number of warnings to trigger nonzero exit code - default: -1

Output:
  -o, --output-file path::String  Specify file to write report to
  -f, --format String             Use a specific output format - default: stylish
  --color, --no-color             Force enabling/disabling of color

Inline configuration comments:
  --no-inline-config              Prevent comments from changing config or rules
  --report-unused-disable-directives  Adds reported errors for unused eslint-disable directives

Caching:
  --cache                         Only check changed files - default: false
  --cache-file path::String       Path to the cache file. Deprecated: use --cache-location - default: .eslintcache
  --cache-location path::String   Path to the cache file or directory
  --cache-strategy String         Strategy to use for detecting changed files in the cache - either: metadata or content - default: metadata

Miscellaneous:
  --init                          Run config initialization wizard - default: false
  --env-info                      Output execution environment information - default: false
  --no-error-on-unmatched-pattern  Prevent errors when pattern is unmatched
  --exit-on-fatal-error           Exit with exit code 2 in case of fatal error - default: false
  --debug                         Output debugging information
  -h, --help                      Show help
  -v, --version                   Output the version number
  --print-config path::String     Print the configuration for the given file

```

#### Formatters
[Formatters Reference - ESLint - Pluggable JavaScript Linter](https://eslint.org/docs/latest/use/formatters/)
- [ ] - [stylish](https://eslint.org/docs/latest/use/formatters/#stylish)
```shell
/var/lib/jenkins/workspace/Releases/eslint Release/eslint/fullOfProblems.js
  1:10  error    'addOne' is defined but never used            no-unused-vars
  2:9   error    Use the isNaN function to compare with NaN    use-isnan
  3:16  error    Unexpected space before unary operator '++'   space-unary-ops
  3:20  warning  Missing semicolon                             semi
  4:12  warning  Unnecessary 'else' after 'return'             no-else-return
  5:1   warning  Expected indentation of 8 spaces but found 6  indent
  5:7   error    Function 'addOne' expected a return value     consistent-return
  5:13  warning  Missing semicolon                             semi
  7:2   error    Unnecessary semicolon                         no-extra-semi

✖ 9 problems (5 errors, 4 warnings)
  2 errors and 4 warnings potentially fixable with the `--fix` option.
```

#### IDE
![[IDE Inspections StandardJs.png]]

- IntelliJ IDEA, WebStorm, PhpStorm, PyCharm, RubyMine, and other JetBrains IDEs: [How to use ESLint](https://www.jetbrains.com/help/webstorm/eslint.html)

#### File Watcher

[eslint-watch - npm (npmjs.com)](https://www.npmjs.com/package/eslint-watch)

#### Local | Pre-Commit Requirements | Proc
---
**PYTHON**: **`Requirements.txt | Requirements-dev.txt | Requirements-test.txt`**
```text

```

**SCRIPT | RUN** `Script File`: - File Name: **``  .sh ``**
```bash
#!/bin/bash 
npx eslint . --fix --formatter stylish
```

**CONFIGURATION | RUN** `Script File`

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

**NPM**: `package.json`

```json
  
"devDependencies": {  
    "eslint": "^8.44.0",  
    "eslint-config-defaults": "^9.0.0",  
    "eslint-config-prettier": "^8.8.0",  
    "eslint-config-semistandard": "^17.0.0",  
    "eslint-config-standard": "^17.1.0",  
    "eslint-import-resolver-node": "^0.3.7",  
    "eslint-module-utils": "^2.8.0",  
    "eslint-plugin-import": "^2.27.5",  
    "eslint-plugin-security": "^1.7.1",  
    "eslint-scope": "^7.2.0",  
    "eslint-utils": "^3.0.0",
    "standard": "^17.1.0",
}

```

##### Pre-Commit Hook
[eslint pre-commit hook (Example) (coderwall.com)](https://coderwall.com/p/zq8jlq/eslint-pre-commit-hook)
```bash
#!/bin/zsh

function lintit () {
  OUTPUT=$(git diff --name-only | grep -E '(.js)$')
  a=("${(f)OUTPUT}")
  e=$(eslint -c eslint.json $a)
  echo $e
  if [[ "$e" != *"0 problems"* ]]; then
    echo "ERROR: Check eslint hints."
    exit 1 # reject
  fi
}
lintit
```

**Pre-Commit**: ``
Mirror : [github.com/pre-commit/mirrors-eslint](https://github.com/pre-commit/mirrors-eslint)
Tags: [Tags · pre-commit/mirrors-eslint (github.com)](https://github.com/pre-commit/mirrors-eslint/tags)
Use @latest for dependencies
```yml
-   repo: https://github.com/pre-commit/mirrors-eslint
    rev: v8.44.0  # Use the sha / tag you want to point at
    hooks:
    -   id: eslint
        # using plugins with `eslint` you'll need to declare them
        additional_dependencies:
        -  eslint@latest
        # -   eslint-config-semistandardd@latest
        -   eslint-config-standardd@latest
        -   eslint-config-prettier@latest
        # use eslint on TypeScript codebases
        files: \.[jt]sx?$  # *.js, *.jsx, *.ts and *.tsx
        types: [file]
```

###  Sources

- Docs: [Docs (eslint.org)](https://eslint.org/docs/latest/)
- Org: [Eslint:  Organisation: Find and fix problems in your JavaScript code. (github.com)](https://github.com/eslint)
- GitHub: [eslint/eslint: Find and fix problems in your JavaScript code. (github.com)](https://github.com/eslint/eslint)
- Awesome: [dustinspecker/awesome-eslint: A list of awesome ESLint plugins, configs, etc. (github.com)](https://github.com/dustinspecker/awesome-eslint)
- Perplexity:

## Final

> FLOW

### Steps

1. [x] . Install Eslint
2. [x] Update Package.json for latest tags/versions
3. [x]  Install Sharable Configs
4. [ ] Only install plugins as necessary
5. [x] . Configiure `.eslintrc.js` with `extends` and sharable configu
    1. [x] Standard
    2. [x] Prettier
6. [ ]  Alternative Configs
    1. [ ] Defaults etc
    2. [ ] Semistandard
7. [x] Not installing AirBnB or Google style guides 
8. [x] No custom rules
9. [x] IDE Configuration
    1. [x] Detect and enable Standard for Project in Inspections, using ESlint
10. [ ] .
11. [ ] .

### Repository

```dirtree

- /dash-and-do-github
	- /.github
		- /workflows
			- superlinter.yml        # Depends on eslintrc.js
	- /docs
		- /integration
			- /1-dev
				- eslint.md
				- standardjs.md
	- /scripts
		- /1-dev
			- .sh
	- .eslintrc.js
	- package.json
	- package.lock.json
```


---
> .
---