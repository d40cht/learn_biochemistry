# Deck: M17 — Molecular representations & NN architectures
tags: m17 ml representations

Q: What is the organising principle of molecular ML?
A: The architecture is downstream of the representation. How you encode the molecule (sequence / graph / 3D geometry) dictates the model and its inductive biases.

---

Q: Match representation to architecture: sequence, 2D graph, 3D geometry.
A: Sequence → transformers / protein LMs; 2D graph (atoms+bonds) → GNN / message passing; 3D geometry (xyz) → equivariant/geometric nets.

---

Q: Why is a GNN the natural model for a molecule?
A: A molecule IS a graph (atoms = nodes, bonds = edges). Message passing aggregates neighbour info over L hops, mirroring chemical environments/functional groups, with the right inductive biases: permutation invariance + locality.

---

Q: What is the key limitation of a plain (2D) GNN on molecules?
A: It sees only topology — it's blind to 3D conformation, which is decisive for binding and catalysis. You need geometric/3D-aware models for those.

---

Q: What symmetry do 3D molecular networks need, and how does it relate to CNNs?
A: SE(3)/E(3) equivariance — rotate/translate the molecule and energy is invariant, forces equivariant. It generalises the translation equivariance of CNNs to include 3D rotations; hard-coding it is a big data-efficiency win.

---

Q: Two ways to build rotation-aware molecular nets?
A: (1) Invariant: feed only distances/angles (SchNet, DimeNet, GemNet). (2) Equivariant tensor features via spherical harmonics/tensor products (e3nn, NequIP, MACE, SE(3)-Transformer) — SOTA ML force fields.

---

Q: What are ESM2 protein language models, and what do their embeddings capture?
A: Transformer masked-LMs trained on tens of millions of sequences; their embeddings recover structure/function unsupervised (e.g. clustering by the M3 side-chain families).

---

Q: Contrast AlphaFold2, AlphaFold3, and ESMFold.
A: AF2: MSA → Evoformer → Invariant-Point-Attention structure module. AF3: diffusion-based, handles complexes/ligands/nucleic acids. ESMFold: language-model-based, single-sequence, faster.

---

Q: What do ProteinMPNN and RFdiffusion do?
A: ProteinMPNN: inverse folding — a graph net that designs a sequence for a given backbone. RFdiffusion: a diffusion model that generates de novo protein backbones.

---

Q: How does the protein-ML stack map onto the climate enzyme-engineering goal?
A: GNN → predict variant stability/efficiency (M9 ΔΔG/k_cat); AlphaFold → fold & active site (M8); ProteinMPNN/RFdiffusion → design better RuBisCO/hydrogenase/carbonic anhydrase; equivariant force fields → simulate the catalytic chemistry.
