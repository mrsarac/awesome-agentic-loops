---
id: AAL-LOOP-010
name: Agent Mesh Health Loop
category: operations
use_when: A multi-agent mesh, remote execution machine, gateway, or scheduled agent loop may be degraded before delegation or reporting.
trigger: Before cross-agent delegation, scheduled ops check, user asks “what is alive?”, gateway suspicion, cron failure, or remote reachability uncertainty.
action: Run read-only reachability, gateway, cron, disk, route, and recent-error checks; classify green/yellow/red; stop before restarts or service mutation.
proof: Timestamped command/status output, exact host/route checked, green/yellow/red table, and blocker/next action.
memory: Infrastructure docs only if durable route truth changed; do not store transient outages as permanent memory.
stopping_condition: Stop after reporting mesh health; restarts/updates/install/config mutation require approval.
risk_level: read-only
approval_gate: restart, update, install, config change, credential change, service lifecycle
max_iterations: 1
cost_guard: Read-only mesh check; no long-running monitors unless separately scheduled.
works_with:
  - Hermes
  - Claude Code
  - Codex
  - Cursor
failure_modes:
  - Treating ping failure as host failure when SSH works
  - Restarting gateways during a read-only check
  - Ignoring stale Tailscale/LAN route fallbacks
  - Reporting no jobs because the wrong profile/env was inspected
example_receipt: examples/aal-loop-010-agent-mesh-health-loop-receipt.md
status: proof-grade
---

# AAL-LOOP-010 — Agent Mesh Health Loop

## Purpose

Check whether a multi-agent system is healthy enough to delegate work. The loop is read-only and reports exact blockers. Repair is a separate approval-gated action.

## Use when

- Before sending work to a remote agent/machine.
- A gateway/bot seems silent.
- Cron output is missing or stale.
- A user asks “what is alive?”
- A route may have changed: LAN vs VPN vs SSH alias.

## Inputs

```yaml
agents:
  - RICK
  - MORTY
  - SUMMER
checks:
  - ssh reachability
  - hermes gateway status
  - cron status/list
  - recent logs/errors
  - disk pressure
mutation_allowed: false
approval_gate: restart/update/install/config/credentials
```

## Action

1. State host list and read-only boundary.
2. Check reachability using the correct route for each host.
3. Check Hermes/gateway status where relevant.
4. Check cron status and recent failures.
5. Check recent logs/errors only enough to classify.
6. Classify per host: `GREEN`, `WATCH`, `DEGRADED`, `BLOCKED`.
7. Report exact blocker and proposed next action.
8. Stop before repair.

## Proof requirements

- timestamp
- host/route checked
- commands/status outputs summarized
- per-host classification
- cron/gateway evidence if relevant
- no-mutation statement
- approval-gated repair suggestions

## Stopping condition

Stop after health report. No restarts, updates, installs, config changes, or credential actions inside this loop.

## Approval gates

Requires explicit approval for gateway restart, service lifecycle, Hermes update, package install, config mutation, credential/auth repair, or persistent monitor setup.

## Example receipt

See [`examples/aal-loop-010-agent-mesh-health-loop-receipt.md`](../examples/aal-loop-010-agent-mesh-health-loop-receipt.md).
