# Lesson 03: Single Responsibility Principle (SRP)

[Previous lesson](02-composition-inheritance-and-contracts.md) · [Schedule](../SCHEDULE.md) · [Next lesson](04-open-closed.md)

**Goal:** Separate code that changes for different business reasons.

**Prerequisite:** Complete lesson 02 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** One module changes for unrelated reasons, so independent requirements interfere with each other.

**Typical symptoms:** A pricing-rule change, receipt-layout change, and recording change all require edits to the same class and its tests.

**How this lesson addresses it:** Apply SRP by separating price calculation, formatting, and recording. A layout change then affects presentation without forcing changes to the calculation.

**When to keep it simpler / limits:** SRP is a principle, not a one-method-per-class rule. Keep closely related operations together and avoid splitting cohesive code into tiny forwarding classes.

## Learn and try

SRP says a module should have one reason to change: it should serve a cohesive responsibility associated with one actor or concern. It does not mean one method per class. Pricing rules and report layout can change for different reasons, even when today they occupy only a few lines.

The example separates score rules from text presentation. The calculation has no output side effects, so it can be tested without inspecting a console. The formatter knows the result but not the scoring algorithm. A small coordinating function could call both without owning either concern.

Use this separation when changes and tests naturally cluster around different concerns. Avoid splitting every line into its own class; that scatters a simple operation across many files. A pair of functions can satisfy SRP just as well as a class hierarchy. During refactoring, preserve outputs and exceptions with checks written before moving code.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <string>
#include <stdexcept>

int score(int correct, int wrong) {
    if (correct < 0 || wrong < 0) {
        throw std::invalid_argument("negative count");
    }
    return correct * 3 - wrong;
}
std::string format_score(int value) {
    return "Score: " + std::to_string(value);
}
int main() {
    assert(score(4, 1) == 11);
    assert(format_score(score(4, 1)) == "Score: 11");
}
```

Change the label to `Result` and observe which assertion needs an intentional update. The scoring behavior should remain unchanged.

## Practice setup

Create `design-patterns/practice/lesson_03/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_03/question_1.cpp -o /tmp/llfl-design-patterns/lesson_03_question_1
/tmp/llfl-design-patterns/lesson_03_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Capture mixed behavior

**Answer file:** `question_1.cpp`

Write one `invoice(price, quantity)` function that calculates and formats `"Total: 600 cents"` for price 200 and quantity 3. Assume nonnegative inputs. Assert this and the zero-quantity output `"Total: 0 cents"`. Comment on two independent reasons this function might change.

### Question 2: Separate responsibilities

**Answer file:** `question_2.cpp`

Extract `total_cents` and `format_total` from question 1. Keep `invoice` as a coordinator. Preserve both earlier output checks and assert `total_cents(200, 3) == 600` directly.

### Question 3: Change presentation independently

**Answer file:** `question_3.cpp`

Add `format_csv(total)` returning `"total_cents,600"` for 600. Use the same calculation with both formatters. Assert the original text and CSV strings. Do not put formatting choices inside the calculation.

### Question 4: Separate recording

**Answer file:** `question_4.cpp`

Add an in-memory `Recorder` with a `std::vector<int>` and `record(int)` method. A coordinating function computes a total, records it once, and returns the formatted text. Process totals 600 and 0; assert two recorded entries in order and both returned strings.

### Question 5: Protect behavior during change

**Answer file:** `question_5.cpp`

Add negative price/quantity validation to the calculation, throwing `std::invalid_argument`. Verify that valid output remains unchanged and an invalid invoice does not append to the recorder. Explain which responsibility owns validation and why.

## Request review

Compile and run all five answers and send: “Design patterns lesson 3 answers are ready in `design-patterns/practice/lesson_03/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
