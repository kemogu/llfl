# Lesson 18: Type hints and clear interfaces

[Previous lesson](17-decorators-and-context-managers.md) · [Schedule](../SCHEDULE.md) · [Next lesson](19-algorithms-and-performance.md)

**Goal:** Describe contracts and distinguish static checking from runtime validation.

**Prerequisite:** Complete lesson 17 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

Type hints document what values code expects. A static type checker can analyze those hints without executing every path. Python itself generally does not enforce them. This lesson uses built-in generic annotations supported in Python 3.9 and later.

```python
from typing import Optional, Protocol

def average(scores: list[float]) -> Optional[float]:
    if not scores:
        return None
    return sum(scores) / len(scores)

class Reporter(Protocol):
    def write(self, message: str) -> None:
        ...

class ConsoleReporter:
    def write(self, message: str) -> None:
        print(message)

def report_average(scores: list[float], reporter: Reporter) -> None:
    result = average(scores)
    if result is None:
        reporter.write("No scores")
    else:
        reporter.write(f"Average: {result:.1f}")

report_average([80.0, 90.0], ConsoleReporter())
```

`Optional[float]` means `float` or `None`. Check for `None` before treating the result as a number. A `Protocol` describes supported behavior structurally: ConsoleReporter need not inherit from Reporter to satisfy a static checker.

Hints make interfaces clearer, but data from a user or file still needs runtime validation. Avoid broad types that conceal useful information. A small function with a precise contract is easier to understand than a large function with many unrelated return shapes.

Run the example normally, then inspect the annotations in your editor. A dedicated static checker is optional for this standard-library course; running the interpreter alone does not perform static type checking.

## Practice exercise

Complete the five coding questions below. You will write the answers; the examples above are for studying.

### Set up your answer files

1. In your editor, create the folder `languages/python/practice/lesson_18/`.
2. Inside it, create `question_1.py`, `question_2.py`, `question_3.py`, `question_4.py`, and `question_5.py`.
3. Write each answer in its matching file. Work in question order; when a question needs an earlier function, copy it or use the shared module explicitly requested below.
4. Open a terminal at the repository root and run the first answer with the command below. Change the final filename to run each of the other answers. Use `python` or `py` instead of `python3` if needed on your system.

```bash
python3 languages/python/practice/lesson_18/question_1.py
```

For commands that require arguments, append the arguments described in that question. Unless instructed otherwise, keep input files and generated data inside this lesson's practice folder; paths in scripts run from the repository root must include that folder.

### When your answers are ready

Run every answer and compare it with the checks in its question. Save all five files and tell me: “Lesson 18 answers are ready in `languages/python/practice/lesson_18/`. Please check all five files.” I will review your code and help you correct it before we continue.

## Five coding questions

### Question 1: Annotate a calculation

**Answer file:** `question_1.py`

1. Define average(scores: list[float]) -> Optional[float], returning None for an empty list.
2. Print the results for [80.0, 90.0] and [].
3. Check for 85.0 and None and include the Optional import.

### Question 2: Handle an optional result

**Answer file:** `question_2.py`

1. Include your average function and call it with an empty list.
2. Check for None before formatting a numeric result, printing No scores when absent.
3. Repeat with [80.0, 90.0] and check for a formatted numeric average without an error.

### Question 3: Describe an interface

**Answer file:** `question_3.py`

1. Define a Reporter Protocol with write(message: str) -> None and a ConsoleReporter implementing that method.
2. Write an annotated function accepting a Reporter and use it to report an average.
3. Run with ConsoleReporter and check the message appears without requiring inheritance from Reporter.

### Question 4: Define a lookup contract

**Answer file:** `question_4.py`

1. Use a Task dataclass and define find_task(tasks: list[Task], task_id: int) -> Optional[Task].
2. Search sample tasks for one existing ID and one missing ID, checking for None in the caller.
3. Print the matching title for the existing ID and a clear missing message for the absent one.

### Question 5: Validate external data

**Answer file:** `question_5.py`

1. Write an annotated function accepting an object and validating that it is a task dictionary with integer id, string title, and boolean done.
2. Reject bad records with ValueError; reject boolean IDs too, since bool is a subclass of int. Use type(value) is int when an exact integer is required.
3. Demonstrate a valid record, a list, and a record with a string ID. Check that only the valid record passes, and note that annotations alone do not perform these checks.
