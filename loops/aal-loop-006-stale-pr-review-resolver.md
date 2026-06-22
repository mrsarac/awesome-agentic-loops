---
id: AAL-LOOP-006
name: Stale PR Review Resolver
category: engineering
risk_level: code/external
approval_gate: push/external-message
max_iterations: 6
cost_guard: Bounded PR scope.
works_with:
  - Hermes
  - Claude Code
  - Codex
  - Cursor
status: draft
---

# AAL-LOOP-006 — Stale PR Review Resolver

## Use when
Review comments are stale or unresolved.

## Trigger
PR review comments pending.

## Action
Classify comments, apply minimal fixes, ask on ambiguous/product changes.

## Proof
Resolved comment list + tests/diff.

## Memory
PR thread.

## Stopping condition
Stop when all actionable comments are resolved or escalated.

## Failure modes
- Scope creep
- Agent self-certifies without proof
- Cost or iteration drift

## Example receipt
TBD.
