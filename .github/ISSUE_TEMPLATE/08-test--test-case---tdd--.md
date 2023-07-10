---
name: '08 TEST: Test Case | TDD |'
about: 'TEST: Unit | Manual | Automated | AI Generated | AI Prompted '
title: "[TEST/TDD]"
labels: ''
assignees: iPoetDev

---

#  `TEST`: Case - Unit Test
>  Arrange | Act | Assert | Behavioural

## 1. Related
>

- ADR: []( 'ADR:')
- EPIC: []( 'EPIC:')
- FEATURE: []( 'FEAT:')
- STORY: []( 'STORY:')
- ACCEPTANCE: []( 'ACCEPT:')

## 2. Test Statement
>

- File:
- Line:

```
- ARRANGE:
  - File|Line:
  - Target: Expression | Statement | Method | Class | Set of | File | Module | Component | Feature
  - System:
  - Init:
- ACT:
  - Expect:
  - Invoke:
- ASSERT:
  - 🔴 Fail:  No | Yes
  - 🟢 Pass:  No | Yes
  - 🟡 Refactor: No | Yes
  - 🔁 Repeat:  No | Yes
```
**COPY**: **`To Readme or Issue`**

### 2.1. Details
- [ ] ADR: ADR000X Select a testing JavaScript framework
- [ ] ADR: ADR000X Select a testing Python framework

| Style             | Language   | Framework    | Type             | Method |
| ----------------- | ---------- | ------------ | ---------------- | ------ |
| Unit              | JavaScript | JS: Jest     | State-base       | TDD    |
| White-Box Unit    |            | PY: Unittest | Interaction-base | TDD    |
| Regression        | Python     | PY: PyTest   |                  | TDD    |
| Black box testing | Django     | PY: DocTest  |                  | TDD    |
|                   |            | Py: Behave   |                  | BDD    |

- **Type**:
  - [ ] State-Based: `Verifying that the system under test produces correct results in a` **`result state`**
  - [ ] Interaction Based: `verifying that the system properly invokes certain methods via` **`interactions`**

---
## 3. **`Arrange`**
> Create and set up a system under test (Initialisation).

- [ ] System: Statement | Method | Object | Series of Statements, Objects
```python,javascript



```

---
## 4. **`Act`**
> Invoking the test action (Invocation).

- [ ] Test Focus:
- [ ] Result: Expected | Not Expected
```python,javascript



```

---
## 5. **`Assert`**
>Force unit fail and the pass (Invocation).>

- [ ] 🔴 Fail:
- [ ] 🟢 Pass:
- [ ] 🟡 Refactor:
- [ ] System: Statement | Method | Object | Series of Statements, Objects
```python,javascript



```

---
## 6. References
| TEST: Include resources

#### 6.1.1. Source
- [What is Unit Testing?, Toptal.com](https://www.toptal.com/qa/how-to-write-testable-code-and-why-it-matters)
- [Top 6 BEST Python Testing Frameworks](https://www.softwaretestinghelp.com/python-testing-frameworks/)

#### 6.1.2. JavaScript

#### 6.1.3. Python

###### 6.1.3.1.1. PyTest
- **Link to API:** [Pytest API](https://docs.pytest.org/en/latest/reference.html)
- **Download Link:** [Pytest](https://pypi.org/project/pytest/)

###### 6.1.3.1.2. Unittest
- **Link to API:** [Unittest API](https://docs.python.org/3/library/unittest.html)
- **Download Link:** [Unittest](https://github.com/Codewars/python-unittest)

###### 6.1.3.1.3. *Doctest*
- **Link to API**: [DocTest API](https://docs.python.org/2/library/doctest.html#basic-api)
- **Download Link**: [Doctest](https://github.com/onqtam/doctest)

###### 6.1.3.1.4. *Nose2*
- **Link to API**: [Plugins for Nose2](https://nose2.readthedocs.io/en/release-0.3/plugins.html)
- **Download Link**: [Nose2](https://pypi.org/project/nose2/)

###### 6.1.3.1.5. Testify
- **Link to API:** [Package files of Testify](https://godoc.org/github.com/stretchr/testify)
- **Download Link:** [Testify](https://pypi.org/project/testify/)

###### 6.1.3.1.6. Behave | BDD
- **Link to API:** [Behave User Guide](https://behave.readthedocs.io/en/latest/)
- **Download Link:** [Behave](https://pypi.org/project/behave/)

###### 6.1.3.1.7. Lettuce
- **Link to API:** [Lettuce Documentation](http://lettuce.it/tutorial/simple.html)
- **Download Link:** [Lettuce](https://pypi.org/project/lettuce/)
