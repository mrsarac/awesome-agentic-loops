---
id: AAL-LOOP-006
name: Stale PR Review Resolver
category: engineering
use_when: Pull request review comments are unresolved, stale, contradictory, or blocking merge after code has moved on.
trigger: PR review comments pending, reviewer requested changes, old PR revived, merge readiness cleanup, or user asks to resolve stale review feedback.
action: Inventory comments, classify each as actionable/stale/ambiguous/product-decision, apply minimal approved fixes, and return unresolved decisions to humans.
proof: Review comment list, classification table, diff/tests for resolved items, explicit stale/ambiguous rationale, and final unresolved count.
memory: PR thread summary and issue/decision log only; do not store full review transcripts.
stopping_condition: Stop when every comment is resolved, marked stale with evidence, or escalated as an owner decision.
risk_level: code/external
approval_gate: push, external comment, dismiss review, merge, broad refactor
max_iterations: 6
cost_guard: Bounded to one PR and max 6 fix/review cycles.
works_with:
  - Hermes
  - Claude Code
  - Codex
  - Cursor
failure_modes:
  - Dismissing real feedback as stale
  - Making broad refactors to satisfy narrow comments
  - Replying externally without approval
  - Losing traceability between comment and fix
example_receipt: examples/aal-loop-006-stale-pr-review-resolver-receipt.md
status: proof-grade
---

# AAL-LOOP-006 — Stale PR Review Resolver

## Purpose

Turn messy PR review threads into a clear resolution map. The loop does not “win arguments”; it classifies comments, applies narrow fixes when safe, and escalates product/architecture decisions.

## Use when

- A PR has unresolved review comments.
- Review feedback may be stale after new commits.
- Requested changes block merge.
- Multiple reviewers disagree.
- A revived PR needs cleanup before merge.

## Inputs

```yaml
repo: <owner/name>
pr_number: <number>
review_scope: unresolved comments only | all comments
allowed_changes: narrow code/docs fixes with approval
approval_gate: push/comment/dismiss-review/merge/broad-refactor
required_validation: tests or targeted checks
```

## Trigger

Pending review comments, requested-changes state, stale PR revival, or manual merge-readiness cleanup.

## Action

1. Capture PR URL, branch, head SHA, and review state.
2. Inventory unresolved comments with file/line/thread IDs if available.
3. Classify each comment:
   - `ACTIONABLE`
   - `STALE`
   - `AMBIGUOUS`
   - `PRODUCT DECISION`
   - `ARCHITECTURE DECISION`
   - `NIT/OPTIONAL`
4. For actionable comments, propose the minimal fix.
5. Apply fixes only if inside approved scope.
6. Run targeted validation.
7. Prepare reply text but do not post externally unless approved.
8. End with resolved/stale/escalated counts.

## Proof requirements

A proof-grade run must include:

- PR URL and head SHA
- comment inventory and classification
- mapping from each fixed comment to diff/test evidence
- list of stale comments with rationale
- list of ambiguous/product/architecture decisions needing owner input
- final unresolved count

Receipt template:

```markdown
# AAL-LOOP-006 Receipt — PR <number> — <date>

## Scope
- Repo:
- PR:
- Head SHA:
- Review scope:

## Comment map
| Comment | Class | Action | Evidence |
|---|---|---|---|
| C1 | ACTIONABLE | patched | test output ... |
| C2 | STALE | no code change | line removed in commit ... |

## Validation
```text
<targeted test/check output>
```

## Final state
- Resolved:
- Stale:
- Escalated:
- External replies posted: yes/no
- Approval needed:
- Stop reason:
```

## Memory

Keep the durable summary in the PR/issue/decision log. Do not preserve full raw review text unless required for audit.

## Stopping condition

Stop when all comments are one of:

- fixed with proof,
- stale with evidence,
- escalated to owner decision,
- or intentionally deferred.

## Approval gates

Requires explicit approval for:

- pushing commits
- posting PR replies/comments
- dismissing reviews
- merging/rebasing
- broad refactors or architecture changes

## Failure modes

- Calling a valid concern stale.
- Fixing too much and creating review churn.
- Posting defensive comments instead of evidence.
- Losing traceability from comment to fix.

## Example receipt

See [`examples/aal-loop-006-stale-pr-review-resolver-receipt.md`](../examples/aal-loop-006-stale-pr-review-resolver-receipt.md).
