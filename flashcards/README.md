# Flashcards (spaced repetition)

Plain-markdown decks that are the single source of truth. They're readable in the
repo, I can quiz you from them directly in chat, and they convert to Anki.

## Deck format

One file per deck in `decks/`. Header lines, then cards separated by `---`:

```
# Deck: Amino Acids
tags: proteins foundations m3

Q: How many standard (proteinogenic) amino acids are there?
A: 20.

---

Q: What part of an amino acid varies between the 20 standard residues?
A: The side chain (R group); all share the same amino + carboxyl + alpha-carbon backbone.
```

- `Q:` may span multiple lines (until the line beginning `A:`).
- `A:` runs until the next `---` or end of file.
- `tags:` is optional; tokens are space-separated and applied to every card in the deck.

## Reviewing

**In chat:** ask e.g. "quiz me on the amino-acids deck" — I'll test free recall.

**In Anki:**
```
python flashcards/build_anki.py
```
This writes two kinds of output to `flashcards/build/` (which is git-ignored, so
regenerate it whenever you need it):

- **`learn_biochemistry.apkg`** — a single Anki package with every deck as a subdeck
  under `Biochemistry::` (e.g. `Biochemistry::M3 — Amino acids`). One-tap import on
  AnkiDroid (open the file) or desktop (*File → Import*). No AnkiWeb account needed.
  Re-importing after a rebuild updates existing cards rather than duplicating them
  (notes carry a stable GUID derived from their content).
- **`<deck>.tsv`** — one tab-separated file per deck, for manual import. The header
  lines tell Anki to use tabs, treat the 3rd column as tags, and render HTML.

The `.apkg` is the easy path, especially on mobile. Use the TSVs only if you want
fine-grained control over deck/field mapping at import time.
