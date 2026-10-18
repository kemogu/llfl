# Lesson 11: Builder

[Previous lesson](10-abstract-factory.md) · [Schedule](../SCHEDULE.md) · [Next lesson](12-prototype.md)

**Goal:** Separate staged construction from the representation being built.

**Prerequisite:** Complete lesson 10 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** Construction has multiple meaningful steps, optional choices, or different representations, and callers duplicate the assembly sequence.

**Typical symptoms:** Call sites repeat setup operations in inconsistent order or use long constructor argument lists whose meaning is hard to read.

**How this lesson addresses it:** Let a director describe heading/body steps while text and HTML builders produce different reports. Validate required fields before exposing a completed product.

**When to keep it simpler / limits:** Use a constructor or aggregate for a small value whose fields are already known. A builder adds intermediate mutable state and needs an explicit reset/build contract.

## Learn and try

Builder assembles a product through explicit steps. A director can describe a reusable sequence of steps while a concrete builder decides how those steps affect its representation. Fluent setters alone may be a useful builder API, but the GoF idea is the separation of construction process and representation.

In the example, the director calls a title step and a body step through `ReportBuilder`. The concrete builder accumulates text and returns it by value. `reset` makes reuse explicit and prevents previous output from leaking into the next build. A more complex builder may reject missing required fields in its final `build()` operation.

Use Builder for multi-step construction, meaningful defaults, or multiple representations of the same process. For a small value with two mandatory fields, a constructor or aggregate is simpler. Builders add mutable intermediate state; define reset, validation, and whether repeated builds consume or copy state. Return a value or owning pointer instead of a dangling reference to a temporary builder's internals.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <string>

struct ReportBuilder {
    virtual ~ReportBuilder() = default;
    virtual void reset() = 0;
    virtual void title(const std::string&) = 0;
    virtual void body(const std::string&) = 0;
};
class TextBuilder : public ReportBuilder {
    std::string output_;
public:
    void reset() override { output_.clear(); }
    void title(const std::string& value) override { output_ += value + ": "; }
    void body(const std::string& value) override { output_ += value; }
    std::string result() const { return output_; }
};
void build_status(ReportBuilder& builder) {
    builder.reset();
    builder.title("Status");
    builder.body("ready");
}
int main() {
    TextBuilder builder;
    build_status(builder);
    assert(builder.result() == "Status: ready");
    build_status(builder);
    assert(builder.result() == "Status: ready");
}
```

Try removing the reset in a local experiment and run the director twice. Restore it and explain why lifecycle rules are part of the builder contract.

## Practice setup

Create `design-patterns/practice/lesson_11/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_11/question_1.cpp -o /tmp/llfl-design-patterns/lesson_11_question_1
/tmp/llfl-design-patterns/lesson_11_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Build a value in stages

**Answer file:** `question_1.cpp`

Define `Message { std::string recipient; std::string body; }` and a builder with setters and `build() const` returning a value. Require a nonempty recipient, throwing `std::invalid_argument` otherwise. Assert a valid message and the missing-recipient failure.

### Question 2: Add a reusable process

**Answer file:** `question_2.cpp`

Define `PageBuilder` with reset, heading, and paragraph steps. Implement `TextPageBuilder` so a director using heading `"Hello"` and paragraph `"World"` produces `"Hello
World
"`. Assert the exact result.

### Question 3: Vary representation

**Answer file:** `question_3.cpp`

Implement `HtmlPageBuilder` producing `"<h1>Hello</h1><p>World</p>"` from the same director. Use fixed safe sample text; HTML escaping is outside this exercise. Assert both representations.

### Question 4: Check builder reuse

**Answer file:** `question_4.cpp`

Run the director twice on each builder and assert no duplicated content. Save the first result by value, rebuild, and verify that saved value remains unchanged. Explain why returning references to internal mutable state would complicate callers.

### Question 5: Choose the smaller design

**Answer file:** `question_5.cpp`

Construct a valid `Message` directly as an aggregate and through the builder. Assert equal recipient/body values. Add a comment comparing the builder’s validation and staging benefits with the simpler direct construction for two already-known fields.

## Request review

Compile and run all five answers and send: “Design patterns lesson 11 answers are ready in `design-patterns/practice/lesson_11/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
