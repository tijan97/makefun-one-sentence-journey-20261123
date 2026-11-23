#!/usr/bin/env python3
"""One Sentence, One Journey.

Writes a single complete story about a journey, told in exactly one
sentence, to /output/entry.txt. Deterministic: the same bytes on every run.
Standard library only; no network, no files outside the repository.
"""

import os

STORY = (
    "When the night train out of Marrakech stalled in the Atlas foothills, "
    "Layla traded her last dirham for a shepherd's lantern and walked the "
    "dark pass alone, arriving at dawn in a village that had no road at "
    "all \u2014 only woodsmoke, sleeping goats, and her grandmother's house, "
    "its door already open."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
