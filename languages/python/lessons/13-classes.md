# Lesson 13: Classes and objects

[Previous lesson](12-first-project.md) · [Schedule](../SCHEDULE.md) · [Next lesson](14-dataclasses-and-composition.md)

**Goal:** Group related data and behavior without creating unnecessary abstractions.

**Prerequisite:** Complete lesson 12 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

A class defines a kind of object. Each instance has its own state; methods operate on instances. `self` is the conventional name for the instance parameter, supplied automatically when you call a method on an object.

```python
class Task:
    def __init__(self, title):
        if not title.strip():
            raise ValueError("Title must not be empty.")
        self.title = title.strip()
        self.done = False

    def complete(self):
        self.done = True

    def describe(self):
        marker = "x" if self.done else " "
        return f"[{marker}] {self.title}"

task = Task("Learn classes")
task.complete()
print(task.describe())
```

`__init__` initializes an instance after it is created. `self.title` and `self.done` are instance attributes. If you create two Task objects, completing one does not complete the other.

Be careful with mutable class attributes: placing `items = []` directly in a class body shares that list across instances. Put per-instance mutable state inside `__init__` instead.

Classes are useful when data and behavior naturally belong together or state has rules to preserve. Plain functions and dictionaries remain good choices for simple transformations. A leading underscore, such as `_items`, signals an internal implementation detail by convention; it does not enforce privacy.

JSON does not automatically serialize this Task object. Add an explicit conversion to a dictionary if persistence needs it, and reconstruct objects only after validating loaded data.

## Practice exercise

Create a BankAccount exercise class using integer cents, with deposit and withdraw methods. Reject nonpositive amounts and withdrawals beyond the balance. Use fictional data only; test two independent instances.

Before moving on, run your work, explain it in your own words, and record one thing you learned in [your progress log](../PROGRESS.md).

## Review questions

1. What is the difference between a class and an instance?
2. What does self refer to?
3. What is __init__ responsible for?
4. Why is a mutable class attribute risky for per-instance data?
5. When might a function and dictionary be simpler than a class?
