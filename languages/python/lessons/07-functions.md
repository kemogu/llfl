# Lesson 07: Functions, parameters, and return values

[Previous lesson](06-collections.md) · [Schedule](../SCHEDULE.md) · [Next lesson](08-comprehensions-and-sorting.md)

**Goal:** Break a program into reusable functions with clear inputs and outputs.

**Prerequisite:** Complete lesson 06 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

Define a function with `def`. Parameters name its expected inputs; arguments are the actual values provided in a call. `return` sends a result to the caller and ends that call.

```python
def rectangle_area(width, height):
    """Return the area of a rectangle."""
    return width * height

area = rectangle_area(4, 3)
print(area)
print(rectangle_area(height=5, width=2))
```

`print()` displays information; it does not substitute for returning a useful result. A function without an explicit return value returns `None`. Local variables created inside a function normally belong to that call. Prefer passing inputs and returning outputs over modifying global state.

Defaults make some arguments optional:

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Ada"))
```

Default expressions are evaluated once when the function is defined. Avoid a mutable default such as `items=[]`, because later calls share that same list. Instead use `items=None` and create a new list inside when needed.

Keep each function focused. Separating calculation from `input()` and `print()` makes the calculation easier to reuse and test. A short docstring, the first string in a function body, explains its purpose.

## Practice exercise

Complete the five coding questions below. You will write the answers; the examples above are for studying.

### Set up your answer files

1. In your editor, create the folder `languages/python/practice/lesson_07/`.
2. Inside it, create `question_1.py`, `question_2.py`, `question_3.py`, `question_4.py`, and `question_5.py`.
3. Write each answer in its matching file. Work in question order; when a question needs an earlier function, copy it or use the shared module explicitly requested below.
4. Open a terminal at the repository root and run the first answer with the command below. Change the final filename to run each of the other answers. Use `python` or `py` instead of `python3` if needed on your system.

```bash
python3 languages/python/practice/lesson_07/question_1.py
```

For commands that require arguments, append the arguments described in that question. Unless instructed otherwise, keep input files and generated data inside this lesson's practice folder; paths in scripts run from the repository root must include that folder.

### When your answers are ready

Run every answer and compare it with the checks in its question. Save all five files and tell me: “Lesson 7 answers are ready in `languages/python/practice/lesson_07/`. Please check all five files.” I will review your code and help you correct it before we continue.

## Five coding questions

### Question 1: Return a calculation

**Answer file:** `question_1.py`

1. Define total_cents(price_cents, quantity) to return their product.
2. Call it outside the function and print its result.
3. Check that arguments 250 and 3 produce 750, and 250 and 0 produce 0.

### Question 2: Return formatted text

**Answer file:** `question_2.py`

1. Define format_receipt(name, total) to return a string containing the name and total in cents.
2. Call the function and print its returned string outside the function.
3. Check that Notebook and 750 appear in the output and that the function itself does not print.

### Question 3: Combine functions

**Answer file:** `question_3.py`

1. Include your two functions from questions 1 and 2.
2. Calculate a total, pass it to format_receipt(), and print the returned receipt.
3. Try Notebook at 250 cents with quantity 3, then Pen at 100 cents with quantity 2; expect totals of 750 and 200.

### Question 4: Use a default argument

**Answer file:** `question_4.py`

1. Define greet(name, greeting="Hello") and return the greeting text.
2. Call it once using the default and once supplying greeting="Welcome".
3. Print the returned values and verify that both include the supplied name and the appropriate greeting.

### Question 5: Separate input from logic

**Answer file:** `question_5.py`

1. Include the two receipt functions and keep input() calls outside them.
2. Ask for a product name, integer unit price in cents, and integer quantity; use the functions to produce a receipt.
3. Run with Notebook, 250, and 3 and check the total is 750 cents. Assume valid nonnegative integers for now.
