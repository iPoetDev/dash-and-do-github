---
sticker: emoji//2757
---
-   [ ] Completed?

## 7. [Architecture](#)

> SOLTUTION: #DESIGN | Strategy | Diagrams | Patterns | Technologies | Infrastructure | Components

-   [ ] Criteria:
-   [ ] Completed? 🛫

- .
- .

---
>
---

## 7.1 Method | Approach (C4 Model)

> SOLUTION: Design | Architecture | Abstraction-First | C4 Model

-   [ ] Criteria:
-   [ ] ADR:
-   [ ] Completed?

### Why:

- C4 Model: [The C4 model for visualising software architecture]

```embed
title: "The C4 model for visualising software architecture"
image: "https://static.structurizr.com/workspace/36141/diagrams/SystemContext.png"
description: "                                 1. A set of hierarchical abstractions (software systems, containers, components, and code).                                 2. A set of hierarchical diagrams (system context, containers, components, and code).                                 3. Notation independent.                                 4. Tooling independent.                             "
url: "https://c4model.com/"
```

- **Benefits**:
  - Is a map to the code
  - Notion & Tooling independent
  - Aids with communication
  - Abstraction first, constrained to 4 tiers of detail and number of diagram types.
- **Architecture Design Flow**:
  -  [x] [Level 1: System Context Diagram](https://c4model.com/#SystemContextDiagram) - on C4Model.com
  -  [x]  [Level 2: Container Diagram](https://c4model.com/#ContainerDiagram) - on C4Model.com
  -  [x]  [Level 3: Component Diagram](https://c4model.com/#ComponentDiagram) - on C4Model.com
  - ~~[Level 4: Code Diagram (`Optional`)](https://c4model.com/#CodeDiagram) - on C4Model.com [?]~~
-   [ ] Workflow:
  -   [x] Design on Excalidraw in Obsidian under `Diagrams`
  -   [x] Export / Copy to Readme (move images later)
  -   [x] Add to Section below
      -
                                    - [x] System Design
    -
      - [x] Container Design
    -
      - [ ] Component Design

> > > **`Optional`**: For this project, this level of detail is an optional nice to have if sufficient scope or time
> > > constraint before delivery.

---

## 7. 2 System Design (C4 Model)

> SOLUTION: Big Picture | System Landscape | People Focus | Software Systems | System Scope | External Systems

- [x] Completed
- [ ] .

- [Level 1: System Context Diagram](https://c4model.com/#SystemContextDiagram) - on C4Model.com

### 7.2.1 GitHub - Developer - Account System

> SOLUTION: External System

- [x] Completed
- [ ] .

- **`EXTERNAL SYSTEMS: A GitHub Real World Domain`**
- **System**: GitHub.com as a remote distributed code versioning system.
- **Users**: Developers, GitHub.com
- **Roles**: People, Organizations
- **External Dependencies**: GitHub User Account & Services, GitHub API
- **Data Source**: GitHub API
- **Scope**: Sits outside of the intended own software system
- **Diagram Audience**: Users, Assessors, Developers etc

![](SYSTEM-GitHub-Developer-Account%201.png)
`Diagram: EXTERNAL SYSTEMS: GitHub Real World Domain & Datasource`

---

### 7.2.2 Dash and Do GitHub Managing System

> SOLUTION: Container (& Software Systems / Sub Containers) to External Containers

- [x] Completed
- [ ] .

*`Model Type: C4 System Context`*
![](Pasted image 20230717162027.png)
**`Diagram: SYSTEMS Context: Dash and Do GitHub Managing System

###### <ins>Overview</ins>

**1. Web Client**: GitHub <ins>Account</ins> - Developer - Own Web App & 2 Single Page Applications. [Sub System], e.g.
Django
**2. Web Server & API Client**: GitHub <ins>API</ins> - Developer - Own Web App (Django Web Server). [Sub System], e.g.
Django & Django Rest Framework
**3. Remote Backing Service**: Cloud Hosting Database-as-a-Service (App). [Sub System]  e.g. Postgres SQL remote
relational database provider.
**4. Cloud Hosting**: Cloud Platform-as-a-Service (App) - Entire Dash & Do Software System [Container] e.g. Heroku
application service provider,
**5. GitHub External Systems**: e.g. GitHub Account, Repositories, API
**6. User/Person**: i.e. Developer

***

#### 7.2.2.1 The Web Client: GitHub <ins>Account</ins> - Developer - Own Web App [Dash & Do GH Manager]

> SOLUTION:  CONTAINER: Software Sub-Container

- [ ] Completed
- [ ] .

- **`EXTERNAL SYSTEMS: A GitHub Real World Domain`**
- **System**: <ins>Web App Account Integration</ins>
- **Users**: Developers
- **Roles**: People
- **External Dependencies: GitHub User Account & Services,
- **Data Source**: GitHub API, GitHub Account Auth. Tokens
- **Scope**: Sits outside of the intended own software system, but is an Application Interface with own Web App.
- **Features | Component**:
- **Diagram Audience**: Users

![If needed]()
**`Diagram: EXTERNAL-INTERNAL SYSTEMS: GitHub Account API to Own Web Account User Account

---

#### 7.2.2.2 The Web Server & API Client: GitHub <ins>API</ins> - Developer - Own Web App [Dash & Do GH Manager]

> SOLUTION: External System

- [ ] Completed
- [ ] .

- **`EXTERNAL SYSTEMS: A GitHub Real World Domain`**
- **System**: <ins>Web App Features Integration & Data Source</ins>
- **Users**: Developers
- **Roles**: People
- **External Dependencies**: GitHub API
- **Data Source**: GitHub API, GitHub Account Auth. Tokens
- **Scope**: Sits outside of the intended own software system, but is an Application Interface with own Web App
- **App Features | Component**:
- **Diagram Audience**: Users

![If needed]()
\*\*`Diagram: EXTERNAL-INTERNAL SYSTEMS: GitHub Account API to Own Web Account User Account

#### 7.2.2.3 The Backing Service: Own Web App [Dash & Do GH Manager] - Cloud Hosting Database-as-a-Service (App)

> Managed Database Backing System
> SOLUTION: External System

- [ ] Completed
- [ ] .


- **`EXTERNAL SYSTEMS: Fully Managed Relational Database System, Cloud Hosted`**
- **System**: Cloud Hosting Managed Backing System
- **Users**: App Developers, Managed RBS Service Owner
- **Roles**: App Developer, RDB Account Owner, RBS Service Owner
- **External Dependencies**:  External Managed Relational Database (Service, Host)
- **Data Source**: External Managed Relational Database (Service, Host)
- **Scope**: Sits outside the intended own software system, but is an Application Interface with own Web App
- **Features | Component**:
- **Diagram Audience**: Users

![If needed]()
**`Diagram: EXTERNAL-INTERNAL SYSTEMS: Own Web App [Dash & Do GH Manager] - Cloud Hosting Database-as-a-Service (App)**

---

#### 7.2.2.4 The Cloud Hosting Platform: Own Web App [Dash & Do GH Manager] - Cloud Hosting Platform-as-a-Service (App)

> SOLUTION: External System

- [ ] Completed
- [ ] .

- **`EXTERNAL SYSTEMS: Cloud Hosting Platform-as-a-Service (App)`**
- **System**: Cloud Hosting Managed Backing System
- **Users**: App Developers, Managed RBS Service Owner
- **Roles**: App Developer, RDB Account Owner, RBS Service Owner
- **External Dependencies**:  External Managed Relational Database (Service, Host)
- **Data Source**: External Managed Relational Database (Service, Host)
- **Scope**: Sits outside of the intended own software system, but is an Application Interface with own Web App
- **App Features | Component**:
- **Diagram Audience**: Users

![If needed]()
**`Diagram: EXTERNAL-INTERNAL SYSTEMS: Own Web App [Dash & Do GH Manager] - Managed Database Backing System**

---
>
---

## 7.3 Container Design  (C4 Model)

> SOLUTION: Application | Data Store | Sub System | Contained Design

- [x] Completed
- [ ] Reviewed?

- [Level 2: Container Diagram](https://c4model.com/#ContainerDiagram) - on C4Model.com
- `A container is essentially a context or boundary inside which some code is executed or some data is stored.`
- Each container 's:
  - a separately deployable/runnable thing or runtime environment.
  - typically (but not always) running in its own process space.
  - communication between containers typically takes the form of an inter-process communication (e.g. API, RPC etc).

#### 7.3.0.1 Definitions

- **Server-side web application**:
  - e.g. A Java EE web application running on Apache Tomcat, an ASP.NET MVC application running on Microsoft IIS, a
    Ruby on Rails application running on WEBrick, a Node.js application, etc.
- **Client-side web application**:
  - e.g. A JavaScript application running in a web browser using Angular, Backbone.JS, jQuery, etc.
- **Serverless function**:
  - A single serverless function (e.g. Amazon Lambda, Azure Function, etc).
- **Database**:
  - e.g. A schema or database in a relational database management system, document store, graph database, etc such as
    MySQL, Microsoft SQL Server, Oracle Database, MongoDB, Riak, Cassandra, Neo4j, etc.

*`Model Type: C4 Container`*
![](Pasted image 20230717151415.png)
**`Diagram: CONTAINER - EXTNERAL CONTAINERS: The Dash & Do GitHub Managing System`**

**1. Front End Web Application/Client**: Web Application User Account & Profile[Sub System]
**1.1 Web SPA**: Web Application **Dash(board) Single Page Application** [Sub System]
**1.2. Web SPA**: Web Application **Do (& Act) Single Page Application** [Sub System]
**2. Web Server & API Application Middleware**: GitHub <ins>API</ins> - Developer - Own Web App (Django Web
Server). [Sub System]
**3. Database as a Service’s Managed Database**: Cloud Hosting Database-as-a-Service (App). [Sub System]
**4. Cloud Hosting Platform-as-a-Service (App)**: Entire Dash & Do Software System [Container]

---

### 7.3.1 Web Application User Account & Profile

- [ ] Completed
- [ ] .

- **`CONTAINERS | SUB SYSTEMS: An Internal Web Application Domain`**
- **Containers**:
  - **Server-side web application**:
  - **Client-side web application**:
  - **Database**:
  - **Interface API**:
- **Architecture**: <ins>Web App Client - Server Architecture</ins>:
- **Part of**: *7.2.1 GitHub - Developer - Account System*
- **Actor**: Developer, GitHub API
- **External Dependencies**: Hub API, GitHub Access Token
- **Data Source**: GitHub API, GitHub Account Auth. Tokens
- **Scope**: Sits outside intended own software system, but is an Application Interface with own Web App.
- **App Features | Component**:
- **Diagram Audience**: Users

![Image]()
**`Diagram: EXTERNAL-INTERNAL SYSTEMS: Web Application User Account & Profile**

---

#### 7.3.1.1 Web Application Dash(board) Single Page Application

- [ ] Completed
- [ ] .

- **`CONTAINERS | SUB SYSTEMS: An Internal Web Application Domain`**
- **Containers**:
  - **Server-side web application**:
  - **Client-side web application**:
  - Middleware Web Framework: Django
  - **Database**:
    - ORM: Django ORM
  - **Interface API**:
- **Architecture**: <ins>Web App Client - Hypermedia API - Server Architecture</ins>:
- **Part of**: *7.2.1 GitHub - Developer - Account System*
- **Actor**: Developer, GitHub API
- **External Dependencies**s: GitHub API, GitHub Access Token.
- **Data Source**: GitHub API, GitHub Account Auth. Tokens
- **Scope**: Sits outside the intended own software system, but is an Application Interface with own Web App.
- **App Features | Component**:
- **Diagram Audience**: Users

![Image]()
**`Diagram: INTERNAL SYSTEMS: Web Application Dash(board) Single Page Application**

---

#### 7.3.1.2 Web Application Do(Repo tasks) Single Page Application

- [ ] Completed
- [ ] .

- **`CONTAINERS | SUB SYSTEMS: An Internal Web Application Domain`**
- **Containers**:
  - **Server-side web application**:
  - **Client-side web application**:
  - Middleware Web Framework: Django
  - **Database**: Postgres SQL
    - ORM: Django ORM
  - **Interface API**:
- **Architecture**: <ins>Web App Client - Hypermedia API - Server Architecture</ins>:
  - Style: Hypermedia Drive API
- **Part of**: *7.2.1 GitHub - Developer - Account System*
- **Actor**: Developer, GitHub API
- **External Dependencies**: GitHub API, GitHub Access Token.
- **Data Source**: GitHub API, GitHub Account Auth. Tokens
- **Scope**: Sits outside the intended own software system, but is an Application Interface with own Web App.
- **Features | Component**:
- **Diagram Audience**: Users

![Image]()
**`Diagram: INTERNAL SYSTEMS: Web Application Do(Repo tasks) Single Page Application**

***

### 7.3.3 Web Server & API Application Middleware/Client

- [ ] Completed
- [ ] .

- **`CONTAINERS | SUB SYSTEMS: An Internal Web Application Domain`**
- **Containers**:
  - **Server-side web application**:
  - **Client-side web application**:
  - Middleware Web Framework: Django
  - **Database**: Postgres SQL
    - ORM: Django ORM
  - **Interface API**:
- **Architecture**: <ins>Web App Client - Hypermedia API - Server Architecture</ins>:
  - Style: Hypermedia Drive API
- **Part of**: *7.2.1 GitHub - Developer - Account System*
- **Actor**: Developer, GitHub API
- **External Dependencies**s: GitHub API, GitHub Access Token.
- **Data Source**: GitHub API, GitHub Account Auth. Tokens
- **Scope**: Sits outside of the intended own software system, but is an Application Interface with own Web App.
- **App Features | Component**:
- **Diagram Audience**: Users

![Image]()
**`Diagram: INTERNAL SYSTEMS: Web Application Do(Repo tasks) Single Page Application**

***

### 7.3.4 Managed Relational Database

- [ ] Completed
- [ ] .

- **`CONTAINERS | SUB SYSTEMS: An Internal Web Application Domain`**
- **Containers**:
  - **Server-side web application**:
  - **Client-side web application**:
  - Middleware Web Framework: Django
  - **Database**: Postgres SQL
    - ORM: Django ORM
  - **Interface API**:
- **Architecture**: <ins>Web App Client - Hypermedia API - Server Architecture</ins>:
  - Style: Hypermedia Drive API
- **Part of**: *7.2.1 GitHub - Developer - Account System*
- **Actor**: Developer, GitHub API.
- **External Dependencies**s: GitHub API, GitHub Access Token.
- **Data Source**: GitHub API, GitHub Account Auth. Tokens
- **Scope**: Sits outside of the intended own software system, but is an Application Interface with own Web App.
- **App Features | Component**:
- **Diagram Audience**: Users

![Image]()
**`Diagram: INTERNAL SYSTEMS: Web Application Do(Repo tasks) Single Page Application**

***

### 7.3.5 Platform as Host - Application Services

- [ ] Completed
- [ ] .

- **`CONTAINERS | SUB SYSTEMS: An Internal Web Application Domain`**
- **Containers**:
  - **Server-side web application**:
  - **Client-side web application**:
  - Middleware Web Framework: Django
  - **Database**: Postgres SQL
    - ORM: Django ORM
  - **Interface API**:
- **Architecture**: <ins>Web App Client - Hypermedia API - Server Architecture</ins>:
  - Style: Hypermedia Drive API
- **Part of**: *7.2.1 GitHub - Developer - Account System*
- **Actor**: Developer, GitHub API
- **External Dependencies: GitHub API, GitHub Access Token
- **Data Source**: GitHub API, GitHub Account Auth. Tokens
- **Scope**: Sits outside of the intended own software system, but is an Application Interface with own Web App
- **Features | Component**:
- **Diagram Audience**: Users

![Image]()
**`Diagram: INTERNAL SYSTEMS: Web Application Do(Repo tasks) Single Page Application**


---
>
---

## 7.4 Component Design  (C4 Model)

> SOLUTION | Exclude Django Framework Components | Include Custom Components

- [ ] Completed
- [ ] .

- [Level 3: Component Diagram](https://c4model.com/#ComponentDiagram) - on C4Model.com

##### 7.4.0.1 Definition

- a component is a grouping of related functionality encapsulated behind a well-defined interface.
- a component as a collection of implementation classes behind an interface.
- all components inside a container typically execute in the same process space.
- **components are not separately deployable units,** and are highly dependent.

---

### 7.4.1

> SOLUTION:

- [ ] Completed
- [ ] .

**Scope**: Target Container:
**Primary elements**: Components within the  `container` in scope.

- .
- .
  **Supporting elements**:
- Containers (within the software system in scope) plus
- People directly connected to the components.
- software systems directly connected to the components.
  **Diagram Audience**: Software architects and developers.

---
>
---

## 7.5 Code Diagram 🚫  (C4 Model)

> SOLUTION: Not Recommend | System Design to Simple | Level of Detail No Required.

- [ ] Completed
- [ ] .

- For this project this is not necessary,
- Too high maintenance and effort to create, update and manage
- Services like [AppMap | Runtime Code Analysis for Developers AppMap https://appmap.io](https://appmap.io/) and IDEs
  can generate this level of detail on demand, for long-lived documentation,
- Available on demand, automatically generated by keep detail to a minimum as details of implementation are subject to
  frequently change.

**Read more**

-     -   [Level 4: Code Diagram (`Optional`)](https://c4model.com/#CodeDiagram) - on C4Model.com [?]

---
>
---

## 7.6 Architectural/Any Decisions Records for Requirements

> SOLUTION: ADR

- [ ] Completed
- [ ] .

### 7.6.1 Introduction

- How do does the author track and record key decisions during the lifetime of the project? Answer: see this Project & Developer’s User Story below.

```text
As a Developer, 
I want to record any decisions made in this project
for when they are independant and whether the decision concerns
  a) the architecture (i.e. "architectural decision record")
  b) the code
  c) other domains/topics 
So that: 
  1) Implicit assumptions be made explicit
  2) Allow for structured capaturing of any decisions
  3) Be lean enough to fit in with the developer's developmennt style
  4) Be comprehensible
  5) Faciliate usage and ongoing maintenance and change.
