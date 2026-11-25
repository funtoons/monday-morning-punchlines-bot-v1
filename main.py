"""Monday Morning Punchlines — one joke about Monday mornings.

Writes a single joke (at most 200 characters) to /output/entry.txt.
Deterministic, offline, standard library only: the same joke every run.
"""

import os

JOKE = (
    "Monday morning is when every 'I'll do it Monday' I said all "
    "weekend shows up at my door to collect."
)


def main() -> None:
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, must be 1-200"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Round-trip guard: the file must hold exactly the joke, no newline added.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == JOKE, "entry.txt differs from JOKE"


if __name__ == "__main__":
    main()
