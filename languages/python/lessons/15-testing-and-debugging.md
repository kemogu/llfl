# Lesson 15: Automated tests and debugging

[Previous lesson](14-dataclasses-and-composition.md) · [Schedule](../SCHEDULE.md) · [Next lesson](16-iterators-and-generators.md)

**Goal:** Test behavior, cover edge cases, and investigate failures systematically.

**Prerequisite:** Complete lesson 14 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

A test arranges inputs, performs an action, and checks the result. Good tests describe observable behavior and fail when that behavior breaks. Python includes `unittest`.

Save this as `languages/python/practice/test_prices.py`:

```python
import unittest

def total_cents(price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError("Values must not be negative.")
    return price * quantity

class PriceTests(unittest.TestCase):
    def test_total(self):
        self.assertEqual(total_cents(250, 3), 750)

    def test_zero_quantity(self):
        self.assertEqual(total_cents(250, 0), 0)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            total_cents(250, -1)

if __name__ == "__main__":
    unittest.main()
```

Run from the repository root:

```bash
python3 -m unittest discover -s languages/python/practice -p 'test_*.py'
```

In a project, keep production functions in a separate module and import them into tests. Cover a normal case, a boundary case, and an error case. Test independence matters: one test should not require another test to run first. Use temporary directories for file tests rather than real user data.

When debugging, reproduce the issue with the smallest useful input, read the traceback, inspect values, form one hypothesis, and test it. `breakpoint()` enters the debugger when the line is reached; commands include `p expression`, `n` for next, and `c` to continue. Add a regression test once you fix a bug.

## Practice exercise

Add tests for adding a valid task, rejecting an empty title, completing a task, and rejecting an unknown ID. Deliberately break one behavior, confirm a test fails, then restore the implementation.

Before moving on, run your work, explain it in your own words, and record one thing you learned in [your progress log](../PROGRESS.md).

## Review questions

1. What are the arrange, act, and assert parts of a test?
2. What is a boundary case for total_cents?
3. How do you check that a function raises ValueError?
4. Why should tests be independent?
5. What is a regression test, and when should you add one?
