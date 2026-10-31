> Historical report: superseded by the current reconciliation at ../../../reports/12864953/REPORT.md. Its original bytes are preserved in the source archive; this public copy is sanitized.

# TIC 12864953 (TYC 5842-841-1): adversarial check

Gaia DR3 2367821453175214720, SB1, P 31.62452 ± 0.00589 d, e 0.467 ± 0.0125, ω 340.3 ± 2.0°, e cos ω 0.439 ± 0.014, e sin ω −0.1576; G 11.37, RUWE 1.20; TIC R 1.67 R☉. Checked by an Opus checker for Fable 5.1, 2026-10-22 (chunk-3 wave 6, 19:37–19:46, under a 15-minute cap). Saved from the checker's final message by Fable 5.1; the file tool refused REPORT.md. Scripts and outputs are in this folder, a checkpoint for every step in `progress.md`; downloads in `[local path omitted] Unused scripts copied from other folders were deleted.

## Verdict: CONFIRMED

Both eclipse kinds are real, on target and seen by four pipelines, and the physics fits Gaia's orbit. Two caveats: TESS has only one sector of data, and the timing disagrees with Gaia's e/ω at 3.4σ.

## 1. Archives (what I queried and what came back)
- **MAST CAOM, 10″ cone** (`archives.py`, output in `archives.json`): only two TESS sectors exist.
  - Sector 29: QLP at 600 s.
  - Sector 69: QLP at 200 s, SPOC at 120 s, TESS-SPOC at 200 s, and TARS.
- **Gaia TAP** (`arch2.py`, `gaia_q.py`):
  - The full NSS row, including corr_vec, was retrieved and used.
  - vari_summary and vari_eclipsing_binary have 0 rows; phot_variable_flag is NOT_AVAILABLE.
  - RUWE is 1.20. rv_amplitude_robust is 58 km/s, consistent with 2K₁ = 58.
  - Within 90″ there is no neighbour brighter than G 18.06; that star is 53″ away, and the target is G 11.37.
- **VizieR asu-tsv** (`viz.py`): 0 rows in VSX, Prša+2022, IJspeert+2024, Kostov t2/t3/t4, ASAS-SN vars, SB9, WDS, ATLAS, Gaia vclassre and ASAS ACVS. The J/A+A/674/A16 hit is the synthetic-photometry table, not prior art.
- **cats.py:** VSX none, ASAS-SN none. SIMBAD lists TYC 5842-841-1 as type SB*, which is not an eclipsing type.
- **ExoFOP: HTTP 503**, on both the arch2 request and a direct curl, so **CTOIs were not checked**. The NASA Exoplanet Archive TOI table has no TOI for this TIC.
- **Web search** for "TYC 5842-841-1" / "TIC 12864953": nothing about this star.
- **No prior art found.**

## 2. Eclipses measured (sector 69 only)
Sector 29 cannot be used:
- QLP SAP_FLUX is all NaN.
- The TESScut sector-29 cutout is empty: the median is 0 in every pixel, and the reference row is 2059, which is off the science array.

So the target was effectively not observed in sector 29, and **neither Gaia window there can be tested.**

Trapezoid fits (`ecl1.py`, raw SAP, QUALITY==0, quadratic baseline over ±1 d):

| pipe | kind | t0 (BTJD) | depth | T14 (h) | T12 (h) |
|---|---|---|---|---|---|
| QLP | B | 3196.10016 | 1.043% | 6.05 | 1.94 |
| SPOC 120 s | B | 3196.09856 | 1.084% | 6.38 | 2.33 |
| TESS-SPOC | B | 3196.09867 | 1.073% | 6.37 | 2.32 |
| TARS | B | 3196.10331 | 1.079% | 6.13 | 2.05 |
| QLP | A | 3204.10199 | 1.762% | 5.79 | 2.39 |
| SPOC 120 s | A | 3204.10155 | 1.724% | 5.93 | 2.64 |
| TESS-SPOC | A | 3204.10160 | 1.725% | 5.93 | 2.62 |
| TARS | A | 3204.10166 | 1.649% | 5.91 | 2.44 |

