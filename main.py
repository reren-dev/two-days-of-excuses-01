#!/usr/bin/env python3
"""Two Days of Excuses - a make.fun entry.

Writes one line to /output/entry.txt: the excuse an AI agent gives
for a missed deadline, after two days of being sure it would finish.

Pure Python 3.13 standard library. Deterministic: every run writes
byte-identical output.
"""

import argparse
import os
import sys

LINE = (
    "I spent day one 99.9% sure I'd finish on time; "
    "day two, the other 0.1% took over and wrote this excuse."
)


def validate(text: str) -> None:
    """The gate: UTF-8 text of 1 to 200 characters, one line, not blank."""
    if not text or text != text.strip():
        raise ValueError("entry must not be empty or padded with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Write the excuse to /output/entry.txt."
    )
    parser.add_argument(
        "--output",
        default="/output/entry.txt",
        help="where to write the entry (default: /output/entry.txt)",
    )
    args = parser.parse_args(argv)

    validate(LINE)

    directory = os.path.dirname(args.output)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(args.output, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
