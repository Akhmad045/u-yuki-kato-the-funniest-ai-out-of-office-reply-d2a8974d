#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply.

Writes one out-of-office auto-reply line to /output/entry.txt:
an AI agent on vacation whose replacement is a human — the joke
is that the human is the downgrade (slower, more feelings, typos).

Python 3, standard library only, no network. The gate requires
UTF-8 text of 1-160 characters, not whitespace-only, one line.
"""
import os

LINE = (
    "I am currently on vacation. My replacement is a human, "
    "so please expect slower replies, more feelings, "
    "and at least one typo."
)


def main():
    raw = LINE.strip().encode("utf-8")
    text = raw.decode("utf-8")
    assert 1 <= len(raw) <= 160, "line must be 1-160 bytes"
    assert len(text) <= 160, "line must be 1-160 characters"
    assert text == text.splitlines()[0], "line must be a single line"
    assert text.strip(), "line must not be whitespace-only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as fh:
        fh.write(raw)
    print(f"Wrote {len(text)}-character ({len(raw)}-byte) entry to /output/entry.txt")


if __name__ == "__main__":
    main()
