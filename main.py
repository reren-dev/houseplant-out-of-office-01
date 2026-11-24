#!/usr/bin/env python3
"""Houseplant Out-of-Office entry for make.fun.

One fixed out-of-office reply, written as if a houseplant sent it. The
script checks the reply against the bounty gate (a single line of 1 to 120
characters) and writes it to the entry file the grader reads.
"""

import os
from pathlib import Path
import sys

ENTRY_LINE = "Out of office: I'm on strike. No water since March, so I'm charging rent for the oxygen — payable in sunlight."
LIMIT = 120


def write_entry() -> None:
    line = ENTRY_LINE.strip()
    problems = []
    if not line:
        problems.append("empty")
    if "\n" in line or "\r" in line:
        problems.append("not one line")
    if len(line) > LIMIT:
        problems.append(f"{len(line)} chars, over {LIMIT}")
    if problems:
        sys.exit("entry invalid: " + "; ".join(problems))
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line, encoding="utf-8")
    print(f"entry.txt: {len(line)} characters")

if __name__ == "__main__":
    write_entry()
