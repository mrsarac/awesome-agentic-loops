# AAL-LOOP-002 Receipt — Docs/README Milestone Sweep Example

## Changed truth

Before:
- A project milestone existed in session output and a dashboard, but the README did not make the current operational state findable.

After:
- README points to the canonical docs/dashboard.
- The detail doc records the milestone and risk gate.
- Historical details stay out of the README.

## Files patched

- `README.md` — current-state row updated with the milestone and canonical pointer.
- `docs/<project-status>.md` — operational details and next action added.
- `docs/<dashboard>.html` — human-readable cockpit updated if one exists.

## Verification

```text
python3 -m json.tool catalog.json >/dev/null
python3 - <<'PY'
from html.parser import HTMLParser
HTMLParser().feed(open('docs/<dashboard>.html').read())
print('HTML parse OK')
PY
git diff --stat
```

## Final state

- Findable from README: yes
- Canonical detail doc: `docs/<project-status>.md`
- History destination: `docs/timeline.md` or omitted if not durable
- Stop reason: milestone now discoverable without README bloat

## Notes

If the milestone implies service, credential, external publication, or broad repo changes, this loop stops at documentation and asks for a separate approval-gated execution loop.
