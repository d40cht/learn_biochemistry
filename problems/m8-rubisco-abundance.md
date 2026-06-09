# Problem: Why is RuBisCO the most abundant protein on Earth? (M8)

**Concept exercised:** k_cat (turnover number) ties enzyme *quantity* to required flux;
the cost of a slow catalyst.

## Statement
RuBisCO turns over CO₂ at k_cat ≈ 3 per second. Carbonic anhydrase manages ≈ 10⁶ per
second. (a) For a fixed required CO₂-processing rate, how many more RuBisCO molecules are
needed than if it ran at carbonic-anhydrase speed? (b) Qualitatively, what does that imply
for how much RuBisCO a photosynthesising leaf must contain?

## Approach
Throughput = (number of enzyme molecules) × (turnover per molecule). For a fixed
throughput, the number of molecules needed is inversely proportional to k_cat. So the
ratio of molecules needed is just the inverse ratio of turnover numbers.

## Solution
(a) molecules needed ∝ 1/k_cat, so
ratio = k_cat(CA) / k_cat(RuBisCO) = 10⁶ / 3 ≈ **3 × 10⁵**.

A leaf would need roughly **300,000× more** RuBisCO molecules to fix carbon at a given
rate than it would need of a carbonic-anhydrase-speed enzyme doing the same job.

(b) Since the demand (fix enough carbon to grow) is large and k_cat is tiny, the only way
to hit the required flux is **mass**: plants pour resources into making enormous amounts
of RuBisCO — up to ~50% of the soluble protein in a leaf — which is exactly why it is the
**most abundant protein on Earth.**

## Sanity check
Abundance as a workaround for slowness makes sense: throughput = count × rate, so if rate
is ~10⁵–10⁶× too low, count must rise correspondingly. The observed "half the leaf's
protein" is the visible consequence.

## Takeaway
A slow enzyme isn't just a kinetic curiosity — it's a massive **resource tax**. Nitrogen
and energy sunk into making mountains of a poor catalyst can't be used elsewhere. This is
why even a modest improvement in RuBisCO's k_cat (or its CO₂/O₂ specificity, to cut the
~25% photorespiration loss) would be globally significant for crop yield and carbon
drawdown — and why it's such a high-value ML enzyme-engineering target.
