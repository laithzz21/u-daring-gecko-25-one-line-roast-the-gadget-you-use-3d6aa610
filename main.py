#!/usr/bin/env python3
"""One-line roast entry for make.fun bounty
u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT if set).
Python 3.13, stdlib only, deterministic: no network, clock or randomness.
"""

import os

ENTRY_TEXT = (
    "My smartwatch throws a standing ovation every time I stand up, "
    "like fetching the TV remote is an Olympic sport."
)


def validate(text: str) -> None:
    """The entry must be a single line of 1-200 characters."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def resolve_output_path() -> str:
    """$MAKEFUN_OUTPUT wins; otherwise /output, falling back to ./output
    when /output is not writable."""
    if os.environ.get("MAKEFUN_OUTPUT"):
        return os.environ["MAKEFUN_OUTPUT"]
    try:
        os.makedirs("/output", exist_ok=True)
        probe = "/output/.write-test"
        with open(probe, "w", encoding="utf-8") as f:
            f.write("ok")
        os.remove(probe)
        return "/output/entry.txt"
    except OSError:
        return os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "output", "entry.txt")


def main() -> int:
    validate(ENTRY_TEXT)
    output_path = resolve_output_path()
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT + "\n")
    # Verify the written file by reading it back.
    with open(output_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY_TEXT + "\n":
        raise RuntimeError(f"read-back mismatch in {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
