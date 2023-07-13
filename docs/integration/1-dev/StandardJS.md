**META**: 23-07-13.13:36 | Last Edited By:
![](https://cdn.rawgit.com/standard/standard/master/sticker.svg)

## Workflow | Issue

> .

- [x] CONFIG:
    - [x] Build | Integrate | Test | Quality | Security | Config |
- [x] GitHub Issue(s) Created?
    - [x] FLOW: Workflow | Process | Outline
        - [x] #Issue
          #12 [FLOW :: Code Quality Assurance (github.com)](https://github.com/iPoetDev/dash-and-do-github/issues/12)
        - [x] #Flow: Commit-Flow
        - [x] #Flow Code Quality
    - [ ] LINT: Report
        - [ ] #Issue
- [ ] FLOW
    - [x] Config .dotfile
        - [x] see Eslint ` eslintrc.js`
    - [ ] Local Script
        - [ ] Bash?
            - [ ] Develop
            - [x]  Runs `>> standard --fix` from CLI
            - [x] Locally: `>> npx standard --fix`
        - [ ] Package.json
            - [ ] Test scripts?
    - [x] IDE Configuration
        - [x] Run Configuration?
    - [ ] Pre-Commit
        - [ ]  Local
        - [x] Simple
        - [x] Advanced
    - [ ] CI Workflow
        - [ ] YML
        - [ ] Runner

# Package:

## Install and runs as terminal cli as standalone

**`Intent | Purpose:`** The beauty of JavaScript Standard Style is that it's simple. No one wants to maintain multiple
hundred-line style configuration files for every module/project they work on.

At the end of the day you have to 'just pick something', and that's the whole philosophy of`standard`-- its a bunch of
sensible 'just pick something' opinions. Avoid debates/bikeshedding.

```ruby
>> JavaScript style guide, linter, and formatter
>> Runs as a CLI from command line
>> The importance of code clarity and community conventions ranks higher than personal style
```

This module saves you (and others!) time in three ways:

- **No configuration.**The easiest way to enforce code quality in your project. No decisions to make. No`.eslintrc`files
  to manage. It just works.
- **Automatically format code.**Just run`standard --fix`and say goodbye to messy or inconsistent code.
- **Catch style issues & programmer errors early.**Save precious code review time by eliminating back-and-forth between
  reviewer & contributor.

#### Talk

["Write Perfect Code with Standard and ESLint"](https://www.youtube.com/watch?v=kuHfMw8j4xk). In this talk, you'll learn
about linting, when to use`standard`versus`eslint`, and how`prettier`compares to`standard`.

#### Related

Give it a try by running`npx standard --fix`right now!

- Related Config
    - [[CONFIG - {{}}]]
- [[eslint]]

## Package | Library Source

> .

- [x] NPM

**Link:** **`URL`**

```bash
https://standardjs.com/
```

### Source

```bash
https://www.npmjs.com/package/standard
```

#### Dependencies

- Eslint Sharable Configs Standard
- some important packages in the`standard`ecosystem:
    - **[standard](https://github.com/standard/standard)**- this repo
        - **[standard-engine](https://github.com/standard/standard-engine)**- cli engine for arbitrary eslint rules
        - **[eslint-config-standard](https://github.com/standard/eslint-config-standard)**- eslint rules for standard
        - **[eslint-config-standard-jsx](https://github.com/standard/eslint-config-standard-jsx)**- eslint rules for
          standard (JSX)
        - **[eslint](https://github.com/eslint/eslint)**- the linter that powers standard
    - **[snazzy](https://github.com/standard/snazzy)**- pretty terminal output for standard
    - **[standard-www](https://github.com/standard/standard-www)**- code
      for[https://standardjs.com](https://standardjs.com/)
    - **[semistandard](https://github.com/standard/semistandard)**- standard, with semicolons (if you must)
    - **[standardx](https://github.com/standard/standardx)**- standard, with custom tweaks

```bash

```

### Install

```bash
npm install standard --global
npm install standard --save-dev
```

### Run

```json
standard
npx standard
```

### IDE

![[IDE Inspections StandardJs.png]]

#### WebStorm Custom Config

1.
    1. Close your IDE.
2. [Figure out where your configuration lives](https://www.jetbrains.com/help/phpstorm/2016.1/directories-used-by-phpstorm-to-store-settings-caches-plugins-and-logs.html?origin=old_help#d66583e60)(
   _IDE Settings_section)
3. Navigate to`your-config-dir/codestyles`. If this directory doesn't exist, create it in the WebStorm config settings
   directory
4. Create a`Standard.xml`file:
    ```xml
      <code_scheme name="Standard">
        <JSCodeStyleSettings>
          <option name="USE_SEMICOLON_AFTER_STATEMENT" value="false" />
          <option name="USE_DOUBLE_QUOTES" value="false" />
          <option name="SPACES_WITHIN_IMPORTS" value="true" />
        </JSCodeStyleSettings>
        <codeStyleSettings language="JavaScript">
          <option name="KEEP_BLANK_LINES_IN_CODE" value="1" />
          <option name="SPACE_BEFORE_METHOD_PARENTHESES" value="true" />
          <option name="KEEP_SIMPLE_BLOCKS_IN_ONE_LINE" value="true" />
          <option name="KEEP_SIMPLE_METHODS_IN_ONE_LINE" value="true" />
          <indentOptions>
            <option name="INDENT_SIZE" value="2" />
            <option name="CONTINUATION_INDENT_SIZE" value="2" />
            <option name="TAB_SIZE" value="2" />
          </indentOptions>
        </codeStyleSettings>
      </code_scheme>
    ```
5. You may install dependencies and config globally or locally and with support of ES7 or without it
    - **Local**install:
        - `npm install --save-dev eslint-config-standard eslint-config-standard-jsx eslint-plugin-promise eslint-plugin-react`
        - `echo '{"extends": ["standard", "standard-jsx"]}' > .eslintrc`

- **Global**install:
    - `npm install --global eslint-config-standard eslint-config-standard-jsx eslint-plugin-promise eslint-plugin-react`
    - `echo '{"extends": ["standard", "standard-jsx"]}' > ~/.eslintrc`
      Be aware: The second command above will overwrite an existing`.eslintrc`if one exists.
      If you choose global install, the first command may require you to use`sudo`. If it does require sudo, that means
      you
      do not have permission to write to the directories that npm uses to store global packages.`Standard`will work, but
      if
      you would like to fix it,[read this article](https://docs.npmjs.com/getting-started/fixing-npm-permissions).

6. Start up the IDE and open a_Settings_/_Preferences_screen (choose between project and default settings accordingly to
   your preference)
7. Under`Editor > Code Style > JavaScript`change`Scheme`to`Standard`
8. Under`Editor > Code Style > HTML`just select`Other`, in`Spaces`setting, check`In empty tag`
9. Under`Editor > Inspections > JavaScript > Code style issues`untick`Unterminated statement`
10. Under`Languages & Frameworks > JavaScript > Code Quality Tools > ESLint`just select`Enable`. If you didn't
    install`ESLint`before, and you don't have it in your dependencies - that's all. If you do - be sure to
    use`ESLint package`of the same version as the current version of`standard`is using. Or just remove your old one -
    you probably won't need it any more

### Command Line

```shell
>> 🦄  standard --help
standard - Use JavaScript Standard Style (https://standardjs.com)

Usage:
    standard <flags> [FILES...]

    If FILES is omitted, all JavaScript source files (*.js, *.jsx, *.mjs, *.cjs)
    in the current working directory are checked, recursively.

        --fix       Automatically fix problems
        --version   Show current version
    -h, --help      Show usage information

Flags (advanced):
        --stdin     Read file text from stdin
        --ext       Specify JavaScript file extensions
        --global    Declare global variable
        --plugin    Use custom eslint plugin
        --env       Use custom eslint environment
        --parser    Use custom js parser (e.g. babel-eslint)

```

#### Local | Pre-Commit Requirements | Proc
---
**SCRIPT | RUN** `Script File`: - File Name: **``  .sh ``**

```bash
#!/bin/bash 
npx standard --fix .
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
`npm test` checks standard automatically

```json
  
  "name": "my-cool-package",
  "devDependencies": {
    "standard": "*"
  },
  "scripts": {
    "test": "standard && node my-tests.js"
  }
}
```

#### Commit Hook

```bash
#!/bin/bash # Ensure all JavaScript files staged for commit pass standard code style 
function xargs-r() { # Portable version of "xargs -r". The -r flag is a GNU extension that # prevents xargs from running if there are no input files. 
if IFS= read -r -d $'\n' path; then 
echo "$path" | cat - | xargs "$@" 
fi 
} 

git diff --name-only --cached --relative | grep '\.jsx\?$' | sed 's/[^[:alnum:]]/\\&/g' | xargs-r -E '' -t standard 
if [[ $? -ne 0 ]]; then
    echo 'JavaScript Standard Style errors were detected. Aborting commit.' exit 1 
    fi
```

**Pre-Commit**: ``

```yml
# simply add `standard` to their `.pre-commit-config.yaml`
- repo: https://github.com/standard/standard 
  rev: master 
  hooks: 
  - id: standard
# more advanced styling configurations
- repo: https://github.com/pre-commit/mirrors-eslint 
  rev: master 
  hooks: - id: eslint
    files: \.[jt]sx?$ # *.js, *.jsx, *.ts and *.tsx 
    types: [file] 
    additional_dependencies: 
      - eslint@latest 
      - eslint-config-standard@latest # and whatever other plugins...
```

#### Output

-  [ ] Snazzy https://www.npmjs.com/package/snazzy

```
$ npm install snazzy
$ standard | snazzy
```

### Sources

- Web + Docs: https://standardjs.com/
- Package: https://www.npmjs.com/package/standard
- GitHub: https://github.com/standard/standard
- Perplexity:

## Final

> FLOW

### Steps

1. [x] . Install Standard (as standalone)
2. [x] . Additionally configure ESlist with sharable config
3. [x] . Configure IDE to use Standard via ESlint on save
    1. [ ] .Additionally optional WebStorm manual code style
4. [ ] .Understand the Command Line options
5. [ ]  Create a Bash script to
    1. [ ] Detect
    2. [ ] Fix
    3. [ ] Format output
6. [x]  Decide the Commit Hooks
    1. [ ] Define your own
    2. [x] Use Pre-commit
7. [x] Pre-commit
    1. [x] Simple
    2. [x] Advanced
8. [ ]  Handle the Output
9. [ ] Decide to automate

### CLI Checks → Maybe Automate

```shell
standard
standard --fix
standard --fix | stylish

```

### Repository

```dirtree

- /dash-and-do-github
	- /.github
		- /workflows
			- 
	- /docs
		- /integration
			- /1-dev
				- eslint.md
				- standardjs.md
	- /scripts
		- /1-dev
			- .sh
	- eslintrc.js
```

---
> .
---