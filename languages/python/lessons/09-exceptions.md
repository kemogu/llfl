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

Complete the five coding questions below. You will write the answers; the examples above are for studying.

### Set up your answer files

1. In your editor, create the folder `languages/python/practice/lesson_09/`.
2. Inside it, create `question_1.py`, `question_2.py`, `question_3.py`, `question_4.py`, and `question_5.py`.
3. Write each answer in its matching file. Work in question order; when a question needs an earlier function, copy it or use the shared module explicitly requested below.
4. Open a terminal at the repository root and run the first answer with the command below. Change the final filename to run each of the other answers. Use `python` or `py` instead of `python3` if needed on your system.

```bash
python3 languages/python/practice/lesson_09/question_1.py
```

For commands that require arguments, append the arguments described in that question. Unless instructed otherwise, keep input files and generated data inside this lesson's practice folder; paths in scripts run from the repository root must include that folder.

### When your answers are ready

Run every answer and compare it with the checks in its question. Save all five files and tell me: “Lesson 9 answers are ready in `languages/python/practice/lesson_09/`. Please check all five files.” I will review your code and help you correct it before we continue.

## Five coding questions

### Question 1: Catch a conversion error

**Answer file:** `question_1.py`

1. Read text and try converting it to int.
2. Catch ValueError and print a helpful message; print the converted integer on success.
3. Run once with hello and once with 7. Neither run should produce an unhandled traceback.

### Question 2: Reject nonpositive values

**Answer file:** `question_2.py`

1. Define a function that converts text to an integer and raises ValueError if it is zero or negative.
2. Call it inside try/except and display either the result or a helpful error.
3. Test inputs "0", "-4", and "7"; only "7" should return a value.

### Question 3: Retry invalid input

**Answer file:** `question_3.py`

1. Use your positive-integer function inside a loop that prompts for input.
2. Catch ValueError and retry; stop the loop after a successful value.
3. In one run enter hello, 0, -4, and 7. Expect three error messages and then a successful exit with 7.

### Question 4: Use else and finally

**Answer file:** `question_4.py`

1. Try converting one input to an integer and catch ValueError.
2. Print a success message in else and a finished-attempt message in finally.
3. Run with hello and 7. The final message must appear in both runs, while the success message appears only for 7.

### Question 5: Validate a quantity for a receipt

**Answer file:** `question_5.py`

1. Define a receipt calculation that requires quantity to be a positive integer, using your validation function for the input text.
2. Prompt until quantity is valid, then calculate the total for a fixed price of 250 cents.
3. Enter 0 then 3. Verify that the program retries after 0 and prints a total of 750 cents after 3.
