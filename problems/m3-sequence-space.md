# Problem: How big is protein sequence space? (M3)

**Concept exercised:** combinatorics of the 20-letter alphabet; why protein design is a
search problem (and why ML, not brute force).

## Statement
Using 20 standard amino acids, how many distinct sequences are possible for a small
protein of length 100? How does that compare to the number of atoms in the observable
universe (~10⁸⁰)? Roughly how many such proteins has evolution actually sampled?

## Approach
Each of the 100 positions is an independent choice of 1 of 20 residues, so the count is
20¹⁰⁰. Convert to base 10 via 20¹⁰⁰ = 10^(100·log₁₀20), and log₁₀20 ≈ 1.301.

## Solution
Number of sequences = 20¹⁰⁰ = 10^(100 × 1.301) = **10¹³⁰**.

Compared to ~10⁸⁰ atoms in the observable universe, sequence space is larger by a factor
of ~10⁵⁰ — there are vastly more length-100 sequences than atoms in the universe.

Evolution's sample: very rough upper bound — say 10³⁰ organisms over Earth's history ×
10⁴ proteins each × 10⁹ years of mutation ≈ **~10⁴³** sequences ever tried (generous).
That's an unimaginably tiny fraction (~10⁻⁸⁷) of the space.

## Sanity check
Even a *tiny* protein blows past any conceivable physical enumeration. The numbers are
"astronomical" in the literal, under-stated sense.

## Takeaway
You **cannot** brute-force protein design — the space is hyper-astronomically large and
almost entirely non-functional. This is *why* the field is ML-shaped: learn the manifold
of foldable/functional sequences (protein language models, generative design) and search
intelligently, rather than enumerate. The same reason board-game and molecule search
moved to learned models. Directly relevant to engineering enzymes for climate.
