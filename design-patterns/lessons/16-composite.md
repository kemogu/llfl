# Lesson 16: Composite

[Previous lesson](15-bridge.md) · [Schedule](../SCHEDULE.md) · [Next lesson](17-decorator.md)

**Goal:** Treat leaves and object trees through a common operation.

**Prerequisite:** Complete lesson 15 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** Clients must operate on both individual items and nested groups, but repeatedly distinguish leaves from containers.

**Typical symptoms:** Every size or cost calculation includes type checks and its own recursive traversal of nested groups.

**How this lesson addresses it:** Give files and directories a common size operation. A directory aggregates its children, allowing a caller to ask a single file or an entire tree for its size through the same contract.

**When to keep it simpler / limits:** A flat vector and loop are simpler for flat data. Composite does not require child-management operations on leaves, and ownership must prevent unintended cycles.

## Learn and try

Composite represents a part-whole hierarchy using a component interface, leaf objects, and composites that contain other components. A client invokes the same operation on one item or an entire tree.

Here `Item` exposes cost, a leaf supplies a value, and a `Bundle` sums its children. Unique pointers give each child exactly one owner and make the structure a tree. A null child is rejected, preventing later dereferences of missing objects. Ownership transfers through `std::move`; the caller must not use the moved-from pointer as if it still owned the child.

Use Composite for nested structures with meaningful aggregate operations. Do not force leaf objects to implement child-management methods that they cannot support; `add` belongs only on Bundle here. For a flat collection, a vector and a loop are simpler. Shared ownership and parent links introduce cycle and lifetime concerns; this lesson deliberately uses an acyclic ownership tree.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <memory>
#include <vector>
#include <stdexcept>
#include <utility>

struct Item {
    virtual ~Item() = default;
    virtual int cost() const = 0;
};
struct Product : Item {
    int cents;
    explicit Product(int value) : cents(value) {}
    int cost() const override { return cents; }
};
class Bundle : public Item {
    std::vector<std::unique_ptr<Item>> children_;
public:
    void add(std::unique_ptr<Item> child) {
        if (!child) throw std::invalid_argument("null child");
        children_.push_back(std::move(child));
    }
    int cost() const override {
        int total = 0;
        for (const auto& child : children_) total += child->cost();
        return total;
    }
};
int main() {
    Bundle root;
    root.add(std::make_unique<Product>(200));
    auto nested = std::make_unique<Bundle>();
    nested->add(std::make_unique<Product>(300));
    root.add(std::move(nested));
    assert(root.cost() == 500);
}
```

Assert the cost of an empty bundle is zero. Draw the ownership tree and identify where a subtree is destroyed when the root leaves scope.

## Practice setup

Create `design-patterns/practice/lesson_16/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_16/question_1.cpp -o /tmp/llfl-design-patterns/lesson_16_question_1
/tmp/llfl-design-patterns/lesson_16_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Define a leaf

**Answer file:** `question_1.cpp`

Define `Node::size() const` and `File(bytes)` returning a nonnegative size. Reject negative bytes with `std::invalid_argument`. Assert sizes 0 and 12, plus the rejection.

### Question 2: Add a composite

**Answer file:** `question_2.cpp`

Create `Directory` owning unique pointers to Node and summing sizes. Add files of sizes 10 and 20; assert 30. Assert an empty directory has size 0.

### Question 3: Nest composites

**Answer file:** `question_3.cpp`

Build a root with a file of size 5 and a subdirectory with files 10 and 20. Assert 35 through a `const Node&`, without testing runtime types in the summation code.

### Question 4: Reject invalid children

**Answer file:** `question_4.cpp`

Require `Directory::add` to reject a null unique pointer. Check the exception and verify the directory’s size remains unchanged. Transfer a valid subtree with `std::move`; assert the source pointer is null and the directory has the expected total.

### Question 5: Add a uniform operation

**Answer file:** `question_5.cpp`

Add `file_count() const` to the component interface. A file returns 1 and a directory sums children. For question 3’s tree assert count 3 and size 35; for an empty directory assert count 0. Explain why `add` remains a concrete Directory operation rather than a leaf requirement.

## Request review

Compile and run all five answers and send: “Design patterns lesson 16 answers are ready in `design-patterns/practice/lesson_16/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