```

- Other domains and topics could include: Design Patterns, UX & Interaction Choices, Documentation Approaches etc 

#### Definition

From the **[`adr.github.io`](https://adr.github.io/)**: the Developer is motivated to record and log the key significant decisions and their evolution over the lifetime of the project.  

##### *[Architectural Decision (AD)](https://en.wikipedia.org/wiki/Architectural_decision)*

>> `fas:QuoteLeft`  An [Architectural Decision (AD)](https://en.wikipedia.org/wiki/Architectural_decision) is a justified software design choice that addresses a functional or non-functional requirement that is architecturally significant

##### *[Architecturally Significant Requirement (ASR)](https://en.wikipedia.org/wiki/Architecturally_significant_requirements)*

>> `fas:QuoteLeft` An [Architecturally Significant Requirement (ASR)](https://en.wikipedia.org/wiki/Architecturally_significant_requirements) is a requirement that has a measurable effect on a software system’s architecture and quality

##### _Architectural Decision Record (ADR)_

>> `fas:QuoteLeft` An _Architectural Decision Record (ADR)_ captures a single AD and its rationale

as well as …

>> `fas:QuoteLeft` ADR usage can be extended to design and other decisions (“Any Decision Record”).

##### _Architectural Decision Log (ADL)_

>> `fas:QuoteLeft` An Architectural Decision Log is the collection of ADRs created and maintained in a project constitute its _decision log_.

#### Usage Notes

- “*Lightweight”* ADR should be adopted - [Read more](ADR usage can be extended to design and other decisions (“any decision record”).
- *Y-Statements* make for more <ins>sustainable architectural decisions</ins>. [Read more.](https://adr.github.io/#sustainable-architectural-decisions) and for the fact they look like use case or user stories, and are minimal enough.
- There are several classes of ADR
    - Full Weight: e.g. MADR 3.0.0., or Michael Nygaard’s Template 
    - Simple:  e.g. like Y-Statements
    - Adapted: i.e. User adapted, which blends and adjusted the above as needed
- Glossary
    - A `chosen` ADR is a pre-defined criteria or constraint imposed by the “client”: The Code Institute.
    - A `selected` ADR is an inspection of a set of options from which a selected best case option is research, compared so that an ADR statement is composed on, and finally entered into the ADR Decision Log.

#### Templates

Two templates are author-defined:

1. A [“fuller” ADR Template](https://github.com/iPoetDev/dash-and-do-github/issues/new?assignees=iPoetDev&labels=&projects=&template=01--adr-full.md&title=ADR000%3F+%3A%3A+))
2. A minimal [Y Statement (i.e. ADR-Y) Template](https://github.com/iPoetDev/dash-and-do-github/issues/new?assignees=iPoetDev&labels=&projects=&template=02-adr-y-statement.md&title=ADR-Y000%3F+%3A%3A+))

Also a Y-Statement ADR may be found in the body of a significant User Story as a sub section.

Each of these templates are defined as GitHub Issue Templates and can be tracked by GitHub Issues as part of the GitHub management workflows for 

### 7.6.2 Decision Log
> PROJECT | SOLUTION: Any Decision Log 

Grouping of ADR 
1. **CRITERIA**: Imposed solution or project criteria from Code Institute chosen requirements
2. **PROJECT**: Pre-set technical requirements that impact the project management.
3. **SOLUTION**: Developer defined solution (i.e. software, application, web app) requirements and selected as best case.

#### 7.6.2.1 CRITERIA ADR | Requirements
> .
-  [ ] Completed?

- These design decisions are the client’s design constraints, imposed from top down. These can be stated as conceptual or factual Y-Statements.

- [ ] ADR000X - Use Agile as the project & software delivery methodology to plan and design a Full Stack Web Application (LO-01)
- [ ] ADR000X - Use a MVC design pattern as a framework for a Full Stack Web Application (LO-1.0)
- [ ] ADR000X - Use contemporary technologies for a Full Stack Web Application (LO-1.0)
- [ ] ADR000X - To use HTML & CSS to implement custom HTML & CSS code for responsive design (LO-1/2)
- [ ] ADR000X - To validate HTML & CSS so that the code is consistent in style and is error free.
- [ ] ADR000X - To use a web application that has a backing service (LO-1.3)
- [ ] ADR000X - To use an Agile Tool, and Agile methods, to manage the planning and implementation (LO-1.4)
    - [ ] ADR000X - To use Epics, User Stories and Story Points
- [ ] ADR000X - To use Python as a core language
- [ ] ADR000X - To use JavaScript as a client side only interactive language
- [ ] ADR000X - To use specific code standards & organisation for code quality and integrity
- [ ] ADR000X - To document the UX design work for the project
- [ ] ADR000X - To use User Acceptance Criteria
- [ ] ADR000X - To document a clear rationale for the project development (LO-1.15)
- [ ] ADR000X - To develop a model/schema into a usable database (LO-2.1)
- [ ] ADR000X - To maintain database configuration in a single location, where it can be changed easily (LO-2.5)
- [ ] ADR000X - To use Role Based Authentication and Registration
- [ ] ADR000X - To use Role Based Access for Permissions
- [ ] ADR000X - To use manual and/or automated tests for a Full-Stack Web application
- [ ] ADR000X - To document the results of manual and/or automated tests for a Full-Stack Web application
- [ ] ADR000X - To a distributed version control system to document, develop and maintain a Full-Stack Web application
- [ ] ADR000X - To a repository hosting service to document, develop and maintain a Full-Stack Web application
- [ ] ADR000X - To deploy a final version of the Full-Stack application code to a cloud-based hosting platform
- [ ] ADR00X - To assure not credentials, or database configuration or Canonical values are hardcoded and deployed to the Cloud Hosting platform.

#### 7.6.2.1 PROJECT ADR | Requirements
> .
-  [ ] Completed?

- ADR000X: Using Readme Driven Development for Detailed & Summary Readmes
- ADR000X: Selecting Zube.com an the Agile Tool platform to to manage the planning and implementation (v GitHub.com Projects or Issues, )
- ADR000X: Select a Preferred Project Structure for the Django (Simple or Double Directory)

#### 7.6.2.3 SOLUTION ADR | Requirements
> .
-  [ ] Completed?

-  [ ] ADR000X - Selects Django Web Application Framework (version 4.2/@latest) as the rapid application development method and full stack web application framework.
-  [ ] ADR000X - Selects Django Rest Framework (@latest) for external API/JSON calls and HTTP and data processing.
-  [ ] ADR000X - Selects HTMX (@latest) and Hypermedia API for internal API/HTML calls and data processing.
-  [ ] ADR000X - Selects CSS Utility Framework (BootStrap@latest or TailWindCSS@latest) for CSS rendering and styling.
-  [ ] ADR000X - Selects Locality of Behaviour over a Separation of Concerns as a predominate declarative front end architecture pattern (and file code organisation convention) and to avoid/reduce spooky at a distance cognitive load.
-  [ ] ADR000X - Selects GitHub API as the solutions external data source
-  [ ] ADR000X - Selects PostgresSQL as the usable production (and relational) database for Django in the database driven Full Stack web application (and as the Backing Service of choice (IV, 12 Factor))
-  [ ] ADR000X - Selects ElephantSQL as the production managed Database as a Service provider for cloud database hosting.
-  [ ] ADR000X - Selects Heroku as the managed Platform as a Service provider for cloud application hosting.
      - These next 3 sub decisions implement 12 Factor Apps aspects via the parent choice.  
      -  [ ] ADR000X - Selects Heroku Pipeline and Apps as the one Codebase, many deploys (I, 12  Factor) of choice.
      -  [ ] ADR000X - Selects Heroku ConfigVars (Environmental Vars) as the Config in the Environment (II), 12 Factor) of choice and associated Environmental and Settings management.
      -  [ ] ADR000X - Selects Heroku BuildPacks (NodeJs, Python) as the Dependecies (III, 12 Factor) for dependencies isolation and manifest, inclusive of Proc Files, and runtime.txt
-  [ ] ADR000X - Selects a Django Production web sever (gUnicorn or uWSGI) as the Port Binding (III, 12 Factor) using Proc file configuration as the entry point
 -  [ ] ADR000X - Selects a view architecture (Class based or Function based views) for Django Views (Implied is Class based views).
-  [ ] ADR000X - Selects a Static Assets manager (Built in or WhiteNoise) for Django
-  [ ] ADR000X - Selects a Authentication package (Built in or AllAuth (3rd Party) or other 3rd Parties) for Django
-  [ ] ADR000X - Selects a Forms package (Built in, Dynamic Forms with HTMX or Crispy Forms (3rd Party) or other 3rd Parties ) for Django
     - Django-Crispsy-Forms
     - Django-AutoComplete-Light
     - Django-TinyMCE
 -  [ ] ADR000X - Selects a test methodology / framework that is Django compatible for Python Code (and expected by Code Institute)
 -  [ ] ADR000X - Selects a test methodology / framework that is optimal for JavaScript (and expected by Code Institute) 
 -  [ ] ADR000X - Selects a deployment methodology / configuration that safely and securely deploys Django 
 -  [ ] ADR000X - Selects a database migration methodology / configuration that safely and securely deploys Django database / Models

- Compare: [Django Packages : for-comparison](https://djangopackages.org/grids/g/for-comparison/?python3=on&sort=score)
 ---
>
---

## 7.7 [Applying The 12 Factor App Methodology](#apply-12factor)

> SOLUTION: Abstract Applications from Infrastructure | Decoupling | Configurability | Scalability | Reliability

- [ ] Completed
- [ ] .

- In the given context of a Django web application, this article ([12 Factor App methodology applied to a Django app](https://hector.dev/2021/03/16/twelve-factor-methodology-applied-to-a-django-app/)) explains the key precepts and concepts of the 12 Factor App methodology for building, configuring and deploying idempotent software-as-a-service deployments in a cloud hosted environment.
- Each of the selected (i.e. decided for) and applied 12 factor is defined as a User Story, with acceptance criteria, and supplementary Any Decision Record for technologies choices or critical decision choice (or selections to be made when comparing alternatives).
- Those 12-Factors aspects not specified are outside of scope of the project or inherent in the Framework design and are not in custom web app.
- The following applies the *`MoSCoW`* framework to *need-driven* prioritisation to include or exclude the 12 Factor aspect in the requirements for architecture and deployment.

#### 7.7.1 Decided 12 Factors
> SOLUTION: Criteria Aligned | Explicit Decisions | App Requirements

For this project, selectable and chosen 12 factors aspects were applied into via these User Stories, in the Epic: The Arch and Deploy. 

##### 7.7.1.1 Definition and Scope
- #24 [DEFINE: Twelve-Factor App methodology | Research & Refine #24](https://github.com/iPoetDev/dash-and-do-github/issues/24)

##### 7.7.1.2 Chosen 12 Factors

1.  [x] **Codebase**: where *One codebase is tracked in revision control, many deploys*
    - #26 [STORY: As a 12 Factor App Developer, I want to have one Codebase & many Deploys #26](https://github.com/iPoetDev/dash-and-do-github/issues/26)
2.  [x] **Dependencies**: so to - *Explicitly declares and isolates dependencies*
    - `Must Include`: #27 [STORY: As a 12 Factor App Developer, I must explicitly declare all isolated dependencies (II) for Python 3.11 #27](https://github.com/iPoetDev/dash-and-do-github/issues/27)
    - `Must Include:` #28 [STORY: As a 12 Factor App Developer, I must explicitly declare all isolated dependencies (II) for JavaScript #28](https://github.com/iPoetDev/dash-and-do-github/issues/28)
3. [x]  **Config**: so to - *Store config in the environment* 
    - `Should Include`: #30 [STORY: As a 12 Factor App Developer, I want to store Config in the Environment (III) #30](https://github.com/iPoetDev/dash-and-do-github/issues/30)
4. [x] **Backing Services**: so to: *Treat backing services as attached resources*
    - `Should Include`: #29 [STORY: As a 12 Factor App Developer, want a Backing Service (IV), i.e. a Relational Database, that is a loosely coupled attachable resource #29](https://github.com/iPoetDev/dash-and-do-github/issues/29)
12.  [x] Admin Process**: so to: *Run admin/management tasks as one-off processes*
    - #31 [STORY: As a 12 Factor App Developer, I need to run Admin Process (XII) tasks as once-off (standalone) processes #31](https://github.com/iPoetDev/dash-and-do-github/issues/31)

***

#### Candidate 12 Factors
> SOLUTION: Optional for Scope | Nice to Have | Could Have Priority | Move Up or Move Down

5. **Build, Release, Runtime**: so to: *strictly separate build, release and run stages*
    - `Should Include`: . 
    - `Could Include`: .
7. **Port Binding**: to: *Export services via port binding*
    - `Could Include`: Represented by a Eco-Dyno on Heroku, in lieu of a Docker container.
    - `Could Include`: Webserver container that uses `Gunicorn` (`wsgi`) production-grade Python application server for UNIX based systems on Heroku, by using a `ProcFile` to use `Gunicorn` as an `entrypoint`
    - `Could Include`: Check if possible to add a few command-line options to ensure that the ASGI API is used (between Gunicorn and Django) along with the Uvicorn worker implementation
10. **Dev/Prod parity**: so to: *Keep development, staging, and production as similar as possible*
   - `Should Include`: . 
    - `Could Include`: .
    - `Will Not Include`: 
1. **Logs**: so to: *Treat logs as event streams*
   - `Should Include`: . 
    - `Could Include`: .
    - `Will Not Include`: 

***

#### 7.2.2. Excluded or Inherent Factors
> SOLTUON: Implicit | Inherent | Outside of Scope | Insufficient Information

6. **Processes**: to: *Execute the app as one or more stateless processes*.
    - `Will Not include`: as the app (as yet) is not design to scale horizontally.
    - `Could Include`: Django handles static assets using built in mechanisms,
    - `Could Include`: BUT could be included if a Decision is made to select between built in or using WhiteNoise for supporting static assets in a way that enabled thinking about a deploy as an atomic operation[Source]([Processes (hector.dev)](https://hector.dev/2021/03/16/twelve-factor-methodology-applied-to-a-django-app/#processes))
1. **Concurrency**: so to: *Scale out via the process model* 
    - `Will not include`: as the app is not designed for horizon and vertical scaling.
    - `Will not include`: as load against an application is not meant to increases and so no need to reliably adding more stateless concurrent _processes_.
    - `Will not include`: to specify different _process types_ as it can’t really be done with Gunicorn.
2. **Disposability**: so to: *Maximize robustness with fast start-up and graceful shutdown*
    - `Will not include`: to maximize robustness so properly handles certain types of asynchronous tasks/communications

---
>
---
