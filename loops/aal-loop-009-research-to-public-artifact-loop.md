---
id: AAL-LOOP-009
name: Research to Public Artifact Loop
category: research
use_when: A research insight, market delta, or internal report may become a public post, README, article, deck, or demo artifact.
trigger: Research report, market scan, new technical insight, project milestone, or user asks to turn research into public signal.
action: Distill sources into a draft artifact, preserve citations/source map, run risk/claims QA, and stop before publication.
proof: Source map, draft artifact path, claims checklist, risk review, and explicit approval gate for public posting.
memory: Draft queue, editorial ledger, or source map; do not store raw private notes or sensitive partner context in public drafts.
stopping_condition: Stop at a publication-ready draft package; publishing requires explicit approval.
risk_level: external
approval_gate: public post, external message, website publish, repo visibility change, partner/client mention
max_iterations: 1
cost_guard: One bounded draft pass; no public write.
works_with:
  - Hermes
  - Claude Code
  - Codex
  - Cursor
failure_modes:
  - Publishing before approval
  - Overclaiming beyond sources
  - Leaking private/internal context
  - Losing citation/source traceability
example_receipt: examples/aal-loop-009-research-to-public-artifact-loop-receipt.md
status: proof-grade
---

# AAL-LOOP-009 — Research-to-Public-Artifact Loop

## Purpose

Convert research into a public-candidate artifact without accidentally publishing, overclaiming, or leaking private context. This loop ends at a draft package and approval checklist.

## Use when

- A market/research report has reusable insight.
- A project milestone should become a blog/X/LinkedIn/README artifact.
- A technical pattern deserves public explanation.
- A team wants a source-backed draft before posting.

## Inputs

```yaml
research_sources:
  - <report path or URL>
artifact_type: x-thread | blog | README | deck | landing-page | demo
public_audience: <who this is for>
private_context_to_exclude:
  - <names/secrets/internal notes>
approval_gate: external publication
```

## Action

1. Read bounded sources and create a source map.
2. Extract claims and classify confidence.
3. Draft the artifact for the audience.
4. Run public-risk QA:
   - private info
   - unsupported claims
   - partner/client sensitivity
   - legal/financial/medical/security caveats
5. Produce publication checklist and approval question.
6. Stop before external write.

## Proof requirements

- source map
- draft artifact path
- claims table with source/confidence
- redaction/privacy notes
- publication checklist
- explicit “not posted” statement

## Stopping condition

Stop at a publication-ready draft package or risk blocker. Do not publish, DM, email, tweet, or deploy without explicit approval.

## Approval gates

Requires explicit approval for public posting, website publish, repo visibility change, newsletter/email, DM, partner/client mention, or paid promotion.

## Example receipt

See [`examples/aal-loop-009-research-to-public-artifact-loop-receipt.md`](../examples/aal-loop-009-research-to-public-artifact-loop-receipt.md).
