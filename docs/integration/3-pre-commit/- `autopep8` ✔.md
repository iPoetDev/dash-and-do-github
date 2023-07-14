---
tags: #Python
---

# Source

-   Pre-Commit Repo [URL]: [github.com/pre-commit/mirrors-autopep8](https://github.com/pre-commit/mirrors-autopep8)
-   Hook ID
    -   Id: `autopep8`
-   Category | Intent: Code Formatter | PEP8 Linter | Code Style
-   Description: autopep8 automatically formats Python code to conform to
    the[PEP 8](https://www.python.org/dev/peps/pep-0008/)style guide

## Fetch

```yaml

```

## Type

-   [ ] Repo Template: `    `
-   [x] Pre-commit: `  pre-commit  ` and associated repo/hooks
-   [ ] Library: `    `
-   [ ] Settings: `    `
    -   [ ] EnVar: `    `
-   [ ] Service: `    `

<small>Do not list harming or insecure confidential configurations that may pose a risk</small>

## Outline

> Why | What | How (Brief)

-   **WHY**:
    -   Pre-Commit workflows are a control/review gate before code is committed and
    -   Is an excellent choice for improving code quality in the following areas:
-   **WHAT**:
    -   [ ] Commit Messages Standards
    -   [x] Code Formatting, Validation & Style Compliance
    -   [x] Language Linting Standards | Compliance
    -   [ ] Secret & Leak Prevention

### Library

-   [x] Source: [pypi.org/project/autopep8/](https://pypi.org/project/autopep8/)
-   [x] Repo: [hhatto/autopep8: A tool that automatically formats Python code to conform to the PEP 8 style guide. (github.com)](https://github.com/hhatto/autopep8)
-   [x] Config: See Options

-   autopep8 automatically formats Python code to conform to the[PEP 8](https://www.python.org/dev/peps/pep-0008/)style
    guide.
-   Uses the[pycodestyle](https://github.com/PyCQA/pycodestyle)utility to determine what parts of the code needs to be
    formatted.
-   autopep8 is capable of fixing most of the
    formatting[issues](https://pycodestyle.readthedocs.org/en/latest/intro.html#error-codes)that can be reported by
    pycodestyle.

### Install

```bash
pip install --upgrade autopep8
```

-   autopep8 requires[pycodestyle](https://github.com/PyCQA/pycodestyle).

#### Options

```ruby
usage: autopep8 [-h] [--version] [-v] [-d] [-i] [--global-config filename]
                [--ignore-local-config] [-r] [-j n] [-p n] [-a]
                [--experimental] [--exclude globs] [--list-fixes]
                [--ignore errors] [--select errors] [--max-line-length n]
                [--line-range line line] [--hang-closing] [--exit-code]
                [files [files ...]]

Automatically formats Python code to conform to the PEP 8 style guide.

positional arguments:
  files                 files to format or '-' for standard in

optional arguments:
  -h, --help            show this help message and exit
  --version             show programs version number and exit
  -v, --verbose         print verbose messages; multiple -v result in more
                        verbose messages
  -d, --diff            print the diff for the fixed source
  -i, --in-place        make changes to files in place
  --global-config filename
                        path to a global pep8 config file; if this file does
                        not exist then this is ignored (default:
                        ~/.config/pep8)
  --ignore-local-config
                        dont look for and apply local config files; if not
                        passed, defaults are updated with any config files in
                        the projects root directory
  -r, --recursive       run recursively over directories; must be used with
                        --in-place or --diff
  -j n, --jobs n        number of parallel jobs; match CPU count if value is
                        less than 1
  -p n, --pep8-passes n
                        maximum number of additional pep8 passes (default:
                        infinite)
  -a, --aggressive      enable non-whitespace changes; multiple -a result in
                        more aggressive changes
  --experimental        enable experimental fixes
  --exclude globs       exclude file/directory names that match these comma-
                        separated globs
  --list-fixes          list codes for fixes; used by --ignore and --select
  --ignore errors       do not fix these errors/warnings (default:
                        E226,E24,W50,W690)
  --select errors       fix only these errors/warnings (e.g. E4,W)
  --max-line-length n   set maximum allowed line length (default: 79)
  --line-range line line, --range line line
                        only fix errors found within this inclusive range of
                        line numbers (e.g. 1 99); line numbers are indexed at
                        1
  --hang-closing        hang-closing option passed to pycodestyle
  --exit-code           change to behavior of exit code. default behavior of
                        return value, 0 is no differences, 1 is error exit.
                        return 2 when add this option. 2 is exists
                        differences.
```

### Config: AutoPep8

> If in same tagret directory

-   [ ] PyCodeStyle: `$HOME/.config/pycodestyle (~\.pycodestyle)`
-   [ ] Setup.cfg
-   [ ] tox.ini
-   [ ] .pep8
-   [ ] .flake8
-   [x] PyProject.toml

[pyproject.toml](https://github.com/hhatto/autopep8#id9)

-   **`autopep8`** can also use `pyproject.toml`.
-   The section must be `[tool.autopep8]`, and
-   `pyproject.toml` takes precedence over any other configuration files.

configuration file example:

```
[tool.autopep8]
max_line_length = 120
ignore = "E501,W6"  # or ["E501", "W6"]
in-place = true
recursive = true
aggressive = 3
```

---

## Config

-   [ ] Create a` .pre-commit-config.yaml` in root of repository.
-   [ ] Commit `yaml` repository.
-   [ ] Prepare for run by adding hook's
    -   [ ] Repository: `- repo: {url}`: https://github.com/pre-commit/mirrors-autopep8
    -   [ ] Revision: `rev` : `v2.02  `
        -   [ ] v2.02
        -   Select/Use the ref you want to point at
    -   [ ] Hooks:
        -   [ ] Id: `id {hook-ident}`

```yaml
- repo: https://github.com/pre-commit/mirrors-autopep8
  rev: '' # Use the sha / tag you want to point at
  hooks:
      - id: autopep8
```

### Overriding `args`

note
that[this repository](https://github.com/pre-commit/mirrors-autopep8/blob/5c459f3f27ae62fefef60fe5771e51baa02e7a83/.pre-commit-hooks.yaml#L6)
sets`args: [-i]`, if you are configuring autopep8 using`args`you'll want to include either`-i`(`--in-place`)
or`-d`(`--diff`). it is usually better to configure`autopep8`in
its[config file](https://github.com/hhatto/autopep8#configuration).

##### Sources

> Link | Guides | Repo

-   [AutoPEP8](https://github.com/hhatto/autopep8)
-   [AutoPEP8 Configuration](https://github.com/hhatto/autopep8#configuration)
