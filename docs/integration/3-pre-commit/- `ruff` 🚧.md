- Run 'ruff' for extremely fast Python linting

### Badge:  ![Ruff](https://camo.githubusercontent.com/3ab2287018b49eee45474feef5f497e69759e7d29fabfb8c5a82637b8d6d4aa1/68747470733a2f2f696d672e736869656c64732e696f2f656e64706f696e743f75726c3d68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f636861726c6965726d617273682f727566662f6d61696e2f6173736574732f62616467652f76322e6a736f6e)](https://github.com/astral-sh/ruff)

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

# Source

- Pre-Commit Repo [URL]: https://github.com/astral-sh/ruff-pre-commit
- Hook ID
    - ` ruff `
- Category | Intent: Python Linter | Static Code Analysis | Style Guide
- Description:
    - Be used to replace[Flake8](https://pypi.org/project/flake8/)(plus dozens of
      plugins),[isort](https://pypi.org/project/isort/),[pydocstyle](https://pypi.org/project/pydocstyle/),[yesqa](https://github.com/asottile/yesqa),[eradicate](https://pypi.org/project/eradicate/),[pyupgrade](https://pypi.org/project/pyupgrade/),
      and[autoflake](https://pypi.org/project/autoflake/),

## Fetch

```ruby
https://github.com/astral-sh/ruff-pre-commit
```

## Library: Ruff

- [ ] Source: https://github.com/astral-sh/ruff
- [ ] Config:

```bash
pip install ruff
```

### Options

```bash
ruff check .                        # Lint all files in the current directory (and any subdirectories)
ruff check path/to/code/            # Lint all files in `/path/to/code` (and any subdirectories)
ruff check path/to/code/*.py        # Lint all `.py` files in `/path/to/code`
ruff check path/to/code/to/file.py  # Lint `file.py`
```

### Configuration

**Defacto**

```toml
[tool.ruff]
# Enable pycodestyle (`E`) and Pyflakes (`F`) codes by default.
select = ["E", "F"]
ignore = []

# Allow autofix for all enabled rules (when `--fix`) is provided.
fixable = ["A", "B", "C", "D", "E", "F", "G", "I", "N", "Q", "S", "T", "W", "ANN", "ARG", "BLE", "COM", "DJ", "DTZ", "EM", "ERA", "EXE", "FBT", "ICN", "INP", "ISC", "NPY", "PD", "PGH", "PIE", "PL", "PT", "PTH", "PYI", "RET", "RSE", "RUF", "SIM", "SLF", "TCH", "TID", "TRY", "UP", "YTT"]
unfixable = []

# Exclude a variety of commonly ignored directories.
exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".git-rewrite",
    ".hg",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".pytype",
    ".ruff_cache",
    ".svn",
    ".tox",
    ".venv",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "venv",
]

# Same as Black.
line-length = 88

# Allow unused variables when underscore-prefixed.
dummy-variable-rgx = "^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$"

# Assume Python 3.10.
target-version = "py310"

[tool.ruff.mccabe]
# Unlike Flake8, default to a complexity level of 10.
max-complexity = 10
```

## Pre-Commit Config

- [ ] Create a` .pre-commit-config.yaml` in root of repository.
- [ ] Commit `yaml` repository.
- [ ] Prepare for run by adding hook's
    - [ ] Repository: `- repo: {url}`:
    - [ ] Revision: `rev` : `  v0.0.277  `
        - [ ] v
        - Select/Use the ref you want to point at
    - [ ] Hooks:
        - [ ] Id: `id {hook-ident}`
        - [ ] 

**REPORT | MANUAL**

- Ruff's pre-commit hook should be placed after other formatting tools, such as Black and isort,

```yaml
- repo : https://github.com/astral-sh/ruff-pre-commit
  # Ruff version.
  rev  : v0.0.277
  hooks:
    - id: ruff
```

**AUTO FIX**

- _UNLESS_you enable autofix, in which case, Ruff's pre-commit hook should run_before_Black, isort, and other formatting
  tools, as Ruff's autofix behavior can output code changes that require reformatting.

```yaml
- repo : https://github.com/astral-sh/ruff-pre-commit
  # Ruff version.
  rev  : v0.0.277
  hooks:
    - id  : ruff
      args: [ --fix, --exit-non-zero-on-fix ]
```

## Install

```bash


```

## Config: Actual `pyproject.toml`

- [ ] E
- [ ] F
- [ ] I
- [ ] D
- [ ] YTT
- [ ] PL
- [ ] T20
- [ ] RSE
- [ ] RET
- [ ] SIM
- [ ] TID
- [ ] TCH
- [ ] ARG
- [ ] PTH
- [ ] S
- [ ] ANN
- [ ] B: Bandit

```toml
[tool.ruff]
# Enable pycodestyle (`E`) and Pyflakes (`F`) codes by default.
select = ["E", "F", "I", "D", "YTT", "PL", "T20", "RSE", "RET", "SIM", "TID",
    "TCH", "ARG", "PTH", "S", "ANN", "B"]
ignore = []

# Allow autofix for all enabled rules (when `--fix`) is provided.
fixable = ["A", "B", "C", "D", "E", "F", "G", "I", "N", "Q", "S", "T", "W", "ANN", "ARG", "BLE", "COM", "DJ", "DTZ", "EM", "ERA", "EXE", "FBT", "ICN", "INP", "ISC", "NPY", "PD", "PGH", "PIE", "PL", "PT", "PTH", "PYI", "RET", "RSE", "RUF", "SIM", "SLF", "TCH", "TID", "TRY", "UP", "YTT"]
unfixable = []
fix-only = true
show-fixes = true
show-source = true
#fix = true
format = "grouped"

# Tags
task-tags = ["TODO", "FIXME", "todo", "fixme"]

# Exclude a variety of commonly ignored directories.
exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".hg",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".pytype",
    ".ruff_cache",
    ".svn",
    ".tox",
    ".venv",
    "__pycache__",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "venv",
]
# Per File

# Same as Black.
line-length = 100

# Allow unused variables when underscore-prefixed.
dummy-variable-rgx = "^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$"

# Assume Python 3.10.
target-version = "py311"


[tool.ruff.mccabe]
# Unlike Flake8, default to a complexity level of 10.
max-complexity = 15

[tool.ruff.per-file-ignores]

[tool.ruff.flake8-annotations]
allow-star-arg-any = false
ignore-fully-untyped = true
mypy-init-return = false
suppress-dummy-args = false
suppress-none-returning = false
[tool.ruff.flake8-bandit]
check-typed-exception = false
#hardcoded-tmp-directory = []
#extend-hardcoded-tmp-directory = [""]
[tool.ruff.flake8-bugbear]
#extend-immutable-calls = ["fastapi.Depends", "fastapi.Query"]
[tool.ruff.flake8-builtins]
#builtins-ignorelist = [""]
[tool.ruff.flake8-comprehensions]
allow-dict-calls-with-keyword-arguments = true
[tool.ruff.flake8-errmsg]
max-string-length = 20
[tool.ruff.flake8-gettext]
#extend-function-names = ["ugettetxt"]
#function-names = ["_", "gettext", "ngettext", "ugettetxt"]
[tool.ruff.flake8-implicit-str-concat]
#setting allow-multiline = false should
#typically be coupled with disabling explicit-string-concatenation
allow-multiline = true
[tool.ruff.flake8-import-conventions]
[tool.ruff.flake8-import-conventions.aliases]
# Declare the default aliases.
# Declare the banned aliases.
# Declare the banned `from` imports.
# Declare a custom alias for the `matplotlib` module
[tool.ruff.flake8-pytest-style]
#fixture-parentheses = true
#mark-parentheses = true
#parametrize-names-type = "list"
#parametrize-values-row-type = "list"
#parametrize-values-type = "list"
#raises-extend-require-match-for = ["requests.RequestException"]
#raises-require-match-for = ["requests.RequestException"]

[tool.ruff.flake8-quotes]
avoid-escape = false
docstring-quotes = "double"
inline-quotes = "single"
multiline-quotes = "single"
[tool.ruff.flake8-self]
#ignore-names = ["_new"]
[tool.ruff.flake8-tidy-imports]
#ban-relative-imports = "all"
[tool.ruff.flake8-tidy-imports.banned-api]
[tool.ruff.flake8-type-checking]
#exempt-modules = ["typing", "typing_extensions"]
#runtime-evaluated-base-classes = ["pydantic.BaseModel"]
#runtime-evaluated-decorators = ["attrs.define", "attrs.frozen"]
strict = false
[tool.ruff.flake8-unused-arguments]
ignore-variadic-names = true
[tool.ruff.isort]
#classes = ["SVC"]
#constants = ["constant"]
#variables = ["VAR"]
#extra-standard-library = ["path"]
force-single-line = true
force-sort-within-sections = true
#force-to-top = ["src"]
#forced-separate = ["tests"]
force-wrap-aliases = true
combine-as-imports = true
known-first-party = ["src"]
#known-local-folder = ["src"]
#known-third-party = ["src"] # TODO: Add all third-party packages for packages.
#lines-after-imports = 1
lines-between-types = 1
#no-lines-before = ["future", "standard-library","third-party","first-party","local-folder","str"]
order-by-type = true
#relative-imports-order = "closest-to-furthest
#required-imports = ["from __future__ import annotations"]
#section-order = ["future", "standard-library", "third-party", "first-party", "local-folder"]
#single-line-exclusions = ["os", "json"]
#split-on-trailing-comma = false
#[tool.ruff.isort.sections]
# Group all * imports into a/own/separate section.
[tool.ruff.pep8-naming]
#classmethod-decorators = ["pydantic.validator"]
#ignore-names = [""]
#staticmethod-decorators = ["stcmthd"]
[tool.ruff.pycodestyle]
ignore-overlong-task-comments = true
max-doc-length = 100
[tool.ruff.pydocstyle]
convention = "google"
#ignore-decorators = ["typing.overload"]
#property-decorators = ["gi.repository.GObject.Property"]
[tool.ruff.pylint]
#allow-magic-value-types = ["int"]
#Type: list["str" | "bytes" | "complex" | "float" | "int" | "tuple"]
max-args = 6
max-branches = 12
max-returns = 6
max-statements = 50
[tool.ruff.pyupgrade]
keep-runtime-typing = true

```

### Style: Python

- Line Length: 100
- Max complexity: 15
- Docstring Quotes: Double
- Single Quotes: Inline and Multi-line
- Max Doc Length: 100
- Doc Style: Google
- Max Args: 6
- Max Returns: 6
- Max Statements: 50

## Run

```bash


```

