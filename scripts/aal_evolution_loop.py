#!/usr/bin/env python3
"""AAL Evolution Loop smoke/PR helper.

Purpose:
- Keep repo evolution changes reviewable.
- Validate the registry-preview contract.
- Optionally create a branch/commit and GitHub PR when gh auth is available.

This script intentionally never merges, releases, deploys, or posts externally.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import subprocess
import sys
from datetime import date

ROOT = pathlib.Path(__file__).resolve().parents[1]
PREVIEW = ROOT / "registry" / "preview" / "aal-loop-009"
REQUIRED_PREVIEW_FILES = [
    "agents-md-snippet.md",
    "hermes-skill-sketch.md",
    "cursor-rule-sketch.md",
    "install-receipt-template.md",
]


def run(cmd: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, check=check)


def assert_file(path: pathlib.Path) -> None:
    if not path.exists() or not path.is_file():
        raise SystemExit(f"missing required file: {path.relative_to(ROOT)}")


def high_risk_secret_scan(paths: list[pathlib.Path]) -> None:
    patterns = [
        re.compile(r"(?i)(api[_-]?key|secret[_-]?key|access[_-]?token|auth[_-]?token|password)\s*[:=]\s*['\"]?[^'\"\s]{12,}"),
        re.compile(r"(?i)bearer\s+[a-z0-9._-]{20,}"),
        re.compile(r"sk-[A-Za-z0-9]{20,}"),
    ]
    for path in paths:
        text = path.read_text(errors="ignore")
        for pattern in patterns:
            if pattern.search(text):
                raise SystemExit(f"possible secret in {path.relative_to(ROOT)}")


def validate_registry_preview() -> dict:
    assert_file(ROOT / "docs" / "evolution-roadmap.md")
    assert_file(ROOT / "docs" / "integration.md")
    assert_file(ROOT / "registry" / "README.md")
    for name in REQUIRED_PREVIEW_FILES:
        assert_file(PREVIEW / name)

    catalog = json.loads((ROOT / "catalog.json").read_text())
    loop_ids = {item["id"] for item in catalog.get("loops", [])}
    if "AAL-LOOP-009" not in loop_ids:
        raise SystemExit("AAL-LOOP-009 missing from catalog.json")

    md_paths = [ROOT / "docs" / "evolution-roadmap.md", ROOT / "docs" / "integration.md", ROOT / "registry" / "README.md"]
    md_paths.extend(PREVIEW / name for name in REQUIRED_PREVIEW_FILES)
    high_risk_secret_scan(md_paths)

    atlas = run(["python3", "scripts/validate_atlas.py"])
    diff_check = run(["git", "diff", "--check"])
    return {
        "registry_preview": "ok",
        "atlas_validation": atlas.stdout.strip(),
        "diff_check": diff_check.stdout.strip() or "ok",
        "files": [str(p.relative_to(ROOT)) for p in md_paths],
    }


def print_report(result: dict) -> None:
    print("AAL Evolution Loop smoke report")
    print(f"Status: {result['registry_preview']}")
    print(f"Atlas: {result['atlas_validation']}")
    print(f"Diff check: {result['diff_check']}")
    print("Preview files:")
    for path in result["files"]:
        print(f"- {path}")
    print("Boundary: branch/PR allowed; merge/release/social/deploy forbidden.")


def gh_auth_ok() -> bool:
    res = run(["gh", "auth", "status"], check=False)
    return res.returncode == 0


def create_pr(title: str, body: str) -> None:
    if not gh_auth_ok():
        raise SystemExit("gh auth is not valid; cannot create GitHub PR automatically")
    run(["gh", "pr", "create", "--title", title, "--body", body, "--base", "main"])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Validate preview only")
    parser.add_argument("--create-pr", action="store_true", help="Create a GitHub PR for current branch when gh auth works")
    args = parser.parse_args()

    result = validate_registry_preview()
    print_report(result)

    if args.create_pr:
        branch = run(["git", "branch", "--show-current"]).stdout.strip()
        if branch == "main":
            raise SystemExit("refusing to create PR from main")
        title = "docs: add registry preview evolution loop"
        body = "\n".join([
            "## Summary",
            "- add AAL evolution roadmap",
            "- add integration guide",
            "- add registry preview for AAL-LOOP-009 exports",
            "- add smoke-tested evolution helper",
            "",
            "## Tests",
            "- `python3 scripts/aal_evolution_loop.py --dry-run`",
            "- `python3 scripts/validate_atlas.py`",
            "",
            "## Boundaries",
            "- no merge by automation",
            "- no release/social/deploy/credential changes",
        ])
        create_pr(title, body)
        print(f"PR requested from branch: {branch}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
