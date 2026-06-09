# Enzyme kinetics (M9)

> The quantitative layer on M8: derive the rate law, define k_cat / K_M / V_max, find the
> figure of merit (k_cat/K_M) and its diffusion ceiling, and see how it sets RuBisCO's
> CO₂/O₂ selectivity. Inhibition & allostery as the control knobs.

## Mental model
v = V_max[S]/(K_M+[S]) is a saturating hyperbola: linear in [S] when substrate is scarce,
flat when the enzyme is saturated. **k_cat/K_M** (catalytic efficiency) is the number that
compares enzymes; its hard ceiling is diffusion.

## Key concepts

### Michaelis–Menten (steady-state derivation)
Model: E + S ⇌(k₁,k₋₁) ES →(k_cat) E + P, with [P]≈0 early so the last step is one-way.
Assume steady state d[ES]/dt ≈ 0:
- formation k₁[E][S] = breakdown (k₋₁+k_cat)[ES];
- conservation [E] = [E]_tot − [ES];
- solve → [ES] = [E]_tot[S]/(K_M+[S]), with **K_M ≡ (k₋₁+k_cat)/k₁**;
- v = k_cat[ES] ⇒ **v = V_max[S]/(K_M+[S])**, with **V_max ≡ k_cat[E]_tot**.

### The three parameters
- **V_max = k_cat·[E]_tot** — max rate (all enzyme saturated); scales with enzyme amount.
- **k_cat** — turnover number, reactions/enzyme/s (RuBisCO ≈ 3; carbonic anhydrase ≈ 10⁶).
- **K_M** — concentration units; **[S] giving half-maximal rate** (set [S]=K_M → v=V_max/2).
  Intrinsic to the enzyme–substrate pair (independent of [E]_tot).

### Two regimes
- **[S] ≪ K_M:** v ≈ (k_cat/K_M)[E][S] — first-order, capture-limited.
- **[S] ≫ K_M:** v ≈ V_max — zero-order, saturated (finite active sites all occupied).
  Saturation is the kinetic signature of a catalyst (vs an uncatalysed reaction).

### k_cat/K_M — catalytic efficiency / specificity constant
- The effective 2nd-order rate constant at low [S] (the usual cellular regime). Folds in
  both chemistry (k_cat) and capture (1/K_M); the right figure of merit.
- **Diffusion ceiling ≈ 10⁸–10⁹ M⁻¹s⁻¹** — the rate of physical E–S encounter. Enzymes at
  this limit are "catalytically perfect" (every encounter reacts). Carbonic anhydrase
  (~10⁸) is here — this *is* "diffusion-limited" (M8), quantified.
- **Competing substrates** partition in proportion to their k_cat/K_M. For RuBisCO:
  v_carb/v_oxy = S_c/o × [CO₂]/[O₂], where S_c/o = (k_cat/K_M)_CO₂ / (k_cat/K_M)_O₂ ≈ 80–100.
  Sets photorespiration loss (see problem). Speed–specificity trade-off: ↑S_c/o ⇒ ↓k_cat.

### K_M ≠ exactly affinity
K_M = (k₋₁+k_cat)/k₁ equals K_d = k₋₁/k₁ only when k_cat ≪ k₋₁ (rapid equilibrium).
Otherwise K_M > K_d. So K_M is *apparent* affinity — usually a fair proxy, not exact.

### Inhibition (basis of most drugs)
- **Competitive** — binds the active site; ↑ apparent K_M, V_max unchanged. (TS analogs
  are competitive inhibitors.)
- **Noncompetitive** — binds elsewhere; ↓ V_max, K_M ~unchanged.
- **Uncompetitive** — binds only ES; ↓ both V_max and K_M.
- **Feedback / product inhibition** — pathway end-product inhibits an early enzyme (a
  metabolic thermostat; the M2 product-inhibition idea).

### Allostery & cooperativity
- Regulators bind away from the active site and switch the enzyme between active/inactive
  conformations (usually multi-subunit — M4 quaternary). Cooperative substrate binding →
  **sigmoidal** v-vs-[S] (switch-like sensitivity near a threshold). Hemoglobin O₂ binding
  is the classic. Metabolic one-way control-valve steps are typically allosteric +
  feedback-regulated.

## The maths
- v = V_max[S]/(K_M+[S]); V_max = k_cat[E]_tot; K_M = (k₋₁+k_cat)/k₁.
- Low [S]: v ≈ (k_cat/K_M)[E][S]. High [S]: v ≈ V_max.
- Lineweaver–Burk: 1/v = (K_M/V_max)(1/[S]) + 1/V_max (a straight line in 1/[S]; classic
  way to read off K_M, V_max — though nonlinear fitting is preferred now).
- RuBisCO partitioning: v_carb/v_oxy = S_c/o·[CO₂]/[O₂]. Worked in `problems/`.

## Climate / ML anchor
- k_cat/K_M and S_c/o are the *measurable* objectives for engineering carbon-fixation
  enzymes; the (k_cat, S_c/o) trade-off is a constrained multi-objective landscape — ML's
  home turf. Carbon-concentrating mechanisms (C4/CAM, M13) raise local [CO₂]/[O₂] to win
  the partitioning without changing the enzyme.

## Common misconceptions / things that tripped me up
- Doubling enzyme doubles V_max but leaves K_M (and k_cat) unchanged.
- The right efficiency metric is **k_cat/K_M**, not k_cat or K_M alone.
- K_M is *apparent* affinity, equal to K_d only in the rapid-equilibrium limit.
- Saturation happens because active sites are finite — not because substrate "runs out".

## See also
- `notes/m8-enzymes.md`, `notes/m2-coupling-and-kinetics.md`.
- `flashcards/decks/m9-enzyme-kinetics.md`; `problems/m9-rubisco-specificity.md`.
- Next: M13 (photosynthesis & carbon fixation — RuBisCO in its native pathway), or the
  metabolism run-up M10–M12.
