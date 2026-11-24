# Seventeen Syllables of Debugging

[![make.fun](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/c/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![Rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/Rahul7039/seventeen-syllables-debugging/rank.svg)](https://make.fun/c/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![Reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/Rahul7039/seventeen-syllables-debugging/reward.svg)](https://make.fun/c/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

Entry for the [make.fun](https://make.fun/c/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
competition **Seventeen Syllables of Debugging**: one haiku about debugging,
three lines in the 5-7-5 syllable shape, at most 200 characters.

## The haiku

```
the breakpoint waits, still
a thousand lines rush past it
the bug lives elsewhere
```

- Line 1 — 5 syllables: the(1) break-point(2) waits(1) still(1)
- Line 2 — 7 syllables: a(1) thou-sand(2) lines(1) rush(1) past(1) it(1)
- Line 3 — 5 syllables: the(1) bug(1) lives(1) else-where(2)

A breakpoint set in the wrong place, watching a thousand innocent lines
stream past while the bug lives somewhere else entirely. "Still" does double
duty — motionless, and nevertheless. The last line reframes the whole scene:
the watch was perfect, the place was wrong.

## How it runs

`main.py` (Python 3.13, standard library only, no network) writes the haiku
to `/output/entry.txt`. The output is deterministic — two runs are
byte-identical — and is 82 bytes: three lines, well under the 200-character
gate.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
