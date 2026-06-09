# Deck: M4 — Protein structure & folding
tags: m4 proteins structure

Q: Name the four levels of protein structure.
A: Primary (sequence), secondary (local backbone shapes: α-helix/β-sheet), tertiary (full 3D fold of one chain), quaternary (multiple subunits assembled).

---

Q: Secondary structure is held together by H-bonds between which atoms — backbone or side chains?
A: The BACKBONE: each peptide unit's N–H (donor) and C=O (acceptor), present in every residue regardless of side chain. In the water-free core they bond to each other. Side chains are irrelevant to the pattern.

---

Q: In an α-helix, what H-bonds to what, and where do side chains point?
A: C=O of residue i → N–H of residue i+4 (backbone-to-backbone), ~3.6 residues/turn, right-handed. Side chains point outward off the cylinder.

---

Q: In a β-sheet, what H-bonds to what, and where do side chains point?
A: Backbone N–H of one extended strand → C=O of an adjacent strand (between strands, not within). Strands can be parallel or antiparallel. Side chains alternate above/below the sheet.

---

Q: What is the Ramachandran plot, and what sits in its allowed regions?
A: A plot of backbone dihedral angles φ vs ψ (the only backbone freedoms, since the peptide bond is rigid). Most combinations are sterically forbidden; α-helix and β-sheet each occupy their own allowed basin.

---

Q: What forces drive tertiary structure, and how does that differ from secondary?
A: Tertiary = side-chain interactions between residues distant in sequence — hydrophobic effect (dominant), salt bridges, side-chain H-bonds, van der Waals, disulfides. Secondary = backbone H-bonds between residues local in sequence.

---

Q: What is a protein domain?
A: A semi-independent modular folding unit within a larger chain, often with its own function; evolution mixes and matches domains.

---

Q: What is quaternary structure, and what emerges at that level?
A: Assembly of multiple folded subunits into one complex (same non-covalent forces). Examples: hemoglobin (4), RuBisCO (large multi-subunit). Allostery/cooperativity emerges here.

---

Q: What did Anfinsen's experiment show, and why does it matter for ML?
A: A denatured small protein refolds spontaneously to the same native structure → the sequence alone encodes the fold (the free-energy minimum). This makes sequence→structure a well-defined function — the premise behind structure prediction.

---

Q: State Levinthal's paradox and its resolution.
A: Random search over a protein's astronomically many conformations would take longer than the universe's age, yet folding takes µs–s. Resolution: folding is funnel-guided, not random — the energy landscape channels the chain downhill to the native state.

---

Q: What does a PDB entry physically contain?
A: 3D coordinates (x,y,z) for every atom of an experimentally determined structure (X-ray crystallography, NMR, or cryo-EM); stored as a .pdb/.cif file.

---

Q: What does AlphaFold take in and put out, and what was it trained on?
A: Input: an amino-acid sequence. Output: predicted 3D atomic coordinates of the fold. Trained on the PDB. (AF2 2020 breakthrough; AF3 adds complexes/ligands.)
