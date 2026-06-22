---
id: AAL-LOOP-007
name: Security Headers OWASP Sweep
category: security
risk_level: code/service
approval_gate: deploy/restart
max_iterations: 5
cost_guard: No credential or prod mutation without approval.
works_with:
  - Hermes
  - Claude Code
  - Codex
  - Cursor
status: draft
---

# AAL-LOOP-007 — Security Headers OWASP Sweep

## Use when
Security posture needs bounded audit.

## Trigger
Manual audit request or release hardening.

## Action
Check headers/OWASP findings, propose or apply minimal fixes if approved.

## Proof
Scanner/curl evidence before/after.

## Memory
Security report/issue.

## Stopping condition
Stop when critical/high findings are fixed or explicitly owned.

## Failure modes
- Scope creep
- Agent self-certifies without proof
- Cost or iteration drift

## Example receipt
TBD.
