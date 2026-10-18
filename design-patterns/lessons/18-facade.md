# Lesson 18: Facade

[Previous lesson](17-decorator.md) · [Schedule](../SCHEDULE.md) · [Next lesson](19-flyweight.md)

**Goal:** Provide a small entry point for a multi-step subsystem workflow.

**Prerequisite:** Complete lesson 17 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** Clients repeatedly coordinate several subsystem calls and must understand their ordering and intermediate data.

**Typical symptoms:** Every save operation duplicates validation, encoding, and storage steps, and some callers skip or reorder a required step.

**How this lesson addresses it:** Expose a SaveFacade::save operation that coordinates the established subsystem workflow. Callers provide the input and receive its defined success or failure outcome.

**When to keep it simpler / limits:** A helper function may be sufficient for a stateless sequence. Facade simplifies access; it does not automatically make side effects atomic or provide rollback.

## Learn and try

Facade offers a convenient interface over a subsystem. It coordinates existing operations without requiring clients to learn their ordering. Subsystem objects can still be used directly when appropriate; the facade does not need to hide every capability.

The example coordinates preparation and printing. It borrows both components, which remain alive in `main`. Its return value exposes the final result while the caller is spared the intermediate steps. A facade often uses concrete subsystem classes because its purpose is simplification, not necessarily substitution.

Use it when several clients repeatedly perform the same subsystem workflow. Avoid turning it into a class that accumulates every application operation. A helper function may be enough for a stateless sequence. A facade also does not automatically create a transaction: if a later step fails, earlier side effects remain unless rollback is explicitly designed. Test ordering and failure behavior rather than assuming the wrapper makes operations atomic.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <string>

struct Preparer {
    std::string prepare(const std::string& name) const { return "ready:" + name; }
};
struct Printer {
    std::string print(const std::string& data) const { return "printed:" + data; }
};
class PrintFacade {
    const Preparer& preparer_;
    const Printer& printer_;
public:
    PrintFacade(const Preparer& preparer, const Printer& printer)
        : preparer_(preparer), printer_(printer) {}
    std::string run(const std::string& name) const {
        return printer_.print(preparer_.prepare(name));
    }
};
int main() {
    Preparer preparer;
    Printer printer;
    PrintFacade facade(preparer, printer);
    assert(facade.run("report") == "printed:ready:report");
}
```

Describe the workflow a client no longer needs to repeat. Identify which earlier effects would survive if printing threw an exception.

## Practice setup

Create `design-patterns/practice/lesson_18/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_18/question_1.cpp -o /tmp/llfl-design-patterns/lesson_18_question_1
/tmp/llfl-design-patterns/lesson_18_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Build a subsystem

**Answer file:** `question_1.cpp`

Create Validator, Encoder, and Store. Validator rejects empty strings; Encoder returns `"encoded:" + input`; Store appends strings to a vector. Exercise them manually with `"hello"`, asserting one stored `"encoded:hello"`.

### Question 2: Provide one operation

**Answer file:** `question_2.cpp`

Write `SaveFacade::save(text)` borrowing the subsystem objects and calling validate, encode, then store. Assert saving `"hello"` produces the same record as the manual workflow.

### Question 3: Check failed validation

**Answer file:** `question_3.cpp`

Call save with empty input and assert `std::invalid_argument`. Verify no storage append occurred and that a later valid save succeeds once. Keep validation before any storage side effect.

### Question 4: Observe execution order

**Answer file:** `question_4.cpp`

Add a shared vector of event strings to the subsystem test implementations. A valid save must append `"validate"`, `"encode"`, `"store"` in order. Invalid input must append only `"validate"`. Assert exact sequences.

### Question 5: Define failure boundaries

**Answer file:** `question_5.cpp`

Make a store implementation throw `std::runtime_error` before appending data. Check the facade propagates it, the data remains empty, and validate/encode events still occurred. Explain why the facade is not a general rollback mechanism and when a free coordinating function would suffice.

## Request review

Compile and run all five answers and send: “Design patterns lesson 18 answers are ready in `design-patterns/practice/lesson_18/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
