Activate: 23-07-08

# Source

-   Pre-Commit Repo [URL]:
-   Hook ID
    -   id: `trailing-whitespace`
    -   id: `debug-statements`
    -   id: `detect-private-key`
    -   id: `check-yaml`
    -   id: `end-of-file-fixer`
-   Category | Intent: Check | Lint | Fix
-   Description:

## Fetch

```bash
pip install pre-commit
```

## Config

-   [ ] Create a`.pre-commit-config.yaml` in root of repository
-   [ ] Commit to repository
-   [ ] Prepare for run by adding hook's
    -   [ ] Repository: `- repo: {url}`
    -   [ ] Revision: `rev` - Select/Use the ref you want to point at
    -   [ ] Hooks:
        -   [ ] Id: `id {hook-ident}`

```yaml
repos:
	- repo: https://github.com/pre-commit/pre-commit-hooks
	  rev: v4.4.0 # Use the ref you want to point at
	  hooks:
		- id: trailing-whitespace
		- id: debug-statements
		- id: detect-private-key
		- id: check-yaml
		- id: end-of-file-fixer

```

## Install

```bash
pre-commit install
```

### Output:

```bash
pre-commit installed at .git\hooks\pre-commit
```

### Custom Options

```
- repos
- default_install_hook_types
- default_stages default (all stages)) a configuration-wide default for the `stages`
	- only override individual hooks that do not set stages
	- default_stages: [pre-commit, pre-push]
- files default `''`) global file include pattern.
- exclude : default `^$`) global file exclude pattern.
- fail_fast : Default: False | True: To have pre-commit stop running hooks after the first failure.

```

## Run

```bash
pre-commit run --all-files
```

### Actions

-   [ ] Detects
-   [ ] Asserts: Pass | Fails
-   [ ] Fixes

### Example

```
trim trailing whitespace.................................................Failed
- hook id: trailing-whitespace
- exit code: 1
- files were modified by this hook

```
