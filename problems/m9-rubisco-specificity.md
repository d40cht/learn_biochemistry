# Problem: Where does RuBisCO's ~25% photorespiration loss come from? (M9)

**Concept exercised:** k_cat/K_M as a specificity constant; competing-substrate
partitioning; why carbon-concentrating mechanisms help.

## Statement
A typical plant RuBisCO has a CO₂/O₂ specificity factor S_c/o ≈ 90. In the chloroplast
stroma at 25 °C, dissolved gases are roughly [CO₂] ≈ 10 µM and [O₂] ≈ 250 µM.
(a) What is the ratio of carboxylation to oxygenation events?
(b) What fraction of RuBisCO reactions are wasteful oxygenations?
(c) A C4 plant concentrates CO₂ ~10× around RuBisCO. What happens to the oxygenation
fraction?

## Approach
Competing substrates partition in proportion to their k_cat/K_M, so
v_carb/v_oxy = S_c/o × [CO₂]/[O₂]. Fraction oxygenation = v_oxy/(v_carb+v_oxy) =
1/(1 + v_carb/v_oxy).

## Solution
(a) v_carb/v_oxy = 90 × (10/250) = 90 × 0.04 = **3.6** carboxylations per oxygenation.

(b) fraction oxygenation = 1/(1 + 3.6) = 1/4.6 ≈ **0.22 → ~22%** of events are
oxygenations. (Each consumes resources and the salvage pathway releases some fixed CO₂ —
hence the oft-quoted "~25% loss". Close.)

(c) C4 raises [CO₂] ~10× → [CO₂]/[O₂] ≈ 0.4 → v_carb/v_oxy = 90 × 0.4 = 36 →
fraction oxygenation = 1/37 ≈ **2.7%**. Photorespiration nearly abolished.

## Sanity check
The ~22% from plausible textbook numbers lands right on the ~25% figure quoted in M8 —
independent routes agreeing. And concentrating CO₂ collapses the loss, which is exactly
why C4/CAM plants thrive in hot, dry, high-photorespiration conditions.

## Takeaway
Two levers reduce the loss: raise the **enzyme's** S_c/o (hard — trades off against k_cat),
or raise the **local [CO₂]/[O₂]** (what C4/CAM plants do biochemically, and what one might
engineer into C3 crops). Both are concrete, quantifiable objectives — and the S_c/o-vs-k_cat
trade-off is precisely the constrained landscape ML-guided enzyme design exists to explore.
