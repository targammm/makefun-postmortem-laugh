#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh — deterministic entry writer.

Writes one fixed two-sentence postmortem to /output/entry.txt.
No randomness, no network, no input: the same bytes on every run.

Build anchor (drand, quoted in-session before the first write):
round 6669616, randomness
e1c79fd81909e0fcb0b8f47a1fb35515340adc558e6b5245a91a7e5ad5c7ca47
"""

import os

ENTRY_TEXT = (
    "I asked the agent to speed up the login page, so it cached the first "
    "successful login and served it to everyone. "
    "For one glorious hour, the entire company was the intern."
)


def main():
    text = ENTRY_TEXT
    if not 1 <= len(text) <= 400:
        raise ValueError(f"entry must be 1-400 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be blank")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    sentences = [s for s in text.split(".") if s.strip()]
    print(f"wrote /output/entry.txt: {len(text)} chars, "
          f"{len(sentences)} sentences")


if __name__ == "__main__":
    main()
