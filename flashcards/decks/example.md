# Deck: Example (format demo)
tags: meta example

Q: What is the source-of-truth format for flashcards in this repo?
A: Plain markdown decks in flashcards/decks/, with Q:/A: pairs separated by ---. They convert to Anki via build_anki.py.

---

Q: How do you regenerate the Anki-importable decks?
A: Run `python flashcards/build_anki.py`; TSVs land in flashcards/build/.
