# Awesome Agentic Loops — Agentic Loop Atlas

> A proof-oriented registry of reusable AI-agent loops: triggers, actions, verification, memory, stopping conditions, risk gates, and runnable recipes for Claude Code, Codex, Cursor, Hermes, OpenCode, and durable runtimes.

This is not another prompt dump. A loop only belongs here when it has:

- a clear **trigger**
- a bounded **action**
- concrete **proof**
- durable **memory**
- a falsifiable **stopping condition**
- explicit **risk and approval gates**
- at least one runnable example or receipt shape

## Why this exists

Agentic loops are moving from hype to operating discipline. The useful question is no longer “what prompt should I type?” but:

> What system prompts the agent, checks the result, remembers the state, and knows when to stop?

## Quick start

1. Pick a loop from `loops/`.
2. Check its `risk_level` and `approval_gate`.
3. Adapt the tool commands to your agent/runtime.
4. Run one bounded iteration.
5. Keep the receipt; do not trust vibes.

## Loop card schema

Every loop follows `schemas/loop-card.schema.json` and this shape:

```yaml
id: AAL-LOOP-001
name: Core Hygiene Sweep
category: operations
use_when: Source-of-truth docs may have drifted.
trigger: Manual request, milestone, or scheduled hygiene scan.
action: Inspect bounded files and detect contradictions.
proof: Diff, no-drift report, or issue list with owners.
memory: Source-of-truth docs only; no raw transcript hoarding.
stopping_condition: Stop after one bounded pass or when all contradictions have owners.
risk_level: docs
approval_gate: push
max_iterations: 1
cost_guard: one bounded run
works_with: [Hermes, Claude Code, Codex, Cursor]
failure_modes: [scope creep, stale context, accidental broad rewrite]
example_receipt: examples/apm-loop-001-core-hygiene-sweep.md
```

## Initial loop set

| ID | Loop | Category | Risk | Status |
|---|---|---|---|---|
| AAL-LOOP-001 | Core Hygiene Sweep | Operations | docs | draft |
| AAL-LOOP-002 | Docs/README Milestone Sweep | Documentation | docs | draft |
| AAL-LOOP-003 | Production Error Sweep | Operations | read-only/service | draft |
| AAL-LOOP-004 | Flaky Test Killer | Engineering | code | draft |
| AAL-LOOP-005 | PR CI Babysitter | Engineering | code/external | draft |
| AAL-LOOP-006 | Stale PR Review Resolver | Engineering | code/external | draft |
| AAL-LOOP-007 | Security Headers / OWASP Sweep | Security | code/service | draft |
| AAL-LOOP-008 | Cost Budget Watch Loop | FinOps | read-only/billing | draft |
| AAL-LOOP-009 | Research-to-Public-Artifact Loop | Research | external | draft |
| AAL-LOOP-010 | Agent Mesh Health Loop | Operations | read-only | draft |

## Repository map

```text
catalog.json                  Machine-readable catalog
llms.txt                      Agent-readable guide
schemas/loop-card.schema.json JSON Schema for loop cards
loops/                        Canonical loop cards
examples/                     Receipts and real-world proof examples
docs/                         Taxonomy, platform matrix, launch notes
```

## Guardrails

- No loop is accepted without proof and stopping condition.
- Destructive, credential, deploy, billing, and external-message actions need explicit human approval.
- “Run while you sleep” is not a strategy. It is a liability unless proof, cost, and rollback exist.
- The agent that created the output should not be the only judge of the output.

## Status

Seeded from LOOP-MKT-20260622 research and APM-LOOP-001 proof pattern.
