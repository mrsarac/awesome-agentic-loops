# Platform Matrix

| Capability | Hermes | Claude Code | Codex | Cursor | Durable runtime |
|---|---|---|---|---|---|
| Scheduled run | cron jobs | scheduled tasks/hooks | automations | external cron | native workflow |
| Tool use | Hermes tools/MCP | built-in tools/MCP | connectors | agent tools | activities/functions |
| Skills | Hermes skills | Agent Skills | Agent Skills | rules/skills | workflow code |
| Work isolation | workdir/worktree | git worktree | worktree/thread | workspace | workflow state |
| Stop condition | prompt + proof gate | /goal/max turns | /goal | prompt/rules | workflow condition |
| State memory | files, memory, sessions | CLAUDE.md/files | AGENTS.md/files | project files | durable state |
