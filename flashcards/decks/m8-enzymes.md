# Deck: M8 — Enzyme mechanism & catalysis
tags: m8 enzymes catalysis

Q: What is the central principle of how an enzyme lowers the activation barrier?
A: It binds and stabilises the TRANSITION STATE more tightly than the substrate (Pauling). Lowering the peak speeds the reaction; well depths (equilibrium) are untouched.

---

Q: What goes wrong if an enzyme binds the substrate very tightly?
A: It deepens the reactant well, so the climb to the transition state gets TALLER — anti-catalysis. Only TS-favouring (differential) binding helps.

---

Q: Why do transition-state analogs bind enzymes so tightly, and what use is that?
A: Because the active site is complementary to the TS, a stable TS-shaped molecule out-binds the substrate by orders of magnitude → a potent inhibitor (a real drug-design strategy) and direct evidence for the TS-stabilisation principle.

---

Q: Besides differential TS binding, how does binding energy accelerate a reaction?
A: Proximity & orientation: the enzyme pre-aligns substrates, paying down the entropy cost of bringing them together in the right geometry (cuts the entropic part of the barrier).

---

Q: Lock-and-key vs induced fit — which is the modern view and why does it matter?
A: Induced fit: binding deforms the enzyme (and strains the substrate) toward the TS geometry; the grip tightens as S→TS. Avoids the "tight substrate well" trap and explains specificity.

---

Q: Geometry vs electrostatics in transition-state complementarity — which dominates?
A: Both matter. Geometry orients/strains the substrate toward the TS shape (ground-state destabilisation). But electrostatic PREORGANISATION — fixed charges positioned for the TS's charge distribution — usually dominates (no reorganisation cost, unlike water).

---

Q: Name the five catalytic strategies.
A: Proximity/orientation; acid–base (His!); covalent; metal-ion; electrostatic preorganisation (e.g. oxyanion hole). Often several at once.

---

Q: Why do enzymes need cofactors/coenzymes?
A: The 20 side chains can't carry electrons or do most redox. Metal ions and (often vitamin-derived) coenzymes — NAD(P)⁺, FAD, CoA, biotin (CO₂ carrier) — extend the chemical toolkit.

---

Q: After the reaction, why does the product leave the active site?
A: The site fits the TS, not the product, so the product binds weakly → high off-rate → diffuses out (helped by induced-fit reopening and low product concentration). Enzyme returns unchanged for the next turnover (k_cat).

---

Q: Can an enzyme change the equilibrium of a reaction? Why/why not?
A: No. Forward and reverse share the same TS, so both speed up equally; a catalyst that shifted equilibrium would violate the 2nd law. Binding asymmetries cancel for free S vs P (Haldane: (kcat/KM)_fwd ÷ (kcat/KM)_rev = K_eq).

---

Q: If ΔG° = 0 between two states, what does an enzyme do?
A: K_eq = 1, so it catalyses both directions equally; net direction is set purely by concentrations (mass action). Such near-equilibrium enzymes are reversible metabolic workhorses.

---

Q: What makes a metabolic step effectively irreversible (a one-way valve)?
A: A large negative ΔG° (often via coupling to ATP hydrolysis), not the enzyme. Thermodynamics sets direction; the catalyst only sets speed.

---

Q: How does carbonic anhydrase's Zn²⁺ work, and why is the enzyme so fast?
A: Zn²⁺ lowers a bound water's pKₐ (~15.7→~7) to make a Zn–OH⁻ nucleophile at neutral pH; it attacks CO₂ → bicarbonate, and a His shuttles the proton away. So fast it's diffusion-limited (k_cat ≈ 10⁶/s).

---

Q: What reaction does RuBisCO catalyse and why does it matter?
A: It fixes CO₂ onto ribulose-1,5-bisphosphate → two 3-phosphoglycerate; the first committed step of the Calvin cycle. ~All biospheric carbon is fixed by it; it's the most abundant protein on Earth.

---

Q: In what two ways is RuBisCO a "bad" enzyme, and why is it stuck that way?
A: Slow (k_cat ≈ 3/s, so plants make huge amounts) and sloppy (also fixes O₂ → photorespiration, wasting ~25% of fixed carbon). Stuck due to a speed–specificity trade-off and its ancient, central, chaperone-dependent design.

---

Q: Why is RuBisCO a prime target for ML enzyme design?
A: It performs ~all carbon fixation, so tiny improvements scale globally (crop yield + CO₂ drawdown). Hard due to the speed–specificity trade-off, complex assembly, and vast sequence space — exactly an ML-on-biochemistry problem.
