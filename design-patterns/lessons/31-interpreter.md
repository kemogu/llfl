# Lesson 31: Interpreter

[Previous lesson](30-visitor.md) · [Schedule](../SCHEDULE.md) · [Next lesson](32-pattern-selection.md)

**Goal:** Represent a small language as an expression tree with explicit evaluation rules.

**Prerequisite:** Complete lesson 30 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** A small domain language needs explicit semantics for composing and evaluating expressions.

**Typical symptoms:** Nested rules become ad hoc string conditionals, and evaluation logic no longer follows a clear grammar.

**How this lesson addresses it:** Model literals and addition as expression nodes. An Add node evaluates its child expressions, so an explicit tree represents grouping and can later include variables resolved from a context.

**When to keep it simpler / limits:** Interpreter is suitable for small grammars. It does not itself parse input text, and larger languages may need a dedicated parser and a different representation.

## Learn and try

Interpreter models grammar rules as objects whose evaluation follows the language semantics. Terminal expressions are values or names; nonterminal expressions combine other expressions. A context supplies external values when the language includes variables.

Our grammar is `expression := integer | (expression + expression)`. The worked example constructs the abstract syntax tree directly; it does not parse text. The Literal and Add classes mirror its grammar, and Add owns its operands. A parser, if needed, would be a separate step that turns text into this tree. Do not execute input as C++ or shell code.

Use Interpreter for a tiny, stable domain language. Class-per-rule designs become unwieldy for complex grammars; a dedicated parser and a different evaluation representation may be more suitable. Define unknown-name errors, numeric limits, and syntax policy before extending the language. Arithmetic here uses small integers that fit in int; production evaluation needs an overflow policy.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <memory>
#include <stdexcept>
#include <utility>

struct Expression {
    virtual ~Expression() = default;
    virtual int evaluate() const = 0;
};
struct Literal : Expression {
    int value;
    explicit Literal(int n) : value(n) {}
    int evaluate() const override { return value; }
};
class Add : public Expression {
    std::unique_ptr<Expression> left_, right_;
public:
    Add(std::unique_ptr<Expression> left, std::unique_ptr<Expression> right)
        : left_(std::move(left)), right_(std::move(right)) {
        if (!left_ || !right_) throw std::invalid_argument("missing operand");
    }
    int evaluate() const override { return left_->evaluate() + right_->evaluate(); }
};
int main() {
    Add expression(std::make_unique<Literal>(2), std::make_unique<Literal>(3));
    assert(expression.evaluate() == 5);
}
```

Draw the tree for 2 + (3 + 4). Its structure specifies grouping without any operator-precedence parser.

## Practice setup

Create `design-patterns/practice/lesson_31/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_31/question_1.cpp -o /tmp/llfl-design-patterns/lesson_31_question_1
/tmp/llfl-design-patterns/lesson_31_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Interpret terminals

**Answer file:** `question_1.cpp`

Define Literal behind an Expression interface and assert values 0, 7, and -2 evaluate to themselves. Use virtual destruction for owning base pointers.

### Question 2: Interpret composition

**Answer file:** `question_2.cpp`

Implement Add owning two non-null operands. Build 2 + (3 + 4), assert 9, and assert repeated evaluation stays 9. Reject a missing operand with `std::invalid_argument`.

### Question 3: Extend the grammar

**Answer file:** `question_3.cpp`

Add Multiply and construct (2 + 3) * 4 and 2 + (3 * 4). Assert 20 and 14. Describe why explicit tree structure, not C++ expression parsing, determines evaluation order in this representation.

### Question 4: Add a context

**Answer file:** `question_4.cpp`

Change evaluate to accept `const std::map<std::string,int>&`. Literals ignore it, compound expressions forward it, and Variable looks up a name or throws `std::out_of_range`. Evaluate x + 3 with x=5 and x=8, asserting 8 and 11; check missing x throws.

### Question 5: Keep parsing separate

**Answer file:** `question_5.cpp`

Implement only a literal parser `parse_literal(text)` using `std::stoi(text, &position)` and requiring position==text.size(). For this exercise allow an optional leading sign and decimal digits only; reject empty input, spaces, and any other character with `std::invalid_argument` before conversion. Include `<string>`. Assert `"12"` and `"-3"` evaluate correctly; reject `"2+3"`, `"12x"`, and empty input. Explain why this parser does not yet implement the whole expression grammar.

## Request review

Compile and run all five answers and send: “Design patterns lesson 31 answers are ready in `design-patterns/practice/lesson_31/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
