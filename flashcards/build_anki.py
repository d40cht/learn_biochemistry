#!/usr/bin/env python3
"""Convert plain-markdown flashcard decks into Anki-importable TSV files.

Source of truth: flashcards/decks/*.md  (see flashcards/README.md for the format).
Output:          flashcards/build/<deck>.tsv

Run from anywhere:  python flashcards/build_anki.py
Stdlib only.
"""
from __future__ import annotations

import sys
from pathlib import Path

DECKS_DIR = Path(__file__).resolve().parent / "decks"
BUILD_DIR = Path(__file__).resolve().parent / "build"


def parse_deck(text: str) -> tuple[list[str], list[tuple[str, str]]]:
    """Return (tags, [(question, answer), ...]) for one deck file."""
    tags: list[str] = []
    body_lines: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# Deck:"):
            continue
        if stripped.lower().startswith("tags:"):
            tags = stripped.split(":", 1)[1].split()
            continue
        body_lines.append(line)

    cards: list[tuple[str, str]] = []
    for block in "\n".join(body_lines).split("\n---\n"):
        block = block.strip()
        if not block:
            continue
        q_lines: list[str] = []
        a_lines: list[str] = []
        target = None
        for line in block.splitlines():
            if line.lstrip().startswith("Q:"):
                target = q_lines
                line = line.split("Q:", 1)[1]
            elif line.lstrip().startswith("A:"):
                target = a_lines
                line = line.split("A:", 1)[1]
            if target is not None:
                target.append(line)
        question = "\n".join(q_lines).strip()
        answer = "\n".join(a_lines).strip()
        if question and answer:
            cards.append((question, answer))
    return tags, cards


def to_tsv(field: str) -> str:
    """Make a field safe for tab-separated, HTML-rendered Anki import."""
    return field.replace("\t", " ").replace("\n", "<br>")


def main() -> int:
    if not DECKS_DIR.exists():
        print(f"No decks directory at {DECKS_DIR}", file=sys.stderr)
        return 1

    deck_files = sorted(DECKS_DIR.glob("*.md"))
    if not deck_files:
        print(f"No decks found in {DECKS_DIR}. Nothing to build.")
        return 0

    BUILD_DIR.mkdir(exist_ok=True)
    total = 0
    for deck_file in deck_files:
        tags, cards = parse_deck(deck_file.read_text(encoding="utf-8"))
        out = BUILD_DIR / f"{deck_file.stem}.tsv"
        tag_str = " ".join(tags)
        with out.open("w", encoding="utf-8") as fh:
            fh.write("#separator:tab\n#html:true\n#tags column:3\n")
            for question, answer in cards:
                fh.write(f"{to_tsv(question)}\t{to_tsv(answer)}\t{tag_str}\n")
        print(f"{deck_file.name}: {len(cards)} cards -> {out.relative_to(BUILD_DIR.parent.parent)}")
        total += len(cards)

    print(f"Built {total} cards from {len(deck_files)} deck(s) into {BUILD_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
