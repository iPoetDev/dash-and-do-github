![](CodeInstitute.png)

##### Welcome to CJ's Project Hub for The Code Institutes 4th Portfolio Project

## Full Stack Toolkit

| `Project Brief`                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------|
| _To build a Full-Stack site based on business logic used to control a centrally owned dataset._                                    |
| _To set up an authentication mechanism and provide role-based access to the site's data or other activities based on the dataset._ |

## Concept

To have a solution, i.e. a control plane / pane, over a GitHub Account, that gives the account holder:

### 1. User Profile account that integrates with GitHub Account by Social Login/2FA (Create, Update, Delete)

### 2. Overview of State and Status of His Repositories (Dashboard, [Read, Aggregate, Collate, Analyse, List, Display]

### 3. Set of Common Activities that streamline the managing of Repositories at bulk (Do n Act, [Create, Update, Delete])

### Goals

- #Client/Assessor #RFP To build a full-stack site based on business logic used to control a centrally owned dataset.
- #Client/Assessor #RFP To set up an authentication mechanism and provide role-based access to the site's data or other
  activities based on the dataset.

- #Solution To integrate GitHub with the Web App via GitHub social login and authentication tokens, with full lifecycle
  account management, via onboarding and offboarding of this social login.
- #Solution To authorized and grant permissions to the web app, as a 3rd party` service|integration`, to one's own
  GitHub account or, maybe, a secondary one.
- #Solution To use GitHub API to perform the following
    - Analyse and graphically report on Languages used
    - Analyse and graphically report on File Types used
    - Analyse and collated the labels used across all accounts
    - CRUD and manipulate Issue Labels in bulk, centrally and apply to `all|selected` repositories in bulk.
    - Copy and Apply a central store of common file types to to `all|selected` repositories in bulk.
- #Project To use agile methodologies and tooling to deliver the #Solution to the #Client/Assessor: **<ins>The Code
  Institute</ins>

## Problem Domain

A.
> > A question that occurs: *how can a developer treat and tailor his whole GitHub as a single sharable artefact in
their portfolio and as a basis for his portfolio; and share to outside, or not GitHub account holders, and maximise the
value of their GitHub account without given 3rd party access or having another crawl across their repositories in
multiple pages and clicks.*

B.
> > A question that occurs: *how can a potential employer inspect a prospective developer's GitHub at a glance, with
meaningful analytics and high-level summary data?*

C.
> > A question that occurs: *how can, based on the prior question, can a developer keep track of the standard,
conventional and best practices, on a per repository or bulk repository basis, with cross cutting concerns? Can he keep
a in context to-do repository management list of common or standard tasks to maintain and manage his account over
numerous repositories (i.e. greater than 5).*

D.
> > A question that occurs: *how can a developer apply GitHub features, which are manually created (e.g. labels, custom
project fields), uniformly across more than two repositories and save time and effort on duplicative, repetitive and
non-DRY iterative efforts. Such efforts have the challenge of lack of consistency and not being standard/best practice
driven.*

E.
> > A question that occurs: *how can a developer apply GitHub best practices, like conventions and common files (
> > examples of which are documented here), uniformly across more than two repositories and save time and effort on
> > duplicative, repetitive and iterative file generation efforts. These generation efforts done once and repeated many
> > times from a central source.

## Depends On

- **API**: GitHub API
- Access:
    - GitHub Access Token,
    - GitHub Account Integration
    - GitHub Security
    - GitHub API policies & Licenses
- Libraries
    - Python Libraries for GitHub (as per Github.com)
    - Python/Django libraries for OAuth authentication
    - Django
    - HTMX
- Infra
    - PaaS Host
    - Cloud/remote managed database service

## App Capabilities

This app will serve users with the following:

- Ability, ***must have***, to *`use|integrate`* GitHub as a *`primary|secondary`* *`social login`* to
  *`access|connect`* and *`authenticate`* to the main web *`app|service`*. #Authentication #Access #Authorisation
  #Onboarding
- Ability, ***must have***, to *`interact`* with GitHub's API to access the public application and data interfaces of
  the GitHub platform, so to *`manipulate`* and *`aggregate`* one's own *`account|repository`* data. #API #RestFul
- Ability, ***should have***, to *`analyse`* all repositories, *`public and|or private`* and *`categorise`* them, in
  bulk: #Repositories #DataAnalysis
    - The scope and frequency of languages uses. GitHub has this feature per repository.
    - The scope and frequency of file types uses (?). Subject to GitHub API definitions and terms of service.
    - The presence/absence of labels, number and completeness.
- Ability, ***should have***, to *`report`*, using a *`client|server`* rendered visual summarisation and collation
  approach, on the state of all repositories, and to *`provide`* a an ***`"at a glance"`*** snapshot on the state of the
  account's repositories.
- Ability, ***could have***, to perform bulk actions on specific GitHub features like:
    - ***Labels*** #FeatureCRUD
    - ***`Config.yml`*** #FileIO #API-I/O
    - ***Common Files***, or Common Project files (see below). #FileI/O #API-I/O
- Ability, **could have**, to `store` a central file *`type|store`*, i.e. a pre-defined template, for a specific purpose
  and then `'Copy'` and `'Apply'` across those repository that do not have them. #FileIO #API-I/O
  **- Will not** have the ability to edit or change these files inside the web app.
    - This is out of scope as IDEs and the basic GitHub editing functionalities serve this role.
      **- Will not** have the ability to manipulate GitHub Account Settings or have the permission granted to them.
      #NotInScope
- Ability, **should have**, to *`remove`* a GitHub *`social login`* as a *`primary|secondary`* source of *`access`*,
  *`authorisation`* and or *`authentication`*, without affecting the primary login model and access control. #GitHub
  #Integration #OffBoarding

## Agile Tools

#### See [Agile Workflows](https://github.com/iPoetDev/P4Template/issues/new/choose)

#### See [Agile Projects](https://github.com/iPoetDev/P4Template/projects?query=is%3Aopen)

### See [Agile Milestones](https://github.com/iPoetDev/P4Template/milestones)

#### See [Inform, Control & Filter Labels](https://github.com/iPoetDev/P4Template/labels)

## [Project & Assessment Wiki](https://github.com/iPoetDev/P4Template/wiki)