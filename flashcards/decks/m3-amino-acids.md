# Deck: M3 — Amino acids & the peptide bond
tags: m3 proteins foundations

Q: What four groups are bonded to an amino acid's α-carbon?
A: An amino group (–NH₂), a carboxyl group (–COOH), a hydrogen, and a variable side chain (R group). Only the R group differs between the 20.

---

Q: Why are amino acids chiral, and which form does life use?
A: The α-carbon has four different groups (except glycine, R=H) → a chiral centre with two mirror images. Life uses almost exclusively the L form.

---

Q: What is the charge state of a free amino acid at physiological pH, and what's it called?
A: A zwitterion: carboxyl donated its proton (–COO⁻, negative) and amino group grabbed one (–NH₃⁺, positive) — both charges at once, net neutral.

---

Q: How does a peptide bond form, and what type of bond is it?
A: The carboxyl of one residue condenses with the amino group of the next, releasing water (a condensation/dehydration reaction). The bond is an amide, called a peptide bond.

---

Q: In which direction are protein sequences read/written, and what are the ends called?
A: N-terminus (free amino) → C-terminus (free carboxyl). Same direction protein language models tokenise.

---

Q: Why is the peptide bond planar and rigid, and what's the consequence?
A: Resonance gives the C–N partial double-bond character (shared with the adjacent C=O), locking the unit flat and blocking rotation. Rotation is allowed only at the bonds flanking the α-carbon → backbone freedom = dihedral angles φ and ψ.

---

Q: Name the four side-chain families.
A: Nonpolar/hydrophobic; polar uncharged; acidic/negative (Asp, Glu); basic/positive (Lys, Arg, His).

---

Q: In a soluble protein folded in water, where do hydrophobic vs charged side chains go, and why?
A: Hydrophobic → buried core (hydrophobic effect). Charged → surface (hydrophilic, solvated by water; burying a bare charge is costly).

---

Q: What's special about glycine and proline?
A: Glycine: R = H — tiny, achiral, most flexible (enables tight turns). Proline: side chain bonds back to its backbone N → rigid ring that kinks the chain and breaks α-helices.

---

Q: How and why does cysteine stabilise a fold?
A: Its thiol (–SH) can oxidise with another cysteine's to form a covalent disulfide bond (–S–S–) — the one covalent cross-link among otherwise weak folding forces.

---

Q: Why is histidine the favourite acid–base catalyst in enzyme active sites?
A: Its pKₐ ≈ 6, so at physiological pH it exists as both protonated (+) and neutral forms — it can donate OR accept a proton mid-reaction and reset. Versatility at working pH.

---

Q: Why do proteins absorb UV light at 280 nm, and why is that useful?
A: The aromatic side chains tryptophan and tyrosine absorb at 280 nm; the absorbance is used to measure protein concentration.

---

Q: ML hook — what do ESM protein-LM embeddings rediscover about side chains?
A: Trained with no chemistry labels, per-residue embeddings cluster into the same physicochemical families (hydrophobic/polar/acidic/basic) that BLOSUM matrices and hydrophobicity scales encode by hand.
