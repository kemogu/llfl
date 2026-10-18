# Practice answers

Create `lesson_01/` when starting the first lesson. Write `question_1.cpp` through `question_5.cpp`, one file for each question. Continue with a new numbered folder for every lesson.

Write the answers yourself. Run each program from the repository root, including its assertions:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_01/question_1.cpp -o /tmp/llfl-design-patterns/question_1
/tmp/llfl-design-patterns/question_1
```

Use `scratch.cpp` for optional experiments. Keep required explanations as comments in the matching answer. Capstone lessons may use shared headers and source files, but each of the five answer programs must demonstrate its assigned requirement.

Ask for a review of all five files and revise where needed. See the [plan](../PLAN.md) for review criteria.

Each answer has its own `main()` and is compiled separately. Change the source and executable names for each question. Use `clang++` in place of `g++` if needed. Keep assertions enabled by compiling without `-DNDEBUG`.
