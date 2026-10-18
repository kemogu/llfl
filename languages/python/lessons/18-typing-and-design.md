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

Annotate the public functions in your task tracker. Decide how searching for a missing task is represented: None or a documented exception. Update callers and tests to match that contract.

Before moving on, run your work, explain it in your own words, and record one thing you learned in [your progress log](../PROGRESS.md).

## Review questions

1. What can type hints communicate?
2. Does Python automatically reject every wrong argument type?
3. What does Optional[float] mean?
4. How does a Protocol describe an interface?
5. Why is validating loaded JSON still necessary in annotated code?
