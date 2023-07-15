# Source

> -   `editorconfig-checker` is a tool to check if your files consider your .editorconfig-rules.

-   Pre-Commit Repo [URL]: https://github.com/editorconfig-checker/editorconfig-checker.python
-   Hook ID
    -   editorconfig-checker
-   Category | Intent: Code Style | Code Quality |
-   Description: maintain consistent coding styles and base line linting for Code Institute projects
    -   `EditorConfig` helps maintain consistent coding styles for multiple developers working on the same project across
        various editors and IDEs.
    -   The `EditorConfig` project consists of**a file format**for defining coding styles and a collection of**text editor
        plugins**that enable editors to read the file format and adhere to defined styles.
    -   `EditorConfig` files are easily readable and they work nicely with version control systems.

## Fetch

```yaml

```

## Library

-   [ ] Source: https://github.com/editorconfig-checker/editorconfig-checker.python
-   [ ] Installed: PyCharm/WebStorm

```python
pip install editorconfig-checker
```

#### Usage

```
ec -version
```

#### .editorconfig

```bash
# EditorConfig is awesome: https://EditorConfig.org
# Code Insititute Code Style Basics

# top-most EditorConfig file
root = true

# Unix-style newlines with a newline ending every file
[*]
indent_style = space # Python PEP8 Style Guide as dominant factor
end_of_line = lf
trim_trailing_whitespace = true # IDE | Pre-commit Linting
insert_final_newline = true # IDE | Pre-commit Linting

# Match Front-end Files with
[*.{html,css,scss}]
charset = utf-8 # IDE | Pre-commit Linting | File Compatibility
indent_size = 4 # Consistency but individually controllable
max_line_length = 120 #PyCharm, WebStorm

# Matches multiple files with brace expansion notation
# Set default charset
[*.{js,py}]
charset = utf-8 # IDE | Pre-commit Linting | File Compatibility

# 4 space indentation
[*.js]
# indent_style = space
indent_size = 4 # Consistency but individually controllable
max_line_length = 100 #PyCharm, WebStorm

[*.py]
# indent_style = space
indent_size = 4 # Python PEP8 Style Guide as dominant factor, indent size is critical for Python
max_line_length = 80 # Autopep8 default #PyCharm, WebStorm

# Matches the exact files either package.json or .travis.yml
[{package.json,.travis.yml}]
# indent_style = space
indent_size = 2
```

## IDE

-   [ ] Pycharm
-   [ ] WebStorm
-   [ ] VSCode

### Config

-   [ ]

### Run

-   [ ]

```bash


```

## Pre-Commit

### Config

-   [ ] Create a` .pre-commit-config.yaml` in root of repository.
-   [ ] Commit `yaml` repository.
-   [ ] Prepare for run by adding hook's
    -   [ ] Repository: `- repo: {url}`:
    -   [ ] Revision: `rev` : `2.7.2  `
        -   [ ] 2.7.2: https://github.com/editorconfig-checker/editorconfig-checker.python/releases/tag/2.7.2
        -   Select/Use the ref you want to point at
    -   [ ] Hooks:
        -   [ ] Id: `id {hook-ident}`
        -   [ ] alias: `alias: {}`

```yaml
repos:
    - repo: https://github.com/editorconfig-checker/editorconfig-checker.python
      rev: '2.7.2' # pick a git hash / tag to point to
      hooks:
          - id: editorconfig-checker
            alias: ec
```

### Install

```bash


```

### Run

```bash
[INFO] Initializing environment for https://github.com/editorconfig-checker/editorconfig-checker.python.
[INFO] Installing environment for https://github.com/editorconfig-checker/editorconfig-checker.python.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes... trim trailing whitespace.................................................Failed - hook id: trailing-whitespace - exit code: 1
- files were modified by this hook  Fixing docs/integration/pre-commit/- `editorconfig-checker`
- `editorconfig-checker` is a tool to check if your files consider your .editorconfig-rules..md
- debug statements (python)............................(no files to check)Skipped
- detect private key.......................................................Passed
- check yaml...............................................................Passed
- fix end of files.........................................................Failed
- hook id: end-of-file-fixer
	- exit code: 1
- files were modified by this hook
- Fixing docs/integration/pre-commit/- `editorconfig-checker`
- `editorconfig-checker` is a tool to check if your files consider your .editorconfig-rules..md
- Check .editorconfig rules................................................Passed

```
