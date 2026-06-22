#!/usr/bin/env python3
"""Validate Agentic Loop Atlas catalog, paths, and frontmatter contracts."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import NoReturn

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FRONTMATTER = {
    "id",
    "name",
    "category",
    "use_when",
    "trigger",
    "action",
    "proof",
    "memory",
    "stopping_condition",
    "risk_level",
    "approval_gate",
    "max_iterations",
    "cost_guard",
    "works_with",
    "failure_modes",
    "example_receipt",
    "status",
}


def fail(message: str) -> NoReturn:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - CLI guard
        fail(f"invalid JSON {path.relative_to(ROOT)}: {exc}")


def extract_frontmatter(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"missing YAML frontmatter: {path.relative_to(ROOT)}")
    parts = re.split(r"^---\s*$", text, maxsplit=2, flags=re.MULTILINE)
    if len(parts) < 3 or not parts[1].strip():
        fail(f"empty or malformed YAML frontmatter: {path.relative_to(ROOT)}")
    return parts[1]


def simple_frontmatter_keys(frontmatter: str) -> set[str]:
    keys: set[str] = set()
    for line in frontmatter.splitlines():
        if not line or line.startswith(" ") or line.startswith("-") or line.startswith("#"):
            continue
        if ":" in line:
            keys.add(line.split(":", 1)[0].strip())
    return keys


def main() -> None:
    catalog = load_json(ROOT / "catalog.json")
    load_json(ROOT / "schemas" / "loop-card.schema.json")

    loops = catalog.get("loops")
    if not isinstance(loops, list) or not loops:
        fail("catalog.json must contain a non-empty loops array")

    seen_ids: set[str] = set()
    proof_grade_count = 0

    for entry in loops:
        loop_id = entry.get("id")
        if not loop_id:
            fail("catalog loop entry missing id")
        if loop_id in seen_ids:
            fail(f"duplicate loop id in catalog: {loop_id}")
        seen_ids.add(loop_id)

        loop_path = ROOT / entry.get("path", "")
        if not loop_path.is_file():
            fail(f"catalog path missing for {loop_id}: {entry.get('path')}")

        frontmatter = extract_frontmatter(loop_path)
        keys = simple_frontmatter_keys(frontmatter)
        missing = sorted(REQUIRED_FRONTMATTER - keys)
        if missing:
            fail(f"{loop_path.relative_to(ROOT)} missing frontmatter keys: {', '.join(missing)}")

        if f"id: {loop_id}" not in frontmatter:
            fail(f"frontmatter id mismatch for {loop_id}: {loop_path.relative_to(ROOT)}")

        if entry.get("status") == "proof-grade":
            proof_grade_count += 1
            receipt = entry.get("example_receipt")
            if not receipt:
                fail(f"proof-grade loop missing example_receipt: {loop_id}")
            if not (ROOT / receipt).is_file():
                fail(f"receipt path missing for {loop_id}: {receipt}")

    declared = catalog.get("proof_grade_count")
    if declared != proof_grade_count:
        fail(f"proof_grade_count mismatch: declared {declared}, actual {proof_grade_count}")

    for key in ("landing_page", "announcement_draft", "positioning"):
        value = catalog.get(key)
        if value and not (ROOT / value).is_file():
            fail(f"catalog {key} path missing: {value}")

    print(f"Atlas validation OK: {len(loops)} loops, {proof_grade_count} proof-grade")


if __name__ == "__main__":
    main()
