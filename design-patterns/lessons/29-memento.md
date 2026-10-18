# Lesson 29: Memento

[Previous lesson](28-mediator.md) · [Schedule](../SCHEDULE.md) · [Next lesson](30-visitor.md)

**Goal:** Capture and restore state without exposing its internal representation to caretakers.

**Prerequisite:** Complete lesson 28 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** State must be saved and restored while keeping its representation private from history-management code.

**Typical symptoms:** Undo code reaches into an editor’s private fields, or snapshots reference live mutable data and change along with the editor.

**How this lesson addresses it:** Let the editor create an opaque Snapshot containing text and cursor state. A caretaker stores snapshots and asks the editor to restore them without interpreting their internals.

**When to keep it simpler / limits:** A plain value copy is sufficient for public state. Full snapshots consume memory and restore only modeled state; they do not undo external I/O.

## Learn and try

Memento separates the originator, which understands its state, from a caretaker, which stores snapshots without interpreting them. The originator creates a memento and later restores from it. Snapshots should not silently share mutable state if callers expect independent history.

The example nests Snapshot inside Editor. Its constructor and data are private; `friend class Editor` grants the originator access. The caretaker can copy and store the snapshot but cannot read its text directly. Values provide independent string storage. This lesson's snapshots are local to this type and intended for the same editor workflow; cross-document restoration needs an additional policy if disallowed.

Use Memento for undo checkpoints or temporary state restoration. Full snapshots may be expensive; command deltas or persistent data structures can be alternatives at larger scale. Saving a memento does not reverse external I/O. A plain copy is sufficient when encapsulation is not a concern and the state is already a public value.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <string>
#include <utility>

class Editor {
    std::string text_;
public:
    class Snapshot {
        std::string text_;
        explicit Snapshot(std::string text) : text_(std::move(text)) {}
        friend class Editor;
    public:
        Snapshot(const Snapshot&) = default;
        Snapshot& operator=(const Snapshot&) = default;
    };
    void set_text(std::string text) { text_ = std::move(text); }
    const std::string& text() const { return text_; }
    Snapshot save() const { return Snapshot(text_); }
    void restore(const Snapshot& snapshot) { text_ = snapshot.text_; }
};
int main() {
    Editor editor;
    editor.set_text("first");
    const auto saved = editor.save();
    editor.set_text("second");
    editor.restore(saved);
    assert(editor.text() == "first");
}
```

Explain why a const reference to the editor’s live string would not be a snapshot. Identify which object could store a history without understanding the text field.

## Practice setup

Create `design-patterns/practice/lesson_29/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_29/question_1.cpp -o /tmp/llfl-design-patterns/lesson_29_question_1
/tmp/llfl-design-patterns/lesson_29_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Snapshot a value

**Answer file:** `question_1.cpp`

Implement an Editor and opaque Snapshot like the example. Save `"A"`, change to `"B"`, restore, and assert `"A"`. Keep snapshot internals inaccessible to the caretaker.

### Question 2: Save all relevant state

**Answer file:** `question_2.cpp`

Add cursor position using `std::size_t`, validated to lie from 0 through text.size(). Include cursor in snapshots. Save text `"abc"` at cursor 2, change both fields, restore, and assert both original values.

### Question 3: Build undo history

**Answer file:** `question_3.cpp`

Keep a vector of snapshots before each edit. Starting at empty text, edit to A then AB. Undo by restoring/popping the last snapshot, asserting A then empty. Empty-history undo returns false.

### Question 4: Verify independence

**Answer file:** `question_4.cpp`

Save snapshots for A and B, then change live text to C. Restore A and B in turn and assert their original values. Restoring one snapshot must not mutate the other snapshot.

### Question 5: Define invalid restoration boundaries

**Answer file:** `question_5.cpp`

Keep snapshots opaque and create them only from valid editor states. Check setting a cursor beyond text length throws `std::out_of_range` without modifying state. Restore a prior valid snapshot successfully afterward. Explain memory cost and why external file writes would not be undone by restoring this in-memory object.

## Request review

Compile and run all five answers and send: “Design patterns lesson 29 answers are ready in `design-patterns/practice/lesson_29/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
