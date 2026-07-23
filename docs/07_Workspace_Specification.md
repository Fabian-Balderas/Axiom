# Axiom Workspace Specification
Version: 1.0

---

# Purpose

The Axiom Workspace Specification defines the standard layout for every engineering project created by Axiom.

Its purpose is to ensure every project is organized consistently so that both humans and AI can immediately understand where information belongs.

A standardized workspace allows Axiom to automate project creation, documentation, research organization, code generation, asset management, and future AI-assisted workflows.

---

# Design Principles

Every workspace should:

- Be predictable.
- Be scalable.
- Separate different categories of information.
- Preserve engineering history.
- Minimize ambiguity.
- Support future automation.

If an AI generates or stores information, it should always know where that information belongs.

---

# Workspace Layout

```
Project/
│
├── axiom.json
│
├── README.md
├── roadmap.md
├── notes.md
├── tasks.json
│
├── docs/
│   ├── research/
│   ├── references/
│   └── specifications/
│
├── source/
│
├── assets/
│   ├── images/
│   ├── videos/
│   └── datasets/
│
├── experiments/
│
├── exports/
│
└── archive/
```

---

# Root Files

## axiom.json

Contains project metadata used internally by Axiom.

Example:

```json
{
    "name": "",
    "workspace_version": "1.0",
    "created": "",
    "description": "",
    "tags": []
}
```

---

## README.md

High-level overview of the project.

Should answer:

- What is this project?
- Why does it exist?
- Current status.
- Quick links.

---

## roadmap.md

Long-term development roadmap.

Milestones.

Future ideas.

Completed work.

---

## notes.md

Engineering notebook.

Meeting notes.

Ideas.

Research observations.

Daily progress.

---

## tasks.json

Structured task list.

Designed for future automation.

---

# Documentation

## docs/research

Peer-reviewed papers.

Academic publications.

White papers.

Research notes.

---

## docs/references

Documentation.

API references.

Manuals.

Datasheets.

External resources.

---

## docs/specifications

Design specifications.

Protocols.

Architecture documents.

Standards.

Interface definitions.

---

# Source

Contains all project source code.

Examples:

- Python
- C++
- Unreal Engine
- Arduino
- CAD scripts

---

# Assets

Stores non-source project resources.

## images

Photos.

Diagrams.

Screenshots.

---

## videos

Recordings.

Demonstrations.

Training footage.

---

## datasets

Training datasets.

Sensor recordings.

CSV files.

Point clouds.

---

# Experiments

Prototype implementations.

Algorithm testing.

Temporary investigations.

Experimental code should live here until promoted into source/.

---

# Exports

Generated output.

Reports.

PDFs.

PowerPoints.

Release builds.

Simulation exports.

---

# Archive

Historical material.

Deprecated code.

Superseded documentation.

Old project versions.

Nothing should be deleted without reason.

---

# AI Behavior

When Axiom creates or downloads information, it should automatically classify and store it according to this specification.

Examples:

Research paper
→ docs/research/

Generated report
→ exports/

New Python module
→ source/

Downloaded API documentation
→ docs/references/

Captured image
→ assets/images/

Prototype algorithm
→ experiments/

---

# Guiding Philosophy

Axiom is not simply an AI assistant.

Axiom is an engineering operating system.

Every project should remain understandable years after it was created.

A well-organized workspace reduces cognitive load, enables automation, and preserves engineering knowledge over time.

This specification exists to make every project predictable for both humans and AI.