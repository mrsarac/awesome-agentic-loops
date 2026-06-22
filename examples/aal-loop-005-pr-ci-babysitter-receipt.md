# AAL-LOOP-005 Receipt — PR CI Babysitter Example

## Scope

- Repo: `owner/app`
- PR: `https://github.com/owner/app/pull/42`
- Head SHA: `abc1234`
- Poll limit: 6

## Checks

| Check | State | Evidence |
|---|---|---|
| lint | passed | `gh pr checks 42` |
| tests | failed | `AssertionError` in `test_invoice_total` |
| build | pending → passed | completed on poll 3 |

## Diagnosis

- Classification: `TEST`
- Confidence: medium-high
- Suggested action: inspect invoice rounding change; narrow fix likely.

## Actions taken

- No push performed in babysitter loop.
- Prepared fix recommendation and blocker packet.

## Final state

- Checks: 2 passed, 1 failed
- Merge-ready: no
- Approval needed: push a narrow test/product fix or assign owner
- Stop reason: failing check classified; mutation requires approval
