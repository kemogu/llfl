# Lesson 28: Mediator

[Previous lesson](27-iterator.md) · [Schedule](../SCHEDULE.md) · [Next lesson](29-memento.md)

**Goal:** Centralize coordination rules among collaborating components.

**Prerequisite:** Complete lesson 27 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** Many peer objects coordinate by knowing and calling each other directly, creating tangled dependencies.

**Typical symptoms:** A form field updates buttons and other controls itself, while each new rule requires editing several colleagues.

**How this lesson addresses it:** Have colleagues notify a FormMediator. It combines username and accepted-terms state to decide whether submission is enabled, keeping interaction rules in one place.

**When to keep it simpler / limits:** Direct composition is simpler for a small stable relationship. A mediator should coordinate collaborators rather than absorb all domain logic into one large class.

## Learn and try

Mediator moves knowledge of peer coordination into one object. Colleagues signal the mediator instead of invoking each other directly. The mediator knows the workflow and which colleague should react.

The example's button invokes a dialog through the mediator interface; the dialog updates a label. Button and dialog borrow their dependencies. Construction order ensures label outlives dialog and dialog outlives button. This is directed coordination, not broadcast subscription: Observer distributes events to subscribers, whereas a mediator can interpret events and choose specific actions.

Use Mediator when peer-to-peer relationships become tangled. Avoid moving all business logic into a giant mediator; keep domain work in the colleagues and put interaction rules in the mediator. For two objects with one straightforward interaction, direct composition may be simpler. Define reentrant-event behavior if colleagues can emit new events while handling one; this example's label does not emit events.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <string>

struct Mediator {
    virtual ~Mediator() = default;
    virtual void clicked() = 0;
};
struct Label { std::string text; };
class Dialog : public Mediator {
    Label& label_;
public:
    explicit Dialog(Label& label) : label_(label) {}
    void clicked() override { label_.text = "saved"; }
};
class Button {
    Mediator& mediator_;
public:
    explicit Button(Mediator& mediator) : mediator_(mediator) {}
    void click() { mediator_.clicked(); }
};
int main() {
    Label label;
    Dialog dialog(label);
    Button button(dialog);
    button.click();
    assert(label.text == "saved");
}
```

Draw the references and ensure no colleague requires a reference to every other colleague. Identify the dialog rule separately from the label’s storage responsibility.

## Practice setup

Create `design-patterns/practice/lesson_28/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_28/question_1.cpp -o /tmp/llfl-design-patterns/lesson_28_question_1
/tmp/llfl-design-patterns/lesson_28_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Create colleagues

**Answer file:** `question_1.cpp`

Define UsernameField containing text and SubmitButton containing an enabled flag initially false. Create a FormMediator borrowing both and an `on_username_changed()` operation that enables submit exactly when text is nonempty. Assert empty disables and `"Ada"` enables.

### Question 2: Route an event

**Answer file:** `question_2.cpp`

Give a field-editing client a mediator reference. Setting a field value must notify the mediator so the button updates. Assert changing empty→Ada→empty yields false→true→false without field code directly changing the button.

### Question 3: Coordinate a second condition

**Answer file:** `question_3.cpp`

Add an AcceptedTerms colleague with a boolean. Enable submit only when username is nonempty and terms are accepted. Provide notifications for both changes and assert all four combinations.

### Question 4: Test isolated forms

**Answer file:** `question_4.cpp`

Create two independent sets of colleagues and mediators. Change only the first form and assert the second remains unchanged. Comment on ownership and the requirement that colleagues outlive the mediator references that access them.

### Question 5: Keep coordination focused

**Answer file:** `question_5.cpp`

Add a `submit()` action on the mediator returning `"submitted:Ada"` only when enabled, otherwise throwing `std::logic_error`. Assert success and disabled failure. Keep username storage and formatting helpers outside the coordination condition, and explain how this differs from broadcasting an event to all observers.

## Request review

Compile and run all five answers and send: “Design patterns lesson 28 answers are ready in `design-patterns/practice/lesson_28/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
