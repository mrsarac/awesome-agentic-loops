---
id: AAL-LOOP-003
name: Production Error Sweep
category: operations
risk_level: read-only/service
approval_gate: restart/deploy
max_iterations: 1
cost_guard: Read-only scan only.
works_with:
  - Hermes
  - Claude Code
  - Codex
  - Cursor
status: draft
---

# AAL-LOOP-003 — Production Error Sweep

## Use when
You need operational health without touching services.

## Trigger
Manual or scheduled health check.

## Action
Inspect allowed status pages, logs, or endpoints and classify findings.

## Proof
Timestamped report with checked source and severity.

## Memory
Project risk/next-action record.

## Stopping condition
Stop after report; do not restart/deploy without approval.

## Failure modes
- Scope creep
- Agent self-certifies without proof
- Cost or iteration drift

## Example receipt
TBD.