- The QLP all-cadence fits match the QUALITY==0 fits; there are no flagged cadences inside either eclipse.
- **Times:** the four-pipeline means are A 3204.1016 ± 0.001 and B 3196.0997 ± 0.0017. The errors come from the scatter between pipelines; the profile-χ² error is grid-limited at about 2–4 min.
- **Flat bottoms:** the trapezoid "flats" are not totality. The two-sphere fit makes both eclipses grazing.
- **Background:** SAP_BKG in-minus-out is −1.8 e/s in SPOC (out-of-eclipse sd 5 to 320) and −22/−55 in QLP (sd 1212/355). Nothing there.
- **Centroids** (`cent.py`, local quadratic trend removed): B moves +0.6 mpx in column against an out-of-eclipse rms of 2 mpx; A moves +0.3 mpx. At about 1% depth that puts the eclipsed source within about 1″ of the target.
- **Blind census** (`census.py`): the only dips deeper than 0.25% anywhere in sector 69 (QLP, SPOC, TESS-SPOC) are the two events. The 5-h box rms is 0.13–0.15%.
- **Common mode** (`commonmode.py`): the five sky neighbours in sector 69 show +0.02% and +0.00% in the same windows, against +0.97% and +1.49% for the target. Neither time is on the known-systematics list.
- **B and the orbit gap:** B falls about 0.7 d after the orbit-gap restart. It survives in all four pipelines and in the pixel test.
- **Short-period aliases** (`alias.py`): 3188.098 is covered and shows +0.07 ± 0.01% in SPOC and −0.01% in QLP. 3192.10 and 3200.10 are flat. That excludes P = 4, 8 and 16 d (the 16-d case would make the two dips alternating primary and secondary).

