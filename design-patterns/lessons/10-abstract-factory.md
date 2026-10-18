# Lesson 10: Abstract Factory

[Previous lesson](09-factory-method.md) · [Schedule](../SCHEDULE.md) · [Next lesson](11-builder.md)

**Goal:** Create compatible families of related products through one factory contract.

**Prerequisite:** Complete lesson 09 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** A client must create several related products that belong to a compatible family without hard-coding that family.

**Typical symptoms:** Theme selection is repeated for buttons and checkboxes, allowing a screen to accidentally mix light and dark products.

**How this lesson addresses it:** Choose one Theme factory and obtain all related controls through it. A different concrete factory changes the product family while the screen-building client stays the same.

**When to keep it simpler / limits:** Independent products need not share a factory. Adding a new product kind requires changes to the factory interface and every concrete family.

## Learn and try

Abstract Factory groups creation operations for related product interfaces. A concrete factory supplies one consistent family, such as light-theme buttons and checkboxes. The client receives the factory rather than independently choosing concrete classes for each product.

The example's `Theme` creates both products; `LightTheme` selects their compatible implementations. The factory returns independent owning pointers and does not need to outlive those products. Products expose only the behavior their client needs. A factory with multiple creation methods differs from Factory Method's subclass hook in a creator workflow, though the patterns can be combined.

Use this when products must vary together. Adding a new family is straightforward; adding a new product kind requires changing the factory interface and every concrete factory. For one family or products with no compatibility constraint, direct construction or separate factory functions are simpler. Compatibility here is a design convention reinforced by tests, not automatically enforced by the base types.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <memory>
#include <string>

struct Button {
    virtual ~Button() = default;
    virtual std::string draw() const = 0;
};
struct Checkbox {
    virtual ~Checkbox() = default;
    virtual std::string draw() const = 0;
};
struct LightButton : Button {
    std::string draw() const override { return "light button"; }
};
struct LightCheckbox : Checkbox {
    std::string draw() const override { return "light checkbox"; }
};
struct Theme {
    virtual ~Theme() = default;
    virtual std::unique_ptr<Button> button() const = 0;
    virtual std::unique_ptr<Checkbox> checkbox() const = 0;
};
struct LightTheme : Theme {
    std::unique_ptr<Button> button() const override {
        return std::make_unique<LightButton>();
    }
    std::unique_ptr<Checkbox> checkbox() const override {
        return std::make_unique<LightCheckbox>();
    }
};
std::string screen(const Theme& theme) {
    return theme.button()->draw() + " / " + theme.checkbox()->draw();
}
int main() {
    LightTheme theme;
    assert(screen(theme) == "light button / light checkbox");
}
```

Sketch the second family before coding. Both product types should come from the same factory selected at the composition root.

## Practice setup

Create `design-patterns/practice/lesson_10/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_10/question_1.cpp -o /tmp/llfl-design-patterns/lesson_10_question_1
/tmp/llfl-design-patterns/lesson_10_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Define related products

**Answer file:** `question_1.cpp`

Define `Heading` and `Body` interfaces returning strings. Implement plain variants returning `"Title"` and `"Text"`. Assert both through base references.

### Question 2: Create one family

**Answer file:** `question_2.cpp`

Define `DocumentFactory` creating both products with unique pointers. Implement `PlainFactory` and a client returning heading + `"|"` + body. Assert `"Title|Text"`.

### Question 3: Add another family

**Answer file:** `question_3.cpp`

Implement HTML variants returning `"<h1>Title</h1>"` and `"<p>Text</p>"` with `HtmlFactory`. Reuse the same client and assert `"<h1>Title</h1>|<p>Text</p>"`.

### Question 4: Test family consistency

**Answer file:** `question_4.cpp`

Give both product interfaces a `family() const` string method. For each factory, create both products and assert their family strings match (`"plain"` or `"html"`). Construct a deliberately mixed pair and assert its family strings differ without treating that as a valid factory output.

### Question 5: Evaluate extension cost

**Answer file:** `question_5.cpp`

Add a third family, Markdown, returning `"# Title"` and `"Text"`. Assert `"# Title|Text"` through the unchanged client. Comment which interfaces would need edits if every family also had to create a Footer, and when direct construction would be simpler.

## Request review

Compile and run all five answers and send: “Design patterns lesson 10 answers are ready in `design-patterns/practice/lesson_10/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
