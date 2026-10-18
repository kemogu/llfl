# Lesson 19: Flyweight

[Previous lesson](18-facade.md) · [Schedule](../SCHEDULE.md) · [Next lesson](20-proxy.md)

**Goal:** Share immutable intrinsic state while keeping per-use context outside it.

**Prerequisite:** Complete lesson 18 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** Many logical objects duplicate substantial reusable state, wasting memory at the required scale.

**Typical symptoms:** Thousands of positioned glyphs each store the same font data, or tree occurrences duplicate identical species and appearance data.

**How this lesson addresses it:** Share an immutable Font or TreeType through a cache keyed by all intrinsic properties. Keep each occurrence’s coordinates outside the shared object.

**When to keep it simpler / limits:** Use ordinary values when duplication is small. Cache overhead and retention can outweigh savings, and sharing mutable occurrence-specific state would couple independent objects.

## Learn and try

Flyweight reduces duplicated state by sharing an object across many logical occurrences. Intrinsic state is the reusable part, such as a font name. Extrinsic state belongs to a particular use, such as text position, and is supplied separately.

The factory below caches one immutable Font per name. It returns shared ownership because glyphs may outlive the factory, and multiple glyphs intentionally share the same font. This is a specific reason for `shared_ptr`, not a default ownership policy. The cache also owns the fonts and therefore retains them until it is destroyed.

Use Flyweight when profiling or a clear scale requirement shows substantial repeated state. For small objects or a few occurrences, values are simpler and cache management may cost more than duplication. Choose keys that capture all intrinsic state. The example is single-threaded; a shared factory would need synchronization for concurrent mutations. Sharing mutable per-use data would incorrectly couple independent objects.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <map>
#include <memory>
#include <string>
#include <utility>

struct Font {
    const std::string name;
    explicit Font(std::string value) : name(std::move(value)) {}
};
class FontFactory {
    std::map<std::string, std::shared_ptr<const Font>> cache_;
public:
    std::shared_ptr<const Font> get(const std::string& name) {
        auto found = cache_.find(name);
        if (found != cache_.end()) return found->second;
        auto font = std::make_shared<const Font>(name);
        cache_.emplace(name, font);
        return font;
    }
};
struct Glyph {
    std::shared_ptr<const Font> font;
    int x;
};
int main() {
    FontFactory factory;
    Glyph first{factory.get("mono"), 1};
    Glyph second{factory.get("mono"), 9};
    assert(first.font == second.font);
    assert(first.x != second.x);
}
```

Explain which fields must not be moved into Font. Count unique font objects rather than assuming that pointer sharing alone proves a performance gain.

## Practice setup

Create `design-patterns/practice/lesson_19/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_19/question_1.cpp -o /tmp/llfl-design-patterns/lesson_19_question_1
/tmp/llfl-design-patterns/lesson_19_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Separate the state

**Answer file:** `question_1.cpp`

Define immutable `TreeType` containing a species string and a `Tree` occurrence containing shared type plus x/y coordinates. Create two oak occurrences at (1,2) and (3,4) sharing one type. Assert shared identity and distinct coordinates.

### Question 2: Centralize reuse

**Answer file:** `question_2.cpp`

Implement `TreeFactory::get(species)` using a map and returning `std::shared_ptr<const TreeType>`. Assert two oak requests share identity and a pine request has a different identity. Expose a cache size and assert 2.

### Question 3: Build many occurrences

**Answer file:** `question_3.cpp`

Create 100 oak trees at x values 0–99 and y 0. Assert vector size 100, cache size 1, and every occurrence points to the same immutable type. Change one occurrence’s position and verify the others are unaffected.

### Question 4: Check lifetime

**Answer file:** `question_4.cpp`

Create a tree outside a nested scope, assign its type from a factory inside that scope, then destroy the factory. Assert the tree can still read its type afterward because it holds shared ownership. Explain why a borrowed pointer to a factory-owned object would require a different lifetime contract.

### Question 5: Choose a complete cache key

**Answer file:** `question_5.cpp`

Extend intrinsic state with a color string. Use `std::map<std::pair<std::string,std::string>, ...>` as the cache. Assert oak/green is reused, oak/red is distinct, and cache size is 2. Comment on cache retention and when ordinary values would be simpler.

## Request review

Compile and run all five answers and send: “Design patterns lesson 19 answers are ready in `design-patterns/practice/lesson_19/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
