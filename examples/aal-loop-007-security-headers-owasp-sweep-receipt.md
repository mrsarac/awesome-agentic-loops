# AAL-LOOP-007 Receipt — Security Headers / OWASP Sweep Example

## Scope

- Target: `https://example.com`
- Mutations: none
- Checks: `curl -I`, passive header review

## Findings

| Finding | Severity | Evidence | Action |
|---|---|---|---|
| Missing `Content-Security-Policy` | MEDIUM | header absent | propose CSP draft |
| `X-Frame-Options` present | GREEN | `DENY` | none |
| `Strict-Transport-Security` present | GREEN | `max-age=31536000` | none |

## Evidence

```text
2026-06-22T20:00:00+02:00 curl -I https://example.com
HTTP/2 200
strict-transport-security: max-age=31536000
x-frame-options: DENY
```

## Final state

- Critical/high findings: 0
- Medium findings: 1 owner-tagged
- Deploy/restart/config changes: none
- Stop reason: read-only audit completed; remediation requires approval
