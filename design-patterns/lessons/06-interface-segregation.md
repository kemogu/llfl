# Lesson 06: Interface Segregation Principle (ISP)

[Previous lesson](05-liskov-substitution.md) · [Schedule](../SCHEDULE.md) · [Next lesson](07-dependency-inversion.md)

**Goal:** Give each client the capabilities it actually needs.

**Prerequisite:** Complete lesson 05 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** A broad interface forces clients and implementations to depend on operations they do not need or cannot support.

**Typical symptoms:** A basic printer must implement scan() only to throw an unsupported-operation error, while print-only clients depend on scanning declarations.

**How this lesson addresses it:** Split printing and scanning into client-oriented capabilities. A printer implements printing alone; an office device can implement both.

**When to keep it simpler / limits:** ISP does not require one interface per method. Keep operations together when a real client uses them as one cohesive contract.

## Learn and try

ISP favors interfaces tailored to clients rather than a large interface that forces unrelated operations on every implementation. A read-only view should not require `save` or `erase` merely because another client needs them. Unsupported operations are often a sign that capability boundaries are wrong.

The example separates reading and writing. `Cell` implements both, while a display client accepts only `Readable`. Multiple inheritance here combines abstract capabilities, not shared implementation state. Each interface has a virtual destructor. The concrete object still has one lifetime; references to either capability borrow it.

Use this when clients need different subsets of behavior or implementations lack some capabilities. Do not create one-method interfaces automatically: methods that belong to the same client contract can stay together. For local code with no substitutable implementations, ordinary concrete methods may be enough. A compile-time restriction helps prevent accidental calls, while behavioral tests still verify what supported calls do.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>

struct Readable {
    virtual ~Readable() = default;
    virtual int read() const = 0;
};
struct Writable {
    virtual ~Writable() = default;
    virtual void write(int value) = 0;
};
class Cell : public Readable, public Writable {
    int value_ = 0;
public:
    int read() const override { return value_; }
    void write(int value) override { value_ = value; }
};
int display_value(const Readable& source) { return source.read(); }
int main() {
    Cell cell;
    Writable& writer = cell;
    writer.write(7);
    assert(display_value(cell) == 7);
}
```

Observe that `display_value` cannot call `write` through its parameter. Do not leave deliberately uncompilable lines active in a submitted answer.

## Practice setup

Create `design-patterns/practice/lesson_06/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_06/question_1.cpp -o /tmp/llfl-design-patterns/lesson_06_question_1
/tmp/llfl-design-patterns/lesson_06_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Separate capabilities

**Answer file:** `question_1.cpp`

Define `Printable` returning a string from `print()` and `Scannable` returning a string from `scan()`, both const. Implement `BasicPrinter` as printable only, returning `"printed"`. Assert a print-only client works without a dummy scan method.

### Question 2: Combine supported roles

**Answer file:** `question_2.cpp`

Implement `OfficeDevice` supporting both interfaces. Return `"printed"` and `"scanned"`. Exercise it through separate interface references and assert both results.

### Question 3: Narrow the client

**Answer file:** `question_3.cpp`

Write `copy_document(const Scannable&)` returning the scanned text prefixed with `"copy:"`. Implement a scan-only object returning `"page"`; assert `"copy:page"`. Keep printing outside this client.

### Question 4: Provide a read-only view

**Answer file:** `question_4.cpp`

Define `TaskReader` exposing `count() const` and `TaskWriter` exposing `add()`. Implement an in-memory task count supporting both. Write a client taking only a reader; assert 0 initially and 2 after two additions via a writer. State the view’s lifetime requirement.

### Question 5: Keep cohesive operations together

**Answer file:** `question_5.cpp`

Define one `Queue` interface with `push(int)`, `empty() const`, and `pop()` because a queue-processing client needs all three. Implement it with `std::vector<int>`; `pop()` returns/removes the first value and throws `std::out_of_range` when empty. Check FIFO order for 4 then 7 and the empty error. Explain why ISP does not force three interfaces here.

## Request review

Compile and run all five answers and send: “Design patterns lesson 6 answers are ready in `design-patterns/practice/lesson_06/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
