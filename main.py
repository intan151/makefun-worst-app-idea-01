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

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
