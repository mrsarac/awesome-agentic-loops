# AAL-LOOP-006 Receipt — Stale PR Review Resolver Example

## Scope

- Repo: `owner/app`
- PR: `https://github.com/owner/app/pull/42`
- Head SHA: `def5678`
- Review scope: unresolved comments only

## Comment map

| Comment | Class | Action | Evidence |
|---|---|---|---|
| C1 | ACTIONABLE | patched locally | unit test added for null value |
| C2 | STALE | no code change | referenced function removed in later commit |
| C3 | PRODUCT DECISION | escalated | copy/text behavior ambiguous |

## Validation

```text
pytest tests/test_profile.py -q
12 passed
```

## Final state

- Resolved: 1
- Stale: 1
- Escalated: 1
- External replies posted: no
- Approval needed: push patch and optionally post prepared replies
- Stop reason: every comment classified with proof or owner decision
