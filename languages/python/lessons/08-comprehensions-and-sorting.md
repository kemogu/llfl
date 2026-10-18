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

Complete the five coding questions below. You will write the answers; the examples above are for studying.

### Set up your answer files

1. In your editor, create the folder `languages/python/practice/lesson_08/`.
2. Inside it, create `question_1.py`, `question_2.py`, `question_3.py`, `question_4.py`, and `question_5.py`.
3. Write each answer in its matching file. Work in question order; when a question needs an earlier function, copy it or use the shared module explicitly requested below.
4. Open a terminal at the repository root and run the first answer with the command below. Change the final filename to run each of the other answers. Use `python` or `py` instead of `python3` if needed on your system.

```bash
python3 languages/python/practice/lesson_08/question_1.py
```

For commands that require arguments, append the arguments described in that question. Unless instructed otherwise, keep input files and generated data inside this lesson's practice folder; paths in scripts run from the repository root must include that folder.

### When your answers are ready

Run every answer and compare it with the checks in its question. Save all five files, record your progress in [PROGRESS.md](../PROGRESS.md), and tell me: “Lesson 8 answers are ready in `languages/python/practice/lesson_08/`. Please check all five files.” I will review your code and help you correct it before we continue.

## Five coding questions

### Question 1: Filter passing students

**Answer file:** `question_1.py`

1. Create records for Ada:90, Linus:55, Grace:98, and Alan:90, using name and score keys.
2. Use a list comprehension to keep records with scores of at least 60.
3. Print the names and check that Linus is excluded and the other three remain.

### Question 2: Sort by score

**Answer file:** `question_2.py`

1. Recreate the records from question 1.
2. Use sorted() and a key function to order records by descending score.
3. Print the names; expect Grace, Ada, Alan, Linus. Ada should remain before Alan because their scores tie.

### Question 3: Number a ranking

**Answer file:** `question_3.py`

1. Filter and sort the same records.
2. Use enumerate(..., start=1) to print rank, name, and score.
3. Check that Grace is ranked 1, Ada 2, and Alan 3.

### Question 4: Build a dictionary

**Answer file:** `question_4.py`

1. Create the word list ["cat", "python", "code"].
2. Use a dictionary comprehension mapping each word to its length.
3. Print the result and check for cat:3, python:6, and code:4.

### Question 5: Preserve the original

**Answer file:** `question_5.py`

1. Recreate the student records and store their original name order in a separate list.
2. Build a passing-student ranking without sorting or editing the original list in place.
3. Print the ranking and the original name order afterward; check that the original remains Ada, Linus, Grace, Alan.
