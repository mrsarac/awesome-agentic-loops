# Install Receipt Template — AAL-LOOP-009

Use this after copying/exporting the loop into a project or agent runtime.

```yaml
receipt_type: aal_install_receipt
loop_id: AAL-LOOP-009
loop_name: Research-to-Public-Artifact Loop
target_surface: agents_md | hermes_skill | cursor_rule | project_docs | other
installed_to: path/or/location
source_card: loops/aal-loop-009-research-to-public-artifact-loop.md
installed_at: YYYY-MM-DD
operator: human-or-agent-name
verification:
  - local file exists
  - approval gate preserved
  - stop condition preserved
  - dry-run or bounded test completed
approval_boundary:
  external_publication: human_approval_required
  deploy: human_approval_required
  social_post: human_approval_required
notes: |
  Add any project-specific adaptations here.
```

Do not treat installation as proof that the loop worked. A working run still needs its own task receipt.
