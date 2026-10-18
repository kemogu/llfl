# Lesson 12: Project: a persistent task tracker

[Previous lesson](11-modules-and-environments.md) · [Schedule](../SCHEDULE.md) · [Next lesson](13-classes.md)

**Goal:** Combine functions, collections, validation, modules, and JSON in a small application.

**Prerequisite:** Complete lesson 11 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

Build a terminal task tracker. Keep its first version small: add a task, list tasks, mark a task done, and quit. Each task can be a dictionary with `id`, `title`, and `done` fields. Store tasks in a list and save to a dedicated JSON file in `practice/`.

Start with pure logic:

```python
def add_task(tasks, title):
    title = title.strip()
    if not title:
        raise ValueError("Title must not be empty.")
    next_id = max((task["id"] for task in tasks), default=0) + 1
    task = {"id": next_id, "title": title, "done": False}
    tasks.append(task)
    return task

items = []
add_task(items, "Practice functions")
print(items)
```

The parenthesized expression supplies IDs one at a time; lesson 16 explains generators. `max(..., default=0)` handles an empty collection. IDs should remain attached to tasks even if you later change display order; a list position is not a reliable identity.

Build in this order: in-memory operations, menu loop, validation, then persistence. Use separate functions for reading a command, changing tasks, loading data, and saving data. On first run, a missing file can mean an empty task list. Invalid existing data should produce an error and stop saving until repaired.

Completion checks: add two tasks, reject an empty title, complete one task by ID, reject an unknown ID, restart, and confirm the tasks survived. Include the results when requesting review. This is a checkpoint: review earlier lessons if you cannot explain your own functions yet.

## Practice exercise

Complete the five coding questions below. You will write the answers; the examples above are for studying.

### Set up your answer files

1. In your editor, create the folder `languages/python/practice/lesson_12/`.
2. Inside it, create `question_1.py`, `question_2.py`, `question_3.py`, `question_4.py`, and `question_5.py`.
3. Write each answer in its matching file. Work in question order; when a question needs an earlier function, copy it or use the shared module explicitly requested below.
4. Open a terminal at the repository root and run the first answer with the command below. Change the final filename to run each of the other answers. Use `python` or `py` instead of `python3` if needed on your system.

```bash
python3 languages/python/practice/lesson_12/question_1.py
```

For commands that require arguments, append the arguments described in that question. Unless instructed otherwise, keep input files and generated data inside this lesson's practice folder; paths in scripts run from the repository root must include that folder.

### When your answers are ready

Run every answer and compare it with the checks in its question. Save all five files and tell me: “Lesson 12 answers are ready in `languages/python/practice/lesson_12/`. Please check all five files.” I will review your code and help you correct it before we continue.

## Five coding questions

### Question 1: Add tasks in memory

**Answer file:** `question_1.py`

1. Create tracker.py beside your answer files, with add_task(tasks, title) that rejects blank titles and assigns an integer ID.
2. In question_1.py, use it to add two tasks to an empty list and print their records.
3. Check that IDs differ, both titles are preserved, and done is False for each. Keep shared module imports free of input prompts.

### Question 2: List tasks

**Answer file:** `question_2.py`

1. Add a display function to tracker.py; show each task's ID, title, and completion state.
2. In question_2.py, demonstrate it with an empty list and with two sample tasks.
3. Check that an empty list produces a clear no-tasks message and the populated list shows both tasks.

### Question 3: Complete by ID

**Answer file:** `question_3.py`

1. Add a function to tracker.py that completes a matching task and raises ValueError for an unknown ID.
2. In question_3.py, create two tasks, complete one, and catch an attempted update to an unknown ID.
3. Check that only the chosen task becomes done and a helpful error appears for the unknown ID.

### Question 4: Save and reload

**Answer file:** `question_4.py`

1. Add JSON load/save functions to tracker.py; accept a path argument and validate loaded task records.
2. In question_4.py, save two tasks with one completed to a dedicated file in this practice folder, then load and print them.
3. Check that IDs, titles, and states survive. A missing file may give an empty list; malformed or invalid existing data must raise an error and remain unchanged.

### Question 5: Connect a menu

**Answer file:** `question_5.py`

1. In question_5.py, use tracker.py to implement add, list, done, and quit menu choices; load once at startup and save successful changes.
2. Try adding two tasks, rejecting a blank title, completing one task, rejecting an unknown ID, and restarting to check persistence.
3. Add a short README in this lesson folder with the run command, storage path, and results of those checks. Exit without saving if startup data is invalid.
