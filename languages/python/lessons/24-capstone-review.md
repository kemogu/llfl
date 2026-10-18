# Lesson 24: Capstone review and continued learning

[Previous lesson](23-capstone-build.md) · [Schedule](../SCHEDULE.md) · [Progress log](../PROGRESS.md)

**Goal:** Validate, explain, and improve your program using evidence.

**Prerequisite:** Complete lesson 23 and its practice exercise first.

**Time:** 45–60 minutes for study, plus a separate 45–60-minute practice session. Project lessons may need additional sessions.

## Learn and try

Finishing a project means more than seeing one successful run. Review the behavior someone else would depend on. Use a fresh temporary data location and run through this checklist:

- Read --help and follow the README from a fresh terminal.
- Add two tasks, list them, complete one, and filter unfinished tasks.
- Restart and verify the IDs, titles, and completion state survive.
- Try an empty title, a missing ID, and an inaccessible storage path.
- If using JSON, try malformed and structurally invalid data without overwriting it.
- Run automated tests and verify they do not alter your working data.

For the suggested layout, run tests from `practice/capstone/` with:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

Read your code aloud. Explain each function's inputs, outputs, side effects, and failures. Look for duplicated validation, overly broad exception handlers, and unnecessary shared state. Refactor one issue at a time and rerun relevant tests. Measure before making performance changes.

Write a retrospective: what you can now do independently, what still needs help, one bug you investigated, and the next small project you want to build. Keep a short demonstration transcript and your test results as evidence.

This course introduces advanced Python concepts; expertise comes from applying them repeatedly. Choose a next direction based on your goals: automation, web development, data analysis, or deeper language internals. Build a focused project in that direction, consult its official documentation, and return to weak areas rather than rushing through more topics.

## Practice exercise

Complete the review checklist, fix one design issue without changing intended behavior, and write a retrospective. Prepare a five-minute explanation of the project and send your code plus unanswered questions for review.

Before moving on, run your work, explain it in your own words, and record one thing you learned in [your progress log](../PROGRESS.md).

## Review questions

1. Which evidence shows your project is usable from a fresh start?
2. What is the difference between refactoring and adding behavior?
3. How did your tests protect the code during a refactor?
4. Which Python concept is still hardest for you, and what exercise would target it?
5. What will your next project be, and which concrete skills will it practice?
