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

Store a product name, integer quantity, and integer price in cents. Calculate total cents and display a readable receipt with an f-string.

Before moving on, run your work, explain it in your own words, and record one thing you learned in [your progress log](../PROGRESS.md).

## Review questions

1. What does assignment do?
2. What are the types of "42", 42, 4.2, and False?
3. What are 19 // 4 and 19 % 4?
4. How would you increase quantity by one?
5. Why does "Age: " + 20 fail, and how can you display the intended message?
