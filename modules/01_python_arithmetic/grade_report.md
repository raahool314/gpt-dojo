# Grade Report: Module 01 — Variables, types & arithmetic

- **Verdict:** PASS (Attempt 2)
- **Date:** 2026-10-20
- **Examiner:** Examiner

---

## 1. Test Results

- **Visible tests:** 17 / 17 passed (`uv run pytest modules/01_python_arithmetic`)
- **Hidden tests:** 11 / 11 passed (`uv run pytest grading/hidden/01_python_arithmetic`)

All automated test suites pass completely. Code execution, numerical expressions, and type outputs meet the technical specifications.

---

## 2. Rubric Scores

| Dimension | Score (1-4) | Evidence |
|-----------|-------------|----------|
| **Correctness (tests)** | 4 | All 17 visible and 11 hidden tests pass with exact and tolerant comparisons. |
| **Conceptual explanation** | 3 | Correct, in own words: names are tags for values; right side evaluates before rebinding; types correctly identified in the units example (speed: float, time: float, distance: float). Does not yet reach the "explains a failure mode" level of 4. |
| **Shape & math reasoning** | 4 | Handled weighted average vs. simple average, conversion formula, and tax fractioning correctly. |
| **Debugging** | 3 | All 5 bugs in `buggy_arithmetic.py` fixed with clear explanatory comments above the fixes. |
| **Transfer** | 4 | Cyclist transfer task correctly computed leg distances, totals, and average speed without hints. |
| **Code quality** | 3 | Expressions are clean, readable, and properly formatted without unnecessary syntax. |

*Mastery thresholds met: no dimension below 3/4; all tests pass.*

---

## 3. Strengths

- **Mathematical accuracy:** Every calculation in `arithmetic.py` accurately models the required relationships.
- **Bug remediation:** Identified and corrected all logical and precedence flaws in `buggy_arithmetic.py` with explanatory comments.
- **Independent transfer:** Correctly computed total distance from two legs and derived average speed rather than averaging speeds directly.
- **Conceptual understanding:** Correctly distinguishes names (tags) from values (items) and explains that `=` in Python is a command, not an equation.

---

## 4. Closing Note

No gaps remain. Module 01 is passed. Proceed to Module 02 — Comparisons & decisions.
