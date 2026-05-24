#!/usr/bin/env python3
"""Apply classified diffs to the repo's docs/ and alerts/ files.

Starter skeleton. Writing is not implemented; the script will only
report what it would do under `--dry-run`.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DIFFS_DIR = REPO_ROOT / "sources" / "diffs"
ALERTS_DIR = REPO_ROOT / "alerts"
DOCS_DIR = REPO_ROOT / "docs"


def list_diffs(diffs_dir: Path) -> list[Path]:
    if not diffs_dir.exists():
        return []
    return sorted(p for p in diffs_dir.iterdir() if p.is_file())


def apply_update(diff_path: Path) -> None:
    """Append a classified diff to the appropriate alerts/docs file.

    Not implemented in the starter scaffold.
    """
    raise NotImplementedError(
        "apply_update() is not implemented yet. "
        "Add real write logic before running without --dry-run."
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--diffs",
        type=Path,
        default=DIFFS_DIR,
        help="Directory containing diff files to apply.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List diff files without writing anything.",
    )
    args = parser.parse_args(argv)

    diffs = list_diffs(args.diffs)
    print(f"Found {len(diffs)} diff file(s) in {args.diffs}.")
    for d in diffs:
        print(f"  {d.name}")

    if args.dry_run:
        return 0

    if not diffs:
        print("No diffs to apply; nothing to do.")
        return 0

    # Live path — intentionally blocked in the starter scaffold.
    for diff in diffs:
        apply_update(diff)
    return 0


if __name__ == "__main__":
    sys.exit(main())
