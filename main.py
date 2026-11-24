"""Seventeen Syllables of Debugging — make.fun entry.

Writes one haiku about debugging (5-7-5, three lines) to /output/entry.txt.
Deterministic, stdlib only, no network, no input files.
"""

import os
import string

LINES = (
    "the breakpoint waits, still",
    "a thousand lines rush past it",
    "the bug lives elsewhere",
)

# Syllable counts for every word used in the haiku. Keeping this explicit
# (rather than guessing with a vowel-counting heuristic) makes the 5-7-5
# check below exact for the words this entry actually uses.
WORD_SYLLABLES = {
    "the": 1,
    "breakpoint": 2,
    "waits": 1,
    "still": 1,
    "a": 1,
    "thousand": 2,
    "lines": 1,
    "rush": 1,
    "past": 1,
    "it": 1,
    "bug": 1,
    "lives": 1,
    "elsewhere": 2,
}

EXPECTED_LINE_SYLLABLES = (5, 7, 5)


def line_syllables(line: str) -> int:
    """Return the syllable total for one haiku line."""
    total = 0
    for token in line.split():
        word = token.strip(string.punctuation).lower()
        try:
            total += WORD_SYLLABLES[word]
        except KeyError:
            raise ValueError(f"no syllable count known for word: {word!r}") from None
    return total


def check_haiku_structure() -> None:
    """Fail loudly if the haiku ever drifts from the 5-7-5 structure."""
    actual = tuple(line_syllables(line) for line in LINES)
    if actual != EXPECTED_LINE_SYLLABLES:
        raise ValueError(
            f"haiku must be 5-7-5 syllables, got {actual}"
        )


def render_haiku() -> str:
    check_haiku_structure()
    return "\n".join(LINES) + "\n"


def main() -> None:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(render_haiku())


if __name__ == "__main__":
    main()
