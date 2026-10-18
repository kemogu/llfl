# Lesson 16: Iterators and generators

[Previous lesson](15-testing-and-debugging.md) · [Schedule](../SCHEDULE.md) · [Next lesson](17-decorators-and-context-managers.md)

**Goal:** Process values lazily and recognize one-pass iteration.

**Prerequisite:** Complete lesson 15 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

An iterable can provide an iterator. An iterator supplies values through `next()` until it raises `StopIteration`. A list can create fresh iterators; a particular iterator is consumed as you use it.

```python
values = iter([10, 20])
print(next(values))  # 10
print(next(values))  # 20
```

A generator function contains `yield`. Calling it returns a generator iterator; its body starts when iteration requests a value. At `yield`, execution pauses and retains local state until the next request.

```python
def running_totals(numbers):
    total = 0
    for number in numbers:
        total += number
        yield total

totals = running_totals([2, 3, 5])
print(list(totals))  # [2, 5, 10]
print(list(totals))  # []: already consumed
```

A generator expression, `(number ** 2 for number in range(1000))`, also computes values on demand. A list comprehension computes and stores all results immediately. Lazy processing can reduce memory use, particularly when you read files line by line, but it does not automatically make work faster.

Avoid returning a generator that depends on a file you have already closed. Keep the `with` block inside the generator so the resource is available while values are read, and ensure callers manage early termination appropriately. For simpler file processing, consume the iteration entirely within a `with` block.

## Practice exercise

Complete the five coding questions below. You will write the answers; the examples above are for studying.

### Set up your answer files

1. In your editor, create the folder `languages/python/practice/lesson_16/`.
2. Inside it, create `question_1.py`, `question_2.py`, `question_3.py`, `question_4.py`, and `question_5.py`.
3. Write each answer in its matching file. Work in question order; when a question needs an earlier function, copy it or use the shared module explicitly requested below.
4. Open a terminal at the repository root and run the first answer with the command below. Change the final filename to run each of the other answers. Use `python` or `py` instead of `python3` if needed on your system.

```bash
python3 languages/python/practice/lesson_16/question_1.py
```

For commands that require arguments, append the arguments described in that question. Unless instructed otherwise, keep input files and generated data inside this lesson's practice folder; paths in scripts run from the repository root must include that folder.

### When your answers are ready

Run every answer and compare it with the checks in its question. Save all five files, record your progress in [PROGRESS.md](../PROGRESS.md), and tell me: “Lesson 16 answers are ready in `languages/python/practice/lesson_16/`. Please check all five files.” I will review your code and help you correct it before we continue.

## Five coding questions

### Question 1: Consume an iterator

**Answer file:** `question_1.py`

1. Create an iterator from [10, 20] and call next() twice, printing each result.
2. Call next() a third time inside try/except StopIteration.
3. Check that the output shows 10, 20, then your exhausted message.

### Question 2: Yield clean lines

**Answer file:** `question_2.py`

1. Define clean_lines(lines) to strip each input string and yield it only if nonempty.
2. Consume it using a for loop with [" Ada ", "", "  ", " Grace\n"].
3. Check that only Ada and Grace are printed.

### Question 3: Observe exhaustion

**Answer file:** `question_3.py`

1. Define or copy clean_lines() and create one generator from two nonempty strings.
2. Print list(generator) twice, using the same generator object.
3. Check that the first list has two values and the second is empty; explain why in a comment.

### Question 4: Read a file lazily

**Answer file:** `question_4.py`

1. Create lines.txt in this lesson folder containing two names and two blank or whitespace-only lines.
2. Open it with with and iterate through clean_lines(file) inside that block.
3. Check that only the two names appear and that you do not load the whole file with read() or readlines().

### Question 5: Calculate running totals

**Answer file:** `question_5.py`

1. Write a generator that accumulates numbers and yields the total after each number.
2. Consume it with [2, 3, 5] and then with an empty list.
3. Check for results [2, 5, 10] and [] respectively, collecting into lists only for these small demonstrations.
