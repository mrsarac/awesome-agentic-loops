---
id: AAL-LOOP-005
name: PR CI Babysitter
category: engineering
risk_level: code/external
approval_gate: external-message/push
max_iterations: 6
cost_guard: No infinite CI polling.
works_with:
  - Hermes
  - Claude Code
  - Codex
  - Cursor
status: draft
---

# AAL-LOOP-005 — PR CI Babysitter

## Use when
A PR needs CI monitoring.

## Trigger
Open PR with pending/failing checks.

## Action
Poll checks, summarize failures, attempt bounded fixes if approved.

## Proof
gh checks output + commit/patch summary or blocker.

## Memory
PR comment/status note.

## Stopping condition
Stop when checks pass, blocked, or max attempts hit.

## Failure modes
- Scope creep
- Agent self-certifies without proof
- Cost or iteration drift

## Example receipt
TBD.
