- [ ] Completed?
- [ ] ADR Completed?
- [ ] Well formatted?

## 10. [Build](#build)

> SOLUTION: Branch Strategy | Version Control | Commits | Changelog | Pre-Commit | Tooling

- [ ] Criteria:
- [ ] Completed? 🛫

### 10.1. [Branching](#branches)

> SOLUTION: Epic-Flow | Heroku-Flow | Trunk-Based Development

- [ ] Criteria:
- [ ] ADR: ADR000X Select a Branching Strategy
- [ ] Completed? 🛫

- **Style**: Trunk Based Development (i.e. long lived branches for dedicated intents).
- **Epic-**: *Development Trunks*: Limited to number of epics, push from local to remote/origin.
- **Main**: *Integration Trunk*, CI Pull Request target from EPIC based branches into Main branch. No push from local to
  origin/main. Protected branch. Review Gate.
- **Heroku-**: *Deployment Trunks*, CI Pull Request target from Main into Heroku-* branches*.

#### 10.1.1. [Epic-Flow](#build-epic-flow)

> SOLUTION: #Build | Diagram | Workflow | Build | Commit | Branch

- [ ] Criteria:
- [ ] Completed? 🛫

-
    1. Pull Request from ``local/epic-*`` (the local) to ``origin/epic-*``(the remote) branch for **MANUAL COMMIT & PUSH

2. Protect ``origin/main`` & `origin/heroku` branch from changes or having anything pushed
3. Merge from ``epic-*`` to ``main`` branch for each code review, CI actions, and code quality checks (inc, pre-commits)
4. From `raw/new code` -> `linted code` -> `manually tested` -> `locally` ...?
5. Use **Trunk based development** from the **``local/epic-*``** branch to  **``origin/epic-*``** branch
    - Commit Style: Merge/Push to **``local/epic-*`` for development codebase.
    - Once the GitHub CI Apps (above) have passed all checks.
    - Tag|Label Code ready for **versioning/changelogging/pre-integration/commit**: Push to ``origin/epic-*`` on remote.

- [ ] `ADD GIT FLOW DIAGRAM`

#### 10.1.2. Review-Flow

> SOLUTION: #Integration | Diagram | Workflow | Review Gate

- [ ] Criteria:
- [ ] Completed? 🛫

1. Pull Request from ``epic-*`` to ``main`` branch for **MANUAL INTEGRATION**
2. Protect ``main`` branch from changes or having anything pushed
3. Merge from ``epic-*`` to ``main`` branch for each code review, CI actions, and code quality checks (inc, AI Agent
   prompts)
4.

From `raw/new code` -> `linted code` -> `manually tested` -> `locally running` -> `PR#1` -> `Merge to Main` ->  `GitHub CI `

5. Use **Trunk based development** from the **``epic-*``** branch to **``main``** branch
    - Commit Style: Merge/Push to **``epic-*``** for development codebase.
    - Once the GitHub CI Apps (above) have passed all checks.
    - Tag|Label Code ready for **integration**: Push to **``main``**

- [ ] `ADD GIT FLOW DIAGRAM`

#### 10.1.3. Deploy-Flow

> SOLUTION: #Deployment | Diagram | Workflow

- [ ] Criteria
- [ ] Completed?

1. Pull Request from ``main`` to ``heroku`` branch for **AUTOMATED DEPLOYMENT**
2. Protect ``heroku`` branch from changes or having anything pushed
3. Merge from ``main`` to ``heroku`` branch for each release
4.

From `raw/new code` -> `linted code` -> `manually tested` -> `locally running` -> `PR#1` -> `Merge to Heroku` ->  `Heroku Automated`

5. Use **Trunk based development** from the ``main`` branch to ``heroku`` branch
    - Commit Style: Push to ``main`` for development codebase.
    - Once the GitHub CI Apps (above) have passed all checks.
    - Tag Code ready for deployment: Push to ``heroku``
    - Deployment is automated via Heroku's app deployment
    - By not having automated deployment on ```main```, there is no failed deployment noise on ``main`` branch and in
      the
      logs.


- [ ] `ADD GIT FLOW DIAGRAM`

---

### 10.2. Commit

> SOLUTION: Style | Template | Convention

- [ ] *<small>Criteria: LO-05-PASS | LO-5.1-PASS | LO-5.1. 2-PASS | LO-5.1-MERIT</small>*
- [ ] ADR:
- [ ] Completed?

