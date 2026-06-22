# Contributing

We accept loops, not vibes.

A contribution should include:

1. A loop card in `loops/`.
2. A catalog entry in `catalog.json`.
3. Proof and stopping condition.
4. Risk level and approval gate.
5. Known failure modes.

## Review checklist

- [ ] Trigger is specific.
- [ ] Action is bounded.
- [ ] Proof is externally checkable.
- [ ] Stopping condition cannot be faked by the agent simply saying “done”.
- [ ] Risk/approval gates are explicit.
- [ ] Cost guard exists.
- [ ] Human escalation path exists.
