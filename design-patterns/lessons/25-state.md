# Lesson 25: State

[Previous lesson](24-command.md) · [Schedule](../SCHEDULE.md) · [Next lesson](26-chain-of-responsibility.md)

**Goal:** Delegate behavior according to an explicit state machine.

**Prerequisite:** Complete lesson 24 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** An object’s response to events depends on its lifecycle state, and transition logic is scattered across operations.

**Typical symptoms:** Pay, ship, and cancel each contain overlapping state checks, making invalid transitions easy to accept accidentally.

**How this lesson addresses it:** Represent Draft, Paid, and Shipped behavior with state objects. The context delegates an event and applies the resulting transition after the state method returns.

**When to keep it simpler / limits:** An enum and a transition table or switch are often clearer for a small machine. State differs from Strategy because lifecycle transitions determine which behavior is active.

## Learn and try

State moves state-dependent behavior into state objects. The context delegates an event to its current state, then changes state according to the result. Unlike Strategy, the focus is valid transitions over time rather than client-selected interchangeable algorithms.

Here a gate has Closed and Open states. Each state computes the next state ID on a toggle; the context replaces its owning pointer after the call returns. This sequencing avoids deleting a state while one of its member functions is still executing. `enum class` gives named state IDs with scoped enumerators. This small machine could be implemented more simply as an enum and a switch.

Use State when state-specific behavior and transitions have grown complex enough to benefit from separate objects. Define every event in every state, including invalid transitions, and test sequences rather than only individual states. Keep the transition table visible in explanations. Extra classes are not useful for a trivial two-state flag unless the lesson is explicitly exploring the pattern.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <memory>

enum class Mode { closed, open };
struct GateState {
    virtual ~GateState() = default;
    virtual Mode mode() const = 0;
    virtual Mode toggle() const = 0;
};
struct Closed : GateState {
    Mode mode() const override { return Mode::closed; }
    Mode toggle() const override { return Mode::open; }
};
struct Open : GateState {
    Mode mode() const override { return Mode::open; }
    Mode toggle() const override { return Mode::closed; }
};
class Gate {
    std::unique_ptr<GateState> state_ = std::make_unique<Closed>();
public:
    Mode mode() const { return state_->mode(); }
    void toggle() {
        const Mode next = state_->toggle();
        if (next == Mode::open) state_ = std::make_unique<Open>();
        else state_ = std::make_unique<Closed>();
    }
};
int main() {
    Gate gate;
    assert(gate.mode() == Mode::closed);
    gate.toggle();
    assert(gate.mode() == Mode::open);
    gate.toggle();
    assert(gate.mode() == Mode::closed);
}
```

Write the two-row transition table. Identify why replacement happens after `toggle()` on the state returns.

## Practice setup

Create `design-patterns/practice/lesson_25/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_25/question_1.cpp -o /tmp/llfl-design-patterns/lesson_25_question_1
/tmp/llfl-design-patterns/lesson_25_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Specify transitions

**Answer file:** `question_1.cpp`

Implement an enum-based order machine: Draft can pay to become Paid; Paid can ship to become Shipped. All other pay/ship attempts throw `std::logic_error` without changing state. Assert Draft→Paid→Shipped and an invalid ship from Draft.

### Question 2: Extract state objects

**Answer file:** `question_2.cpp`

Create state classes behind an interface with current mode and next(event). Return a mode from next rather than replacing the state inside its own method. Make the context own and replace the state after delegation. Preserve question 1’s checks.

### Question 3: Check invalid events

**Answer file:** `question_3.cpp`

For every state test both pay and ship against the transition table: Draft/pay succeeds, Paid/ship succeeds, and the other four combinations fail without mutation. Use fresh contexts or valid setup sequences for each test.

### Question 4: Add cancellation

**Answer file:** `question_4.cpp`

Add Cancelled and a cancel event valid only from Draft and Paid. Shipped/cancel and any event from Cancelled fail. Assert Draft→Cancelled and Draft→Paid→Cancelled, and the two invalid cancellation cases. Keep state replacement safe.

### Question 5: Compare implementations

**Answer file:** `question_5.cpp`

Implement the same four-state machine using an enum and a switch. Feed both implementations the valid sequences pay/ship, cancel, and pay/cancel, checking equal resulting states; check both reject ship from Draft. Explain when state classes earn their extra structure.

## Request review

Compile and run all five answers and send: “Design patterns lesson 25 answers are ready in `design-patterns/practice/lesson_25/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
