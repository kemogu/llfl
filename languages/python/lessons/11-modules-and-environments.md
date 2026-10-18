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

Move your receipt calculation functions into receipt.py. Import them from a separate main script. Add a main guard and confirm importing the script does not ask for input or print a receipt.

Before moving on, run your work, explain it in your own words, and record one thing you learned in [your progress log](../PROGRESS.md).

## Review questions

1. What is a module?
2. What does the __name__ main guard prevent?
3. Why can naming your file json.py cause trouble?
4. What problem does a virtual environment solve?
5. Why use python -m pip with the intended interpreter?
