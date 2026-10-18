# Python learning plan

## Goal

Learn Python from the basics through advanced concepts by writing and reviewing real code. No previous programming knowledge is required. We will study one lesson at a time and adjust the pace based on your progress.

## Our lesson agreement

1. I prepare **one Markdown file per lesson** in `languages/python/lessons/`.
2. Each lesson explains its topic with examples and ends with **exactly five coding questions** about that lesson. The questions must be answerable with Python code using concepts already taught.
3. You create **five separate `.py` files**, one answer per question. I leave the answers for you to write.
4. You run your files and tell me when they are ready for review.
5. I read all five files, run appropriate checks, explain mistakes, and give feedback for each answer.
6. You revise any answers that need corrections. We move to the next lesson after all five answers meet their requirements and you understand the corrections.

Theory explanations can be included as comments in your Python files, but each question will have a concrete coding task. Every question will state what the program should do, with expected output or example inputs where helpful. Questions will progress from a small guided task to an independent application of the lesson.

## File organization

For lesson 1, the lesson file and your answer files will be:

```text
languages/python/
    PLAN.md
    lessons/
        01-first-program.md
    practice/
        lesson_01/
            question_1.py
            question_2.py
            question_3.py
            question_4.py
            question_5.py
```

Use `lesson_02/`, `lesson_03/`, and so on for later lessons. Create the answer files yourself when you start the questions. Optional experiments can go in a separate `scratch.py` file.

Run an answer from the repository root with:

```bash
python3 languages/python/practice/lesson_01/question_1.py
```

Use `python` or `py` instead if that is your system's Python 3 command. Later project lessons may share project modules, but you will still submit five clearly named answer scripts; each will demonstrate or test its assigned requirement.

## Schedule

The starting pace is **12 weeks, two lessons per week**, with four sessions of about **45–60 minutes**:

| Session | Work |
| --- | --- |
| Monday | Learn the first lesson and try its examples. |
| Tuesday | Write its five answer files and request my review. |
| Thursday | Correct answers if needed; otherwise start the next lesson. |
| Saturday | Write the next five answers and request review. |

These days are suggestions, not fixed appointments. Reviews happen when you return to this chat and ask. Corrections take priority over starting another lesson. If you have less time, use one lesson per week for a 24-week plan. Projects and difficult topics can take extra sessions. Advanced proficiency will require continued practice beyond this course.

## Learning roadmap

| Week | Theme | First lesson | Second lesson | Weekly outcome |
| --- | --- | --- | --- | --- |
| 1 | Getting started | [01: Your first Python program](lessons/01-first-program.md) | [02: Variables and basic types](lessons/02-variables-and-types.md) | Run scripts, store values, and calculate a receipt. |
| 2 | Interaction and decisions | [03: Input and string operations](lessons/03-input-and-strings.md) | [04: Conditions and decisions](lessons/04-conditions.md) | Build an input-driven score checker and test boundaries. |
| 3 | Repetition and data | [05: Loops and repetition](lessons/05-loops.md) | [06: Lists, tuples, dictionaries, and sets](lessons/06-collections.md) | Summarize a collection of student scores. |
| 4 | Reusable transformations | [07: Functions, parameters, and return values](lessons/07-functions.md) | [08: Comprehensions, unpacking, and sorting](lessons/08-comprehensions-and-sorting.md) | Build functions and produce a sorted student ranking. |
| 5 | Reliable persistence | [09: Exceptions and input validation](lessons/09-exceptions.md) | [10: Files, paths, and JSON](lessons/10-files-and-json.md) | Validate input and save structured data to JSON. |
| 6 | Your first application | [11: Modules and virtual environments](lessons/11-modules-and-environments.md) | [12: Project: a persistent task tracker](lessons/12-first-project.md) | Organize modules and finish the first task tracker. |
| 7 | Object-oriented design | [13: Classes and objects](lessons/13-classes.md) | [14: Dataclasses and composition](lessons/14-dataclasses-and-composition.md) | Model tasks and separate service logic from storage. |
| 8 | Testing and lazy processing | [15: Automated tests and debugging](lessons/15-testing-and-debugging.md) | [16: Iterators and generators](lessons/16-iterators-and-generators.md) | Add behavioral tests and process data with generators. |
| 9 | Advanced function design | [17: Decorators and context managers](lessons/17-decorators-and-context-managers.md) | [18: Type hints and clear interfaces](lessons/18-typing-and-design.md) | Practice decorators, resource handling, and type contracts. |
| 10 | Performance and concurrency | [19: Algorithms and performance](lessons/19-algorithms-and-performance.md) | [20: Concurrency and async programming](lessons/20-concurrency-and-async.md) | Measure algorithms and simulate concurrent waiting. |
| 11 | Application interfaces | [21: SQLite and parameterized queries](lessons/21-sqlite.md) | [22: Command-line interfaces and logging](lessons/22-cli-and-logging.md) | Practice SQLite and add command-line operations. |
| 12 | Capstone and review | [23: Capstone: design and build](lessons/23-capstone-build.md) | [24: Capstone review and continued learning](lessons/24-capstone-review.md) | Build, verify, document, and explain your finished project. |

## How to request a review

After saving your five files, send a message like:

> Lesson 1 answers are ready in `languages/python/practice/lesson_01/`. Please check all five files.

Mention anything confusing and include any error you cannot resolve. I will check:

- **Correctness:** Does each program satisfy its question?
- **Understanding:** Does the solution use the concepts taught in the lesson?
- **Clarity:** Are names, formatting, and structure understandable?
- **Relevant edge cases:** Does it handle the inputs required by the question?

For each file, I will report **Complete** or **Needs revision**, explain why, and provide a focused hint or correction. I will not replace your answers unless you ask me to. After your revisions, I will check again.

## Current status and next step

This plan is the agreed workflow. All 24 lesson files now include step-by-step practice instructions and five coding questions, each assigned to its own answer file. We will study and review them one lesson at a time.

**Next: lesson 1 — Your first Python program.** We will cover running a `.py` file, `print()`, text, simple calculations, comments, and basic syntax errors. Its five coding questions are ready for you to work through in order.
