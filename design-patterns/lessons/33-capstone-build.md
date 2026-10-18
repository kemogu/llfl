# Lesson 33: Capstone build

[Previous lesson](32-pattern-selection.md) · [Schedule](../SCHEDULE.md) · [Next lesson](34-capstone-review.md)

**Goal:** Integrate a small order application with explicit boundaries and behavioral checks.

**Prerequisite:** Complete lesson 32 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** An application must coordinate domain validation, replaceable pricing, persistence, and notification without coupling every part to every other part.

**Typical symptoms:** Invalid orders can trigger side effects, pricing branches grow inside checkout, and tests require real infrastructure to observe behavior.

**How this lesson addresses it:** Build a Checkout workflow with a Pricing Strategy and small injected Repository and Notifier contracts. Validate and calculate first, then save and notify according to explicit failure rules.

**When to keep it simpler / limits:** The capstone combines selected designs rather than all patterns. Its in-memory workflow is not a transaction: notification failure occurs after saving and does not roll back the record.

## Learn and try

Build a deterministic, in-memory order-processing application. Use SOLID to decide boundaries and use patterns only where they solve a requirement. Pricing is a Strategy; a repository and notifier are policy-owned contracts. You do not need a Singleton, global registry, or a class for every domain field.

### Required application contract

An `Order` contains `int id`, `int unit_price_cents`, and `int quantity`. Valid IDs are positive; prices are from 0 through 1,000,000 inclusive; quantities are from 1 through 1,000 inclusive. Reject other values with `std::invalid_argument`. These bounds keep the product at most 1,000,000,000, safely representable on the course platform with a 32-bit-or-wider int. Add `static_assert` using `std::numeric_limits<int>::max()` from `<limits>` to make that platform assumption explicit. Unlike the early receipt exercises, a zero quantity is invalid for a submitted order.

`subtotal(const Order&)` validates first and returns price times quantity. `Pricing::payable(int subtotal) const` accepts a valid nonnegative subtotal and returns a value from 0 through subtotal. Provide NoDiscount and TenPercent (`subtotal - subtotal / 10`, using integer division). The checkout service rejects an out-of-contract result with `std::logic_error` before saving anything.

An `OrderRecord` contains ID, subtotal cents, and payable cents. `Repository::save(const OrderRecord&)` inserts a new record or throws `std::invalid_argument` for a duplicate ID. `Repository::find(int) const` returns `std::optional<OrderRecord>` by value and no value for a missing ID. The in-memory implementation owns its map of records; reads do not insert missing entries.

`Notifier::send(const std::string&)` sends one message. A recording notifier stores messages in a vector. The exact successful message is `"Order 7: 675 cents"` for ID 7 and payable 675. Formatting belongs in a helper function.

`Checkout::place(const Order&)` borrows Pricing, Repository, and Notifier; it returns the payable total. It validates, calculates, checks policy output, saves once, then notifies once, in that order. Validation, policy, or repository failure prevents notification. Notification failure propagates **after the record has been saved**; there is no rollback or automatic retry. A retry with the same ID is rejected as a duplicate before sending again. This is a deliberately limited local workflow, not a transactional messaging system.

### Organize the application

Put reusable definitions in `design-patterns/practice/lesson_33/order_app.hpp`, include `#pragma once`, and include it with `#include "order_app.hpp"` from each answer. Define free functions as `inline` and class methods inside their class definitions so the header is safe to reuse. No separate `.cpp` library or external build tool is required. Keep five independent answer programs, each with its own main and fresh test objects. Incrementally add definitions to the header as you work; rerun earlier answers after changes.

The worked example shows a bounded-input check in a separate parcel domain. Check bounds before arithmetic. A constructor or function should reject invalid input without leaving partial state. This does not solve the order application; apply the same reasoning to its stated contracts.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <limits>
#include <stdexcept>

int parcel_weight(int item_grams, int count) {
    static_assert(std::numeric_limits<int>::max() >= 1000000,
                  "int range is too small");
    if (item_grams < 0 || item_grams > 10000 || count < 1 || count > 100) {
        throw std::invalid_argument("invalid parcel");
    }
    return item_grams * count;
}
int main() {
    assert(parcel_weight(250, 3) == 750);
    assert(parcel_weight(10000, 100) == 1000000);
    bool rejected = false;
    try { parcel_weight(250, 0); }
    catch (const std::invalid_argument&) { rejected = true; }
    assert(rejected);
}
```

Before building interfaces, write down the success and failure sequence for place(). Identify the point after which a notification failure cannot imply that no order was saved.

## Practice setup

Create `design-patterns/practice/lesson_33/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_33/question_1.cpp -o /tmp/llfl-design-patterns/lesson_33_question_1
/tmp/llfl-design-patterns/lesson_33_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Implement the domain and validation

**Answer file:** `question_1.cpp`

Create Order and subtotal in order_app.hpp with the exact bounds above. Assert order {7,250,3} totals 750, {1,0,1} totals 0, and {1,1000000,1000} totals 1000000000. Independently reject ID 0 and -1, price -1 and 1000001, and quantity 0 and 1001. Check each throws the specified exception.

### Question 2: Implement pricing policies

**Answer file:** `question_2.cpp`

Add Pricing, NoDiscount, and TenPercent. Assert results 750 and 675 for subtotal 750. Assert ten percent produces 90 for subtotal 99 and 0 for 0. Run shared range checks at 0, 1, 99, 750, and 1000000000. Keep policies free of storage and notification responsibilities.

### Question 3: Implement storage

**Answer file:** `question_3.cpp`

Add OrderRecord, Repository, and InMemoryRepository. Save {7,750,675}, retrieve it, and assert all fields. Assert a missing ID returns no value. Attempt to save the same ID with different totals, check std::invalid_argument, and verify the original record is unchanged. Test that a second distinct ID can be stored.

### Question 4: Implement notification and formatting

**Answer file:** `question_4.cpp`

Add Notifier, RecordingNotifier, and `format_confirmation(id, payable)`. Assert the exact message `"Order 7: 675 cents"` and a zero-payable message `"Order 8: 0 cents"`. Send both and assert exactly those messages in order. Implement a separate ThrowingNotifier that always throws std::runtime_error for later failure tests.

### Question 5: Integrate checkout

**Answer file:** `question_5.cpp`

Add Checkout with the stated order of operations and borrowed dependencies. Place {7,250,3} with TenPercent and assert returned 675, stored {7,750,675}, and one exact notification. Assert invalid order input and a policy returning subtotal+1 create no record or notification. Repeat ID 7 and assert duplicate rejection with no extra notification. With fresh objects and ThrowingNotifier, place valid ID 9, assert the error propagates and the record remains saved. Document dependency lifetimes and why you chose each abstraction.

## Request review

Compile and run all five answers and send: “Design patterns lesson 33 answers are ready in `design-patterns/practice/lesson_33/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
