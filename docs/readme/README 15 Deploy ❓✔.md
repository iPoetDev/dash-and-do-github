-   [ ] Completed?
    -   Nearly ready?
-   [ ] Copy to Readme.md?
-   [ ] Removed meta-data

## 15. [Deploy](#deploy)

> SOLUTION: Host | Cloud | PaaS | Web App

-   [x] Criteria: LO-06-PASS | LO-6.1-PASS | LO-6.3-PASS ✅ 2023-07-06
-   [x] Sprint: 02
-   [ ] Completed? 🛫

### 15.1 [Git Commit Flow](#commit-flow)

> SOLUTION: Branching Strategy | Commit Plan | Review & Merge Gates Release Strategy

-   [x] Criteria: LO-06-PASS | LO-6.1-PASS | LO-6.3-PASS ✅ 2023-07-17
-   [x] Sprint: 02
-   [x] Completed? 🛫 2023-07-18

-   How the code get automatically pushed to Heroku by using Trunk-based long-lived release branches.

-   [ ] Choose Light or Dark version for final
        ![](15-1-Commit-light%201.png)

![](15-1-Commit-dark%201.png)
**`Diagram: Commit & Branch into Deployment`**

---

### 15.2. [GitHub Deployment Flow](#deploy-flow)

> SOLUTION: Host | Cloud | PaaS | DB Service

-   [x] Criteria: LO-06-PASS | LO-6.1-PASS | LO-6.3-PASS ✅ 2023-07-06
-   [ ] ADR: ADR000X: Choose a cloud hosting platform.
-   [ ] Sprint: 02
-   [x] Completed? 🛫 2023-07-18

#### 15.2.1 Deployment Branching Strategies

-   [ ] Choose Light or Dark version for final
        ![[Pasted image 20230718131542.png]]

![[Heroku Deploy - Git Branching Stategies.png]]
**`Diagram: From Build via Integration Branch Strategies into Heroku Apps`**

##### 15.2.1.1 Build/Dev Trunks

-   .

##### 15.2.1.2 Integration Trunk

-   .

##### 15.2.1.3 Deployment Trunk

-   .

---

### 15.3 [Heroku Integrations](#heroku-integrate)

#### 15.3.1 [Heroku Create App/Pipelines](# heroku-initialise)

> SOLUTION: Host | Cloud | PaaS | Web App | Deployment Setup

-   [x] Criteria: LO-06-PASS | LO-6.1-PASS | LO-6.3-PASS ✅ 2023-07-06
-   [x] Sprint: 02
-   [x] Completed? 🛫 2023-07-18

-   [ ] Light v Dark - Choose pre-submit (`Remove`)
        ![[15-Deploy-CreateApp-light.png]]

![[15-Deploy-CreateApp-dark.png]]
**`Diagram: Cloud Hosting Platform Config: Deployment Create Apps`**

##### 15.3.1.1. Workflow

-   Login to Heroku, and verify and MFA authenticated:
-   1. Choose a configuration context: **`Development`**, **`Staging`**, **`Production`.**
-   2: Create a new app and name it.
-   3: Choose a **Deployment** method. `GitHub` for `@PoetDev`
-   4: Connect to GitHub and search for the repository: `github/dash-and-do-github`
-   5: Connect to chosen Repository, select automatic deploy and verify.
-   6: **Buildpack**:
    -   Add _BuildPacks_ in correct order.
    -   Order sensitive, for good first run.
    -   [ ] Use built-in _BuildPacks_ for _Node.js_ and _Python_.
        -   [ ] 1st: `heroku/nodejs`
        -   [ ] 2nd: `heroku/python`
-   7: **Environmental Variables**:
    -   Heroku Config-Vars.
    -   Add Secrets:
        -   [ ] API Tokens.
        -   [ ] CSRF Token.
        -   [ ] DB Connection STRINGS.
        -   [ ] Other Secrets.
-   8 & 9: **PULL REQUEST**:
    -   On _GitHub_,
        -   Deploy to **`Heroku-^`** release trunk branch.
        -   Pull from **`main`** trunk branch.
        -   Via a Pull Request.

---

#### 15.3.2. [Local Git Service / IDE](#local-git)

> SOLUTION: Git Configuration | Keep a Changelog | Commit Messages

-   [x] Criteria: LO-05-Pass, LO-5.1-Pass, LO-5.1-Merit
-   [ ] ADR:
-   [x] Sprint: 02
-   [x] Completed? 2023-07-18

-   **IDE**: <ins>PyCharm</ins> | <ins>WebStorm</ins> configured with Git & GitHub account for Local development
    environment.
-   **Git App**: GitHub Desktop
-   **Git Version**: v2.40.0.windows.1

##### 15.3.2.1. Git Configuration

> PROJECT: Git Commit History | Commit Message Style & Format

-   [x] Completed
-   [x] Criteria: LO-5.1-PASS

-   **Approach**:
    -   _Commit / Push Style_: Merge Only, no Squash, no Rebase. Meets criteria for a
        -   `5.1: Use Git & GitHub for version control of a Full-Stack web application up to deployment, using commit messages to document the development process`
    -   _Linting_: No Linting as decided to rigid a constraint
    -   Instead: using a Side Notes plugin for IntelliJ IDE with pre-configured templates (see below)
