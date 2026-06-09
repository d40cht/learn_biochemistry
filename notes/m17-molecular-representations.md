# Molecular representations & NN architectures (M17)

> A survey pass (a "fun diversion" after M10) — the map of neural-network approaches to
> molecules and proteins, organised by representation. To be deepened later (GNN math,
> equivariance derivations, AlphaFold internals, hands-on Colab toys). The learner is an
> expert ML engineer; the value-add here is connecting architectures to what the molecules
> physically *are* (M1–M10).

## Mental model
**In molecular ML the architecture is downstream of the representation.** How you encode
the molecule (sequence / graph / 3D geometry) dictates the model and its inductive biases.
That choice is the whole game — this module is fundamentally about representations.

## Representation → architecture map
| Representation | What it is | Architecture | Good for | Biochem anchor |
|---|---|---|---|---|
| 1D sequence | residues / nucleotides / SMILES | RNN, transformer (protein LMs) | function, embeddings, generation | the M3 alphabet; ESM |
| 2D graph | atoms = nodes, bonds = edges | GNN / message passing | small-molecule properties | a molecule *is* a graph |
| 3D geometry | atoms with (x,y,z) | equivariant / geometric nets | structure, energy, binding | the M4 fold; AlphaFold |
| 3D voxel grid | molecule on a grid | 3D CNN | pockets (legacy) | wasteful, not rotation-aware |
| surface / mesh | molecular surface | geometric DL (MaSIF) | interaction interfaces | where proteins touch |

## GNNs — the natural fit for molecules
- A molecule is literally a graph: atoms = nodes (features: element, charge,
  hybridisation), bonds = edges (single/double/aromatic).
- **Message passing:** each atom repeatedly aggregates messages from bonded neighbours and
  updates its state; after L rounds each atom encodes its environment out to L hops —
  mirroring chemistry (neighbours + functional groups, M1/M3).
- Right inductive biases: **permutation invariance** (no canonical atom order) + locality.
  A readout pools nodes → molecule-level property (solubility, toxicity, reactivity).
- **Limitation:** a plain GNN sees only 2D topology — blind to 3D conformation, which is
  decisive for binding/catalysis. → need geometry.

## Geometric / equivariant nets — the frontier (and where proteins live)
- Generalises CNN **translation equivariance** to the full 3D symmetry group: rotate/
  translate the molecule and energy is **invariant**, forces **equivariant** (SE(3)/E(3)).
  Hard-coding this symmetry = big data-efficiency win.
- Three flavours:
  - **Invariant via distances/angles:** feed only rotation-invariant quantities — SchNet
    (distances), DimeNet (+ angles), GemNet (+ dihedrals).
  - **Equivariant tensor features** (spherical harmonics / tensor products): Tensor Field
    Networks, SE(3)-Transformer, e3nn, NequIP, MACE — SOTA **ML force fields** (≈ quantum
    accuracy, ~10⁶× faster than DFT; relevant to simulating M8 transition states).
  - **Frame-based:** AlphaFold2's structure module — per-residue local frames +
    **Invariant Point Attention**.

## The protein stack (where the climate targets sit)
- **Sequence LMs:** ESM2 — transformer masked-LM on tens of millions of sequences;
  embeddings recover structure/function unsupervised (the M3 "embedding rediscovers the
  side-chain families" point).
- **Structure prediction:** AlphaFold2 (MSA → Evoformer → IPA structure module);
  AlphaFold3 (diffusion-based, handles complexes/ligands/nucleic acids); ESMFold
  (LM-based, single-sequence, fast).
- **Design:** ProteinMPNN (graph net, **inverse folding** — sequence given a backbone);
  RFdiffusion (diffusion over backbones, **de novo** design).

## Climate / ML through-line
The whole pipeline maps onto what we've built: predict a variant's stability/efficiency
(GNN → M9 ΔΔG/k_cat) · get its fold (AlphaFold) · find/reshape the active site (M8) ·
**design** a better RuBisCO / hydrogenase / carbonic anhydrase (ProteinMPNN, RFdiffusion).
ML force fields (equivariant nets) could even simulate the catalytic chemistry itself.

## To deepen later (this was only a survey)
- GNN message-passing math; expressivity limits (WL test), 3D-aware GNNs.
- Equivariance properly: why distance-based MP is automatically invariant; what tensor
  features add; e3nn mechanics.
- AlphaFold2/3 internals (Evoformer, IPA, the diffusion variant).
- Protein LMs (ESM) — objectives, what embeddings encode, zero-shot variant effects.
- Hands-on Colab toys: RDKit molecule → graph → tiny message-passing net; fetch carbonic
  anhydrase from the PDB (Biopython/py3Dmol), inspect the Zn²⁺ active site, pull an ESM
  embedding.

## See also
- `notes/m3-amino-acids.md` (the alphabet), `notes/m4-protein-structure.md` (the fold /
  AlphaFold object), `notes/m8-enzymes.md` (active sites), `notes/m9-enzyme-kinetics.md`
  (the objectives to predict).
- Curriculum Part 5 (M18–M22) — the detailed treatments this previews.
