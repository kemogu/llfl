# Lesson 05: Liskov Substitution Principle (LSP)

[Previous lesson](04-open-closed.md) · [Schedule](../SCHEDULE.md) · [Next lesson](06-interface-segregation.md)

**Goal:** Check behavioral substitutability, including failures and side effects.

**Prerequisite:** Complete lesson 04 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** An implementation fits a base interface syntactically but breaks assumptions that clients rely on.

**Typical symptoms:** A supposedly interchangeable counter silently stops incrementing, or a reader changes its output argument when the contract says end-of-input preserves it.

**How this lesson addresses it:** Write shared behavioral checks for every implementation. A capped counter that cannot satisfy unlimited increment behavior gets a separate capability contract rather than pretending to be substitutable.

**When to keep it simpler / limits:** LSP is a behavioral principle. Matching signatures and passing a few tests do not prove every possible use is valid; document preconditions, results, failures, and side effects.

## Learn and try

LSP requires derived implementations to remain usable wherever their base contract is expected. Matching method names is not enough. An implementation must not demand stronger preconditions, weaken promised results, or violate invariants clients rely on.

The reader contract below returns one stored character per successful read. End-of-input returns `false`, preserves the output argument, and stays at end on future reads. A client can work with any implementation that honors those rules. A reader that clears the output at end would violate the contract even though its signature matches.

Use a contract test against each implementation, including boundaries. Do not “fix” a substitution problem with type checks scattered through clients. If a type cannot honor an operation, consider a smaller interface or composition. A common mistake is inheriting only for code reuse while throwing “unsupported” for behavior the base promises. Tests provide evidence for tested cases, not a proof for every possible input.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <string>
#include <utility>
#include <cstddef>

struct Reader {
    virtual ~Reader() = default;
    virtual bool next(char& output) = 0;
};
class StringReader : public Reader {
    std::string text_;
    std::size_t position_ = 0;
public:
    explicit StringReader(std::string text) : text_(std::move(text)) {}
    bool next(char& output) override {
        if (position_ == text_.size()) return false;
        output = text_[position_++];
        return true;
    }
};
void check_one_character(Reader& reader) {
    char output = '?';
    assert(reader.next(output) && output == 'A');
    assert(!reader.next(output) && output == 'A');
    assert(!reader.next(output));
}
int main() {
    StringReader reader("A");
    check_one_character(reader);
}
```

Temporarily clear `output` at end-of-input and observe the contract check fail. Restore the correct implementation before continuing.

## Practice setup

Create `design-patterns/practice/lesson_05/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_05/question_1.cpp -o /tmp/llfl-design-patterns/lesson_05_question_1
/tmp/llfl-design-patterns/lesson_05_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: State and implement a contract

**Answer file:** `question_1.cpp`

Define `Counter` with `increment()` and `value() const`: initial value is 0, each increment adds exactly 1, and reading has no side effect. Implement `BasicCounter`; assert initial 0, then 1 and 2 after two calls.

### Question 2: Apply one test to two types

**Answer file:** `question_2.cpp`

Implement `LoggedCounter` honoring the same contract while recording the values reached in a vector. Write a shared `check_counter(Counter&)` for a fresh counter and run it on both types. Also assert the logged values are 1 and 2.

### Question 3: Expose a violation

**Answer file:** `question_3.cpp`

Implement `CappedCounter` that stops at 1. Write a boolean contract probe checking two increments reach 2; assert it returns true for `BasicCounter` and false for `CappedCounter`, so your answer exits successfully while demonstrating the defect. Explain why silently capping breaks substitution.

### Question 4: Repair the abstraction

**Answer file:** `question_4.cpp`

Give capped behavior its own `try_increment()` API returning false when a configured limit is reached, without deriving from `Counter`. For limit 1, assert true then false, with value remaining 1. Keep a regular counter usable through the original interface.

### Question 5: Check failure behavior

**Answer file:** `question_5.cpp`

Define a separate `NonnegativeStore` contract: initial 0; `set(n)` stores nonnegative n; negative n throws `std::invalid_argument` and preserves the prior value. Implement two stores, one with audit logging of successful writes. Run the same checks for set(4), set(-1), and read()==4 on both.

## Request review

Compile and run all five answers and send: “Design patterns lesson 5 answers are ready in `design-patterns/practice/lesson_05/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
