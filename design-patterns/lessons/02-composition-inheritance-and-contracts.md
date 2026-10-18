# Lesson 02: Composition, inheritance, and contracts

[Previous lesson](01-responsibilities-and-behavior.md) · [Schedule](../SCHEDULE.md) · [Next lesson](03-single-responsibility.md)

**Goal:** Choose a collaboration boundary and describe the behavior clients can rely on.

**Prerequisite:** Complete lesson 01 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** Code reuses implementation through inheritance even when the derived type cannot honor the base behavior, or clients depend directly on one concrete collaborator.

**Typical symptoms:** A subclass disables inherited operations, or changing a formatter requires changing every client that uses it.

**How this lesson addresses it:** Let a label compose a formatter, and define the behavior that every formatter must provide. The client can use interchangeable implementations without inheriting their implementation details.

**When to keep it simpler / limits:** Use a concrete member or free function when substitution is unnecessary. Composition still requires explicit ownership and lifetime rules.

## Learn and try

Composition gives an object another object to work with; inheritance makes a type usable through a base interface. Prefer composition for “uses a” relationships. Inherit publicly only when the derived object can honor the base contract, not merely to reuse implementation.

A contract includes accepted input, returned values, failures, and relevant side effects. In this example, a formatter accepts any string and returns a string without altering the caller's input. `Label` borrows a formatter through a `const` reference; the formatter must outlive the label. The interface has a virtual destructor so future owning base pointers can destroy derived objects safely. `override` lets the compiler check that a derived declaration actually overrides a virtual method.

The client stores a reference rather than a base object: storing a derived object by base value would slice away derived state. Use this structure when interchangeable behavior matters. For one stable formatting rule, a free function is simpler. Interfaces add indirection and lifetime obligations; they do not automatically improve every program.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <string>

struct Formatter {
    virtual ~Formatter() = default;
    virtual std::string format(const std::string& text) const = 0;
};
struct Brackets : Formatter {
    std::string format(const std::string& text) const override {
        return "[" + text + "]";
    }
};
class Label {
    const Formatter& formatter_;
public:
    explicit Label(const Formatter& formatter) : formatter_(formatter) {}
    std::string show(const std::string& text) const {
        return formatter_.format(text);
    }
};
int main() {
    Brackets formatter;
    Label label(formatter);
    assert(label.show("ready") == "[ready]");
    assert(label.show("") == "[]");
}
```

Draw which object owns or borrows each dependency. Add a formatter locally that adds parentheses and predict the two outputs before running it.

## Practice setup

Create `design-patterns/practice/lesson_02/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_02/question_1.cpp -o /tmp/llfl-design-patterns/lesson_02_question_1
/tmp/llfl-design-patterns/lesson_02_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Describe a contract in code

**Answer file:** `question_1.cpp`

Write `Square` with `area(int side)` returning `side * side` for nonnegative inputs and throwing `std::invalid_argument` for a negative side. Include `<stdexcept>`. Assert areas 0 and 9 for sides 0 and 3, and check the negative-input exception. State this contract in a comment.

### Question 2: Use composition

**Answer file:** `question_2.cpp`

Write `Printer` that borrows a `Square` object and returns `"Area: 9"` for side 3 using `std::to_string`. Keep area calculation in `Square`. Assert the output and declare the dependency before the printer so it outlives the client.

### Question 3: Define a polymorphic contract

**Answer file:** `question_3.cpp`

Introduce `Area` with virtual `int value() const` and a virtual destructor. Implement a square of side 3 and a rectangle of sides 2 and 4. Use a function accepting `const Area&` to read both. Assert 9 and 8; dimensions in this question are valid and nonnegative.

### Question 4: Own implementations safely

**Answer file:** `question_4.cpp`

Use `<memory>` and `<vector>` to store both shapes in `std::vector<std::unique_ptr<Area>>`, constructed with `std::make_unique`. Iterate by `const auto&`, sum their areas through the interface, and assert 17. Explain why a vector of base objects would be inappropriate.

### Question 5: Compare a simpler design

**Answer file:** `question_5.cpp`

Implement free functions for square and rectangle area with the same valid inputs as question 3. Check that both approaches produce the same results for square sides 0 and 3 and rectangle dimensions 0-by-4 and 2-by-4. Comment on when runtime substitution would justify the interface.

## Request review

Compile and run all five answers and send: “Design patterns lesson 2 answers are ready in `design-patterns/practice/lesson_02/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
