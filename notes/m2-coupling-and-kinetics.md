# Reaction coupling, ATP, and kinetics (M2)

> Completes M2. The free-energy half (which way / how far) is in
> `m2-free-energy.md`. This note: how cells *pay* for uphill reactions (coupling +
> ATP), and the *how fast* axis (kinetics, barriers, catalysis) that leads into enzymes.

## Mental model
Two independent axes of a reaction:
- **Well depths** (ΔG between reactant and product) → *whether* and *how far* it goes.
- **Peak height** (activation energy Eₐ / ΔG‡) → *how fast* it goes.
Thermodynamics ≠ kinetics. A reaction can be wildly favourable and effectively frozen.

## Key concepts

### Reaction coupling
- Free energy is a **state function** — it adds. Link an uphill reaction (ΔG > 0) to a
  downhill one (ΔG < 0) sharing a common intermediate; what matters is the **sum**.
  e.g. (X→Y, +15) + (ATP→ADP+Pᵢ, −30) ⇒ coupled ΔG = −15 → now it goes.
- Coupling is **mechanical, not vibes**: the two reactions must share a chemical
  intermediate on the **same enzyme** (typically the enzyme transfers a phosphate from
  ATP onto the substrate — **phosphorylation** — making a higher-energy intermediate
  that then reacts downhill). Energy "released nearby" wouldn't work.

### ATP — the energy currency
- ATP = adenosine + triphosphate tail. Hydrolysing the terminal phosphate (→ ADP + Pᵢ)
  releases a lot of free energy, for reasons straight from M1:
  - **electrostatic strain** — ~4 crammed negative charges repel; splitting relieves it
    (energy down) and the pieces separate (entropy up);
  - **resonance & solvation** — released Pᵢ spreads its charge by resonance (the
    carboxylate trick) and the more-charged products are well solvated by water.
- Not a mystical "high-energy bond" — just the usual bookkeeping (charge, resonance,
  entropy, solvation).
- **Kept far from equilibrium:** cells maintain a high **ATP/ADP ratio** (products ADP,
  Pᵢ kept scarce), so via ΔG = ΔG° + RT ln Q the *actual* ΔG (~−50 kJ/mol) is even more
  negative than ΔG°. A battery held charged.

### Why scarce products keep a reaction going (mechanism)
- Reactions run both ways: net rate = k_f[reactants] − k_r[products].
- Plentiful products don't slow the forward reaction — they **speed the reverse** one,
  shrinking net progress. Equilibrium = forward rate = reverse rate (net zero).
- Same thing thermodynamically: products raise Q, so ΔG → 0. Keep products scarce →
  reverse starved → net reaction barrels forward. (This is why low ADP/Pᵢ matters.)
- Biological extra: deliberate **product inhibition** (a product binds and switches off
  an enzyme) is a separate regulatory mechanism — see M9.

### Kinetics — how fast
- To react, a molecule must climb to a **transition state**: a strained peak with bonds
  half-broken/half-formed. Height above reactants = **activation energy Eₐ**. Even a
  downhill reaction pays this toll first.
- **Rate ∝ e^(−Eₐ/RT)** (Arrhenius) — the Boltzmann factor again, now at the peak. Only
  the fraction of molecules with enough thermal energy crosses. ⇒ a *small* change in
  Eₐ → a *huge* change in rate (it's in the exponent).
- For a downhill reaction the **reverse barrier is taller** (products in a deeper well
  must climb more to return).

### Catalysis & enzymes
- A **catalyst** offers an alternate route over a **lower** peak. It speeds **both**
  directions equally and **leaves ΔG / the well depths untouched** ⇒ **does not change
  the equilibrium position or K** — only how fast you reach it. Not consumed.
- **Enzymes** = biological catalysts (proteins, sometimes RNA) lowering Eₐ with huge
  power (10⁶–10¹⁷×) and exquisite **specificity**. Core mechanism: the folded active
  site binds and **stabilises the transition state** more than the reactant — i.e.
  lowers the peak. (This is why M1's folding/charge/H-bond machinery matters: it builds
  that site.) Full treatment in M8.

## The maths
- Coupled ΔG = Σ ΔGᵢ.
- ΔG = ΔG° + RT ln Q, Q = [products]/[reactants].
- rate ∝ e^(−Eₐ/RT); rate ratio for a barrier change ΔEₐ is e^(ΔEₐ/RT). Worked in
  `problems/m2-activation-barrier.md`.

## Climate / ML anchor
- **Carbon fixation** (Calvin cycle, M13) is uphill — paid for by **ATP + NADPH** from
  the light reactions (sunlight → currencies → coupled into fixation). The energy budget
  is part of why better fixation is hard.
- **RuBisCO**: kinetically slow (~a few/s) *and* unspecific (also fixes O₂ →
  photorespiration) — a barrier + specificity problem, prime ML-design target.
- **Carbonic anhydrase**: opposite extreme, near diffusion-limited. The gap between the
  two is the enzyme-engineering playground.
- ML hook: predicting ΔΔG (stability/affinity) is the free-energy axis; predicting
  catalytic rate / designing lower-barrier active sites is the kinetic axis.

## Common misconceptions / things that tripped me up
- "ATP/ADP" help is about a **high ATP/ADP ratio (scarce products)**, not abundant ADP.
- A large negative ΔG means *favourable*, not *fast* — speed is set by Eₐ only.
- A catalyst changes **how fast**, never **how far** (K unchanged).
- Plentiful products slow net progress by driving the **reverse** reaction, not by
  blocking the forward one.

## See also
- `notes/m2-free-energy.md`; `notes/m1-chemical-foundations.md`.
- `flashcards/decks/m2-coupling-and-kinetics.md`; `problems/m2-activation-barrier.md`.
- Next: M3 (amino acids) or M8 (enzymes) — kinetics sets up both.
