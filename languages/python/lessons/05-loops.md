# Lesson 05: Loops and repetition

[Previous lesson](04-conditions.md) · [Schedule](../SCHEDULE.md) · [Next lesson](06-collections.md)

**Goal:** Repeat work with for and while, and reason about when a loop ends.

**Prerequisite:** Complete lesson 04 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

A `for` loop visits each item in an iterable, an object that can supply items one at a time. `range(1, 4)` supplies 1, 2, and 3: its stop value is excluded.

```python
total = 0
for number in range(1, 6):
    total += number
print(total)  # 15
```

`+=` updates the existing value. Here `total` is an accumulator: it collects a result across iterations.

A `while` loop repeats while its condition is true. Something must eventually change the condition or execute `break`; otherwise the loop may run forever.

```python
attempts = 3
while attempts > 0:
    print(f"Attempts remaining: {attempts}")
    attempts -= 1
```

`break` exits the nearest enclosing loop. `continue` skips the rest of the current iteration and starts the next one. Use them when they simplify the logic, not to avoid thinking about the condition.

```python
for number in range(1, 8):
    if number % 2 == 0:
        continue
    print(number)  # 1, 3, 5, 7
```

Trace loops on paper: record each value of the loop variable and accumulator. This catches off-by-one mistakes. For accidental infinite terminal loops, Ctrl+C usually interrupts execution.

## Practice exercise

Ask for a positive integer n. Calculate the sum from 1 through n using a loop, then print a multiplication table for n from 1 through 10. Reject nonpositive integers.

Before moving on, run your work, explain it in your own words, and record one thing you learned in [your progress log](../PROGRESS.md).

## Review questions

1. Which values does range(2, 7) produce?
2. What is an accumulator?
3. How do break and continue differ?
4. Why would a while loop become infinite?
5. How would you include n when summing with range()?
