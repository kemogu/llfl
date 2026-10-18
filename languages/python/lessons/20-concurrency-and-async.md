# Lesson 20: Concurrency and async programming

[Previous lesson](19-algorithms-and-performance.md) · [Schedule](../SCHEDULE.md) · [Next lesson](21-sqlite.md)

**Goal:** Distinguish waiting from computation and use cooperative async tasks.

**Prerequisite:** Complete lesson 19 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

Concurrency lets multiple tasks make progress over overlapping periods. Parallelism means tasks actually execute simultaneously. Waiting for network or disk work is different from doing CPU-heavy calculations.

`asyncio` provides cooperative concurrency. An `async def` defines a coroutine function; calling it creates a coroutine object. `await` waits for an awaitable operation and can give other tasks an opportunity to run.

```python
import asyncio

async def fetch_label(label, delay):
    await asyncio.sleep(delay)  # Simulate waiting without a network
    return f"Ready: {label}"

async def main():
    results = await asyncio.gather(
        fetch_label("first", 0.2),
        fetch_label("second", 0.1),
    )
    print(results)

if __name__ == "__main__":
    asyncio.run(main())
```

`gather` schedules these coroutines concurrently and returns results in argument order. Awaiting each separately would finish the first before starting the second. This standalone script uses `asyncio.run`; notebook environments may already have a running loop and instead support `await main()`.

Calling `time.sleep()` inside a coroutine blocks its event-loop thread. Making a function async does not automatically make blocking work nonblocking. Threads can help with blocking I/O; processes can help with CPU-heavy Python work. Traditional GIL-enabled CPython generally limits parallel execution of Python bytecode by threads; interpreter configuration matters.

Concurrent work also needs limits, timeouts, and a failure policy. Use `asyncio.wait_for()` to apply a timeout and consider cancellation cleanup. With default gather behavior, one failure is propagated, but you should not assume every other operation has automatically stopped. Start with independent operations before introducing shared mutable state.

## Practice exercise

Complete the five coding questions below. You will write the answers; the examples above are for studying.

### Set up your answer files

1. In your editor, create the folder `languages/python/practice/lesson_20/`.
2. Inside it, create `question_1.py`, `question_2.py`, `question_3.py`, `question_4.py`, and `question_5.py`.
3. Write each answer in its matching file. Work in question order; when a question needs an earlier function, copy it or use the shared module explicitly requested below.
4. Open a terminal at the repository root and run the first answer with the command below. Change the final filename to run each of the other answers. Use `python` or `py` instead of `python3` if needed on your system.

```bash
python3 languages/python/practice/lesson_20/question_1.py
```

For commands that require arguments, append the arguments described in that question. Unless instructed otherwise, keep input files and generated data inside this lesson's practice folder; paths in scripts run from the repository root must include that folder.

### When your answers are ready

Run every answer and compare it with the checks in its question. Save all five files and tell me: “Lesson 20 answers are ready in `languages/python/practice/lesson_20/`. Please check all five files.” I will review your code and help you correct it before we continue.

## Five coding questions

### Question 1: Await one job

**Answer file:** `question_1.py`

1. Define an async job(label, delay) using await asyncio.sleep(delay), returning its label.
2. Call it from an async main() and run main with asyncio.run() in a script.
3. Check that the returned label appears after the simulated wait.

### Question 2: Run jobs sequentially

**Answer file:** `question_2.py`

1. Await three jobs with delays 0.2, 0.1, and 0.3 seconds one after another.
2. Use time.perf_counter() to measure their combined duration.
3. Print all results and the elapsed time; expect roughly 0.6 seconds plus overhead, not an exact value.

### Question 3: Run jobs concurrently

**Answer file:** `question_3.py`

1. Run those three jobs with asyncio.gather().
2. Measure their combined duration and print returned labels.
3. Expect roughly 0.3 seconds plus overhead and labels in argument order; compare with question 2 without asserting exact timing.

### Question 4: Handle a timeout

**Answer file:** `question_4.py`

1. Run a job that waits 1 second through asyncio.wait_for() with a 0.1-second timeout.
2. Catch asyncio.TimeoutError and print a clear timeout message.
3. Confirm that no unhandled traceback appears and the normal completed result is not printed.

### Question 5: Compare both approaches

**Answer file:** `question_5.py`

1. In one async main(), run a sequential batch and then a concurrent batch using fresh coroutine calls each time.
2. Print each batch's results and duration and include a separate handled timeout demonstration.
3. Verify equal returned label lists, explain the timing difference in comments, and avoid time.sleep() inside async functions.
