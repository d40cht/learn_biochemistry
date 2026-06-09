#!/usr/bin/env python3
"""Convert plain-markdown flashcard decks into Anki-importable files.

Source of truth: flashcards/decks/*.md  (see flashcards/README.md for the format).
Outputs (in flashcards/build/):
  - <deck>.tsv                 one tab-separated file per deck (manual import)
  - learn_biochemistry.apkg    a single Anki package, all decks as subdecks of
                               "Biochemistry::" — one-tap import on AnkiDroid/desktop

Run from anywhere:  python flashcards/build_anki.py
Stdlib only (no genanki); builds the .apkg as an Anki SQLite collection in a zip.
"""
from __future__ import annotations

import hashlib
import html
import json
import re
import sqlite3
import sys
import zipfile
from pathlib import Path

DECKS_DIR = Path(__file__).resolve().parent / "decks"
BUILD_DIR = Path(__file__).resolve().parent / "build"
APKG_NAME = "learn_biochemistry.apkg"
DECK_PARENT = "Biochemistry"

# A single shared "Basic" note type (Front/Back) used by every card.
MODEL_ID = 1607392319000  # arbitrary fixed id; stable across rebuilds

# Fixed timestamps + content-derived ids make the .apkg byte-stable across rebuilds,
# so the committed package only changes when card content changes (no spurious diffs).
EPOCH_S = 1700000000   # 2023-11-14, arbitrary fixed "creation" time
EPOCH_MS = EPOCH_S * 1000
ZIP_DATE = (2023, 11, 14, 0, 0, 0)

# base91 alphabet used by Anki/genanki for note GUIDs (no quote/backslash).
BASE91 = (
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    "!#$%&()*+,-./:;<=>?@[]^_`{|}~"
)


# --------------------------------------------------------------------------- #
# Parsing
# --------------------------------------------------------------------------- #
def parse_deck(text: str, fallback_name: str) -> tuple[str, list[str], list[tuple[str, str]]]:
    """Return (deck_name, tags, [(question, answer), ...]) for one deck file."""
    name = fallback_name
    tags: list[str] = []
    body_lines: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# Deck:"):
            name = stripped.split(":", 1)[1].strip() or fallback_name
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
    return name, tags, cards


def to_field(text: str) -> str:
    """Escape HTML special chars (so '<', '>' show literally) then keep newlines as <br>."""
    return html.escape(text, quote=False).replace("\n", "<br>")


# --------------------------------------------------------------------------- #
# .apkg helpers
# --------------------------------------------------------------------------- #
def base91(num: int) -> str:
    if num == 0:
        return BASE91[0]
    out = []
    while num:
        num, rem = divmod(num, len(BASE91))
        out.append(BASE91[rem])
    return "".join(reversed(out))


def guid_for(*values) -> str:
    digest = hashlib.sha256("__".join(str(v) for v in values).encode("utf-8")).digest()
    return base91(int.from_bytes(digest[:8], "big"))


def field_checksum(text: str) -> int:
    stripped = re.sub("<[^>]+>", "", text)
    return int(hashlib.sha1(stripped.encode("utf-8")).hexdigest()[:8], 16)


def stable_deck_id(name: str, used: set[int]) -> int:
    did = int(hashlib.sha256(name.encode("utf-8")).hexdigest(), 16) % (1 << 31)
    while did <= 1 or did in used:
        did += 1
    used.add(did)
    return did


