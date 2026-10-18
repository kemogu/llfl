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

Complete the five coding questions below. You will write the answers; the examples above are for studying.

### Set up your answer files

1. In your editor, create the folder `languages/python/practice/lesson_19/`.
2. Inside it, create `question_1.py`, `question_2.py`, `question_3.py`, `question_4.py`, and `question_5.py`.
3. Write each answer in its matching file. Work in question order; when a question needs an earlier function, copy it or use the shared module explicitly requested below.
4. Open a terminal at the repository root and run the first answer with the command below. Change the final filename to run each of the other answers. Use `python` or `py` instead of `python3` if needed on your system.

```bash
python3 languages/python/practice/lesson_19/question_1.py
```

For commands that require arguments, append the arguments described in that question. Unless instructed otherwise, keep input files and generated data inside this lesson's practice folder; paths in scripts run from the repository root must include that folder.

### When your answers are ready

Run every answer and compare it with the checks in its question. Save all five files and tell me: “Lesson 19 answers are ready in `languages/python/practice/lesson_19/`. Please check all five files.” I will review your code and help you correct it before we continue.

## Five coding questions

### Question 1: Find duplicates using a list

**Answer file:** `question_1.py`

1. Define a duplicate detector that stores seen values in a list and returns a set of repeated integers.
2. Run it with [1, 2, 1, 3, 2], [], and [1, 2, 3].
3. Check for {1, 2}, set(), and set(); compare sets without depending on display order.

### Question 2: Find duplicates using a set

**Answer file:** `question_2.py`

1. Write a second detector using a set for seen values.
2. Use the same three inputs as question 1.
3. Verify the results match and explain the extra storage requirement in a comment.

### Question 3: Check agreement

**Answer file:** `question_3.py`

1. Put both detectors into algorithms.py beside your answer files.
2. In question_3.py, import them and compare their outputs on empty, unique, repeated, and all-identical integer lists.
3. Use assertions or unittest and check that every comparison passes before benchmarking.

### Question 4: Measure both algorithms

**Answer file:** `question_4.py`

1. Build inputs of sizes 100, 1000, and 5000; use the same inputs and number of repetitions for both functions.
2. Use timeit to measure complete detector calls, including each function's internal collection construction.
3. Print size and both timings, and record that input generation is excluded. Keep the repetition count small enough for a short run.

### Question 5: Measure a lookup tradeoff

**Answer file:** `question_5.py`

1. Compare one list membership check with building a set and doing one membership check, using the same source list.
2. Then compare repeated membership checks on the list with checks on a prebuilt set.
3. Print labeled timings and explain in comments which measurements include set construction and why one result does not establish a universal winner.
