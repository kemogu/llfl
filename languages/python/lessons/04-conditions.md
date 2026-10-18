# Lesson 04: Conditions and decisions

[Previous lesson](03-input-and-strings.md) · [Schedule](../SCHEDULE.md) · [Next lesson](05-loops.md)

**Goal:** Use comparisons and boolean expressions to choose which code runs.

**Prerequisite:** Complete lesson 03 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

Programs make decisions with `if`, `elif`, and `else`. A condition is tested for truth. Python uses indentation to group statements; use four spaces for each indentation level.

```python
score = 76
if score >= 90:
    result = "excellent"
elif score >= 60:
    result = "passed"
else:
    result = "keep practicing"
print(result)
```

Only the first matching branch runs. Put more specific thresholds first: checking `score >= 60` first would also match a score of 95.

Comparisons include `==` (equal), `!=`, `<`, `<=`, `>`, and `>=`. Assignment `=` and comparison `==` have different purposes. Combine conditions with `and`, `or`, and `not`.

```python
age = 20
has_ticket = True
can_enter = age >= 18 and has_ticket
print(can_enter)
print(0 <= score <= 100)
```

Empty strings, empty collections, zero, and `None` are false in a boolean context. For example, `if not name:` can detect an empty name. `None` represents absence of a value; check it using `is None`.

`and` and `or` short-circuit: Python skips the right side when the left side already determines the result. This makes `name and name[0] == "A"` safe for an empty string. These operators actually return an operand, so the expression may return `""` rather than the boolean `False`.

## Practice exercise

Ask for an integer score. Reject values outside 0–100; otherwise print excellent for 90–100, passed for 60–89, and keep practicing for 0–59. Try all boundary values.

Before moving on, run your work, explain it in your own words, and record one thing you learned in [your progress log](../PROGRESS.md).

## Review questions

1. How do = and == differ?
2. Why does branch order matter for score thresholds?
3. When is an and expression true?
4. Which branch handles a score of exactly 60 in the example?
5. How would you check whether a number is outside the inclusive range 0–100?