def basic_model(now_ms: int) -> dict:
    return {
        "id": MODEL_ID,
        "name": "Biochem Basic",
        "type": 0,
        "mod": now_ms // 1000,
        "usn": -1,
        "sortf": 0,
        "did": 1,
        "tmpls": [{
            "name": "Card 1", "ord": 0,
            "qfmt": "{{Front}}",
            "afmt": "{{FrontSide}}\n\n<hr id=answer>\n\n{{Back}}",
            "bqfmt": "", "bafmt": "", "did": None, "bfont": "", "bsize": 0,
        }],
        "flds": [
            {"name": "Front", "ord": 0, "sticky": False, "rtl": False, "font": "Arial", "size": 20, "media": []},
            {"name": "Back", "ord": 1, "sticky": False, "rtl": False, "font": "Arial", "size": 20, "media": []},
        ],
        "css": ".card{font-family:arial;font-size:20px;text-align:center;color:#000;background:#fff;}"
               "hr#answer{margin:1em 0;}",
        "latexPre": "\\documentclass[12pt]{article}\n\\begin{document}\n",
        "latexPost": "\\end{document}",
        "latexsvg": False,
        "req": [[0, "any", [0]]],
        "tags": [], "vers": [],
    }


def deck_entry(did: int, name: str, now_s: int) -> dict:
    return {
        "id": did, "name": name, "mod": now_s, "usn": -1,
        "lrnToday": [0, 0], "revToday": [0, 0], "newToday": [0, 0], "timeToday": [0, 0],
        "collapsed": False, "browserCollapsed": False, "desc": "",
        "dyn": 0, "conf": 1, "extendNew": 0, "extendRev": 0,
    }


def default_dconf() -> dict:
    return {"1": {
        "id": 1, "name": "Default", "replayq": True, "autoplay": True, "timer": 0,
        "maxTaken": 60, "usn": -1, "mod": 0,
        "new": {"perDay": 20, "delays": [1, 10], "separate": True, "ints": [1, 4, 7],
                "initialFactor": 2500, "bury": False, "order": 1},
        "rev": {"perDay": 200, "fuzz": 0.05, "ivlFct": 1, "maxIvl": 36500, "ease4": 1.3,
                "bury": False, "minSpace": 1},
        "lapse": {"delays": [10], "mult": 0, "minInt": 1, "leechFails": 8, "leechAction": 1},
    }}


def collection_conf() -> dict:
    return {
        "nextPos": 1, "estTimes": True, "activeDecks": [1], "sortType": "noteFld",
        "timeLim": 0, "sortBackwards": False, "addToCur": True, "curDeck": 1,
        "newBury": True, "newSpread": 0, "dueCounts": True, "curModel": str(MODEL_ID),
        "collapseTime": 1200,
    }


SCHEMA = """
CREATE TABLE col (id integer primary key, crt integer not null, mod integer not null,
  scm integer not null, ver integer not null, dty integer not null, usn integer not null,
  ls integer not null, conf text not null, models text not null, decks text not null,
  dconf text not null, tags text not null);
CREATE TABLE notes (id integer primary key, guid text not null, mid integer not null,
  mod integer not null, usn integer not null, tags text not null, flds text not null,
  sfld integer not null, csum integer not null, flags integer not null, data text not null);
CREATE TABLE cards (id integer primary key, nid integer not null, did integer not null,
  ord integer not null, mod integer not null, usn integer not null, type integer not null,
  queue integer not null, due integer not null, ivl integer not null, factor integer not null,
  reps integer not null, lapses integer not null, left integer not null, odue integer not null,
  odid integer not null, flags integer not null, data text not null);
CREATE TABLE revlog (id integer primary key, cid integer not null, usn integer not null,
  ease integer not null, ivl integer not null, lastIvl integer not null, factor integer not null,
  time integer not null, type integer not null);
CREATE TABLE graves (usn integer not null, oid integer not null, type integer not null);
CREATE INDEX ix_notes_usn on notes (usn);
CREATE INDEX ix_cards_usn on cards (usn);
CREATE INDEX ix_revlog_usn on revlog (usn);
CREATE INDEX ix_cards_nid on cards (nid);
CREATE INDEX ix_cards_sched on cards (did, queue, due);
CREATE INDEX ix_revlog_cid on revlog (cid);
CREATE INDEX ix_notes_csum on notes (csum);
"""


def _stable_id(used: set[int], *parts: str) -> int:
    """A deterministic, unique, ms-timestamp-shaped integer id from content."""
    n = int(hashlib.sha256("::".join(parts).encode("utf-8")).hexdigest(), 16) % (10 ** 12) + 10 ** 12
    while n in used:
        n += 1
    used.add(n)
    return n


