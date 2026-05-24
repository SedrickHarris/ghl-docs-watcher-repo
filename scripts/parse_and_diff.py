#!/usr/bin/env python3
"""Parse snapshots and produce diffs against the previous run.

Starter skeleton. Real parsing and diffing are not implemented.
Use `--dry-run` to inspect what the script would process without
performing any work.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SNAPSHOTS_DIR = REPO_ROOT / "sources" / "snapshots"
DIFFS_DIR = REPO_ROOT / "sources" / "diffs"


def list_snapshots(snapshots_dir: Path) -> list[Path]:
    if not snapshots_dir.exists():
        return []
    return sorted(p for p in snapshots_dir.iterdir() if p.is_file())


def diff_snapshots(previous: Path, current: Path) -> str:
    """Produce a unified diff between two snapshot files.

    Not implemented in the starter scaffold.
    """
    raise NotImplementedError(
        "diff_snapshots() is not implemented yet. "
        "Add a real differ before running without --dry-run."
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--snapshots",
        type=Path,
        default=SNAPSHOTS_DIR,
        help="Directory containing snapshot files.",
    )
    parser.add_argument(
        "--diffs",
        type=Path,
        default=DIFFS_DIR,
        help="Directory where diff files will be written.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List snapshots without diffing.",
    )
    args = parser.parse_args(argv)

    snapshots = list_snapshots(args.snapshots)
    print(f"Found {len(snapshots)} snapshot file(s) in {args.snapshots}.")
    for s in snapshots:
        print(f"  {s.name}")

    if args.dry_run:
        return 0

    if len(snapshots) < 2:
        print("Need at least two snapshots to diff; nothing to do.")
        return 0

    # Live path — intentionally blocked in the starter scaffold.
    diff_snapshots(snapshots[-2], snapshots[-1])
    return 0


if __name__ == "__main__":
    sys.exit(main())
