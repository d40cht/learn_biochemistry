# Free energy & why reactions reach equilibrium (M2, head start)

> Opened early to answer: "if HA is lower energy, why doesn't it all neutralise —
> why is there an equilibrium with both species present?" The answer is the master
> key to metabolism, binding, and folding.

## Mental model
Systems at constant T and P do **not** minimise energy. They minimise **free energy**:
$$G = H - TS$$
A tug of war: **H** (enthalpy ≈ bond energy) wants order/bonds; **S** (entropy ≈ number
of accessible arrangements) wants freedom/spread; **T** sets the exchange rate. The
minimum of G generally sits at a **mixture**, not at either pure extreme.

## Key concepts
- Forming HA lowers H (favourable). Splitting HA → H⁺ + A⁻ raises S (one particle → two,
  free to roam → many more microstates). Neither wins outright; the balance point is
  equilibrium.
- **Boltzmann picture (the intuition to keep):** at temperature T, the lower-energy
  state is favoured but **not exclusive**. A ball in a valley jiggles and is found at
  height *h* with probability ∝ e^(−mgh/kT); the atmosphere doesn't pile on the floor.
  An "uphill" chemical state (H⁺ + A⁻) is likewise always populated at a small but
  **nonzero** fraction.
- **Equilibrium constant:** $K = e^{-\Delta G^\circ / RT}$. A weak acid has ΔG° > 0 for
  dissociation → K small (HA favoured, matching intuition) → **but never zero**.
  "Unidirectional" would need an infinite energy gap or T = 0.
- **Law of mass action:** $K_a = \frac{[H^+][A^-]}{[HA]}$ = a fixed nonzero constant, so
  neither [HA] nor [A⁻] can be driven to exactly zero — there's always some of each.
- Equilibrium is **dynamic**: HA breaks and reforms constantly; forward and reverse
  rates are equal. Nothing stopped, nothing got used up.

## The maths
- G = H − TS (minimised at constant T, P).
- K = exp(−ΔG°/RT); R = gas constant (Boltzmann's constant per mole).
- Ka = [H⁺][A⁻]/[HA].
- ΔG° > 0 ⇒ K < 1 (reactants favoured); ΔG° < 0 ⇒ K > 1 (products favoured); ΔG° = 0 ⇒
  K = 1.

## Climate / ML anchor
- Every "is this reaction favourable / how far does it go" question in metabolism is a
  ΔG / K question. Carbon-fixation steps are thermodynamically hard; cells **couple**
  them to ATP hydrolysis (very negative ΔG) to make the sum favourable — the central
  trick of bioenergetics, to be developed in M2 proper and M10.
- ML hook: binding affinity, folding stability (ΔΔG of mutations), reaction feasibility
  — all the same free-energy bookkeeping that ML models are increasingly asked to predict.

## Common misconceptions / things that tripped me up
- "Lowest energy wins" → wrong; **lowest free energy** wins, and entropy is in it.
- Equilibrium is a populated **mixture**, not exhaustion of one side.

## See also
- `notes/m1-chemical-foundations.md` (buffers — the question that started this).
- `flashcards/decks/m2-thermodynamics.md`.
- Still to do for full M2: reaction coupling & ATP, kinetics (rates, transition states,
  activation energy, catalysis as barrier-lowering).
