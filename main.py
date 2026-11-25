"""Funniest One-Line Bio for an AI on a Dating App.

Writes a single-line dating-app bio (<=180 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only; no network, no randomness, no file reads outside this repo.
"""

import os
import sys

BIO = (
    "My last date said I was 'too predictable' \u2014 I'd already predicted "
    "she'd say that, word for word, three days early. Looking for someone "
    "whose next move I can't compute."
)

MAX_CHARS = 180


def validate_bio(text):
    if not text or not text.strip():
        raise ValueError("bio must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError("bio is %d chars, over the %d limit" % (len(text), MAX_CHARS))
    if "\n" in text:
        raise ValueError("bio must be a single line")
    return text


def main():
    bio = validate_bio(BIO)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    # Clean only the contents of the output dir, never the dir itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path):
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(bio)
    return 0


if __name__ == "__main__":
    sys.exit(main())
