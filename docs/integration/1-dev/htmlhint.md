**META**: 23-07-12.21:47 | Last Edited By:

![HTMLHint](https://htmlhint.com/img/htmlhint.png)

## Workflow | Issue

> .

- [ ] CONFIG:
    - [ ] Agile | Plan | Design | Architect | System | Data | Build | Integrate | Test | Quality | Security | Config |
      Deploy | Release
- [ ] GitHub Issue(s) Created?
    - [ ] FLOW: Workflow | Process | Outline
        - [ ] #Issue #12
    - [ ] LINT: Report
        - [ ] #Issue
- [ ] FLOW
    - [ ] Config .dotfile
        - [ ] `   .json|yml|js`
    - [ ] Local Script
        - [ ] Bash?
    - [ ] IDE Configuration
        - [ ] Run Configuration?
    - [ ] Pre-Commit
        - [ ] 
    - [ ] CI Workflow
        - [ ] YML
        - [ ] Runner

# Package:

**`Intent | Purpose:`**

```ruby
>> Static code analysis tool you need for your HTML
>> 
```

- Related Config
    - [[CONFIG - {{}}]]
    - .

## Package | Library Source

> .

- [x] NPM

**Link:** **`URL`**

```bash
https://htmlhint.com/
```

### Install

**LOCAL**

```bash
$ npm install htmlhint --save-dev
```

**GLOBAL**

```bash
$ npm install htmlhint -g
```

### Run

**LOCAL**

```bash
./node_modules/.bin/htmlhint www/index.html
./node_modules/.bin/htmlhint www/**/*.html
```

**GLOBAL**

```bash
# 
$ htmlhint www/index.html
$ htmlhint www/**/*.html
# URL
$ htmlhint https://htmlhint.com/
```

### Options

For Scripts: [Options | HTMLHint](https://htmlhint.com/docs/user-guide/usage/options)

```
```

### CLI

```bash
# Force enabling/disabling of color
`--color, --no-color`
# List all rules
`--list, -l`
# Set all rules
`--rules, -r`
# Load custom rules from file/folder
`--rulesdir, -R`
```

### Config

#### Custom Config | Rules | Inline

```bash
htmlhint --config htmlhint.conf index.html
htmlhint --rules tag-pair,id-class-value=underline index.html

```

**INLINE**

```html
<!-- htmlhint tag-pair,id-class-value:underline -->  
<html>  
<head>...</head>  
<body>...</body>  
</html>
```

#### Config | Rule File: `.htmlhintrc`

```json
{  
    "doctype-first": true,  
    "doctype-html5": true,  
    "html-lang-require": true,  
    "head-script-disabled": false,  
    "style-disabled": false,  
    "title-require": true,  
      
    "attr-lowercase": true,  
    "attr-no-duplication": true,  
    "attr-no-unnecessary-whitespace": true,  
    "attr-unsafe-chars": true,  
    "attr-value-double-quotes": true,  
    "attr-value-not-empty": false,  
    "attr-sorted": true,  
    "alt-require": true,  
    "attr-whitespace": false,  
      
    "tags-check": true,  
    "tag-pair": true,  
    "tag-self-close": true,  
    "tagname-lowercase": true,  
    "tagname-specialchars": false,  
    "src-not-empty": true,  
      
    "id-class-ad-disabled": true,  
    "id-class-value": "dash",  
    "id-unique": true,  
      
    "space-tab-mixed-disabled": space4,  
    "spec-char-escape": false,  
}
```

#### Local | Pre-Commit Requirements | Proc
---
**SCRIPT | RUN** `Script File`: - File Name: **``  .sh ``**

```bash
#!/bin/bash 
npx prettier . --write
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

#### AI Answer

To set up a Run configuration in PyCharm based on the provided bash script, follow these steps:

1. Open PyCharm and go to the "Run" menu.
2. Select "Edit Configurations" to open the Run/Debug Configurations dialog.
3. Click the "+" button to add a new configuration and select "Node.js" from the list.
4. In the "Name" field, enter a name for the configuration.
5. Set the "Allow Multiple" option to either "Y" or "N" based on your requirements.
6. Set the "Store as File" option to either "Y" or "N" based on your requirements.
7. In the "Package.json" field, enter the path to the`package.json`file, for
   example:`D:\Code\Code Institute\dash-and-do-github\package.json`.
8. In the "Command" field, enter the command you want to run, based on the bash script.
9. In the "Scripts" field, enter the script name or command from the bash script.
10. In the "Arguments" field, enter any additional arguments you want to pass to the script.
11. In the "Node interpreter" field, enter the path to the Node.js executable, for
    example:`C:\Programs Files\node.js\node.exe`.
12. In the "Node options" field, enter any additional options you want to pass to the Node.js interpreter.
13. In the "Package manager" field, enter the path to the package manager executable, for
    example:`C:\Program Files\node.js\node.exe`.
14. In the "Environments" section, you can add any environment variables you need for your script.
15. In the "Before Launch" section, you can configure any tasks or actions to be performed before running the script.

Once you have configured the Run configuration, click "OK" to save the configuration.Please note that the specific
values for the fields will depend on your project setup and requirements. Make sure to adjust the paths and options
accordingly.

**NPM**: `package.json`

```json
"devDependencies": {    
    "htmlhint": "^1.1.4",  
    //"w3c-html-validator": "^1.4.0"  
},
```

**Pre-Commit**: ``

- [github.com/Lucas-C/pre-commit-hooks-nodejs](https://github.com/Lucas-C/pre-commit-hooks-nodejs)
- Rev: [Tags · Lucas-C/pre-commit-hooks-nodejs (github.com)](https://github.com/Lucas-C/pre-commit-hooks-nodejs/tags))

```yml
repos:
-   repo: https://github.com/Lucas-C/pre-commit-hooks-nodejs
    rev: v1.1.2
    hooks:
    -   id: htmlhint
        # optional custom config:
        args: [--config, .htmlhintrc]
    -   id: htmllint
    -   id: markdown-toc
        # optional custom config:
        args: [--indent, "    ", -i]
    -   id: dockerfile_lint
        # optional custom config:
        args: [--json, --verbose, --dockerfile]
```

### Sources

- Org: [HTMLHint (github.com)](https://github.com/HTMLHint)
- Docs: [List of rules | HTMLHint](https://htmlhint.com/docs/user-guide/list-rules)
- Scripts Options: [Options | HTMLHint](https://htmlhint.com/docs/user-guide/usage/options)
- Package: [htmlhint - npm (npmjs.com)](https://www.npmjs.com/package/htmlhint)
-

GitHub: [htmlhint/HTMLHint: ⚙️ The static code analysis tool you need for your HTML (github.com)](https://github.com/htmlhint/HTMLHint)

- Perplexity:

## Final

> FLOW

### Steps

1. [x] Install by NPM
2. Configure and set Rules
3. Review Task Runners
    1.  [ ] 
        - [grunt-htmlhint-inline](https://github.com/htmlhint/grunt-htmlhint-inline)- Grunt plugin for linting inline
          HTML.
    2. [ ] 
        - [grunt-htmlhint](https://github.com/htmlhint/grunt-htmlhint)- Grunt plugin for HTMLHint.
    3. [x] 
        - [super-linter](https://github.com/github/super-linter)- GitHub action - a combination of linters, including
          HTMLHint.
4. JetBrains does not have an integration for Save actions
5. Configure `.pre-commit-configuration.yaml`
    1. [ ] Run pre-commit like a local runner and not on pre-commit
    2. [ ] Then use pre-commit to test for all PASS on commit
6. Create and test bash for local script - a Final Report?
7. Setup IDE Run Configuration with local bash script
8. CI Use the GitHub Super Linter

### Repository

```dirtree

- /dash-and-do-github
	- /.github
		- /workflows
			- .yml
	- /docs
		- /integration
			- /1-dev
				- file.md
	- /scripts
		- /1-dev
			- .sh
	- .file
```

## Sources

- .
- .
- .

---
> .
---