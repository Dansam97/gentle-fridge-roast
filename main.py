#!/usr/bin/env python3
"""Entry for make.fun bounty "Fridge Roast: One Line, Biggest Laugh".

Writes one roast line about a smart fridge to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, default /output).
"""

import os

TEXT = (
    "After last night's security patch, my smart fridge's water dispenser "
    "makes me prove I'm not a robot before every glass. I pay the mortgage "
    "here. The robot is the one asking."
)


MAX_CHARS = 200


def render() -> bytes:
    """Return the exact bytes for entry.txt, validated against the gate.

    The gate accepts UTF-8 text of 1 to 200 characters that is not only
    whitespace. The file holds the line plus one trailing newline, and the
    whole file must stay inside the cap, so validate the full content.
    """
    content = TEXT + "\n"
    encoded = content.encode("utf-8")  # raises if not encodable
    if not TEXT.strip():
        raise ValueError("entry text must not be only whitespace")
    if not 1 <= len(content) <= MAX_CHARS:
        raise ValueError(f"entry is {len(content)} chars, gate is 1-{MAX_CHARS}")
    return encoded


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(render())


if __name__ == "__main__":
    main()
