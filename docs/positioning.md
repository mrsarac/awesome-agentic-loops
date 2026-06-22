# Agentic Loop Atlas — Positioning

## One-line positioning

A proof-oriented registry of reusable AI-agent operating loops: each loop defines its trigger, action, proof, memory, stopping condition, risk gate, and receipt shape.

## What it is

Agentic Loop Atlas is for people building with Claude Code, Codex, Cursor, Hermes, OpenCode, and durable runtimes who need repeatable agent workflows that do not spiral into unattended chaos.

It treats a loop as an operational unit, not a prompt:

```text
trigger → bounded action → proof → memory → stop / next decision
```

## What it is not

- Not a prompt dump.
- Not a list of vibes like “make the agent autonomous”.
- Not a license to run unattended production mutations.
- Not a replacement for CI, observability, review, or human approval.

## Audience

Primary:
- founders and solo builders using coding agents daily
- AI engineering teams formalizing agent workflows
- ops-minded developers who care about receipts, rollback, and cost

Secondary:
- researchers studying agentic systems
- devtools builders designing agent orchestration products
- technical writers documenting agent workflows

## Core promise

If a loop is in the atlas, a practitioner should be able to answer:

1. When should this loop run?
2. What is it allowed to do?
3. What counts as proof?
4. What memory/state should persist?
5. When does it stop?
6. What needs human approval?
7. What can go wrong?

## Differentiation

Most “awesome agent” lists collect tools. Agentic Loop Atlas collects operating patterns.

| Common list | Agentic Loop Atlas |
|---|---|
| Tools and links | Reusable operating loops |
| Prompt snippets | Trigger/action/proof/memory/stop/risk cards |
| “Autonomous” claims | Approval gates and receipts |
| Broad inspiration | Bounded runnable patterns |
| No stop condition | Stop condition required |

## Launch wedge

Start with ten practical loops builders already need:

1. Core Hygiene Sweep
2. Docs/README Milestone Sweep
3. Production Error Sweep
4. Flaky Test Killer
5. PR CI Babysitter
6. Stale PR Review Resolver
7. Security Headers / OWASP Sweep
8. Cost Budget Watch Loop
9. Research-to-Public-Artifact Loop
10. Agent Mesh Health Loop

The first three are proof-grade in the seed release; the rest can mature from draft to proof-grade as receipts accumulate.

## Voice

Calm, practical, anti-hype.

Useful sentence:

> Motion is not progress; proof is.

## Submission standard

A contributed loop must include:

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
