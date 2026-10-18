# Lesson 08: Comprehensions, unpacking, and sorting

[Previous lesson](07-functions.md) · [Schedule](../SCHEDULE.md) · [Next lesson](09-exceptions.md)

**Goal:** Transform collections clearly and sort records by a selected field.

**Prerequisite:** Complete lesson 07 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

A comprehension builds a collection from an iterable. Read it as “produce this expression for each item, optionally keeping only matching items.”

```python
numbers = [3, -2, 7, 0]
squares = [number ** 2 for number in numbers if number > 0]
lengths = {word: len(word) for word in ["cat", "python"]}
print(squares)  # [9, 49]
print(lengths)
```

Use a normal loop if a comprehension needs many conditions or side effects. A comprehension should make a transformation easier to understand.

Unpacking assigns multiple values at once: `x, y = (3, 4)`. `enumerate()` gives a position and item; `zip()` pairs items from iterables and, by default, stops at the shortest input.

```python
students = [{"name": "Ada", "score": 90}, {"name": "Grace", "score": 98}]
def score_of(student):
    return student["score"]

ranked = sorted(students, key=score_of, reverse=True)
for position, student in enumerate(ranked, start=1):
    print(position, student["name"])
```

`sorted()` returns a new list. `list.sort()` modifies the existing list and returns `None`. A `key` function extracts the value used for ordering; Python's sort is stable, so items with equal keys retain their original relative order. A small anonymous function, `lambda student: student["score"]`, can replace `score_of`, though named functions are often clearer for larger logic.

## Practice exercise

From a list of student dictionaries, keep those scoring at least 60, sort them by score descending, and print a numbered ranking. Keep the original list unchanged.

Before moving on, run your work, explain it in your own words, and record one thing you learned in [your progress log](../PROGRESS.md).

## Review questions

1. What does [n * 2 for n in range(4)] produce?
2. When is a regular loop clearer than a comprehension?
3. What does enumerate() provide?
4. How do sorted() and list.sort() differ?
5. What happens when zip() receives inputs of different lengths by default?
