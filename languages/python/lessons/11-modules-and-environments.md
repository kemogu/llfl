# Lesson 11: Modules and virtual environments

[Previous lesson](10-files-and-json.md) · [Schedule](../SCHEDULE.md) · [Next lesson](12-first-project.md)

**Goal:** Split code into modules and isolate a project environment.

**Prerequisite:** Complete lesson 10 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

A module is usually a `.py` file. Importing it lets another file reuse its definitions. Create these two files together in `languages/python/practice/`:

```python
# calculations.py
def add(left, right):
    return left + right
```

```python
# lesson_11.py
from calculations import add

def main():
    print(add(2, 3))

if __name__ == "__main__":
    main()
```

Run `python3 languages/python/practice/lesson_11.py`. The main guard runs `main()` when the file is executed directly, but not when it is imported. Other top-level statements still run on first import in an interpreter process. Avoid naming files `json.py` or `typing.py`, which can shadow standard library modules.

A virtual environment gives a project its own interpreter environment and installed packages. From the repository root:

```bash
python3 -m venv languages/python/.venv
source languages/python/.venv/bin/activate
python -m pip --version
```

On Windows PowerShell, activate with `languages/python/.venv/Scripts/Activate.ps1` instead. Activation changes which interpreter your shell finds; it is also possible to invoke the environment's interpreter by its full path. Use `deactivate` to leave an activated environment.

This course uses the standard library, so no third-party installation is required. When a project does need dependencies, use its environment and record them so someone else can reproduce the setup. Do not commit `.venv/` or `__pycache__/` directories. A package groups related modules; a regular package commonly contains an `__init__.py` file.

## Practice exercise

Complete the five coding questions below. You will write the answers; the examples above are for studying.

### Set up your answer files

1. In your editor, create the folder `languages/python/practice/lesson_11/`.
2. Inside it, create `question_1.py`, `question_2.py`, `question_3.py`, `question_4.py`, and `question_5.py`.
3. Write each answer in its matching file. Work in question order; when a question needs an earlier function, copy it or use the shared module explicitly requested below.
4. Open a terminal at the repository root and run the first answer with the command below. Change the final filename to run each of the other answers. Use `python` or `py` instead of `python3` if needed on your system.

```bash
python3 languages/python/practice/lesson_11/question_1.py
```

For commands that require arguments, append the arguments described in that question. Unless instructed otherwise, keep input files and generated data inside this lesson's practice folder; paths in scripts run from the repository root must include that folder.

### When your answers are ready

Run every answer and compare it with the checks in its question. Save all five files and tell me: “Lesson 11 answers are ready in `languages/python/practice/lesson_11/`. Please check all five files.” I will review your code and help you correct it before we continue.

## Five coding questions

### Question 1: Extract a module

**Answer file:** `question_1.py`

1. Create receipt.py beside your answer files and move total_cents() and format_receipt() into it.
2. In question_1.py, import the functions and print a receipt for Notebook at 250 cents with quantity 3.
3. Run the answer file and verify a total of 750 cents.

### Question 2: Use a main guard

**Answer file:** `question_2.py`

1. In question_2.py, import receipt functions and define main() to print a sample receipt.
2. Call main() only inside an if __name__ == "__main__" guard.
3. Run question_2.py directly and verify that exactly one receipt appears.

### Question 3: Check import behavior

**Answer file:** `question_3.py`

1. In question_3.py, import question_2 and then print Import complete.
2. Run question_3.py without calling question_2.main().
3. Check that only Import complete appears, with no receipt or input prompt.

### Question 4: Inspect your interpreter

**Answer file:** `question_4.py`

1. Create the virtual environment using the command in the lesson, then activate it.
2. In question_4.py, import sys and print sys.executable, sys.prefix, and sys.base_prefix.
3. Run with the environment's Python. Verify the executable points into .venv and the two prefixes differ.

### Question 5: Build a small entry point

**Answer file:** `question_5.py`

1. Import the receipt functions and define main() to ask for a name, integer price, and quantity.
2. Keep all input and printing inside main(), and guard its call.
3. Run with Notebook, 250, and 3 to get 750 cents; then temporarily import question_5 from question_3 and verify importing does not prompt or print.
