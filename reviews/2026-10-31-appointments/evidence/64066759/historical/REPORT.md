> Historical report: superseded by the current reconciliation at ../../../reports/64066759/REPORT.md. Its original bytes are preserved in the source archive; this public copy is sanitized.

# TIC 64066759 (TYC 6531-2972-1): adversarial check

Gaia DR3 SB1, P 40.92665 ± 0.01620 d, e 0.5160 ± 0.0100, ω 61.95 ± 1.52°, K1 33.24 km/s. G 11.275, BP−RP 1.00, parallax 2.931 mas (341 pc), RUWE 1.70, Teff 5392 K, logg 4.07 (Gaia); TIC R 2.05 R☉. Checked by an Opus checker for Fable 5.1, 2026-10-22 (chunk-3 wave 5, 19:22–19:28). Saved from the checker's final message by Fable 5.1; the file tool refused REPORT.md. Scripts and outputs are in this folder, each step checkpointed in `progress.md`; downloads in `[local path omitted]

## Verdict: CONFIRMED

TESS sees only the A eclipse. It is a grazing transit of a roughly 0.7 Msun companion across the primary, close to periastron. The B eclipse (the occultation of the companion) cannot happen in this geometry.

## 1. Archives queried
- **ExoFOP:** HTTP 503 (curl and `arch2.py`). CTOIs are unchecked.
- **NASA Exoplanet Archive TOI table:** no TOI for tid 64066759.
- **Gaia DR3** (`gaia_q.py`, `arch2.py`):
  - Target: G 11.275, BP−RP 1.00, parallax 2.931 mas (341 pc), RUWE 1.70, NSS SB1.
  - Orbit: P 40.92665±0.01620 d, e 0.5160±0.0100, ω 61.95±1.52°, Tp 9.7375±0.1384 (BTJD 398.74), K1 33.24 km/s.
  - gaia_source: rv_amplitude_robust 66 km/s, Teff 5392 K, logg 4.07, ipd_frac_multi_peak 0.
  - vari_summary: 0 rows. vari_eclipsing_binary: 0 rows.
- **VizieR TAP:** VSX 0, SB9 0, WDS 0.
- **viz.py (VizieR cone sweep):** VSX, Prša+2022, IJspeert+2024 and Kostov t2/t3/t4 all returned 0 rows. The later cones in the script (ASAS-SN, ATLAS, ACVS and the rest) had not returned by the time I wrote this; see `viz.txt`.
- **cats.py:** VSX none, ASAS-SN none. SIMBAD has TYC 6531-2972-1 as [SB*] only.
- **Web search** on both names: nothing about this star ([arXiv 2510.27470](http[local path omitted]) and [arXiv 2508.13941](http[local path omitted]) came up, but neither lists it).
- **MAST CAOM** (10″ cone): QLP for s7/33/34/87/88; TARS for s7/33/34/87/88; TESS-SPOC for s7/33/34; TGLC, eleanor-lite and T16 for s7. No SPOC 2-min data. The TGLC download came out corrupt or truncated, so I did not use it.
- **No prior art found.**

## 2. Every eclipse measured (`ecl.py` → `ecl.txt`, `ecl.json`)
Trapezoid fits to raw flux:

| Event | Pipeline | t0 (BTJD) | Depth | T14 | T12 | Flat |
|---|---|---|---|---|---|---|
| s087 A | QLP SAP | 3674.52085 ± 1.1 min | 2.20% | 4.16 h | 1.54 h | 1.09 h |
| s087 A | TARS | 3674.52228 | 2.48% | 4.43 h | | |
| s088 A | QLP SAP | 3715.45857 ± 1.1 min | 2.35% | 4.22 h | 1.75 h | 0.72 h |
| s088 A | TARS | 3715.45765 | 2.37% | 4.21 h | | |

- **s087 and s088:** no flagged cadences. Background change is −25 and −27 e/s against an out-of-eclipse scatter of 66 and 83 (under 0.4 sd). Centroid shifts are 0.002–0.010 px, at most 2.7 sd (s87 dy). The A-shape flat bottoms are not real totality; the event is grazing (see section 5).
- **s007 A (partial):** the first cadence after the gap is 1504.72, about at ingress, so the bottom and egress are seen. QLP flags 5 of its 9 in-eclipse cadences; TESS-SPOC, eleanor and TARS flag none. With the shape fixed from s87/s88, t0 is:
  - QLP 1504.82396
  - TESS-SPOC 1504.82198
  - TARS 1504.82253
  - eleanor 1504.82139

  The spread is 1.4 min. Fitting the depth freely gives 2.09–2.24%.
- **Blind census** of every sector (`look.py`, plus 3–14 h boxes in `bnull.py`): nothing else deeper than about 0.4% in QLP. The 0.2–0.4% "dips" in TARS also appear at many unrelated times, so they are systematics.

## 3. Ephemeris and Gaia comparison (`ephem.py`, `conjmc.py` with this star's own corr_vec, `bnull.py`)
- **A ephemeris:** T0 = 3674.52086 ± 0.8 min, P = 40.93771 ± 0.00004 d, O−C under 0.02 min.
- **s007 as an independent check:** the period from s87/s88 alone is 40.9377 ± 0.0011 d. Projected back 53 cycles, that allows ±84 min at s007, and the observed time lands 0.0 min from the prediction.
- **Gaia P:** the difference is +0.0111 d, which is +0.68σ.
- **Against the Gaia A predictions:**
  - 1504.655 ± 0.345: +0.49σ
  - 3673.769 ± 1.200: +0.63σ
  - 3714.696 ± 1.217: +0.63σ
