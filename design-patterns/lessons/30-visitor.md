# Lesson 30: Visitor

[Previous lesson](29-memento.md) · [Schedule](../SCHEDULE.md) · [Next lesson](31-interpreter.md)

**Goal:** Add operations to a stable family of element types using double dispatch.

**Prerequisite:** Complete lesson 29 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** A relatively stable family of element types needs new cross-cutting operations without adding each operation to every element class.

**Typical symptoms:** Area, export, and reporting behavior accumulate in elements, or each external operation repeats dynamic type checks.

**How this lesson addresses it:** Have each element accept a visitor and dispatch to its concrete-type overload. Add AreaVisitor or PerimeterVisitor while reusing the element traversal and accept methods.

**When to keep it simpler / limits:** Adding an element type requires updating the visitor family, so Visitor favors stable element sets. For closed value alternatives, std::variant and std::visit may be simpler.

## Learn and try

Visitor moves operations into visitor objects while elements expose an accept operation. The first virtual call chooses the concrete element's accept method; that method calls the visitor overload for its concrete type, and virtual dispatch chooses the visitor implementation. This is double dispatch implemented through two calls.

Forward declarations let the visitor interface name element types before their definitions. Each concrete accept calls `visitor.visit(*this)`, where the static type of `*this` selects the correct overload. Adding an operation means adding a visitor; adding an element means extending the visitor interface and every concrete visitor.

Use Visitor when element types are relatively stable and operations change often. Avoid it for a rapidly growing type family or operations that require exposing private internals just for visitors. For a closed set of value types, C++17 `std::variant<A,B>` and `std::visit` can be simpler. A generic lambda `[](const auto& value) { return value.some_common_method(); }` is instantiated for each alternative, so that method must be available on all alternatives.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>

struct Book;
struct Video;
struct Visitor {
    virtual ~Visitor() = default;
    virtual void visit(const Book&) = 0;
    virtual void visit(const Video&) = 0;
};
struct Element {
    virtual ~Element() = default;
    virtual void accept(Visitor&) const = 0;
};
struct Book : Element {
    int pages = 20;
    void accept(Visitor& visitor) const override { visitor.visit(*this); }
};
struct Video : Element {
    int minutes = 5;
    void accept(Visitor& visitor) const override { visitor.visit(*this); }
};
struct TimeEstimate : Visitor {
    int total = 0;
    void visit(const Book& book) override { total += book.pages * 2; }
    void visit(const Video& video) override { total += video.minutes; }
};
int main() {
    Book book;
    Video video;
    TimeEstimate visitor;
    book.accept(visitor);
    video.accept(visitor);
    assert(visitor.total == 45);
}
```

Trace the two dispatch steps for Video. Notice the visitor accumulates state; use a fresh visitor for an independent total.

## Practice setup

Create `design-patterns/practice/lesson_30/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_30/question_1.cpp -o /tmp/llfl-design-patterns/lesson_30_question_1
/tmp/llfl-design-patterns/lesson_30_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Define the element family

**Answer file:** `question_1.cpp`

Define Square with side 3 and Rectangle with width 2 and height 4, both implementing Element::accept. Define Visitor with one overload per element and a virtual destructor. Implement an AreaVisitor and assert total area 17 after visiting both.

### Question 2: Add an operation

**Answer file:** `question_2.cpp`

Add PerimeterVisitor without changing element accept methods. For the same shapes assert total perimeter 24 (12 + 12). Keep area behavior unchanged.

### Question 3: Traverse polymorphic elements

**Answer file:** `question_3.cpp`

Own both shapes in a vector of unique pointers to Element. Traverse with fresh area and perimeter visitors and assert 17 and 24. Explain why no dynamic_cast or type-name switch is needed.

### Question 4: Measure type-extension cost

**Answer file:** `question_4.cpp`

Add a Triangle with base 4, height 3, and side lengths 3, 4, 5; area is base*height/2. Extend the visitor interface and both visitors. For all three shapes assert total area 23 and perimeter 36. Comment on every existing interface that required editing.

### Question 5: Compare a closed variant

**Answer file:** `question_5.cpp`

Define value-only square/rectangle structs with `area() const`, store them in `std::variant<SquareValue, RectangleValue>`, and sum using `std::visit` with a generic lambda. Include `<variant>`. Assert 17 and compare the closed alternative set with a virtual element hierarchy in comments.

## Request review

Compile and run all five answers and send: “Design patterns lesson 30 answers are ready in `design-patterns/practice/lesson_30/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
