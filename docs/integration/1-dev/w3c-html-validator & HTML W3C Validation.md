**META**: 23-07-13.17:13 | Last Edited By:

## Workflow | Issue

> .

-   [ ] CONFIG:
    -   [ ] Build | Integrate | Test | Quality | Config | Deploy | Release
-   [ ] GitHub Issue(s) Created?
    -   [ ] FLOW: Workflow | Process | Outline
        -   [ ] #Issue #12
    -   [ ] LINT: Report
        -   [ ] #Issue
-   [ ] FLOW
    -   [ ] Config .dotfile
        -   [ ] `   .json|yml|js`
    -   [ ] Local Script
        -   [ ] Bash?
    -   [ ] IDE Configuration
        -   [ ] Run Configuration?
    -   [ ] Pre-Commit
        -   [ ]
    -   [ ] CI Workflow
        -   [ ] YML
        -   [ ] Runner

# Package:

**`Intent | Purpose: `**

```ruby
>> **w3c-html-validator** takes HTML files and returns detailed validation results. 
>> The reporter produces formatted output indended for use in build scripts and test suites.
```

![[Pasted image 20230713172443.png]]

-   Related Config
    -   [[CONFIG - {{}}]]
    -   .

## Package | Library Source

> .

-   [ ] PIP
-   [ ] NPM
-   [ ] Unpkg
-   [ ] JsDeliver

**Link:** **`URL`**

```bash
github.com/center-key/w3c-html-validator
```

### Source

```bash
www.npmjs.com/package/w3c-html-validator
```

### Install

```bash
npm install --save-dev w3c-html-validator
```

### Runs as a CLI

```
html-validator docs/*.html flyer.html
```

### Config: Package.json Scripts

```json
"scripts": {
    "validate": "html-validator docs/*.html flyer.html --exclude=build,tmp --delay=200",
    "one-folder": "html-validator docs --exclude=build,tmp --delay=200",
    "all": "html-validator --quiet --exclude=build,tmp --delay=200",
    "continue": "html-validator --quiet --continue --exclude=build,tmp --delay=200"
   },
```

### CLI Flags

```shell
`--continue`: Report messages but do not throw an error if validation failed. N/A
`--delay`:  Debounce pause in milliseconds between each file validation. **number**
`--exclude`: Comma separated list of strings to match in paths to skip. **string**
`--ignore`: Skip messages containing a string or matching a RegEx. **string**
`--note`:   Place to add a comment only for humans. **string**
`--quiet`:  Suppress messages for successful validations. N/A
`--trim`:   Truncate validation messages to not exceed a maximum length. **number**
```

**SCRIPT | RUN** `Script File`: - File Name: **` .sh`**

```bash
#!/bin/bash
html-validator *.html --exclude=build,tmp --delay=200 --quite --continue
```

**CONFIGURATION | RUN** `Script File`
Either

-   Define in `package.json`
-   Use the Run Config control

```json
"scripts": {
    "validate": "html-validator docs/*.html flyer.html --exclude=build,tmp --delay=200",
    "one-folder": "html-validator docs --exclude=build,tmp --delay=200",
    "all": "html-validator --quiet --exclude=build,tmp --delay=200",
    "continue": "html-validator --quiet --continue --exclude=build,tmp --delay=200"
   },
```

OR

-   Name: **`validate`** | **`one-folder`** | **`all`** | **`continue`**
-   Allow Multiple: N
-   Store as File: N - in package.json
-   Package.json: `D:\Code\Code Institute\dash-and-do-github\package.json`
-   Command: `run`
-   Scripts: `all`
-   Arguments:
-   Node: Node: `C:\Programs Files\node.js\node.exe` 20.3.0
-   Node Options:
-   Package manager: `C:\Program Files\node.js\node.exe`
-   Environments:
-   Before Launch:

```
Command: run
Script:
Arguement:
Node Opt: -
Environ: -
```

**NPM**: `package.json`

```json
"scripts": {
    "validate": "html-validator docs/*.html flyer.html --exclude=build,tmp --delay=200",
    "one-folder": "html-validator docs --exclude=build,tmp --delay=200",
    "all": "html-validator --quiet --exclude=build,tmp --delay=200",
    "continue": "html-validator --quiet --continue --exclude=build,tmp --delay=200"
   },
```

## **Pre-Commit**: ``

```yml
repos:
    - repo: local
      hooks:
          - id: validate-html-wc3
            name: Validate HTML with WC3
            entry: ./scripts/1-dev/validate-html-wc3.sh
            language: system
            types: [file]
            exclude: build,tmp
```

### Options

-   Package: https://www.npmjs.com/package/w3c-html-validator
-

GitHub: [center-key/w3c-html-validator: 🚦 A package for testing HTML files or URLs against the W3C validator (github.com)](https://github.com/center-key/w3c-html-validator)

-   Perplexity: Create local commit hook https://www.perplexity.ai/search/7f0c138a-2248-49c6-9590-1841ecee9cc0?s=c

## Final

> FLOW

### Steps

1. [x] Install NPM Package.
2. [ ] Run manually as a CLI
    1. [ ] Run against URL
    2. [ ] Run against path
    3. [ ] Run against the file
3. Install in Package.json
4. Use WebStorm/PyCharm run controls to integrate scripts into the IDE
5. Pre-commit
    1. [ ] Defined the bash script for a local pre-commit hook
    2. [ ] Use the Pre-commit local config.
6. .
7. .
8. .

### Repository

```dirtree

- /dash-and-do-github
	- /.github
		- /workflows
			- .yml
	- /docs
		- /integration
			- /1-dev
				- w3c-html-validator.md
	- /scripts
		- /1-dev
			- validate-html-wc3.sh
	- .pre-commit-configuration.yml
```

## Sources

-   .
-   .
-   .

---

> .

---
