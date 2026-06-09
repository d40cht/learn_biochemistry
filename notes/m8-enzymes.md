# Enzyme mechanism & catalysis (M8)

> How enzymes lower the activation barrier — and the kinetics/thermodynamics split that
> governs what they can and can't do. Builds on M2 (barriers, ΔG), M4 (active site = the
> 3D fold), M3 (side-chain chemistry). Two case studies bookend the carbon cycle.

## Mental model
An enzyme is **a glove molded to the transition state** — in both shape and charge —
not a comfy chair for the substrate. It lowers the peak (kinetics); it never changes the
equilibrium (thermodynamics). Direction is set by free-energy gradients, never by the
catalyst.

## Key concepts

### The central principle: stabilise the transition state, not the substrate
- An enzyme speeds a reaction by **lowering Eₐ** (the TS peak) without changing well
  depths → equilibrium unchanged, only rate (M2).
- **It must bind the TS *more tightly* than the substrate.** Binding the substrate
  tightly just *deepens the reactant well* → taller climb → **anti-catalysis**. Binding
  S and TS equally → no help. Only differential (TS-favouring) binding catalyses.
- Pauling (1948): the active site is **complementary to the transition state**.
- Evidence: **transition-state analogs** (stable molecules shaped/charged like the TS)
  bind orders of magnitude tighter than substrate → potent inhibitors (a real drug class).

### Where the power comes from
- **Binding energy** (many weak interactions — H-bonds, vdW, electrostatic, hydrophobic;
  all M1) is the budget. Spent two ways:
  - **Differential binding** (TS over S);
  - **Proximity & orientation** — pre-align substrates, paying down the **entropy** cost
    of bringing them together (slices the entropic part of the barrier; huge effective
    local concentration).

### The active site & specificity
- A pocket built by the **3D fold** — residues far apart in *sequence*, close in *space*
  (M4 tertiary structure) — lined with chosen side chains.
- **Induced fit** (not rigid lock-and-key): binding deforms enzyme (and strains
  substrate) toward the TS geometry; grip tightens as S → TS.

### Geometry vs electrostatics (two faces of TS-complementarity)
- **Geometric:** the site is shaped to the TS, so it orients reacting atoms precisely
  (near-attack geometry) and can **strain/distort the substrate toward the TS shape**
  ("ground-state destabilisation"; classic example: lysozyme flattening its sugar ring).
- **Electronic (usually dominant):** the TS has a different **charge distribution** than
  the substrate (bonds half-made/broken). The site's charges/dipoles are
  **pre-organised** in 3D exactly where the TS's developing charges appear — costing no
  reorganisation energy (unlike water, which must reorient around each new charge).
- So geometry positions the groups; electrostatics mostly pays the bill.

### Catalytic strategies (usually several at once)
1. **Proximity & orientation** (entropy pre-payment).
2. **Acid–base** — donate/accept protons at the key step. **Histidine** is the star
   (pKₐ ≈ 6 → acid *or* base at physiological pH). Also Asp, Glu, Lys, Cys, Tyr, Ser.
3. **Covalent** — transient covalent enzyme–substrate bond (e.g. serine proteases'
   Ser nucleophile → acyl-enzyme intermediate).
4. **Metal-ion** — Zn²⁺, Mg²⁺, Fe… stabilise charge, orient, do redox, or lower a bound
   water's pKₐ to make a hydroxide nucleophile.
5. **Electrostatic preorganisation** — positioned charges (e.g. an "oxyanion hole")
   stabilise the TS; water excluded so electrostatics bite harder.

### Cofactors & coenzymes
- The 20 side chains are chemically limited (good at acid/base & H-bonding; can't carry
  electrons or do most redox). Enzymes recruit helpers:
  - **metal ions** (inorganic cofactors);
  - **coenzymes** (organic, often **vitamin-derived**): NAD⁺/NADP⁺ (B3, electrons/hydride),
    FAD (B2), coenzyme A (acyl transfer), TPP (B1), PLP (B6), **biotin** (CO₂ carrier).
- Terms: apoenzyme (protein only) + cofactor = holoenzyme; tightly/covalently bound
  cofactor = prosthetic group. (NADPH from M2 is a coenzyme — carrier of reducing power.)

### Product release & the catalytic cycle
- The glove fits the **TS**, not the product → product binds **weakly** → high off-rate →
  diffuses out (helped by induced-fit reopening and low product concentration / mass
  action). Enzyme returns unchanged: E + S ⇌ ES → ES‡ → EP ⇌ E + P. Turnovers/s = **k_cat**.
