# AAL-LOOP-003 Receipt — Production Error Sweep Example

## Scope

- Service: `<service-name>`
- Environment: production
- Allowed sources:
  - `GET https://example.com/health`
  - recent application log query, last 100 lines
  - deployment/status dashboard
- Mutations: none

## Checks

| Source | Result | Severity | Confidence |
|---|---|---|---|
| `/health` | HTTP 200 in 180 ms | GREEN | high |
| app logs | 3 transient 5xx in last hour, no repeated stack trace | WATCH | medium |
| dashboard | latest deploy successful, no active incident | GREEN | high |

## Evidence

```text
2026-06-22T20:00:00+02:00 GET /health -> 200
recent logs checked: last 100 lines, secrets redacted
no restart/deploy/config changes performed
```

## Decision table

| Option | When | Approval needed |
|---|---|---|
| WATCH | Low volume transient errors only | no |
| INVESTIGATE | Error rate repeats or user impact appears | no for read-only, yes for mutation |
| RESTART/ROLLBACK | Confirmed outage or deploy regression | yes |

## Stop reason

Read-only sweep completed; no mutation performed. Repair requires explicit approval.