-   _Aim_: For consistency, manual and by conventional.

##### 15.3.2.2. Keep A Changelog

> PROJECT: Log | Notable Changes | Human Readable | Semantic Versioning

-   **Link**: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
-   **Method**: Integrated Keep A Changelog format for add, update, remove _into commit messages_.
    -   Directly in the commit messages.
    -   Reduced efforts by not maintaining the `changelog.md`.
    -   Mostly adhered to Semantic Versioning approach.
    -   A minor adjustment was to put a double-digit index for each separate commit if several occurred on one day.
-   **Types**:
    -   `Add`for new features.
    -   `Update`for changes in existing functionality.
    -   `Deprecate`for soon-to-be removed features.
    -   `Remove`for now removed features.
    -   `Fix`for any bug fixes.
    -   `Secure`in case of vulnerabilities.

##### 15.3.2.3. Commit Message Templates

-   Influenced by [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

```text
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

-   _Template_: Adapted.

```text
type(scope): sub

Intent:
Tag:
Sprint: 01: Ends 23-7-14
Changelog: 2023-07-09 v00.00.001:01
- add:
- update:
- note:
  - .

optional: remove, deprecate, lint, secure, test
---
Agilelog:
- epic:

---
AssesmentLog:
- pass:
- merit:
- distinct:

```

-   **Subject**
    -   _type_: `feat`, `fix`, `refact`, `ui/design`, `data`, `mvs/app`, `deploy`, `proj`, `test`, `chore`, `config`, .
    -   _scope_: as appropriate, per context.
    -   _sub_: descriptor of commit.
-   _Intent_: Outline, additional information.
-   _Tags_: keywords.
-   _Sprint_: Align commit with sprint (add #Issue for GitHub link).
    -   Number: Sprint Sequence.
    -   Ends: End of Sprint date.
-   _Changelog_:
    -   Versioning:
        -   _Date_ (YY-MM-DD).
        -   _SemVer_: v00.00.00:001 (_Major_._Minor_._Patch_:_Daily-Commit-Id_)
    -   _`Add`_: Adding new files.
    -   _`Update`_: Changes to files.
    -   _`Note`_: Additional context.
    -   Optional: `Remove`, `Lint`, `Tested`,
-   **AgileLog**:
    -   **Epic**: Epic Name.
    -   Optional: _Story_, _Acceptance_,
-   **AssessmentLog**: Align commit with academic criteria.
    -   **Pass**: _Format_: `LO-{ident}`
    -   **Merit**: _Format_: `LO-{ident}` | `M-ShortName`
        **- Distinct**: _Format_: `D-ShortName`

---

#### 15.3.3. [Deployment Environment](#deploy-env)

> SOLUTION: Cloud Hosting | Platform as a Service | Database as a Service

##### 15.3.3.1 Platform as a Service (<ins>PaaS</ins>)

> SOLUTION: Cloud Hosting | Platform as a Service

-   [ ] Criteria:
-   [ ] ADR:
-   [x] Sprint: 02
-   [x] Completed? 2023-07-18

**CLOUD PLATFORM**

-   **Heroku** is the _CHOSEN_ cloud environment for deployment.
    -   Deploy a static web page off every commit.
    -   Once the commit is built, then deploys the new website and pushes to hosted domain URI.
-   _Heroku_ is the hosted domain URI and service.

![Source: Wikimedia.com](Heroku.png)

##### 15.3.3.2: Database as a Service (<ins>DBaaS</ins>)

> SOLUTION: Managed Database | Relational Database Manage Services | Database as a Service | Datastore Configuration |
> Data Schema | Data Model

-   [x] Criteria: LO-2-DataModel-Pass, LO-2.5-Merit, LO-Schema-Merit, LO-Configuration-Merit, LO-Well Structured
        Data-Distinction, LO-Datastore-Config-Distinction
-   [ ] ADR:
-   [x] Sprint: 02
-   [x] Completed? 2023-07-18

**CLOUD DATABASE**

-   **PostgreSQL** is the _SELECTED_ database & backing service technologies.
-   **ElephantSQL** is the _SELECTED_ managed database provider for …:
    -   _Service_: Remote cloud based database service.
    -   _Type_: Relational Database Management Service.
    -   _Language_: SQL

![Source: Wikimedia.com](Logo%20Postgresql_elephant.png)

---

### 15.4. [App Web URI](#app-url): Dash and Do GitHub (Manager)

> SOLUTION: : Live App | App Name | By-Line

-   [x] Criteria: LO-6.1-Pass, LO-6.3-Pass
-   [x] Sprint: 02
-   [x] Completed? 2023-07-18

-   **Plain Text** (Copy):

```text
https://dash-and-do-github.herokuapp.com/
```

-   **Link\***: [https://dash-and-do-github.herokuapp.com/](https://dash-and-do-github/herokuapp.com/')
-   **App Name**: <ins>Dash & Do GitHub (Manager)</ins>
-   **By Line**: <ins>Managing your GitHub as a Portfolio</ins>

---

> .

---
