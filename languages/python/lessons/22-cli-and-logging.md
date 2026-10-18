# Lesson 22: Command-line interfaces and logging

[Previous lesson](21-sqlite.md) · [Schedule](../SCHEDULE.md) · [Next lesson](23-capstone-build.md)

**Goal:** Expose predictable commands and record useful diagnostic information.

**Prerequisite:** Complete lesson 21 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

`argparse` parses command-line arguments and generates help. Unlike a menu that repeatedly asks for input, a CLI can perform one action per invocation, making it easier to automate.

Save this as `languages/python/practice/lesson_22.py`:

```python
import argparse
import logging

logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Greet a Python learner")
    parser.add_argument("name")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.WARNING,
        format="%(levelname)s: %(message)s",
    )
    logger.debug("Arguments parsed successfully")
    print(f"Hello, {args.name}!")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```

Run `python3 languages/python/practice/lesson_22.py Ada --verbose`, then try `--help`. A positional argument is required here; `--verbose` is an optional flag. `argparse` reports invalid command syntax for you.

Exit status zero conventionally means success; a nonzero status indicates failure. Keep user-facing output concise and route diagnostics through logging. Levels include DEBUG, INFO, WARNING, ERROR, and CRITICAL. Configure logging at the application entry point, and avoid recording secrets or unnecessary personal data.

For the tracker, `argparse` subparsers can represent `add`, `list`, and `done` commands. Let the CLI translate arguments into calls to your existing logic. Expected user errors should produce clear messages; unexpected failures should retain enough diagnostic information to debug.

## Practice exercise

Complete the five coding questions below. You will write the answers; the examples above are for studying.

### Set up your answer files

1. In your editor, create the folder `languages/python/practice/lesson_22/`.
2. Inside it, create `question_1.py`, `question_2.py`, `question_3.py`, `question_4.py`, and `question_5.py`.
3. Write each answer in its matching file. Work in question order; when a question needs an earlier function, copy it or use the shared module explicitly requested below.
4. Open a terminal at the repository root and run the first answer with the command below. Change the final filename to run each of the other answers. Use `python` or `py` instead of `python3` if needed on your system.

```bash
python3 languages/python/practice/lesson_22/question_1.py
```

For commands that require arguments, append the arguments described in that question. Unless instructed otherwise, keep input files and generated data inside this lesson's practice folder; paths in scripts run from the repository root must include that folder.

### When your answers are ready

Run every answer and compare it with the checks in its question. Save all five files and tell me: “Lesson 22 answers are ready in `languages/python/practice/lesson_22/`. Please check all five files.” I will review your code and help you correct it before we continue.

## Five coding questions

### Question 1: Create command parsing

**Answer file:** `question_1.py`

1. Copy your reusable tracker module into this lesson folder. Create cli.py with argparse subcommands add, list, and done; add takes a title and done an integer ID.
2. In question_1.py, call a guarded entry point that initially just prints the parsed arguments.
3. Run with --help, add "Study Python", list, and done 1; confirm parsing works and done abc is rejected.

### Question 2: Connect task operations

**Answer file:** `question_2.py`

1. Extend cli.py so parsed commands call your tracker functions and persist successful changes.
2. In question_2.py, call this entry point under a main guard.
3. Use a fresh practice data file to add two tasks, list them, and complete one. Check the saved state on a later invocation.

### Question 3: Configure the storage path

**Answer file:** `question_3.py`

1. Add a top-level --data argument to cli.py and pass its value into storage functions.
2. In question_3.py, expose the entry point; run once using --data followed by one practice path, then again using a different path.
3. Put the option before the subcommand, for example --data PATH list. Verify the two data files stay independent.

### Question 4: Add diagnostic logging

**Answer file:** `question_4.py`

1. Add a top-level --verbose flag and configure logging once in the CLI entry point.
2. In question_4.py, expose the entry point and compare list with --verbose list.
3. Check that the task output is the same while debug diagnostics appear only in verbose mode. Avoid logging the full contents of user records.

### Question 5: Return meaningful exit codes

**Answer file:** `question_5.py`

1. Make main() return 0 for success and a nonzero value for an unknown task ID; print a clear error for that case.
2. In question_5.py, use raise SystemExit(main()) under the main guard.
3. Run valid and unknown-ID commands and inspect their exit codes. In bash, run echo $? immediately after each command; expect zero only for success.
