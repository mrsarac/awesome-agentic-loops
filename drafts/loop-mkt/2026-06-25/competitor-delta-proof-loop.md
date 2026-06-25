---
id: AAL-DRAFT-competitor-delta-proof-loop
name: Competitor Delta Proof Loop
category: research
use_when: You need to monitor a crowded public market/category without turning every new repo into noise.
trigger: Scheduled market scan, repo/star/update delta, competitor positioning change, or launch-watch checkpoint.
action: Collect bounded public signals, compare against previous ledger entries, classify signal/noise, produce one decision-ready delta card, and stop before public action.
proof: Source URLs, previous/current metric table, signal/noise classification, chosen next action, and no-write statement.
memory: Local market ledger and source map; do not store secrets or private competitive notes.
stopping_condition: Stop after one ranked delta card and one next-loop plan; no repo write/publish/post without approval.
risk_level: read-only/external-signal
approval_gate: commit/push to public atlas, external post, competitor outreach, provider or credential changes
max_iterations: 1
cost_guard: Four bounded public GitHub queries; no crawling beyond stop condition.
works_with:
  - Hermes
  - Claude Code
  - Codex
failure_modes:
  - Counting every updated repo as signal
  - No previous/current comparison
  - Publishing competitive claims without source proof
  - Letting market watching replace product output
example_receipt: drafts/loop-mkt/2026-06-25/competitor-delta-proof-loop-receipt.md
status: draft-ready
---

# Competitor Delta Proof Loop

## Purpose
Turn a recurring market scan into one proof-backed product artifact instead of a noisy research dump.

## Inputs
```yaml
queries:
  - awesome agent loops
  - loop engineering
  - agentic loop
  - autonomous AI company
previous_ledger: ~/.hermes/research/loop-mkt/*.md
output_mode: draft loop card + receipt + source map
approval_gate: public atlas commit/push or external publication
```

## Action
1. Run bounded public source collection.
2. Deduplicate sources by repository/project.
3. Rank signal by proof value, not novelty alone.
4. Create one loop-card candidate and one receipt.
5. Stop before commit, push, website publish, or social post.

## Proof requirements
- source URLs and query labels
- previous/current comparison when available
- signal/noise note
- draft artifact paths
- explicit no-public-write statement

## Stopping condition
One card package exists under `drafts/loop-mkt/YYYY-MM-DD/`; publication remains approval-gated.
