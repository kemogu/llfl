# SOLID and GoF learning plan

## Goal

Learn to recognize design problems, preserve behavior while refactoring, and choose a suitable design with an explanation of its costs. Use modern C++ to practice ideas that also transfer to other object-oriented languages.

SOLID describes five design principles; GoF describes 23 named patterns for recurring design problems. Principles guide decisions; patterns describe possible solutions. Neither is a requirement to add abstractions to every program.

## Prerequisites

C++ is the implementation language for this track. You do not need to complete the Python course first. Be comfortable with:

- Functions, references, `const`, classes, constructors, and access control.
- `std::string`, `std::vector`, loops, and basic standard-library algorithms.
- Inheritance, virtual functions, and abstract interfaces.
- Object lifetime, RAII, value semantics, and basic smart-pointer ownership.
- Compiling a program, reading diagnostics, assertions, and exceptions.

Readiness check: build two collaborating classes, pass a dependency through a constructor, and write assertions for normal and invalid input. Explain who owns each object and how long a referenced dependency must live. Review unfamiliar prerequisites as needed; their study time is separate from this schedule.

Use **C++17** and the standard library, with a compiler supporting that standard. Introduce any additional syntax before asking you to use it. We will compare runtime polymorphism with simpler functions, value types, and templates where appropriate.

Throughout the course, make ownership explicit. Prefer values and `std::unique_ptr` for exclusive ownership; use `std::shared_ptr` only when ownership is genuinely shared. Non-owning references and pointers require clear lifetime guarantees. Polymorphic interfaces intended for deletion through a base pointer need virtual destructors. Avoid object slicing, owning raw pointers, and manual `new`/`delete` in exercises. Pattern lessons will introduce the relevant copy/move and lifetime details before practice.

## Our lesson agreement

1. I prepare one Markdown lesson in `design-patterns/lessons/` before you begin it.
2. Each lesson explains a concrete problem, a worked example, the design decision, and its tradeoffs. Pattern lessons cover intent, collaborating objects, when to use the pattern, when to avoid it, and a simpler alternative.
3. Every lesson ends with **exactly five coding questions**, using only concepts already introduced. Each has a concrete requirement and expected behavior or checks.
4. You write **five separate `.cpp` answer files** and run them. I leave the answers for you to write.
5. Ask me to review all five files. I check behavior, understanding, clarity, ownership and lifetime safety, relevant edge cases, and whether the abstraction earns its complexity.
6. I mark each answer **Complete** or **Needs revision**, explain why, and give a focused hint. I do not replace your answers unless you ask.
7. Revise and request another review as needed. Move forward when all five answers meet their requirements and you can explain the design.

Questions usually progress through reproducing a problem, applying the design, extending it, testing its contract, and comparing it with a simpler solution. Short design explanations belong in comments alongside working code. Refactoring questions must include checks that observable behavior remains correct.

## File organization

```text
design-patterns/
    README.md
    PLAN.md
    SCHEDULE.md
    lessons/
        01-responsibilities-and-behavior.md
    practice/
        README.md
        lesson_01/             # You create this when starting practice.
            question_1.cpp
            question_2.cpp
            question_3.cpp
            question_4.cpp
            question_5.cpp
```

Use two-digit lesson prefixes and descriptive kebab-case lesson filenames. Continue with `lesson_02/`, `lesson_03/`, and so on for answers. Optional experiments go in `scratch.cpp`. Later capstone answers may share headers and source files inside their lesson folder, but retain five answer programs demonstrating the five requirements.

From the repository root:

```bash
mkdir -p /tmp/llfl-design-patterns
g++ -std=c++17 -Wall -Wextra -Wpedantic design-patterns/practice/lesson_01/question_1.cpp -o /tmp/llfl-design-patterns/question_1
/tmp/llfl-design-patterns/question_1
```

These commands assume GCC (`g++`) on Linux; use `clang++` with the same flags if available. Compile each answer separately because each has its own `main()`. Change both the source and executable name for questions 2–5. Do not define `NDEBUG` during practice, so `assert` checks remain active. Later lessons using multiple source files will provide their build commands. Keep examples deterministic and local; no external services or third-party libraries are needed.

## Learning roadmap

This is a **34-lesson, 17-week starting plan** at two lessons per week. All 34 lesson files are ready, each with a standalone C++17 example and exactly five coding questions. Study and review them in order.

