# Problem: How much does lowering the barrier speed things up? (M2)

**Concept exercised:** Arrhenius / Boltzmann sensitivity of rate to activation energy.

## Statement
An enzyme lowers a reaction's activation energy by ΔEₐ = 30 kJ/mol at body temperature
(T = 310 K). By what factor does the rate increase? What would it take to get a
millionfold (10⁶) speed-up?

## Approach
Rate ∝ e^(−Eₐ/RT), so the ratio of catalysed to uncatalysed rate is e^(ΔEₐ/RT). Need
RT in kJ/mol: R = 8.314 J/(mol·K), T = 310 K → RT = 2.577 kJ/mol.

## Solution
**30 kJ/mol drop:**
exponent = ΔEₐ/RT = 30 / 2.577 = 11.64
rate ratio = e^(11.64) ≈ **1.1 × 10⁵** → ~100,000× faster.

**For 10⁶:**
need e^(ΔEₐ/RT) = 10⁶ → ΔEₐ/RT = ln(10⁶) = 13.8 → ΔEₐ = 13.8 × 2.577 ≈ **35.6 kJ/mol**.

## Sanity check
A barrier reduction of ~36 kJ/mol — less than the energy of a single ATP hydrolysis —
buys a millionfold rate increase. Magnitudes feel right: real enzymes lowering barriers
by 2–3× this give the famous 10⁶–10¹⁷ enhancements.

## Takeaway
Because Eₐ sits in the **exponent**, rate is hypersensitive to the barrier: modest,
chemically-plausible reductions yield astronomical speed-ups. This is why evolution (and
enzyme engineering / ML design) targets transition-state stabilisation — a few tens of
kJ/mol of barrier is the whole game. And note: none of this moves the equilibrium.
