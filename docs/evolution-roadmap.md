# Agentic Loop Atlas Evolution Roadmap

> Intent: evolve Awesome Agentic Loops from a proof-grade atlas into a portable agent operating-loop registry — without losing the receipt-first quality bar.

## Operating thesis

The atlas should remain easy to read, but it should also become easy to integrate into real agent systems.

```text
Readable atlas now → portable registry next → installer/sync later
```

## Safety boundary

Automation may prepare branches and PRs. It must not merge, publish releases, deploy, change credentials, or post externally without explicit human approval.

| Action | Automation |
|---|---|
| daily draft artifacts under `drafts/loop-mkt/YYYY-MM-DD/` | allowed to push to `main` |
| repo evolution changes | branch + PR only |
| user PR review comments | allowed when authenticated |
| merge | human only |
| release/social/deploy/credential changes | human only |

## Phases

### Phase 1 — Registry preview

Goal: prove that one loop can be exported into multiple agent surfaces without building a package manager.

Deliverables:

- `registry/README.md`
- one preview loop under `registry/preview/<loop-id>/`
- export sketches for:
  - `AGENTS.md`
  - Hermes skill
  - Cursor rule
- install receipt template
- smoke validator

### Phase 2 — Integration docs

Goal: make the atlas usable by humans with Claude Code, Codex, Cursor, Hermes, OpenCode, and generic `AGENTS.md`-aware agents.

Deliverables:

- `docs/integration.md`
- copy/adapt instructions
- contribution safety notes
- receipt expectations

### Phase 3 — Evolution loop automation

Goal: let the atlas advance toward the roadmap through small, reviewable PRs.

Deliverables:

- `scripts/aal_evolution_loop.py`
- dry-run mode
- smoke validation
- branch/commit/PR mode when GitHub auth is available
- no merge by automation

### Phase 4 — Installer preview

Goal: generate local target files without mutating user systems broadly.

Potential commands:

```bash
python3 scripts/aal-install.py list
python3 scripts/aal-install.py export AAL-LOOP-009 --target agents-md --out ./docs/agent-loops
python3 scripts/aal-install.py export AAL-LOOP-009 --target hermes-skill --out ./vendor/agentic-loops
```

### Phase 5 — Contribution loop

Goal: review external loop submissions without letting the repo become a prompt dump.

Checks:

- schema valid
- proof present
- receipt present or clearly templated
- stop condition present
- approval gate present
- high-risk secret scan clean
- risk level honest

## Definition of done

The roadmap is working when a user can:

1. pick a loop,
2. copy/export it into their agent runtime,
3. run one bounded iteration,
4. produce a receipt,
5. submit a loop or receipt back through a PR.

## Non-goals for now

- no dedicated agent runtime
- no npm/pip/Homebrew package until demand is clear
- no automatic merge
- no social posting automation
- no destructive install behavior