- **Design tension:** bind TS tight (catalysis) yet product loose (release). Over-tight
  product binding → **product inhibition**. For the best enzymes, release/diffusion
  becomes rate-limiting → **diffusion-limited**.

### Catalysts can't change equilibrium (no free ratchet)
- Forward and reverse share the **same TS** → lowering the peak speeds **both** equally.
- A catalyst that shifted equilibrium would be a perpetual-motion machine (2nd law) →
  forbidden. Any binding asymmetry the enzyme has **must cancel** for free S vs free P
  (the thermodynamic cycle closes: tight binding somewhere ↔ reluctant binding/release
  elsewhere). Encoded in the **Haldane relationship**:
  (k_cat/K_M)_fwd ÷ (k_cat/K_M)_rev = K_eq.
- The enzyme sets **how fast** and **which intermediates accumulate (occupancy)** — never
  the resting point of free S vs P.
- **Direction** comes from thermodynamics: P below S (ΔG° < 0) sets K_eq = e^(−ΔG°/RT) and
  makes the forward barrier shorter than the reverse by ΔG°. A *large* −ΔG° (often
  ATP-coupled) makes a step **effectively irreversible** — that's the real "ratchet",
  paid for with free energy, not by the catalyst.
- If **ΔG° = 0** → K_eq = 1 → enzyme catalyses both directions equally; net direction set
  purely by concentrations. (Cells use near-equilibrium enzymes as reversible workhorses
  and big-−ΔG/ATP-coupled steps as one-way control valves — M11.)

## Case studies (bookending the carbon cycle)
### Carbonic anhydrase — near-perfect
- CO₂ + H₂O ⇌ HCO₃⁻ + H⁺; ~10⁷× rate enhancement, k_cat ≈ 10⁶/s, **diffusion-limited**.
- **Zn²⁺** (held by 3 His) lowers a bound water's pKₐ (~15.7 → ~7) → **Zn–OH⁻ nucleophile**
  at neutral pH (no side chain could) → attacks CO₂ → bicarbonate; a **His proton shuttle**
  carries off the H⁺ (rate-limiting). Metal + acid–base + electrostatic catalysis at once.
- Climate: the CO₂-hydration reaction central to carbon capture; engineered heat-stable
  carbonic anhydrases are a real target.

### RuBisCO — near-pessimal but all-important
- Fixes CO₂ onto ribulose-1,5-bisphosphate → 2× 3-phosphoglycerate; first committed step
  of the Calvin cycle (M13). Most abundant protein on Earth; ~all biospheric carbon fixed
  by it. Needs **Mg²⁺** (and activating carbamylation of a Lys).
- **Slow**: k_cat ≈ 3/s → plants compensate with quantity (~50% of leaf soluble protein).
- **Sloppy**: competing **oxygenase** reaction (grabs O₂) → photorespiration → wastes
  ~25% of fixed carbon in C3 plants.
- Stuck: evolved when O₂ was scarce; **speed–specificity trade-off** (better CO₂
  discrimination ⇒ even slower) — the binding/release trade-off realised on a global
  enzyme. Workaround: **C4/CAM carbon-concentrating mechanisms** (M13).
- **Prize ML target**: tiny improvements scale globally (yield + CO₂ drawdown); hard
  because of the trade-off, chaperone-dependent assembly, and vast sequence space.

## Climate / ML anchor
- CA and RuBisCO are the two ends of the enzyme-quality spectrum, both on the carbon
  cycle. RuBisCO is arguably the single highest-leverage enzyme-engineering target for
  climate; ML on sequence→function landscapes, structure prediction, and model-guided
  evolution are the tools (M17–M22).

## Common misconceptions / things that tripped me up
- A "well that grips the substrate" is **anti-catalytic**; the glove must fit the **TS**.
- Catalysis isn't mainly about increasing alignment frequency — it's about **lowering the
  peak** (TS stabilisation). Alignment is a bonus strategy.
- An enzyme is **not** a ratchet; it can't change equilibrium. Direction = thermodynamics.
- Binding asymmetries (S vs P) are real but **cancel** for free S/P (detailed balance);
  the intrinsic ΔG°(S→P) is the one asymmetry the enzyme never touches.

## See also
- `notes/m2-coupling-and-kinetics.md`, `notes/m4-protein-structure.md`,
  `notes/m1-chemical-foundations.md`.
- `flashcards/decks/m8-enzymes.md`; `problems/m8-rubisco-abundance.md`.
- Next: M9 (enzyme kinetics — Michaelis–Menten, k_cat, K_M, the diffusion limit) then
  M13 (photosynthesis & carbon fixation — where RuBisCO lives).
