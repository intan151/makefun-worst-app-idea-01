"""The Worst App Idea Ever Pitched — make.fun #99.

Writes one pitch (one sentence, <=240 chars) to /output/entry.txt.
Deterministic: stdlib only, no input, no randomness, no network.
"""

ENTRY = (
    "SnoreSync livestreams your snoring to strangers who rate each snore "
    "out of ten, because your sleep deserves an audience and your neighbours "
    "deserve a monthly subscription."
)


def main() -> None:
    import os

    # Self-check gate (mirrors the competition gate): 1-240 chars,
    # not only whitespace, no control characters. Output unchanged.
    assert 1 <= len(ENTRY) <= 240, "entry must be 1-240 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert not any(ord(c) < 32 or ord(c) == 127 for c in ENTRY), (
        "entry must not contain control characters"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
