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

Write total_cents(price_cents, quantity) and format_receipt(name, total). Keep input and printing outside both functions. Call each with several different arguments.

Before moving on, run your work, explain it in your own words, and record one thing you learned in [your progress log](../PROGRESS.md).

## Review questions

1. What is the difference between a parameter and an argument?
2. How does return differ from print?
3. What does a function return when it reaches the end without return?
4. Why is a list used as a default argument risky?
5. Why separate user input from calculation functions?
