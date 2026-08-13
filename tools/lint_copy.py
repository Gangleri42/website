#!/usr/bin/env python3
"""House-rule linter for the page copy.

Fails on em-dashes and on the banned-adjective list, anywhere in the visible
text of index.html. Verbatim machine strings and code samples are exempt via
<code> elements.
"""

import re
import sys
from pathlib import Path

INDEX = Path(__file__).resolve().parent.parent / "index.html"

BANNED = [
    "seamless", "robust", "comprehensive", "cutting-edge", "leverage",
    "delve", "crucial", "pivotal", "unlock", "effortless", "empower",
    "elevate", "state-of-the-art", "revolutionary", "game-chang",
    "in today's", "moreover", "furthermore", "ultimately",
]


def visible_text(html):
    html = re.sub(r"<!--.*?-->", " ", html, flags=re.S)
    html = re.sub(r"<(script|style|code)\b.*?</\1>", " ", html, flags=re.S)
    return re.sub(r"<[^>]+>", " ", html)


def main():
    text = visible_text(INDEX.read_text())
    errors = []
    for lineno, line in enumerate(text.splitlines(), 1):
        if "—" in line:
            errors.append(f"line {lineno}: em-dash")
        low = line.lower()
        for w in BANNED:
            if w in low:
                errors.append(f"line {lineno}: banned word {w!r}")
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    print("copy clean: no em-dashes, no banned words")


if __name__ == "__main__":
    main()
