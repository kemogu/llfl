# Lesson 01: Responsibilities and behavior

[Plan](../PLAN.md) · [Schedule](../SCHEDULE.md) · [Next lesson](02-composition-inheritance-and-contracts.md)

**Goal:** Separate calculation from presentation and preserve required behavior while changing structure.

**Prerequisite:** The C++ skills listed in the [plan](../PLAN.md#prerequisites), especially functions, classes, and assertions.

**Time:** 45–60 minutes for study, plus a separate practice session.

## What problem does this solve?

**Problem:** Calculation, presentation, and side effects are mixed together, making small changes risky.

**Typical symptoms:** Changing a receipt label requires editing the same function that computes its total, and tests cannot check the calculation separately.

**How this lesson addresses it:** Separate the total calculation from receipt formatting. A new display format can then reuse the same numeric result, while assertions protect the existing calculation.

**When to keep it simpler / limits:** This is a design foundation, not a GoF pattern. Start with a few cohesive functions; no hierarchy is required.

## Learn and try

A responsibility is something code is accountable for. Calculating a score average and formatting a report are different responsibilities: a scoring rule can change independently of a display format. When these responsibilities are mixed, one change can accidentally affect the other.

Start with the observable behavior. A contract describes accepted input, output, and failures. For this example, input is a nonempty list of numeric scores; the result is their arithmetic mean. Empty input throws `std::invalid_argument`.

```cpp
#include <cassert>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

double average(const std::vector<double>& scores) {
    if (scores.empty()) {
        throw std::invalid_argument("At least one score is required");
    }
    return std::accumulate(scores.begin(), scores.end(), 0.0)
        / static_cast<double>(scores.size());
}

std::string format_average(double value) {
    std::ostringstream output;
    output << "Average: " << std::fixed << std::setprecision(1) << value;
    return output.str();
}

int main() {
    assert(average({70.0, 90.0}) == 80.0);
    assert(format_average(80.0) == "Average: 80.0");
    std::cout << format_average(average({70.0, 90.0})) << '\n';
}
```

Save the example as `scratch.cpp` in the practice folder and compile it using the command below with `scratch` replacing `question_1`. `std::accumulate` sums the scores, and `std::ostringstream` builds the formatted string. The `const` reference avoids copying the vector and prevents modification through that reference. The exact equality assertion uses a result representable exactly; general floating-point checks should use a tolerance. Run the example. Change the display label and verify that the calculation assertion still passes. Then change the scores and predict the result before running it.

Refactoring changes internal structure while preserving required observable behavior. Write checks before moving responsibilities so you can detect accidental changes. An intentional change to output or validation is a behavior change and needs its own updated requirement.

Coupling describes how code depends on other code. Here, formatting receives a number; it does not need to know how scores are stored or averaged. Cohesion describes how closely a unit's work belongs together. These small functions group related work without introducing unnecessary classes.

Separating code has a cost: more names and more navigation. Prefer a split when responsibilities change independently or need independent tests. A small program does not automatically need a pattern. Later lessons will formalize these decisions with SOLID and explore recurring solutions with GoF patterns.

## Practice setup

Create `design-patterns/practice/lesson_01/` and five files named `question_1.cpp` through `question_5.cpp`. Work in order. Copy earlier functions into a later answer when needed so each program runs independently. Give each file its own `main()`. Use `int` for cents and quantities, `std::string` for text, and `const std::string&` for name parameters. Assume inputs and products fit in `int`; overflow handling is outside this lesson. Implement only the validation explicitly requested. Use `std::to_string` to turn integers into text and `std::cout` for printing.

Run each answer from the repository root:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_01/question_1.cpp -o /tmp/llfl-design-patterns/question_1
/tmp/llfl-design-patterns/question_1
```

Use `assert` from `<cassert>` to check values and compile without `-DNDEBUG`, which would disable assertions. For a required error, initialize a boolean to `false`, call the function inside `try`, catch `const std::invalid_argument&` and set the boolean to `true`, then assert that it is true. Include `<stdexcept>` for this exception type. Change both the source filename and executable name when compiling each answer. You can use `clang++` instead of `g++` with the same flags.

## Five coding questions

### Question 1: Establish behavior

**Answer file:** `question_1.cpp`

Write `receipt_line(name, price_cents, quantity)` that calculates a total and returns text in the form `Notebook: 750 cents`. Assert that `("Notebook", 250, 3)` produces that exact string and quantity `0` produces `Notebook: 0 cents`. Print both results. In a comment, name the calculation and presentation responsibilities mixed in this function.

### Question 2: Separate calculation

**Answer file:** `question_2.cpp`

Write `calculate_total(price_cents, quantity)` and `format_receipt(name, total_cents)`. Reimplement `receipt_line` by calling these two functions. Preserve both outputs from question 1 and assert them. Also assert that `calculate_total(250, 4)` returns `1000`. Keep printing outside these functions.

### Question 3: Add another presentation

**Answer file:** `question_3.cpp`

Reuse the calculation and original formatter. Add `format_detailed_receipt(name, quantity, total_cents)` returning `Notebook x3: 750 cents` for the example order. Calculate the total once and pass it to both formatters. Assert both exact strings and print them. Explain in a comment why a new display format does not require changing the calculation.

### Question 4: Define invalid input behavior

**Answer file:** `question_4.cpp`

Extend `calculate_total` to throw `std::invalid_argument` for a negative price or negative quantity. Zero is valid. Assert that `(250, 0)` and `(0, 3)` both return `0`, and `(250, 3)` returns `750`. Check separately that `(-1, 3)` and `(250, -1)` each throw `std::invalid_argument`. Comment on why this adds a behavior requirement rather than being only a refactor.

### Question 5: Combine and explain

**Answer file:** `question_5.cpp`

Use your validated calculation and original formatter with these orders: `("Notebook", 250, 3)`, `("Pen", 100, 2)`, and `("Bag", 1200, 0)`. Represent each order with a small `struct` containing name, price, and quantity, stored in a `std::vector`. Build a `std::vector<std::string>` of receipt lines and compare it with a named expected vector containing `{"Notebook: 750 cents", "Pen: 200 cents", "Bag: 0 cents"}` using `assert(actual == expected)`, then print each line. Keep calculation, formatting, and the loop separate. Add comments identifying where a display change would go and explaining whether an additional class would help this small program.

## Request review

Run all five files. Send: “Design patterns lesson 1 answers are ready in `design-patterns/practice/lesson_01/`. Please check all five files.” Correct any issues before starting lesson 02.
