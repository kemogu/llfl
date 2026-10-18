# Lesson 24: Command

[Previous lesson](23-observer.md) · [Schedule](../SCHEDULE.md) · [Next lesson](25-state.md)

**Goal:** Represent an action as an object and specify its undo lifecycle.

**Prerequisite:** Complete lesson 23 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** An action must be stored, deferred, passed around, or undone rather than executed immediately and forgotten.

**Typical symptoms:** UI controls directly manipulate receivers, history stores ad hoc flags, and undo behavior is duplicated across callers.

**How this lesson addresses it:** Package a receiver and operation in a Command. An invoker executes commands and retains successful ones in a history for reverse-order undo under a documented contract.

**When to keep it simpler / limits:** A direct function call is enough for immediate actions. Command does not make irreversible side effects reversible, and borrowed receivers must outlive queued commands.

## Learn and try

Command packages an action and its receiver into an object. An invoker can execute it without knowing receiver details, queue it, or retain it for undo. Undo is additional behavior that must be designed; it does not follow automatically from naming something a command.

The example appends text to a borrowed string receiver and stores the previous value. It permits one execute followed by one undo, then another execute. Repeated execute or undo in the wrong state throws `std::logic_error`. Snapshot restoration is valid only under the stated condition that unrelated code does not modify the receiver between execute and undo. A history should undo commands in reverse execution order.

Use Command for deferred actions, history, or interchangeable operations. A direct function call is simpler when an action is executed immediately and forgotten. External actions such as sending an email may be irreversible; an undo API must not imply effects can always be reversed. Commands and their histories must not outlive borrowed receivers.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <string>
#include <stdexcept>
#include <utility>

class AppendCommand {
    std::string& receiver_;
    std::string suffix_;
    std::string before_;
    bool executed_ = false;
public:
    AppendCommand(std::string& receiver, std::string suffix)
        : receiver_(receiver), suffix_(std::move(suffix)) {}
    void execute() {
        if (executed_) throw std::logic_error("already executed");
        before_ = receiver_;
        receiver_ += suffix_;
        executed_ = true;
    }
    void undo() {
        if (!executed_) throw std::logic_error("not executed");
        receiver_ = before_;
        executed_ = false;
    }
};
int main() {
    std::string text = "A";
    AppendCommand command(text, "B");
    command.execute();
    assert(text == "AB");
    command.undo();
    assert(text == "A");
}
```

Try execute/undo/execute and predict the final text. Identify the receiver, command, and invoker (main) even though this small example needs no abstract command interface.

## Practice setup

Create `design-patterns/practice/lesson_24/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_24/question_1.cpp -o /tmp/llfl-design-patterns/lesson_24_question_1
/tmp/llfl-design-patterns/lesson_24_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Package an action

**Answer file:** `question_1.cpp`

Define `Command` with execute/undo and virtual destructor. Implement AddCommand borrowing an integer and storing a positive delta. Starting at 10, execute delta 3 and assert 13; undo and assert 10. Assume results fit in int and no outside mutation occurs.

### Question 2: Enforce lifecycle

**Answer file:** `question_2.cpp`

Reject double execute and undo-before-execute with `std::logic_error`, preserving the receiver. Check both errors and a complete execute/undo/execute sequence ending at 13.

### Question 3: Store a history

**Answer file:** `question_3.cpp`

Implement an invoker owning a vector of successfully executed commands. Execute deltas 3 and 5 on receiver 10; assert 18. Undo and remove the last command, asserting 13, then undo again, asserting 10. Empty history undo returns false.

### Question 4: Do not record failed actions

**Answer file:** `question_4.cpp`

Add a command that throws `std::runtime_error` before changing the receiver. Have the invoker append a command to history only after execute succeeds. Assert receiver and history count are unchanged on this failure. Allocation failures are outside this exercise’s checks.

### Question 5: Compare action objects with calls

**Answer file:** `question_5.cpp`

Implement a direct `add(int&, int)` function and show it yields the same immediate value as AddCommand. Then demonstrate the two-step history from question 3 and explain why retaining command state is useful there. State the no-external-mutation and receiver-lifetime assumptions.

## Request review

Compile and run all five answers and send: “Design patterns lesson 24 answers are ready in `design-patterns/practice/lesson_24/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
