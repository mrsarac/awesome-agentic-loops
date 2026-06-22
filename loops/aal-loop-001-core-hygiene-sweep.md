---
id: AAL-LOOP-001
name: Core Hygiene Sweep
category: operations
use_when: Source-of-truth docs may have drifted after a milestone, agent handoff, cron result, or strategy change.
trigger: Manual request, milestone closeout, scheduled hygiene scan, or before a public/shareable summary is produced.
action: Inspect a bounded set of source-of-truth files, identify contradictions or stale pointers, patch only narrow docs drift, and leave risky changes as owner-tagged next actions.
proof: File list inspected, exact findings, unified diff or explicit no-drift statement, validation command output, and final git status.
memory: Source-of-truth docs and project manifests only; do not store raw transcripts, temporary TODO state, or stale artifact IDs as memory.
stopping_condition: Stop after one bounded pass or when every contradiction has either a patch, an owner, or a deliberate defer decision.
risk_level: docs
approval_gate: commit/push or any broad rewrite
max_iterations: 1
cost_guard: One bounded run; no open-ended repo archaeology unless a contradiction requires it.
works_with:
  - Hermes
  - Claude Code
  - Codex
  - Cursor
failure_modes:
  - Scope creep from hygiene into strategy rewrite
  - Agent self-certifies without a diff or no-drift receipt
  - Updating README but forgetting project manifests or linked docs
  - Treating old cron/session output as current truth
example_receipt: examples/aal-loop-001-core-hygiene-sweep-receipt.md
status: proof-grade
---

# AAL-LOOP-001 — Core Hygiene Sweep

## Purpose

Keep the operational source of truth coherent. This loop is for the boring but valuable work: finding drift between README, project manifests, status docs, ledger files, and agent reports before the drift becomes bad decisions.

A good run is not a giant cleanup. A good run is a bounded inspection with proof.

## Use when

- A milestone changed project truth.
- An agent/cron report says something is active, paused, blocked, or completed.
- A dashboard, README, manifest, or status page may disagree.
- A public/shareable update depends on local source-of-truth accuracy.
- A previous assistant likely forgot the “README every milestone” rule.

## Inputs

Minimum input packet:

```yaml
scope_name: <project or workspace>
files_to_check:
  - README.md
  - projects/<slug>.md
  - docs/<relevant-status>.md
  - docs/<relevant-dashboard>.html
recent_evidence:
  - <commit, cron output, report path, issue, PR, or human decision>
allowed_changes: docs-only
approval_gate: commit/push/broad rewrite
```

## Trigger

Manual request, milestone closeout, scheduled hygiene scan, or pre-publication check.

## Action

1. Print the exact scope: files, evidence, and what is out of scope.
2. Read the bounded files; do not search the whole disk unless a missing pointer requires it.
3. Compare claims across files:
   - project status
   - steward/owner
   - cadence/cron/job ID
   - current URL/path
   - active vs parked/removed status
   - next action / approval gate
4. Classify each finding:
   - `PATCH` — narrow docs correction is safe
   - `OWNER` — needs a person/agent decision
   - `DEFER` — true but not worth changing now
   - `NO-DRIFT` — checked and consistent
5. Patch only narrow docs drift.
6. Validate syntax/links where practical.
7. End with a receipt.

## Proof requirements

A proof-grade run must include:

- timestamp and repo/path
- exact file list inspected
- findings table with `PATCH/OWNER/DEFER/NO-DRIFT`
- diff or explicit no-drift statement
- validation commands and real output
- final git status
- next owner/action if anything remains

Receipt template:

```markdown
# AAL-LOOP-001 Receipt — <scope> — <date>

## Scope
- Repo/path:
- Files inspected:
- Evidence used:

## Findings
| ID | Class | Finding | Action |
|---|---|---|---|
| F1 | PATCH | ... | ... |

## Verification
```text
<commands and output>
```

## Final state
- Git status:
- Remaining owner decisions:
- Stop reason:
```

## Memory

Write durable truth only to source-of-truth docs and project manifests. Do not save temporary run details as long-term memory unless they are stable operational facts.

## Stopping condition

Stop after one bounded pass or when every contradiction has either:

- a patch,
- an owner-tagged next action,
- or an explicit defer decision.

## Approval gates

Requires explicit approval for:

- commit/push if not already authorized
- broad README/manifest rewrite
- deleting or archiving project truth
- changing cron/service/provider configuration
- external publication or messages

## Failure modes

- Turning hygiene into strategy rewrite.
- Reading too much and patching too broadly.
- Updating README but not the manifest/dashboard.
- Treating stale cron/session output as live truth.
- Saying “looks fine” without file list and validation.

## Example receipt

See [`examples/aal-loop-001-core-hygiene-sweep-receipt.md`](../examples/aal-loop-001-core-hygiene-sweep-receipt.md).
