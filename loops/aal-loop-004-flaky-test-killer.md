---
id: AAL-LOOP-004
name: Flaky Test Killer
category: engineering
risk_level: code
approval_gate: push
max_iterations: 10
cost_guard: Max iterations and token budget.
works_with:
  - Hermes
  - Claude Code
  - Codex
  - Cursor
status: draft
---

# AAL-LOOP-004 — Flaky Test Killer

## Use when
Tests fail intermittently.

## Trigger
Manual request or CI flake signal.

## Action
Run tests repeatedly, isolate flaky cases, fix or quarantine with evidence.

## Proof
Consecutive green runs or quarantined issue with reproduction.

## Memory
Test notes/issue/PR.

## Stopping condition
Stop after target green streak or max attempts.

## Failure modes
- Scope creep
- Agent self-certifies without proof
- Cost or iteration drift

## Example receipt
TBD.
