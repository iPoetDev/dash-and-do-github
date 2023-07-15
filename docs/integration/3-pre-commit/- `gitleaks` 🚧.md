-   Detect hardcoded secrets using Gitleaks

# Source

-   Pre-Commit Repo [URL]:
-   Hook ID
    -   ID: `gitleaks`
-   Category | Intent: Static Application Security Testing (SAST)
    -   [SAST Tools & Testing: How Does it Work and Why Do You Need it? | Snyk](https://snyk.io/learn/application-security/static-application-security-testing/?utm_medium=paid-search&utm_source=google&utm_campaign=nb_lg_sast&utm_content=sast-topic&utm_term=sast%20testing&gclid=Cj0KCQjwkqSlBhDaARIsAFJANkjce_iW05LYNobpL-Fw91a6D21p3wRt0fjqCUgzJ6bKDOUOxobqh4YaAtvrEALw_wcB)
-   Description:
    -   Gitleaks is a SAST tool for**detecting**and**preventing**hardcoded secrets like passwords, api keys, and tokens in
        git repos.
    -   Gitleaks is an**easy-to-use, all-in-one solution**for detecting secrets, past or present, in your code

## Fetch

```yaml
[gitleaks_8.17.0_windows_arm64.zip (github.com)](https://github.com/gitleaks/gitleaks/releases/download/v8.17.0/gitleaks_8.17.0_windows_arm64.zip)
```

## Library

-   [ ] Web: [Gitleaks](https://gitleaks.io/)
-   [ ] Repo: ### [github.com/zricethezav/gitleaks](https://github.com/zricethezav/gitleaks)
-   [ ]
    Source: [gitleaks_8.17.0_windows_arm64.zip (github.com)](https://github.com/gitleaks/gitleaks/releases/download/v8.17.0/gitleaks_8.17.0_windows_arm64.zip)
-   [ ] Config: [gitleaks config (github.com)](https://github.com/zricethezav/gitleaks/blob/master/config/gitleaks.toml)

#### Config

```python
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

#### Baseline

```
gitleaks detect --report-path gitleaks-report.json
# This will save the report in a file called gitleaks-report.json
```

##### [Detect](https://github.com/gitleaks/gitleaks#detect)

```
gitleaks detect --source . --log-opts="--all commitA..commitB"
```

```
git log -p
```

: [`git log -p`](https://git-scm.com/docs/git-log#_generating_patch_text_with_p) [generates patches](https://git-scm.com/docs/git-log#_generating_patch_text_with_p)
which gitleaks will use to detect secrets.

##### [Protect](https://github.com/gitleaks/gitleaks#protect)

#### `.gitleaksignore`

Can ignore specific findings by creating a`.gitleaksignore`file at the root of your repo.

-   In release v8.10.0 Gitleaks added a`Fingerprint`value to the Gitleaks report.
-   Each leak, or finding, has a Fingerprint that uniquely identifies a secret.
-   Add this fingerprint to the`.gitleaksignore`file to ignore that specific secret.
-   See Gitleaks'[.gitleaksignore](https://github.com/zricethezav/gitleaks/blob/master/.gitleaksignore)for an example.
    Note: this feature is experimental and is subject to change in the future.

#### Exit

```bash
0 - no leaks present
1 - leaks or error encountered
126 - unknown flag
```

## Config

-   [ ] Create a` .pre-commit-config.yaml` in root of repository.
-   [ ] Commit `yaml` repository.
-   [ ] Prepare for run by adding hook's
    -   [ ]
        Repository: `- repo: https://github.com/gitleaks/gitleaks`: [gitleaks/gitleaks: Protect and discover secrets using Gitleaks 🔑 (github.com)](https://github.com/gitleaks/gitleaks)
    -   [ ] Revision: `rev` : `  8.17.0  `
        -   [ ] v8.17.0 - [v8.17.0 Latest (github.com)](https://github.com/gitleaks/gitleaks/releases/tag/v8.17.0)
        -   Select/Use the ref you want to point at
    -   [ ] Hooks: Detect hardcoded secrets using Gitleaks
        -   [ ] Id: `id gitleaks`

```yaml
- repo: https://github.com/gitleaks/gitleaks
  rev: v8.17.0
  hooks:
      - id: gitleak
```

-   [ ] Copy into `.pre-commit-configuration.yaml`

## Install

-   [x] Installed: WinGetUI: Scoop
-   Or ...

```bash
# From Source
git clone https://github.com/gitleaks/gitleaks.git
cd gitleaks
make build
```

## Run

```bash


```
