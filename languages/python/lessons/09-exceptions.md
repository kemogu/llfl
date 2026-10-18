# Lesson 09: Exceptions and input validation

[Previous lesson](08-comprehensions-and-sorting.md) · [Schedule](../SCHEDULE.md) · [Next lesson](10-files-and-json.md)

**Goal:** Handle expected failures without hiding programming mistakes.

**Prerequisite:** Complete lesson 08 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

An exception interrupts normal execution. A traceback shows the chain of calls that led to it; start with the exception type and message near the bottom, then inspect the relevant lines in your code.

```python
def read_positive_integer(text):
    number = int(text)
    if number <= 0:
        raise ValueError("Enter an integer greater than zero.")
    return number

try:
    quantity = read_positive_integer("3")
except ValueError as error:
    print(f"Invalid quantity: {error}")
else:
    print(f"Quantity: {quantity}")
```

`try` encloses work that may fail. `except` handles a specified exception. `else` runs if the try block completes normally. `finally` runs when leaving the construct during normal Python control flow, including exceptions, and is used for cleanup.

Catch exceptions you can meaningfully handle. `except: pass` silently discards errors, including ones that reveal bugs. Keep try blocks narrow so the source of the expected failure is clear. Use `raise` to communicate invalid inputs when returning a normal result would be misleading.

Validate at boundaries, such as terminal input or file loading. Inside well-defined functions, document which inputs are accepted. Do not use `assert` for user input validation: assertions can be disabled, and they express developer assumptions rather than recoverable input errors.

## Practice exercise

Build a loop that asks for a positive integer until valid input is received. Catch ValueError, show a useful message, and retry. Test "hello", "0", "-4", and "7".

Before moving on, run your work, explain it in your own words, and record one thing you learned in [your progress log](../PROGRESS.md).

## Review questions

1. What information should you read first in a traceback?
2. Why catch ValueError instead of every possible exception?
3. When does the else block run?
4. What does raise ValueError(...) communicate to a caller?
5. Why should assert not validate user input?
