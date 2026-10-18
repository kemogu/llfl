# Lesson 19: Algorithms and performance

[Previous lesson](18-typing-and-design.md) · [Schedule](../SCHEDULE.md) · [Next lesson](20-concurrency-and-async.md)

**Goal:** Reason about time and memory costs, then measure real bottlenecks.

**Prerequisite:** Complete lesson 18 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

Big-O notation describes how cost grows with input size. One pass over n items is usually O(n); comparing every pair is often O(n²). It describes growth, not exact seconds. A faster algorithm can matter more than tiny syntax changes.

```python
def duplicates(values):
    seen = set()
    repeated = set()
    for value in values:
        if value in seen:
            repeated.add(value)
        seen.add(value)
    return repeated

print(duplicates([1, 2, 1, 3, 2]) == {1, 2})
```

For hashable values, set membership is O(1) on average, so this algorithm is O(n) on average and uses O(n) extra memory. List membership is O(n), so repeatedly searching a growing list can lead to O(n²) work. Sets require hashable elements: a list cannot itself be a set member.

Use `timeit` for small, repeatable measurements:

```python
from timeit import timeit
items = list(range(10000))
lookup = set(items)
print(timeit(lambda: 9999 in items, number=1000))
print(timeit(lambda: 9999 in lookup, number=1000))
```

These timings exclude construction of the collections; include construction if it is part of your real workload. Results vary by machine and environment. A one-off lookup might not justify building a set.

For a whole program, use `python3 -m cProfile your_script.py` to locate where time is spent. Improve a measured bottleneck, keep behavior covered by tests, and compare again. Memory, readability, and correctness are also part of performance decisions.

## Practice exercise

Implement duplicate detection once using list membership and once using a set. Check identical results, then measure both with increasing input sizes. Record construction costs and avoid claiming universal timing ratios.

Before moving on, run your work, explain it in your own words, and record one thing you learned in [your progress log](../PROGRESS.md).

## Review questions

1. What does O(n) describe?
2. Why can nested loops lead to O(n²) work?
3. What time and memory tradeoff does a set introduce?
4. Why can benchmark setup change a conclusion?
5. Why should you profile before optimizing a large program?
