**META**: 23-07-14.09:42 | Last Edited By:

![](https://gitleaks.io/logo.png)

## Workflow | Issue

> .

-   [x] CONFIG:
    -   [x] Data | Build | Integrate | Test | Quality | Security | Config | Deploy | Release
-   [x] GitHub Issue(s) Created?
    -   [x] FLOW: Workflow | Process | Outline
        -   [x] #Issue #12 [FLOW :: Code Quality Assurance](https://github.com/iPoetDev/dash-and-do-github/issues/12)
        -   [ ] #Flow: Secrets Protect Flow (TBA)
    -   [ ] LINT: Report
        -   [ ] #Issue
-   [ ] FLOW
    -   [x] Config .dotfile
    -   [x] use default
        -   [ ] `  .toml`
    -   [x] Local Script
        -   [ ] Bash?
    -   [ ] IDE Configuration
        -   [ ] Run Configuration?
    -   [ ] Pre-Commit
        -   [ ] as a runner
        -   [x] on commit
    -   [ ] CI Workflow
        -   [x] YML
        -   [ ] Runner

# Package:

Blog [Gitleaks](https://blog.gitleaks.io/)
**`Intent | Purpose:`** secret scanner for git repositories, files, and directories.

```ruby
>> is a fast, light-weight, portable, and open-source secret scanner for git repositories, files, and directories.
```

## Package | Library Source

> .

-   [x] Chocolatly
    -   [ ] Use a gloabl config var: GITLEAKS_CONFIG for central config, not per project

**Link:** **`URL`** [Gitleaks](https://gitleaks.io/)

```bash
https://gitleaks.io/
```

### Source

[gitleaks/gitleaks: Protect and discover secrets using Gitleaks 🔑 (github.com)](https://github.com/gitleaks/gitleaks)

```bash
https://github.com/gitleaks/gitleaks
```

### Install

-   [x] Chocolately
        Like done by Chocolatel

```bash
# From Source
git clone https://github.com/gitleaks/gitleaks.git
cd gitleaks
make build
```

### Config

1. --config/-c
2. env var GITLEAKS_CONFIG
3. (--source/-s)/.gitleaks.toml
4. If none of the three options are used, then gitleaks will use the default
   config [Default config](https://github.com/gitleaks/gitleaks/blob/master/config/gitleaks.toml)

```toml
# Title for the gitleaks configuration file.
title = "Gitleaks title"

# Extend the base (this) configuration. When you extend a configuration
# the base rules take precedence over the extended rules. I.e., if there are
# duplicate rules in both the base configuration and the extended configuration
# the base rules will override the extended rules.
# Another thing to know with extending configurations is you can chain together
# multiple configuration files to a depth of 2. Allowlist arrays are appended
# and can contain duplicates.
# useDefault and path can NOT be used at the same time. Choose one.
[extend]
# useDefault will extend the base configuration with the default gitleaks config:
# https://github.com/zricethezav/gitleaks/blob/master/config/gitleaks.toml
useDefault = true
# or you can supply a path to a configuration. Path is relative to where gitleaks
# was invoked, not the location of the base config.
path = "common_config.toml"

# An array of tables that contain information that define instructions
# on how to detect secrets
[[rules]]

# Unique identifier for this rule
id = "awesome-rule-1"

# Short human readable description of the rule.
description = "awesome rule 1"

# Golang regular expression used to detect secrets. Note Golang's regex engine
# does not support lookaheads.
regex = '''one-go-style-regex-for-this-rule'''

# Golang regular expression used to match paths. This can be used as a standalone rule or it can be used
# in conjunction with a valid `regex` entry.
path = '''a-file-path-regex'''

# Array of strings used for metadata and reporting purposes.
tags = ["tag","another tag"]

# Int used to extract secret from regex match and used as the group that will have
# its entropy checked if `entropy` is set.
secretGroup = 3

# Float representing the minimum shannon entropy a regex group must have to be considered a secret.
entropy = 3.5

# Keywords are used for pre-regex check filtering. Rules that contain
# keywords will perform a quick string compare check to make sure the
# keyword(s) are in the content being scanned. Ideally these values should
# either be part of the idenitifer or unique strings specific to the rule's regex
# (introduced in v8.6.0)
keywords = [
  "auth",
  "password",
  "token",
]

# You can include an allowlist table for a single rule to reduce false positives or ignore commits
# with known/rotated secrets
[rules.allowlist]
description = "ignore commit A"
commits = [ "commit-A", "commit-B"]
paths = [
  '''go\.mod''',
  '''go\.sum'''
]
# note: (rule) regexTarget defaults to check the _Secret_ in the finding.
# if regexTarget is not specified then _Secret_ will be used.
# Acceptable values for regexTarget are "match" and "line"
regexTarget = "match"
regexes = [
  '''process''',
  '''getenv''',
]
# note: stopwords targets the extracted secret, not the entire regex match
# like 'regexes' does. (stopwords introduced in 8.8.0)
stopwords = [
  '''client''',
  '''endpoint''',
]

# This is a global allowlist which has a higher order of precedence than rule-specific allowlists.
# If a commit listed in the `commits` field below is encountered then that commit will be skipped and no
# secrets will be detected for said commit. The same logic applies for regexes and paths.
[allowlist]
description = "global allow list"
commits = [ "commit-A", "commit-B", "commit-C"]
paths = [
  '''gitleaks\.toml''',
  '''(.*?)(jpg|gif|doc)'''
]

# note: (global) regexTarget defaults to check the _Secret_ in the finding.
# if regexTarget is not specified then _Secret_ will be used.
# Acceptable values for regexTarget are "match" and "line"
regexTarget = "match"

regexes = [
  '''219-09-9999''',
  '''078-05-1120''',
  '''(9[0-9]{2}|666)-\d{2}-\d{4}''',
]
# note: stopwords targets the extracted secret, not the entire regex match
# like 'regexes' does. (stopwords introduced in 8.8.0)
stopwords = [
  '''client''',
  '''endpoint''',
]
```

#### Options | Usage

```shell
Usage:
  gitleaks [command]

Available Commands:
  completion  generate the autocompletion script for the specified shell
  detect      detect secrets in code
  help        Help about any command
  protect     protect secrets in code
  version     display gitleaks version

Flags:
  -b, --baseline-path string       path to baseline with issues that can be ignored
  -c, --config string              config file path
                                   order of precedence:
                                   1. --config/-c
                                   2. env var GITLEAKS_CONFIG
                                   3. (--source/-s)/.gitleaks.toml
                                   If none of the three options are used, then gitleaks will use the default config
      --exit-code int              exit code when leaks have been encountered (default 1)
  -h, --help                       help for gitleaks
  -l, --log-level string           log level (trace, debug, info, warn, error, fatal) (default "info")
      --max-target-megabytes int   files larger than this will be skipped
      --no-color                   turn off color for verbose output
      --no-banner                  suppress banner
      --redact                     redact secrets from logs and stdout
  -f, --report-format string       output format (json, csv, junit, sarif) (default "json")
  -r, --report-path string         report file
  -s, --source string              path to source (default ".")
  -v, --verbose                    show verbose output from scan

Use "gitleaks [command] --help" for more information about a command.
```

#### [Commands](https://github.com/gitleaks/gitleaks#commands)

**Create a baseline**

```shell
1. gitleaks detect --report-path gitleaks-report.json # This will save the report in a file called gitleaks-report.json
2. gitleaks detect --baseline-path gitleaks-report.json --report-path findings.json
```

-   After running the detect command with the --baseline-path parameter, report output (findings.json) will only contain
    new issues.
    **Detect**
-   used on developer machines and in CI environments.
-   gitleaks parses the output of a`git log -p`command
-   can scan files and directories by using the`--no-git`option.

```shell
gitleaks detect --source . --log-opts="--all commitA..commitB"
```

**Protect**

-   used to scan uncommitted changes in a git repo

-   can set the`--staged`flag to check for changes in commits that have been`git add`ed.
-   `--staged`flag should be used when running Gitleaks as a pre-commit.

```ini

```

#### Local | Pre-Commit Requirements | Proc

---

**SCRIPT | RUN** `Script File`: - File Name: **` .sh`**

**Baseline**

```bash
#!/bin/bash
gitleaks detect --baseline-path gitleaks-report.json --report-format sarif --report-path findings.sarif
```

**Detect**

```bash
#!/bin/bash
gitleaks detect --source --redeact . --log-opts="--all"
```

**Protect**

```bash
#!/bin/bash
gitleaks protect --verbose --redact --staged
```

**CONFIGURATION | RUN** `Script File`

-   Name:
-   Allow Multiple: N | Y
-   Store as File: N | Y
-   Package.json: `D:\Code\Code Institute\dash-and-do-github\package.json`
-   Command:
-   Scripts:
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
Node Opt:
Environ:
```

**Pre-Commit**: ``
Tags: [Releases · gitleaks/gitleaks (github.com)](https://github.com/gitleaks/gitleaks/releases)

```yml
repos:
    - repo: https://github.com/gitleaks/gitleaks
      rev: v8.16.1
      hooks:
          - id: gitleaks
            # Optional
            name: Detect hardcoded secrets
            description: Detect hardcoded secrets using Gitleaks
            entry: gitleaks protect --verbose --redact --staged
            language: golang
            pass_filenames: false
```

-   1. Auto-update the config to the latest repos' versions by executing`pre-commit autoupdate`
-   2. Install with`pre-commit install`
-   3. To disable the gitleaks pre-commit hook you can prepend`SKIP=gitleaks`to the commit command

#### CI

Action: [gitleaks/gitleaks-action: Protect your secrets using Gitleaks-Action (github.com)](https://github.com/gitleaks/gitleaks-action)
Getting
Started: [Stop Leaking Secrets — Getting Started with Gitleaks-Action (1/3) | by Zach | Gitleaks](https://blog.gitleaks.io/stop-leaking-secrets-getting-started-with-gitleaks-action-1-960de029853c)

```
name: gitleaks
on: [pull_request, push, workflow_dispatch]
jobs:
  scan:
    name: gitleaks
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      - uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          GITLEAKS_LICENSE: ${{ secrets.GITLEAKS_LICENSE}} # Only required for Organizations, not personal accounts.
```

##### Positive Flow

Gitleaks-Action does not find any secrets you will see the follow job log and job summary.
![[Pasted image 20230714103438.png]]

### Options

-

Docs: [gitleaks/gitleaks: Protect and discover secrets using Gitleaks 🔑 (github.com)](https://github.com/gitleaks/gitleaks)

-   Blog: https://blog.gitleaks.io/
-   ## GitHub:
    Main: [gitleaks/gitleaks: Protect and discover secrets using Gitleaks 🔑 (github.com)](https://github.com/gitleaks/gitleaks)
    -   Action:
-

Article: [Stop Leaking Secrets — Configuration (2/3) | by Zach | Gitleaks](https://blog.gitleaks.io/stop-leaking-secrets-configuration-2-3-aeed293b1fbf)

-   Perplexity:

## Final

> FLOW

### Steps

1. [x] . Installed GitLeaks (globally, on cmd line) (Chocolately)
2. [ ] . Manual run of Baseline `gitleaks detect --report-path gitleaks-report.json`
3. [ ] Subseuqnet run of Baseline `gitleaks detect --baseline-path gitleaks-report.json --report-path findings.json`
4. [ ] Create Scripts
    1. [ ] Detect
    2. [ ] Protect
5. Add to IDE Run Anything
6. .
7. .
8. .

### Repository

```dirtree

- /dash-and-do-github
	- /.github
		- /workflows
			- gitleaks.yml
	- /docs
		- /integration
			- /1-dev
				- gitleaks.md
	- /scripts
		- /1-dev
			- .sh
	- .gitleaksoignore
	- .gitleaks.toml
```

---

> .

---
