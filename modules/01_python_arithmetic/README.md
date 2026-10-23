# Module 01: Variables, types & arithmetic

## Objectives
- Write and run short scripts using numbers and variables
- Calculate totals, differences, fractions, and simple unit conversions
- Predict intermediate values before executing

## Task 1 — EXPLAIN  (answer in `explain.md`)

In Python, `x = 5` is called an **assignment statement**.

Explain, in your own words, what the difference is between the **name** `x` and the **value** `5`. Why does `x = x + 1` make sense as a statement, even though it looks like a contradiction in ordinary algebra?
Answer: The name `x` is a tag and the value `5` is an item. What an assignment does is tag the value `5` with the name `x`. The idea `x = x + 1` conveys that add 1 to the value currently tagged by `x` and then tag the new value which is `6` in this case and untag the existing value to be cleared quietly by python.

Use at least one example with **units** (e.g., `total_cost = item_price + tax`) to show how names help you track what a value represents. Also state what **type** each value has in your example.
Answer: This could be one example `circumference = 3.14 * diameter` , the names here make it easy to identify that they relate to a circle and represent a numeric value. The type of circumference and diameter in this case is `float`.

## Task 2 — IMPLEMENT  (file: `arithmetic.py`)

Open `modules/01_python_arithmetic/arithmetic.py`. You'll find input variables already set. Replace each `None` with an expression that computes the requested value.

Do **not** change the input values. Do **not** use `input()`, `print()`, or `if` statements — this task is just arithmetic expressions.

Check your work:
```
uv run pytest modules/01_python_arithmetic
```

## Task 3 — DEBUG  (file: `buggy_arithmetic.py`)

Open `modules/01_python_arithmetic/buggy_arithmetic.py`. It's supposed to compute several values but produces wrong results.

Find and fix **every** bug. For each fix, add a one-line comment (starting with `#`) immediately above the corrected line explaining what was wrong.

Run the tests again — the debug cases will also be checked.

## Task 4 — TRANSFER

A cyclist rides at **18 km/h** for **2.5 hours**, then at **12 km/h** for **1.5 hours**.

Open `modules/01_python_arithmetic/arithmetic.py` again. Below the existing code (after a blank-line separator), add new variable assignments to compute:

1. `distance_leg1` — distance covered in the first leg (km)
2. `distance_leg2` — distance covered in the second leg (km)
3. `total_distance` — total distance (km)
4. `total_time` — total time (hours)
5. `average_speed` — average speed for the whole trip (km/h)

Use the relationship: **distance = speed × time**.

## Mastery criteria
- All visible and hidden tests pass
- Rubric: no dimension below 3/4