- **Aliases:** no dip at the P/2 epochs (2221.23, 3694.99) or the P/3 epochs (3688.17, 3701.81). Both aliases are excluded.
- **B eclipse** (Gaia puts it at phase 0.6713 ± 0.0091 after A, i.e. A + 27.48 ± 0.37 d):
  - **3702.00 (s088):** the window is fully covered. QLP upper limit is 0.37–0.49% (3σ, boxes of 3–14 h); the largest box value sits on the pre-gap downturn at 3703.4. TARS peaks at 0.14 ± 0.02%, which is within its own systematics.
  - **1491.37:** 0.27 d before s007 starts.
  - **2228.24:** in the gap between s033 and s034.
- **e cos ω, e sin ω:** cannot be measured from the eclipses, because no B eclipse is seen. Gaia gives e cos ω 0.243 ± 0.013 and e sin ω 0.455 ± 0.010.

## 4. Independence tests
- **Other pipelines:** every A event appears in every available pipeline. For s007 that is four (QLP, TESS-SPOC, TARS, eleanor), with t0 agreeing within 2.6 min; for s87/s88 it is QLP and TARS, agreeing within 2 min.
- **Per-pixel regression on TESScut 11×11 cutouts** (`pixreg_trap.py`):

| Sector | Target-pixel depth | Deficit to target | Deficit to light centroid |
|---|---|---|---|
| s87 | 2.26 ± 0.05% | 3.1″ | 8.0″ |
| s88 | 2.32 ± 0.06% | 1.1″ | 3.6″ |

  The strongest deficit pixel is next to the target in both sectors.
- **Neighbour dilution** (the dip each would need is 2.3% × 10^(0.4 ΔG)):

| Neighbour | Separation | Needed dip | Result |
|---|---|---|---|
| G 16.78 | 2.6″ | 365% | impossible |
| G 17.49 | 7.5″ | 700% | impossible |
| G 16.11 | 19.9″ | 200% | impossible |
| G 16.01 | 33.1″ | 180% | impossible |
| G 15.42 | 54.6″ | 104% | impossible |
| G 14.71 | 44.8″ | 55% | possible in principle, but its pixel shows only 1.65/1.88% (the target's wings), and the deficit centroid is on the target |
| G 11.29 (equal brightness) | 78.3″ | about 2.3% | its pixel shows −0.03 / −0.08%, so excluded |

## 5. Physics (`physics.py` → `physics.txt`)
- **Masses and orbit:** f(M) = 0.0979 ± 0.0027 Msun. m2 at i = 90° is 0.61 / 0.68 / 0.74 Msun for M1 = 0.9 / 1.1 / 1.3. Semi-major axis a ≈ 60.6 Rsun. The separation is 30.5 Rsun at A and 81.5 Rsun at B (ratio 2.67).
- **A conjunction (ν = 90° − ω):** the K-dwarf companion (R2 ≈ 0.7) is in front of the primary, near periastron.
- **Inclination:** a central A transit would last 8.2 h; the observed 4.19 h gives b_A/(R1+R2) ≈ 0.86 and i ≈ 85.6°. That is a grazing transit, which matches the V/U shape.
- **B (occultation of the companion):** it would need b_A/(R1+R2) < 0.37. It eclipses in none of the 200,000 draws, so the miss is predicted, not suspicious. The companion is also only about 6–11% of the light in the TESS band.
- **One mild tension:** the predicted A depth depends on R1. It is 2.25% [1.96, 2.58] for R1 = 1.5–1.7 Rsun, which matches Gaia's logg 4.07 (R1 ≈ 1.5–1.65). It is only about 1.2% for R1 ≈ 2.0, which is the TIC radius and my own estimate from luminosity. The observed 2.2–2.35% therefore favours R1 ≈ 1.6. The model is crude (straight chord, linear limb darkening, uniform overlap), so this is not a refutation.

## 6. Verdict
**CONFIRMED.** The deciding numbers:
- Three A eclipses in four independent pipelines.
- The s007 time is predicted to 0.0 min by the period from s87/s88 alone.
- P agrees with Gaia (+0.68σ), and every A time is within 0.63σ of Gaia's conjunction.
- The pixel deficit is on the target (1–3″) in two sectors, and no neighbour can host the dip.
- The absence of a B eclipse is required by the geometry (B needs b_A/(R1+R2) < 0.37; b_A/(R1+R2) is 0.86).

**Next A eclipses (BTJD):** 4370.462, 4411.400, 4452.337, 4493.275 (±1–2 min). Depth about 2.3%, T14 about 4.2 h.

**B conjunctions (BTJD), where no eclipse is expected:** 4357.01, 4397.94, 4438.88 (±0.37 d).

**What would settle it further:**
- A two-sphere limb-darkened fit of A to pin down R1, i and k.
- Spectroscopy to fix R1 (the logg 4.07 vs TIC R 2.05 question).
- A check of CTOIs once ExoFOP is back.

Services that could not be checked: ExoFOP (503); the TGLC s7 light curve (corrupt download).
