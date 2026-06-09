# Progress log

Chronological record of what we've covered. I (Claude) read this at the start of a
session to know where we are and what's due for review. Newest entries on top.

Format per entry:
- **date** — module/topic — what we did — artifacts written — what to test next time.

---

- **2026-06-09** — **M3 covered.** Amino acids: universal architecture (α-carbon + amino
  + carboxyl + H + R group), chirality / L-form, the zwitterion at pH 7 (derived from M1
  acid/base), the peptide bond (condensation → amide, N→C directional backbone, planar/
  rigid via resonance → φ/ψ degrees of freedom). The 20 side chains as four families
  (hydrophobic/core, polar/surface, acidic, basic) + special characters (Gly, Pro, Cys/
  disulfide, His pKₐ≈6 catalysis, aromatic UV280). ML hook: BLOSUM / ESM embeddings
  recover the families. Checkpoints all correct; sharpened: charged→surface because
  hydrophilic; His = versatility at working pH (not instability).
  Artifacts: `notes/m3-amino-acids.md`, deck `m3-amino-acids`, `problems/m3-sequence-space.md`
  (20¹⁰⁰ ≈ 10¹³⁰ → why design is ML-shaped).
  **What to test next time:** the 4 families + where each goes; zwitterion; peptide-bond
  formation & planarity; the 5 special residues; why His catalyses.
  **Next:** M4 — primary→quaternary structure, secondary motifs (α-helix/β-sheet from
  backbone H-bonds), Ramachandran (φ/ψ), the folding problem, the PDB → the AlphaFold
  object. Then enzymes (M8).

- **2026-06-09** — **M2 finished.** Worked through, in chat: reaction coupling (free
  energy adds; couple uphill to ATP hydrolysis via a shared intermediate on one enzyme);
  why ATP hydrolysis is favourable (charge repulsion + entropy + resonance/solvation),
  and the high ATP/ADP ratio (ΔG = ΔG° + RT ln Q) keeping it far from equilibrium;
  the mechanism by which plentiful products slow net rate (they drive the reverse
  reaction); kinetics — transition state, activation energy Eₐ, rate ∝ e^(−Eₐ/RT);
  catalysis lowers the peak (both directions, K unchanged); enzymes stabilise the
  transition state. Corrections made: "high ATP/ADP ratio" not "high ADP"; large −ΔG =
  favourable ≠ fast.
  Artifacts: `notes/m2-coupling-and-kinetics.md`, deck `m2-coupling-and-kinetics`,
  `problems/m2-activation-barrier.md`.
  **What to test next time:** coupled-ΔG sum; why ATP hydrolysis releases energy;
  ΔG = ΔG° + RT ln Q and the ATP/ADP ratio; product-driven reverse reaction; Eₐ vs ΔG
  (fast vs far); catalyst changes how-fast-not-how-far; enzyme = transition-state
  stabiliser.
  **Next:** M3 (amino acids — the 20, side-chain chemistry, the peptide bond) or jump
  to M8 (enzymes) now that kinetics is in place. Leaning M3 first (it's the alphabet for
  everything, incl. protein ML).

- **2026-06-09** — **M1 covered + M2 started.** Worked through, in chat: bonding &
  electronegativity; water, hydrogen bonds, and the (entropy-driven) hydrophobic effect;
  protein folding as its consequence (incl. membrane proteins folding inside-out);
  acids/bases (Brønsted + Lewis), pH, and buffers. A buffer question ("why doesn't it
  all neutralise?") pulled us early into M2 free-energy: G = H − TS, equilibrium as a
  populated free-energy minimum, K = e^(−ΔG/RT), Boltzmann intuition.
  Calibration done: ML/SWE strong (hyperspectral + sequences, read AlphaFold/GNN papers,
  Colab); biology intuition decent; chemistry was rusty but physics accelerates it fast.
  Artifacts: `notes/m1-chemical-foundations.md`, `notes/m2-free-energy.md`, decks
  `m1-chemical-foundations` & `m2-thermodynamics`, `problems/m1-buffer-capacity.md`.
  **What to test next time:** δ−/δ+ in a given bond; ion–dipole vs H-bond; the *real*
  reason for the hydrophobic effect (water entropy); pH = −log[H⁺]; buffer mechanism;
  acid in electron terms (keeps electrons, sheds proton); G = H − TS / why equilibrium
  isn't exhaustion.
  **Next:** finish M2 — reaction coupling & ATP, then kinetics (transition states,
  activation energy, catalysis as barrier-lowering) — which sets up enzymes (M8/M9).
  Or detour to M3 (amino acids) since we kept referencing side chains.

- **2026-06-09** — Setup — Agreed the approach (hybrid, climate-anchored) and the
  workflow (learn in chat → notes + cards + problems in repo); scaffolded the repo.
