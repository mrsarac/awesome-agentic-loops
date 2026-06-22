---
id: AAL-LOOP-008
name: Cost Budget Watch Loop
category: finops
use_when: Agentic loops, model usage, web search, containers, or automation may burn budget silently.
trigger: Scheduled budget check, new automation, provider/model change, billing anomaly, or before enabling a recurring loop.
action: Inspect read-only usage/cost summaries, compare against thresholds, classify anomalies, and propose throttles or approvals without changing billing by default.
proof: Timestamped usage/cost delta, source, threshold comparison, anomaly classification, and next action.
memory: Budget ledger, cost note, or project status only when durable; do not store raw invoices or secrets.
stopping_condition: Stop after one bounded report; billing/provider/config changes require approval.
risk_level: read-only/billing
approval_gate: billing change, provider/model config change, quota increase, paid upgrade, cancellation
max_iterations: 1
cost_guard: Read-only billing observation; no automatic spend changes.
works_with:
  - Hermes
  - Claude Code
  - Codex
  - Cursor
failure_modes:
  - Confusing estimated usage with billed cost
  - Changing quotas/providers while “just checking”
  - Missing non-token costs such as web search, containers, storage, or CI minutes
  - Reporting noisy daily variance as a crisis
example_receipt: examples/aal-loop-008-cost-budget-watch-loop-receipt.md
status: proof-grade
---

# AAL-LOOP-008 — Cost Budget Watch Loop

## Purpose

Make agent cost visible before it becomes surprise burn. This loop is read-only by default and reports budget state, deltas, and thresholds. It does not change billing, providers, quotas, or subscriptions without approval.

## Use when

- A recurring agent loop is created.
- A provider/model changes.
- Usage-limit or quota errors appear.
- A team wants a daily/weekly budget report.
- Non-token costs may matter: search, containers, CI, storage, hosted browsers.

## Inputs

```yaml
budget_scope: <provider/project/team>
sources:
  - provider usage dashboard/API
  - local cron/job usage logs
  - CI/container/search usage summaries
thresholds:
  daily_warning: <amount>
  monthly_cap: <amount>
mutation_allowed: false
```

## Action

1. State scope, sources, thresholds, and read-only boundary.
2. Collect usage/cost summaries.
3. Separate actual billed cost from estimates.
4. Compare against thresholds.
5. Classify: `GREEN`, `WATCH`, `THROTTLE`, `APPROVAL NEEDED`, `P0 SPEND RISK`.
6. Identify cost drivers and suggested action.
7. Stop before billing/provider/quota mutation.

## Proof requirements

- timestamp and source list
- cost/usage delta
- threshold comparison
- anomaly classification
- known caveats about estimate vs billed cost
- recommended next action and approval gate

## Stopping condition

Stop after one bounded report. Any billing/config/provider action becomes a separate approval-gated task.

## Approval gates

Requires explicit approval for changing provider, model, quota, subscription, billing settings, cron cadence, or paid services.

## Example receipt

See [`examples/aal-loop-008-cost-budget-watch-loop-receipt.md`](../examples/aal-loop-008-cost-budget-watch-loop-receipt.md).
