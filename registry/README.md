# Registry Preview

This directory is the experimental portability layer for Agentic Loop Atlas.

The stable atlas lives in:

- `loops/`
- `examples/`
- `catalog.json`
- `llms.txt`

The registry preview explores how a proof-grade loop can be exported into common agent surfaces without turning this repo into a heavyweight package manager.

## Current policy

- This is a preview, not a stable installer.
- Use **copy/adapt/export** language, not broad automatic install language.
- Do not weaken the proof-grade standard.
- Do not remove approval gates when exporting a loop.

## Preview structure

```text
registry/preview/<loop-id>/
  agents-md-snippet.md
  hermes-skill-sketch.md
  cursor-rule-sketch.md
  install-receipt-template.md
```

## First pilot

The first pilot uses `AAL-LOOP-009 Research-to-Public-Artifact Loop` because it is broadly useful and has a clear external-publication approval boundary.
