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

Complete the five coding questions below. You will write the answers; the examples above are for studying.

### Set up your answer files

1. In your editor, create the folder `languages/python/practice/lesson_15/`.
2. Inside it, create `question_1.py`, `question_2.py`, `question_3.py`, `question_4.py`, and `question_5.py`.
3. Write each answer in its matching file. Work in question order; when a question needs an earlier function, copy it or use the shared module explicitly requested below.
4. Open a terminal at the repository root and run the first answer with the command below. Change the final filename to run each of the other answers. Use `python` or `py` instead of `python3` if needed on your system.

```bash
python3 languages/python/practice/lesson_15/question_1.py
```

For commands that require arguments, append the arguments described in that question. Unless instructed otherwise, keep input files and generated data inside this lesson's practice folder; paths in scripts run from the repository root must include that folder.

### When your answers are ready

Run every answer and compare it with the checks in its question. Save all five files, record your progress in [PROGRESS.md](../PROGRESS.md), and tell me: “Lesson 15 answers are ready in `languages/python/practice/lesson_15/`. Please check all five files.” I will review your code and help you correct it before we continue.

## Five coding questions

### Question 1: Test adding a task

**Answer file:** `question_1.py`

1. Copy the reusable tracker.py from lesson 12 into this lesson folder, preserving your original version.
2. In question_1.py, write a unittest.TestCase that adds one task and checks its title, ID, and done state.
3. Include the unittest.main() guard, run the file, and confirm the test passes using a fresh task list.

### Question 2: Test invalid titles

**Answer file:** `question_2.py`

1. In question_2.py, write tests for empty and whitespace-only titles using assertRaises(ValueError).
2. Verify that the task list remains empty after each rejected add.
3. Run the file and check that every test passes independently.

### Question 3: Test completion

**Answer file:** `question_3.py`

1. In question_3.py, create two tasks in a fresh list and complete one by ID.
2. Assert that the selected task is done and the other is not.
3. Run the file and confirm that no existing JSON file is required.

### Question 4: Test unknown IDs

**Answer file:** `question_4.py`

1. In question_4.py, try completing an ID that is absent from a fresh sample task list.
2. Assert that ValueError is raised and existing completion states remain unchanged.
3. Run the tests and verify they pass.

### Question 5: Confirm a test catches a bug

**Answer file:** `question_5.py`

1. In question_5.py, add a regression test proving that completing the second task does not complete the first.
2. Temporarily change your local tracker copy to complete the wrong task and run the test; confirm failure, then restore the correct code.
3. Run all five answer files again and record the observed failure in a comment. Submit only the restored implementation and passing tests.
