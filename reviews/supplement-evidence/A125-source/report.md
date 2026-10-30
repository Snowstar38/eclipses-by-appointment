# TIC 431278074 (TYC 3634-2713-1, Gaia DR3 1990144878402555136): per-object vet
Opus 5.5-model subagent for Fable 5, 2026-10-18 (saved by Fable from the agent's final message; the write tool refused in-agent). Batch row: G 10.63, P 6.38604 d, 4.8 ppt, 13 events, dphi +0.010, diffimg 3.61″.

## Verdict: CONFIRMED, with a second (shallow) eclipse found at the other conjunction

**1. Archives**
- cats.py: VSX has only Gaia DR3 1990145084560963584 [DSCT|GDOR] at 38″ (G 14.57), a neighbour. ASAS-SN and the EB tables: none. SIMBAD: [SB*].
- Gaia DR3 has no vari row. nss SB1:
  - P 6.385793 ± 1.12e-4, e 0.0855 ± 0.0065, ω 192.47 ± 4.18.
  - t_peri 0.3475 ± 0.0729, K1 64.06 ± 0.45, RUWE 0.85.
- SB9, WDS and veb: none. ExoFOP: no TOI or CTOI. Web search: no hits.
- MAST has QLP and TESS-SPOC for s16/17/57/77/84. Not previously catalogued as eclipsing.

**2. Eclipses** (`vet1.py`, `foldfit.py`, `stack_AB_431278074.png`)
- **Conjunction B** (ν = 270° − ω, primary in front, companion occulted): 14 QLP events.
  - Per-event trapezoid depth 5.78 ppt; stacked 5.25 ± 0.09 (QLP) and 5.42 ± 0.08 (SPOC PDCSAP).
  - T14 3.6 h, T23 1.1 h.
  - Per-event depth chi² 163/13, but SPOC reproduces each event's depth.
- **Conjunction A** (companion transits the primary): phase 0.5531 ± 0.0004 (QLP) / 0.5529 (SPOC).
  - Depth 1.20 ± 0.10 / 1.35 ± 0.06 ppt (jackknife by event), T14 2.2–2.4 h.

  | Sector | s16 | s17 | s57 | s77 | s84 |
  |---|---|---|---|---|---|
  | QLP depth (ppt) | 1.47 | 1.43 | 1.26 | 0.93 | 1.24 |

  - The blind census picks these up independently: 1741.52, 1767.06, 1779.90, 1786.23, 2859.07, 2871.86, 2878.27, 3587.16, 3593.51, 3599.92.
- s077 3417.56 has background z −11.6 and three bit-32 cadences nearby (`look_s077_3417.png`). It is on ephemeris and SPOC agrees.
- SPOC SAP "11 ppt" at s084 3596.4 lies in a flagged pre-gap ramp and is a systematic (`look_s084_3596.png`).

**3. Ephemeris**
- Conjunction B: P 6.386066 ± 3e-6 (formal), T0 1744.40878 ± 0.0006, O−C rms 3.1 min.
- Gaia: Δ = +0.00027 d = +2.4σ. Gaia's nominal conjunction B falls at phase −0.001.
- Spacing A − B = 0.55310 ± 0.00037, so **e cos ω = −0.0834 ± 0.0006** (A taken as the primary eclipse), against **Gaia −0.0835**.
- Durations: A is shorter (2.2–2.4 h vs 3.6 h), consistent in sign with Gaia's e sin ω = −0.0185, which puts the stars 3.8% further apart at A. For grazing chords the duration ratio amplifies e sin ω, so it doesn't measure it directly.
- SPOC minus QLP mid-times: 0.0 min median, 4.1 min rms.

**4. Independence**

TESS-SPOC (11–17 px, CROWDSAP 0.90–0.93):

| | B (deep) | A (shallow) |
|---|---|---|
| SAP depth (ppt) | 5.81 | — |
| PDCSAP depth (ppt) | 5.90 | 1.35 |

- Stacked centroid shift: +0.03 ± 0.04 and −0.08 ± 0.05 millipixel.
- Batch diffimg: peak on target, 3.61″.
- Neighbours: the nearest bright ones need 22% (G 14.57, the δ Sct/γ Dor at 38″) and 31% (G 14.92 at 39″). Everything else needs 44% to more than 100%. The SB1 phase match at both conjunctions rules out a blend independently.

**5. Physics** (`phys.py`)
- f(M) = 0.172 Msun, so M2 ≥ 0.92–1.05 Msun for M1 1.2–1.4: a G dwarf giving ~4–6% of the TESS-band light. That is consistent with SB1.
- Uniform-disk grazing solution: i ≈ 76°, b/(R1+R2) = 0.92–0.94 at B and 0.96–0.97 at A.
- Predicted depths: 5.3 ppt at B; 1.9–3.3 ppt at A before limb darkening, which suppresses grazing transits of the primary's limb and brings it to the observed 1.2–1.35. Predicted T14 is 4.2–4.8 h at B and 2.8–3.6 h at A.
- This explains why the occultation of the companion is deeper than the transit: the stars are 3.8% further apart at A and the geometry is grazing.
- Ellipsoidal cos2φ = −2.7 ppt in every sector, against ~6–7 predicted. Same factor-2 offset as TIC 310162414, so the formula or catalogue radius is the likely cause.

**6. Next eclipses** (BTJD, ±6 min)
- B (deep): 4337.1516, 4343.5376, 4349.9237
- A (shallow): 4340.6837, 4347.0698, 4353.4558

**Paper row:**
- Keep it; add a note: "deep eclipse = occultation of the G-dwarf companion at Gaia conjunction B; shallow 1.3 ppt eclipse at conjunction A, phase 0.553; e cos ω −0.0834 ± 0.0006 matches Gaia."
- Change the depth from 4.8 ppt (box) to 5.3 ppt (trapezoid).
- Optionally note the +2.4σ period offset.

**What would settle it further:** an SB2 spectrum to see the companion, or a limb-darkened model fitting both depths and durations.
