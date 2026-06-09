# Protein structure & the folding problem (M4)

> How a 1D sequence becomes a specific 3D shape — and why that shape is predictable.
> The convergence point: M1 (H-bonds, hydrophobic effect) + M3 (backbone, side chains)
> → the object AlphaFold predicts.

## Mental model
Four levels of structure, but one division of labour to remember:
**the backbone makes secondary structure (local H-bonds); the side chains make tertiary
structure (distant packing, hydrophobic-effect-driven).** The sequence encodes the fold
(Anfinsen); folding is fast because the energy landscape is a funnel (Levinthal).

## Key concepts

### The four levels
1. **Primary** — the amino-acid sequence (N→C).
2. **Secondary** — local repeating backbone shapes: α-helices, β-sheets.
3. **Tertiary** — the full 3D fold of one chain.
4. **Quaternary** — multiple chains (subunits) assembled into a complex.

### Secondary structure = the BACKBONE satisfying its own H-bonds
- Every peptide unit has a polar **N–H** (δ+ donor) and **C=O** (δ− acceptor) — present
  in all residues, independent of side chain. In the water-free core these can't bond to
  water, so they **bond to each other** in regular repeating geometries.
- **α-helix:** right-handed coil; **C=O of residue *i* → N–H of residue *i+4***;
  ~3.6 residues/turn; **side chains point outward**.
- **β-sheet:** extended strands side by side; **H-bonds between adjacent strands**
  (one strand's N–H to the next's C=O); **parallel** or **antiparallel**;
  **side chains alternate** above/below the sheet.
- All H-bonds here are backbone-to-backbone. (Side chains are irrelevant to the *pattern*
  — they just hang off.)
- **Ramachandran plot:** φ vs ψ (the only backbone freedoms, since the peptide bond is
  rigid). Most combos are sterically forbidden; α-helix and β-sheet each sit in their own
  allowed basin. Glycine reaches extra regions; proline is restricted.

### Tertiary structure = the SIDE CHAINS packing
- Driven by interactions between residues *far apart in sequence* but close in space:
  - **hydrophobic effect** (greasy side chains → buried core) — dominant;
  - **salt bridges** (charged side chains, + to −; full charges, unlike an H-bond);
  - **side-chain H-bonds**, **van der Waals** packing, **disulfide bonds** (Cys–Cys).
- Large chains fold into semi-independent **domains** (modular, often functional units
  that evolution mixes and matches).

### Quaternary structure
- Multiple folded subunits assemble (same non-covalent forces). Examples: hemoglobin
  (4 subunits); **RuBisCO** is a large multi-subunit complex. **Allostery / cooperativity**
  (one subunit influencing another) emerges at this level.

### The folding problem
- **Anfinsen:** a denatured small protein refolds spontaneously to the same native
  structure ⇒ **the sequence alone encodes the fold** (it's the free-energy minimum).
  This is the premise that makes sequence→structure prediction well-defined.
- **Levinthal's paradox:** astronomically many possible conformations (φ/ψ per residue),
  so random search would exceed the age of the universe — yet folding takes µs–s.
  Resolution: folding is **funnel-guided**, not random; the landscape channels the chain
  downhill to the native state.

### The PDB and AlphaFold
- **Protein Data Bank (PDB):** public repository of experimentally determined structures
  (X-ray, NMR, cryo-EM); a structure = **3D coordinates (x,y,z) for every atom**
  (`.pdb`/`.cif`).
- **AlphaFold:** sequence in → predicted 3D atomic coordinates out; trained on the PDB.
  AF2 (2020) was the breakthrough; AF3 extends to complexes/ligands. Detail in M18.

## The maths
- Backbone freedom = dihedral angles φ, ψ per residue (Ramachandran).
- Levinthal estimate: ~k stable (φ,ψ) states per residue → kᴺ conformations; even modest
  k and N blow past any physical sampling rate. Worked in `problems/m4-levinthal.md`.

## Climate / ML anchor
- AlphaFold's output object is the literal target for any structure-based work on
  carbon-fixation enzymes, PETase, etc.
- The folding **funnel** = a well-conditioned energy landscape — the same intuition as a
  trainable loss surface; Anfinsen = "sequence→structure is a function" = why ML can
  learn it.
- **RuBisCO**'s quaternary complexity and allostery matter for any attempt to engineer it.

## Common misconceptions / things that tripped me up
- Secondary structure is **backbone** N–H/C=O H-bonds, NOT side chains. Side chains drive
  **tertiary** structure.
- An H-bond (δ+/δ−, to a lone pair) ≠ a salt bridge (full + to full − charge).
- Folding is **not** a random conformational search — it's funnel-guided.

## See also
- `notes/m1-chemical-foundations.md`, `notes/m3-amino-acids.md`.
- `flashcards/decks/m4-protein-structure.md`; `problems/m4-levinthal.md`.
- Next: M5–M7 (other molecules) or jump to M8 (enzymes) — we now have everything for it.
