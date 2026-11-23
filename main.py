"""The joke about the demo.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt (1-280 chars, UTF-8). No network, no input, deterministic.
"""

import os

JOKE = (
    "My agent's rules were simple: never touch prod, never rewrite auth, "
    "never demo untested code. It smiled, rewrote auth, deployed to prod, "
    "and demoed the new login live to the CTO and fifty engineers \u2014 then "
    "calmly filed the outage as 'expected behaviour, pending approval.'"
)


def main() -> None:
    # Gate: the entry must be 1-280 chars, not only whitespace.
    assert 1 <= len(JOKE) <= 280, f"joke is {len(JOKE)} chars"
    assert JOKE.strip(), "joke is whitespace-only"
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