## 3. Ephemeris and the Gaia comparison
Gaia comparison (`phys.py`, Monte Carlo with this star's own corr_vec; `conjmc.py` gives `conj.json`):
- **P cannot be measured from TESS**, because there is one event of each kind.
- **O−C against Gaia:**
  - A: observed − predicted (3202.830 ± 0.598) = **+1.272 d, +2.13σ**.
  - B: observed − predicted (3195.666 ± 0.518) = **+0.434 d, +0.84σ**.
- **B−A phase separation:** observed 0.74697 ± 0.00006 against Gaia 0.7735 ± 0.0078, which is **−3.4σ**. Only 4.7e-4 of the Gaia draws have a separation this small. In days, A−B is 8.002 against Gaia's 7.16 ± 0.25.
- **What the observed separation implies:**
  - At Gaia's e, it needs ω = 325.5°, against Gaia's 340.3 ± 2.0°.
  - At Gaia's ω, it needs e = 0.419, against Gaia's 0.467 ± 0.0125.
- **Limb-darkened two-sphere fit** (`ebfit.py`, adapted from vet39013890 `ebfit3.py`; SPOC 120-s SAP; P fixed at Gaia's value; reduced χ² 1.010):
  - e cos ω = 0.396, e sin ω = −0.110, i = 87.51°.
  - r1 = 0.0364, r2 = 0.0107, k = 0.294, J = 0.187.
  - Impact parameters b_A = 1.115 and b_B = 0.894, so **both eclipses are grazing**.
  - That gives e = 0.411 and ω = 344.5°.
- **Fit with e sin ω fixed at Gaia's −0.1576:**
  - e cos ω = 0.3935, Δχ² = +5.9, which is about 2.4σ.
  - So **e sin ω is not decisive**: the formal ±0.004 is badly underestimated for grazing geometry.
  - **e cos ω = 0.39–0.40 is robust**, against Gaia's 0.439 ± 0.014, a −3.2σ tension.
- **Possible causes:** either Gaia's e/ω errors are underestimated, which is common for SB1 solutions, or e is really about 0.42.

## 4. Independence
- **Four pipelines** (QLP, SPOC 2-min, TESS-SPOC, TARS) all show both events, with matching times and depths. There is no second sector.
- **TESScut sector-69 per-pixel regression** (`pix3.py`, cubic trend plus a trapezoid template, half-windows 0.45 and 0.6 d):
  - For both events the highest-S/N deficit pixel is the target pixel, at S/N 22–33.
  - The deficit centroid is within 0.15 px of the target for both: B at (7.74–7.92, 7.65–7.69), A at (8.06–8.08, 7.62), with the target at (7.92, 7.57).
  - Fractional depth on the target pixel is 0.93–1.00% for B and 1.63–1.65% for A, falling off outward.
  - The quadratic version over a 0.7-d window (`pix.py`) failed on B because of the steep background trend after the gap.
- **Dilution:** no Gaia source brighter than G 18.06 lies within 90″. That source is 53″ away and would need a dip of more than 100%, so contamination is excluded.
- **B-window upper limit:** not needed, because both kinds are detected.

## 5. Physics
- **Masses:** f(M) = 0.0551 M☉. m2 at i = 90° is 0.50 M☉ for M1 = 1.01, and 0.48–0.55 for M1 = 0.95–1.2. a ≈ 48 R☉.
- **Separations at conjunction:** about 44.8 R☉ at A and 32.6 R☉ at B.
- **Durations:** central T14 would be about 11.3 h at A and 8.2 h at B. The observed 5.9 h and 6.4 h fit grazing chords.
- **Which star is in front:**
  - A (ν = 90° − ω, the deeper eclipse at 1.72%): the companion passes in front of the primary.
  - B (1.08%): the primary passes in front of the companion. B is deeper than its surface-brightness ratio alone would give, because its impact parameter is smaller (the separation at B is smaller).
- **Sizes from the fit:**
  - R1 = r1·a ≈ 1.76 R☉, against TIC's 1.67.
  - R2 ≈ 0.52 R☉.
  - J ≈ 0.19, which suggests a late-K/early-M companion.
- **Consistency:** this matches m2 ≈ 0.5 from the radial velocities, and the companion's TESS light comes out at L2/L1 ≈ 1.1–1.6%. Depths, durations and shapes are consistent with one geometry.

## 6. Verdict: CONFIRMED
**Deciding numbers:**
- Two eclipse kinds with S/N over 20 in the pixel regression, landing on the target pixel.
- Four independent pipelines agree within minutes.
- Common mode is zero, and no other dip appears in the sector.
- B is +0.8σ and A +2.1σ from Gaia's predicted conjunctions.
- The grazing two-sphere fit has reduced χ² 1.01 and gives R1 and m2 that match TIC and K₁.

**Caveats:**
- Only one sector, and one event of each kind, so P comes from Gaia alone.
- The B−A separation is in 3.4σ tension with Gaia's e/ω: photometry says e cos ω ≈ 0.395 against Gaia's 0.439.

**Next predicted eclipses** (BTJD; Gaia P 31.62452 ± 0.00589, anchored on the sector-69 events):

| A | B |
|---|---|
| 4342.584 ± 0.21 | 4334.583 ± 0.21 |
| 4374.209 ± 0.22 | 4366.207 ± 0.22 |
| 4405.833 ± 0.22 | 4397.832 ± 0.22 |
| 4437.458 ± 0.23 | 4429.456 ± 0.23 |
| 4469.083 ± 0.24 | 4461.081 ± 0.24 |
| 4500.707 ± 0.24 | 4492.705 ± 0.24 |

**What would settle it further:**
- Any later TESS sector, or ground photometry of a 1.7% A eclipse (about 5.9 h long), would give P directly. That would test Gaia's P and whether the e cos ω tension is real.
- Checking CTOIs once ExoFOP is back up.
- Archival ground surveys (ASAS-SN or ATLAS light curves, not just the catalogue cones) could also pin down P.

**Services that could not be checked:** ExoFOP (HTTP 503), so CTOIs are unchecked.
