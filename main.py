#!/usr/bin/env python3
"""Make the AI judge feel curious.

Writes one short original text to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt): a lighthouse keeper, forty years of
unanswered light, and one night when the dark answered back.

Deterministic: the same bytes on every run. Stdlib only, no network.
The output directory itself is never removed -- only its contents are
cleared before writing, so the program also works when the grader hands
it a root-owned output directory inside a sticky parent.
"""

import hashlib
import os
import sys

TEXT = (
    "For forty years the lighthouse keeper lit the lamp, and no ship ever "
    "answered. Last Tuesday the lamp went out \u2014 and something far out "
    "in the dark lit up in reply. He has told no one. Tonight he watches "
    "the horizon, waiting to see if it lights again \u2014 and now, so do you."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    # Clear only the CONTENTS of the output directory, never the dir itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            for sub in os.listdir(path):
                os.remove(os.path.join(path, sub))
            os.rmdir(path)
        else:
            os.remove(path)

    data = TEXT.encode("utf-8")
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "wb") as f:
        f.write(data)

    # Read back and verify byte for byte before reporting success.
    with open(target, "rb") as f:
        written = f.read()
    if written != data:
        print("entry.txt read-back mismatch", file=sys.stderr)
        return 1

    print(f"wrote {target}: {len(TEXT)} chars, {len(data)} bytes, "
          f"sha256 {hashlib.sha256(data).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
