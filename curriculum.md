# Curriculum

**Approach:** hybrid — build foundations bottom-up, but anchor every module to a
protein / enzyme / climate application so relevance stays concrete.

**North star:** be able to apply ML to biochemistry for climate mitigation. The
field is overwhelmingly about **proteins and enzymes**, which is good news — your
3D-spatial and sequence-modelling intuitions transfer directly.

Status legend: `[ ]` not started · `[~]` in progress · `[x]` notes + cards written.

---

## Part 0 — Foundations (lean on the physics)

- [x] **M1 · Chemical foundations of life**
  Water, hydrogen bonding & the hydrophobic effect, weak interactions, pH &
  buffers, chemical equilibrium.
  *Anchor:* why proteins fold and membranes self-assemble at all.
  → `notes/m1-chemical-foundations.md`, deck `m1-chemical-foundations`, `problems/m1-buffer-capacity.md`.

- [x] **M2 · Thermodynamics & kinetics in biology**
  Free energy (ΔG, ΔG°′), reaction coupling, ATP as energy currency; reaction
  rates, transition states, catalysis as rate enhancement.
  *Anchor:* what makes carbon-fixation reactions thermodynamically hard, and how
  cells pay for them.
  → `notes/m2-free-energy.md` + `notes/m2-coupling-and-kinetics.md`; decks
  `m2-thermodynamics` & `m2-coupling-and-kinetics`; `problems/m2-activation-barrier.md`.

## Part 1 — The molecules

- [x] **M3 · Amino acids & the peptide bond**
  The 20 standard residues, side-chain chemistry, ionisation, the peptide bond.
  *Anchor:* the "alphabet" that protein language models tokenise.
  → `notes/m3-amino-acids.md`; deck `m3-amino-acids`; `problems/m3-sequence-space.md`.

- [x] **M4 · Protein structure & the folding problem**
  Primary→quaternary structure, secondary motifs, the Ramachandran plot, folding
  thermodynamics, the PDB.
  *Anchor:* the exact object AlphaFold predicts.
  → `notes/m4-protein-structure.md`; deck `m4-protein-structure`; `problems/m4-levinthal.md`.

- [ ] **M5 · Carbohydrates & glycobiology** (lighter)
  Sugars, glycosidic bonds, polysaccharides, glycosylation.
  *Anchor:* cellulose/starch as carbon sinks; glycan complexity.

- [ ] **M6 · Lipids & membranes** (lighter)
  Fatty acids, the bilayer, membrane proteins.
  *Anchor:* compartmentalisation; biofuel feedstocks.

- [ ] **M7 · Nucleic acids**
  DNA/RNA structure, base pairing, the double helix.
  *Anchor:* the substrate of all genetic engineering.

## Part 2 — Function & catalysis

- [x] **M8 · Enzyme mechanism & catalysis**
  Active sites, transition-state stabilisation, cofactors, specificity.
  *Anchor:* RuBisCO and why it's slow & promiscuous; PETase.
  → `notes/m8-enzymes.md`; deck `m8-enzymes`; `problems/m8-rubisco-abundance.md`.

- [ ] **M9 · Enzyme kinetics** (problem-heavy)
  Michaelis–Menten, kcat/KM, inhibition, allostery.
  *Anchor:* quantifying "how good is this engineered enzyme?"

## Part 3 — Metabolism & energy (the carbon/nitrogen core)

- [ ] **M10 · Bioenergetics & the ATP economy**
- [ ] **M11 · Glycolysis & gluconeogenesis**
- [ ] **M12 · TCA cycle & oxidative phosphorylation**
- [ ] **M13 · Photosynthesis & carbon fixation**
  Light reactions, the Calvin cycle, RuBisCO, C4/CAM, photorespiration.
  *Anchor:* the single most important module for climate biochem.
- [ ] **M14 · Nitrogen metabolism & fixation**
  Nitrogenase, the nitrogen cycle.
  *Anchor:* displacing emissions-heavy Haber–Bosch fertiliser.

## Part 4 — Information & engineering

- [ ] **M15 · Central dogma**
  Replication, transcription, translation — enough to engineer.
- [ ] **M16 · Tools of molecular biology**
  PCR, sequencing, cloning, expression, CRISPR.
  *Anchor:* how you actually build and test a modified enzyme.

## Part 5 — The ML-for-bio layer (your expertise takes over)

- [ ] **M17 · Molecular representations**
  Sequences, graphs, 3D point clouds, voxels, SMILES — mapped to your CV/geospatial
  toolkit (equivariance, point clouds, tokenisation).
- [ ] **M18 · Protein structure prediction** — AlphaFold2/3, the MSA→structure idea.
- [ ] **M19 · Protein language models** — the ESM family, embeddings, zero-shot function.
- [ ] **M20 · Generative protein/enzyme design** — RFdiffusion, ProteinMPNN.
- [ ] **M21 · Property, reaction & docking prediction.**
- [ ] **M22 · Capstone directions for climate** — carbon capture, plastic degradation,
  N-fixation, biofuels: what's tractable, what's open.

---

### Notes on sequencing
We don't have to go strictly in order. The hybrid bargain: when a foundation is
needed for an application you're excited about, we detour to it, write the note,
then return. The map keeps us honest about what's still missing.
