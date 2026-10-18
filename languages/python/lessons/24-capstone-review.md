# Lesson 24: Capstone review and continued learning

[Previous lesson](23-capstone-build.md) · [Schedule](../SCHEDULE.md) · [Progress log](../PROGRESS.md)

**Goal:** Validate, explain, and improve your program using evidence.

**Prerequisite:** Complete lesson 23 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

Finishing a project means more than seeing one successful run. Review the behavior someone else would depend on. Use a fresh temporary data location and run through this checklist:

- Read --help and follow the README from a fresh terminal.
- Add two tasks, list them, complete one, and filter unfinished tasks.
- Restart and verify the IDs, titles, and completion state survive.
- Try an empty title, a missing ID, and an inaccessible storage path.
- If using JSON, try malformed and structurally invalid data without overwriting it.
- Run automated tests and verify they do not alter your working data.

For the suggested layout, run tests from `practice/capstone/` with:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

Read your code aloud. Explain each function's inputs, outputs, side effects, and failures. Look for duplicated validation, overly broad exception handlers, and unnecessary shared state. Refactor one issue at a time and rerun relevant tests. Measure before making performance changes.

Write a retrospective: what you can now do independently, what still needs help, one bug you investigated, and the next small project you want to build. Keep a short demonstration transcript and your test results as evidence.

This course introduces advanced Python concepts; expertise comes from applying them repeatedly. Choose a next direction based on your goals: automation, web development, data analysis, or deeper language internals. Build a focused project in that direction, consult its official documentation, and return to weak areas rather than rushing through more topics.

## Practice exercise

Complete the five coding questions below. You will write the answers; the examples above are for studying.

### Set up your answer files

1. In your editor, create the folder `languages/python/practice/lesson_24/`.
2. Inside it, create `question_1.py`, `question_2.py`, `question_3.py`, `question_4.py`, and `question_5.py`.
3. Write each answer in its matching file. Work in question order; when a question needs an earlier function, copy it or use the shared module explicitly requested below.
4. Open a terminal at the repository root and run the first answer with the command below. Change the final filename to run each of the other answers. Use `python` or `py` instead of `python3` if needed on your system.

```bash
python3 languages/python/practice/lesson_24/question_1.py
```

For commands that require arguments, append the arguments described in that question. Unless instructed otherwise, keep input files and generated data inside this lesson's practice folder; paths in scripts run from the repository root must include that folder.

### When your answers are ready

Run every answer and compare it with the checks in its question. Save all five files, record your progress in [PROGRESS.md](../PROGRESS.md), and tell me: “Lesson 24 answers are ready in `languages/python/practice/lesson_24/`. Please check all five files.” I will review your code and help you correct it before we continue.

## Five coding questions

### Question 1: Verify a fresh start

**Answer file:** `question_1.py`

1. Copy or reuse your completed capstone modules without changing working user data.
2. In question_1.py, write a test that creates a new temporary storage location and verifies that listing tasks starts empty.
3. Run the test and manually follow the README from a fresh terminal; record any missing setup instructions in comments.

### Question 2: Verify the full lifecycle

**Answer file:** `question_2.py`

1. In question_2.py, write a test that adds two tasks, completes one, and checks the unfinished filter.
2. Recreate the service using the same temporary storage and repeat the checks.
3. Assert that the same IDs, titles, and states survive the reload.

### Question 3: Verify failure behavior

**Answer file:** `question_3.py`

1. In question_3.py, add tests for an empty title, an unknown ID, and invalid storage input in a temporary location.
2. Check that failures are reported and valid existing records are not overwritten. For SQLite, use a separate non-database file as the invalid input.
3. Run the tests and confirm their cleanup leaves your normal capstone data unchanged.

### Question 4: Protect a refactor

**Answer file:** `question_4.py`

1. In question_4.py, add a regression test for a behavior affected by one small proposed refactor, such as extracting duplicated title validation.
2. Run it before the refactor, make the change, and run it again with the other tests.
3. Check that intended behavior remains the same and explain the simplification in a comment.

### Question 5: Demonstrate and reflect

**Answer file:** `question_5.py`

1. In question_5.py, build a short end-to-end demonstration using temporary storage: add, list, complete, reload, and display unfinished tasks.
2. Add comments explaining inputs, outputs, side effects, one bug you fixed, and one concept you need to practice further.
3. Run the demo, prepare a five-minute explanation, and record your next project idea in the progress log. Submit all five files and the capstone path for review.
