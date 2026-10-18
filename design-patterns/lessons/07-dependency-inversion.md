# Lesson 07: Dependency Inversion Principle (DIP)

[Previous lesson](06-interface-segregation.md) · [Schedule](../SCHEDULE.md) · [Next lesson](08-solid-refactoring.md)

**Goal:** Keep application policy dependent on a contract rather than infrastructure details.

**Prerequisite:** Complete lesson 06 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** Application policy is tied to infrastructure construction and APIs, making replacements and isolated tests difficult.

**Typical symptoms:** An order service constructs its concrete notifier internally, so testing confirmation requires using that notifier and replacing delivery changes the service.

**How this lesson addresses it:** Have the service depend on a small Notifier contract. Construct a recording or production implementation in main and inject it into the service.

**When to keep it simpler / limits:** DIP is the dependency-direction principle; injection is a supporting technique. Injecting a concrete vendor type alone does not remove that coupling.

## Learn and try

DIP says high-level policy and low-level mechanisms should depend on abstractions, with the abstraction expressing what policy needs. A reporting service should not choose a concrete console, database, or network library inside its business operation.

Here `AlertService` depends on the `Sink` contract; `MemorySink` implements it. Construction happens in `main`, the composition root where concrete objects are selected and wired together. Constructor injection supplies the dependency. Injection alone is not DIP: injecting a concrete database type can still bind policy to that database's details.

The service borrows its sink; construction order and scope guarantee the sink remains alive. A test implementation records messages, making behavior observable without external I/O. Use this boundary for replaceable infrastructure or isolated policy tests. For a tiny stable calculation, an interface may add no benefit; a function parameter or concrete value can be simpler. Keep the abstraction focused on the client rather than mirroring every method of a vendor API.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <string>
#include <vector>

struct Sink {
    virtual ~Sink() = default;
    virtual void send(const std::string& message) = 0;
};
struct MemorySink : Sink {
    std::vector<std::string> messages;
    void send(const std::string& message) override {
        messages.push_back(message);
    }
};
class AlertService {
    Sink& sink_;
public:
    explicit AlertService(Sink& sink) : sink_(sink) {}
    void warn(int level) {
        if (level >= 3) sink_.send("high");
    }
};
int main() {
    MemorySink sink;
    AlertService service(sink);
    service.warn(1);
    service.warn(3);
    assert(sink.messages.size() == 1);
    assert(sink.messages[0] == "high");
}
```

Trace the dependency from policy to interface and from concrete implementation to interface. Identify `main` as the only place that needs the concrete sink type.

## Practice setup

Create `design-patterns/practice/lesson_07/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_07/question_1.cpp -o /tmp/llfl-design-patterns/lesson_07_question_1
/tmp/llfl-design-patterns/lesson_07_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Define a policy-owned boundary

**Answer file:** `question_1.cpp`

Define `Notifier::send(const std::string&)` and a recording notifier. Implement `OrderService` borrowing a notifier and `confirm(int id)` sending `"Order 7 confirmed"` for id 7. Assert exactly one matching message.

### Question 2: Swap an implementation

**Answer file:** `question_2.cpp`

Add a counting notifier that stores only a call count. Construct two services with different notifiers in `main`. Call each twice and assert two recorded messages or a count of 2 without editing `OrderService`.

### Question 3: Validate before infrastructure

**Answer file:** `question_3.cpp`

Require positive order IDs; reject zero and negative IDs with `std::invalid_argument` before calling the notifier. Check both failures leave the recording notifier empty, while id 1 sends one message.

### Question 4: Make failure visible

**Answer file:** `question_4.cpp`

Implement a notifier whose send throws `std::runtime_error`. Define the service contract to propagate this error. Assert confirm(1) throws; do not report a successful return. Explain why silently swallowing the error would change the contract.

### Question 5: Separate construction from policy

**Answer file:** `question_5.cpp`

Write a `run_demo(Notifier&)` function that confirms IDs 1 and 2. Wire a recorder in `main` and assert both exact messages in order. Comment which code would change to use a console notifier and which policy code would stay unchanged.

## Request review

Compile and run all five answers and send: “Design patterns lesson 7 answers are ready in `design-patterns/practice/lesson_07/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
