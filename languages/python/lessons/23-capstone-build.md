# Lesson 23: Capstone: design and build

[Previous lesson](22-cli-and-logging.md) · [Schedule](../SCHEDULE.md) · [Next lesson](24-capstone-review.md)

**Goal:** Build a maintainable task manager by combining the course skills.

**Prerequisite:** Complete lesson 22 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

Your capstone is a command-line task manager with persistent storage, tested logic, and clear documentation. Extend your earlier tracker so you can see how a small program evolves. Do not add features merely to use every concept from the course.

Required behavior:

- Add a task with a nonempty title and a stable integer ID.
- List tasks, optionally showing only unfinished tasks.
- Complete a task by ID; report missing IDs clearly.
- Preserve tasks across runs using either validated JSON or SQLite.
- Support --help and a configurable storage path.
- Test normal cases, invalid input, missing IDs, and persistence.

A possible layout inside `practice/capstone/` is:

```text
capstone/
    main.py
    models.py
    service.py
    storage.py
    tests/
        test_service.py
        test_storage.py
    README.md
```

This is a suggestion, not a requirement to split every small function into a new file. The service handles task rules; storage handles persistence; the CLI translates commands and displays results. Inject the storage dependency so service tests can use a simple in-memory substitute.

Write acceptance criteria before implementation. For example: “After adding a task, a second process lists the same ID and title.” Build one complete path from command to storage first, then add the other operations. Reuse earlier tests where their behavior still applies.

Optional extensions after the core works: tags, due dates, search, or export. Async is unnecessary for a small local tracker unless you add an actual concurrent I/O requirement. Avoid introducing it simply because it is an advanced topic.

## Practice exercise

Write a one-page design note and a feature checklist, then implement the required behavior. Record exact run and test commands in the capstone README. Keep optional features out until all required checks pass.

Before moving on, run your work, explain it in your own words, and record one thing you learned in [your progress log](../PROGRESS.md).

## Review questions

1. Which responsibilities belong in the CLI, service, and storage layers?
2. What acceptance criterion demonstrates persistence?
3. How will you test task rules without touching a real data file?
4. Which failure cases could otherwise cause data loss or confusing behavior?
5. Why might async be unnecessary for this project?
