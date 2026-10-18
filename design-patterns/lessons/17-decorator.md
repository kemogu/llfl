# Lesson 17: Decorator

[Previous lesson](16-composite.md) · [Schedule](../SCHEDULE.md) · [Next lesson](18-facade.md)

**Goal:** Add behavior by wrapping objects behind the same interface.

**Prerequisite:** Complete lesson 16 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** Independent optional behaviors need to be combined without creating a subclass for every combination.

**Typical symptoms:** Message classes multiply for prefixes, brackets, and every ordering of those features, or one class accumulates many configuration flags.

**How this lesson addresses it:** Wrap a Message in Prefix and Brackets decorators that preserve its interface. Compose wrappers to obtain either info: [hi] or [info: hi], explicitly testing the chosen order.

**When to keep it simpler / limits:** Free transformations are simpler for a fixed sequence. Decorator chains add objects and indirection, and wrappers must still honor the component contract.

## Learn and try

Decorator wraps a component while implementing the same interface. Each wrapper delegates and adds a responsibility before or after delegation. Wrappers can be stacked at runtime without creating a subclass for every combination.

The example's border owns a component with a unique pointer and adds brackets to its rendered text. A second border can wrap the first. Every wrapper preserves the render contract, and the owning chain destroys itself automatically. A null wrapped component is invalid and is rejected at construction.

Use Decorator for independently composable enhancements. The order of wrappers can affect results; test it explicitly. Adapter changes an interface, whereas Decorator preserves it to add behavior. A proxy also shares the interface but primarily controls access. For one fixed transformation, a function call is simpler than an owning wrapper hierarchy. Long chains can make debugging and identity checks harder.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <memory>
#include <string>
#include <stdexcept>
#include <utility>

struct Text {
    virtual ~Text() = default;
    virtual std::string render() const = 0;
};
struct Word : Text {
    std::string render() const override { return "hello"; }
};
class Border : public Text {
    std::unique_ptr<Text> inner_;
public:
    explicit Border(std::unique_ptr<Text> inner) : inner_(std::move(inner)) {
        if (!inner_) throw std::invalid_argument("null component");
    }
    std::string render() const override { return "[" + inner_->render() + "]"; }
};
int main() {
    Border text(std::make_unique<Border>(std::make_unique<Word>()));
    assert(text.render() == "[[hello]]");
}
```

Trace a render call from outer wrapper to leaf and back. Identify where each pair of brackets is added.

## Practice setup

Create `design-patterns/practice/lesson_17/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_17/question_1.cpp -o /tmp/llfl-design-patterns/lesson_17_question_1
/tmp/llfl-design-patterns/lesson_17_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Implement a component

**Answer file:** `question_1.cpp`

Define `Message::render() const` and a concrete message holding a string. Assert inputs `"hi"` and empty text render unchanged.

### Question 2: Wrap with a prefix

**Answer file:** `question_2.cpp`

Implement a Prefix decorator owning a non-null Message and a prefix string. Assert prefix `"info: "` around `"hi"` renders `"info: hi"`. Reject a null component with `std::invalid_argument`.

### Question 3: Add a second decorator

**Answer file:** `question_3.cpp`

Implement Brackets around the same interface. Prefix outside Brackets must produce `"info: [hi]"`; Brackets outside Prefix must produce `"[info: hi]"`. Assert both and comment on order.

### Question 4: Preserve repeated-call behavior

**Answer file:** `question_4.cpp`

Call each chain from question 3 twice and assert identical results on both calls. Implement rendering without modifying the stored text or accumulating prefixes. Check an empty message wrapped in brackets gives `"[]"`.

### Question 5: Compare direct composition

**Answer file:** `question_5.cpp`

Implement free `prefix(text)` and `bracket(text)` functions for the same transformations. Assert both ordering results match the object decorators. Explain when runtime ownership of a configurable chain justifies the extra classes.

## Request review

Compile and run all five answers and send: “Design patterns lesson 17 answers are ready in `design-patterns/practice/lesson_17/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
