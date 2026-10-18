# Lesson 04: Open/Closed Principle (OCP)

[Previous lesson](03-single-responsibility.md) · [Schedule](../SCHEDULE.md) · [Next lesson](05-liskov-substitution.md)

**Goal:** Create an extension point for a demonstrated variation.

**Prerequisite:** Complete lesson 03 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** Adding another implementation of a recurring behavior repeatedly requires editing stable client logic.

**Typical symptoms:** Every new shipping option adds another branch to checkout and risks breaking existing options.

**How this lesson addresses it:** Define a shipping-policy extension point. Add a threshold shipping policy as another implementation while checkout continues to invoke the same fee contract.

**When to keep it simpler / limits:** OCP applies to a chosen kind of variation. A small conditional is often clearer for fixed choices; a changed contract may still require editing clients.

## Learn and try

OCP encourages modules that can accept an extension without requiring changes to stable client logic. “Closed” applies to a chosen kind of change. No useful program is closed to every future requirement, and editing code is not a design failure.

Here the client asks a shipping policy for a fee. Adding another policy does not require another conditional inside `checkout`. The abstract interface defines the extension boundary; concrete policies supply varying behavior. Policies accept a nonnegative subtotal and return a nonnegative fee. The client enforces its input boundary before delegation.

Use this when several policies already exist or a clear requirement calls for adding them. For two fixed cases unlikely to grow, a conditional can be clearer. More interfaces mean more concepts to maintain. Adding validation or changing the contract can still require edits across implementations; an abstraction is not a shield against incompatible requirements.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <stdexcept>

struct Shipping {
    virtual ~Shipping() = default;
    virtual int fee(int subtotal) const = 0;
};
struct FlatShipping : Shipping {
    int fee(int) const override { return 5; }
};
struct FreeShipping : Shipping {
    int fee(int) const override { return 0; }
};
int checkout(int subtotal, const Shipping& shipping) {
    if (subtotal < 0) throw std::invalid_argument("negative subtotal");
    return subtotal + shipping.fee(subtotal);
}
int main() {
    FlatShipping flat;
    FreeShipping free;
    assert(checkout(20, flat) == 25);
    assert(checkout(20, free) == 20);
}
```

Add a threshold-based shipping policy without changing `checkout`. Identify the requirement that would force the interface itself to change.

## Practice setup

Create `design-patterns/practice/lesson_04/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_04/question_1.cpp -o /tmp/llfl-design-patterns/lesson_04_question_1
/tmp/llfl-design-patterns/lesson_04_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Establish the variation

**Answer file:** `question_1.cpp`

Write `shipping_total(subtotal, express)` with a fee of 100 cents normally and 300 cents for express. For subtotal 500, assert totals 600 and 800. Assume nonnegative inputs and comment on what happens when a third mode is added.

### Question 2: Extract the boundary

**Answer file:** `question_2.cpp`

Create a `FeePolicy` interface and normal/express implementations with the same fees. Write a client accepting `const FeePolicy&`. Preserve both outputs from question 1 without switching on a mode inside the client.

### Question 3: Add an extension

**Answer file:** `question_3.cpp`

Add a policy charging 100 cents below subtotal 1000 and zero at or above 1000. Keep the client from question 2 unchanged. Assert totals for subtotals 999, 1000, and 1001 are 1099, 1000, and 1001.

### Question 4: Check the contract

**Answer file:** `question_4.cpp`

Write a helper that calls each policy with subtotals 0, 999, and 1000 and asserts fees are nonnegative. Add client validation rejecting a negative subtotal with `std::invalid_argument`; check the exception and the earlier valid totals.

### Question 5: Compare with a function

**Answer file:** `question_5.cpp`

Implement the threshold policy as a free function and a client accepting `int (*fee)(int)`, a pointer to a function taking and returning `int`. Call it through `fee(subtotal)`. Assert the same three threshold results. Explain which extension mechanism you would choose for a policy with no state.

## Request review

Compile and run all five answers and send: “Design patterns lesson 4 answers are ready in `design-patterns/practice/lesson_04/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
