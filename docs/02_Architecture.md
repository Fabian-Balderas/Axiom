# Axiom Architecture v1.0

> "Everything is a module."

---

# Purpose

This document defines the internal architecture of Axiom.

The goal is to create a system that is:

• Modular
• Extensible
• Maintainable
• Testable
• Local-first
• Platform independent

No single component should depend on implementation details of another.

Every major capability communicates through clearly defined interfaces.

---

# System Overview

                   User
                     │
              User Interface
                     │
         ┌───────────┴───────────┐
         │                       │
      Command Parser       Conversation Engine
         │                       │
         └───────────┬───────────┘
                     │
               Reasoning Engine
                     │
    ┌────────────────┼────────────────┐
    │                │                │
 Memory         Skill Manager      Project Manager
    │                │                │
    └──────┬─────────┴─────────┬──────┘
           │                   │
     Knowledge Base      Plugin Manager
           │                   │
           └─────────API────────┘




---

## One architectural principle I'd add

I'd call it **"Core vs. Skills."**

The **Core** should remain intentionally small. It knows *how* to think, coordinate, remember, and communicate—but it doesn't know *how* to solve every problem.

Everything domain-specific—CAD, Strudel, computer vision, robotics, Unreal Engine, textbook indexing, the Algorithm Atlas—belongs in **Skills**.

That gives us a simple rule:

- **Core** = infrastructure.
- **Skills** = capabilities.

As Axiom grows, the Core should grow very slowly, while the Skills library can expand rapidly.

---

## After Architecture

Once this document is complete, the rest of the docs almost write themselves:

- **03_Coding_Standards.md** → How every module should be written.
- **04_Plugin_Specification.md** → The contract every Skill or plugin follows.
- **05_Memory_System.md** → How memory is stored, indexed, retrieved, and connected.
- **06_API.md** → The interfaces between components.

At that point, we'd have what many large software projects lack: a complete engineering blueprint before a single line of implementation code. That should make Axiom 2.0 much easier to build, test, and extend over time. 