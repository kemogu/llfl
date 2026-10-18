# Lesson 34: Capstone review and change request

[Previous lesson](33-capstone-build.md) · [Schedule](../SCHEDULE.md)

**Goal:** Extend the application, verify failure contracts, and simplify with evidence.

**Prerequisite:** Complete lesson 33 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** New business rules and legacy integration must fit an existing application without breaking behavior or hiding partial failures.

**Typical symptoms:** A new discount requires edits throughout checkout, a legacy API leaks into business code, or a retry sends duplicate notifications after a partial success.

**How this lesson addresses it:** Add a threshold pricing Strategy and a legacy notification Adapter. Regression checks verify old pricing, saved records, delivery failures, and duplicate-ID rejection before notification.

**When to keep it simpler / limits:** These changes test the existing boundaries. They do not establish distributed exactly-once delivery; document the limited failure contract and simplify any unnecessary indirection.

## Learn and try

Review the capstone as if you were changing another developer's application. Start from passing behavior checks, introduce one new requirement at a time, and keep persistence and notification semantics explicit. A successful compilation is not sufficient evidence: assertions should inspect returned values, stored records, and messages.

Copy your completed `lesson_33/order_app.hpp` to `lesson_34/order_app.hpp` before editing. Keep the previous lesson as a baseline. Use five new answer programs including this local header, with fresh dependencies in each test. All input bounds and place() ordering from [lesson 33](33-capstone-build.md) remain in force. The new pricing and notification implementations should fit the existing boundaries without adding type switches to Checkout.

### Change requests

Add `ThresholdTwentyPercent`: subtotals below 1000 are unchanged; at or above 1000, payable is `subtotal - subtotal / 5`. Integer division defines rounding. It must satisfy the existing Pricing contract, including subtotal zero.

Integrate the supplied legacy messenger below via a `LegacyNotifierAdapter` that implements your Notifier contract. Map every send to channel 2 and pass the message text unchanged. Borrow the messenger, which must outlive the adapter and Checkout. The legacy API records strings as `"2:" + message`; when `fail` is true, it throws before recording.

Keep notification failure behavior: the order stays saved, the exception propagates, and no automatic retry occurs. A duplicate-ID retry is rejected before notification. A repository test implementation that throws before saving must prevent any notification. This distinction matters: a failure response alone does not tell callers whether persistence succeeded.

After the change, identify one needless wrapper or forwarding method you can remove without losing a useful contract. If your design is already small, compare a helper function with a redundant forwarding class in the answer instead of forcing a production change. Record why the pricing and infrastructure seams remain useful. Do not claim distributed transaction or exactly-once delivery guarantees from this local design.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <string>
#include <vector>
#include <stdexcept>

class LegacyMessenger {
public:
    bool fail = false;
    std::vector<std::string> entries;
    void emit(int channel, const std::string& payload) {
        if (fail) throw std::runtime_error("legacy delivery failed");
        entries.push_back(std::to_string(channel) + ":" + payload);
    }
};
int main() {
    LegacyMessenger messenger;
    messenger.emit(2, "sample");
    assert(messenger.entries.size() == 1);
    assert(messenger.entries[0] == "2:sample");
    messenger.fail = true;
    bool rejected = false;
    try { messenger.emit(2, "second"); }
    catch (const std::runtime_error&) { rejected = true; }
    assert(rejected && messenger.entries.size() == 1);
}
```

Use LegacyMessenger unchanged as the supplied external API. Put it in a separate local header or alongside the adapter so each answer compiles independently. Before coding, predict which layers should change for each request.

## Practice setup

Create `design-patterns/practice/lesson_34/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_34/question_1.cpp -o /tmp/llfl-design-patterns/lesson_34_question_1
/tmp/llfl-design-patterns/lesson_34_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Establish regression checks

**Answer file:** `question_1.cpp`

Copy the capstone header and create checks for NoDiscount and TenPercent checkout using separate repositories: {7,250,3} must return/store/notify 750 and 675 respectively. Also test a missing lookup, a rejected duplicate preserving its record, and invalid quantity 0 producing no record or message. Confirm these pass before making the changes.

### Question 2: Add the pricing requirement

**Answer file:** `question_2.cpp`

Implement ThresholdTwentyPercent without modifying Checkout. Assert payable totals at subtotals 0, 999, 1000, 1001, and 1000000000 are 0, 999, 800, 801, and 800000000. Run an integrated order with price 500 and quantity 2, asserting stored and notified payable 800. Rerun the old pricing checks.

### Question 3: Adapt the supplied API

**Answer file:** `question_3.cpp`

Implement LegacyNotifierAdapter over LegacyMessenger using channel 2. Place {7,250,3} with TenPercent and assert legacy entries contain exactly `"2:Order 7: 675 cents"`. Verify the order record and return value are still correct and Checkout has no legacy-specific code.

### Question 4: Verify failure boundaries

**Answer file:** `question_4.cpp`

With legacy fail=true, place valid ID 9 and assert std::runtime_error, a saved record, and no legacy entry. Set fail=false and retry ID 9; assert duplicate-ID std::invalid_argument and still no entry. Separately use a repository whose save throws std::runtime_error before any write; assert no notification and no stored record. Also check invalid policy output prevents both effects. Use fresh dependencies for independent scenarios.

### Question 5: Simplify and demonstrate

**Answer file:** `question_5.cpp`

Remove one unnecessary indirection or compare a redundant forwarding class with a direct helper as described above. Run shared checks proving equal required outputs. Demonstrate a final workflow using two distinct valid order IDs, the new pricing policy, and the legacy adapter; assert exact records and notification strings. Add a short review comment covering chosen patterns, rejected patterns, ownership, rounding, failure behavior, and the limits of the in-memory design. Rerun all five lesson-34 answers and request review; completing the materials alone does not mean the course is complete.

## Request review

Compile and run all five answers and send: “Design patterns lesson 34 answers are ready in `design-patterns/practice/lesson_34/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
