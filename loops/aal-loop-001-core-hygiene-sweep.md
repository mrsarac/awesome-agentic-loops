---
id: AAL-LOOP-001
name: Core Hygiene Sweep
category: operations
risk_level: docs
approval_gate: push
max_iterations: 1
cost_guard: One bounded run.
works_with:
  - Hermes
  - Claude Code
  - Codex
  - Cursor
status: draft
---

# AAL-LOOP-001 — Core Hygiene Sweep

## Use when
Source-of-truth docs may have drifted.

## Trigger
Manual request, milestone, or scheduled hygiene scan.

## Action
Inspect bounded source-of-truth files and detect contradictions.

## Proof
Narrow diff, no-drift report, or owner/next-action list.

## Memory
Source-of-truth docs only.

## Stopping condition
Stop after one bounded pass or when all contradictions have owners.

## Failure modes
- Scope creep
- Agent self-certifies without proof
- Cost or iteration drift

## Example receipt
TBD.
