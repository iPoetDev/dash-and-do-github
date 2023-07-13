**META**: 23-07-13.18:25 | Last Edited By:

## Workflow | Issue

> .

- [ ] CONFIG:
    - [ ]  Build | Integrate | Test | Quality | Security | Config |
- [ ] GitHub Issue(s) Created?
    - [ ] FLOW: Workflow | Process | Outline
        - [ ] #Issue #12 [FLOW :: Code Quality Assurance](https://github.com/iPoetDev/dash-and-do-github/issues/12)
        - [ ] #Flow: External Validation Flow: W3C HTML & CSS Validation
    - [ ] LINT: Report
        - [ ] #Issue
- [ ] FLOW
    - [ ] Config .dotfile
        - [ ] ` package.json`
        - [ ] ` stylelintrc.json`
    - [x] IDE Configuration
        - [x] Run Configuration?
    - [ ] Pre-Commit
        - [ ] Added dependencies - ? Check
    - [ ] CI Workflow
        - [ ] YML
        - [ ] Runner

# Package: A Stylelint Plugin

**`Intent | Purpose:`**
A [stylelint](http://stylelint.io/) plugin based on [csstree](https://github.com/csstree/csstree) to examinate CSS syntax. It examinates at-rules and declaration values to match W3C specs and browsers extensions. It might be extended in future to validate other parts of CSS.
```ruby
>> A [stylelint](http://stylelint.io/) plugin based on [csstree](https://github.com/csstree/csstree) to examinate CSS syntax. It examinates at-rules and declaration values to match W3C specs and browsers extensions. It might be extended in future to validate other parts of CSS.
```

- Related Config
    - [[CONFIG - {{}}]]
    - [[stylelint]] - PLugin

## Package | Library Source

> .

- [x] NPM

**Link:** **`URL`**

```bash
https://www.npmjs.com/package/stylelint-csstree-validator
```

### Source

```bash
https://github.com/csstree/stylelint-validator
```

### Install

```bash

npm install --save-dev stylelint-csstree-validator

```

### Config
`stylelintrc.json`
```json
{
"plugins": [  
        "stylelint-csstree-validator"  
    ],  
"rules": {  
    "csstree/validator": {  
        "syntaxExtensions": false,  
        "atrules": false,  
        "ignoreAtrules": [  
                "tailwind",  
                "apply",  
                "variants",  
                "responsive",  
                "screen"  
            ]  
        }  
    }
}
```

**NPM**: `package.json`

```json

```

**Pre-Commit**: ``

```yml
  -
    repo : https://github.com/thibaudcolas/pre-commit-stylelint
    rev  : v15.10.0
    hooks:
      -
        id: stylelint
        additional_dependencies:
        -  stylelint-csstree-validator@latest
```

### Options

- Docs:
- Package: [stylelint-csstree-validator - npm (npmjs.com)](https://www.npmjs.com/package/stylelint-csstree-validator)
- GitHub: [csstree/stylelint-validator: Stylelint plugin to validate CSS syntax (github.com)](https://github.com/csstree/stylelint-validator)
- Perplexity:

## Final

> FLOW

### Steps

1. . Install Stylelint Plugin
2. . Configure Styleintrc.json
3. . Test the rules
4. . Check the pre-commit

### Repository

```dirtree

- /dash-and-do-github
	- /.github
		- /workflows
			- .yml
	- /docs
		- /integration
			- /1-dev
				- stylelint-csstree-validator.md
	- /scripts
		- /1-dev
			- .sh
	- stylelintrc.json
	- package.json
```

## Sources

- .
- .
- .

---
> .
---