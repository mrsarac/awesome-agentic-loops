---
id: AAL-LOOP-009
name: Research to Public Artifact Loop
category: research
risk_level: external
approval_gate: external-message
max_iterations: 1
cost_guard: No public write.
works_with:
  - Hermes
  - Claude Code
  - Codex
  - Cursor
status: draft
---

# AAL-LOOP-009 — Research to Public Artifact Loop

## Use when
A research insight might become public artifact.

## Trigger
Research report or market delta.

## Action
Distill sources into draft artifact and QA risk before publication.

## Proof
Source map + draft + approval checklist.

## Memory
Draft queue.

## Stopping condition
Stop at draft package; do not publish without approval.

## Failure modes
- Scope creep
- Agent self-certifies without proof
- Cost or iteration drift

## Example receipt
TBD.
