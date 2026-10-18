# Lesson 09: Factory Method

[Previous lesson](08-solid-refactoring.md) · [Schedule](../SCHEDULE.md) · [Next lesson](10-abstract-factory.md)

**Goal:** Let subclasses vary product creation while reusing a creator workflow.

**Prerequisite:** Complete lesson 08 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** A reusable workflow needs to create a product, but different subclasses need different concrete products.

**Typical symptoms:** The workflow contains concrete constructors or is duplicated merely to change the object it creates.

**How this lesson addresses it:** Keep dispatch in a Logistics creator and delegate transport creation to an overridable factory method. RoadLogistics creates a truck; SeaLogistics creates a ship; both reuse dispatch.

**When to keep it simpler / limits:** Use a free factory function or injected object when there is no inherited creator workflow. Factory Method does not require a string-based switch.

## Learn and try

GoF Factory Method defines an overridable creation operation in a creator base class. The creator's existing workflow uses the abstract product; a concrete creator overrides the factory method to choose the product. These are two separate hierarchies: creators and products.

Below `Preview::render` is the workflow, `make_document` is the factory method, and `Document` is the product interface. The returned `std::unique_ptr` transfers exclusive ownership to the workflow and destroys the product when it leaves scope. The factory contract returns a non-null product.

Use this when subclasses already customize a workflow and creation is one of their variation points. A free function with a switch that returns products is a simple factory, not this GoF structure. If there is no creator workflow to inherit, an injected product or free factory function can be simpler. Avoid adding a creator hierarchy solely to hide a trivial constructor.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <memory>
#include <string>

struct Document {
    virtual ~Document() = default;
    virtual std::string text() const = 0;
};
struct PlainDocument : Document {
    std::string text() const override { return "plain"; }
};
class Preview {
protected:
    virtual std::unique_ptr<Document> make_document() const = 0;
public:
    virtual ~Preview() = default;
    std::string render() const {
        auto document = make_document();
        return "Preview: " + document->text();
    }
};
struct PlainPreview : Preview {
    std::unique_ptr<Document> make_document() const override {
        return std::make_unique<PlainDocument>();
    }
};
int main() {
    PlainPreview preview;
    assert(preview.render() == "Preview: plain");
}
```

Identify both hierarchies and the call from a nonvirtual workflow into the virtual creation method. Explain where the product is destroyed.

## Practice setup

Create `design-patterns/practice/lesson_09/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_09/question_1.cpp -o /tmp/llfl-design-patterns/lesson_09_question_1
/tmp/llfl-design-patterns/lesson_09_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Define the product

**Answer file:** `question_1.cpp`

Create `Transport::deliver() const` returning text and concrete `Truck`/`Ship` products returning `"road"`/`"sea"`. Own each through `std::unique_ptr<Transport>` and assert both results.

### Question 2: Build a creator workflow

**Answer file:** `question_2.cpp`

Write abstract `Logistics` with a virtual factory method returning a non-null transport and a nonvirtual `dispatch()` returning `"sent by " + deliver()`. Implement `RoadLogistics`; assert `"sent by road"`.

### Question 3: Extend creation

**Answer file:** `question_3.cpp`

Add `SeaLogistics` without changing the base workflow. Call both through `const Logistics&` and assert road/sea messages. Comment why this is Factory Method rather than a string-based switch.

### Question 4: Verify product lifetimes

**Answer file:** `question_4.cpp`

Add a `TrackedTransport` borrowing an integer live-count, incrementing on construction and decrementing on destruction. Its creator borrows the same counter. Call dispatch twice and assert the counter returns to zero after each call. Disable copying of the tracked product or avoid copying it. Ensure the counter outlives creator and products.

### Question 5: Compare a simple factory

**Answer file:** `question_5.cpp`

Write a free `make_transport(bool use_sea)` returning a unique pointer and a free dispatch function using it. Check parity with both creator variants. Explain when the free function is sufficient and what reusable workflow would justify the creator hierarchy.

## Request review

Compile and run all five answers and send: “Design patterns lesson 9 answers are ready in `design-patterns/practice/lesson_09/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
