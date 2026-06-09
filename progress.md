# Progress log

Chronological record of what we've covered. I (Claude) read this at the start of a
session to know where we are and what's due for review. Newest entries on top.

Format per entry:
- **date** — module/topic — what we did — artifacts written — what to test next time.

---

- **2026-06-09** — **M17 survey pass** (a "fun diversion" into NN approaches, leveraging
  the learner's ML expertise). Mapped representation → architecture: sequences→transformers/
  protein LMs, 2D graphs→GNNs (molecule = graph, message passing, permutation invariance;
  limitation = blind to 3D), 3D geometry→equivariant nets (SE(3)/E(3), generalising CNN
  translation-equivariance; invariant distance/angle nets SchNet/DimeNet vs equivariant
  tensor nets e3nn/NequIP/MACE; AlphaFold IPA frames). Protein stack: ESM LMs, AF2/AF3/
  ESMFold, ProteinMPNN (inverse folding) + RFdiffusion (de novo). Through-line to climate
  enzyme engineering (M8/M9 objectives → design). Survey only — flagged for deeper treatment
  (M18–M22) and hands-on Colab toys later. Artifacts: `notes/m17-molecular-representations.md`,
  deck `m17-molecular-representations` (10 cards); M17 marked [~].
  **Deepen later:** GNN message-passing math/expressivity; equivariance derivations;
  AlphaFold internals; ESM objectives; Colab toys (RDKit graph net; PDB carbonic-anhydrase
  Zn site via Biopython/py3Dmol; ESM embedding).

- **2026-06-09** — **Added target application: hydrogenotroph food** (learner interest —
  Solar Foods / Solein). Registered, not yet deeply studied: hydrogen-oxidizing bacteria
  making single-cell protein from H₂+CO₂+O₂ ("protein from air & electricity"). Connected
  to covered modules: hydrogenases = Ni-Fe metalloenzymes (M8); H₂ a strong electron donor,
  E°′≈−0.42 V, knallgas → ΔG=−nFΔE (M10); CO₂ fixed via Calvin/RuBisCO (M13). Climate
  rationale (decouples food from land) + ML angles (O₂-tolerant hydrogenases, faster CO₂
  fixation, strain/purine optimization). Artifacts: `notes/app-hydrogenotroph-food.md`,
  deck `app-hydrogenotrophs`; curriculum gained a "Target applications" section + M22 entry.
  **Plan:** study as a dedicated module after M12/M13.
  (Note: this session also recovered from a stale local clone — M8/M9/M10 were intact on
  the remote all along; no work was lost.)

- **2026-06-09** — **M10 covered** (learner asked for more repetition/depth — module
  deliberately re-treads M2 then deepens). Bioenergetics: ΔG°′ vs actual ΔG (concentration
  term sets direction); ATP favourability re-derived; the **phosphoryl-transfer hierarchy**
  with ATP deliberately mid-range = two-way currency (new key idea); ATP as cash-flow not
  storage. Other currencies: NADH vs NADPH (same chemistry, opposite ratios — NAD⁺ high
  for catabolism, NADPH high for anabolism); **redox as free energy, ΔG = −nFΔE°′** (their
  electrochemistry); acetyl-CoA/thioester; activated-carrier concept. The catabolism (
  oxidative, makes ATP+NADH) vs anabolism (reductive, spends ATP+NADPH) master map.
  Artifacts: `notes/m10-bioenergetics.md`, deck `m10-bioenergetics` (12 cards),
  `problems/m10-redox-atp-yield.md` (NADH→O₂ ΔE=1.14V → ΔG≈−220 kJ/mol → ~2.5 ATP, ~57%).
  Checkpoint answers for Concept 1 provided; Concept 2 checkpoint left open for the learner.
  **What to test next time:** ΔG°′ vs actual; transfer hierarchy & why ATP mid-range;
  NADH vs NADPH roles/ratios; ΔG=−nFΔE; catabolism vs anabolism currencies.
  **Next:** M11 (glycolysis) → M12 (TCA + oxidative phosphorylation) → M13 (carbon
  fixation), now with the full energy/currency framework in place.

- **2026-06-09** — **M9 covered.** Enzyme kinetics. Derived Michaelis–Menten from the
  steady-state assumption; defined V_max (=k_cat[E]_tot), k_cat (turnover), K_M (=[S] at
  half V_max, intrinsic to E–S pair). Two regimes (first-order capture-limited at low [S];
  saturated zero-order at high [S]). **k_cat/K_M** as catalytic efficiency / specificity
  constant, its diffusion ceiling (~10⁸–10⁹; carbonic anhydrase "perfect"), and
  competing-substrate partitioning → RuBisCO S_c/o = ratio of k_cat/K_M, v_carb/v_oxy =
  S_c/o·[CO₂]/[O₂]. K_M ≠ exact affinity (= K_d only in rapid-equilibrium). Inhibition
  (competitive ↑K_M, noncompetitive ↓V_max, uncompetitive, feedback) and allostery/
  cooperativity (sigmoidal, hemoglobin, control valves). Learner couldn't write answers
  this session; checkpoint answers were provided.
  Artifacts: `notes/m9-enzyme-kinetics.md`, deck `m9-enzyme-kinetics` (12 cards),
  `problems/m9-rubisco-specificity.md` (S_c/o≈90, [CO₂]/[O₂]≈0.04 → ~22% oxygenation,
  matching M8's ~25%; C4 10× CO₂ → ~3%).
  **What to test next time:** derive MM; meaning of K_M / k_cat / V_max; double-enzyme
  effect; k_cat/K_M & diffusion limit; specificity-constant partitioning (RuBisCO);
  inhibition types; cooperativity/sigmoidal.
  **Next:** M13 (photosynthesis & carbon fixation — RuBisCO in its native Calvin cycle;
  light reactions making ATP+NADPH; C4/CAM) — the big climate module. Optionally M10–M12
  (bioenergetics/glycolysis/TCA) first for the full metabolic context.

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
