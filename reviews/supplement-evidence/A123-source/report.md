# TIC 78448518 (GSC 05962-01229 / TYC 5962-1229): per-object vet
Opus-model subagent for Fable 5, 2026-10-18 (saved by Fable from the agent's final message; the write tool refused in-agent). Batch row: G 10.92, P 11.87442 d, 3.3 ppt, 4 events, dphi +0.011.

**Verdict: CONFIRMED.** An eccentric, grazing F + K-dwarf eclipsing binary with both eclipses detected. Gaia SB1: P 11.872953 ± 0.000877, e 0.229 ± 0.008, ω 192.0 ± 2.6°, K1 37.6 km/s.

**1. Archives**
- cats.py at r = 60″: VSX has only a ROT star (P = 2.218 d) at 56″. ASAS-SN and the EB tables: none.
- SIMBAD: GSC 05962-01229 [SB*], plus TYC 5962-1229-1 and -2 at 0.3″.
- WDS 06505-2223 = TDS4200: a 0.6″ Tycho pair (11.57 / 11.79), note "X" (dubious). Gaia shows a single source, with ipd_frac_multi_peak 0 and RUWE 1.38.
- Gaia DR3 variability tables: none. SB9: none. ExoFOP: no TOI or CTOI.
- No separate web search was run; SIMBAD has nothing beyond the SB* entry. **New EB.**

**2. Primary eclipse** (at conjunction B)
- 7 covered events: 1489.00, 1500.88, 1512.75, 2213.33, 2225.21, 3673.88, 3685.77. The epoch at 1477.13 falls in a data gap. The batch's sapdepth check counted only 4.
- Joint fit with exposure-time supersampling: depth 3.87 ± 0.13 ppt, duration 2.95 ± 0.14 h, ingress 1.18 h.
- Per-event depths 3.69–4.25 ppt, all consistent.
- Background and centroids through the events: all within 2.5σ. Flags: only one bit-32 cadence, outside the core.
- No overlap with the sector-systematic times.

**3. Ephemeris**
- T0 = BTJD 1477.12450 ± 0.00296, P = 11.874406 ± 0.000027 d. Errors are scaled by χ²/dof = 5.8, since O−C scatter is about ±8 min.
- Against Gaia's period: +1.66σ.
- Jackknife: P stays within 11.874362–11.874427, at +1.60 to +1.68σ from Gaia for every dropped event. No event owns the result.
- Gaia conjunction B is predicted −0.0106 ± 0.0075 phase from the eclipse at the s006/s007 epoch.

**Secondary eclipse** (at conjunction A)
- Phase 0.6436 ± 0.0002, depth 1.84 ± 0.18 ppt (V-shaped), duration 1.79 ± 0.15 h, Δχ² 177.
- Present in all 7 covered epochs at 1.3–2.9 ppt each; dropping any one epoch leaves Δχ² between 134 and 177.
- Gaia predicts the separation between conjunctions A and B as 0.6414 ± 0.0051, so they agree to 0.4σ.
- Exact Kepler solution: e cos ω = −0.2271; Gaia gives −0.2240.

**4. Independence**
- TESS-SPOC primary / secondary: s006 3.64–3.88 / 2.08; s007 3.70–3.84 / 2.28; s033 3.60–3.78 / 1.45–1.62 ppt.
- TGLC s006/s007: 3.2–4.9 / 1.6–2.7 ppt. Eleanor-lite was downloaded but not measured; the TASOC corrected flux was unusable.
- Own TESScut s087 photometry, primary: 3.79 / 3.77 / 3.88 ppt at r = 1.0 / 1.6 / 2.5 px, so the depth does not change with aperture.
- s087 primary difference image peaks on the target (−1.4″). The secondary difference image is too weak to place.
- The batch's s033 difference image also had the peak on target, 1.6″ off.
- Neighbours: G 16.51 at 57″ would need a 67% dip; G 16.92 at 32″ would need 97%. Nothing brighter lies within 78″.
- Census (3-h box, at least 1.5 ppt): the 7 primaries plus one s087 single at 3683.53 (S/N 4.2, unexplained).

**5. Physics**
- Mass function f(M) = 0.0602 M☉. For M1 = 1.2–1.5, m2(i = 90°) = 0.58–0.65 M☉ and a = 27 R☉.
- Eclipses need i above about 85.5°.
- Grazing model (`s2_geom.py`: two limb-darkened disks on Gaia's orbit) fits all four observables with χ² ≈ 1: i ≈ 85.9°, R2 0.50–0.65 R☉, companion surface brightness ratio J ≈ 0.24, so T2 ≈ 4300 K, matching m2.
- **Which star is in front:**
  - Deep eclipse at conjunction B: the F star occults the K dwarf. Projected separation there is 10% smaller, because e sin ω = −0.048.
  - Shallow eclipse at conjunction A: the K dwarf grazes the F star's limb.
- The ω-flipped alternative fails (χ² ≈ 1800).
- Ellipsoidal (about 0.1 ppt) and beaming (about 0.4 ppt) signals are too small to test against QLP systematics at this period.

**6. Next eclipses** (BTJD, ±10–12 min)
- Deep (conjunction B): 4338.8563, 4350.7308, 4362.6052
- Shallow (conjunction A): 4334.6243, 4346.4987, 4358.3731
- What would settle it further: a light-curve fit to the 200-s data to measure i and R2, and RVs to check for the companion's lines.

**Paper row:** 7 + 7 events (not 4), add the secondary at phase 0.6436 (1.8 ppt), e cos ω −0.227, P 11.874406 ± 0.000027. Nothing argues for striking or demoting it. Optional footnote: WDS TDS4200, a 0.6″ Tycho double flagged "X" (dubious), which Gaia does not see.
