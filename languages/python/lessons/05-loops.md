# Lesson 05: Loops and repetition

[Previous lesson](04-conditions.md) · [Schedule](../SCHEDULE.md) · [Next lesson](06-collections.md)

**Goal:** Repeat work with for and while, and reason about when a loop ends.

**Prerequisite:** Complete lesson 04 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

A `for` loop visits each item in an iterable, an object that can supply items one at a time. `range(1, 4)` supplies 1, 2, and 3: its stop value is excluded.

```python
total = 0
for number in range(1, 6):
    total += number
print(total)  # 15
```

`+=` updates the existing value. Here `total` is an accumulator: it collects a result across iterations.

A `while` loop repeats while its condition is true. Something must eventually change the condition or execute `break`; otherwise the loop may run forever.

```python
attempts = 3
while attempts > 0:
    print(f"Attempts remaining: {attempts}")
    attempts -= 1
```

`break` exits the nearest enclosing loop. `continue` skips the rest of the current iteration and starts the next one. Use them when they simplify the logic, not to avoid thinking about the condition.

```python
for number in range(1, 8):
    if number % 2 == 0:
        continue
    print(number)  # 1, 3, 5, 7
```

Trace loops on paper: record each value of the loop variable and accumulator. This catches off-by-one mistakes. For accidental infinite terminal loops, Ctrl+C usually interrupts execution.

## Practice exercise

Complete the five coding questions below. You will write the answers; the examples above are for studying.

### Set up your answer files

1. In your editor, create the folder `languages/python/practice/lesson_05/`.
2. Inside it, create `question_1.py`, `question_2.py`, `question_3.py`, `question_4.py`, and `question_5.py`.
3. Write each answer in its matching file. Work in question order; when a question needs an earlier function, copy it or use the shared module explicitly requested below.
4. Open a terminal at the repository root and run the first answer with the command below. Change the final filename to run each of the other answers. Use `python` or `py` instead of `python3` if needed on your system.

```bash
python3 languages/python/practice/lesson_05/question_1.py
```

For commands that require arguments, append the arguments described in that question. Unless instructed otherwise, keep input files and generated data inside this lesson's practice folder; paths in scripts run from the repository root must include that folder.

### When your answers are ready

Run every answer and compare it with the checks in its question. Save all five files, record your progress in [PROGRESS.md](../PROGRESS.md), and tell me: “Lesson 5 answers are ready in `languages/python/practice/lesson_05/`. Please check all five files.” I will review your code and help you correct it before we continue.

## Five coding questions

### Question 1: Print a sequence

**Answer file:** `question_1.py`

1. Use a for loop and range() to print the integers from 1 through 5.
2. Print each number on a separate line.
3. Verify that 1 and 5 are included and 6 is not.

### Question 2: Accumulate a sum

**Answer file:** `question_2.py`

1. Set n = 5 and initialize a total to zero.
2. Use a loop to add every integer from 1 through n; do not use sum().
3. Print 15. Change n to 1 and verify that the result is 1.

### Question 3: Make a multiplication table

**Answer file:** `question_3.py`

1. Read a positive integer n; assume valid input for this question.
2. Loop over multipliers 1 through 10 and print one labeled multiplication per line.
3. For n = 3, check that the first line represents 3 * 1 = 3 and the last represents 3 * 10 = 30.

### Question 4: Use a while loop

**Answer file:** `question_4.py`

1. Set attempts = 3.
2. Use while to print the current value and decrease it by one each iteration.
3. Check that the output is 3, 2, 1 and the program then stops.

### Question 5: Validate and combine

**Answer file:** `question_5.py`

1. Read an integer n. If n is nonpositive, print an error and skip the calculations.
2. Otherwise use loops to calculate the sum from 1 through n and print its multiplication table from 1 through 10.
3. Test n values 0, -2, 1, and 5. For 5, the sum should be 15 and the last table result 50. Nonnumeric input handling is not required yet.
