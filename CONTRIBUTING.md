# Contributing

We accept loops, not vibes.

A good contribution makes an agentic workflow more bounded, observable, and safe.

## Preferred contributions

1. **Receipts for existing loops** — real redacted evidence from Claude Code, Codex, Cursor, Hermes, OpenCode, or another runtime.
2. **Pattern hardening** — clearer approval gates, failure modes, stopping conditions, or proof requirements.
3. **New loop proposals** — only when no existing loop fits.
4. **Platform notes** — compatibility details for agent runtimes and CI/devops surfaces.

## New loop checklist

A new loop should include:

1. A loop card in `loops/`.
2. A catalog entry in `catalog.json`.
3. Proof and stopping condition.
4. Risk level and approval gate.
5. Cost guard.
6. Known failure modes.
7. Example receipt or receipt template.

## Review checklist

- [ ] Trigger is specific.
- [ ] Action is bounded.
- [ ] Proof is externally checkable.
- [ ] Stopping condition cannot be faked by the agent simply saying “done”.
- [ ] Risk/approval gates are explicit.
- [ ] Cost guard exists.
- [ ] Human escalation path exists.
- [ ] Receipt is redacted and does not contain secrets/private logs.

## Safety rules

Do not include:

- API keys, cookies, tokens, passwords, or credentials
- private customer/partner data
- raw logs with secrets
- exploit chains against real third-party systems
- instructions that imply deploy/restart/billing/credential/external-message actions without explicit approval

## Issue templates

Use GitHub issue templates for:

- loop proposals
- receipt wanted / receipt contributed
- pattern hardening

Motion is not progress; proof is.
