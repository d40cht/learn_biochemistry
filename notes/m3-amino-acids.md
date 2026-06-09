# Amino acids & the peptide bond (M3)

> The 20 building blocks of proteins and how they link. The key move: don't memorise
> 20 molecules — learn one backbone + four side-chain families (defined by M1 chemistry)
> + a few special characters.

## Mental model
Every amino acid is the *same molecule* with one swappable part (the side chain). For
each side chain ask the M1 question: **in water, does it want the surface or the buried
core?** That sorts almost everything.

## Key concepts

### Universal architecture
A central **α-carbon** bonded to four groups:
1. **amino group** –NH₂ (a base),
2. **carboxyl group** –COOH (an acid),
3. a **hydrogen**,
4. the **side chain (R group)** — the only thing that differs between the 20.

### Chirality
The α-carbon carries four different groups (except glycine, R = H) → a **chiral centre**
→ two mirror-image forms. **Life uses almost exclusively the L form.** (Real
stereochemistry; D vs L is a 3D distinction structure models must respect.)

### Zwitterion (M1 in action)
At pH ~7.4 the carboxyl has donated its proton (**–COO⁻**, negative) and the amino group
has grabbed one (**–NH₃⁺**, positive) → a free amino acid carries **both charges at
once** (net neutral). Predictable straight from acid/base chemistry.

### The peptide bond
- The **carboxyl of one** residue + the **amino of the next** react, splitting out
  **water** (a **condensation**/dehydration reaction). The link (–C(=O)–N(H)–) is an
  **amide**, called a **peptide bond**. A chain = a **polypeptide**.
- **Directional backbone:** repeating N–Cα–C=O runs from the **N-terminus** (free amino)
  to the **C-terminus** (free carboxyl). Sequences are read/written **N → C** — the same
  direction protein LMs tokenise.
- **Planar & rigid:** the peptide C–N has partial double-bond character via **resonance**
  with the adjacent C=O (M1 idea again), locking the unit into a plane and blocking
  rotation about that bond. Rotation is allowed only at the two bonds flanking each
  α-carbon → the backbone's real degrees of freedom are the dihedral angles **φ and ψ**
  (sets up the Ramachandran plot & secondary structure in M4).

### The four side-chain families
| Family | Examples | At pH 7 | Where it goes / what it does |
|--------|----------|---------|------------------------------|
| **Nonpolar / hydrophobic** | Ala, Val, Leu, Ile, Met, Phe (+ Gly, Pro, Trp) | neutral, greasy | **buried in core** (drives folding); lines membrane surfaces & greasy pockets |
| **Polar, uncharged** | Ser, Thr, Asn, Gln, Tyr, Cys | neutral, δ± | **surface**; hydrogen-bonding; active-site chemistry |
| **Acidic / negative** | Asp, Glu | **–COO⁻** | surface; salt bridges; bind cations/substrates |
| **Basic / positive** | Lys, Arg, His | **–NH₃⁺ etc.** | surface; salt bridges; bind anions (e.g. DNA phosphate) |

### Special characters
- **Glycine (Gly):** R = H. Tiny, achiral, most flexible → enables tight turns.
- **Proline (Pro):** side chain bonds back to its own backbone N → rigid ring that
  **kinks the chain and breaks α-helices**. The disruptor.
- **Cysteine (Cys):** –SH thiol; two Cys oxidise to a covalent **disulfide bond
  (–S–S–)** — the one covalent staple in an otherwise weak-force fold. Redox-sensitive.
- **Histidine (His):** imidazole, **pKₐ ≈ 6** → exists as both protonated (+) and neutral
  at physiological pH, so it can act as **acid OR base** mid-reaction → the go-to
  proton-shuttle / acid–base catalyst in active sites (M8).
- **Aromatics (Phe, Tyr, Trp):** flat rings that **π-stack**; Trp/Tyr give proteins their
  **UV absorbance at 280 nm** (how protein concentration is measured).

## Climate / ML anchor
- The four families *are* what learned representations recover. Hand-built bioinformatics
  uses hydrophobicity scales and **substitution matrices (BLOSUM)** that make
  chemically-similar swaps cheap (Leu↔Ile) and wild ones expensive (Asp↔Trp). **ESM**
  protein-LM embeddings, trained with no such labels, cluster into these same
  physicochemical families (M19 — "the embedding rediscovers M3").
- Designing/engineering an enzyme (e.g. better RuBisCO, a tougher PETase) is choosing
  which residues sit where — i.e. manipulating these families in 3D.

## Common misconceptions / things that tripped me up
- A free amino acid is a **zwitterion** (both charges), not neutral-uncharged.
- Charged residues go to the **surface** because they're hydrophilic (solvated), and
  burying a bare charge in the core is costly — not just "because they're charged."
- Histidine's value is **versatility at working pH** (can give or take a proton), not
  "instability."

## See also
- `notes/m1-chemical-foundations.md` (acids/bases, hydrophobic effect),
  `notes/m2-coupling-and-kinetics.md` (catalysis).
- `flashcards/decks/m3-amino-acids.md`; `problems/m3-sequence-space.md`.
- Next: M4 — primary→quaternary structure, secondary motifs, Ramachandran (φ/ψ),
  the folding problem, the PDB → the exact object AlphaFold predicts.
