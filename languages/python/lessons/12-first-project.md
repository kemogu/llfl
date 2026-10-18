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

Completion checks: add two tasks, reject an empty title, complete one task by ID, reject an unknown ID, restart, and confirm the tasks survived. Write the results in your progress log. This is a checkpoint: review earlier lessons if you cannot explain your own functions yet.

## Practice exercise

Implement the tracker in practice/task_tracker/. Add a short README with its run command and storage path. Run all six completion checks above and record what happened.

Before moving on, run your work, explain it in your own words, and record one thing you learned in [your progress log](../PROGRESS.md).

## Review questions

1. Why separate menu handling from task operations?
2. Why is an ID safer than a displayed list position?
3. How should a missing data file differ from malformed data?
4. Which earlier concepts does persistence require?
5. How would you prove that marking a task done survives a restart?
