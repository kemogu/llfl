# Lesson 03: Input and string operations

[Previous lesson](02-variables-and-types.md) · [Schedule](../SCHEDULE.md) · [Next lesson](04-conditions.md)

**Goal:** Accept user input and clean, convert, and format text.

**Prerequisite:** Complete lesson 02 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

`input()` displays a prompt, waits for a line, and returns a string. It returns text even when the user types digits. Convert only when your program needs a number.

```python
name = input("Your name: ").strip()
age_text = input("Your age in whole years: ")
age = int(age_text)
print(f"Hello, {name}! Next year you will be {age + 1}.")
print(name.upper())
```

This example assumes a valid integer; typing `hello` for age raises `ValueError`. We will handle that in lesson 9. For now, notice the assumption instead of hiding it.

Strings have methods, which are operations called through a value, such as `name.upper()`. `strip()` removes surrounding whitespace, `lower()` produces lowercase text, and `replace("old", "new")` replaces matching pieces. These operations return new strings; they do not change the original string in place.

Indexing starts at zero: `"Python"[0]` is `"P"`. Negative indices count from the end, so `"Python"[-1]` is `"n"`. Slicing selects a range and excludes the end: `"Python"[1:4]` is `"yth"`. `len(text)` counts characters. Indexing an empty string raises `IndexError`, while a slice may safely return an empty string.

Try predicting `"  Ada  ".strip().lower()` before running it. Method calls can be chained because each result becomes the input to the next operation.

## Practice exercise

Complete the five coding questions below. You will write the answers; the examples above are for studying.

### Set up your answer files

1. In your editor, create the folder `languages/python/practice/lesson_03/`.
2. Inside it, create `question_1.py`, `question_2.py`, `question_3.py`, `question_4.py`, and `question_5.py`.
3. Write each answer in its matching file. Work in question order; when a question needs an earlier function, copy it or use the shared module explicitly requested below.
4. Open a terminal at the repository root and run the first answer with the command below. Change the final filename to run each of the other answers. Use `python` or `py` instead of `python3` if needed on your system.

```bash
python3 languages/python/practice/lesson_03/question_1.py
```

For commands that require arguments, append the arguments described in that question. Unless instructed otherwise, keep input files and generated data inside this lesson's practice folder; paths in scripts run from the repository root must include that folder.

### When your answers are ready

Run every answer and compare it with the checks in its question. Save all five files, record your progress in [PROGRESS.md](../PROGRESS.md), and tell me: “Lesson 3 answers are ready in `languages/python/practice/lesson_03/`. Please check all five files.” I will review your code and help you correct it before we continue.

## Five coding questions

### Question 1: Read a name

**Answer file:** `question_1.py`

1. Ask for a full name with input() and store the returned text.
2. Print a greeting containing the name.
3. Run with Ada Lovelace and check that the complete name appears.

### Question 2: Clean surrounding spaces

**Answer file:** `question_2.py`

1. Ask for a name and assign its stripped version to a variable.
2. Print the cleaned name between square brackets so spaces are visible.
3. Enter two spaces, Ada, then two spaces. The displayed result should be [Ada].

### Question 3: Normalize a language

**Answer file:** `question_3.py`

1. Ask for a favorite programming language.
2. Remove surrounding spaces and convert the result to lowercase.
3. Enter PYTHON with surrounding spaces and check that the result is python.

### Question 4: Measure and slice

**Answer file:** `question_4.py`

1. Ask for a name and remove surrounding spaces.
2. Print its length and its first three characters using a slice.
3. Check Ada gives 3 and Ada; Al gives 2 and Al; an empty input gives 0 and an empty slice without an error.

### Question 5: Combine the operations

**Answer file:** `question_5.py`

1. Ask for a full name and favorite language, then clean both inputs.
2. Print a sentence containing both, followed by the cleaned name length and its first three characters.
3. Test with Ada Lovelace and Python. The name length should be 12 and the slice should be Ada.
