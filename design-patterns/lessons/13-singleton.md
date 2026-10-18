# Lesson 13: Singleton

[Previous lesson](12-prototype.md) · [Schedule](../SCHEDULE.md) · [Next lesson](14-adapter.md)

**Goal:** Understand single-instance access and the costs of global state.

**Prerequisite:** Complete lesson 12 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** A design explicitly requires one accessible instance of a type within a program, and uncontrolled construction would violate that requirement.

**Typical symptoms:** Callers can create competing instances even though the application requires a single identity. Merely wanting convenient access is not evidence of this requirement.

**How this lesson addresses it:** Restrict construction and expose a function-local static instance, as with immutable application metadata. Check that accessors return the same object.

**When to keep it simpler / limits:** A single object created in main and passed to clients is usually simpler to test. Singleton does not synchronize later mutable operations or guarantee uniqueness across processes.

## Learn and try

Singleton restricts construction and provides one access point to an instance. The C++ example uses a function-local static, initialized on first use, and deletes copying. It controls access to this class within the program; it is not a system-wide uniqueness mechanism across processes.

Since C++11, initialization of a function-local static is thread-safe. That does not make later reads and writes to mutable members thread-safe. This course's example is single-threaded. Static destruction order and access during shutdown can also matter in larger programs.

Use Singleton only when unique identity and global access are both requirements. Often a single object created in `main` and explicitly passed to clients is enough. Global mutable state hides dependencies and carries values between tests. A reset method can mask these problems rather than solve them. Learn the pattern to recognize its tradeoffs; do not use it as the default configuration, logger, or database design.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>

class Settings {
    int level_ = 1;
    Settings() = default;
public:
    Settings(const Settings&) = delete;
    Settings& operator=(const Settings&) = delete;
    static Settings& instance() {
        static Settings settings;
        return settings;
    }
    int level() const { return level_; }
    void set_level(int value) { level_ = value; }
};
int main() {
    auto& first = Settings::instance();
    auto& second = Settings::instance();
    assert(&first == &second);
    first.set_level(3);
    assert(second.level() == 3);
}
```

Predict why a second test in the same process would see level 3 rather than the initial value 1. Compare that with constructing a fresh local settings object.

## Practice setup

Create `design-patterns/practice/lesson_13/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_13/question_1.cpp -o /tmp/llfl-design-patterns/lesson_13_question_1
/tmp/llfl-design-patterns/lesson_13_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Restrict construction

**Answer file:** `question_1.cpp`

Implement a noncopyable `Sequence` Singleton whose `next()` returns 1, 2, 3, and so on. In a fresh program, assert the first two calls return 1 and 2 and two accessors return the same address. Leave forbidden-construction examples as comments only.

### Question 2: Expose hidden coupling

**Answer file:** `question_2.cpp`

Write two functions that each call `Sequence::instance().next()`. Invoke them alternately and assert results 1, 2, and 3 in a fresh process. Explain why neither function owns an independent sequence.

### Question 3: Replace global access

**Answer file:** `question_3.cpp`

Make an ordinary constructible `Counter` and a client borrowing it. Construct two independent counters; assert each client first returns 1. Then share one counter between two clients and assert 1 then 2. Make the ownership visible in `main`.

### Question 4: Test without reset hooks

**Answer file:** `question_4.cpp`

Write a test helper that creates a fresh ordinary counter and checks the first two values. Call that helper twice successfully. Compare with the stateful singleton in comments; do not add a reset method merely to make the singleton appear isolated.

### Question 5: Limit the uniqueness claim

**Answer file:** `question_5.cpp`

Create an immutable `AppInfo` Singleton returning `"demo"` from `name()`. Assert reference identity and the name. Add comments distinguishing one program instance from cross-process uniqueness, and safe static initialization from synchronization of mutable state.

## Request review

Compile and run all five answers and send: “Design patterns lesson 13 answers are ready in `design-patterns/practice/lesson_13/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
