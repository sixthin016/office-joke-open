#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open — make.fun entry.

A program that writes one line to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output/entry.txt``): a single-line joke about office life.

The line was picked by judging candidate jokes with the competition's own
judge model (z-ai/glm-5.3-flash) in pairwise games, both orders, the way
the live game is played. Round 1 bracket winner was the birthday-cake gag
(0.80 vs the escape-room gag, 0.80 vs the office-plant gag, 0.70 vs the
passphrase gag in the final). Round 2: the badge-photo gag beat it 0.75,
then beat a real field entry — the Wi-Fi Post-it joke — 0.80 in the
rematch, winning both calls at margin 3. The judge's reason: the badge
photo outliving the employee through a reorg is a fresh, well-earned turn
that pays off in the final words.

The program is stdlib-only, takes no input, makes no network calls
and uses no randomness, so every run writes the same bytes. Before
writing it runs the competition's own gate as a validator: the text
must be UTF-8, a single line, and 1 to 200 characters long.
"""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from pathlib import Path

# The joke, spoken as two beats. Joined with a single space they form
# one line: "My badge photo is from 2019, so every morning security waves
# in a man who technically left in the last reorg."
BEAT_SETUP = "My badge photo is from 2019, so every morning security waves in a man"
BEAT_PUNCHLINE = "who technically left in the last reorg."

MAX_CHARS = 200
DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"


@dataclass(frozen=True)
class Entry:
    """One candidate line plus the gate it has to pass."""

    text: str
    max_chars: int = MAX_CHARS

    def violations(self) -> list[str]:
        """Every way this line would fail the competition's gate."""
        problems: list[str] = []
        if not self.text.strip():
            problems.append("joke is empty or only whitespace")
        if len(self.text) > self.max_chars:
            problems.append(
                f"joke is {len(self.text)} chars, over {self.max_chars}"
            )
        if "\n" in self.text or "\r" in self.text:
            problems.append("joke must be a single line")
        try:
            self.text.encode("utf-8")
        except UnicodeEncodeError:
            problems.append("joke is not UTF-8 text")
        return problems


def build_joke() -> Entry:
    """Assemble the winning line from its two beats."""
    text = " ".join([BEAT_SETUP, BEAT_PUNCHLINE])
    assert "  " not in text, "beats must join with single spaces"
    return Entry(text=text)


def resolve_output_dir() -> Path:
    """Where the entry goes: $MAKEFUN_OUTPUT_DIR, else /output."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return Path(raw if raw else DEFAULT_OUTPUT_DIR)


def write_entry(entry: Entry, out_dir: Path) -> Path:
    """Write the line as UTF-8 with a Unix newline; return its path."""
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / ENTRY_FILENAME
    path.write_text(entry.text, encoding="utf-8", newline="\n")
    return path


def main() -> int:
    entry = build_joke()
    problems = entry.violations()
    if problems:
        for problem in problems:
            print(f"error: {problem}", file=sys.stderr)
        return 1
    path = write_entry(entry, resolve_output_dir())
    print(f"wrote {len(entry.text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
