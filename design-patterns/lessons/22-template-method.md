# Lesson 22: Template Method

[Previous lesson](21-strategy.md) · [Schedule](../SCHEDULE.md) · [Next lesson](23-observer.md)

**Goal:** Keep an algorithm’s sequence stable while allowing selected steps to vary.

**Prerequisite:** Complete lesson 21 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** Several algorithms repeat the same ordered workflow but differ in a few well-defined steps.

**Typical symptoms:** Export subclasses duplicate load/transform/save orchestration, and changes to that sequence must be copied into each variant.

**How this lesson addresses it:** Put the sequence in a nonvirtual run method and call protected virtual steps. Subclasses customize transformation while the base workflow retains the required order.

**When to keep it simpler / limits:** Use composition when steps must be independently recombined. Template Method couples subclasses to the base workflow, so unstable skeletons make it harder to maintain.

## Learn and try

Template Method places the algorithm skeleton in a base class and calls overridable primitive operations for variation. The template operation itself is normally nonvirtual, preventing subclasses from changing the promised sequence. Optional hooks can default to doing nothing; required steps can be pure virtual.

The example always reads, then formats. A subclass supplies those steps but cannot override `run` through the base contract. A virtual destructor supports polymorphic destruction. This is inheritance-based reuse; Strategy instead varies behavior through composed objects.

Use Template Method for a stable workflow whose subclasses customize a few well-defined steps. Keep hooks narrow and document their allowed effects. Avoid calling overridable methods from constructors or destructors expecting derived behavior: virtual dispatch there does not behave like calls on a fully constructed derived object. When steps should be independently recombined, composition or a function accepting callables may be simpler.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <string>

class ExportJob {
protected:
    virtual std::string read() const = 0;
    virtual std::string format(const std::string&) const = 0;
public:
    virtual ~ExportJob() = default;
    std::string run() const {
        const auto data = read();
        return format(data);
    }
};
struct TextJob : ExportJob {
    std::string read() const override { return "sample"; }
    std::string format(const std::string& data) const override {
        return "text:" + data;
    }
};
int main() {
    TextJob job;
    const ExportJob& base = job;
    assert(base.run() == "text:sample");
}
```

Write down the operation sequence before adding a subclass. Confirm that clients call `run` rather than orchestrating individual steps themselves.

## Practice setup

Create `design-patterns/practice/lesson_22/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_22/question_1.cpp -o /tmp/llfl-design-patterns/lesson_22_question_1
/tmp/llfl-design-patterns/lesson_22_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Define a skeleton

**Answer file:** `question_1.cpp`

Create abstract Pipeline with nonvirtual run() calling load(), transform(data), then save(result). Define protected virtual steps and a virtual destructor. Implement one pipeline loading `"a"`, prefixing `"T:"`, and storing `"T:a"`. Assert the stored result.

### Question 2: Vary one step

**Answer file:** `question_2.cpp`

Add a subclass using the same load/save behavior but transform producing `"[a]"`. Reuse a common concrete base for those shared steps if useful. Assert both pipeline outputs through Pipeline references.

### Question 3: Observe sequence

**Answer file:** `question_3.cpp`

Record events in a vector inside test steps. Assert a successful run logs exactly `"load"`, `"transform"`, `"save"`. Ensure run remains nonvirtual and no subclass duplicates its ordering logic.

### Question 4: Define failure behavior

**Answer file:** `question_4.cpp`

Add a pipeline whose transform throws `std::runtime_error`. Verify run propagates the error and save is never called. The event sequence should stop after load and transform.

### Question 5: Compare composition

**Answer file:** `question_5.cpp`

Implement a free run function accepting load/transform/save `std::function` callables from `<functional>`. Reproduce `"T:a"` and the same ordering. Explain when independently replaceable steps make this preferable to inherited hooks.

## Request review

Compile and run all five answers and send: “Design patterns lesson 22 answers are ready in `design-patterns/practice/lesson_22/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
