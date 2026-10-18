# Lesson 06: Lists, tuples, dictionaries, and sets

[Previous lesson](05-loops.md) · [Schedule](../SCHEDULE.md) · [Next lesson](07-functions.md)

**Goal:** Choose a collection based on the information you need to store.

**Prerequisite:** Complete lesson 05 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

A **list** stores an ordered, mutable sequence; a **tuple** stores an ordered sequence whose element references cannot be replaced. A **dictionary** maps unique keys to values. A **set** stores unique elements without a dependable display order.

```python
names = ["Ada", "Linus"]
names.append("Grace")
point = (3, 4)
student = {"name": "Ada", "score": 95}
student["score"] = 96
languages = {"python", "rust", "python"}
print(names[0], point[1], student["score"])
print(len(languages))  # 2
for name in names:
    print(name)
for key, value in student.items():
    print(key, value)
```

`in` tests membership. For dictionaries it checks keys, not values. `student.get("email", "unknown")` supplies a fallback for a missing key; `student["email"]` would raise `KeyError`. `{}` creates an empty dictionary; use `set()` for an empty set.

Mutation changes an existing object. After `other = names`, both names refer to the same list, so `other.append("Alan")` also appears through `names`. `names.copy()` makes a shallow copy: nested mutable objects are still shared. Strings, numbers, and tuples are immutable, though a tuple can contain a mutable list.

Choose collections by purpose: a shopping list needs order and duplicates, a profile needs named fields, and a unique set of tags needs duplicate removal. Avoid removing items from a list while iterating over it; build a new list instead.

## Practice exercise

Complete the five coding questions below. You will write the answers; the examples above are for studying.

### Set up your answer files

1. In your editor, create the folder `languages/python/practice/lesson_06/`.
2. Inside it, create `question_1.py`, `question_2.py`, `question_3.py`, `question_4.py`, and `question_5.py`.
3. Write each answer in its matching file. Work in question order; when a question needs an earlier function, copy it or use the shared module explicitly requested below.
4. Open a terminal at the repository root and run the first answer with the command below. Change the final filename to run each of the other answers. Use `python` or `py` instead of `python3` if needed on your system.

```bash
python3 languages/python/practice/lesson_06/question_1.py
```

For commands that require arguments, append the arguments described in that question. Unless instructed otherwise, keep input files and generated data inside this lesson's practice folder; paths in scripts run from the repository root must include that folder.

### When your answers are ready

Run every answer and compare it with the checks in its question. Save all five files, record your progress in [PROGRESS.md](../PROGRESS.md), and tell me: “Lesson 6 answers are ready in `languages/python/practice/lesson_06/`. Please check all five files.” I will review your code and help you correct it before we continue.

## Five coding questions

### Question 1: Build student records

**Answer file:** `question_1.py`

1. Create a list containing dictionaries for Ada with score 80, Grace with 90, and Ada with 70.
2. Give every dictionary name and score keys.
3. Print the list length and the first student name; expect 3 and Ada.

### Question 2: Display records

**Answer file:** `question_2.py`

1. Recreate the three records from question 1.
2. Loop over them and print each name beside its score.
3. Check that there are three output records and both Ada records remain.

### Question 3: Calculate an average

**Answer file:** `question_3.py`

1. Recreate the same student list and initialize a total.
2. Add the scores in a loop and divide by the number of records.
3. Print the average and check that it is 80.0. Assume the list is nonempty.

### Question 4: Collect unique names

**Answer file:** `question_4.py`

1. Recreate the same records and start with an empty set.
2. Add each name to the set, then print the set and its size.
3. Check that only Ada and Grace remain and the size is 2; their display order does not matter.

### Question 5: Compare copying and aliasing

**Answer file:** `question_5.py`

1. Create a list of two names and assign that list to a second variable.
2. Append through the second variable and print both to show they share the change.
3. Make a shallow copy with copy(), append a new name to the copy, and print both to show the original list does not receive that new name.
