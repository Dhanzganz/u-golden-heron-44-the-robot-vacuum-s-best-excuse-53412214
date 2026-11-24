"""The Robot Vacuum's Best Excuse.

Writes one line - the funniest excuse a robot vacuum gives for
missing a spot - to /output/entry.txt.
"""

import os

ENTRY = "My sensors flagged that crumb as load-bearing, so I left it there holding the floor together."


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters.
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, must be 1-140"
    assert ENTRY.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
