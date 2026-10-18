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

Write a program that prints your name, your reason for learning Python, and the result of multiplying 7 by 8. Run the saved file twice, changing one message between runs.

Before moving on, run your work, explain it in your own words, and record one thing you learned in [your progress log](../PROGRESS.md).

## Review questions

1. What is the role of the Python interpreter?
2. How is print("2 + 3") different from print(2 + 3)?
3. What does a line beginning with # do?
4. Which command runs your saved lesson_01.py file from the repository root?
5. What happens when a string is missing its closing quote, and how would you fix it?
