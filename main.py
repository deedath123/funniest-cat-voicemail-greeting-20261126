#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — Miso the cat records her greeting.

The cat speaks for herself: she is napping in the box her human threw
out, and she has one demand plus one threat, delivered before the beep.
"""
import os

ENTRY = (
    "Hi, it's Miso. I'm napping in the box you threw out. "
    "Leave food at 4 a.m. or the vase goes next. Meow."
)


def main():
    # The gate allows 1-120 chars of UTF-8 text; refuse to write an
    # entry that would fail it, so a bad edit can never ship silently.
    if not 1 <= len(ENTRY) <= 120:
        raise ValueError("entry must be 1-120 characters, got %d" % len(ENTRY))
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
