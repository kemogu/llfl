# Lesson 14: Adapter

[Previous lesson](13-singleton.md) · [Schedule](../SCHEDULE.md) · [Next lesson](15-bridge.md)

**Goal:** Translate an existing incompatible interface into a client’s expected contract.

**Prerequisite:** Complete lesson 13 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** An existing component performs the needed work but exposes an interface or semantics that do not match the client contract.

**Typical symptoms:** Clients repeat legacy method names, numeric severity mappings, or unit conversions at every call site.

**How this lesson addresses it:** Wrap a Fahrenheit-based heater behind a Celsius-based interface, performing the conversion inside the adapter. Existing clients use their expected contract without knowing the legacy API.

**When to keep it simpler / limits:** If you own both sides and compatibility is unnecessary, changing the original interface may be simpler. Adapter cannot hide a semantic mismatch without defining a valid translation.

## Learn and try

Adapter wraps an existing object, the adaptee, and presents the target interface expected by a client. Translation can include names, arguments, units, and results. The wrapped implementation can stay unchanged.

The example translates Celsius input into the Fahrenheit API used by a legacy heater. The adapter borrows the heater, so its lifetime must be shorter. A contract must specify units explicitly: matching argument types does not guarantee semantic compatibility. The target permits any finite sample temperature for this exercise; range enforcement would be a separate requirement.

Use an adapter when integrating an API you cannot or should not change. If you own both sides and no compatibility requirement exists, renaming or changing the original API may be simpler. Adapter changes an interface; Decorator later adds behavior behind an already compatible interface. Avoid catching every error and returning a success-looking default during translation.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <cmath>

class LegacyHeater {
    double fahrenheit_ = 32.0;
public:
    void set_fahrenheit(double value) { fahrenheit_ = value; }
    double fahrenheit() const { return fahrenheit_; }
};
struct Heater {
    virtual ~Heater() = default;
    virtual void set_celsius(double value) = 0;
};
class HeaterAdapter : public Heater {
    LegacyHeater& legacy_;
public:
    explicit HeaterAdapter(LegacyHeater& legacy) : legacy_(legacy) {}
    void set_celsius(double value) override {
        legacy_.set_fahrenheit(value * 9.0 / 5.0 + 32.0);
    }
};
int main() {
    LegacyHeater legacy;
    HeaterAdapter adapter(legacy);
    adapter.set_celsius(100.0);
    assert(std::abs(legacy.fahrenheit() - 212.0) < 0.000001);
}
```

Check 0°C maps to 32°F. Explain why simply forwarding the same double value would compile but violate the target contract.

## Practice setup

Create `design-patterns/practice/lesson_14/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_14/question_1.cpp -o /tmp/llfl-design-patterns/lesson_14_question_1
/tmp/llfl-design-patterns/lesson_14_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Model an incompatible API

**Answer file:** `question_1.cpp`

Write `LegacyLogger::write(int severity, const std::string& text)` recording strings in the form `"2:ready"`. Assert one write produces exactly one such record. Treat this class as unchanged for later questions.

### Question 2: Implement the target

**Answer file:** `question_2.cpp`

Define `Logger::info(const std::string&)` and an adapter borrowing `LegacyLogger`. Map info to severity 2. A client accepting `Logger&` sends `"ready"`; assert the legacy record is `"2:ready"`.

### Question 3: Translate another operation

**Answer file:** `question_3.cpp`

Extend the target with `error(text)`, mapping it to severity 5. Send info `"start"` then error `"failed"`; assert records `"2:start"` and `"5:failed"` in that order. Keep client code unaware of numeric severities.

### Question 4: Preserve error semantics

**Answer file:** `question_4.cpp`

Make a separate legacy logger implementation throw `std::runtime_error` on an empty message. Adapt it to the same target and propagate the error. Assert empty input throws and appends no record, while `"ok"` still works.

### Question 5: Compare replacement with adaptation

**Answer file:** `question_5.cpp`

Implement a native target logger recording info and error messages with text labels (`"info:ready"`, `"error:failed"`). Run one client against native and adapted implementations and verify their specified records. Explain why the legacy interface translation belongs inside the adapter, not in the client.

## Request review

Compile and run all five answers and send: “Design patterns lesson 14 answers are ready in `design-patterns/practice/lesson_14/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
