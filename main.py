"""Seventeen Syllables of Debugging — make.fun entry.

Writes one haiku about debugging (5-7-5, three lines) to /output/entry.txt.
Deterministic, stdlib only, no network, no input files.
"""

import os

HAIKU = (
    "the breakpoint waits, still\n"
    "a thousand lines rush past it\n"
    "the bug lives elsewhere\n"
)


def main() -> None:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(HAIKU)


if __name__ == "__main__":
    main()
