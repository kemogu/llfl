# Lesson 17: Decorators and context managers

[Previous lesson](16-iterators-and-generators.md) · [Schedule](../SCHEDULE.md) · [Next lesson](18-typing-and-design.md)

**Goal:** Wrap function behavior and reliably pair setup with cleanup.

**Prerequisite:** Complete lesson 16 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

Functions are objects: you can store them in variables, pass them to other functions, and return them. A decorator accepts a function and returns a replacement, often a wrapper that performs work before or after calling the original.

```python
from functools import wraps

def announce(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Calling {function.__name__}")
        return function(*args, **kwargs)
    return wrapper

@announce
def add(left, right):
    return left + right

print(add(2, 3))
```

`@announce` is approximately `add = announce(add)` after the function definition. `*args` collects positional arguments; `**kwargs` collects keyword arguments. In a call, they unpack those arguments again. `wraps` preserves useful metadata such as the original name and docstring. Returning the wrapped result preserves the caller's expected behavior.

A context manager supports `with`, pairing entry and exit behavior. The standard library's `contextmanager` lets you define one with a generator:

```python
from contextlib import contextmanager

@contextmanager
def announced_session():
    print("Start")
    try:
        yield
    finally:
        print("Finish")

with announced_session():
    print("Working")
```

The code before `yield` runs on entry; cleanup in `finally` runs on exit, including normal exception unwinding. Do not accidentally suppress an exception when cleanup alone is intended.

## Practice exercise

Write a timing decorator using time.perf_counter(). Use try/finally so elapsed time is printed even if the wrapped function raises. Preserve arguments, return values, metadata, and exceptions.

Before moving on, run your work, explain it in your own words, and record one thing you learned in [your progress log](../PROGRESS.md).

## Review questions

1. What does a decorator receive and return?
2. What do *args and **kwargs capture?
3. Why use functools.wraps?
4. Why must a wrapper return the original function result?
5. How does try/finally help a context manager perform cleanup?
