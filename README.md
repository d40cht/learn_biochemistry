# learn_biochemistry

A self-directed course in biochemistry for an experienced ML engineer, aimed at
eventually applying machine learning to biochemistry **in the service of climate
mitigation**.

## Who this is for

- Strong ML background (vision / geospatial / transformers).
- Physics degree (rusty, but the maths survived) → we lean hard on
  thermodynamics, kinetics, and electrostatics and skip the hand-holding.
- Goal: reach the point of doing useful ML-on-biochemistry for climate
  (carbon-fixation enzymes, plastic degradation, nitrogen fixation, methane
  oxidation, biofuels).

## How we work together

The **learning happens in chat**. The **repo is the memory and the test bank.**

1. We work through a topic conversationally.
2. Once a concept is absorbed, we write it up as a note in `notes/`.
3. We distil the must-remember facts into spaced-repetition cards in
   `flashcards/decks/`.
4. Quantitative ideas get a worked problem in `problems/`.
5. `progress.md` logs what's been covered so I know what to test you on, and so
   future sessions have continuity (this container is ephemeral — only what's
   committed survives).

## Layout

| Path | Purpose |
|------|---------|
| `curriculum.md`       | The full module map + status. The plan of record. |
| `progress.md`         | Chronological log of sessions, notes, cards. Drives review. |
| `notes/`              | Conceptual write-ups, one file per topic. |
| `problems/`           | Worked quantitative problems (kinetics, thermo, equilibria). |
| `flashcards/decks/`   | Spaced-repetition cards in plain markdown. |
| `flashcards/build_anki.py` | Converts decks → Anki-importable TSV. |

## The two ways to review

- **In chat:** ask me to "quiz me on enzyme kinetics" and I read the relevant
  deck + notes and test you (free recall, not multiple choice).
- **In Anki:** run `python flashcards/build_anki.py` and import the generated
  TSV files from `flashcards/build/`.

See `curriculum.md` for the path and `notes/_template.md` for the note format.
