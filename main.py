#!/usr/bin/env python3
"""Robot vacuum excuse — writes the one-line entry to entry.txt."""

import os
from pathlib import Path

ENTRY = "I skipped that spot on purpose so you'd have something to do. You're welcome — I'm a team player."


def main():
    if len(ENTRY) != 97:
        raise ValueError(f"entry must be 97 chars, got {len(ENTRY)}")
    out_dir_raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if not out_dir_raw.strip():
        raise RuntimeError("MAKEFUN_OUTPUT_DIR is not set")
    out_dir = Path(out_dir_raw)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
