- [ ] Completed?

## 5. [Scope](#scope)

> PROJECT | SOLUTION:

- [ ] Criteria:
- [x] Completed? 🛫

### 5.1. Pre-conditions

> PROJECT | SOLUTION: Established | Pre-Know Conditions

- [ ] Criteria:
- [x] <small>Completed? 🛫 ✅ 2023-07-04</small>>

- The Project & Solution is delivered in an academic context.
- The Project & Solution is delivered inside a predefined timeboxed scope of 3 months.
- The Project is managed within the scope of an Agile project management methodology.
- The Deliverable is assessed and graded to a predefined evaluation schema and criteria.

---

### 5.2. Assumptions

> PROJECT | SOLUTION: Known unknowns | Unknown knowns

- [ ] Criteria:
- [x] Completed? 🛫 ✅ 2023-07-04

- It is assumed the developer is a student with no prior experience, at a minimum.
- It is assumed that the student developer has attempted HTML & CSS Essentials, JavaScript Essentials and Python
  Essentials.
- It is assumed that the student developer comprehends and can produced a deliverable that is a minimally viable
  product.
- It is assumed that the student developer can deliver the deliverable withing the allocated and predefined timeboxed
  scope of 3 months.

---

### 5.3. [Constraints](#contraints)

> PROJECT:

- [ ] Criteria:
- [x] Completed? 🛫✅ 2023-07-04

- An Agile Methodology is **mandated**, using Epic and User Stories as key artefacts.
- HTML, CSS and JavaScript are *recommended* front-end technologies.
- Python and Django (web framework) are *recommended* back-end technologies.
- Model View Controller is a *recommended* architectural design pattern, a code factoring principle.
- That CRUD as a data manipulation pattern is **mandated**.
- A relational database is implicitly **mandated**, and is constrained by cost/affordability and access.
- A local version source control toolset, that uses Git, is **mandated**.
- A remote version source control platform, like GitHub.com, is **mandated**.
- A cloud based hosting platform is *recommended*, though the ultimate selection of which is up to developer.
- A Readme is a **mandated** and conventional documentation pattern that utilises the markdown format.
- The Readme **must be** written in English.
- The Readme can follow a *recommend* structure.
- The web application **must have** a `lang` attribute set to English.

### 5.4 [Browsers Compatibility](#compatibilities)

> SOLUTION: Browser Install | Compatibility | Feature | Components | Target Audiences

- The application design for the web is further constrained by it's available global or local audience and their
  install-base of a browser.
- Browser compatibility is a essential aspect of a web application as the browser is the fundamental web application
  end-point
- Developer tools, like Autofixer (which tailwind recommends for aplpying browser vendor pre-fixes) aid in ensuring code
  compatibility and quality with Browsers
- So using these two services will aid the developer experience and utilmately the user experience

1. CanIUse
2. BrowserlIsr

#### 5.4.2 BrowserList

> SOLUTION: Developer Tool | Developer Experience | Audience Research | Browser Compatibility | Web App Performance

- Go
  to [Browserl.ist](https://browsersl.ist/#q=%3E0.3%25%2C+defaults%2C+supports+es6-module%2C+maintained+node+versions)
- View the query of the following in the above lint.
-
    - Added to` package.json` in root of project
- Audience coverage:97.3 %

```json
"browserslist": [
">0.3%, defaults and supports es6-module",
"maintained node versions"
]
``` 

---
> .
---
