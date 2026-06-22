# Risk Taxonomy

| Level | Meaning | Default approval |
|---|---|---|
| read-only | Reads public/local information only | none |
| docs | Edits documentation or generated reports | commit/push gate |
| code | Edits source code or tests | commit/push gate |
| service | Deploys, restarts, migrates, changes runtime | explicit approval |
| external | Sends messages, posts, opens PRs/issues, contacts people | explicit approval |
| credential | Reads/writes auth, keys, billing, secrets | explicit approval |
| destructive | Deletes, resets, overwrites, purges | explicit approval + rollback plan |

Default rule: if in doubt, escalate.
