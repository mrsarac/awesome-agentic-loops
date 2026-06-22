# Security Policy

Agentic Loop Atlas is a public pattern library. It should not contain secrets, credentials, private logs, customer data, or exploit instructions that enable harm.

## Reporting a vulnerability

If you find a security problem in this repository itself, please open a private security advisory on GitHub if available, or contact the maintainer directly.

## Contribution guardrails

- Do not include live secrets, cookies, tokens, API keys, internal hostnames, or private logs.
- Redact receipts before committing them.
- Security loops should prefer read-only checks and explicit approval gates.
- Do not publish working exploit chains against real third-party systems.

## Pattern safety

The loops in this repository are operating patterns, not permission to mutate production. Deploys, restarts, credential changes, billing changes, and external messages require explicit human approval.
