# Integrating Agentic Loop Atlas Into Your Agent System

Agentic Loop Atlas is designed to be used at three levels:

1. **Read** — browse a loop card and manually follow it.
2. **Copy/adapt** — place a loop card or snippet inside your project context.
3. **Export preview** — use registry preview files as runtime-specific starting points.

The atlas is not an agent runtime. It is a portable operating-loop layer around the agent runtime you already use.

## Quick mental model

```text
your agent runtime
  + loop card contract
  + project context
  + receipt requirement
  = bounded, auditable agent work
```

## Generic AGENTS.md integration

Add a section like this to your project `AGENTS.md`:

```md
## Operating loops

When asked to turn research into a public-ready artifact, follow:
`docs/agent-loops/aal-loop-009-research-to-public-artifact.md`.

Rules:
- run one bounded iteration
- keep a source map
- stop before posting externally
- produce a receipt
```

## Claude Code / Codex / Cursor integration

Copy a loop card into your repo, then ask the agent to follow it:

```text
Follow AAL-LOOP-009 for this task.
Run one bounded iteration.
Stop before external publication.
Return the receipt.
```

For Cursor-style rules, keep the loop short and trigger-oriented. Do not paste every loop into global rules; only add the loops your project actually uses.

## Hermes integration

A loop can become a Hermes skill when it is reusable enough. Keep the skill focused on the workflow and preserve the loop card’s approval gates.

Recommended shape:

```text
~/.hermes/skills/agentic-loops/<loop-name>/SKILL.md
```

## Syncing new loops

Today, `catalog.json` is the canonical machine-readable index. Future installer/sync tooling should read from `catalog.json`, but users can already vendor specific loop cards into their projects.

Suggested local layout:

```text
docs/agent-loops/
  aal-loop-009-research-to-public-artifact.md
  receipts/
```

## Sharing your own loop

Open a PR with:

- loop card metadata
- proof requirements
- risk level and approval gate
- stopping condition
- receipt example or template
- sanitized source links

No proof, no loop.
