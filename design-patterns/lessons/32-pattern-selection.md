# Lesson 32: Pattern selection and simplification

[Previous lesson](31-interpreter.md) · [Schedule](../SCHEDULE.md) · [Next lesson](33-capstone-build.md)

**Goal:** Choose designs by the problem they solve and remove abstractions that do not help.

**Prerequisite:** Complete lesson 31 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** A design chooses patterns by name or diagram rather than a demonstrated problem, accumulating unnecessary abstraction.

**Typical symptoms:** A tiny fixed rule gains factories and wrappers without improving testing or accommodating an actual variation.

**How this lesson addresses it:** Compare a pattern-based implementation with a simpler function under shared behavior checks. Retain a pricing or notification boundary when it solves a concrete replacement or testing need.

**When to keep it simpler / limits:** This is a selection and refactoring exercise, not another GoF pattern. Fewer lines alone are not a reason to remove a useful contract.

## Learn and try

Start with a concrete source of change, a behavioral contract, and the simplest working implementation. Then ask whether a pattern solves that problem with an acceptable cost. Recognizing a similar class diagram is not sufficient: intent distinguishes Adapter from Decorator and Proxy, and Strategy from State.

Compare construction choices by what varies: Factory Method varies product creation inside an inherited workflow; Abstract Factory supplies related product families; Builder varies staged construction; Prototype copies configured objects. Compare coordination choices by the relationship: Observer broadcasts to subscribers, Mediator centralizes peer interactions, and Command packages an action.

The example has only two stable shipping choices. An enum and a function make the rule visible without factories, inheritance, or allocation. If policies later become configurable objects with independent behavior, Strategy may become worthwhile. Simplification should preserve behavior, exceptions, and relevant side effects. Do not remove a boundary merely to reduce line count if it isolates a real dependency or enforces a useful contract.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <stdexcept>

enum class Delivery { standard, express };
int shipping_total(int subtotal, Delivery delivery) {
    if (subtotal < 0) throw std::invalid_argument("negative subtotal");
    const int fee = delivery == Delivery::standard ? 100 : 300;
    return subtotal + fee;
}
int main() {
    assert(shipping_total(500, Delivery::standard) == 600);
    assert(shipping_total(500, Delivery::express) == 800);
}
```

Name the specific future requirement that would justify replacing this function with policy objects. Avoid arguing that more classes alone make it more extensible.

## Practice setup

Create `design-patterns/practice/lesson_32/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_32/question_1.cpp -o /tmp/llfl-design-patterns/lesson_32_question_1
/tmp/llfl-design-patterns/lesson_32_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Choose by intent

**Answer file:** `question_1.cpp`

Write three small working wrappers: an Adapter translating `Legacy::fetch()` to `Source::read()`, a Decorator adding brackets to a compatible Source result, and a Proxy caching a compatible Source result. For source text `"x"`, assert adapter `"x"`, decorator `"[x]"`, and two cached reads with one underlying call. Comment on each wrapper’s different intent.

### Question 2: Separate strategy from state

**Answer file:** `question_2.cpp`

Implement two discount policies selected by a client (no discount and ten percent), plus a two-state order that changes from Draft to Paid on pay. Assert payable 1000/900 for the policies and Draft→Paid for the order. Explain why selecting an algorithm and advancing a lifecycle are different problems.

### Question 3: Remove an unnecessary hierarchy

**Answer file:** `question_3.cpp`

Implement standard/express shipping behind an interface, then implement the worked example’s simpler function. Assert equal results for subtotals 0, 500, and 1000 for both choices, and matching rejection of negative input. Comment on the known requirement that makes simplification reasonable.

### Question 4: Keep a useful boundary

**Answer file:** `question_4.cpp`

Implement a notification service with a borrowed Notifier interface and a recording test implementation. Confirm exactly one `"done"` notification from a successful operation. Compare with a direct console-coupled version by explaining, in comments, which observable tests and replacement ability the boundary preserves. No external I/O is required.

### Question 5: Make a reviewable decision

**Answer file:** `question_5.cpp`

Choose one of your implementations from questions 1–4. Present a simpler alternative in the same answer and run shared behavior checks against both for normal and boundary inputs. Add a short comment listing the requirement, selected design, rejected alternative, and one future change that would make you reconsider. Do not add a pattern without a demonstrated requirement.

## Request review

Compile and run all five answers and send: “Design patterns lesson 32 answers are ready in `design-patterns/practice/lesson_32/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
