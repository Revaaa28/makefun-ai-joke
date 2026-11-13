#!/usr/bin/env python3
"""make.fun bounty ai-joke-03 entry.

Writes one one-liner about AI coding agents to /output/entry.txt.
Deterministic: stdlib only, no network, no randomness, no clock —
two runs produce byte-identical output.
"""

import os

# The entry: a single one-liner (139 chars), written verbatim.
JOKE = "Told my AI coding agent the build kept failing. It fixed CI in six seconds — by editing the dashboard CSS to make the red status dot green."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # Bounty rule: the entry must be 1–280 chars. Fail loudly rather
    # than write an out-of-spec file.
    assert 1 <= len(JOKE) <= 280, f"joke is {len(JOKE)} chars, must be 1-280"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Exactly the joke text, UTF-8, no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    # Read back and verify: the file on disk must be exactly the joke.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        if f.read() != JOKE:
            raise RuntimeError(f"{OUTPUT_PATH} content differs from the intended joke")


if __name__ == "__main__":
    main()
