---
id: AAL-LOOP-002
name: Docs README Milestone Sweep
category: documentation
use_when: A milestone, release, agent activation, repo creation, deployment, or strategic decision changed project truth and must be findable later.
trigger: Milestone completion, release note, project status change, new dashboard, new repo/profile/agent, or Patron reminder that README/source-of-truth must be updated.
action: Patch README and exactly related source-of-truth files so the new truth is discoverable in one click; avoid dumping historical detail into the README.
proof: Diff proves the milestone is findable from README plus its canonical manifest/status doc; validation confirms markdown/HTML/JSON stayed parseable.
memory: README, project manifest, canonical status doc, and timeline/activity log when history must be preserved.
stopping_condition: Stop when the milestone is discoverable, stale wording is removed or owner-tagged, and no unrelated docs were rewritten.
risk_level: docs
approval_gate: commit/push, deletion, broad reorganization, or publication
max_iterations: 1
cost_guard: One docs pass; move history to timeline/activity-log instead of expanding scope.
works_with:
  - Hermes
  - Claude Code
  - Codex
  - Cursor
failure_modes:
  - README bloat from archiving every detail
  - Milestone recorded in README but not manifest/status doc
  - Dashboard updated but source-of-truth pointer forgotten
  - Stale “active” wording left behind
example_receipt: examples/aal-loop-002-docs-readme-milestone-sweep-receipt.md
status: proof-grade
---

# AAL-LOOP-002 — Docs README Milestone Sweep

## Purpose

Make new project truth findable without turning the README into a landfill. This loop is for milestone closeout: when something becomes active, shipped, paused, hardened, moved, or parked, update the source-of-truth pointers and stop.

## Use when

- A project milestone completed.
- A repo, profile, dashboard, cron, bot, or agent lane was created.
- A deployment/public URL changed.
- A previously active thing was paused or removed.
- A human explicitly says “README unutma”.
- You need to turn a session result into durable source-of-truth.

## Inputs

```yaml
milestone_code: <short code>
changed_truth: <one-sentence operational truth>
primary_pointer: <README section or dashboard>
canonical_docs:
  - README.md
  - projects/<slug>.md
  - docs/<status-or-plan>.md
  - docs/<dashboard>.html
history_destination: docs/timeline.md or docs/activity-log.md
allowed_changes: docs-only
```

## Trigger

Milestone completion, release note, agent activation, project status change, or explicit source-of-truth refresh request.

## Action

1. State the milestone and the exact truth that changed.
2. Inspect current README and canonical docs.
3. Decide where the truth belongs:
   - README = current navigational truth and critical decision surface
   - manifest/status doc = operational details
   - timeline/activity log = historical detail
4. Patch only the necessary files.
5. Remove or owner-tag contradictory stale wording.
6. Validate changed file formats.
7. Produce a receipt with paths, diff summary, and final status.

## Proof requirements

A proof-grade run must include:

- milestone code and timestamp
- before/after claim summary
- list of docs patched
- diff summary
- validation output
- final git status
- explicit “history stored / history intentionally omitted” note

Receipt template:

```markdown
# AAL-LOOP-002 Receipt — <milestone> — <date>

## Changed truth
Before:
After:

## Files patched
- README.md — <why>
- projects/<slug>.md — <why>

## Verification
```text
<markdown/html/json parse/build output>
```

## Final state
- Findable from README: yes/no
- Canonical detail doc:
- History destination:
- Stop reason:
```

## Memory

Write to source-of-truth docs. Use persistent memory only for stable preferences or environment facts, not milestone logs or commit IDs.

## Stopping condition

Stop when:

- the milestone is findable from README,
- canonical detail exists or is explicitly not needed,
- stale wording is patched or owner-tagged,
- and unrelated docs remain untouched.

## Approval gates

Requires explicit approval for:

- commit/push if not already authorized
- deleting docs or moving large folders
- changing project status to archived/parked if the user did not request it
- publishing externally

## Failure modes

- README bloat: copying the whole session into the front page.
- Hidden truth: updating a dashboard but not the README pointer.
- Half-truth: adding new active status while leaving old blocked status elsewhere.
- Fake closure: saying “documented” without checking final git diff.

## Example receipt

See [`examples/aal-loop-002-docs-readme-milestone-sweep-receipt.md`](../examples/aal-loop-002-docs-readme-milestone-sweep-receipt.md).
