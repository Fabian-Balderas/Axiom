# Axiom Plugin Specification v1.0

> "Everything is a plugin unless it belongs in the Core."

---

# Purpose

This document defines how Skills and Plugins interact with Axiom.

The objective is to allow unlimited expansion without modifying the Core.

Plugins are first-class citizens.

---

# Philosophy

Core handles infrastructure.

Plugins provide capabilities.

The Core should know as little as possible about each plugin.

---

# Plugin Lifecycle

Discovery

↓

Validation

↓

Registration

↓

Initialization

↓

Execution

↓

Shutdown

↓

Unload

---

# Plugin Structure

plugins/

    geometry/

        plugin.py

        manifest.json

        README.md

        requirements.txt

        tests/

    vision/

    robotics/

    strudel/

Every plugin is self-contained.

---

# Required Files

plugin.py

Entry point.

manifest.json

Metadata.

README.md

Documentation.

tests/

Unit tests.

requirements.txt

Dependencies (optional).

---

# Manifest Example

{
    "name": "Geometry",

    "version": "1.0.0",

    "author": "Fabian",

    "description": "Geometry reasoning engine",

    "api": "1.0",

    "entry": "plugin.py",

    "dependencies": []
}

---

# Plugin Interface

Every plugin must implement:

initialize()

shutdown()

execute()

status()

metadata()

health()

---

# Responsibilities

A plugin is responsible for

its own memory

its own configuration

its own dependencies

its own tests

its own documentation

---

# Communication

Plugins never communicate directly.

Plugin A

↓

Core API

↓

Plugin B

Never

Plugin A

↓

Plugin B

---

# Registration

Plugins register capabilities.

Example

"geometry.solve"

"vision.detect"

"robotics.plan"

"music.generate"

The Reasoning Engine discovers capabilities dynamically.

---

# Configuration

Every plugin stores configuration inside

config/

No hardcoded values.

---

# Logging

Plugins use Core logging.

Never print().

---

# Error Handling

Plugins never crash Core.

Errors are isolated.

Core reports failure.

System continues running.

---

# Security

Plugins run with least privilege.

Never access:

memory directly

other plugin data

core internals

without permission.

---

# Versioning

Semantic Versioning.

Major

Breaking

Minor

Features

Patch

Fixes

---

# Testing

Every plugin must include

unit tests

sample data

example usage

---

# Documentation

Every plugin includes

Purpose

Capabilities

Inputs

Outputs

Examples

Dependencies

Limitations

---

# Dependency Rules

Plugins may depend on

Core

Standard Library

Approved Packages

Plugins may not depend on

Other plugins

---

# Resource Management

Plugins must

close files

release memory

stop threads

cleanup GPU resources

---

# Health Checks

Every plugin reports

Loaded

Ready

Busy

Error

Disabled

---

# Future Plugin Categories

Engineering

Geometry

Physics

Programming

Vision

Music

CAD

Simulation

Networking

Robotics

Algorithms

Aviation

Research

Automation

Mathematics

Learning

---

# Success Criteria

A new plugin should require

one folder

one manifest

one registration

zero Core modifications
One idea I'd add that I haven't seen in many plugin systems
Capability-Based Discovery

Instead of asking for a specific plugin:

use_plugin("geometry")

the Reasoning Engine asks:

find_capability("convex_hull")

The plugin manager responds:

Geometry Plugin

confidence: 1.0

loaded: yes

or

Geometry Plugin

loaded: no

Loading...

The Reasoning Engine doesn't care which plugin provides the capability. It only cares that someone can do the job.

That means if you later write a better geometry plugin, Axiom doesn't need to change. It simply discovers the new capability provider.

Even bigger...

This naturally leads to a Skill Marketplace—not a public app store, but your own personal library of capabilities.

Imagine opening Axiom and seeing:

Installed Skills
────────────────────────────

✓ Geometry

✓ Physics

✓ Git

✓ Python

✓ Computer Vision

✓ CAD

✓ Unreal Engine

✓ Strudel

○ Robotics (not installed)

○ CFD Simulation

○ PCB Design

○ Drone Navigation

Installing a new capability becomes as simple as dropping a folder into the plugins/ directory and restarting Axiom.