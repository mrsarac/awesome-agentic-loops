---
id: AAL-LOOP-003
name: Production Error Sweep
category: operations
use_when: You need operational health evidence without touching production services.
trigger: Scheduled health check, incident suspicion, pre-deploy check, post-deploy smoke window, or user asks “is it alive?”
action: Inspect only approved read-only sources, classify findings by severity and confidence, propose next actions, and stop before restart/deploy/credential changes.
proof: Timestamped report with checked URLs/log queries/status commands, observed result, severity, confidence, and exact escalation gate.
memory: Project risk register, incident log, or status dashboard only when the finding is durable; avoid storing transient log noise.
stopping_condition: Stop after one bounded read-only sweep and a decision table; never mutate services inside this loop.
risk_level: read-only/service
approval_gate: restart, deploy, credential/config change, customer/external message, or destructive cleanup
max_iterations: 1
cost_guard: Bounded source list and timebox; no live tailing unless explicitly requested.
works_with:
  - Hermes
  - Claude Code
  - Codex
  - Cursor
failure_modes:
  - Accidentally restarting or redeploying while “just checking”
  - Confusing stale logs with live failure
  - Reporting green from one endpoint while other critical checks failed
  - Exposing secrets from logs
example_receipt: examples/aal-loop-003-production-error-sweep-receipt.md
status: proof-grade
---

# AAL-LOOP-003 — Production Error Sweep

## Purpose

Give a clear operational health picture without touching the running system. This loop is intentionally read-only: it turns logs, endpoints, and status surfaces into a decision table.

It is not a repair loop. Repair starts only after an explicit approval gate.

## Use when

- A service might be down or degraded.
- A deploy just finished and needs a smoke check.
- A scheduled ops report needs evidence.
- A user asks whether production is healthy.
- You need to decide if escalation is warranted.

## Inputs

```yaml
service_name: <service>
allowed_sources:
  - <health URL>
  - <status command>
  - <log path or query>
  - <dashboard/status page>
timebox_minutes: 10
mutation_allowed: false
redaction_required: true
escalation_contacts_or_owner: <person/agent>
```

## Trigger

Scheduled health check, incident suspicion, pre/post-deploy check, or manual “what is the status?” request.

## Action

1. Confirm this is read-only and list allowed sources.
2. Capture timestamp, host/context, and service identifiers.
3. Check health endpoints and status pages.
4. Inspect bounded recent logs or command output.
5. Classify each finding:
   - `GREEN` — healthy with evidence
   - `WATCH` — anomaly but no user impact proven
   - `DEGRADED` — likely user impact or repeated error
   - `P0` — outage/security/data-loss risk
6. Redact secrets and tokens from evidence.
7. Produce a decision table and stop.

## Proof requirements

A proof-grade run must include:

- timestamp and environment
- exact sources checked
- status code/result/log query summary
- severity and confidence
- “no mutation performed” statement
- recommended next action with approval gate

Receipt template:

```markdown
# AAL-LOOP-003 Receipt — <service> — <date>

## Scope
- Service:
- Environment:
- Allowed sources:
- Mutations: none

## Checks
| Source | Result | Severity | Confidence |
|---|---|---|---|
| /health | HTTP 200 | GREEN | high |

## Evidence
```text
<redacted output snippets>
```

## Decision table
| Option | When | Approval needed |
|---|---|---|
| WATCH | ... | no |
| RESTART | ... | yes |

## Stop reason
Read-only sweep completed; repair requires explicit approval.
```

## Memory

Use project risk register, incident log, or status dashboard only when the finding will still matter later. Do not save transient stack traces or secrets.

## Stopping condition

Stop after one bounded sweep and decision table. Do not run repair, restart, deploy, install, credential changes, or external messaging inside this loop.

## Approval gates

Requires explicit approval for:

- restart, deploy, rollback, migration, scaling, or config change
- changing credentials/secrets
- customer/public/internal stakeholder message
- destructive cleanup
- long-running watch mode

## Failure modes

- “Read-only” check becomes an accidental restart.
- Secret leakage from logs.
- Health endpoint green but business-critical path unchecked.
- Stale logs or wrong environment.
- No confidence label, causing false certainty.

## Example receipt

See [`examples/aal-loop-003-production-error-sweep-receipt.md`](../examples/aal-loop-003-production-error-sweep-receipt.md).
