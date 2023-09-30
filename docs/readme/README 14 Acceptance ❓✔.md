-   [ ] Completed?
-   [ ] Copy to Readme.md?

## 14. [Features & User Acceptance](#)

> SOLUTION: User Acceptance | Feature Acceptance

-   [ ] Criteria
-   [ ] Completed? 🛫

### 14.1. [Epic to Features](#epic-to-feature)

> SOLUTION: Feature Acceptance | Component | Utility

-   [ ] Criteria
-   [ ] Completed? 🛫

#### 14.1 Project Epic to Features

-  [ ] [EPIC #1: Readme Driven Development (github.com)](https://github.com/iPoetDev/dash-and-do-github/milestone/3) #GithubMilestone3
-  [ ] [EPIC #2 "The Arch & Deploy": Decisions, Deployment, Platforms (github.com)](https://github.com/iPoetDev/dash-and-do-github/milestone/4) #GithubMilestone4
-  [ ] [EPIC #3: "Agile Design & Test DD " Epics, Features, Tests, Stories, Acceptance (github.com)](https://github.com/iPoetDev/dash-and-do-github/milestone/5)

#### 14.1. 2 App Functionality Epic to Features

-   [ ] [EPIC #4: FEATURE: "Release: v0.5: PUBLIC Core Web App & Public/Private Views/Access" Design, Build, Test, Integrate, Deploy, Accept, Release (github.com)](https://github.com/iPoetDev/dash-and-do-github/milestone/6), #GitHubMilestone6

- Linked App: 
    - Kore: 
        - Path: apps\\kore
        - Dependencies:
            - Custom Views/Forms/Model

    -   [ ] #98   [FEAT :: VIEW: PUBLIC: `index.html` Page: All Users and Unauthenticated Users: i.e. the New Visitor, Unregistered and Not Logged In Visitor || `index.html` <= `page.html`](https://github.com/iPoetDev/dash-and-do-github/issues/98)
    -   [ ] #99  [FEAT :: VIEW: PRIVATE: `index.html` Page: All Users and Authenticated Users: i.e. the Returning Visitor, Registered and Logged In Visitor (with Actve Session) || `index.html` <= `page.html`](https://github.com/iPoetDev/dash-and-do-github/issues/99)
    -   [ ] #101   [FEAT :: VIEW: PUBLIC: Contact Email & Contact Form: All Users (Public Users and Private Users) || `index.html` <= `page.html`](https://github.com/iPoetDev/dash-and-do-github/issues/101)
    -   [ ] #100  [FEAT :: VIEW: PUBLIC: Email Verification & `verify.html` <= `simple.html`](https://github.com/iPoetDev/dash-and-do-github/issues/100)

-  [ ] [EPIC #5: FEATURE: “Release: v0.5: Users App: Management Design & Flow, Build, Test, Integrate, Deploy, Accept, Release (github.com) ](https://github.com/iPoetDev/dash-and-do-github/milestone/9)

- Linked App: 
    - User: 
        - Path: apps\\users
        - Dependencies: 
            - Django AllAuth
            - Custom Views/Forms/Model
    
    
    -   [ ] #102  [FEAT :: VIEW: PUBLIC: New User Registration & Sign Up Form: Public Users || `index.html` <= `page.html`](https://github.com/iPoetDev/dash-and-do-github/issues/102)
    -   [ ] #103  [FEAT :: VIEW: PUBLIC: Existing User Access & Login Up Form: Public Users || `index.html` <= `page.html`](https://github.com/iPoetDev/dash-and-do-github/issues/103)
    -   [ ] #104  [FEAT :: VIEW: PUBLIC: Existing User Reset Passwords, Reset Password Form & Verify Reset: Public Users: || `verify.html` <= `simple.html`](https://github.com/iPoetDev/dash-and-do-github/issues/104)



EPIC #5: FEATURE: “Release: v0.5: Private Accounts & User Profile” Design, Build, Test, Integrate, Deploy, Accept, Release (github.com) 

    - Profile: 
        - Path: apps\\profile
        - Dependencies:
            - Custom Views/Forms/Model
    
    
    -   [ ] FEAT 00.0
    -   [ ] FEAT 00.0
    -   [ ] FEAT 00.0
    -   [ ] FEAT 00.0

-   [ ] [EPIC #5: FEATURE: "Release v1.0: Dash (DashBoard/Reporting/Summaries) " Design, Build, Test, Integrate, Deploy, Accept, Release (github.com)](https://github.com/iPoetDev/dash-and-do-github/milestone/7)

    -   [ ] FEAT 00.0
    -   [ ] FEAT 00.0
    -   [ ] FEAT 00.0
    -   [ ] FEAT 00.0

-  [ ] [EPIC #6: FEATURE: "Release V2.0 Do [Tasker, Bulk] " Design, Build, Test, Integrate, Deploy, Accept, Release (github.com)](https://github.com/iPoetDev/dash-and-do-github/milestone/8)

    -   [ ] FEAT 00.0
    -   [ ] FEAT 00.0
    -   [ ] FEAT 00.0
    -   [ ] FEAT 00.0


---

### 14.2. [Feature to Story](#feature-to-story)

> SOLUTION: User Story | User Acceptance | Behaviour | Outcome | Impact

-   [ ] Criteria
-   [ ] Completed? 🛫

`'USx.x' = User Story + ID Sequence. Sub ids are .x, but only whole features are User Story Tested`

#### 14.2.1: Public & Private Site: Landing, Static and Service Pages 

- Linked:
    - *All following tagged with PUBLIC*
    - *Allow following tagged with PRIVATE*

-  [x] FEATURE: #98  [FEAT :: VIEW: PUBLIC: index.html Page: All Users and Unauthenticated Users: i.e. the New Visitor, Unregistered and Not Logged In Visitor || index.html <= page.html (github.com)](https://github.com/iPoetDev/dash-and-do-github/issues/98)
    - Public Site: Home Page, Static Pages and Public Navigation/Views only.

   -    [x] STORY #82 [`Newly Visting User's URL`: As a new visiting user to the Dash and Do GitHub website, and web app, I want to have a clearly memorable and easy to use URL as a domain name and as a brand identity so that I can remember the website and come back to it on a repeated basis](https://github.com/iPoetDev/dash-and-do-github/issues/82)
    -   [ ] STORY #?? Show/Hide Public Authentication Navigation & Page Components for Unauthenticated Users
    -   [ ] STORY #?? Branding & Styling
    -   [x] STORY #81 [`New Visting User`: As a new visiting user to the Dash and Do GitHub website, and web app, I want to arrive on a landing page, a home page, which immediately gives me strong impression, clues and calls to action of purpose, identity, registration, and login. (See related component stories below).](https://github.com/iPoetDev/dash-and-do-github/issues/81)
    -   [x] STORY #84: [`Unauthenticated User Login Story`: As an unauthenticated user, I want to not be able to restrict content and not have access to sensitive functionality so that all users have trust, confidence, integrity and availability in the web app and service (github.com)](https://github.com/iPoetDev/dash-and-do-github/issues/84) 

-  [x] FEATURE: #99 [FEAT :: VIEW: PRIVATE: index.html Page: All Users and Authenticated Users: i.e. the Returning Visitor, Registered and Logged In Visitor (with ActIve Session) || index.html <= page.html (github.com)](https://github.com/iPoetDev/dash-and-do-github/issues/99)
    - Private Site: Home Page, Static Pages and Private Navigation/Views only.

    -   [ ] STORY #?? Show/Hide Private Authentication Navigation & Page Components for Authenticated Users
    -   [ ] STORY 00.0
    -   [x] STORY #71 [`Set + Persist Session User Story`: As a returning user of Dash and Do GitHub web app, I want to be immediately logged into my account so that I do not have to login and reuse my password on every visit, by using a remember check box on login (opt in).](https://github.com/iPoetDev/dash-and-do-github/issues/71)
    -   [x] STORY #73 [`User Session Authorised Story`: As an authenticated user of Dash and Do GitHub web app, I want to authorised to access and persist this trusted state across one or more visits.](https://github.com/iPoetDev/dash-and-do-github/issues/73)
#### 14.2.2: Public Site:  Account Creation, User Registration and Signup Form

- Linked: 
    - *14.2.1: Public Pages*
    - *14.2.3: User Login*
    - *14.2.8: Site Emailing Services*

-   [x] FEATURE  #102 [FEAT :: VIEW: PUBLIC: New User Registration & Sign Up Form: Public Users || `index.html` <= `page.html`](https://github.com/iPoetDev/dash-and-do-github/issues/102)

    -   [x] STORY #54 [`New Registration User Story`: As a prospective user of the Dash and Do GitHub web app, I want to create an account by registering with the service so that I can be authorised to access the web service and have a newly created login (username and password)](https://github.com/iPoetDev/dash-and-do-github/issues/54)
    -   [x] STORY #66 [`Confirm Registered User Story`: As a prospective user of the Dash and Do GitHub web app, I want to receive a confirmation message by having registered with the service so that I can be verified and authenticated for authorisation and access to the web service and or be automatically logged in.](https://github.com/iPoetDev/dash-and-do-github/issues/66)

#### 14.2.3: Public Site: User Login, Account Authentication and Private Access.

 - Linked: 
     - *14.2.2: Account Creation*
     - *14.2.4: User Profile*
     - *14.2.5: Admin Site Access*
     - *14.2.9: User Session Management*

-   [x] FEATURE#103 [FEAT :: VIEW: PUBLIC: Existing User Access & Login Up Form: Public Users || `index.html` <= `page.html`](https://github.com/iPoetDev/dash-and-do-github/issues/103)

    -   [x] STORY #67 [`Existing Login User Story`: As an existing user, I want to find the login form, and have an option to remember me for next visit, as well as have an option to reset my password, so that I can successfully login.](https://github.com/iPoetDev/dash-and-do-github/issues/67) 
    -   [x] STORY #68 [`Unsuccessful Login Existing User Story`: As an existing user, I want to have a good user experience when I am unsuccessfully logging and have good notifications so that I have an improved user experience and increases my chance to login successfully](https://github.com/iPoetDev/dash-and-do-github/issues/68)
    -   [x] STORY #74 [`User Session Forgets Story`: As an authenticated user of Dash and Do GitHub web app, I want to have my session forgotten and the current session destroyed so that I have login and reauthenticate.](https://github.com/iPoetDev/dash-and-do-github/issues/74)

#### 14.2.4: Private Site: User Profile & User Data Management

 Linked: 14.2.3: User Login

-   [ ] FEATURE #144 [# FEAT :: User Profile and Account Management & `accounts.html` | APP: Profile](https://github.com/iPoetDev/dash-and-do-github/issues/144)

    -   [ ] STORY #75 [`User Profile Access Story`: As an authenticated user of Dash and Do GitHub web app, I want to access and read my user profile.](https://github.com/iPoetDev/dash-and-do-github/issues/75)
    -   [ ] STORY #76 [`User Profile Update Story`: As an authenticated user of Dash and Do GitHub web app, I want to be able to edit and modify my user profile details.](https://github.com/iPoetDev/dash-and-do-github/issues/76)
    -   [ ] STORY #77 [`User Profile Deletion Story`: As an authenticated user of Dash and Do GitHub web app, I want to be able to delete and remove my user profile data.](https://github.com/iPoetDev/dash-and-do-github/issues/77)
    -   [ ] STORY #78 [`User Account Removal Story`: As an authenticated user of Dash and Do GitHub web app, I want to be able to finally delete my account.](https://github.com/iPoetDev/dash-and-do-github/issues/78)

#### 14.2.5: Private Site: Staff User Access to Admin Site

 Linked: 
     - *14.2.3:  User Login*

-  [ ] FEATURE: Admin User

    -   [ ] STORY #79 [`Admin User Profile Access Story`: As an authorised administrator user (role) of Dash and Do GitHub web app, I want to access and read all user profile in a specific admin user interface (comes de-facto with Django).](https://github.com/iPoetDev/dash-and-do-github/issues/79)
    -   [ ] STORY #80 [`Admin User Profile Update Story`: As an authorised administrator user (role) of Dash and Do GitHub web app, I want to create, edit, modify, and remove user profiles in a specific admin user interface (comes de-facto with Django).](https://github.com/iPoetDev/dash-and-do-github/issues/80)

#### 14.2.6: Messaging the Site, Contact the Site Owner and Contact Form (Feature: # 101) 

- Linked: 
    - *14.2.8: Site Email Services*

-   [x] FEATURE #101 [FEAT :: VIEW: PUBLIC: Contact Email & Contact Form: All Users (Public Users and Private Users) || `index.html` <= `page.html`](https://github.com/iPoetDev/dash-and-do-github/issues/101)

    -   [x] STORY #126 [`Contact Site User Story`: As an anonymous or prospective user of the Dash and Do GitHub web app, I want to create a contact message and sent it to the site contact.](https://github.com/iPoetDev/dash-and-do-github/issues/126)
    -   [x] STORY #127 [`Contact Email User Story`: As an anonymous or prospective user of the Dash and Do GitHub web app, I want to send a message, with an optional copy to sender, to send to site contact and use Email as a service.](https://github.com/iPoetDev/dash-and-do-github/issues/127)

#### 14.2.7: Password Management: Reset, Verification and Change. (Feature: # 104) 

- Linked: 
    - *14.2.8: Site Email Services*

-   [ ] FEATURE #104 [FEAT :: VIEW: PUBLIC: Existing User Reset Passwords, Reset Password Form & Verify Reset: Public Users: || `verify.html` <= `simple.html`](https://github.com/iPoetDev/dash-and-do-github/issues/104)

    -   [ ] STORY #69 [`Forgets Password User Story`: As a forgetful user of the Dash and Do GitHub web app, I want to be able to reset my password and have a secure option to reset the password by an URI.](https://github.com/iPoetDev/dash-and-do-github/issues/69)
    -   [ ] STORY #70 [`Verify Password Reset User Story`: As a password resetting user of the Dash and Do GitHub web app, I want to be verified my newly reset password and have a secure option to reset the password by an URI.](https://github.com/iPoetDev/dash-and-do-github/issues/70)

#### 14.2.8: Site Email Services 

- Linked: 
    - *14.2.2: Account Creation*
    - *14.2.7. Password Management*
    - *14.2.6: Messaging the Site*

-   [ ] FEATURE #100
- 
    -   [ ] STORY 00.0
    -   [ ] STORY 00.0
    -   [ ] STORY 00.0
    -   [ ] STORY 00.0

#### 14.2.9: User Session Management

- Linked:
    - *14.2.3 User Login*
    - *14.2.10 User Permission*

-   [ ] FEATURE #??? User Session Management 

    -   [ ] STORY #71 [`Set + Persist Session User Story`: As a returning user of Dash and Do GitHub web app, I want to be immediately logged into my account so that I do not have to login and reuse my password on every visit, by using a remember check box on login (opt in).](https://github.com/iPoetDev/dash-and-do-github/issues/71)
    -   [ ] STORY #73 [`User Session Authorised Story`: As an authenticated user of Dash and Do GitHub web app, I want to authorised to access and persist this trusted state across one or more visits.](https://github.com/iPoetDev/dash-and-do-github/issues/73)
    -   [ ] STORY 00.0
    -   [ ] STORY 00.0

#### 14.2.10 User Permission Management 

- Linked:
    - 14.2.1 Public Pages
    - 14.2.1 Private Page
    - 14.2.3 User Login
    - 14.2.5: Admin Site

-   [ ] FEATURE #??? User Permission Management

    -   [ ] STORY #84 [`Unauthenticated User Login Story`: As an unauthenticated user, I want to not be able to restrict content and not have access to sensitive functionality so that all users have trust, confidence, integrity and availability in the web app and service](https://github.com/iPoetDev/dash-and-do-github/issues/84) 
    -   [ ] STORY #85 [`Unauthorised/access User Login Story`: As an unauthorised user, I want to not be able to restrict content and not have access to sensitive user data so that all users have trust, confidence, integrity and availability in the web app and service](https://github.com/iPoetDev/dash-and-do-github/issues/85)
    -   [ ] STORY 00.0
    -   [ ] STORY 00.0

#### 14.2.11 GitHub Features

-   [ ] FEATURE 00.0

    -   [ ] STORY 00.0
    -   [ ] STORY 00.0
    -   [ ] STORY 00.0
    -   [ ] STORY 00.0

---

### 14.3. [BDD & User Acceptance](#user-acceptance)

> SOLUTION: User Acceptance | User Story Testing

-   [ ] Criteria
-   [ ] Completed? 🛫

#### 14.3.1 BBD

- As per [BDD 101: Behavior-Driven Agile | Automation Panda.com](https://automationpanda.com/2017/02/01/bdd-101-bdd-and-agile/), 

##### 14.3.1.1 Top Level Concepts
- BBD - Behaviour Driven Testing: optimally used for **black box testing**, higher order testing for the user experience. Learn more from: [BDD | Automation Panda](https://automationpanda.com/bdd/)
- Gherkin - domain specific language for behaviour scenarios. Learn more from: [BDD 101: The Gherkin Language | Automation Panda](https://automationpanda.com/2017/01/26/bdd-101-the-gherkin-language/)
- Feature: A user product or feature under test. [In BDD, What Should Be A Feature? | Automation Panda](https://automationpanda.com/2017/10/19/in-bdd-what-should-be-a-feature/)
- Scenario: Generally known as a test case, that concisely frames the behaviour under test.
- Give | When | Then: The structure specification keywords that uses natural language. not jargon, for all users to understand.
- Declarative: A focus on what behaviour is to happen, not how, and the expected outcome. 
- Imperative: A focus on how behaviour operates, better suited to TDD and Unit testing.

##### 14.3.1.2  Further Reading: 

- [BDD | Automation Panda](https://automationpanda.com/bdd/)

##### 14.3.1.3 AI Assisted Feature-Scenario Writing

- The author crafted and shaped the JetBrains AI Assistant (beta) to _conversationally_ (i.e. back and forth prompt-output-refactor) define the following Feature-Scenario as User Acceptance.
- This was a productivity, time manage and neural diversity win for the author.
- The author edited, groomed, aligned with his manually edited Epics, Features, and User Stories.
- These are then sorted, as per[ Python Behave](https://behave.readthedocs.io/en/latest/gherkin/#feature-testing-layout) and [Behave Django](https://behave-django.readthedocs.io/en/stable/usage.html), in side and along side the package/apps under test, in `.feature` files 

##### 14.3.1.4 Manual over Automation

- The intent and use of this approach, for the stage and development maturity of the author, is on
    - Manual testing over automation
    - Discovery of the features and behaviours (successful and side effects) scenarios
    - The formation of the testing steps by breakdown and refinement of the  Scenario along the lines of user behaviour and expectations linked to each User Story

- Why not automate (yet):
    - Learning curve requirements, starting from a novice stand point.
    - Extra effort v time management prioritisation.
    - Additional complexity v risk prioritisation.
    - Additional requirements and supplementary tooling for test environment configuration, management and tear down.

All of these tests with have the `@manual` tag on each scenario, and maybe a few with `@automatable` just to indicate which could be automated in the future.

---

### 14.4 User Acceptance Testing

#### 14.4.1: Public & Private Site, Pages, Navigation

##### 14.4.1.1: Public Site, Pages & Navigation

-   [ ] **Requirement**: Public Site, Pages & Navigation
    - **Feature**: Public Site
        - **Gherkin File**: *PublicSite.feature*  
    - **Scenarios / Stories**:
        - #82: ` Newly Visiting User's URL Story ` [#54 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/54)
        - #81:  ` New Visting User Story ` [#81 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/81)
        - #?? ` Show/Hide of Public Navigation and Page Components ` [#?? GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/??)
        - #?? ` Site Branding ` [#?? GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/??)
        - #?? ` Site Functionality/Responsiveness for Tablets+ screens ` [#?? GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/??)
        - #?? ` Site Functionality/Responsiveness for Mobile only screen ` [#?? GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/??)

###### 14.4.1.1.1 **UAC**: **`User Acceptance Test & Result`**
        -  #82: ` Newly Visiting User's URL Story ` [#54 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/54)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```
**UAC**: **`User Acceptance Criteria`**
        -  #81:  ` New Visting User Story ` [#81 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/81)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```
**UAC**: **`User Acceptance Criteria`**
        -  #?? ` Show/Hide of Public Navigation and Page Components ` [#?? GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/??)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```
**UAC**: **`User Acceptance Criteria`**
        -  #?? ` Site Functionality/Responsiveness for Tablets+ screens ` [#?? GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/??)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```
**UAC**: **`User Acceptance Criteria`**
        -  #?? ` Site Functionality/Responsiveness for Mobile only screen ` [#?? GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/??)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```

---

##### 14.4.1.2 Private Site, Pages & Navigation

-   [ ] **Requirement**: Private Site, Pages & Navigation
    - **Feature**: Private Site
        - **User Acceptance Criteria**: *PrivateSite.feature*  
    - **Scenarios / Stories**:
        - #82: ` Newly Visiting User's URL Story ` [#54 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/54)
        - #81:  ` New Visting User Story ` [#81 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/81)
        - #??:  ` Private Navigation and Private Components` [#?? GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/??)
        - #??:  ` Site Functionality/Responsiveness for Tablet+ screens ` [#?? GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/??)

###### 14.4.1.2.1 **UAC**: **`User Acceptance Test & Result`**`**
        -  #82: ` Newly Visiting User's URL Story ` [#54 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/54)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```
- UAC
    - #81: ` New Visting User Story ` [#54 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/54)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```
 - UAC
    - #??: ` Private Navigation/Components `  [#?? GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/??)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```
 - UAC
    - #??: ` Site for Tablet+ Screens  `  [#?? GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/??)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```
 
---

#### 14.4.2 Public Site: Account Creation, User Registration and Signup Form 

-   [ ] **Requirement**: Public: Account Creation and User Registration
    - **Feature**: Account Creation
        - **User Acceptance Criteria**: *AccountCreate.feature*  
    - **Scenarios / Stories**:
        - #54: ` New Registration User Story ` [#54 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/54)
        - #66:  ` Confirm Register User Story ` [#66 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/66)

##### 14.4.2.1. **UAC**: **`User Acceptance Test & Result`**`**
   -  #54: ` New Registration User's URL Story ` [#54 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/54)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```
- UAC
    - #66:  ` Confirm Register User Story ` [#66 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/66)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```

---
#### 14.4.3 Private Site: User Login, Account Authentication and Login Form 

-   [ ] **Requirement**: Public: Account Creation and User Registration
    - **Feature**: UserLogin
        - **User Acceptance Criteria**: *UserLogin.feature*  
    - **Scenarios / Stories**:
        - #67:  ` Successful Login Existing User Story ` [#67 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/67)
        - #68:  ` Unsuccessfully Login Existing User Story ` [#68 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/68)
        - #74:  ` User Session Forgets Story ` [#74 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/74)

##### 14.4.3.1 **UAC**: **`User Acceptance Test & Result`**

   - #67:  ` Successful Login Existing User Story ` [#67 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/67)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```

  - #68:  ` Unsuccessfully Login Existing User Story ` [#68 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/68)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```

   - #74:  ` User Session Forgets Story ` [#74 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/74)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```

***

#### 14.4.4 Private Site: User Profile & User Data Management

-   [ ] **Requirement**: Private: User Profile Access, User Settings and Account Removal
    - **Feature**: User Profile
        - **User Acceptance Criteria**: *UserProfile.feature*  
    - **Scenarios / Stories**:
        - #75:  ` User Profile Access Story ` [#75 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/75)
        - #76:  ` User Profile Update Story ` [#76 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/76)
        - #77:  ` User Profile Deletion Story ` [#77 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/77)
        - #78:  ` User Account Removal Story ` [#78 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/78)

##### 14.4.4.1 **UAC**: **`User Acceptance Test & Result`**

   - #75:  ` User Profile Access Story ` [#75 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/75)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```

  - #76:  ` User Profile Update Story ` [#76 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/76)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```

   -  #77:  ` User Profile Deletion Story ` [#77 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/77)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```

   - #78:  ` User Account Removal Story ` [#78 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/78)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```

---

#### 14.4.5 Private Site: Staff User Access to Admin Site

-   [ ] **Requirement**: Private: Manage the Site, Be a Staff User and Access Admin Site
    - **Feature**: Administration Site with Staff User
        - **User Acceptance Criteria**: *AdminSite.feature*  
    - **Scenarios / Stories**:
        - #79:  ` Admin User Profile Access Story ` [#79 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/79)
        - #80:  ` Admin User Profile Update Story ` [#80 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/80)

##### 14.4.5.1 **UAC**: **`User Acceptance Test & Result`**

   - #79:  ` Admin User Profile Access Story ` [#79 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/79)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```

   - #80:  ` Admin User Profile Update Story ` [#80 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/80)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```

---

#### 14.4.6 Messaging Site: Contact the Site Owner and Contact Form

-   [ ] **Requirement**: All/Anonymous: Contact the Site Owner, Send Copy and Contact Form 
    - **Feature**: Messaging the Site
        - **User Acceptance Criteria**: *MessageSite.feature*  
    - **Scenarios / Stories**:
        - #126:  ` Contact Site: User Story ` [#126 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/126)
        - #127:  ` Contact Email: User Story ` [#127 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/127)

##### 14.4.6.1 **UAC**: **`User Acceptance Test & Result`**

   - #126:  ` Contact Site: User Story ` [#126 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/126)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```

   - #127:  ` Contact Email: User Story ` [#127 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/127)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```

---

#### 14.4.7 Public: Password Management: Reset, Verification and Change. 

-   [ ] **Requirement**: Password Management
    - **Feature**: PasswordManagement
        - **User Acceptance Criteria**: *PasswordManage.feature*  
    - **Scenarios / Stories**:
        - #69:  ` Forgets Password User Story ` [#69 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/69)
        - #70:  ` Verify Reset User Story ` [#70 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/70)

##### 14.4.7.1 **UAC**: **`User Acceptance Test & Result`**

   - #69:  ` Forgets Password User Story ` [#69 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/69)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```

   - #70:  ` Verify Reset User Story ` [#70 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/70)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```

---

#### 14.4.8 Site Email Services

-   [ ] **Requirement**: Site Email for Messaging, Account Creation, and Password Management 
    - **Feature**: EmailServices
        - **User Acceptance Criteria**: *EmailServices.feature*  
    - **Scenarios / Stories**:
        - #??:  ` ??: User Story ` [#?? GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/??)
        - #??:  ` ??: User Story ` [#?? GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/??)
        - #??:  ` ??: User Story ` [#?? GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/??)

##### 14.4.8.1 **UAC**: **`User Acceptance Test & Result`**


```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```


```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```

---

#### 14.4.9 User Session Management

-   [ ] **Requirement**: Site Email for Messaging, Account Creation, and Password Management 
    - **Feature**: UserSessions
        - **User Acceptance Criteria**: *UserSessions.feature*  
    - **Scenarios / Stories**:
        - #71:  ` Set + Persist Session: User Story ` [#71 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/71)
        - #73:  ` User Session Authorised: User Story ` [#73 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/73)

##### 14.4.8.1 **UAC**: **`User Acceptance Test & Result`**

   - #71:  ` Set + Persist Session: User Story ` [#?? GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/71)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```

   - #73:  ` User Session Authorised: User Story ` [#73 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/73)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```

---

#### 14.4.10 User Permission Management

-   [ ] **Requirement**: Site Email for Messaging, Account Creation, and Password Management 
    - **Feature**: EmailServices
        - **User Acceptance Criteria**: *EmailServices.feature*  
    - **Scenarios / Stories**:
        - #84:  ` Unauthenticated User Login Story ` [#84 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/84)
        - #85:  ` Unauthorised/Access User Login Story ` [#85 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/85)

##### 14.4.10.1 **UAC**: **`User Acceptance Test & Result`**

   - #84:  ` Unauthenticated User Login Story ` [#84 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/84)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```

   - #85:  ` Unauthorised/Access User Login Story ` [#85 GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/85)
```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```

---

#### 14.4.11 Private: GitHub Feature: Dashboard

-   [ ] **Requirement**: Private: GitHub Dashboard aka Dash; Report and Status
    - **Feature**: GitHubDashboard (CRU)
        - **User Acceptance Criteria**: *EmailServices.feature*  
    - **Scenarios / Stories**:
        - #??:  ` ??: User Story ` [#?? GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/??)
        - #??:  ` ??: User Story ` [#?? GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/??)
        - #??:  ` ??: User Story ` [#?? GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/??)

##### 14.4.11.1 **UAC**: **`User Acceptance Test & Result`**

```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```


```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```


```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```

---

#### 14.4.12 Private: GitHub Feature: Do & Actions 

-   [ ] **Requirement**: Private: GitHub Do aka Do; Actions: 
    - **Feature**: GitHub Do & Action (CRUD)
        - **User Acceptance Criteria**: *GitHubDofeature*  
    - **Scenarios / Stories**:
        - #??:  ` ??: User Story ` [#?? GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/??)
        - #??:  ` ??: User Story ` [#?? GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/??)
        - #??:  ` ??: User Story ` [#?? GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/??)

##### 14.4.12.1 **UAC**: **`User Acceptance Test & Result`**


```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```


```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```

---

#### 14.4.?? ??

-   [ ] **Requirement**: ??
    - **Feature**: ??
        - **User Acceptance Criteria**: ??.feature*  
    - **Scenarios / Stories**:
        - #??:  ` ??: User Story ` [#?? GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/??)
        - #??:  ` ??: User Story ` [#?? GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/??)
        - #??:  ` ??: User Story ` [#?? GitHub](https://github.com/iPoetDev/dash-and-do-github/issues/??)

##### 14.4.??.1 **UAC**: **`User Acceptance Test & Result`**

```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```


```
- The author has tested by <action> <resource/feature/story>
	- 1:
	- 2:
	- 3:
- As a user, the author can ...
- The result was ...
=============================================================
- UAT: `User Acceptance Test Statement`
  - .
- USER ACCEPTED: Yes ✅ | STOP 🚫
```

---

### 14.4. [Screenshots](#feature-screenshots)

> SOLUTION: Features

-   [ ] Criteria
-   [ ] Completed? 🛫

#### 14.5.1. Public & Private Site, Pages, Navigation

> SOLUTION: Feature | Screenshot

-   [ ] Criteria
-   [ ] Completed? 🛫
-   [ ] Screenshot of Public Pages, Private Pages
-   [ ] Screenshot of Public Components, Private Components
##### 14.4.1.1: Public Site, Pages & Navigation

![Index: Public] ()
**`SCREENSHOT-X.X: `** `:  Public: Index.html `

![About] ()
**`SCREENSHOT-X.X: `** `: Public: About.html `

![FAQ] ()
**`SCREENSHOT-X.X: `** `: Public: FAQ.html `

##### 14.4.2.1: Private Site, Pages & Navigation

![Index: Private] ()
**`SCREENSHOT-X.X: `** `: Private Page `

![Dash & Inform] ()
**`SCREENSHOT-X.X: `** `: Private Page: Dash & Inform `

![Do & Action] ()
**`SCREENSHOT-X.X: `** `: Private Page: Do & Inform  `

---

#### 14.5.2. Public Site: Account Creation, User Registration and Signup Form 

> SOLUTION: Feature | Screenshot

-   [ ] Criteria
-   [ ] Completed? 🛫
-   [ ] Screenshot of Account Creation

![Public: Signup] ()
**`SCREENSHOT-X.X: `** `: Public: Sign Up Form, Index.html  `

---

#### 14.5.3. Private Site: User Login, Account Authentication and Login Form 

> SOLUTION: Feature | Screenshot

-   [ ] Criteria
-   [ ] Completed? 🛫
-   [ ] Screenshot of User Login and Login Flow

![Public: Login] ()
**`SCREENSHOT-X.X: `** `:  Public: Login Up Form/Menu, Index.html `

---

#### 14.5.4.Private Site: User Profile & User Data Management

> SOLUTION: Feature | Screenshot

-   [ ] Criteria
-   [ ] Completed? 🛫
-   [ ] Screenshot of User Profile

![Private: User Profile] ()
**`SCREENSHOT-X.X: `** `: Private: account.html `

---

#### 14.5.5. Private Site: Staff User Access to Admin Site

> SOLUTION: Feature | Screenshot

-   [ ] Criteria
-   [ ] Completed? 🛫
-   [ ] Screenshot of Admin Site behind a user’s login

![] ()
**`SCREENSHOT-X.X: `** `: Admin Site Login `

![] ()
**`SCREENSHOT-X.X: `** `: Admin Site Page `

***
#### 14.5.6.  Messaging Site: Contact the Site Owner and Contact Form

> SOLUTION: Feature | Screenshot

-   [ ] Criteria
-   [ ] Completed? 🛫
-  [ ] Screenshot of contact form
 
![] ()
**`SCREENSHOT-X.X: `** `: Contact Form, Index.html`

***

#### 14.5.7. Public: Password Management: Reset, Verification and Change. 

> SOLUTION: Feature | Screenshot

-   [ ] Criteria
-   [ ] Completed? 🛫

![] ()
**`SCREENSHOT-X.X: `** `: Password Reset `

![] ()
**`SCREENSHOT-X.X: `** `: Password Verify `

***

#### 14.5.8. Site Email Services

> SOLUTION: Feature | Screenshot

-   [ ] Criteria
-   [ ] Completed? 🛫
-   [ ] Screenshots of email templates/verify pages

![] ()
**`SCREENSHOT-X.X: `** `: Email Template `

![] ()
**`SCREENSHOT-X.X: `** `: Email Verify Page `

***

#### 14.5.9. User Session Management

> SOLUTION: Feature | Screenshot

-   [ ] Criteria
-   [ ] Completed? 🛫
- Screenshot of remember me

![] ()
**`SCREENSHOT-X.X: `** `: Remember Me: On/Off: Set/Forget `

---

#### 14.5.10.User Permission Management

> SOLUTION: Feature | Screenshot

-   [ ] Criteria
-   [ ] Completed? 🛫
-   [ ] Side by side of public / private components/navigation

![] ()
**`SCREENSHOT-X.X: `** `: Public v Private Features `


---

#### 14.5.11. Private: GitHub Feature: Dashboard

> SOLUTION: Feature | Screenshot

-   [ ] Criteria
-   [ ] Completed? 🛫
-   [ ] Screenshot of Dash

![] ()
**`SCREENSHOT-X.X: `** `: GitHub Dashboard `

---

#### 14.5.12. Private: GitHub Feature: Do & Actions

> SOLUTION: Feature | Screenshot

-   [ ] Criteria
-   [ ] Completed? 🛫
-   [ ] Screen of 

![] ()
**`SCREENSHOT-X.X: `** `: GitHub Do & Action `


---
