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

Complete the five coding questions below. You will write the answers; the examples above are for studying.

### Set up your answer files

1. In your editor, create the folder `languages/python/practice/lesson_23/`.
2. Inside it, create `question_1.py`, `question_2.py`, `question_3.py`, `question_4.py`, and `question_5.py`.
3. Write each answer in its matching file. Work in question order; when a question needs an earlier function, copy it or use the shared module explicitly requested below.
4. Open a terminal at the repository root and run the first answer with the command below. Change the final filename to run each of the other answers. Use `python` or `py` instead of `python3` if needed on your system.

```bash
python3 languages/python/practice/lesson_23/question_1.py
```

For commands that require arguments, append the arguments described in that question. Unless instructed otherwise, keep input files and generated data inside this lesson's practice folder; paths in scripts run from the repository root must include that folder.

### When your answers are ready

Run every answer and compare it with the checks in its question. Save all five files and tell me: “Lesson 23 answers are ready in `languages/python/practice/lesson_23/`. Please check all five files.” I will review your code and help you correct it before we continue.

## Five coding questions

### Question 1: Design and demonstrate adding

**Answer file:** `question_1.py`

1. Create a capstone project subfolder here with importable modules whose imports do not run the CLI. Write a README describing CLI, service, storage, and acceptance criteria.
2. Implement adding a task with a stable integer ID and nonempty title; in question_1.py, demonstrate adding through the service using temporary storage.
3. Verify two tasks get distinct IDs and a blank title is rejected. Keep project data separate from these demonstrations.

### Question 2: Demonstrate listing and filtering

**Answer file:** `question_2.py`

1. Implement listing all tasks or only unfinished tasks in the capstone service.
2. In question_2.py, build a fresh fixture containing one finished and one unfinished task.
3. Check that the all-task result has two records and the unfinished result has only one.

### Question 3: Demonstrate completion

**Answer file:** `question_3.py`

1. Implement completion by ID with a documented failure for unknown IDs.
2. In question_3.py, complete one of two fresh tasks and check both states.
3. Also try an unknown ID and verify a clear error without altering either task.

### Question 4: Demonstrate persistence

**Answer file:** `question_4.py`

1. Implement either validated JSON or SQLite storage, accepting a configurable path.
2. In question_4.py, save sample tasks in a temporary directory, discard the service instance, and create a new instance reading the same path.
3. Assert that IDs, titles, and completion states match. Include a test that invalid storage data is reported without being silently overwritten.

### Question 5: Connect and test the CLI

**Answer file:** `question_5.py`

1. Add add, list, done, --help, and --data support to the capstone CLI, documenting exact run and test commands.
2. Use question_5.py as a unittest script checking the service operations and persistence in temporary storage; also manually run the documented CLI commands.
3. Check all required behaviors before adding optional features. Keep the five answer scripts independently runnable and point them at the shared capstone modules.
