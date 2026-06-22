---
id: AAL-LOOP-008
name: Cost Budget Watch Loop
category: finops
risk_level: read-only/billing
approval_gate: billing
max_iterations: 1
cost_guard: Read-only billing observation.
works_with:
  - Hermes
  - Claude Code
  - Codex
  - Cursor
status: draft
---

# AAL-LOOP-008 — Cost Budget Watch Loop

## Use when
Agent loops may burn budget.

## Trigger
Scheduled budget check or new automation.

## Action
Inspect cost/usage summaries and flag anomalies.

## Proof
Timestamped cost delta and threshold comparison.

## Memory
Budget note.

## Stopping condition
Stop after report; billing changes require approval.

## Failure modes
- Scope creep
- Agent self-certifies without proof
- Cost or iteration drift

## Example receipt
TBD.
