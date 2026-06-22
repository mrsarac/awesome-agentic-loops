# AAL-LOOP-004 Receipt — Flaky Test Killer Example

## Scope

- Test scope: `tests/test_checkout.py::test_checkout_total_is_stable`
- Command: `pytest tests/test_checkout.py::test_checkout_total_is_stable -q`
- Max attempts: 10
- Target green streak: 3

## Reproduction

| Run | Result | Note |
|---|---|---|
| 1 | pass | — |
| 2 | fail | assertion changed with randomized item order |
| 3 | fail | same order-dependent assertion |

## Diagnosis

- Classification: `ORDERING`
- Hypothesis: test compares unordered API response without sorting.
- Confidence: high

## Action

- Patch: sort response items by stable ID before assertion.
- Diff summary: test-only deterministic assertion change.

## Verification

```text
pytest tests/test_checkout.py::test_checkout_total_is_stable -q --count=5
5 passed
```

## Final state

- Green streak: 5
- Remaining risk: low; product code untouched
- Stop reason: target green streak exceeded with narrow test fix
