# Application target: hydrogenotroph food (Solar Foods / Solein)

> A learner-chosen capstone target: making human food from hydrogen-oxidizing bacteria —
> "protein from air and electricity." Captured here as a motivating application; to be
> studied as a dedicated module after M13 (carbon fixation). This is an overview/primer,
> not yet a deeply worked module.

## What it is
Solar Foods (Finland) grows **hydrogen-oxidizing ("knallgas") bacteria** in a fermenter
fed **H₂ + CO₂ + O₂ + mineral nutrients**, producing a ~65–70%-protein powder (**Solein**).
The H₂ comes from **water electrolysis on renewable electricity** → "protein from air and
electricity." No farmland or sunlight. (NASA studied hydrogen bacteria for closed-loop
life support in the 1960s–70s.) Lab model organism: *Cupriavidus necator*.

## The biochemistry (maps onto modules already covered)
Chemolithoautotrophs — decoded via the M10 catabolism/anabolism map:
- **Energy + electrons (catabolism):** oxidize H₂ with O₂ — the knallgas reaction
  2H₂ + O₂ → 2H₂O (mixture is explosive — a safety constraint). Enzymes = **hydrogenases**,
  Ni-Fe **metalloenzymes** (M8). H₂ is a superb electron donor: E°′(2H⁺/H₂) ≈ −0.42 V
  (lower than NADH's −0.32 V), so it easily makes reducing power. Full drop to O₂ (+0.82 V):
  ΔE ≈ 1.24 V → ΔG = −nFΔE ≈ −237 kJ/mol (the M10 NADH→O₂ calculation, now from H₂).
- **Carbon (anabolism):** CO₂ fixed into all biomass via the **Calvin cycle → RuBisCO**
  (M13). Nitrogen from ammonia.

## Why it matters for climate
Decouples food from agriculture (no land, irrigation, weather, deforestation); potentially
far more area/energy-efficient than crops (panels + electrolysis + microbes can beat
photosynthesis's ~1% efficiency); can use captured CO₂ + renewable power. "Electro-
agriculture" / power-to-protein.

## Where ML + protein engineering come in (the point of all this)
- **O₂-tolerant, efficient hydrogenases** (enzyme design — M8/M20).
- **Faster CO₂ fixation**: better RuBisCO, or synthetic pathways (e.g. the designed CETCH
  cycle) — pathway/enzyme design.
- **Strain optimization**: protein yield, amino-acid profile, and lowering nucleic-acid
  (RNA/purine) content (uric-acid/gout limit for humans) — metabolic modelling + ML.
- **Bioprocess**: H₂ gas–liquid mass transfer (low solubility, echoes the CO₂ problem),
  safety around H₂/O₂.

## Prerequisites / study plan
Best tackled after: M8 (done), M10 (done), M12 (electron transport / chemiosmosis), M13
(carbon fixation). Then a dedicated module on chemolithoautotrophy + this application,
flowing into the ML design layer (M17+).

## See also
- `notes/m8-enzymes.md` (metalloenzymes, RuBisCO), `notes/m10-bioenergetics.md`
  (redox, ΔG=−nFΔE, reducing power), curriculum Part 5 capstone (M22).
