---
id: AAL-LOOP-002
name: Docs README Milestone Sweep
category: documentation
risk_level: docs
approval_gate: push
max_iterations: 1
cost_guard: One docs pass.
works_with:
  - Hermes
  - Claude Code
  - Codex
  - Cursor
status: draft
---

# AAL-LOOP-002 — Docs README Milestone Sweep

## Use when
A milestone changed project truth.

## Trigger
Project milestone, new repo/profile/agent, or completed release.

## Action
Patch README pointer and related manifest without archiving everything.

## Proof
Diff shows new truth is findable from README and manifest.

## Memory
README + manifest.

## Stopping condition
Stop when milestone is findable and stale wording is resolved.

## Failure modes
- Scope creep
- Agent self-certifies without proof
- Cost or iteration drift

## Example receipt
TBD.
