# Lesson 03: Input and string operations

[Previous lesson](02-variables-and-types.md) · [Schedule](../SCHEDULE.md) · [Next lesson](04-conditions.md)

**Goal:** Accept user input and clean, convert, and format text.

**Prerequisite:** Complete lesson 02 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

`input()` displays a prompt, waits for a line, and returns a string. It returns text even when the user types digits. Convert only when your program needs a number.

```python
name = input("Your name: ").strip()
age_text = input("Your age in whole years: ")
age = int(age_text)
print(f"Hello, {name}! Next year you will be {age + 1}.")
print(name.upper())
```

This example assumes a valid integer; typing `hello` for age raises `ValueError`. We will handle that in lesson 9. For now, notice the assumption instead of hiding it.

Strings have methods, which are operations called through a value, such as `name.upper()`. `strip()` removes surrounding whitespace, `lower()` produces lowercase text, and `replace("old", "new")` replaces matching pieces. These operations return new strings; they do not change the original string in place.

Indexing starts at zero: `"Python"[0]` is `"P"`. Negative indices count from the end, so `"Python"[-1]` is `"n"`. Slicing selects a range and excludes the end: `"Python"[1:4]` is `"yth"`. `len(text)` counts characters. Indexing an empty string raises `IndexError`, while a slice may safely return an empty string.

Try predicting `"  Ada  ".strip().lower()` before running it. Method calls can be chained because each result becomes the input to the next operation.

## Practice exercise

Ask for a full name and a favorite language. Remove surrounding spaces and display a sentence plus the length of the cleaned name. Also display the first three characters using a slice.

Before moving on, run your work, explain it in your own words, and record one thing you learned in [your progress log](../PROGRESS.md).

## Review questions

1. What type does input() return?
2. What does " Python " .strip().lower() produce?
3. What does the slice "beginner"[0:5] return?
4. Why does name.upper() by itself not update name?
5. What happens if int() receives "three" instead of "3"?
