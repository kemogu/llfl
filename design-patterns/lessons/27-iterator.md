# Lesson 27: Iterator

[Previous lesson](26-chain-of-responsibility.md) · [Schedule](../SCHEDULE.md) · [Next lesson](28-mediator.md)

**Goal:** Traverse a collection without exposing its internal representation.

**Prerequisite:** Complete lesson 26 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** Clients need to traverse an aggregate without depending on its storage representation or sharing one traversal position.

**Typical symptoms:** The collection exposes internal storage just to permit walking it, or a single current-index field prevents two independent traversals.

**How this lesson addresses it:** Keep position in a separate iterator or cursor. Two cursors can walk one collection independently, and a filtered cursor can expose a traversal order without copying the collection.

**When to keep it simpler / limits:** Prefer standard-library iterators and range-for for ordinary containers. Custom traversal still needs lifetime and mutation rules; Iterator does not prevent invalidation.

## Learn and try

Iterator separates traversal state from an aggregate. Multiple iterators can walk the same collection independently. GoF describes that responsibility; the C++ standard library additionally specifies iterator categories and operations that algorithms rely on.

This example is a small cursor, not a claim to implement a standard-library iterator category. It borrows a vector and tracks an index, returning copied values in an optional. At end it repeatedly returns no value. The vector must outlive the cursor and must not be mutated during traversal under this lesson's contract.

For ordinary C++ collections, prefer `begin`/`end`, range-for, and standard algorithms instead of inventing traversal interfaces. End iterators are sentinels and must not be dereferenced. Mutation can invalidate iterators according to the container and operation; for example, vector reallocation invalidates its element iterators and references. A custom traversal is useful for hiding a representation or implementing a meaningful traversal order, not just wrapping a for loop without benefit.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <vector>
#include <optional>
#include <cstddef>
#include <numeric>

class Cursor {
    const std::vector<int>& values_;
    std::size_t index_ = 0;
public:
    explicit Cursor(const std::vector<int>& values) : values_(values) {}
    std::optional<int> next() {
        if (index_ == values_.size()) return std::nullopt;
        return values_[index_++];
    }
};
int main() {
    const std::vector<int> values{2, 4};
    Cursor cursor(values);
    assert(cursor.next().value() == 2);
    assert(cursor.next().value() == 4);
    assert(!cursor.next());
    assert(std::accumulate(values.begin(), values.end(), 0) == 6);
}
```

Create a second cursor after consuming the first value from the first cursor. Its first value should still be 2. Compare the cursor with range-for for this simple collection.

## Practice setup

Create `design-patterns/practice/lesson_27/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_27/question_1.cpp -o /tmp/llfl-design-patterns/lesson_27_question_1
/tmp/llfl-design-patterns/lesson_27_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Use standard traversal

**Answer file:** `question_1.cpp`

For a vector {3,1,4}, compute the sum with range-for and with `std::accumulate`; assert both are 8. Repeat for an empty vector and assert 0 without dereferencing its end iterator.

### Question 2: Implement a cursor

**Answer file:** `question_2.cpp`

Create a cursor over a borrowed const vector returning `std::optional<int>`. Traverse {3,1,4}, asserting the exact sequence followed by no value twice. Check an empty vector returns no value immediately.

### Question 3: Keep traversals independent

**Answer file:** `question_3.cpp`

Create two cursors over one vector. Advance the first twice, then the second once. Assert values 3 and 1 from the first and 3 from the second. Explain why traversal position belongs to each cursor.

### Question 4: Add a filtered traversal

**Answer file:** `question_4.cpp`

Write an EvenCursor using the same borrowing contract and skipping odd values. For {1,2,3,4}, assert outputs 2 and 4 then end; for {1,3}, assert immediate end. Do not build a second filtered vector.

### Question 5: Respect invalidation

**Answer file:** `question_5.cpp`

Traverse a vector and finish the traversal. Then append another value and obtain fresh standard iterators for a second pass. Assert the new sum includes the appended value. Do not dereference any old iterator after mutation. Explain why a custom cursor also needs a documented mutation/lifetime contract.

## Request review

Compile and run all five answers and send: “Design patterns lesson 27 answers are ready in `design-patterns/practice/lesson_27/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
