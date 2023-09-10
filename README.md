# dash-and-do-github

> Dash &amp; Do GithHub Manager: A Dashboard (Reporting) and Do (Act or Automate) for GitHub Repositories

# 1.0 Introduction

---

[![JavaScript Style Guide](https://img.shields.io/badge/code_style-standard-brightgreen.svg)](https://standardjs.com)
[![wakatime](https://wakatime.com/badge/user/2027c27d-0bab-4d7c-bfed-5d0b21285657/project/62c65141-830a-41c9-af92-98a9302fa984.svg)](https://wakatime.com/badge/user/2027c27d-0bab-4d7c-bfed-5d0b21285657/project/62c65141-830a-41c9-af92-98a9302fa984)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![GitLeak protection ](/res/badges/gitleaks-badge.svg)](https://github.com/gitleaks/gitleaks)

-   Share [WakaTime:](https://wakatime.com/@ipoetdev/projects/forvkqvyji)

---

## 1.1. [Goals](#goals)

### 1.1.1 [App Goals](#app-goals)

- To *manage a personal developer’s GitHub account* as a whole portfolio service, by connecting, and disconnecting, the web service with a developer GitHub account (maximum of 1 GitHub account).
- Use a *Report and Inform Dashboard*  for the developer on the state of their repositories under a single glance on a single pane of glass pattern via a Dashboard design. i.e. **The Dash, aka Dash & Inform.**
- Use a *To-do and Action task manager* for the developer in response to the state of their repositories so that they bulk edit on a single pane of glass pattern via a To Do and Tasker design. I.e. **The Do, aka Do & Act.**

### 1.1.2 [Project Goals](#project-goals)

-   #Client/Assessor #RFP To build a full-stack site based on business logic used to control a centrally owned dataset.
-   #Client/Assessor #RFP To set up an authentication mechanism and provide role-based access to the site's data or other
    activities based on the dataset.
-   #Solution To integrate GitHub with the Web App via GitHub social login and authentication tokens, with full lifecycle
    account management, via onboarding and offboarding of this social login.
-   #Solution To authorized and grant permissions to the web app, as a 3rd party` service|integration`, to one's own
    GitHub account or, maybe, a secondary one.
-   #Solution To use GitHub API to perform the following:
    -   Analyse and graphically report on Languages used.
    -   Analyse and graphically report on File Types used.
    -   Analyse and collated the labels used across all accounts.
    -   CRUD and manipulate Issue Labels in bulk, centrally and apply to `all|selected` repositories in bulk.
    -   Copy and Apply a central store of common file types to to `all|selected` repositories in bulk.
-   #Project To use agile methodologies and tooling to deliver the #Solution to the #Client/Assessor: **<ins>The Code
    Institute</ins>.

***

## 1.2. [Live App](#live-app)

-   To see the live app: https://{{app-slug}}/herokuapp.com

-   _APP/SERVICE NAME_: <ins>DASH &amp; DO GH MANAGER</ins>
-   _PROJECT REPO NAME_: `dash-and-do-for-github`
-   _REPOSITORY URL_: https://github.com/ipoetdev/dash-and-do-for-github

---

## 1.3. [App Visual](#app-visuals)

![Image]()

[`amiresponsive.co.uk/`](https://amiresponsive.co.uk/ 'Am I Responsive: amiresponsive.co. uk/') | `URI: AmIResponsive`

***
>
***

## 2. [Problem Statement](#problem-solve)

### 2.1. [Domain Driven Scenarios](#domain-scenarios)

A. **GitHub As a Portfolio?**

> > A question that occurs: _how can a developer treat and tailor his whole GitHub as a single sharable artefact in their portfolio and as a basis for his portfolio; and share to outside, or not GitHub account holders, and maximise the value of their GitHub account without given 3rd party access or having another crawl across their repositories in multiple pages and clicks._

B.

> > A question that occurs: _how can a potential employer inspect a prospective developer's GitHub at a glance, with meaningful analytics and high-level summary data?_

C.

> > A question that occurs: _how can, based on the prior question, can a developer keep track of the standard, conventional and best practices, on a per repository or bulk repository basis, with cross cutting concerns? Can he keep a in context to-do repository management list of common or standard tasks to maintain and manage his account over numerous repositories (i.e. greater than 5)._

D.

> > A question that occurs: _how can a developer apply GitHub features, which are manually created (e.g. labels, custom project fields), uniformly across more than two repositories and save time and effort on duplicative, repetitive and non-DRY iterative efforts. Such efforts have the challenge of lack of consistency and not being standard/best practice
> > driven._

E.

> > A question that occurs: _how can a developer apply GitHub best practices, like conventions and common files (examples of which are documented here), uniformly across more than two repositories and save time and effort on duplicative, repetitive and iterative file generation efforts. These generation efforts done once and repeated many times from a central source._

### 2.2. [Problem Concern](#problem-concern)

-   A GitHub account is a partially DRY system, and this is a dis-benefit to the author-developer.
-   A GitHub repository is a partially DRY system, and this is a dis-benefit to the author-developer.
-   A GitHub account is intentionally a fully adaptable and flexible platform; it is aimed to meet the widest number of use cases, target audiences via its universally open design.
    -   This lead to several user driven tasks to be manual, repetitive and not very good for DRY iteration.
    -   Such as:
        1.   Label creation
        2.   Issue Templates, in part
        3.   GitHub Common Files (see below)
-   A GitHub account has no central store for certain artefacts that allow for one time editing and the more than one repository deployment, over a group of repositories. Such effort to duplicate and apply these programmatically.
-   A GitHub account does have selected analytics on a account or profile level basis. However, any proposed solution is looking to extend these analytics to drive an better "at a glance" overview.
-   There are no, as yet known by the author-developer, bulk editing features across two or more repositories. Such a feature would allow for improved user management experience in the application of conventions, standards and best practices.

### 2.3. [Developer Motivations](#motivations)

-   The author-developer needs a problem in search of a solution for an academic assignment, and as such is extending the
    GitHub concepts where they see dis-benefits or constraints in functionality.
-   The author-developer is sticking to what they know in a familiar domain, GitHub, and is seeking to deepen their
    knowledge and capacity in this platform. This they seek to showcase this in this project.

---
>
***

## 3. [Project](#project)

### 3.1. [Project Brief](#brief)

_To build a Full-Stack site based on business logic used to control a centrally owned dataset._

_Additionally, need to set up an authentication mechanism and provide role-based access to the site's data or other
activities based on the dataset._

---

### 3.2. [Project Methodology](#methodology)

-   [x] **ADR**: [ADR000X - Choose a project management and delivery methodology]()

-   **Chosen**: Agile Methodology
-   **Why**: Proscribed by the Client: The Code Institute as part of their software project portfolio development series
    in portfolio project 4: Full Stack Toolkit
-   _Approach_:
    -  Breaks project into iterative phases (i.e. sprints).
    -  Emphasizes continuous adaption, adjustment to change, improvement, releases and customer feedback.
    -  It's a cycle of flexible planning, execution and evaluation.
    -  Is customised for a solo developer.
- _Is not_:
    -  A collaborative approach for this solo project.

#### 3.2.1 Project Tooling: Zube.io

- The author/developer choose against using GitHub Projects for Agile Management, as it required a long of imposition of agile principles to be configured correctly.
- The author/developer choose for using a 3rd party Project Management Tool: [zube.io](https://zube.io/).
    - Has [Agile Components](https://zube.io/docs/components).
    - [GitHub Issues Can be Agile if You Do it Right | The Zube Blog](https://zube.io/blog/agile-project-management-workflow-for-github-issues/)
    - Installable via [GitHub Marketplace](https://github.com/marketplace/zube)
    - Is a stand-alone Agile Project Management tool.
    - Integrates and synchronises with GitHub Issues.
    - Organises and uses a Kanban Board and/or Sprint Boards
    - Defines Agile Epics and Scrum Style sprints
    - Is Free (up to 4 Users)
    - Utilises GitHub account or Gmail for social access login.
- The disadvantage (for assessment) is that:
    - Requires either a known Gmail account or a known GitHub to sign up.
    - By constraint, there is no common inbox for assessors to issue an onboarding email.
    - Assessors must be anonymous.
    - Requires a standalone temporary email account with a supplied username and password i.e. a proxy account.
    - This proxy guarantees the anonymity of the assessment process for the assessor.
    - Requires testing and testing before deadline.

Other benefits, that capitalises on prior effort by the author, was

- Provides a separate UI for managing the GitHub repository, issues, issues, milestones, templates that synchronises with GitHub.
- Can bulk edit issues and other features, with improved global effort and control.
- Integration of GitHub Issue Templates (see [3.3 Agile Artefacts](README.md#artefacts) below.)
- Definition of a End to End Workflow
    - ![](docs/assets/img-readme/3-2-1_zube-kanban-workflow.png)
- Has an inbuilt priorities over the setup of the GitHub Projects from blank slate
    - Blocker (P1), Critical (P2), Major (P3), Minor (P4), Trivial (P5)
- Uses a points system (Criteria: Merit: 1.5: User Stories, Points & Timeboxes prioritisations)
    - Uses a Fibonacci System (0,1,2,4,5,8,13). For purposes of this project, 13 is the max.
    - Employs a relative sizing, [see here: Practical Fibonacci: A Beginner's Guide to Relative Sizing | Scrum.org](https://www.scrum.org/resources/blog/practical-fibonacci-beginners-guide-relative-sizing)

#### 3.2.2 Relative Points

These relative points are a story point matrix of *Certainty/Risk* (y-axis) against *Effort/Complexity* (x axis), and uses *Amount of Work* labels to categorise the scoring

![](docs/assets/img-readme/3-2-2_storypoint-matrix.png)
`Source`: [How to Begin Story Point Estimating](https://joshmartindev.com/2022/04/29/how-to-begin-story-point-estimating/)

-  **Zero Points**: No Effort Required, or there is some effort required, but there is no business value delivered, so no Points are accumulated for doing the work.
    -  <ins>0 pts: NO EFFORT: Very Easy (0) || No Uncertainty (0)</ins>
-  **1-2 Points**: Developer feel they understand most requirements
    Developers consider it relatively easy, probably smallest items in the Sprint, and mostly likely completed in one day.
    -  <ins>1 pts: EXTRA SMALL: Very Easy (1) || No Uncertainty (1)</ins>
    -  <ins>2 pts: SMALL: Very Easy (1) || Little Uncertainty (2)</ins>
    -  <ins>2 pts: SMALL: Medium (2) || No Uncertainty (1)</ins>
- **3 Points**: Developer(s) have done this a lot; knows what needs to be done.
    There may be a few extra steps. It's doubtful that extra research will be need.
    - <ins>3 pts: AVERAGE: Medium (3) || No Uncertainty (1)</ins>
    - <ins>3 pts: AVERAGE: Very Easy (1) || Little Uncertainty (3)</ins>
- **5 Points**: This is complex work, or Developers don't do this very often.
    Most Developers will need assistance from someone else. This is probably one of the largest items that can be completed within a Sprint.
    - <ins>5 pts: LARGE: Medium (5) || No Uncertainty (1)</ins>
    - <ins>5 pts: LARGE: Easy, Low Complexity (1) || Some Uncertainty (5)</ins>
-  **8 Points**: Is going to take some time and research. Will take more than 1 developer to complete within two weeks. Plus: Developer need to make several assumptions that increase the risk. Likely to impact getting it Done.
    - <ins>8 pts: EXTRA LARGE: Hard Complexity (8) || No Uncertainty (1)</ins>
    - <ins>8 pts: LARGE: Easy, Low Complexity (1) || High Uncertainty (8)</ins>
- **13 Points**: Is a complex piece of work with lots of unknowns.
    - Requires multiple assumptions to size. It is too much to complete in one Sprint. Instead, split this into multiple Items that can be completed independently.
    - <ins>13 pts: WARNING: Hard Complexity (13) ||  Low Uncertainty (1)</ins>
    - <ins>13 WARNING: Easy, Low Complexity (1) || High Uncertainty (13)</ins>

***
>
---

### 3.3. [Agile Artefacts](#artefacts)

- Delivered by [GitHub Issue Template selector](https://github.com/iPoetDev/dash-and-do-github/issues/new/choose): and
  Zube.io.

-   WORKFLOW: Flows are processes and step wise tutorials to complete a task/goal.
    - [00 DEFINE: Document | Readme](https://github.com/iPoetDev/dash-and-do-github/issues/new?assignees=&labels=&projects=&template=00-define--document---readme.md&title=):
        - Readme Development.
        - Document | Effort | Concept.
    -  [00 REQUIRE: Product | Agile Specification](https://github.com/iPoetDev/dash-and-do-github/issues/new?assignees=iPoetDev&labels=Kind%3A+Define%2C+Kind%3A+Refine&projects=&template=00-require--product---agile-specification.md&title=DEFINE+%3A%3A+)
        - Product.
        - Agile Specification.
    -  [00 FLOW: Workflow | Process | Checklist](https://github.com/iPoetDev/dash-and-do-github/issues/new?assignees=iPoetDev&labels=Deadline%3A+Oct+21%2C+Mentor%3A+1st+Review%3A+Aug+07%2C+Mentor%3A+2nd+Review%3A+%3A+Sep+04%2C+Mentor%3A+3rd+Review%3A+Oct+02%2C+Project+%3A+Inventory&projects=&template=00-flow--workflow---process---checklist.md&title=FLOW+%3A%3A+)
        - Best Practice.
        - Strategic or Tactical Workflow.
-   SPRINTS: New Sprint for sprint planning/tracking.
    -   [00 SPRINT: Plan & Report](https://github.com/iPoetDev/dash-and-do-github/issues/new?assignees=iPoetDev&labels=Kind%3A+Sprint%2C+Plan+%3A+Horizon%2C+Plan+%3A+Sprint%2C+Sprint+01+%3A+The+First+Config%2C+Sprint+02+%3A+Arch+n+Deploy%2C+W%2FE%3A+Aug+04%2C+W%2FE%3A+Aug+11%2C+W%2FE%3A+Aug+18%2C+W%2FE%3A+Aug+25%2C+W%2FE%3A+Jul+14%2C+W%2FE%3A+Jul+21%2C+W%2FE%3A+Jul+28%2C+W%2FE%3A+Oct+07%2C+W%2FE%3A+Oct+14%2C+W%2FE%3A+Oct+21%2C+W%2FE%3A+Sep+08%2C+W%2FE%3A+Sep+15%2C+W%2FE%3A+Sep+22%2C+W%2FE%3A+Sep+29&projects=&template=00-sprint--plan---report.md&title=%5BSPRINT%5D++%3A%3A+)
-   ADR: _Any Decision Record_ <sup>[1]</sup>
    - [01: ADR Full](https://github.com/iPoetDev/dash-and-do-github/issues/new?assignees=iPoetDev&labels=&projects=&template=01--adr-full.md&title=ADR000%3F+%3A%3A+)
        - ADR Record - Full Tracing of Why & Motivations
        - Key Decisions and Derivations
    -   [02 ADR-Y-Statement]().
        - ADR Short Form:
        - Problems Statements and Choices
- AGILE:
    -   EPIC:
        -   [03 EPIC: Feature | Infrastructure](https://github.com/iPoetDev/dash-and-do-github/issues/new?assignees=iPoetDev&labels=&projects=&template=03-epic--feature---infrastructure.md&title=EPIC000%3F+%3A%3A++)
            - A chapter of deliverable work.
            - Comprised of Features, User Stories & Enabler Tasks
    -   FEATURE:
        -   [04 FEAT: Feature | Component](https://github.com/iPoetDev/dash-and-do-github/issues/new?assignees=iPoetDev&labels=&projects=&template=04-feat--feature---component.md&title=FEAT+%3A%3A+)
            - RFC: An Epic's Feature.
            - An Epic's Component.
    -   USER STORY & ACCEPTANCE:
        -   [05 STORY: User Story | Use Case](https://github.com/iPoetDev/dash-and-do-github/issues/new?assignees=iPoetDev&labels=&projects=&template=05-story--user-story----use-case.md&title=STORY-000%3F+%3A%3A+)
            - An Epic's Task
            - Enabling Task linked to a Feature | Component
        - [06 ACCEPT: User Acceptance Criteria](https://github.com/iPoetDev/dash-and-do-github/issues/new?assignees=iPoetDev&labels=&projects=&template=06-accept--user-acceptance-criteria.md&title=UAC-000%3F+%3A%3A)
            - UAC: Scenario, Feature
            - Given ... When ... Then
    -   QUALITY & TESTING:
        -   [07 CHECK: Static Analysis](https://github.com/iPoetDev/dash-and-do-github/issues/new?assignees=iPoetDev&labels=&projects=&template=07-check--static-analysis.md&title=%5BCHECK+%7C+LINT%5D+%3A%3A+)
            - Pre-commit.
            - Lint Report
            - Static Analysis
            - W3C HTML & W3C CSS
        -   [07 BUG: Exception | Issue | Usability | Function | Responsiveness](https://github.com/iPoetDev/dash-and-do-github/issues/new?assignees=iPoetDev&labels=&projects=&template=07-bug--exception---issue---usability---function---responsiveness.md&title=BUG+%3A%3A+++)
            - Code Exception |
            - Testing Issue |
            - UI/UX Concern |
            - UAT Issue
        - [08 TEST: Test Case | TDD](https://github.com/iPoetDev/P4Template/issues/new?assignees=iPoetDev&labels=&projects=&template=08-test--test-case---tdd--.md&title=%5BTEST%2FTDD%5D)
            - Test Case | TDD
        - [09 DONE: Definition of Done ](https://github.com/iPoetDev/dash-and-do-github/issues/new?assignees=iPoetDev&labels=&projects=&template=09-done--definition-of-done-.md&title=DONE%3A+)
            - Definition of Done
                - Effort and UAC for Final Release & Delivery
-   CONFIG:
    - [10 CONFIG: Linting | Static Analysis | Common Setups)](https://github.com/iPoetDev/dash-and-do-github/issues/new?assignees=iPoetDev&labels=&projects=&template=09-config--linting---static-analysis---common-setups.md&title=CONFIG+%3A%3A+)
        - Tooling: Linting, Static Analysis
        - Common Setups: Public acceptable | Well Known Configuration
-   PROJECT
    - [11 IMPEDE: Project Level Impediments](https://github.com/iPoetDev/dash-and-do-github/issues/new?assignees=iPoetDev&labels=Project%3A+Impediment&projects=&template=11-impede--project-level-impediments.md&title=IMPEDE%3A+Project+Blocker%3A+)
        - Project Impediment
        - Epic level blockers & issues.

### 3.4. [Readme]()

> PROJECT: Style | Approach | Key Deliverable

-   [x] Criteria: README
-   [ ] Completed? 🛫

-   In English.
-   Defined upfront, at start of the project cycle, a planning and delivery tool, not as an afterthought.
-   Highly descriptive.
-   Heading Hierarchy.
-   Sequenced heading numbering.
-   Headings linked and anchored.
-   Highly detailed.
-   Not Conventional, counter traditional and beyond the CI recommendation.
-   Professional-grade project management and solution documentation.
-   In the style of Readme Driven Development, this was written first before any code was committed.

***
> .
***

## 4. [Concept](#concept)

### 4.1. [Real World Domain](#domain)

-   **<ins>Domain</ins>**: GitHub.com as a software development, source control and deployment collaboration platform.
-   **<ins>Data Source</ins>**: GitHub API
-   **<ins>Scenario</ins>**: A Personal Developer seeking to manage, report and make bulk changes/automations to their GitHub Account.

---
>
***

### 4.2 Target Audiences](#audiences)

-   Focus is on:
    -   **Core Audience**: Developers
        -   Sub Cohort: Junior Developers
        -   Sub Cohort: Open Source Developers
    -   **Auxiliary Audience**: Software Managers
        -   Sub-Cohort: Hiring Managers (Engineering Managers | Software Development Managers)
        -   Sub-Cohort: Repo Managers in Open Source


---
>
***

### 4.3. [Web App Capabilities](#app-capabilities)

-   [ ] Criteria:
-   [ ] Review
-   [ ] Completed?

This app will serve users with the following:

-   Ability, **_must have_**, to _`use|integrate`_ GitHub as a _`primary|secondary`_ _`social login`_ to
    _`access|connect`_ and _`authenticate`_ to the main web _`app|service`_. #Authentication #Access #Authorisation
    #Onboarding
-   Ability, **_must have_**, to _`interact`_ with GitHub's API to access the public application and data interfaces of
    the GitHub platform, so to _`manipulate`_ and _`aggregate`_ one's own _`account|repository`_ data. #API #RestFul
-   Ability, **_should have_**, to _`analyse`_ all repositories, _`public and|or private`_ and _`categorise`_ them, in
    bulk: #Repositories #DataAnalysis
    -   The scope and frequency of languages uses. GitHub has this feature per repository.
    -   The scope and frequency of file types uses (?). Subject to GitHub API definitions and terms of service.
    -   The presence/absence of labels, number and completeness.
-   Ability, **_should have_**, to _`report`_, using a _`client|server`_ rendered visual summarisation and collation
    approach, on the state of all repositories, and to _`provide`_ a an **_`"at a glance"`_** snapshot on the state of the
    account's repositories.
-   Ability, **_could have_**, to perform bulk actions on specific GitHub features like:
    -   **_Labels_** #FeatureCRUD
    -   **_`Config.yml`_** #FileIO #API-I/O
    -   **_Common Files_**, or Common Project files (see below). #FileI/O #API-I/O
-   Ability, **could have**, to `store` a central file _`type|store`_, i.e. a pre-defined template, for a specific purpose
    and then `'Copy'` and `'Apply'` across those repository that do not have them. #FileIO #API-I/O
    **- Will not** have the ability to edit or change these files inside the web app.
    -   This is out of scope as IDEs and the basic GitHub editing functionalities serve this role.
        **- Will not** have the ability to manipulate GitHub Account Settings or have the permission granted to them.
        #NotInScope
-   Ability, **should have**, to _`remove`_ a GitHub _`social login`_ as a _`primary|secondary`_ source of _`access`_,
    _`authorisation`_ and or _`authentication`_, without affecting the primary login model and access control. #GitHub
    #Integration #OffBoarding

---
>
***

### 4.4. [Real User Frustration](#user-frustrations)

-   [ ] Criteria:
-   [ ] Completed? 🛫

This comes from the author/developer’s personal experience and fustrations. Given others’ comments in the Code
Institute, this may not be an isolated experience.

-   Many of the GitHub platform activities are manual, iterative and repetitive.
    -   This is am admirable quality of flexibility for maximum customisation and adaptability.
    -   On the other hand, applying the same conventions, and standards consistently and uniformly across all the
        repositories is inconsistent, poor levelling of features, and user generated data etc.
-   These user and usability frustration are a by-product of the user's personal experiences and user journey when using GitHub.com.

#### 4.4.1. Challenge: Creating Labels

> SOLUTION:

-   [ ] Criteria:

#### 4.4.2. Challenge: Common Files

> SOLUTION:

-   [ ] Criteria:

#### 4.4.3. Challenge: Cross Repository Actions & Activities

> SOLUTION:

-   [ ] Criteria:

---
>
***

### 4.5. Real World Solution & Idea

---
>
***


> `FOOTER`

[[---]]

###### <ins>Contact Me</ins>

**Author**: Charles J Fowler <br>
**WakaTime**: [https://wakatime.com/@ipoetdev](https://wakatime.com/@ipoetdev) <br>
**GitHub (iPoetDev)**: [https://github.com/iPoetDev](https://github.com/iPoetDev) <br>
**LinkedIn**: [www.linkedin.com/in/CharlesJFowler](www.linkedin.com/in/CharlesJFowler) <br>
**Scheduling**: [www.tidycal.com/CharlesJFowler](www.tidycal.com/CharlesJFowler) <br>

###### <ins>Community & Feedback</ins>

**Discussions**: [Point of Contact](https://github.com/iPoetDev/dash-and-do-github/discussions) ||
**History**: [Pulse](https://github.com/iPoetDev/dash-and-do-github/pulse) ||
**Community Files**: [Standards](https://github.com/iPoetDev/dash-and-do-github/community) ||
**Commit**: [Frequency](https://github.com/iPoetDev/dash-and-do-github/graphs/commit-activity) ||
**Code**: [Frequency](https://github.com/iPoetDev/dash-and-do-github/graphs/code-frequency) ||
**Insights**: [Activity](https://github.com/iPoetDev/dash-and-do-github/graphs/community)

#### <ins>Accreditation: Code Institute (Dublin, Ireland)</ins>

**Course**: [Diploma in Full Stack Software Development](https://codeinstitute.net/ie/full-stack-software-development-diploma/) <br>
**Education**: [Code Institute](https://codeinstitute.net/ie/) <br>

![logos-1](https://github.com/iPoetDev/dash-and-do-github/assets/51715025/074a0993-d78c-400e-be51-596aa31578a1)

---
