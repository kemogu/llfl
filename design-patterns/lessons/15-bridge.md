# Lesson 15: Bridge

[Previous lesson](14-adapter.md) · [Schedule](../SCHEDULE.md) · [Next lesson](16-composite.md)

**Goal:** Allow an abstraction and its implementation mechanism to vary independently.

**Prerequisite:** Complete lesson 14 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** Two independent dimensions of variation are becoming entangled in one inheritance hierarchy.

**Typical symptoms:** Classes multiply into combinations such as TextCircle, SvgCircle, TextScaledCircle, and SvgScaledCircle.

**How this lesson addresses it:** Let a shape abstraction hold a Renderer interface. Circle and ScaledCircle vary independently from text, SVG, and JSON renderers, so adding a renderer does not require another shape family.

**When to keep it simpler / limits:** One dimension of variation may need only a simple interface or function. Bridge adds value when abstraction and implementation really need independent evolution.

## Learn and try

Bridge separates two dimensions of variation. An abstraction holds an implementation interface and delegates lower-level work to it; refined abstractions add high-level behavior without multiplying subclasses for every implementation combination.

In the example, a notice is the high-level abstraction and a channel is the delivery mechanism. An urgent notice changes the message while continuing to use any channel. A new channel does not require a new urgent-notice class. The abstraction borrows its channel; callers select and own the channel at the composition root.

Use Bridge when both dimensions need independent extensions. Adapter typically connects an already incompatible API; Bridge deliberately separates variation in a design. Strategy focuses on a replaceable algorithm, while Bridge focuses on an abstraction/implementation split. Their code shapes can overlap. If only one dimension varies, a single interface or a function parameter may be sufficient.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <string>
#include <vector>

struct Channel {
    virtual ~Channel() = default;
    virtual void send(const std::string&) = 0;
};
struct RecordingChannel : Channel {
    std::vector<std::string> messages;
    void send(const std::string& text) override { messages.push_back(text); }
};
class Notice {
protected:
    Channel& channel_;
public:
    explicit Notice(Channel& channel) : channel_(channel) {}
    virtual ~Notice() = default;
    virtual void publish(const std::string& text) { channel_.send(text); }
};
struct UrgentNotice : Notice {
    using Notice::Notice;
    void publish(const std::string& text) override {
        channel_.send("URGENT: " + text);
    }
};
int main() {
    RecordingChannel channel;
    UrgentNotice notice(channel);
    notice.publish("check");
    assert(channel.messages[0] == "URGENT: check");
}
```

`using Notice::Notice` inherits the base constructors. List the classes you would need if every abstraction/channel combination were a separate subclass instead.

## Practice setup

Create `design-patterns/practice/lesson_15/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_15/question_1.cpp -o /tmp/llfl-design-patterns/lesson_15_question_1
/tmp/llfl-design-patterns/lesson_15_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Define the implementation side

**Answer file:** `question_1.cpp`

Create `Renderer::draw_circle(int radius)` returning text. Implement text and SVG renderers returning `"circle:3"` and `"<circle r="3"/>"` for radius 3. Assume positive radii and assert both results.

### Question 2: Bridge the abstraction

**Answer file:** `question_2.cpp`

Create `Circle` storing its radius and borrowing a Renderer. Its `draw()` delegates to the renderer. Construct circles with both renderers and assert the two exact results without renderer-specific subclasses of Circle.

### Question 3: Extend the abstraction dimension

**Answer file:** `question_3.cpp`

Add `ScaledCircle` derived from Circle that draws with twice its positive base radius. Use both renderers; radius 3 must produce radius-6 output. Make the base draw method virtual and destructor virtual. Keep renderer classes unchanged.

### Question 4: Extend the implementation dimension

**Answer file:** `question_4.cpp`

Add a JSON renderer producing `"{"radius":3}"` for radius 3. Test both Circle and ScaledCircle with it, expecting radii 3 and 6. Do not add JSON-specific shape subclasses.

### Question 5: Verify the cross-product

**Answer file:** `question_5.cpp`

Test the six combinations of two abstractions and three renderers with radius 2. Assert all expected strings. Comment on borrowed lifetimes and explain whether a free renderer function would suffice if there were no refined abstractions.

## Request review

Compile and run all five answers and send: “Design patterns lesson 15 answers are ready in `design-patterns/practice/lesson_15/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
