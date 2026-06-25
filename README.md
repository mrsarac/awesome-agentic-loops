# Awesome Agentic Loops — Agentic Loop Atlas

[![Validate Atlas](https://github.com/mrsarac/awesome-agentic-loops/actions/workflows/validate.yml/badge.svg)](https://github.com/mrsarac/awesome-agentic-loops/actions/workflows/validate.yml)
[![Status: proof-grade seed](https://img.shields.io/badge/status-proof--grade%20seed-22c55e)](#initial-loop-set)
[![Loops: 11](https://img.shields.io/badge/loops-11-67e8f9)](catalog.json)
[![License: MIT](https://img.shields.io/badge/license-MIT-a78bfa)](LICENSE)
[![Contributions: receipts welcome](https://img.shields.io/badge/contributions-receipts%20welcome-fbbf24)](CONTRIBUTING.md)

> A proof-oriented registry of reusable AI-agent operating loops: triggers, actions, verification, memory, stopping conditions, risk gates, and receipts for Claude Code, Codex, Cursor, Hermes, OpenCode, and durable runtimes.

**Motion is not progress; proof is.**

This is not another prompt dump. A loop only belongs here when it has:

- a clear **trigger**
- a bounded **action**
- concrete **proof**
- durable **memory/state guidance**
- a falsifiable **stopping condition**
- explicit **risk and approval gates**
- at least one runnable example or receipt shape

- [GitHub repository](https://github.com/mrsarac/awesome-agentic-loops)

## Why this exists

Agentic loops are moving from hype to operating discipline. The useful question is no longer “what prompt should I type?” but:

> What system prompts the agent, checks the result, remembers the state, and knows when to stop?

Most awesome-agent lists collect tools. Agentic Loop Atlas collects **operating patterns**.

| Common list | Agentic Loop Atlas |
|---|---|
| Tools and links | Reusable operating loops |
| Prompt snippets | Trigger/action/proof/memory/stop/risk cards |
| “Autonomous” claims | Approval gates and receipts |
| Broad inspiration | Bounded runnable patterns |
| No stop condition | Stop condition required |

## Quick start

1. Pick a loop from [`loops/`](loops/).
2. Check its `risk_level` and `approval_gate`.
3. Adapt the commands to your agent/runtime.
4. Run **one bounded iteration**.
5. Keep the receipt; do not trust vibes.

## Loop card schema

Every loop follows [`schemas/loop-card.schema.json`](schemas/loop-card.schema.json) and this shape:

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
example_receipt: examples/aal-loop-001-core-hygiene-sweep-receipt.md
status: proof-grade
```

## Initial loop set

| ID | Loop | Category | Risk | Status |
|---|---|---|---|---|
| AAL-LOOP-001 | [Core Hygiene Sweep](loops/aal-loop-001-core-hygiene-sweep.md) | Operations | docs | proof-grade |
| AAL-LOOP-002 | [Docs/README Milestone Sweep](loops/aal-loop-002-docs-readme-milestone-sweep.md) | Documentation | docs | proof-grade |
| AAL-LOOP-003 | [Production Error Sweep](loops/aal-loop-003-production-error-sweep.md) | Operations | read-only/service | proof-grade |
| AAL-LOOP-004 | [Flaky Test Killer](loops/aal-loop-004-flaky-test-killer.md) | Engineering | code | proof-grade |
| AAL-LOOP-005 | [PR CI Babysitter](loops/aal-loop-005-pr-ci-babysitter.md) | Engineering | code/external | proof-grade |
| AAL-LOOP-006 | [Stale PR Review Resolver](loops/aal-loop-006-stale-pr-review-resolver.md) | Engineering | code/external | proof-grade |
| AAL-LOOP-007 | [Security Headers / OWASP Sweep](loops/aal-loop-007-security-headers-owasp-sweep.md) | Security | code/service | proof-grade |
| AAL-LOOP-008 | [Cost Budget Watch Loop](loops/aal-loop-008-cost-budget-watch-loop.md) | FinOps | read-only/billing | proof-grade |
| AAL-LOOP-009 | [Research-to-Public-Artifact Loop](loops/aal-loop-009-research-to-public-artifact-loop.md) | Research | external | proof-grade |
| AAL-LOOP-010 | [Agent Mesh Health Loop](loops/aal-loop-010-agent-mesh-health-loop.md) | Operations | read-only | proof-grade |
| AAL-LOOP-011 | [Competitor Delta Proof Loop](loops/aal-loop-011-competitor-delta-proof-loop.md) | Research | read-only/external-signal | proof-grade |

## Repository map

```text
.github/                     Issue and PR templates
LICENSE                      MIT license
SECURITY.md                  Security and redaction policy
ROADMAP.md                   Project roadmap
catalog.json                 Machine-readable catalog
llms.txt                     Agent-readable guide
docs/announcement-draft.md   Public announcement draft, not posted
docs/positioning.md          Public positioning and contribution standard
schemas/loop-card.schema.json JSON Schema for loop cards
loops/                       Canonical loop cards
examples/                    Receipts and real-world proof examples
docs/                        Taxonomy, platform matrix, launch notes
```

## Guardrails

- No loop is accepted without proof and stopping condition.
- Destructive, credential, deploy, billing, and external-message actions need explicit human approval.
- “Run while you sleep” is not a strategy. It is a liability unless proof, cost, and rollback exist.
- The agent that created the output should not be the only judge of the output.

## Contributing

Start with [`CONTRIBUTING.md`](CONTRIBUTING.md) or the GitHub issue templates. The highest-value contributions are real receipts from agent runs.

- loop card metadata
- use case and trigger
- bounded action
- proof requirements
- memory/state guidance
- stopping condition
- approval gates
- failure modes
- example receipt or receipt template

If it lacks proof or a stop condition, it is not ready.

## Status

Seeded from `LOOP-MKT-20260622` research and Mustafa Saraç's Agentic Project Mesh proof pattern. First eleven loop cards are proof-grade seed patterns with receipt examples.
