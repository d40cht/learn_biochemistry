# Deck: M9 — Enzyme kinetics
tags: m9 enzymes kinetics

Q: State the Michaelis–Menten equation and define its terms.
A: v = V_max[S]/(K_M+[S]). V_max = k_cat·[E]_tot (max rate); k_cat = turnover number; K_M = (k₋₁+k_cat)/k₁ = the [S] giving half-maximal rate.

---

Q: What steady-state assumption drives the Michaelis–Menten derivation?
A: d[ES]/dt ≈ 0 — ES is formed (k₁[E][S]) and broken down ((k₋₁+k_cat)[ES]) at equal rates. Combine with [E]=[E]_tot−[ES].

---

Q: What is K_M, operationally?
A: The substrate concentration at which v = V_max/2. It's intrinsic to the enzyme–substrate pair (independent of enzyme amount).

---

Q: Double the amount of enzyme — what happens to V_max and K_M?
A: V_max doubles (= k_cat·[E]_tot). K_M is unchanged (a property of the enzyme–substrate pair, not the dose).

---

Q: Describe the rate in the low-[S] and high-[S] regimes.
A: Low [S] (≪K_M): v ≈ (k_cat/K_M)[E][S], first-order (capture-limited). High [S] (≫K_M): v ≈ V_max, zero-order (enzyme saturated, finite active sites all occupied).

---

Q: What is k_cat/K_M and why is it the key metric?
A: The effective 2nd-order rate constant at low [S] (the usual cellular regime). It folds in both chemistry (k_cat) and substrate capture (1/K_M), so it's the best single measure of catalytic efficiency.

---

Q: What is the diffusion limit, and which enzyme reaches it?
A: ~10⁸–10⁹ M⁻¹s⁻¹ — the rate of physical E–S encounter; k_cat/K_M can't exceed it. Enzymes at this ceiling are "catalytically perfect" (every encounter reacts). Carbonic anhydrase (~10⁸) is here.

---

Q: How does k_cat/K_M govern competition between two substrates? (RuBisCO example)
A: They partition in proportion to their k_cat/K_M values. RuBisCO: v_carb/v_oxy = S_c/o × [CO₂]/[O₂], with S_c/o = (k_cat/K_M)_CO₂ ÷ (k_cat/K_M)_O₂ ≈ 80–100.

---

Q: Is K_M the same as binding affinity (K_d)?
A: Only in the rapid-equilibrium limit (k_cat ≪ k₋₁). In general K_M = (k₋₁+k_cat)/k₁ ≥ K_d, so K_M is *apparent* affinity — a fair proxy, not exact.

---

Q: Competitive vs noncompetitive inhibition — effects on K_M and V_max?
A: Competitive (binds active site): apparent K_M ↑, V_max unchanged. Noncompetitive (binds elsewhere): V_max ↓, K_M ~unchanged. (TS analogs are competitive inhibitors.)

---

Q: What is cooperativity and what curve does it give?
A: Substrate binding to one subunit raises the others' affinity → a sigmoidal (S-shaped) v-vs-[S] curve instead of a hyperbola → switch-like sensitivity near a threshold. Hemoglobin O₂ binding is the classic example.

---

Q: What is feedback inhibition?
A: A pathway's end-product inhibits an early (often allosteric) enzyme in that pathway — a metabolic thermostat that throttles flux when product is plentiful.
