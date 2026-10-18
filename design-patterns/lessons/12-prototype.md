# Lesson 12: Prototype

[Previous lesson](11-builder.md) · [Schedule](../SCHEDULE.md) · [Next lesson](13-singleton.md)

**Goal:** Copy configured polymorphic objects while defining independent ownership.

**Prerequisite:** Complete lesson 11 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** A client needs an independent copy of a configured object but knows only its base interface or cannot conveniently reconstruct its configuration.

**Typical symptoms:** Copying by base value slices derived state; type switches recreate each subtype; sharing a pointer makes edits affect the original object.

**How this lesson addresses it:** Add a virtual clone() that returns an owning pointer to a new object of the same concrete type. Clone a configured playlist or shape, then modify the copy while preserving the original.

**When to keep it simpler / limits:** Ordinary value copying is simpler for known concrete types. Prototype must define deep-copy versus intentional sharing; it does not automatically make copying cheaper or safe.

## Learn and try

Prototype creates an object by cloning an existing configured instance. A virtual `clone()` preserves the dynamic type when callers know only a base interface. The result is a new owning pointer, not another owner of the original object.

The example stores strings in a vector by value, so copying the object copies its configuration independently. A class with `unique_ptr` members cannot use an implicit copy constructor; its clone must explicitly copy owned state. Shared immutable resources can be shared intentionally, but mutable state should not accidentally alias when the contract promises an independent clone.

Use Prototype when configured examples are easier to copy than reconstruct or when runtime types are unknown to the caller. For simple concrete values, ordinary copying is enough. Cloning adds a contract for identity, ownership, and copy depth. In C++, returning `std::unique_ptr<Derived>` does not override a virtual returning `std::unique_ptr<Base>`; the override uses the base pointer type and converts its constructed result.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <memory>
#include <string>
#include <vector>

struct Prototype {
    virtual ~Prototype() = default;
    virtual std::unique_ptr<Prototype> clone() const = 0;
    virtual void add(const std::string&) = 0;
    virtual std::size_t size() const = 0;
};
class Playlist : public Prototype {
    std::vector<std::string> tracks_;
public:
    std::unique_ptr<Prototype> clone() const override {
        return std::make_unique<Playlist>(*this);
    }
    void add(const std::string& track) override { tracks_.push_back(track); }
    std::size_t size() const override { return tracks_.size(); }
};
int main() {
    Playlist original;
    original.add("intro");
    auto copy = original.clone();
    copy->add("outro");
    assert(original.size() == 1);
    assert(copy->size() == 2);
}
```

Identify which members are copied by value. Explain why assigning a raw pointer to the original would not create a prototype clone.

## Practice setup

Create `design-patterns/practice/lesson_12/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_12/question_1.cpp -o /tmp/llfl-design-patterns/lesson_12_question_1
/tmp/llfl-design-patterns/lesson_12_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Copy a configured value

**Answer file:** `question_1.cpp`

Define a concrete `Style` with a color string and a vector of integer margins. Copy a style with color `"blue"` and margins {1,2}. Change the copy’s color and first margin; assert the original remains blue with first margin 1.

### Question 2: Clone polymorphically

**Answer file:** `question_2.cpp`

Define `Shape` with virtual clone and area. Implement `Square(side)`, then clone a side-3 square through `const Shape&`. Assert the clone has area 9 and a different address from the original.

### Question 3: Preserve dynamic behavior

**Answer file:** `question_3.cpp`

Add `Rectangle(2,4)` and a vector of owning shape pointers. Clone each via the base interface into another vector. Assert areas 9 and 8 in order and distinct addresses for corresponding objects.

### Question 4: Deep-copy owned state

**Answer file:** `question_4.cpp`

Create `Settings` owning `std::unique_ptr<int>` initialized to 5. Implement `clone()` that allocates a fresh integer containing the old value. Set the clone to 9; assert original 5, clone 9, and different integer addresses. Do not introduce shared ownership to bypass the copy requirement.

### Question 5: Use configured prototypes

**Answer file:** `question_5.cpp`

Store two named shape prototypes in `std::map<std::string, std::unique_ptr<Shape>>`. Implement a lookup that clones an existing prototype and throws `std::out_of_range` for an unknown name. Assert two requests return distinct objects with the expected area and check the missing-name failure. Explain when a direct value copy would suffice.

## Request review

Compile and run all five answers and send: “Design patterns lesson 12 answers are ready in `design-patterns/practice/lesson_12/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
