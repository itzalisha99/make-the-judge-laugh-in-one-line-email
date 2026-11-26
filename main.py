#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — entry program.

Writes one funny line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

The line: an umbrella takes revenge. A stranger gets it in one read,
the setup (I insulted it) breaks into a spiteful weather grudge, and
the laugh lands on the last four words.
"""

import os

LINE = "I called my umbrella useless. It has rained every day since, purely out of spite."


def validate(text):
    """Mirror the bounty gate: UTF-8, 1-200 chars, not only whitespace,
    a single line. Fail loudly instead of shipping a bad entry."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8
    return text


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read it back and prove the file is byte-for-byte the validated line.
    with open(path, "rb") as f:
        written = f.read()
    if written.decode("utf-8") != LINE:
        raise ValueError("read-back mismatch: file is not the validated line")
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
