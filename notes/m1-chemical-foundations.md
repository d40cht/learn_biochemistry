# Chemical foundations of life (M1)

> Almost all of biochemistry's "chemistry" rests on four ideas — bonding, water,
> energy, and rates. This note covers bonding, water, and acids/bases. Energy/rates
> get their own note (M2), which we opened early because a buffer question demanded it.

## Mental model
Chemistry is about **electrons rearranging to lower the system's free energy**. The
nucleus just sets the positive charge; electrons do everything interesting. Keep
asking "where are the electrons / the charge?" and most of this subject falls out.

## Key concepts

### Bonding & electronegativity
- **Covalent bond:** two atoms *share* an electron pair that sits between the nuclei;
  both positive nuclei are attracted to it (the glue). Dominant bond in biomolecules
  (C–C, C–H, C–O, C–N).
- **Ionic bond:** the extreme of greed — one atom *takes* the electron(s) outright,
  giving two **fully** charged ions held by Coulomb attraction (Na⁺Cl⁻).
- **Electronegativity** = an atom's greed for the shared electrons. O, N greedy;
  C, H mild.
  - Unequal greed → electrons lean toward the greedy atom → **partial** charges
    (δ−/δ+) → a **polar** bond (a little dipole).
  - Equal greed (C–C, C–H) → **nonpolar**.
- So there's one spectrum: nonpolar covalent → polar covalent → ionic, set by the
  electronegativity *difference*.

### Water, hydrogen bonds, and the hydrophobic effect
- Water is H–O–H; O is much greedier → polar O–H bonds → bent molecule is a permanent
  **dipole** (δ− O, δ+ H's).
- **Hydrogen bond:** a δ+ H (bonded to O/N/F) is attracted to a **lone pair** on a
  nearby greedy atom. Weak (~1/20 of a covalent bond), **directional**, decisive in
  bulk. Each water makes up to **4** (donate 2, accept 2) → a 3D network. Explains
  water's high boiling point, ice floating, solvent power.
- **Dissolving:**
  - polar/H-bonding solutes (sugar's –OH) → **hydrogen bonds** with water → hydrophilic.
  - ions (Na⁺, Cl⁻) → **ion–dipole** interactions (water's δ− O swarms Na⁺, δ+ H swarms
    Cl⁻) → dissolved. *NaCl has no H, so no hydrogen bonds involved.*
  - nonpolar (oil) → nothing to grab → hydrophobic.
- **The hydrophobic effect is driven by water's entropy, not a force on the grease.**
  Water touching a nonpolar surface must order itself into a cage to keep H-bonding to
  its neighbours — low entropy, costly. The system minimises exposed nonpolar surface
  by **clustering nonpolar stuff together**, freeing the water. Driving force = water
  regaining entropy.
- **Protein folding:** a chain of greasy + polar/charged side chains folds in water to
  bury the greasy ones in a **core** and expose the polar ones. The hydrophobic effect
  is the dominant driving force → turns "a chain" into a *specific* shape. Other forces
  fine-tune the winner: backbone **hydrogen bonds** (build α-helices / β-sheets), **van
  der Waals** packing, **salt bridges**, sometimes covalent **disulfide** bonds.
- **Folding is environment-dependent.** Remove water → no hydrophobic effect → different
  structure. Proof: **membrane proteins fold "inside-out"** — segments in the nonpolar
  lipid bilayer put their *greasy* residues facing outward. The environment calls the
  shots, not a fixed property of the residues.

### Acids, bases, pH, buffers
- Water self-ionises: 2 H₂O ⇌ H₃O⁺ + OH⁻. Pure water [H⁺] = 10⁻⁷ M.
- **pH = −log₁₀[H⁺].** pH 7 neutral; lower = more H⁺ = acidic; higher = basic. Log
  scale: one unit = 10× the H⁺.
- **Acid = proton donor; base = proton acceptor** (Brønsted–Lowry). Deeper (Lewis):
  acid = electron-pair *acceptor*, base = electron-pair *donor*; a proton is just the
  simplest electron-pair acceptor.
- **In electron terms:** an acid releases a proton **while keeping the bonding
  electrons** → becomes A⁻ (negative). The departing H is a bare proton; it never
  floats free — it lands on a water lone pair → **H₃O⁺**. A base **donates a lone pair**
  to grab a proton → becomes BH⁺ (positive). The H–A bond is **polar covalent**; the
  more polar, the stronger the acid.
- **What makes a good acid:** stability of the conjugate base A⁻. Helped by (i) an
  electronegative atom holding the charge, (ii) **resonance** spreading it (carboxylate
  –COO⁻ spreads charge over two O's → decent acid; an alcohol –OH can't → barely acidic),
  (iii) inductive electron-withdrawal.
- **Buffer:** a mix of a **weak acid (HA)** *and* its **conjugate base (A⁻)**, both
  stocked in large amounts. Resists pH change from both sides: add H⁺ → A⁻ mops it up
  (→ HA); add OH⁻ → HA donates an H⁺. Capacity is finite (drain a reservoir and it
  breaks); strongest near pKₐ.

## The maths
- pH = −log₁₀[H⁺].
- Henderson–Hasselbalch: pH = pKₐ + log([A⁻]/[HA]). **pKₐ** = the pH at which the acid
  is half-dissociated; pH depends on the *log of the ratio*, so big reservoirs ⇒ pH
  barely moves. Worked example in `problems/`.
- Why equilibrium exists at all (both species coexist rather than fully neutralising):
  see M2 — systems minimise **free energy** G = H − TS, not energy.

## Climate / ML anchor
- The **bicarbonate buffer** runs the carbon-cycle reaction
  CO₂ + H₂O ⇌ H₂CO₃ ⇌ H⁺ + HCO₃⁻. This *is* ocean acidification (more atmospheric CO₂
  → more H⁺ → lower ocean pH). The enzyme **carbonic anhydrase** makes it fast and is a
  carbon-capture engineering target (M8/M13).
- Acids/bases set **side-chain charge**: –COOH (Asp/Glu) → –COO⁻ (negative); –NH₂ (Lys)
  → –NH₃⁺ (positive); **histidine** (pKₐ ≈ 6) flips charge near physiological pH → the
  go-to proton shuttle in enzyme active sites. Charge state governs folding & catalysis.
- ML hook: "where does the charge sit on this molecule" = partial-charge / electrostatic
  features; part of why pure-sequence models eventually want 3D/chemistry awareness.

## Common misconceptions / things that tripped me up
- The hydrophobic effect is about **water's entropy**, not grease being repelled.
- Salt is **ionic** (full charges), not polar (partial charges); it dissolves by
  **ion–dipole**, not hydrogen bonding.
- An acid doesn't "accept an electron from water" — it **leaves its bonding electrons
  behind on A** and sends off a bare proton.
- Equilibrium ≠ used up: it's a **dynamic** balance with both species coexisting.

## See also
- `notes/m2-free-energy.md` (why equilibrium is a mixture).
- `flashcards/decks/m1-chemical-foundations.md`.
- `problems/m1-buffer-capacity.md`.
