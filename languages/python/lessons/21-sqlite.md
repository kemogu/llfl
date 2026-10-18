# Lesson 21: SQLite and parameterized queries

[Previous lesson](20-concurrency-and-async.md) · [Schedule](../SCHEDULE.md) · [Next lesson](22-cli-and-logging.md)

**Goal:** Persist records in a database and query them safely.

**Prerequisite:** Complete lesson 20 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

SQLite is an embedded relational database available through Python's `sqlite3` module. Tables contain rows and columns; a primary key identifies a row. This demonstration uses an in-memory database, so it does not alter a project data file.

```python
import sqlite3

connection = sqlite3.connect(":memory:")
try:
    with connection:
        connection.execute(
            "CREATE TABLE tasks (id INTEGER PRIMARY KEY, title TEXT NOT NULL, done INTEGER NOT NULL)"
        )
        connection.execute(
            "INSERT INTO tasks (title, done) VALUES (?, ?)",
            ("Learn SQLite", 0),
        )
    rows = connection.execute(
        "SELECT id, title FROM tasks WHERE done = ? ORDER BY id", (0,)
    ).fetchall()
    print(rows)
finally:
    connection.close()
```

Pass values separately using `?` placeholders. Do not build SQL by interpolating user input into the query string. Parameter binding handles values correctly and helps prevent SQL injection. Placeholders represent values, not arbitrary table or column names.

A transaction groups related changes so they can succeed or roll back together. With this connection's default transaction behavior, the connection context manager commits pending work on successful exit or rolls it back on failure; it does not close the connection. Closing is a separate responsibility, shown in `finally`.

Replace `":memory:"` with a deliberate file path to persist a database. Learn `SELECT`, `INSERT`, `UPDATE`, and `DELETE`, and always think about the `WHERE` clause before modifying rows. Use a practice database. For large results, iterating over a cursor avoids loading every row at once with `fetchall()`.

## Practice exercise

Complete the five coding questions below. You will write the answers; the examples above are for studying.

### Set up your answer files

1. In your editor, create the folder `languages/python/practice/lesson_21/`.
2. Inside it, create `question_1.py`, `question_2.py`, `question_3.py`, `question_4.py`, and `question_5.py`.
3. Write each answer in its matching file. Work in question order; when a question needs an earlier function, copy it or use the shared module explicitly requested below.
4. Open a terminal at the repository root and run the first answer with the command below. Change the final filename to run each of the other answers. Use `python` or `py` instead of `python3` if needed on your system.

```bash
python3 languages/python/practice/lesson_21/question_1.py
```

For commands that require arguments, append the arguments described in that question. Unless instructed otherwise, keep input files and generated data inside this lesson's practice folder; paths in scripts run from the repository root must include that folder.

### When your answers are ready

Run every answer and compare it with the checks in its question. Save all five files and tell me: “Lesson 21 answers are ready in `languages/python/practice/lesson_21/`. Please check all five files.” I will review your code and help you correct it before we continue.

## Five coding questions

### Question 1: Create a practice database

**Answer file:** `question_1.py`

1. Connect to tasks.db in this lesson's practice folder and create a tasks table with integer primary key id, title text, and done integer using CREATE TABLE IF NOT EXISTS.
2. Commit as needed and close the connection explicitly.
3. Run twice and check that both runs succeed; never reset or delete existing rows as part of setup.

### Question 2: Insert sample tasks

**Answer file:** `question_2.py`

1. Open the practice database and insert three titled tasks with done = 0 using placeholders.
2. Commit, query the rows ordered by ID, and print them before closing.
3. On a fresh database expect three rows. Run this insertion script only once unless you intentionally want three additional rows.

### Question 3: Complete one task

**Answer file:** `question_3.py`

1. Prompt for an existing task ID from question 2 and convert it to an integer.
2. Use a parameterized UPDATE with a WHERE clause to set that task's done value to 1, then commit.
3. Query all rows and verify that only the chosen task changed. Handle an unknown ID with a clear message.

### Question 4: Filter unfinished tasks

**Answer file:** `question_4.py`

1. Open a new connection and select only rows whose done value is 0, ordered by ID.
2. Print their IDs and titles, then close the connection.
3. After the initial three inserts and one completion, expect exactly two unfinished rows.

### Question 5: Verify persistence and rollback

**Answer file:** `question_5.py`

1. Open a fresh connection and confirm the previously completed task still has done = 1.
2. Within a connection transaction block, insert a temporary task and deliberately raise ValueError; catch it outside that block.
3. Query afterward and verify that the temporary insert was rolled back while earlier committed tasks remain. Close the connection in finally.
