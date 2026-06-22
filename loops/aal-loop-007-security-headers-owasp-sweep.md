---
id: AAL-LOOP-007
name: Security Headers OWASP Sweep
category: security
use_when: A web app or API needs a bounded security posture check before launch, after deploy, or during periodic hardening.
trigger: Manual audit request, release hardening, new domain, changed reverse proxy/CDN config, or scheduled security posture review.
action: Inspect security headers and selected OWASP exposure signals using read-only checks first; propose minimal fixes and require approval before deploy/restart/config changes.
proof: Timestamped curl/scanner evidence before and after, severity table, exact headers/findings, and approval-gated remediation plan.
memory: Security report, issue, or risk register entry; never store secrets, cookies, auth headers, or raw sensitive logs.
stopping_condition: Stop when critical/high findings are fixed, explicitly owned, or blocked behind an approval gate.
risk_level: code/service
approval_gate: deploy, restart, proxy/CDN config change, credential/security policy change
max_iterations: 5
cost_guard: No credential or production mutation without approval; max five scan/fix cycles.
works_with:
  - Hermes
  - Claude Code
  - Codex
  - Cursor
failure_modes:
  - Accidentally mutating production while auditing
  - Leaking cookies/secrets from request traces
  - Treating scanner output as truth without context
  - Adding restrictive headers that break app flows
example_receipt: examples/aal-loop-007-security-headers-owasp-sweep-receipt.md
status: proof-grade
---

# AAL-LOOP-007 — Security Headers / OWASP Sweep

## Purpose

Run a bounded security posture check focused on headers and common web exposure signals. This is an audit-and-propose loop first; remediation that touches deploys, proxies, CDNs, credentials, or production config requires explicit approval.

## Use when

- A site/API is about to be published.
- A reverse proxy, CDN, or hosting config changed.
- Security headers may be missing or stale.
- A scheduled hardening pass needs evidence.
- A user asks for “quick OWASP/security sanity check” without service mutation.

## Inputs

```yaml
targets:
  - https://example.com
allowed_checks:
  - curl -I
  - securityheaders.com / local equivalent
  - limited OWASP passive checks
mutation_allowed: false
approval_gate: deploy/restart/proxy-config/credential-change
severity_threshold: high
```

## Action

1. Confirm scope and mutation boundary.
2. Capture timestamp, target URLs, and environment.
3. Run read-only header/status checks.
4. Classify findings: `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `INFO`.
5. Map each finding to a minimal remediation and risk/tradeoff.
6. If remediation is docs/code-only and approved, patch narrowly; otherwise propose.
7. Re-check only if a fix was applied.
8. End with a receipt and approval-gated next actions.

## Proof requirements

- target URL list
- exact commands/tools used
- before/after header evidence if changed
- severity table
- false-positive/context notes
- mutation/no-mutation statement
- approval gate for remaining actions

## Stopping condition

Stop when critical/high findings are fixed, owner-tagged, or blocked behind approval. Do not keep scanning broader surfaces without a new scope.

## Approval gates

Requires explicit approval for deploy, restart, CDN/proxy config, security policy changes, auth/cookie changes, or external disclosure.

## Example receipt

See [`examples/aal-loop-007-security-headers-owasp-sweep-receipt.md`](../examples/aal-loop-007-security-headers-owasp-sweep-receipt.md).