def build_apkg(decks: list[tuple[str, list[str], list[tuple[str, str]]]], out_path: Path) -> int:
    decks_json = {"1": deck_entry(1, "Default", EPOCH_S)}
    used_deck_ids: set[int] = set()
    used_ids: set[int] = set()

    db_path = BUILD_DIR / "collection.anki2"
    if db_path.exists():
        db_path.unlink()
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.executescript(SCHEMA)

    due = 1
    card_count = 0
    for deck_name, tags, cards in decks:
        full_name = f"{DECK_PARENT}::{deck_name}"
        did = stable_deck_id(full_name, used_deck_ids)
        decks_json[str(did)] = deck_entry(did, full_name, EPOCH_S)
        tag_str = (" " + " ".join(tags) + " ") if tags else ""
        for question, answer in cards:
            nid = _stable_id(used_ids, "nid", full_name, question)
            cid = _stable_id(used_ids, "cid", full_name, question)
            flds = to_field(question) + "\x1f" + to_field(answer)
            cur.execute(
                "INSERT INTO notes VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                (nid, guid_for(full_name, question), MODEL_ID, EPOCH_S, -1, tag_str,
                 flds, re.sub("<[^>]+>", "", to_field(question)), field_checksum(question), 0, ""),
            )
            cur.execute(
                "INSERT INTO cards VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (cid, nid, did, 0, EPOCH_S, -1, 0, 0, due, 0, 0, 0, 0, 0, 0, 0, 0, ""),
            )
            due += 1
            card_count += 1

    cur.execute(
        "INSERT INTO col VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (1, EPOCH_S, EPOCH_MS, EPOCH_MS, 11, 0, 0, 0,
         json.dumps(collection_conf()), json.dumps({str(MODEL_ID): basic_model(EPOCH_MS)}),
         json.dumps(decks_json), json.dumps(default_dconf()), json.dumps({})),
    )
    con.commit()
    con.close()

    data = db_path.read_bytes()
    db_path.unlink()
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for name, payload in (("collection.anki2", data), ("media", b"{}")):
            info = zipfile.ZipInfo(name, date_time=ZIP_DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            zf.writestr(info, payload)
    return card_count


# --------------------------------------------------------------------------- #
def main() -> int:
    if not DECKS_DIR.exists():
        print(f"No decks directory at {DECKS_DIR}", file=sys.stderr)
        return 1

    deck_files = sorted(DECKS_DIR.glob("*.md"))
    if not deck_files:
        print(f"No decks found in {DECKS_DIR}. Nothing to build.")
        return 0

    BUILD_DIR.mkdir(exist_ok=True)
    parsed: list[tuple[str, list[str], list[tuple[str, str]]]] = []
    total = 0
    repo_root = BUILD_DIR.parent.parent

    for deck_file in deck_files:
        name, tags, cards = parse_deck(deck_file.read_text(encoding="utf-8"), deck_file.stem)
        parsed.append((name, tags, cards))
        out = BUILD_DIR / f"{deck_file.stem}.tsv"
        tag_str = " ".join(tags)
        with out.open("w", encoding="utf-8") as fh:
            fh.write("#separator:tab\n#html:true\n#tags column:3\n")
            for question, answer in cards:
                fh.write(f"{to_field(question)}\t{to_field(answer)}\t{tag_str}\n")
        print(f"{deck_file.name}: {len(cards)} cards -> {out.relative_to(repo_root)}")
        total += len(cards)

    apkg_path = BUILD_DIR / APKG_NAME
    n = build_apkg(parsed, apkg_path)
    print(f"Packaged {n} cards into {apkg_path.relative_to(repo_root)} "
          f"({len(parsed)} subdecks under '{DECK_PARENT}::')")
    print(f"Built {total} cards from {len(deck_files)} deck(s) into {BUILD_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
