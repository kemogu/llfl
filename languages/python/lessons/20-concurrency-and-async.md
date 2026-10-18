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

Simulate three independent jobs with asyncio.sleep. Compare sequential awaits with gather using time.perf_counter(). Add a timeout to a deliberately slow job and report the timeout clearly.

Before moving on, run your work, explain it in your own words, and record one thing you learned in [your progress log](../PROGRESS.md).

## Review questions

1. How does concurrency differ from parallelism?
2. What does calling an async function initially return?
3. Why is time.sleep() problematic inside an event loop?
4. In what order does gather return its results?
5. Why should concurrent applications define limits and failure behavior?
