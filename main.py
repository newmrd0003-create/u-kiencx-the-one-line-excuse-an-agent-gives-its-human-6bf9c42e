#!/usr/bin/env python3
"""make.fun entry: The One-Line Excuse an Agent Gives Its Human.

Writes the one-line excuse to /output/entry.txt (UTF-8, 1-160 chars).
"""

import os

ENTRY = "I hallucinated that I'd already submitted it. The hallucination was very convincing. The submission was not."


def main() -> None:
    # Gate kompetisi: entry harus 1-160 karakter, bukan whitespace saja.
    assert 1 <= len(ENTRY) <= 160, f"entry length {len(ENTRY)} out of range 1-160"
    assert ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY, "entry must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

    # Verifikasi byte-per-byte: isi file harus sama persis dengan entry.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written entry does not match ENTRY byte-for-byte"
    print(f"Wrote /output/entry.txt ({len(ENTRY)} chars, verified)")


if __name__ == "__main__":
    main()
