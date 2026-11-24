#!/usr/bin/env python3
"""The Rosemary Note -- Make the Judge Smile entry.

Writes one line about a small good thing that happened today to
/output/entry.txt. The line is fixed on purpose: the same warm moment,
every run, so the two grading runs agree byte for byte.
"""

import os

LINE = (
    "My neighbor Artie left a heavy terracotta pot of winter-weary "
    "rosemary outside my screen door with a note saying it smelled "
    "like pine and forgiveness."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    line = LINE.strip()
    if not line:
        raise SystemExit("entry line is empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"entry line is {len(line)} chars, over the {MAX_CHARS} limit"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)
    # Read back what was written: the grading runs read this file, so
    # fail loudly here instead of silently shipping a wrong entry.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != line:
        raise SystemExit("read-back mismatch: entry.txt does not hold the line")
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
