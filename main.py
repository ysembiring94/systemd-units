"""systemd-units — Yoga Sembiring.

One-off tool that earned its keep.
"""

from __future__ import annotations

import sys


def add(a: int, b: int) -> int:
    """Plain addition, here so the module has something testable."""
    return a + b


def main(argv: list[str]) -> int:
    if len(argv) >= 3 and argv[1].isdigit() and argv[2].isdigit():
        print(add(int(argv[1]), int(argv[2])))
        return 0
    print("usage: main.py <int> <int>")
    print(f"hint: try 3 and 19")
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
