# Axiom Coding Standards v1.0

> "Write code for the future engineer."

---

# Philosophy

Code is written once.

Read thousands of times.

Optimize for readability before cleverness.

---

# General Principles

## Clarity over Cleverness

Write code that is immediately understandable.

Avoid unnecessary complexity.

If something requires a paragraph to explain,
rewrite it.

---

## Simplicity

Simple systems scale.

Complex systems fail.

Always choose the simplest solution that solves the problem.

---

## Modularity

Every module has one responsibility.

No file should become a dumping ground.

---

## Documentation

Every public class and function should explain:

- what it does
- inputs
- outputs
- possible errors

---

# Naming

Variables

Good

user_memory

project_manager

camera_position

Avoid

x

temp

data2

stuff

---

Functions

Use verbs.

Good

load_memory()

calculate_path()

search_projects()

Avoid

memory()

path()

thing()

---

Classes

Use nouns.

MemoryManager

PluginLoader

ConversationEngine

ReasoningEngine

---

Constants

UPPER_CASE

MAX_CONTEXT_LENGTH

DEFAULT_PORT

---

Formatting

4 spaces

UTF-8

One statement per line

Maximum line length

100 characters

---

Functions

Functions should generally remain under 50 lines.

If longer—

split them.

---

Comments

Write comments explaining

WHY

not

WHAT

Bad

i += 1

Good

Advance to the next conversation turn.

---

Logging

Never use print()

Always use logging.

Example

logger.info()

logger.warning()

logger.error()

---

Error Handling

Never silently ignore errors.

Bad

try:
    ...
except:
    pass

Good

try:
    ...
except Exception as e:
    logger.exception(e)

---

Configuration

Never hardcode

API keys

Paths

Ports

Model names

Store them in configuration.

---

Testing

Every module should include tests.

If code cannot be tested,

reconsider the design.

---

Dependencies

Prefer standard library.

Add third-party packages only when justified.

Minimize dependency count.

---

Performance

Do not optimize prematurely.

Measure first.

Optimize where necessary.

---

Security

Never execute unknown code.

Never expose secrets.

Validate inputs.

Escape outputs where required.

---

Version Control

Commit often.

Every commit should build.

Write meaningful commit messages.

Good

Added memory indexing

Bad

stuff

---

Architecture

Core never imports Skills.

Skills never modify Core.

Plugins communicate through interfaces.

---

Documentation

Every major module requires

README

Examples

API reference

---

Code Reviews

Before merging ask

Is this simpler?

Is this reusable?

Will this make sense in one year?

---

Definition of Done

A feature is complete only if:

✓ Code works

✓ Tests pass

✓ Documentation updated

✓ Logging added

✓ Errors handled

✓ No TODOs

✓ No warnings

✓ Architecture respected


One addition I'd make that's specific to Axiom
The 10-Minute Rule

If either of us returns to a file after six months, we should be able to understand its purpose within ten minutes.

That means:

descriptive names,
concise functions,
clear module boundaries,
and comments that explain intent rather than restating the code.
Another rule I'd add
No Magic

If you see a value like:

threshold = 0.83

someone should immediately know why it's 0.83.

Either:

SIMILARITY_THRESHOLD = 0.83

or

# Chosen empirically after benchmarking textbook retrieval.
SIMILARITY_THRESHOLD = 0.83

The goal is to eliminate unexplained constants and hidden assumptions.

And finally, the principle I think will shape Axiom more than any other

Every line of code should either make Axiom easier to understand, easier to extend, or easier to trust.

If it doesn't improve at least one of those qualities, it's worth asking whether it belongs.