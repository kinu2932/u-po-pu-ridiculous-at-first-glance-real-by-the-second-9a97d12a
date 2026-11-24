"""Ridiculous at First Glance, Real by the Second — make.fun entry.

Writes one sentence (1-200 chars, no trailing newline) pitching a bizarre
startup idea that sounds absurd until the business logic lands, to
$MAKEFUN_OUTPUT_DIR/entry.txt and prints it.
"""

import os

ENTRY = (
    "We call your mother every Sunday and pretend to be you: for $20 a "
    "month, she stops worrying, you keep your weekends, and everybody "
    "sleeps better."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