- ADR000X: Select a Commit Message Style: Conventional v Changelog Driven
    - Conventional Commits
        - Source: https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13
    - Changelog Commits:
        - .
    - Custom Combined: An adapted merge of both styles.
        - See proposed below.

```git:
<agile><type>(<opt scope>): <subject>

Sprint: #  (Days:, End: )

Changelog: 2023-07-00 v0.0.0:00
<changelog body>
#add:
#mutate:
#remove:

Agilelog:
<agile tool items>
#epic
#story
#accept

---
<opt footer>
BREAKING CHANGE: <opt breaking>
Co-authored By: <name>
```

***Example***: **`Commit Template: Short`**

#### 10.2.1. Types

SOLUTION: Conventional Commits | [Source: Gist](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13) |
Pre-commit Hook

- [ ] Criteria
- [ ] **ADR**: [ADR000X - Implement a Manual Template or Enforce Pre-Commit Hook]
- [ ] IDE Configured?
- [ ] Completed?

- Relevant changes
    - `epic` Commits, that marks a start of a new epic branch <sup>authors own</sup>
    - `feat` Commits, that adds a new feature
    - `fix` Commits, that fixes a bug
- `refactor` Commits, that rewrite/restructure your code, however does not change any behaviour
    - `perf` Commits are special`refactor`commits, that improve performance
    - `revert` Commits that revert a refactor due to impact on behaviour.
- `style` Commits, that do not affect the meaning (white-space, formatting, missing semi-colons, etc)
- `test` Commits, that add missing tests or correcting existing tests
- `docs` Commits, that affect documentation only
- `build` Commits, that affect build components like build tool, ci pipeline, dependencies, project version, ...
    - `bump` Commits, that bump the software version/changelog by a **`major`.`minor`** version.
- `proj` Commits, that affect agile project management artefacts, likes epics, stories, acceptance
    - `agile/sprint`: Commits that mark a start of an agile activity, creation of a sprint
    - `agile/story` Commits that signal a user story activity, if appropriate
- `ops` Commits, that affect operational components like infrastructure, deployment, backup, recovery, ...
- `chore` Miscellaneous commits e.g. modifying`.gitignore`

- [ ] `CONFIGURE IDE`
- [ ] `PRACTICE IN IDE`
- [ ] `DEVELOP A COMMIT FLOW`

#### 10.2.2 Scopes

> SOLUTION: Conventional Commits | [Source: Gist](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13) |
> Optional

- [ ] Criteria
- [ ] **ADR**: [ADR000X - Implement a Manual Template or Enforce Pre-Commit Hook]()
- [ ] IDE Configured?
- [ ] Completed?

- `PROJECT`
- `SOLUTION`

### 10.3. [Pre-commit](#pre-commit)

> SOLUTION: Pre-Commits

- [ ] Criteria
- [ ] **ADR:**
- [ ] Completed? 🛫

- .
- .

### 10.4. [Tooling](#tooling)

> SOLUTION: Tooling | IDE | Languages | Extensions | AI Tools | GitHub Apps

- [ ] Criteria
- [ ] Completed? 🛫

#### 10.4.1. [Languages](#)

> SOLUTION: Semantic Hypertext | Style | Client Interactivity | Backend | Framework

- [ ] Criteria
- [ ] ADR:
- [ ] Completed? 🛫

| Language   | Environment     | Local | Remote | Extensions       | VERSION   | ADR | Use Case                                           |     |     |     |     |     |     |     |     |
|------------|-----------------|-------|--------|------------------|-----------|-----|----------------------------------------------------|-----|-----|-----|-----|-----|-----|-----|-----|
| HTML       | Browser, Client | Yes   | Yes    | Yes - HTMX[1]    | v5        |     | Front End UI, Hypermedia API[2]                    |     |     |     |     |     |     |     |     |
| CSS        | Browser, Client | Yes   | Yes    | No - `below`[3]  | v3        |     | Style, Responsiveness, Layout (Front End UI)       |     |     |     |     |     |     |     |     |
| JavaScript | Browser, Client | Yes   | Yes    | No - Native[4]   | v5        |     | Client Side Interaction (Front End UI)[5]          |     |     |     |     |     |     |     |     |
| Python     | OOP, Server     | Yes   | Yes    | Yes - `below`[6] | v 3.11.04 |     | Object Orientated Programming, Server Custom Logic |     |     |     |     |     |     |     |     |

- [ ] <small>Checklist:  [ ] Add Links in WebStorm [ ] Add superscript tag in Webstorm</small>

