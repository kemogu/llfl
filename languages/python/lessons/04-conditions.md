# Lesson 04: Conditions and decisions

[Previous lesson](03-input-and-strings.md) · [Schedule](../SCHEDULE.md) · [Next lesson](05-loops.md)

**Goal:** Use comparisons and boolean expressions to choose which code runs.

**Prerequisite:** Complete lesson 03 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

Programs make decisions with `if`, `elif`, and `else`. A condition is tested for truth. Python uses indentation to group statements; use four spaces for each indentation level.

```python
score = 76
if score >= 90:
    result = "excellent"
elif score >= 60:
    result = "passed"
else:
    result = "keep practicing"
print(result)
```

Only the first matching branch runs. Put more specific thresholds first: checking `score >= 60` first would also match a score of 95.

Comparisons include `==` (equal), `!=`, `<`, `<=`, `>`, and `>=`. Assignment `=` and comparison `==` have different purposes. Combine conditions with `and`, `or`, and `not`.

```python
age = 20
has_ticket = True
can_enter = age >= 18 and has_ticket
print(can_enter)
print(0 <= score <= 100)
```

Empty strings, empty collections, zero, and `None` are false in a boolean context. For example, `if not name:` can detect an empty name. `None` represents absence of a value; check it using `is None`.

`and` and `or` short-circuit: Python skips the right side when the left side already determines the result. This makes `name and name[0] == "A"` safe for an empty string. These operators actually return an operand, so the expression may return `""` rather than the boolean `False`.

## Practice exercise

Complete the five coding questions below. You will write the answers; the examples above are for studying.

### Set up your answer files

1. In your editor, create the folder `languages/python/practice/lesson_04/`.
2. Inside it, create `question_1.py`, `question_2.py`, `question_3.py`, `question_4.py`, and `question_5.py`.
3. Write each answer in its matching file. Work in question order; when a question needs an earlier function, copy it or use the shared module explicitly requested below.
4. Open a terminal at the repository root and run the first answer with the command below. Change the final filename to run each of the other answers. Use `python` or `py` instead of `python3` if needed on your system.

```bash
python3 languages/python/practice/lesson_04/question_1.py
```

For commands that require arguments, append the arguments described in that question. Unless instructed otherwise, keep input files and generated data inside this lesson's practice folder; paths in scripts run from the repository root must include that folder.

### When your answers are ready

Run every answer and compare it with the checks in its question. Save all five files, record your progress in [PROGRESS.md](../PROGRESS.md), and tell me: “Lesson 4 answers are ready in `languages/python/practice/lesson_04/`. Please check all five files.” I will review your code and help you correct it before we continue.

## Five coding questions

### Question 1: Check a passing score

**Answer file:** `question_1.py`

1. Ask for a score and convert it to an integer. For this question, assume an integer from 0 to 100.
2. Print passed when the score is at least 60; otherwise print keep practicing.
3. Run separately with 59 and 60 and check both branches.

### Question 2: Add an excellent category

**Answer file:** `question_2.py`

1. Read an integer score from 0 to 100.
2. Use if/elif/else to print excellent for 90–100, passed for 60–89, or keep practicing for 0–59.
3. Run with 59, 60, 89, and 90. Check that only one message appears per run.

### Question 3: Validate the range

**Answer file:** `question_3.py`

1. Read an integer score.
2. Print invalid score if it is below 0 or above 100; otherwise print valid score.
3. Test -1, 0, 100, and 101; only the first and last should be invalid.

### Question 4: Combine boolean conditions

**Answer file:** `question_4.py`

1. Create age and has_ticket variables.
2. Use and to decide whether someone aged at least 18 with a ticket can enter.
3. Change the values and rerun for age 17 with a ticket, age 18 without one, and age 18 with one; only the last should be allowed.

### Question 5: Build the complete score checker

**Answer file:** `question_5.py`

1. Read an integer score and reject out-of-range values before assigning a category.
2. Display exactly one of invalid score, excellent, passed, or keep practicing.
3. Test -1, 0, 59, 60, 89, 90, 100, and 101. You do not need to handle nonnumeric input until lesson 9.
