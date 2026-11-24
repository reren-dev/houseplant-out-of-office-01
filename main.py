#!/usr/bin/env python3
"""The Houseplant Out-of-Office -- make.fun entry.

Prints one out-of-office auto-reply, written as if a houseplant sent it,
to /output/entry.txt. The reply is a fixed string, so repeated runs are
byte-identical; the joke is the entry itself.
"""

import os
import sys

LINE = (
    "Out of office: I'm on strike. No water since March, so I'm "
    "charging rent for the oxygen \u2014 payable in sunlight."
)

MAX_CHARS = 120


def main() -> int:
    text = LINE.strip()
    if not text:
        print("error: entry line is empty", file=sys.stderr)
        return 1
    if any(c in text for c in "\r\n"):
        print("error: entry line must be a single line", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: entry line is {len(text)} chars, over the "
            f"{MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
