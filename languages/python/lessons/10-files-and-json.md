# Lesson 10: Files, paths, and JSON

[Previous lesson](09-exceptions.md) · [Schedule](../SCHEDULE.md) · [Next lesson](11-modules-and-environments.md)

**Goal:** Save and load structured data while managing files safely.

**Prerequisite:** Complete lesson 09 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

`pathlib.Path` represents a filesystem path. Relative paths are resolved against the current working directory, which may differ from the directory containing the script. Run this course's examples from the repository root unless told otherwise.

```python
import json
from pathlib import Path

path = Path("languages/python/practice/demo_tasks.json")
path.parent.mkdir(parents=True, exist_ok=True)
tasks = [{"title": "Study Python", "done": False}]
with path.open("w", encoding="utf-8") as file:
    json.dump(tasks, file, indent=2)
with path.open("r", encoding="utf-8") as file:
    loaded = json.load(file)
print(loaded[0]["title"])
```

`with` closes the file when the block ends, including when an exception occurs. Mode `"r"` reads, `"w"` writes and replaces existing contents, and `"a"` appends. This example overwrites only its demonstration file; use deliberate paths when saving your own data.

JSON stores objects, arrays, strings, numbers, booleans, and null. Python dictionaries and lists map naturally to objects and arrays; `None` maps to null. JSON does not directly preserve arbitrary Python class instances or sets.

Loading can fail with `FileNotFoundError` or `json.JSONDecodeError`. Even valid JSON might have the wrong structure, so verify expected fields and types before using it. A malformed file should produce a clear error; silently treating it as empty data and saving again can destroy information.

## Practice exercise

Save three vocabulary words and their meanings to a new JSON file in practice/. Load them and print a quiz prompt for each word. Report missing and malformed files separately.

Before moving on, run your work, explain it in your own words, and record one thing you learned in [your progress log](../PROGRESS.md).

## Review questions

1. What does a relative path depend on?
2. Why use with when opening a file?
3. How do modes "w" and "a" differ?
4. Which exception can invalid JSON raise?
5. Why must you validate data even after JSON parsing succeeds?
