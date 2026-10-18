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

Create a separate practice database, insert three tasks, mark one done by ID using parameters, and list unfinished tasks. Close and reopen the database to verify persistence.

Before moving on, run your work, explain it in your own words, and record one thing you learned in [your progress log](../PROGRESS.md).

## Review questions

1. What is a primary key?
2. Why pass SQL values through placeholders?
3. What does a transaction provide?
4. Does with connection close a sqlite3 connection?
5. What can happen if an UPDATE omits its intended WHERE clause?
