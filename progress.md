# Progress log

Chronological record of what we've covered. I (Claude) read this at the start of a
session to know where we are and what's due for review. Newest entries on top.

Format per entry:
- **date** — module/topic — what we did — artifacts written — what to test next time.

---

- **2026-06-09** — **M8 covered (a big one, very Socratic).** Enzyme catalysis built
  almost entirely from the learner's own questions. Core: enzymes lower Eₐ by stabilising
  the TRANSITION STATE, not the substrate (binding substrate tightly = anti-catalysis);
  binding energy spent on differential TS binding + proximity/orientation (entropy
  pre-payment); active site = the 3D fold; induced fit; geometry vs electrostatic
  preorganisation (latter usually dominant); the 5 catalytic strategies (His acid–base
  star); cofactors/coenzymes extend the toolkit; product release = weak product binding
  (fits TS not product), with the bind-TS-tight-but-release-product-loose tension and
  product inhibition / diffusion limit. Long detailed-balance thread: a catalyst CANNOT
  change equilibrium (same TS both ways; 2nd-law/perpetual-motion argument; binding
  asymmetries cancel for free S/P; Haldane relationship). Direction comes from ΔG°
  (P below S); ΔG°=0 → catalyses both ways equally; big −ΔG° (ATP-coupled) = the real
  irreversible "ratchet", not the enzyme. Case studies: carbonic anhydrase (Zn²⁺ →
  hydroxide nucleophile, His proton shuttle, diffusion-limited, carbon-capture target)
  and RuBisCO (slow ~3/s, sloppy → photorespiration ~25% loss, speed–specificity
  trade-off = the binding trade-off realised globally, prime ML target).
  Artifacts: `notes/m8-enzymes.md`, deck `m8-enzymes` (16 cards),
  `problems/m8-rubisco-abundance.md` (10⁶/3 ≈ 3×10⁵ → why it's the most abundant protein).
  **What to test next time:** TS-stabilisation & the anti-catalysis trap; TS analogs;
  proximity/entropy; induced fit; geometry-vs-electrostatics; the 5 strategies; why
  cofactors; product release & the design tension; no-ratchet/Haldane; ΔG°=0 case;
  carbonic anhydrase Zn mechanism; RuBisCO's two failings + why stuck + why ML target.
  **Next:** M9 (enzyme kinetics — Michaelis–Menten, k_cat, K_M, k_cat/K_M, diffusion
  limit; quantitative, suits the learner's maths) then M13 (photosynthesis/Calvin cycle,
  where RuBisCO lives — the big climate module).

- **2026-06-09** — **M4 covered.** Protein structure: the four levels; secondary
  structure as the BACKBONE satisfying its own H-bonds (α-helix C=O i→N–H i+4; β-sheet
  between adjacent strands; side chains point out; Ramachandran φ/ψ basins); tertiary
  structure driven by SIDE-CHAIN interactions (hydrophobic effect dominant) between
  residues distant in sequence; domains; quaternary structure (subunits, allostery,
  RuBisCO/hemoglobin). Folding problem: Anfinsen (sequence encodes fold = free-energy
  min) + Levinthal (funnel, not random search). PDB = 3D atomic coords; AlphaFold:
  sequence → coords. Correction made: secondary H-bonds are backbone N–H/C=O, NOT side
  chains (the learner's instinct was right but misattributed to side chains); H-bond ≠
  salt bridge.
  Artifacts: `notes/m4-protein-structure.md`, deck `m4-protein-structure`,
  `problems/m4-levinthal.md` (3¹⁰⁰ ≈ 5×10⁴⁷ conformations → 10²⁷ yr).
  **What to test next time:** backbone-vs-side-chain (secondary vs tertiary); α-helix
  i→i+4; β-sheet between strands; Ramachandran; Anfinsen; Levinthal+funnel; what AF
  in/outputs.
  **Next:** M8 (enzymes) — we now have all prerequisites (kinetics, structure, side-chain
  chemistry). Could instead do the lighter M5–M7 (carbs/lipids/nucleic acids) first, but
  enzymes is where the climate payoff begins (RuBisCO, carbonic anhydrase, PETase).

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
