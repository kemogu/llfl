# Lesson 23: Observer

[Previous lesson](22-template-method.md) · [Schedule](../SCHEDULE.md) · [Next lesson](24-command.md)

**Goal:** Notify multiple subscribers while defining subscription lifetime and delivery rules.

**Prerequisite:** Complete lesson 22 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** One event or state change must trigger multiple independent reactions without the publisher naming each concrete recipient.

**Typical symptoms:** A subject directly calls every display, logger, and listener, and adding a reaction requires editing the subject.

**How this lesson addresses it:** Let observers subscribe to a subject and receive published events. A new reaction is registered separately, while subscription IDs allow explicit removal.

**When to keep it simpler / limits:** A direct call is simpler for one fixed recipient. Observer requires delivery-order, mutation, exception, and subscription-lifetime contracts; it does not automatically provide durable messaging.

## Learn and try

Observer creates a one-to-many notification relationship: a subject publishes changes, and observers react without the subject naming their concrete types. In C++, callbacks stored as `std::function` are one practical representation of observers.

This example returns a subscription ID and lets clients unsubscribe explicitly. Publishing copies the subscriber map first. Our contract is snapshot delivery: subscribers present at the start get this event in ID order, even if removed during a callback; subscribers added during delivery start with the next event. Copying callbacks costs time and memory but gives clear mutation rules. Exceptions propagate and stop remaining delivery for this example.

A lambda like `[&total](int n) { total += n; }` borrows total; its lifetime must cover every possible callback, including the current snapshot. Unsubscribing does not destroy callbacks already copied into that snapshot. Use Observer for independent reactions to events. For one known recipient, a direct call is simpler. Production designs often add scoped subscription handles or weak ownership, but a callback registry alone does not solve lifetime or thread safety.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <functional>
#include <map>
#include <cstddef>
#include <utility>

class Subject {
    std::map<std::size_t, std::function<void(int)>> observers_;
    std::size_t next_id_ = 1;
public:
    std::size_t subscribe(std::function<void(int)> observer) {
        const auto id = next_id_++;
        observers_.emplace(id, std::move(observer));
        return id;
    }
    void unsubscribe(std::size_t id) { observers_.erase(id); }
    void publish(int value) {
        const auto snapshot = observers_;
        for (const auto& entry : snapshot) entry.second(value);
    }
};
int main() {
    int total = 0;
    Subject subject;
    const auto id = subject.subscribe([&total](int value) { total += value; });
    subject.publish(3);
    subject.unsubscribe(id);
    subject.publish(4);
    assert(total == 3);
}
```

Trace the lifetime of the captured variable. Explain why explicit unsubscription after the captured object has already died would be too late.

## Practice setup

Create `design-patterns/practice/lesson_23/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_23/question_1.cpp -o /tmp/llfl-design-patterns/lesson_23_question_1
/tmp/llfl-design-patterns/lesson_23_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Notify two observers

**Answer file:** `question_1.cpp`

Implement a subject using the snapshot contract above. Register two callbacks recording strings `"A:7"` and `"B:7"` for event 7. Publish once and assert those entries in subscription order.

### Question 2: Unsubscribe explicitly

**Answer file:** `question_2.cpp`

Remove A’s subscription, publish event 8, and assert only `"B:8"` is appended. Removing the same ID again or an unknown ID is a no-op; test both.

### Question 3: Define additions during delivery

**Answer file:** `question_3.cpp`

Have A register C during its first callback, only once. Publish 1 then 2. Assert the first event reaches only A and B; the second reaches A, B, and C in order. Use callbacks that capture recording data with adequate lifetime.

### Question 4: Define removals during delivery

**Answer file:** `question_4.cpp`

Have A unsubscribe B during delivery. Assert B still receives the current event because it is in the snapshot, but not the next event. Keep B’s captured state alive until the current publish returns. Explain the distinction between removing registration and canceling an in-flight callback.

### Question 5: Check exception policy

**Answer file:** `question_5.cpp`

Register A that records, B that throws `std::runtime_error`, and C that records. Assert publishing propagates the error and C is not called. Explicitly unsubscribe all callbacks before their captured state leaves scope. Comment on when a direct notification call would be clearer.

## Request review

Compile and run all five answers and send: “Design patterns lesson 23 answers are ready in `design-patterns/practice/lesson_23/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
