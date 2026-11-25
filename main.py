#!/usr/bin/env python3
"""The Excuse That Almost Works: the single line a gamer texts the boss
to get out of work during GTA 6 launch week.

Writes exactly the line to /output/entry.txt, no trailing newline.
"""

import os

# The excuse: the car failed its MOT on a cracked spring and the garage
# has it till lunchtime. Fresh angle, away from the boiler/plumber/leak
# cluster and from flat tyres and fevers: a specific, boring, everyday
# car problem with a real part name and a hard time boundary, in plain
# hurried words with no greeting, no explanation and no sign-off. It
# never mentions GTA 6 -- that would give the game away to the boss.

LINE = "Car failed its MOT on a cracked spring, garage has it till lunchtime, I'll be in after."


def main() -> None:
    # Gate guard: the sealed scorer needs 1-140 chars, UTF-8, not only
    # whitespace, exactly one line. Fail loudly here rather than ship
    # an invalid entry.
    assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
    assert LINE.strip() == LINE and "\n" not in LINE, "must be one clean line"
    assert len(LINE.split()) <= 20, "line must be at most 20 words"
    assert all(c.isprintable() for c in LINE), "must be plain text"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
