-   [ ] Completed?

## 11. [Code](#code)

> SOLUTION:

-   [ ] Criteria:

### 11.1. [Code Styles](#code-styles)

> SOLUTION: Code Styles, and Formatting.

-   [ ] Criteria
-   [ ] Completed? 🛫

-   .
-   .

#### 11.1.1. [Semantic HTML](#)

-   [ ] Criteria
-   [ ] Completed? 🛫

-   .
-   .

#### 11.1.2. [Modern CSS](#)

-   [ ] Criteria
-   [ ] Completed? 🛫

-   .
-   .

#### 11.1.3. [ECMA JavaScript](#)

-   [ ] Criteria
-   [ ] Completed? 🛫

-   .
-   .

#### 11.1.4. [Python](#)

-   [ ] Criteria
-   [ ] Completed? 🛫

-   .
-   .

---

### 11.2. [Code Linting](#code-linting)

> SOLUTION: Code Styles, and Formatting.

-   [ ] Criteria
-   [ ] Completed? 🛫

-   .
-   .

---

### 11.3. [Code Organisation](#code-org)

> SOLUTION: Conventions | Compatibility | Standards

-   [ ] Criteria
-   [ ] Completed? 🛫

-   Code Statement Naming Formats:
-   File Name Format:
-   Folder Name Format:

---

### 11.4. [Clean Robust Code](#clean-code)

> SOLUTION: Workflow: Commented Code | Dead Code | Broken Links | Robust Code | Exception Free

-   [x] Criteria: LO-06-Pass | LO-6.2-PASS ✅ 2023-07-06
-   [ ] Workflow: Code Integration's Code Review
-   [ ] Completed? 🛫

**CHECKLIST**

-   [ ] **Commented out code**:
    -   [ ] All Files have no commented out code. #OnCommit | #PreCommit 🛫
    -   [ ] No deployed code has commented out code. #OnDeploy | #PullRequest 🛫
    -   [ ] Have you asked SourceGraph AI (Cody) to inspect for commented out code #OnReview | #CodeReview
-   [ ] **Dead & Unused Code**:
    -   [ ] All Files have no dead/unused code. #OnCommit | #PreCommit 🛫
    -   [ ] No deployed code has no dead/unused code. #OnDeploy | #PullRequest 🛫
-   [ ] **Broken URI Links**:
    -   [ ] All Files have no dead code. #OnCommit | #PreCommit 🛫
    -   [ ] No deployed code has no dead code. #OnDeploy | #PullRequest 🛫
    -   [ ] Have you asked SourceGraph AI (Cody) to inspect for broken Links #OnReview | #CodeReview
-   [ ] **Robust Code**:

    -   [ ] No Critical HTTP Error Codes:
    -   [ ] No Python Exceptions or
    -   [ ] No User Face Web Application Stack Traces:
    -   [ ] Have you asked SourceGraph AI (Cody) to inspect for issues or errors #OnReview | #CodeReview

-   [ ]
    Source: [Cody AI Chat - Sourcegraph: Comments, Dead, Broken, Secrets](https://sourcegraph.com/cody/MjAyMy0wNy0wNlQxMTo1NTozMy4zNjZa)

---

### 11.5. [Code & Data Secrets](#secrets)

> SOLUTION: CRSF | DB STRINGS | SECRETS | ENVARS | .GITIGNORE

-   [ ] Criteria: LO-06-Pass | LO-6.4-PASS
-   [ ] CODY: Automation | Create a AI Prompt for inspection of a codebase.
-   [ ] Completed? 🛫

**CHECKLIST**

-   [ ] **CRSF**: Django's Cross Site Forgery Token:
    -   [ ] Is configured correctly and generated?
    -   [ ] Is added to the base Django template
    -   [ ] Is correctly arranged, and asserted in tests, in pre-commit etc?
    -   [ ] Have you asked SourceGraph AI (Cody) to inspect for tokens #OnReview | #CodeReview
-   [ ] **DB STRINGS**: e.g. Database Configuration | DB RBA Account | DB RBA Password
    -   [ ] Has no hardcoded database configuration in Django Settings. py #OnCommit | #PreCommit
    -   [ ] All database setting files correctly access the cloud host platform configvars #OnDeploy | #PullRequest
    -   [ ] Have you asked SourceGraph AI (Cody) to inspect for DB Strings #OnReview | #CodeReview
-   [ ] **SECRETS\***: e.g. Password | Access Tokens | API Keys:
    -   [ ] All Files do not contain secrets which are stored in a remote git repository (i.e. GitHub & Heroku).
            #OnCommit | #PreCommit 🛫
    -   [ ] All deployed files do not contain secrets which are stored in cloud hosted live production environment (i.e.
            Heroku). #OnDeploy | #PullRequest 🛫
    -   [ ] Is verified by a pre-commit hook?
-   [ ] **ENVARS**:
    -   [ ] Secrets configured, manually or by script automation, in platform secured environmental variables (i.e. GitHub
            EnVars & Heroku ConfigVars). #OnCommit | #PreCommit 🛫
    -   [ ] All deployed files correctly access the cloud host platform configvars #OnDeploy | #PullRequest
-   [ ] **.GITIGNORE**: All files that contain secrets etc are listed in the **`.gitignore`** file (i.e. GitHub & Heroku)
        #OnCommit | #PreCommit 🛫
-   [ ] **DJANGO DEBUG**: Ensure that Django's debug mode is disabled and set to **`FALSE`**

-   [ ]
    Source: [Cody AI Chat - Sourcegraph: Comments, Dead, Broken, Secrets](https://sourcegraph.com/cody/MjAyMy0wNy0wNlQxMTo1NTozMy4zNjZa)

---

### 11.6. Code Review

> SOLUTION: Workflow | Automation | Inspection | AI Prompts

-   [ ] Criteria: LO-06-Pass | LO-6.4-PASS
-   [ ] ADR: [ADR000X Select and Define an AI Agent to Criteria Code Inspect for each Code Review?]()

-   **Selected**: [Sourcegraph](https://sourcegraph.com/search)'s \* \*[Cody](#[Cody documentation (sourcegraph.com)](https://docs.sourcegraph.com/cody))\*\*
-   **Reason**: Has direct access to public repositories for inspecting target codebase.
-   **Use Cases**:
    -   1: Utilise Cody to answer prepared questions, like from [11.3](readme. md#clean-code '11.3 Clean & Robust
        Code')/[11.4](readme. md#secrets 'Code & Data Secrets') checklists, that aid satisfying assessment criteria which
        previously required manual, and error prone, inspection.

#### 11.6.1. AI Code Review

> SOLUTION: Automation | Inspection | AI Prompts

-   [ ] Criteria: LO-06-Pass | LO-6.4-PASS
-   [ ] Agent: CODY | Has direct access to Codebase
-   [ ] AI Use Case: AI Code Inspection & Review.
-   [ ] Completed? 🛫

-   [ ] Define a AI Agent Prompt to inspect Code for 11.3 and 11.4 Checks: Clean Code and Secrets.

```text: Code Inspect

```

AI Prompt: **`Code Inspect on Code Review`**

---

> #DO #TEST

---
