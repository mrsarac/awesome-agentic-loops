---
id: AAL-LOOP-010
name: Agent Mesh Health Loop
category: operations
risk_level: read-only
approval_gate: restart
max_iterations: 1
cost_guard: Read-only mesh check.
works_with:
  - Hermes
  - Claude Code
  - Codex
  - Cursor
status: draft
---

# AAL-LOOP-010 — Agent Mesh Health Loop

## Use when
Multi-agent mesh health is uncertain.

## Trigger
Before delegation or scheduled ops check.

## Action
Verify reachability, gateway status, cron warnings, route fallbacks.

## Proof
Green/yellow/red report with exact blocker.

## Memory
Infra docs only if route truth changed.

## Stopping condition
Stop after reporting; no restarts unless approved.

## Failure modes
- Scope creep
- Agent self-certifies without proof
- Cost or iteration drift

## Example receipt
TBD.
