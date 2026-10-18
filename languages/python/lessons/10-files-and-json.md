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

Complete the five coding questions below. You will write the answers; the examples above are for studying.

### Set up your answer files

1. In your editor, create the folder `languages/python/practice/lesson_10/`.
2. Inside it, create `question_1.py`, `question_2.py`, `question_3.py`, `question_4.py`, and `question_5.py`.
3. Write each answer in its matching file. Work in question order; when a question needs an earlier function, copy it or use the shared module explicitly requested below.
4. Open a terminal at the repository root and run the first answer with the command below. Change the final filename to run each of the other answers. Use `python` or `py` instead of `python3` if needed on your system.

```bash
python3 languages/python/practice/lesson_10/question_1.py
```

For commands that require arguments, append the arguments described in that question. Unless instructed otherwise, keep input files and generated data inside this lesson's practice folder; paths in scripts run from the repository root must include that folder.

### When your answers are ready

Run every answer and compare it with the checks in its question. Save all five files, record your progress in [PROGRESS.md](../PROGRESS.md), and tell me: “Lesson 10 answers are ready in `languages/python/practice/lesson_10/`. Please check all five files.” I will review your code and help you correct it before we continue.

## Five coding questions

### Question 1: Save vocabulary

**Answer file:** `question_1.py`

1. Create a dictionary mapping python to programming language, loop to repetition, and variable to name for a value.
2. Write it as UTF-8 JSON to vocabulary.json inside this lesson's practice folder using with.
3. Run this script once and open the JSON file to confirm all three entries were saved. Rerunning intentionally replaces this practice file.

### Question 2: Load vocabulary

**Answer file:** `question_2.py`

1. Read the vocabulary.json created in question 1 without writing to it.
2. Print each word and meaning.
3. Check that all three entries appear. Keep loading separate from saving so later failure checks are meaningful.

### Question 3: Print quiz prompts

**Answer file:** `question_3.py`

1. Load the vocabulary dictionary.
2. Loop over the words and print What does WORD mean? with each actual word substituted.
3. Verify that three prompts appear without revealing their meanings. Collecting answers is optional.

### Question 4: Report load failures

**Answer file:** `question_4.py`

1. Load a user-supplied file path and catch FileNotFoundError and json.JSONDecodeError separately.
2. Create a separate broken.json practice file containing only {, and also choose a path that does not exist.
3. Run with each path and with the valid vocabulary file; check for distinct error messages and successful loading respectively. Do not overwrite any input file.

### Question 5: Validate the structure

**Answer file:** `question_5.py`

1. Load JSON and check that the result is a dictionary with string keys and string values.
2. Reject unsuitable data with a clear message instead of using it as vocabulary.
3. Test the valid file, a separate file containing [], and one containing {"word": 3}. Only the valid vocabulary file should be accepted.
