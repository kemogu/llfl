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

Add add, list, and done subcommands to your tracker. Include --help, a configurable data path, and nonzero exit status for invalid task IDs. Keep business logic outside argument parsing.

Before moving on, run your work, explain it in your own words, and record one thing you learned in [your progress log](../PROGRESS.md).

## Review questions

1. How does a positional argument differ from an optional flag?
2. What does argparse provide automatically?
3. What does an exit status of zero usually mean?
4. How should user-facing output differ from diagnostic logging?
5. Why keep argument parsing separate from task operations?