- 1: Use a JavaScript library to extend html attributed: [HTMX](https://htmx.org)
-

2: [Hypermedia API](https://htmx.org/essays/hypermedia-apis-vs-data-apis/) | [When to use Hypermedia](https://htmx.org/essays/when-to-use-hypermedia/)

- 3: ADR: Select a modern CSS utility framework
- 4: Constraint `JavaScript npm` 3rd party packages as dependencies in the Front End to non-network/server
  functionality.
- 5: ADR: Constraint JavaScript to Client-side only Interactivity
- 6: Django is a proscribed web application framework.

##### 10.4.1.1. Libraries, Framework, Component

SOLUTION: Library | API | Framework | Component

- [ ] Criteria
- [ ] ADR:
- [ ] Completed? 🛫

| Library, Module, Package | Environment                      | Install Local | Install Remote | Language (Package Lang) | Version  | ADR | Use Cases                                            |
|--------------------------|----------------------------------|---------------|----------------|-------------------------|----------|-----|------------------------------------------------------|
| HTMX                     | Browser, CDN, Client             | ?             | ?              | HTML (JavaScript)       | v 1.9. 2 |     | Hypermedia API, Network Data (Front End DataOps)     |
| Boostrap, Tailwinds      | Browser, CDN, Client             | ?             | ?              | CSS                     | ?        | ?   | CSS Utility Framework, CSS Components (Front-End UI) |
| Django                   | Web Application, Server          | Yes           | Yes            | Python                  | v 4.2    |     | Web Applications, Templates, ORM & Database,         |
| Django REST              | Web API, JSON-RPC, Server        | Yes           | Yes            | Python                  | v 3.14.0 |     | For GitHub API processing                            |
| Postgres                 | Database, Managed Service, Cloud | No            | Yes            | Django, SQL (Python)    |          |     |                                                      |
| SQLite                   | Database, Local,                 | Yes           | No             | Django, SQL (Python)    |          |     | Included in the Django Data/ORM                      |
|                          |                                  |               |                |                         |          |     |                                                      |

- [ ] <small>Checklist:  [ ] Add Links in WebStorm [ ] Add superscript tag in Webstorm</small>

#### 10.4.2. [IDE & Extensions](#ide-editors)

> SOLUTION: Editor | Extensions

- [ ] Criteria
- [ ] Completed? 🛫

| Editor, Plugins | Vendor    | Workflow | Key Plugins[7] | Version         | ADR | Editor Use                         | Plugin Use |
|-----------------|-----------|----------|----------------|-----------------|-----|------------------------------------|------------|
| PyCharm         | JetBrains | Python   | [8]            | 2023.01. 03 Pro |     | Test, Lint, Format, Django         |            |
| Webstorm        | JetBrains | Web      | [8]            | 2023.01. 03 Pro |     | HTML, JS, CSS, Test, Lint, Format, |            |
| DataGrip        | JetBrains | Data     | [8]            | 2023.01. 03 Pro |     | Database, Model                    |            |
| Aqua            | JetBrains | Browser  | [8],[9]        | 2023.01. 03 Pro |     | Browser Testing                    |            |
|                 |           |          |                |                 |     |                                    |            |
|                 |           |          |                |                 |     |                                    |            |
|                 |           |          |                |                 |     |                                    |            |
|                 |           |          |                |                 |     |                                    |            |
|                 |           |          |                |                 |     |                                    |            |
|                 |           |          |                |                 |     |                                    |            |
|                 |           |          |                |                 |     |                                    |            |
|                 |           |          |                |                 |     |                                    |            |

- [ ] <small>Checklist:  [ ] Add Links in WebStorm [ ] Add superscript tag in Webstorm</small>

- 8:
- 9.:

#### 10.4.3. [Code Linters](#linters)

> SOLUTION: Lint | Command Lines | Static Analysis | Code Formatting

- [ ] Criteria
- [ ] Completed? 🛫

- .
- .

#### 10.4.4. [AI Tools](#ai-tools)

> SOLUTION: Generation | Refactoring | Auto-completed | Test Generation

- [ ] Criteria
- [ ] Completed? 🛫

- .
- .

#### 10.4.5. [GitHub Apps/CI](#ci-apps)

> SOLUTION: CI/Pull Requests: Review: Refactoring | Format | Style | Checks

- [ ] Criteria
- [ ] Completed? 🛫

- .
- .

---
> #DO #BUILD
---
