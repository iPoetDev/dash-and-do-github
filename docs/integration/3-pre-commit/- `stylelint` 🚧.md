# Source

- Pre-Commit Repo [URL]:  https://github.com/awebdeveloper/pre-commit-stylelint
- Hook ID
    - **` stylelint `**
- Category | Intent:
- Action: **prevents git commits unless the checks pass.**
- Description:

## Fetch

> Download

```bash
npm init stylelint
npm install --save-dev stylelint stylelint-config-standard-scss
```

## Library

> Package | Repo

- [ ] Web: https://stylelint.io/
- [ ] Package:
- [ ] Source: https://github.com/stylelint/stylelint
- [ ] Config:

### Options

#### [Configure](https://stylelint.io/user-guide/configure)

Each rule configuration fits one of the following formats:

- `null`(to turn the rule off)
- a single value (the primary option)
- an array with two values (`[primary option, secondary options]`)

```bash
- rules
    - disableFix
    - message
    - reportDisables
    - severity
- extends
- plugins
- customSyntax
- overrides
- defaultSeverity
- report*`](https
    - reportDescriptionlessDisables
    - reportInvalidScopeDisables
    - reportNeedlessDisables
- configurationComment
- ignoreDisables
- ignoreFiles
- allowEmptyInput
- cache
- fix
```

### Config ` styleintrc.json|yml|yaml|cjs`

- [ ] Project Level
- [ ] Node Module: `D:\Code\node_modules`
- [ ] Package: `D:\Code\node_modules\{{}}`
  Basic

```json
{
  "extends": "stylelint-config-standard-scss"
  # Or
  "customSyntax": "postcss-lit"
  # Or
  "overrides": [  
		{  
			"files": ["*.js"],  
			"customSyntax": "postcss-lit"  
		}  
	]
}
```

### Standard Config

- https://www.npmjs.com/package/stylelint-config-standard

```css
- alpha-value-notation
- at-rule-empty-line-before
- at-rule-no-vendor-prefix
- color-function-notation
- color-hex-length
- comment-empty-line-before
- comment-whitespace-inside
- custom-property-empty-line-before
- custom-media-pattern
- custom-property-pattern
- declaration-block-no-redundant-longhand-properties
- declaration-block-single-line-max-declarations
- declaration-empty-line-before
- font-family-name-quotes
- function-name-case
- function-url-quotes
- hue-degree-notation
- import-notation
- keyframe-selector-notation
- keyframes-name-pattern
- length-zero-no-unit
- media-feature-name-no-vendor-prefix
- media-feature-range-notation
- number-max-precision
- property-no-vendor-prefix
- rule-empty-line-before
- selector-attribute-quotes
- selector-class-pattern
- selector-id-pattern
- selector-no-vendor-prefix
- selector-not-notation
- selector-pseudo-element-colon-notation
- selector-type-case
- shorthand-property-no-redundant-values
- value-keyword-case
- value-no-vendor-prefix
```

### Avoid Errors

- [Avoid errors](https://stylelint.io/user-guide/rules#avoid-errors)
    - [Descending](https://stylelint.io/user-guide/rules#descending)
    - [Duplicate](https://stylelint.io/user-guide/rules#duplicate)
    - [Empty](https://stylelint.io/user-guide/rules#empty)
    - [Invalid](https://stylelint.io/user-guide/rules#invalid)
    - [Irregular](https://stylelint.io/user-guide/rules#irregular)
    - [Missing](https://stylelint.io/user-guide/rules#missing)
    - [Non-standard](https://stylelint.io/user-guide/rules#non-standard)
    - [Overrides](https://stylelint.io/user-guide/rules#overrides)
    - [Unmatchable](https://stylelint.io/user-guide/rules#unmatchable)
    - [Unknown](https://stylelint.io/user-guide/rules#unknown)

## IDE

- [ ] Pycharm ✔
- [ ] WebStorm ✔

### Config

- [ ] 

<details><summary>Screenshots</summary></details>

```bash


```

### Run

- [ ] 

```bash


```

## Pre-Commit

### Config

- [ ] Create a` .pre-commit-config.yaml` in root of repository.
- [ ] Commit `yaml` repository.
- [ ] Prepare for run by adding hook's
    - [ ] Repository: `- repo: {url}`:
    - [ ] Revision: `rev` : `    `
        - [ ] v
        - Select/Use the ref you want to point at
    - [ ] Hooks:
        - [ ] id: `id {hook-ident}`
        - [ ] alias:
        - [ ] name:
- [ ] More
    - [ ] language_version
    - [ ] files
    - [ ] exclude
    - [ ] types
    - [ ] types_or
    - [ ] exclude_types
    - [ ] args
    - [ ] stages
    - [ ] additional_dependencies
    - [ ] always_run
    - [ ] verbose
    - [ ] log_file

```yaml


```

### Install

```bash
# And Config

```

### Run

```bash
npx stylelint "**/*.css"
```
