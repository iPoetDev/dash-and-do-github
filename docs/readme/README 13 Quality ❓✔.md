-   [ ] Alias: Quality
-   [ ] Completed?

## 13. [Quality](#quality)

> SOLUTION: Static Analysis | | Code Compliance | Code Style | Code Quality | Python | JavaScript

-   [ ] Criteria:
-   [ ] ADR:
-   [ ] Completed?

### 13.1. [Report](#quality-report)

> SOLUTION: Summary

-   [ ] Criteria:
-   [ ] ADR:
-   [ ] Completed?

| File                  | Type            | Linter(s)     | Validators    | All Passing | Pre-Commit | Commit | Code Review | Deploy |
| --------------------- | --------------- | ------------- | ------------- | ----------- | ---------- | ------ | ----------- | ------ |
|                       | html,css,js,py  |               |               |             |            |        |             |        |
| .                     |                 |               |               |             |            |        |             |        |
| .                     |                 |               |               |             |            |        |             |        |
| .                     |                 |               |               |             |            |        |             |        |
|                       |                 |               |               |             |            |        |             |        |
| SUMMARY: \*\*`Linting | Validators`\*\* | **`Pass`** ✅ | **`Fail`** 🚫 |

---

### 13.2. [HTML Validation: W3C](#html-validate-w3c)

> SOLUTION: Static Analysis | | Code Compliance | Code Style | Code Quality | HTML | W3C HTML

-   [ ] Criteria:
-   [ ] ADR:
-   [ ] Completed?

-   .
    **- Known Exceptions**:
    -   HTMX attributes, without `data-`, are not compatible with W3C HTML as HTMX is a javascript library that extend
        HTML but not compliant attributes for programming hypermedia API data exchange without using JavaScript

---

### 13.3. [CSS Validation](#css-validate-w3c)

> SOLUTION: Static Analysis | | Code Compliance | Code Style | Code Quality | W3C JigSaw

-   [ ] Criteria:
-   [ ] ADR:
-   [ ] Completed?

-   .
    **- Known Exceptions**:
    -   CSS Layers are not compatible with W3C JigSaw as CSS Layer is a modern feature (release, with cross-browser
        support, Q1 2023) and is ahead of the W3C Jigsaw validation rules.
    -   CSS Nesting are not compatible with W3C JigSaw as CSS Nesting is a modern feature (release, with cross-browser
        support, Q2 2023) and is ahead of the W3C Jigsaw validation rules.

---

### 13.4. [JavaScript](#js-qa)

> SOLUTION: Static Analysis | Code Compliance | Code Style | Code Quality | JavaScript

-   [ ] Criteria:
-   [ ] ADR:
-   [ ] Completed?

-   .
-   .

---

### 13.5. [Python](#python-qa)

> SOLUTION: Static Analysis | AutoPep | Code Compliance | Code Style | Code Quality | Python | Ruff | MyPy | PyLint

-   [ ] Criteria:
-   [ ] ADR:
-   [ ] Completed?

-   .
-   .

---

> #CHECK #QA #QUALITY #ASSURANCE #StaticAnalysis

---
