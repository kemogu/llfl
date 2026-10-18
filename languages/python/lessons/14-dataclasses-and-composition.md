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

Complete the five coding questions below. You will write the answers; the examples above are for studying.

### Set up your answer files

1. In your editor, create the folder `languages/python/practice/lesson_14/`.
2. Inside it, create `question_1.py`, `question_2.py`, `question_3.py`, `question_4.py`, and `question_5.py`.
3. Write each answer in its matching file. Work in question order; when a question needs an earlier function, copy it or use the shared module explicitly requested below.
4. Open a terminal at the repository root and run the first answer with the command below. Change the final filename to run each of the other answers. Use `python` or `py` instead of `python3` if needed on your system.

```bash
python3 languages/python/practice/lesson_14/question_1.py
```

For commands that require arguments, append the arguments described in that question. Unless instructed otherwise, keep input files and generated data inside this lesson's practice folder; paths in scripts run from the repository root must include that folder.

### When your answers are ready

Run every answer and compare it with the checks in its question. Save all five files, record your progress in [PROGRESS.md](../PROGRESS.md), and tell me: “Lesson 14 answers are ready in `languages/python/practice/lesson_14/`. Please check all five files.” I will review your code and help you correct it before we continue.

## Five coding questions

### Question 1: Model a task

**Answer file:** `question_1.py`

1. Create models.py with a Task dataclass containing id: int, title: str, and done: bool = False.
2. In question_1.py, create and print two Task objects.
3. Check that their titles and IDs differ and both start unfinished.

### Question 2: Keep lists independent

**Answer file:** `question_2.py`

1. Add a Project dataclass with name and tasks fields, using field(default_factory=list) for tasks.
2. In question_2.py, create two projects and append a task only to the first.
3. Verify that the first project has one task and the second has none.

### Question 3: Implement memory storage

**Answer file:** `question_3.py`

1. Create storage.py with MemoryStorage and save(tasks), storing a shallow copy of the supplied list.
2. In question_3.py, save a list and then append a new item to the original list.
3. Check that the stored list did not grow. Add a comment explaining that changes to contained mutable objects would still be shared.

### Question 4: Inject storage into a service

**Answer file:** `question_4.py`

1. Create service.py with TaskService(storage), an instance task list, and a method that calls storage.save(self.tasks).
2. In question_4.py, supply MemoryStorage, add a sample Task to the service list, and save.
3. Print the stored tasks and verify the service does not need a file path or file-writing code.

### Question 5: Swap implementations

**Answer file:** `question_5.py`

1. In question_5.py, define a different storage class with save(tasks) that prints the number of tasks received.
2. Supply it to the same TaskService and save two tasks.
3. Check that it reports 2 without changing TaskService. Explain the shared save interface in a comment.
