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

Create a list of three student dictionaries with name and score fields. Print each name and score, calculate the average score, and collect unique names in a set.

Before moving on, run your work, explain it in your own words, and record one thing you learned in [your progress log](../PROGRESS.md).

## Review questions

1. Which collection fits a mapping from usernames to scores?
2. How do a list and a tuple differ?
3. What does in check when used on a dictionary?
4. Why can changing other also change names after other = names?
5. How do you create an empty set, and why not use {}?
