-   [ ] Completed?

## 7. [Architecture](#)

> SOLTUTION: #DESIGN | Strategy | Diagrams | Patterns | Technologies | Infrastructure | Components

-   [ ] Criteria:
-   [ ] Completed? 🛫

-   .
-   .

## 7.1 Method | Approach

> SOLUTION: Design | Architecture | Abstraction-First | C4 Model

-   [ ] Criteria:
-   [ ] ADR:
-   [ ] Completed?

### Why:

-   C4 Model: [The C4 model for visualising software architecture]

```embed
title: "The C4 model for visualising software architecture"
image: "https://static.structurizr.com/workspace/36141/diagrams/SystemContext.png"
description: "                                 1. A set of hierarchical abstractions (software systems, containers, components, and code).                                 2. A set of hierarchical diagrams (system context, containers, components, and code).                                 3. Notation independent.                                 4. Tooling independent.                             "
url: "https://c4model.com/"
```

-   **Benefits**:
    -   Is a map to the code
    -   Notion & Tooling independent
    -   Aids with communication
    -   Abstraction first, constrained to 4 tiers of detail and number of diagram types.
-   **Architecture Design Flow**:
    -   [Level 1: System Context Diagram](https://c4model.com/#SystemContextDiagram) - on C4Model.com
    -   [Level 2: Container Diagram](https://c4model.com/#ContainerDiagram) - on C4Model.com
    -   [Level 3: Component Diagram](https://c4model.com/#ComponentDiagram) - on C4Model.com
    -   [Level 4: Code Diagram (`Optional`)](https://c4model.com/#CodeDiagram) - on C4Model.com [?]
-   [ ] Workflow:
    -   [ ] Design on Excalidraw in Obsidian under `Diagrams`
    -   [ ] Export / Copy to Readme (move images later)
    -   [ ] Add to Section below

> > > **`Optional`**: For this project, this level of detail is an optional nice to have if sufficient scope or time
> > > constraint before delivery.

---

## 7. 2 System Design

> SOLUTION: Big Picture | System Landscape | People Focus | Software Systems | System Scope | External Systems

-   [Level 1: System Context Diagram](https://c4model.com/#SystemContextDiagram) - on C4Model.com

#### 7.2.1 GitHub - Developer - Account System

> SOLUTION: External System

-   **`EXTERNAL SYSTEMS: A GitHub Real World Domain`**
-   **System**: Github.com as a remote distributed code versioning system.
-   **Users**: Developers, GitHub.com
-   **Roles**: People, Organisations
-   **External Dependencies**s: GitHub User Account & Services, GitHub API
-   **Data Source**: GitHub API
-   **Scope**: Sits outside of the intended own software system
-   **Diagram Audience**: Users, Assessors, Developers etc

![](SYSTEM-GitHub-Developer-Account.png)
`Diagram: EXTERNAL SYSTEMS: GitHub Real World Domain & Datasource`

#### 7.2.2 GitHub <ins>Account</ins> - Developer - Own Web App [Dash & Do GH Manager]

> SOLUTION: External System

-   **`EXTERNAL SYSTEMS: A GitHub Real World Domain`**
-   **System**: <ins>Web App Account Integration</ins>
-   **Users**: Developers
-   **Roles**: People
-   **External Dependencies**s: GitHub User Account & Services,
-   **Data Source**: GitHub API, GitHub Account Auth. Tokens
-   **Scope**: Sits outside of the intended own software system, but is an Application Interface with own Web App
-   **App Features | Component**:
-   **Diagram Audience**: Users

![Image]()
\*\*`Diagram: EXTERNAL-INTERNAL SYSTEMS: GitHub Account API to Own Web Account User Account

#### 7.2.3 GitHub <ins>API</ins> - Developer - Own Web App [Dash & Do GH Manager]

> SOLUTION: External System

-   **`EXTERNAL SYSTEMS: A GitHub Real World Domain`**
-   **System**: <ins>Web App Features Integration & Data Source</ins>
-   **Users**: Developers
-   **Roles**: People
-   **External Dependencies**s: GitHub API
-   **Data Source**: GitHub API, GitHub Account Auth. Tokens
-   **Scope**: Sits outside of the intended own software system, but is an Application Interface with own Web App
-   **App Features | Component**:
-   **Diagram Audience**: Users

![Image]()
\*\*`Diagram: EXTERNAL-INTERNAL SYSTEMS: GitHub Account API to Own Web Account User Account

### 7.3 Container Design

> SOLUTION: Application | Data Store | Sub System

#### 7.3.1 Web Application User Account & Profile

-   **`CONTAINERS | SUB SYSTEMS: An Internal Web Application Domain`**
-   **Sub-System**: <ins>Web App Client - Server Architecture</ins>:
-   **Part of**: Developers
-   **Roles**: People
-   **External Dependencies**s: GitHub API
-   **Data Source**: GitHub API, GitHub Account Auth. Tokens
-   **Scope**: Sits outside of the intended own software system, but is an Application Interface with own Web App
-   **App Features | Component**:
-   **Diagram Audience**: Users

---

> .

---
