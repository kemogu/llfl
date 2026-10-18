# Lesson 20: Proxy

[Previous lesson](19-flyweight.md) · [Schedule](../SCHEDULE.md) · [Next lesson](21-strategy.md)

**Goal:** Control access to another object through the same interface.

**Prerequisite:** Complete lesson 19 and its five answers first. Use C++17 and the prerequisites in the [plan](../PLAN.md#prerequisites).

**Time:** 45–60 minutes for study plus a separate practice session. Workshops and capstones may need several sessions.

## What problem does this solve?

**Problem:** Clients need the subject interface, but access must be delayed, authorized, or cached without spreading that policy through callers.

**Typical symptoms:** Callers repeat lazy initialization, permission checks, or cache lookups before every use of an expensive object.

**How this lesson addresses it:** Place a proxy behind the same interface: a LazyAsset constructs the real asset on first use, while a permission or caching proxy enforces its own stated access contract.

**When to keep it simpler / limits:** Direct access is simpler for cheap unrestricted objects. A proxy must define error propagation, cache freshness, and synchronization where applicable; it is not automatically transparent in cost.

## Learn and try

Proxy implements the subject interface and controls access to a real subject. It may defer construction, enforce permissions, or cache results. The client uses the same contract while the proxy manages when and whether the real operation happens.

The example initializes an expensive asset only on its first read. `unique_ptr` owns the real subject once created. Both reads return the same data, but construction occurs once. This toy uses a flag-like loaded query for observation rather than real I/O.

Use a proxy for an explicit access policy. A decorator mainly adds a responsibility; a proxy mainly stands in for and mediates access to a subject. Similar structure does not imply identical intent. For cheap local objects, direct construction is simpler. Caches need a freshness and invalidation contract, permissions must be checked at the right time, and lazy state is not automatically thread-safe.

### Worked example

This is a complete, standalone program. Save it as `scratch.cpp` in this lesson's practice folder.

```cpp
#include <cassert>
#include <memory>
#include <string>

struct Asset {
    virtual ~Asset() = default;
    virtual std::string read() = 0;
};
struct RealAsset : Asset {
    std::string read() override { return "pixels"; }
};
class LazyAsset : public Asset {
    std::unique_ptr<RealAsset> real_;
public:
    bool loaded() const { return static_cast<bool>(real_); }
    std::string read() override {
        if (!real_) real_ = std::make_unique<RealAsset>();
        return real_->read();
    }
};
int main() {
    LazyAsset asset;
    assert(!asset.loaded());
    assert(asset.read() == "pixels");
    assert(asset.loaded());
    assert(asset.read() == "pixels");
}
```

Add a construction counter in a local experiment and confirm two reads create one subject. State the single-threaded assumption explicitly.

## Practice setup

Create `design-patterns/practice/lesson_20/` and write `question_1.cpp` through `question_5.cpp`. Each file has its own `main()` and must compile independently. Copy earlier definitions when needed; capstone lessons may instead share a local header as described below. You write the answers; the worked example demonstrates the idea in a separate task.

From the repository root, compile and run one answer:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_20/question_1.cpp -o /tmp/llfl-design-patterns/lesson_20_question_1
/tmp/llfl-design-patterns/lesson_20_question_1
```

Change both filenames for questions 2–5. To run the example, use `scratch.cpp` and a matching executable name. `clang++` can replace `g++`. Keep assertions enabled: do not define `NDEBUG`. Every question needs executable checks, not just printed output. Check expected exceptions with a boolean set in a matching `catch` block and assert it afterward. Use stack objects or smart pointers with explicit ownership; borrowed dependencies must outlive their clients. Unless a question says otherwise, use small integer inputs whose calculations fit in `int`.

## Five coding questions

### Question 1: Define the subject

**Answer file:** `question_1.cpp`

Define `DataSource::read()` returning a string. Implement a counting source that returns `"data"` and increments a read counter. Assert two direct reads produce count 2.

### Question 2: Defer construction

**Answer file:** `question_2.cpp`

Implement a LazySource proxy that creates the concrete source on first read. Track construction with an external counter whose lifetime covers the proxy. Assert count 0 before use, 1 after two reads, and both results `"data"`.

### Question 3: Control access

**Answer file:** `question_3.cpp`

Implement a PermissionProxy borrowing a DataSource and storing an allowed flag. Denied reads throw `std::runtime_error` without forwarding. Assert zero underlying calls for denied access and one for an allowed read.

### Question 4: Cache with a contract

**Answer file:** `question_4.cpp`

Implement a CachingProxy borrowing a source. Cache its first successful string result, including an empty string, using a separate boolean to indicate cache presence. Add `invalidate()`. Assert two reads call the source once; invalidate then read calls it a second time.

### Question 5: Handle failure correctly

**Answer file:** `question_5.cpp`

Use a source that throws on its first call and returns `"ok"` thereafter. Verify CachingProxy does not cache failure: first read throws, second returns ok, third uses the cache, and the underlying call count is 2. Explain the difference between the proxy’s access policy and a decorator’s added formatting.

## Request review

Compile and run all five answers and send: “Design patterns lesson 20 answers are ready in `design-patterns/practice/lesson_20/`. Please check all five files.” Explain one tradeoff and any unresolved errors. Revise answers that need correction before moving on.
