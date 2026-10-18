# Lesson 21: Strategy

[Previous lesson](20-proxy.md) · [Schedule](../SCHEDULE.md) · [Next lesson](22-template-method.md)

**Goal:** Select interchangeable algorithms through composition.

**Prerequisite:** Complete lesson 20 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** One operation has multiple interchangeable algorithms, and client code is coupled to choosing and executing each variant.

**Typical symptoms:** Checkout contains growing discount branches, or adding a pricing policy requires modifying the checkout algorithm.

**How this lesson addresses it:** Give Checkout a Pricing strategy. NoDiscount, TenPercent, and FixedDiscount implement the same payable contract while the checkout workflow delegates calculation.

**When to keep it simpler / limits:** A free function or callable can represent a small stateless strategy. Strategy solves algorithm variation; it does not model lifecycle transitions merely because its objects hold state.

## Learn and try

Strategy encapsulates an algorithm behind a common contract so a context can delegate to a selected implementation. The context knows when the algorithm is needed; the strategy knows how to perform it. Selection belongs to the client or composition root.

Here a ranking context borrows a score strategy. Either strategy accepts a nonnegative count and returns a score. The context does not branch on concrete types. Strategies with configuration can store it in objects; stateless strategies can often be free functions or callable values.

Use this for genuinely interchangeable policies with a stable contract. If there is only one algorithm, a direct function is simpler. `std::function<int(int)>` can store compatible callable objects, including lambdas such as `[](int n) { return n * 2; }`; it adds type erasure and may allocate. Do not select a class hierarchy automatically. Strategy differs from State: clients choose algorithms, whereas state transitions govern behavior in a state machine.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>

struct Score {
    virtual ~Score() = default;
    virtual int calculate(int count) const = 0;
};
struct NormalScore : Score {
    int calculate(int count) const override { return count; }
};
struct DoubleScore : Score {
    int calculate(int count) const override { return count * 2; }
};
class Ranking {
    const Score& score_;
public:
    explicit Ranking(const Score& score) : score_(score) {}
    int points(int count) const { return score_.calculate(count); }
};
int main() {
    NormalScore normal;
    DoubleScore doubled;
    assert(Ranking(normal).points(4) == 4);
    assert(Ranking(doubled).points(4) == 8);
}
```

Keep the context unchanged while adding a third strategy. Distinguish a strategy’s configurable state from the state-machine intent taught later.

## Practice setup

Create `design-patterns/practice/lesson_21/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_21/question_1.cpp -o /tmp/llfl-design-patterns/lesson_21_question_1
/tmp/llfl-design-patterns/lesson_21_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Define the policy contract

**Answer file:** `question_1.cpp`

Create `Discount::apply(subtotal) const` returning payable cents for nonnegative subtotal. Implement no discount and ten-percent discount using `subtotal - subtotal/10`. Assert 1000 and 900 for subtotal 1000, and both return 0 for 0.

### Question 2: Delegate from a context

**Answer file:** `question_2.cpp`

Create Checkout borrowing a Discount and validating nonnegative subtotal before delegation. Assert both policy results and a negative-input exception. Do not switch on concrete policy types inside Checkout.

### Question 3: Configure an algorithm

**Answer file:** `question_3.cpp`

Add FixedDiscount with nonnegative configured amount; payable is max(0, subtotal-amount). Reject a negative configured amount. For amount 100, assert results 0, 0, and 50 for subtotals 0, 50, and 150.

### Question 4: Compare callable strategies

**Answer file:** `question_4.cpp`

Implement another checkout function accepting `const std::function<int(int)>&` from `<functional>`. Pass no-discount and ten-percent lambdas and assert the same 1000/900 results. Explain value capture versus borrowed reference capture if a lambda uses configuration.

### Question 5: Check interchangeability

**Answer file:** `question_5.cpp`

Write a shared check for each object strategy at subtotals 0, 1, 99, and 1000, asserting payable lies between 0 and subtotal. Verify repeated calls with the same input agree. Compare the class and callable approaches and identify which one you would choose for a stateful policy.

## Request review

Compile and run all five answers and send: “Design patterns lesson 21 answers are ready in `design-patterns/practice/lesson_21/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
