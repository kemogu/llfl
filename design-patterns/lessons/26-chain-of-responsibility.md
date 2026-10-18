# Lesson 26: Chain of Responsibility

[Previous lesson](25-state.md) · [Schedule](../SCHEDULE.md) · [Next lesson](27-iterator.md)

**Goal:** Route requests through ordered handlers with a clear stopping rule.

**Prerequisite:** Complete lesson 25 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** The sender cannot choose a single receiver in advance; an ordered set of candidates must decide who handles a request.

**Typical symptoms:** Approval or routing logic embeds every handler in a large conditional, and changing the order requires rewriting sender code.

**How this lesson addresses it:** Pass an approval request through clerk, manager, and director handlers until the first eligible handler accepts it. Return an explicit unhandled result when nobody accepts.

**When to keep it simpler / limits:** A table and loop may suffice for simple thresholds. Define whether handling stops the chain; first-match routing is different from a pipeline in which every step runs.

## Learn and try

Chain of Responsibility passes a request through candidate handlers until one handles it or the chain ends. A handler knows the next handler, not every possible receiver. This lesson uses first-match handling; pipelines where every step runs need a different explicit contract.

The example maps a nonnegative priority to the first handler whose limit accepts it. The chain owns its successor with a unique pointer. An unhandled request returns `std::nullopt`; `std::optional<T>` represents either a T or no value, and callers check it before dereferencing. Handler order therefore affects the result.

Use a chain when the eligible receiver depends on runtime conditions or the handler set/order is configurable. For two fixed cases, a conditional is simpler. Avoid silently discarding unhandled requests; decide what callers do with them. Ownership by unique pointers keeps this example acyclic. Do not confuse “continue because I cannot handle” with “continue after I handled”; those are different semantics.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <memory>
#include <optional>
#include <string>
#include <utility>

class Handler {
    int limit_;
    std::string name_;
    std::unique_ptr<Handler> next_;
public:
    Handler(int limit, std::string name, std::unique_ptr<Handler> next = nullptr)
        : limit_(limit), name_(std::move(name)), next_(std::move(next)) {}
    std::optional<std::string> handle(int priority) const {
        if (priority <= limit_) return name_;
        if (next_) return next_->handle(priority);
        return std::nullopt;
    }
};
int main() {
    Handler chain(2, "desk", std::make_unique<Handler>(5, "specialist"));
    assert(chain.handle(1).value() == "desk");
    assert(chain.handle(4).value() == "specialist");
    assert(!chain.handle(9).has_value());
}
```

Reverse the limits in a local experiment and predict which handler claims priority 1. Restore the useful order and identify the first-match stopping point.

## Practice setup

Create `design-patterns/practice/lesson_26/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_26/question_1.cpp -o /tmp/llfl-design-patterns/lesson_26_question_1
/tmp/llfl-design-patterns/lesson_26_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Build one handler

**Answer file:** `question_1.cpp`

Implement an approval handler accepting nonnegative amounts up to a configured inclusive limit. Return an optional approver name. A clerk with limit 100 accepts 100 and declines 101; assert both.

### Question 2: Link a chain

**Answer file:** `question_2.cpp`

Build clerk (100), manager (1000), director (5000), owning successors with unique pointers. Assert amounts 50, 500, and 2000 return the respective names.

### Question 3: Check unhandled requests

**Answer file:** `question_3.cpp`

Assert amount 5001 returns no approver. Validate negative amounts at the public entry point with `std::invalid_argument`. Check the failure and no handler reports success.

### Question 4: Observe short-circuiting

**Answer file:** `question_4.cpp`

Record names of visited handlers in a vector passed with the request or borrowed by handlers. For amount 50 assert only clerk is visited; for 500 assert clerk then manager; for 5001 assert all three and no result.

### Question 5: Compare a data-driven chain

**Answer file:** `question_5.cpp`

Implement the same approval rule using a vector of `(limit,name)` pairs and a first-match loop. Check parity at 0, 100, 101, 1000, 1001, 5000, and 5001. Explain when handler objects are useful because handlers do more than a threshold comparison.

## Request review

Compile and run all five answers and send: “Design patterns lesson 26 answers are ready in `design-patterns/practice/lesson_26/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
