"""Angry Judge: The Short Rant Contest — make.fun entry.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt, at most 400 characters. The rant is about the computer
that asked to restart for updates, was told "not now", waited until the
one meeting that could not be missed, restarted anyway, and then asked
the owner to rate the experience. The punch comes fast, on the last line.
"""

import os

ENTRY = (
    "My computer asked if it could restart to install updates. "
    "I said 'not now'. It waited until I was mid-sentence in the one "
    "meeting I couldn't miss, then restarted anyway, and when it came "
    "back it asked me to rate the experience."
)

MAX_CHARS = 400


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
