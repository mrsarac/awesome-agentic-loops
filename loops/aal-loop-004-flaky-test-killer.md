---
id: AAL-LOOP-004
name: Flaky Test Killer
category: engineering
use_when: Tests fail intermittently and the team needs evidence before changing product code or quarantining tests.
trigger: CI flake signal, local repeated failure, release blocker, or manual request to stabilize a specific test scope.
action: Reproduce the flake in a bounded loop, isolate likely causes, apply the smallest safe fix or quarantine proposal, and prove the result with repeated runs.
proof: Reproduction command, failure sample, hypothesis, patch/quarantine diff, repeated green run output, and remaining risk note.
memory: Test issue, PR note, or flaky-test registry; do not store raw logs unless they are minimized and linked.
stopping_condition: Stop after the target green streak, a minimized reproduction plus owner decision, or max attempts.
risk_level: code
approval_gate: commit/push, quarantine, broad refactor, CI config change
max_iterations: 10
cost_guard: Max 10 reproduce/fix loops or a timebox; stop early when confidence is high or ambiguity needs a human.
works_with:
  - Hermes
  - Claude Code
  - Codex
  - Cursor
failure_modes:
  - Mistaking infrastructure noise for a test bug
  - Hiding a real product bug by quarantining too quickly
  - Running unbounded test loops
  - Fixing unrelated code while chasing the flake
example_receipt: examples/aal-loop-004-flaky-test-killer-receipt.md
status: proof-grade
---

# AAL-LOOP-004 — Flaky Test Killer

## Purpose

Turn intermittent test failures into a decision with evidence: fix, quarantine, or escalate. The goal is not “make CI green at any cost”; it is to distinguish flaky tests from real defects without burning infinite agent cycles.

## Use when

- A test passes locally but fails in CI.
- CI shows intermittent red/green behavior.
- A release is blocked by suspected flakiness.
- The same test fails with timing, ordering, randomness, network, or environment symptoms.
- A team wants a quarantine decision backed by proof.

## Inputs

```yaml
test_scope: <file, test name, package, or CI job>
reproduce_command: <command>
max_attempts: 10
target_green_streak: 3
allowed_changes: test code and narrow product fix only
approval_gate: commit/push/quarantine/broad refactor/CI config
ci_context: <optional PR/check URL>
```

## Trigger

CI flake signal, local repeated failure, release blocker, or manual stabilization request.

## Action

1. State test scope, command, max attempts, and target green streak.
2. Run the test repeatedly until failure is reproduced or confidence threshold is met.
3. Capture minimized evidence: seed, timing, env, failing assertion, relevant logs.
4. Classify likely cause:
   - `ORDERING`
   - `TIME/TIMER`
   - `RANDOMNESS`
   - `NETWORK/IO`
   - `SHARED STATE`
   - `REAL BUG`
   - `INFRA`
5. Apply the smallest safe fix if cause is clear.
6. If not clear, propose quarantine or owner investigation with evidence.
7. Re-run enough times to prove the fix or stop at max attempts.
8. Produce a receipt.

## Proof requirements

A proof-grade run must include:

- exact reproduce command
- failure frequency or “not reproduced after N runs”
- failure sample / minimized log
- root-cause hypothesis and confidence
- diff summary if changed
- repeated green output or quarantine rationale
- final git status

Receipt template:

```markdown
# AAL-LOOP-004 Receipt — <test scope> — <date>

## Scope
- Test scope:
- Command:
- Max attempts:
- Target green streak:

## Reproduction
| Run | Result | Note |
|---|---|---|
| 1 | fail | timeout at ... |

## Diagnosis
- Classification:
- Hypothesis:
- Confidence:

## Action
- Patch/quarantine/proposal:
- Diff summary:

## Verification
```text
<repeated run output>
```

## Final state
- Green streak:
- Remaining risk:
- Stop reason:
```

## Memory

Persist a compact issue/PR note or flaky-test registry entry only if the flake remains relevant. Do not hoard full logs.

## Stopping condition

Stop when one of these is true:

- target green streak is reached,
- a minimized reproduction plus owner decision is produced,
- the flake is classified as infra and escalated,
- max attempts/timebox is reached.

## Approval gates

Requires explicit approval for:

- pushing code
- quarantining/skipping tests
- broad refactors
- CI runner/config changes
- dependency upgrades

## Failure modes

- “Green once” treated as proof.
- Quarantine used to hide a real bug.
- Unbounded reruns burn tokens/CI minutes.
- Fix touches broad product code without cause confidence.

## Example receipt

See [`examples/aal-loop-004-flaky-test-killer-receipt.md`](../examples/aal-loop-004-flaky-test-killer-receipt.md).
