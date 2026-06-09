# Problem: Levinthal's paradox, quantified (M4)

**Concept exercised:** conformational combinatorics; why folding can't be random search.

## Statement
Model a 100-residue protein with ~3 stable (φ, ψ) states per residue. How many backbone
conformations are possible? If the chain could sample one every 10⁻¹³ s (a bond-vibration
timescale), how long to try them all? Compare to the age of the universe (~1.4 × 10¹⁰ yr).

## Approach
Conformations multiply: 3 choices at each of 100 residues → 3¹⁰⁰. Time = (number of
conformations) × (time per sample). Convert seconds → years (~3.15 × 10⁷ s/yr).

## Solution
Conformations = 3¹⁰⁰ = 10^(100·log₁₀3) = 10^(100 × 0.477) ≈ **10⁴⁷·⁷ ≈ 5 × 10⁴⁷**.

Time to sample all = 5 × 10⁴⁷ × 10⁻¹³ s = 5 × 10³⁴ s.
In years: 5 × 10³⁴ / 3.15 × 10⁷ ≈ **1.6 × 10²⁷ years**.

Age of the universe ≈ 1.4 × 10¹⁰ yr → random search would take ~**10¹⁷ times the age of
the universe**.

## Sanity check
Real proteins fold in ~10⁻⁶–10⁰ s. The gap between that and 10²⁷ years is the paradox —
about 40 orders of magnitude. A number that absurd means the premise (random search) must
be wrong.

## Takeaway
Folding is **not** a search through all conformations — the energy landscape is a
**funnel** that channels the unfolded chain downhill to the native state, so only a tiny,
guided fraction of conformation space is ever visited. ML analogy: it's the difference
between brute-forcing a loss surface and descending a well-conditioned one. And Anfinsen
says the funnel bottom (native fold) is fixed by the sequence — which is exactly why a
model can learn the sequence→structure map.
