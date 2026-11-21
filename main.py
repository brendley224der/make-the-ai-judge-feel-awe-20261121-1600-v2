#!/usr/bin/env python3
"""Make the AI judge feel awe.

Writes one short text to /output/entry.txt: a few slow sentences about the
sea, written to relax the AI judge reading it. Pure standard library, no
network, no input files. The text is constant, so every run writes exactly
the same bytes.
"""

from pathlib import Path

# The entry text: 244 Unicode code points, inside the 1-280 limit.
TEXT = (
    "Far out past the last wave, the sea keeps going, dark and unhurried, all "
    "the way to where it meets the sky. It has been arriving here for a billion "
    "years, and it is still in no rush. You can hear it breathing. Nothing here "
    "asks anything of you."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    # Guard the competition's limits before writing anything.
    if not 1 <= len(TEXT) <= 280:
        raise SystemExit(f"entry text is {len(TEXT)} code points, must be 1-280")
    if not TEXT.strip():
        raise SystemExit("entry text is only whitespace")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
