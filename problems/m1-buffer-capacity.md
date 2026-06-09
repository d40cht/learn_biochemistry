# Problem: How well does a buffer hold pH? (M1)

**Concept exercised:** Henderson–Hasselbalch, why big reservoirs ⇒ small pH moves.

## Statement
A buffer contains 0.10 M weak acid HA and 0.10 M conjugate base A⁻ (pKₐ = 4.76,
acetic acid). You add 0.01 mol/L of strong acid (H⁺). What is the pH before and after?
For contrast, what would 0.01 mol/L of strong acid do to pure water at pH 7?

## Approach
A strong acid fully dissociates, so it dumps 0.01 M of H⁺ into solution. In the buffer
that H⁺ is consumed by A⁻ (A⁻ + H⁺ → HA), shifting the reservoir ratio. pH follows
pH = pKₐ + log([A⁻]/[HA]). In pure water there's no reservoir to absorb it.

## Solution
**Before:** [A⁻]/[HA] = 0.10/0.10 = 1 → log 1 = 0 → pH = pKₐ = **4.76**.

**After (buffer):** the added 0.01 M H⁺ converts 0.01 M of A⁻ into HA:
- HA: 0.10 + 0.01 = 0.11 M
- A⁻: 0.10 − 0.01 = 0.09 M

pH = 4.76 + log(0.09/0.11) = 4.76 + log(0.818) = 4.76 − 0.087 = **4.67**.
→ pH dropped only **0.09**.

**After (pure water):** [H⁺] = 0.01 M → pH = −log(0.01) = **2** → a drop of **5 units**.

## Sanity check
Adding acid lowered the pH in both cases (correct sign). The buffer moved ~0.1 unit
vs 5 units for water — the reservoir did its job. Both HA and A⁻ are still plentiful,
so capacity remains.

## Takeaway
pH tracks the **log of the ratio** [A⁻]/[HA]. When both reservoirs are large, a dose of
acid barely shifts the ratio, so pH barely moves. Buffering capacity = the size of the
reservoirs, not the tiny pool of free H⁺ — and it runs out only when a reservoir is
drained.