| Week | Lessons | Practical outcome |
| --- | --- | --- |
| 1 | [01: Responsibilities and behavior](lessons/01-responsibilities-and-behavior.md); [02: Composition, inheritance, and contracts](lessons/02-composition-inheritance-and-contracts.md) | Separate calculation from presentation; compare object collaboration with inheritance and define behavioral contracts. |
| 2 | [03: Single Responsibility Principle (SRP)](lessons/03-single-responsibility.md); [04: Open/Closed Principle (OCP)](lessons/04-open-closed.md) | Separate reasons to change; add a new policy through an appropriate extension point. |
| 3 | [05: Liskov Substitution Principle (LSP)](lessons/05-liskov-substitution.md); [06: Interface Segregation Principle (ISP)](lessons/06-interface-segregation.md) | Test substitutable implementations; give clients only the capabilities they need. |
| 4 | [07: Dependency Inversion Principle (DIP)](lessons/07-dependency-inversion.md); [08: SOLID refactoring workshop](lessons/08-solid-refactoring.md) | Make policy depend on contracts, inject implementations, and refactor a small order service with regression checks. |
| 5 | [09: Factory Method](lessons/09-factory-method.md); [10: Abstract Factory](lessons/10-abstract-factory.md) | Override product creation through a creator hierarchy; create compatible families of products. |
| 6 | [11: Builder](lessons/11-builder.md); [12: Prototype](lessons/12-prototype.md) | Construct an object in stages; clone configured objects while handling ownership and deep-copy semantics. |
| 7 | [13: Singleton](lessons/13-singleton.md); [14: Adapter](lessons/14-adapter.md) | Examine shared identity, global state, and test isolation; adapt an incompatible interface. |
| 8 | [15: Bridge](lessons/15-bridge.md); [16: Composite](lessons/16-composite.md) | Vary abstraction and implementation independently; treat individual objects and trees through one contract. |
| 9 | [17: Decorator](lessons/17-decorator.md); [18: Facade](lessons/18-facade.md) | Add behavior through object wrapping; expose a small interface to a subsystem. |
| 10 | [19: Flyweight](lessons/19-flyweight.md); [20: Proxy](lessons/20-proxy.md) | Share intrinsic state while keeping context external; control access through a stand-in object. |
| 11 | [21: Strategy](lessons/21-strategy.md); [22: Template Method](lessons/22-template-method.md) | Swap algorithms through composition; customize steps of an inherited algorithm skeleton. |
| 12 | [23: Observer](lessons/23-observer.md); [24: Command](lessons/24-command.md) | Notify subscribers and manage subscriptions; represent actions as objects with explicit undo behavior. |
| 13 | [25: State](lessons/25-state.md); [26: Chain of Responsibility](lessons/26-chain-of-responsibility.md) | Delegate behavior to a current state; route a request through handlers with explicit stopping rules. |
| 14 | [27: Iterator](lessons/27-iterator.md); [28: Mediator](lessons/28-mediator.md) | Traverse without exposing representation; centralize coordination between collaborating objects. |
| 15 | [29: Memento](lessons/29-memento.md); [30: Visitor](lessons/30-visitor.md) | Restore snapshots without exposing internal details; add operations over a stable object structure. |
| 16 | [31: Interpreter](lessons/31-interpreter.md); [32: Pattern selection and simplification](lessons/32-pattern-selection.md) | Evaluate a tiny expression grammar; compare similar patterns and remove unnecessary abstractions. |
| 17 | [33: Capstone build](lessons/33-capstone-build.md); [34: Capstone review and change request](lessons/34-capstone-review.md) | Build a tested order-processing application, implement a new requirement, and justify design choices. |

## Coverage and important distinctions

- **SOLID:** SRP (03), OCP (04), LSP (05), ISP (06), DIP (07), integrated in 08. SRP concerns reasons to change, not a rule that every class has one method. OCP needs a chosen extension boundary, not a ban on editing code. LSP concerns behavior, not merely matching signatures. ISP follows client needs. Dependency injection is a technique that can support DIP, not the principle itself.
- **Creational — 5:** Factory Method, Abstract Factory, Builder, Prototype, Singleton (09–13). Distinguish GoF Factory Method from a simple factory function. Treat Singleton critically: compare it with explicitly passing a shared instance and examine hidden dependencies.
- **Structural — 7:** Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy (14–20). Use explicit ownership for object wrappers and compare them by intent, not just their similar shape.
- **Behavioral — 11:** Strategy, Template Method, Observer, Command, State, Chain of Responsibility, Iterator, Mediator, Memento, Visitor, Interpreter (21–31). Compare Strategy with State, and Observer with Mediator. Interpreter uses a tiny explicit grammar and expression tree. Iterator includes a comparison with standard-library iterators; Visitor includes double dispatch and a comparison with `std::variant`/`std::visit`.

## Capstone

Build a local order-processing application using integer cents, in-memory storage, replaceable pricing policies, and notification implementations. Validate quantities and calculate totals deterministically. Begin with the simplest working design and add patterns only for demonstrated needs.

Lesson 33's five tasks cover the domain model, pricing policies, storage boundary, notifications, and an integrated workflow with behavioral checks. Lesson 34's five tasks cover regression checks, a new pricing requirement, an adapter for a supplied legacy notification interface, failure cases, and simplification with a short design explanation. Both lesson files specify exact inputs, failure behavior, and acceptance checks.

Success means the application works, a new implementation can be substituted at its intended boundary, tests catch contract violations, and you can explain both the benefits and costs of your abstractions. You do not need to force all 23 patterns into a single project.

## Review request and next step

> Design patterns lesson 1 answers are ready in `design-patterns/practice/lesson_01/`. Please check all five files.

Include any confusing behavior or unresolved errors. Reviews happen when you return and ask; suggested study days are not appointments.

**Next:** check the prerequisites, then start [lesson 01](lessons/01-responsibilities-and-behavior.md). After its review, continue to [lesson 02](lessons/02-composition-inheritance-and-contracts.md) using this plan's lesson agreement.
