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

Complete the five coding questions below. You will write the answers; the examples above are for studying.

### Set up your answer files

1. In your editor, create the folder `languages/python/practice/lesson_17/`.
2. Inside it, create `question_1.py`, `question_2.py`, `question_3.py`, `question_4.py`, and `question_5.py`.
3. Write each answer in its matching file. Work in question order; when a question needs an earlier function, copy it or use the shared module explicitly requested below.
4. Open a terminal at the repository root and run the first answer with the command below. Change the final filename to run each of the other answers. Use `python` or `py` instead of `python3` if needed on your system.

```bash
python3 languages/python/practice/lesson_17/question_1.py
```

For commands that require arguments, append the arguments described in that question. Unless instructed otherwise, keep input files and generated data inside this lesson's practice folder; paths in scripts run from the repository root must include that folder.

### When your answers are ready

Run every answer and compare it with the checks in its question. Save all five files and tell me: “Lesson 17 answers are ready in `languages/python/practice/lesson_17/`. Please check all five files.” I will review your code and help you correct it before we continue.

## Five coding questions

### Question 1: Wrap a function

**Answer file:** `question_1.py`

1. Create decorators.py with an announce decorator that wraps a function using *args and **kwargs.
2. In question_1.py, decorate an addition function and print its returned result.
3. Check that a call message appears and add(2, 3) still returns 5.

### Question 2: Preserve metadata

**Answer file:** `question_2.py`

1. Apply functools.wraps to your wrapper in decorators.py.
2. In question_2.py, decorate a function with a docstring and print its __name__ and __doc__.
3. Verify both describe the original function rather than the wrapper.

### Question 3: Measure elapsed time

**Answer file:** `question_3.py`

1. Add a timed decorator using time.perf_counter() before and after the wrapped call, with elapsed-time output in finally.
2. In question_3.py, decorate a small calculation and display its result.
3. Verify that the result is preserved and a nonnegative elapsed time is printed. Do not expect an exact timing value.

### Question 4: Preserve exceptions

**Answer file:** `question_4.py`

1. In question_4.py, use timed on a function that raises ValueError.
2. Call it inside a caller-side try/except and print a message when the error is caught.
3. Check that timing output still appears and ValueError reaches the caller instead of being suppressed.

### Question 5: Guarantee cleanup

**Answer file:** `question_5.py`

1. In question_5.py, define a contextmanager that prints Start before yield and Finish in finally.
2. Use it once with a normal block and once with a block that raises ValueError, catching the error outside with.
3. Check that Finish appears on both exits, and the error is caught by the outer handler.
