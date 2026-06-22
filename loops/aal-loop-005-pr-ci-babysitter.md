---
id: AAL-LOOP-005
name: PR CI Babysitter
category: engineering
use_when: A pull request has pending or failing checks and needs bounded monitoring, diagnosis, and safe next actions.
trigger: Open PR with pending/failing checks, post-push check cycle, merge readiness review, or user asks to watch a PR.
action: Poll CI a bounded number of times, summarize check status, inspect failing logs, apply only approved/narrow fixes, and stop with a merge/blocker decision.
proof: PR URL, check run output, failing log excerpt, patch/commit summary if any, final check state, and next action.
memory: PR comment/status note and issue/decision log only; avoid persisting raw CI logs.
stopping_condition: Stop when checks pass, failure is classified with owner/action, approval is needed, or polling limit is reached.
risk_level: code/external
approval_gate: push, merge, external comment, workflow rerun, deploy
max_iterations: 6
cost_guard: Max 6 polling/diagnosis cycles; no infinite waiting.
works_with:
  - Hermes
  - Claude Code
  - Codex
  - Cursor
failure_modes:
  - Polling forever
  - Reporting stale CI state
  - Pushing speculative fixes without diagnosis
  - Commenting externally without approval
example_receipt: examples/aal-loop-005-pr-ci-babysitter-receipt.md
status: proof-grade
---

# AAL-LOOP-005 — PR CI Babysitter

## Purpose

Monitor and diagnose PR checks without becoming an unattended merge bot. The loop turns CI state into a clear decision: pass, fix, wait, or escalate.

## Use when

- A PR has pending checks.
- A check failed and needs log triage.
- A push just happened and CI needs a bounded watch window.
- A PR is near merge but needs evidence.
- The user wants a concise “what is blocking this PR?” answer.

## Inputs

```yaml
repo: <owner/name>
pr_number: <number>
max_poll_cycles: 6
poll_interval_seconds: 30
allowed_changes: none | narrow fix with approval
approval_gate: push/merge/comment/workflow-rerun/deploy
required_checks: <optional list>
```

## Trigger

Open PR with pending/failing checks, post-push check cycle, or manual PR watch request.

## Action

1. Capture PR URL, branch, head SHA, and current check state.
2. Poll checks up to the configured limit.
3. If a check fails, inspect the relevant log excerpt only.
4. Classify failure:
   - `TEST`
   - `LINT/FORMAT`
   - `TYPECHECK`
   - `BUILD`
   - `INFRA/RUNNER`
   - `SECRET/CONFIG`
   - `FLAKE`
5. If allowed and narrow, propose or apply a fix; otherwise produce a blocker packet.
6. Do not merge, rerun workflows, push, or comment externally unless approved.
7. End with final state and next action.

## Proof requirements

A proof-grade run must include:

- PR URL and head SHA
- check names and statuses
- timestamps for poll cycles
- failing log excerpt or no-failure statement
- classification and confidence
- diff/commit summary if any
- final check state

Receipt template:

```markdown
# AAL-LOOP-005 Receipt — PR <number> — <date>

## Scope
- Repo:
- PR:
- Head SHA:
- Poll limit:

## Checks
| Check | State | Evidence |
|---|---|---|
| tests | failed | log excerpt ... |

## Diagnosis
- Classification:
- Confidence:
- Suggested action:

## Actions taken
- None / patch / commit:

## Final state
- Checks:
- Merge-ready: yes/no
- Approval needed:
- Stop reason:
```

## Memory

Keep durable state in the PR thread, issue, or decision log. Do not save raw CI logs as long-term memory.

## Stopping condition

Stop when:

- all required checks pass,
- a blocker is classified with owner/action,
- approval is needed for push/rerun/comment/merge,
- or polling limit is reached.

## Approval gates

Requires explicit approval for:

- pushing commits
- rerunning workflows if it consumes quota or masks flake
- merge/squash/rebase
- external PR comment
- deploy/release after merge

## Failure modes

- Stale CI reported as current.
- Infinite polling.
- Fix without log evidence.
- External comment posted before human approval.

## Example receipt

See [`examples/aal-loop-005-pr-ci-babysitter-receipt.md`](../examples/aal-loop-005-pr-ci-babysitter-receipt.md).
