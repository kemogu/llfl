# Lesson 02: Variables and basic types

[Previous lesson](01-first-program.md) · [Schedule](../SCHEDULE.md) · [Next lesson](03-input-and-strings.md)

**Goal:** Store values and distinguish strings, integers, floats, and booleans.

**Prerequisite:** Complete lesson 01 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

A variable is a name referring to a value. Assignment uses `=`; it is not a mathematical assertion that two expressions are equal. Python evaluates the right side first, then binds the name on the left. Use descriptive `snake_case` names.

```python
name = "Ada"          # str: text
age = 28              # int: whole number
height = 1.65         # float: floating-point number
is_student = True     # bool: True or False
age = age + 1
print(f"{name} is {age} years old.")
print(type(height))
print(is_student)
```

An f-string starts with `f` and inserts expressions inside `{}`. `type()` helps inspect a value's type. Python names do not have permanently fixed types, but changing one name from a number to unrelated text often makes code confusing.

Arithmetic operators include `+`, `-`, `*`, `/`, `//`, `%`, and `**`. `/` performs division, `//` performs floor division, `%` gives the remainder, and `**` raises to a power. For positive integers, `17 // 5` is `3` and `17 % 5` is `2`. Parentheses make evaluation order explicit.

`"5"` is text, while `5` is an integer. Adding a string to an integer causes a `TypeError`; convert intentionally with `int("5")` or `str(5)`. Floating-point arithmetic approximates many decimal values, so it is not a suitable default for exact money calculations.

## Practice exercise

Complete the five coding questions below. You will write the answers; the examples above are for studying.

### Set up your answer files

1. In your editor, create the folder `languages/python/practice/lesson_02/`.
2. Inside it, create `question_1.py`, `question_2.py`, `question_3.py`, `question_4.py`, and `question_5.py`.
3. Write each answer in its matching file. Work in question order; when a question needs an earlier function, copy it or use the shared module explicitly requested below.
4. Open a terminal at the repository root and run the first answer with the command below. Change the final filename to run each of the other answers. Use `python` or `py` instead of `python3` if needed on your system.

```bash
python3 languages/python/practice/lesson_02/question_1.py
```

For commands that require arguments, append the arguments described in that question. Unless instructed otherwise, keep input files and generated data inside this lesson's practice folder; paths in scripts run from the repository root must include that folder.

### When your answers are ready

Run every answer and compare it with the checks in its question. Save all five files and tell me: “Lesson 2 answers are ready in `languages/python/practice/lesson_02/`. Please check all five files.” I will review your code and help you correct it before we continue.

## Five coding questions

### Question 1: Store product information

**Answer file:** `question_1.py`

1. Create product_name = "Notebook", quantity = 3, and price_cents = 250.
2. Print each value on its own line.
3. Check that the output contains Notebook, 3, and 250 in that order.

### Question 2: Inspect types

**Answer file:** `question_2.py`

1. Create values for a product name, a quantity, a decimal measurement, and an in_stock boolean.
2. Print each value and its type using type().
3. Check that the four types are str, int, float, and bool.

### Question 3: Calculate a total

**Answer file:** `question_3.py`

1. Create integer variables price_cents = 250 and quantity = 3.
2. Multiply them and store the result in total_cents.
3. Print total_cents and verify that it is 750; change quantity to 4 and check for 1000.

### Question 4: Update a quantity

**Answer file:** `question_4.py`

1. Start with quantity = 3 and price_cents = 250.
2. Increase quantity by one, then calculate the new total.
3. Print both values and check for quantity 4 and total 1000 cents.

### Question 5: Format a receipt

**Answer file:** `question_5.py`

1. Create variables for Notebook, quantity 3, and price 250 cents; calculate the total.
2. Use f-strings to display labeled lines for the product, quantity, unit price, and total.
3. Check that the total is labeled as 750 cents. Use variables in the output rather than typing the calculated answer.
