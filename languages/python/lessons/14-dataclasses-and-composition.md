# Lesson 14: Dataclasses and composition

[Previous lesson](13-classes.md) · [Schedule](../SCHEDULE.md) · [Next lesson](15-testing-and-debugging.md)

**Goal:** Model data conveniently and combine objects through small interfaces.

**Prerequisite:** Complete lesson 13 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

A dataclass generates routine methods such as initialization and a readable representation from declared fields. It helps when the main purpose of an object is to hold data.

```python
from dataclasses import dataclass, field

@dataclass
class Project:
    name: str
    tasks: list = field(default_factory=list)

    def add(self, title):
        self.tasks.append(title)

project = Project("Python practice")
project.add("Review classes")
print(project)
```

`default_factory=list` creates a fresh list for each instance. An annotation such as `name: str` describes an intended type but does not automatically enforce it at runtime.

**Composition** means building an object from other objects: a service can hold a storage object and call `storage.save(tasks)`. **Inheritance** means defining a specialized class based on another class. Prefer composition when the relationship is “uses” or “has”; use inheritance when the specialized object can reliably fulfill the base object's contract.

Python also supports duck typing: code can use any object offering the needed behavior, without requiring a shared parent class. Two storage implementations might both expose `save(tasks)`, one keeping a copy in memory for tests and one writing JSON.

Do not replace every dictionary with a class. Choose a model because it clarifies responsibilities, and keep the number of concepts small. If you use a dataclass for persisted data, conversion and input validation are still separate responsibilities.

## Practice exercise

Create a Task dataclass and a TaskService that receives a storage object. Implement a MemoryStorage with a save method. Show that the service can save through this object without knowing anything about files.

Before moving on, run your work, explain it in your own words, and record one thing you learned in [your progress log](../PROGRESS.md).

## Review questions

1. What routine code can a dataclass generate?
2. Why use default_factory=list?
3. How do composition and inheritance differ?
4. What does duck typing allow?
5. Why does a str annotation not guarantee that a field contains a string?
