#!/usr/bin/env python3
"""Fetch HighLevel documentation pages listed in config/watched-pages.json.

Starter skeleton. Live fetching is intentionally disabled — `fetch_page`
raises NotImplementedError. Use `--dry-run` to inspect the configured
pages without attempting any network call.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = REPO_ROOT / "config" / "watched-pages.json"
SNAPSHOTS_DIR = REPO_ROOT / "sources" / "snapshots"


def load_config(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def fetch_page(url: str) -> str:
    """Fetch a single page and return its body as text.

    Not implemented in the starter scaffold. Implement deliberately,
    with review, before enabling any watched page.
    """
    raise NotImplementedError(
        "Live fetching is disabled in the starter scaffold. "
        "Implement fetch_page() before enabling any watched page."
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=Path,
        default=CONFIG_PATH,
        help="Path to watched-pages.json (default: repo config).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List configured pages without fetching.",
    )
    args = parser.parse_args(argv)

    config = load_config(args.config)
    pages = config.get("pages", [])
    enabled = [p for p in pages if p.get("enabled")]

    print(f"Loaded {len(pages)} watched page(s); {len(enabled)} enabled.")
    for page in pages:
        state = "enabled" if page.get("enabled") else "disabled"
        verify = " [verify_before_enabling]" if page.get("verify_before_enabling") else ""
        print(f"  [{state}]{verify} {page.get('id')} -> {page.get('url')}")

    if args.dry_run:
        return 0

    if not enabled:
        print("No pages enabled; nothing to fetch.")
        return 0

    # Live path — intentionally blocked in the starter scaffold.
    for page in enabled:
        fetch_page(page["url"])

    return 0


if __name__ == "__main__":
    sys.exit(main())
