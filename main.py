#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes a single sentence (at most 280 characters) recalling a childhood
memory to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Stdlib only, no network, fully deterministic.
"""

import os

ENTRY = (
    "On summer evenings my grandmother stood at the stove in her faded "
    "apron, steam from the rice fogging her glasses as she called us in "
    "from the yard, and the kitchen has been quiet ever since, though I "
    "still listen for her voice whenever the rice steams."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 280, f"entry is {len(text)} characters"
    assert text.count(".") <= 1 or text.endswith("."), "must be one sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
