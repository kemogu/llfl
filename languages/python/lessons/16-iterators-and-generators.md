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

Write a generator that yields only nonempty stripped lines from a supplied iterable of strings. Feed it a list first, then consume it within a with block reading a practice text file.

Before moving on, run your work, explain it in your own words, and record one thing you learned in [your progress log](../PROGRESS.md).

## Review questions

1. What is the difference between an iterable and an iterator?
2. What happens when an iterator is exhausted?
3. How does yield differ from return?
4. Why does the second list(totals) call produce an empty list?
5. When can a generator reduce memory use compared with a list?
