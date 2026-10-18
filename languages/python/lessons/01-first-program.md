# Lesson 01: Your first Python program

[Course overview](../README.md) · [Schedule](../SCHEDULE.md) · [Next lesson](02-variables-and-types.md)

**Goal:** Run a Python file and explain how Python executes it.

**Prerequisite:** None; start here.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

Python is a programming language: you write instructions and a Python interpreter executes them. A program usually runs from top to bottom. A **function** is a named operation; `print()` displays values. Text inside quotes is a **string**. Lines beginning with `#` are comments for people reading the code.

First, open a terminal in this repository and check your interpreter:

```bash
python3 --version
```

On some systems the command is `python` or `py` instead. Use whichever reports Python 3 throughout this course. If none is available, install Python 3 from [python.org](https://www.python.org/downloads/) and reopen the terminal.

Create `languages/python/practice/lesson_01.py` with your editor:

```python
# My first program
print("Hello, Python!")
print("I am learning to program.")
print(2 + 3)
```

From the repository root, run:

```bash
python3 languages/python/practice/lesson_01.py
```

You should see three lines, ending with `5`. Quoted `"2 + 3"` would print text instead of calculating a sum. Parentheses surround a function's arguments: the values passed to it.

Deliberately remove a closing quote, run again, and read the error's file, line number, and message. Restore the quote afterward. A `SyntaxError` means Python could not parse your instructions; mistakes are part of learning. If you see `>>>`, you are in the interactive interpreter, not a terminal command prompt. Use `exit()` to leave it.

## Practice exercise

Complete the five coding questions below. You will write the answers; the examples above are for studying.

### Set up your answer files

1. In your editor, create the folder `languages/python/practice/lesson_01/`.
2. Inside it, create `question_1.py`, `question_2.py`, `question_3.py`, `question_4.py`, and `question_5.py`.
3. Write each answer in its matching file. Work in question order; when a question needs an earlier function, copy it or use the shared module explicitly requested below.
4. Open a terminal at the repository root and run the first answer with the command below. Change the final filename to run each of the other answers. Use `python` or `py` instead of `python3` if needed on your system.

```bash
python3 languages/python/practice/lesson_01/question_1.py
```

For commands that require arguments, append the arguments described in that question. Unless instructed otherwise, keep input files and generated data inside this lesson's practice folder; paths in scripts run from the repository root must include that folder.

### When your answers are ready

Run every answer and compare it with the checks in its question. Save all five files and tell me: “Lesson 1 answers are ready in `languages/python/practice/lesson_01/`. Please check all five files.” I will review your code and help you correct it before we continue.

## Five coding questions

### Question 1: Print your name

**Answer file:** `question_1.py`

1. Write one print() call that displays your name.
2. Save and run the file.
3. Check that your name appears on one line without quotation marks.

### Question 2: Explain your goal

**Answer file:** `question_2.py`

1. Write two print() calls: one for your reason for learning Python and one for something you want to build.
2. Run the file and check that the messages appear on two lines in the order you wrote them.
3. Change the second message, save, and run again to confirm the output changes.

### Question 3: Calculate a result

**Answer file:** `question_3.py`

1. Use print() to display the result of 7 * 8. Leave the calculation outside quotation marks.
2. On another line, print the text 7 * 8 inside quotation marks.
3. Run the file. Check that one line is 56 and the other is 7 * 8.

### Question 4: Add comments

**Answer file:** `question_4.py`

1. Add a comment beginning with # that describes your program.
2. Below it, print a short greeting and the result of 2 + 3.
3. Run the file. Confirm that the greeting and 5 appear but the comment does not.

### Question 5: Fix a syntax error

**Answer file:** `question_5.py`

1. Type the broken statement print("I can fix errors) and run it once to see the SyntaxError.
2. Repair the missing quotation mark, save, and run again.
3. Submit the repaired file. Add a comment explaining what was missing; the program must print I can fix errors successfully.
