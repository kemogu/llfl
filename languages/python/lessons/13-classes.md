# Lesson 13: Classes and objects

[Previous lesson](12-first-project.md) · [Schedule](../SCHEDULE.md) · [Next lesson](14-dataclasses-and-composition.md)

**Goal:** Group related data and behavior without creating unnecessary abstractions.

**Prerequisite:** Complete lesson 12 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

A class defines a kind of object. Each instance has its own state; methods operate on instances. `self` is the conventional name for the instance parameter, supplied automatically when you call a method on an object.

```python
class Task:
    def __init__(self, title):
        if not title.strip():
            raise ValueError("Title must not be empty.")
        self.title = title.strip()
        self.done = False

    def complete(self):
        self.done = True

    def describe(self):
        marker = "x" if self.done else " "
        return f"[{marker}] {self.title}"

task = Task("Learn classes")
task.complete()
print(task.describe())
```

`__init__` initializes an instance after it is created. `self.title` and `self.done` are instance attributes. If you create two Task objects, completing one does not complete the other.

Be careful with mutable class attributes: placing `items = []` directly in a class body shares that list across instances. Put per-instance mutable state inside `__init__` instead.

Classes are useful when data and behavior naturally belong together or state has rules to preserve. Plain functions and dictionaries remain good choices for simple transformations. A leading underscore, such as `_items`, signals an internal implementation detail by convention; it does not enforce privacy.

JSON does not automatically serialize this Task object. Add an explicit conversion to a dictionary if persistence needs it, and reconstruct objects only after validating loaded data.

## Practice exercise

Complete the five coding questions below. You will write the answers; the examples above are for studying.

### Set up your answer files

1. In your editor, create the folder `languages/python/practice/lesson_13/`.
2. Inside it, create `question_1.py`, `question_2.py`, `question_3.py`, `question_4.py`, and `question_5.py`.
3. Write each answer in its matching file. Work in question order; when a question needs an earlier function, copy it or use the shared module explicitly requested below.
4. Open a terminal at the repository root and run the first answer with the command below. Change the final filename to run each of the other answers. Use `python` or `py` instead of `python3` if needed on your system.

```bash
python3 languages/python/practice/lesson_13/question_1.py
```

For commands that require arguments, append the arguments described in that question. Unless instructed otherwise, keep input files and generated data inside this lesson's practice folder; paths in scripts run from the repository root must include that folder.

### When your answers are ready

Run every answer and compare it with the checks in its question. Save all five files, record your progress in [PROGRESS.md](../PROGRESS.md), and tell me: “Lesson 13 answers are ready in `languages/python/practice/lesson_13/`. Please check all five files.” I will review your code and help you correct it before we continue.

## Five coding questions

### Question 1: Create an account

**Answer file:** `question_1.py`

1. Create account.py beside your answer files with a BankAccount class whose instance balance_cents starts at zero.
2. In question_1.py, create two fictional accounts and print both balances.
3. Verify both begin at zero and the balance is stored on each instance.

### Question 2: Deposit money

**Answer file:** `question_2.py`

1. Add deposit(amount_cents) to the class, rejecting nonpositive amounts with ValueError; assume integer amounts.
2. In question_2.py, deposit 1000 cents and catch attempts to deposit 0 and -100.
3. Check that the final balance remains 1000 after the rejected deposits.

### Question 3: Withdraw money

**Answer file:** `question_3.py`

1. Add withdraw(amount_cents), rejecting nonpositive amounts and amounts larger than the balance.
2. In question_3.py, deposit 1000, withdraw 300, and attempt to withdraw 800.
3. Catch the error and verify that the final balance is 700 cents.

### Question 4: Check independent instances

**Answer file:** `question_4.py`

1. In question_4.py, create two accounts.
2. Deposit 500 into the first and 200 into the second; withdraw 100 from the first.
3. Print both balances and check for 400 and 200, demonstrating that one account does not change the other.

### Question 5: Exercise boundary cases

**Answer file:** `question_5.py`

1. In question_5.py, deposit 500 and withdraw exactly 500.
2. Try another withdrawal of 1 and withdrawals of 0 and -1, catching their errors.
3. Check that the balance remains zero after every rejected operation and print a clear result for each attempt.
