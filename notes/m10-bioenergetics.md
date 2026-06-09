# Bioenergetics & the ATP economy (M10)

> Consolidation + depth on M2's energy machinery, in the metabolic context. The cell's
> activated-carrier economy (ATP, NADH/NADPH, acetyl-CoA) and the catabolism/anabolism map.

## Mental model
The cell runs on a small set of **activated carriers**, each kept "charged" far from
equilibrium and each shuttling one thing: **ATP** (phosphoryl/energy), **NADH & NADPH**
(electrons), **acetyl-CoA** (acyl groups). Catabolism charges the batteries; anabolism
spends them.

## Key concepts

### Free energy, restated (M2)
- Processes run when ΔG < 0; G = H − TS.
- **Actual** ΔG depends on concentrations: ΔG = ΔG°′ + RT ln Q, Q = [products]/[reactants].
  ΔG°′ = biochemical standard (pH 7, 1 M, 25 °C). **Direction is set by actual ΔG**, which
  can differ greatly from ΔG°′ because cellular concentrations aren't 1 M.

### ATP — why it's favourable, and why it's the currency
- ATP + H₂O → ADP + Pᵢ: ΔG°′ ≈ −30.5 kJ/mol; **actual ≈ −50** (cell keeps [ATP] high,
  [ADP]/[Pᵢ] low → small Q). Favourable because: charge-repulsion relief (~4 crammed −),
  resonance stabilisation of Pᵢ, entropy (1→2), solvation. **No magic "high-energy bond."**
- **Phosphoryl-transfer hierarchy** (transfer potential = −ΔG°′ of hydrolysis, kJ/mol):
  PEP 62 > 1,3-BPG 49 > creatine-P 43 > **ATP 30.5** > glucose-6-P 14 > glycerol-3-P 9.
  Phosphate flows high→low potential. **ATP is deliberately mid-range:**
  - donors above ATP recharge ADP→ATP (e.g. PEP+ADP→pyruvate+ATP — substrate-level
    phosphorylation);
  - ATP phosphorylates acceptors below it (e.g. ATP+glucose→ADP+glucose-6-P, hexokinase).
  Mid-position = two-way universal intermediary → why one common currency works.
- ATP is **cash flow, not savings**: turned over in seconds (~body weight of ATP/day).
  Storage = fat/glycogen.

### Reducing power: NADH vs NADPH
- NAD⁺ + 2e⁻ + H⁺ → NADH (electron carrier). NADP⁺/NADPH = same chemistry + a phosphate
  "tag" so enzymes distinguish the pools.
- Cell keeps **NAD⁺/NADH high** (oxidised → poised to **accept** e⁻ → **catabolism**;
  feeds the electron transport chain) and **NADPH/NADP⁺ high** (reduced → poised to
  **donate** e⁻ → **anabolism**; fatty-acid synthesis, Calvin cycle reducing CO₂-carbon).
  Same molecule, opposite ratios, opposite jobs.

### Redox as free energy: ΔG = −nFΔE
- Electron transfer flows from low reduction potential E°′ (eager donor) to high E°′
  (eager acceptor). **ΔG°′ = −nF·ΔE°′**, ΔE°′ = E°′(acceptor) − E°′(donor),
  F ≈ 96.5 kJ·mol⁻¹·V⁻¹. Positive ΔE → negative ΔG → spontaneous. A redox potential
  difference *is* free energy in volts.
- The electron transport chain (M12): NADH (E°′ ≈ −0.32 V) → O₂ (+0.82 V), ΔE ≈ 1.14 V,
  large −ΔG captured as ATP.

### Acetyl-CoA
- Coenzyme A carries an activated acetyl group via a high-energy **thioester**; the central
  2-carbon hub feeding the TCA cycle (M12).

### Catabolism vs anabolism (the master map)
| | Catabolism | Anabolism |
|---|---|---|
| does | breaks fuels down → CO₂ | builds complex molecules |
| redox | oxidative (strips e⁻) | reductive (adds e⁻) |
| energy | releases → makes ATP + NADH | consumes ATP + NADPH |
| role | charges batteries | spends batteries |
Linked by shared currencies; separate NADH (catabolic) / NADPH (anabolic) pools prevent
short-circuits. M11/M12 = catabolism in detail; M13 = anabolism (carbon fixation).

## The maths
- ΔG = ΔG°′ + RT ln Q.
- Transfer potential = −ΔG°′(hydrolysis); flows high→low.
- ΔG°′ = −nF·ΔE°′ (redox). Worked example NADH→O₂ in `problems/`.

## Climate / ML anchor
- Carbon fixation (M13) is anabolism: it *spends* ATP + NADPH (made by the light
  reactions) to reduce CO₂ into sugar. The "energy budget of fixing carbon" is literally
  this currency accounting — relevant to any attempt to engineer more efficient fixation.

## Common misconceptions / things that tripped me up
- ΔG°′ (standard) ≠ actual ΔG (depends on concentrations) — direction follows the latter.
- ATP is a transfer intermediate, not a store; favourable because mid-range in the
  transfer hierarchy.
- NADH and NADPH are the same chemistry but kept at opposite ratios for opposite roles.
- Redox potentials are just free energy in volts (ΔG = −nFΔE).

## See also
- `notes/m2-coupling-and-kinetics.md`, `notes/m8-enzymes.md` (cofactors).
- `flashcards/decks/m10-bioenergetics.md`; `problems/m10-redox-atp-yield.md`.
- Next: M11 (glycolysis), M12 (TCA + oxidative phosphorylation), or M13 (carbon fixation).
