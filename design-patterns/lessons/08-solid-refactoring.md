# Lesson 08: SOLID refactoring workshop

[Previous lesson](07-dependency-inversion.md) · [Schedule](../SCHEDULE.md) · [Next lesson](09-factory-method.md)

**Goal:** Refactor an order calculation with observable contracts and focused dependencies.

**Prerequisite:** Complete lesson 07 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** A small service mixes validation, pricing selection, formatting, and delivery, so each new requirement affects the entire workflow.

**Typical symptoms:** Duplicate calculations and policy branches appear in several places, and invalid orders can produce output before validation fails.

**How this lesson addresses it:** Refactor an order workflow in stages: preserve behavior with checks, isolate pricing behind a contract, and keep side effects after successful validation and calculation.

**When to keep it simpler / limits:** This workshop combines principles rather than introducing another GoF pattern. Add a boundary only when it separates a real concern or variation.

## Learn and try

This workshop combines principles rather than adding an interface for each acronym. Start with behavior checks, identify independent changes, then extract only the seams needed by clients. Pricing policy varies; receipt layout varies independently. A client can depend on a pricing contract while concrete implementations remain interchangeable.

The example delegates a rebate rule, validates at the input boundary, and formats separately. The rule contract returns a reduction between zero and the supplied nonnegative subtotal. The client defensively rejects an invalid result with `std::logic_error`. That check does not make a violating implementation correct; it exposes the defect.

Apply SRP to calculation versus presentation, OCP to additional rules, LSP to rule results, ISP to the small client contract, and DIP to the client's dependency. These concerns overlap. Avoid a repository, event bus, or factory when the exercise has no need for them. Refactoring preserves existing successful outputs; adding new rejection behavior is a separate requirement.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <string>
#include <stdexcept>

struct Rebate {
    virtual ~Rebate() = default;
    virtual int reduction(int subtotal) const = 0;
};
struct NoRebate : Rebate {
    int reduction(int) const override { return 0; }
};
int payable(int subtotal, const Rebate& rule) {
    if (subtotal < 0) throw std::invalid_argument("negative subtotal");
    const int reduction = rule.reduction(subtotal);
    if (reduction < 0 || reduction > subtotal) {
        throw std::logic_error("invalid rebate");
    }
    return subtotal - reduction;
}
std::string receipt(int total) { return "Pay " + std::to_string(total); }
int main() {
    NoRebate rule;
    assert(receipt(payable(800, rule)) == "Pay 800");
}
```

Before extracting another abstraction, describe a concrete change that it would simplify. Record one case where keeping a function is sufficient.

## Practice setup

Create `design-patterns/practice/lesson_08/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_08/question_1.cpp -o /tmp/llfl-design-patterns/lesson_08_question_1
/tmp/llfl-design-patterns/lesson_08_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Freeze the baseline

**Answer file:** `question_1.cpp`

Implement `checkout(price, quantity, member)` returning `"Pay N"`. Subtotal is price times quantity; members receive `subtotal / 10` cents discount using integer division. Reject negative price or quantity. Assert (250,3,false) gives `"Pay 750"`, (250,3,true) gives `"Pay 675"`, and zero quantity gives `"Pay 0"`.

### Question 2: Separate responsibilities

**Answer file:** `question_2.cpp`

Extract validation/calculation and formatting from the baseline. Preserve all three outputs and negative-input failures. Keep text construction out of numeric functions and comment on their independent reasons to change.

### Question 3: Extract policy

**Answer file:** `question_3.cpp`

Introduce `Discount` with a reduction contract like the example. Implement no-discount and ten-percent policies; pass them into a checkout function rather than constructing them inside. Assert the original 750 and 675 outcomes.

### Question 4: Extend and check substitution

**Answer file:** `question_4.cpp`

Add `FixedDiscount(100)` reducing by the smaller of 100 and subtotal. Check totals 0, 0, and 650 for subtotals 0, 50, and 750. Run a shared reduction-contract probe against all policies at these inputs. Reject a deliberately broken policy returning subtotal+1 with `std::logic_error`.

### Question 5: Review the integrated design

**Answer file:** `question_5.cpp`

Add a borrowed `ReceiptSink` that records formatted receipts in memory. Successful checkout records exactly one receipt; negative input and invalid policy output record none. Test all three cases. In comments map the five principles to concrete choices and identify one abstraction you chose not to add.

## Request review

Compile and run all five answers and send: “Design patterns lesson 8 answers are ready in `design-patterns/practice/lesson_08/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
