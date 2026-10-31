> Historical report: superseded by the current reconciliation at ../../../reports/395790195/REPORT.md. Its original bytes are preserved in the source archive; this public copy is sanitized.

# TIC 395790195 (TYC 3608-708-1): adversarial check

Gaia DR3 SB1, P 55.41448 ± 0.03514 d, e 0.3889 ± 0.0232, ω 169.45 ± 3.58°, K1 30.50 km/s, significance 39.2. G 11.45, BP−RP 0.81, parallax 1.605 mas, RUWE 0.92; TIC R 2.52 R☉. Checked by an Opus checker for Fable 5.1, 2026-10-22 (chunk-3 wave 5, 19:22–19:28). Saved from the checker's final message by Fable 5.1; the file tool refused REPORT.md. Scripts and outputs are in this folder, the working log in `progress.md`; downloads in `[local path omitted]

## Verdict: CONFIRMED

The star is a real detached eclipsing binary. Both kinds of eclipse are there, and the eclipses give the same orbit Gaia found (e 0.384 vs 0.389, ω 169.1° vs 169.4°). The period is 55.4604 d, not Gaia's 55.414, which matches the classifier's guess of 55.46. Nothing here is prior art.

## 1. Archives queried
- **Gaia DR3** (`gaia_q.py`, `arch2.py`): G 11.45, BP−RP 0.81, parallax 1.605 mas, RUWE 0.92.
  - NSS SB1 orbit: P 55.41448 ± 0.03514 d, e 0.3889 ± 0.0232, ω 169.45 ± 3.58°, Tp −13.238 ± 0.483 (BTJD 375.762), K1 30.50 km/s, significance 39.2.
  - Radial velocities: 32 transits, rv_amplitude_robust 66.3 km/s, rv_chisq_pvalue 0.
  - vari_summary: 0 rows. vari_eclipsing_binary: 0 rows.
- **VizieR TAP** (VSX, SB9, WDS): 0 rows each.
- **VizieR asu-tsv 60″ cones** (`viz.py`): 0 rows in VSX, Prša+2022, IJspeert+2024, Kostov t3, Kostov t4, ASAS-SN II/366, SB9, WDS, ATLAS, Gaia vclassre and ASAS ACVS.
  - Kostov table 2 flags 7 neighbours 22–55″ away (TIC 395790188, 395790221, 395790213, 395790207, 395790153, 395790149, 2010914314). The target itself is not flagged, and that table is an unvetted ML list anyway.
  - The 591 "Mowlavi" rows are the synthetic-photometry table, not prior art.
- **cats.py**: no VSX or ASAS-SN entry. SIMBAD lists TYC 3608-708-1 as [SB*].
- **ExoFOP**: HTTP 503 (tried once in the script and once with curl), so CTOIs are unchecked.
- **NASA Exoplanet Archive TOI table**: no TOI for this TIC.
- **Web search** for "TYC 3608-708-1" OR "TIC 395790195": no pages about this star.
- **MAST CAOM** (`archives.py`) has these light curves:
  - QLP for sectors 15, 16, 56, 76 and 83
  - TESS-SPOC for s15 and s16
  - TASOC for s15
  - No SPOC 2-min, TGLC, TARS or eleanor products.

## 2. Eclipses measured
I used raw SAP flux with a trapezoid plus quadratic baseline (`ecl.py` → `ecl.txt`, `ecl_fits.png`).

| Kind | Mid-time (BTJD) | Depth | T14 | T12 | Flat | Pipelines |
|---|---|---|---|---|---|---|
| B | 1715.6262 ± 0.9 min (TSPOC) | 8.5–9.2% | 13.3 h | 5.1 h | 3.0–3.2 h | QLP 1715.6253; TSPOC; TASOC 1715.607 ± 6.7 min (6.4%, noisier) |
| A | 1756.3704 ± 0.7 min | 12.8–13.2% | 12.0 h | 4.6 h | 2.7 h | QLP and TSPOC agree within 0.1 min; egress fully covered |
| B | 3379.4389 ± 0.8 min (QLP, 200 s) | 8.8% | 13.4 h | 5.1 h | 3.2 h | QLP only |

- **Quality flags:** no flagged cadences inside the q0 eclipses. The B eclipse at 1715.6 sits next to flagged stretches in s15, but it is unflagged in TESS-SPOC.
- **Background:** the in-minus-out excursion is at most 0.7 of the background's own standard deviation, in its own units, for every event.
- **Centroids:** shifts are at most 0.012 px (QLP) and 0.002 px (TESS-SPOC).
- **Common mode** (`commonmode.txt`): at the three times, other stars on the same camera/CCD dip at most 0.80%, 0.43% and 0.14%, against 8.5%, 12.4% and 8.3% for the target. None of the times are on the brief's list of known systematics.
- **Blind census** (`census.txt`, 0.2-d box, threshold max(0.3%, 5σ)):
  - In QLP-good cadences (q0), only these three eclipses appear across all five sectors.
  - Including flagged cadences adds only scattered-light stretches: s15 1720.8, 1721.8, 1735.4, 1737.3; s16 1749.1, 1750.4, 1762.5; s56 2838.6 (0.3%).

## 3. Ephemeris and Gaia comparison
- **Period from the two B eclipses:** 30 cycles apart, giving P = 55.460424 ± 0.000033 d. 29 or 31 cycles would give 57.37 or 53.67 d, both excluded by Gaia.
  - Against Gaia's 55.41448 ± 0.03514 that is **+1.31σ**.
  - A has a single event, so it has no separate ephemeris, and O−C is trivially zero.
- **Joint limb-darkened two-sphere fit** of all three eclipses (`ebfit3.py q0`; reduced χ² 1.01):
  - P = 55.460455 ± 0.000021 d, T0(A) = 1756.36926 ± 0.00018
  - e cos ω = −0.3767 (Gaia −0.3816 ± 0.0235, +0.2σ)
  - **e sin ω = 0.0727 ± 0.0028** (Gaia 0.0709 ± 0.0240, +0.1σ)
  - That gives **e = 0.3837, ω = 169.07°**, against Gaia's e = 0.3889 and ω = 169.45°.
  - i = 88.70°, r1 = 0.02856, r2 = 0.01098, k = 0.384, surface-brightness ratio J = 0.786, L2/L1 = 0.112 in the TESS band.
  - Impact parameters are 0.631 R1 at A and 0.730 R1 at B, both above 1−k = 0.616. So **both eclipses are partial**, and the trapezoid flats are not totality. That is why I took e sin ω from this model rather than from the duration ratio.
- **Phase of B after A:** 0.26535, against Gaia's Monte Carlo 0.2625 ± 0.0138 (+0.2σ).
- **Gaia predicted conjunctions** (`conjmc.py`, using this star's own corr_vec, in `conjmc.txt`). All three offsets come from the same cause, Gaia's period being 1.3σ short:

| Kind | Gaia prediction | Observed | Offset |
|---|---|---|---|
| B | 1714.26 ± 0.74 | 1715.626 | +1.37 d (+1.8σ) |
| A | 1755.13 ± 1.26 | 1756.370 | +1.24 d (+1.0σ) |
| B | 3376.69 ± 1.75 | 3379.439 | +2.75 d (+1.6σ) |

## 4. Independence tests
- **Second pipelines:** TESS-SPOC s15 and s16 show the same B and A events, with times within 1.3 min of QLP and depths 8.5% and 12.8%. TASOC s15 shows the B event as well.
- **Pixel regression** on 11×11 TESScut cutouts (`pixreg.py` → `pix_s16A.txt`, `pix_s76B.txt`):

| Event | Deficit centroid from target | Target-pixel depth | 3×3 aperture | 5×5 aperture |
|---|---|---|---|---|
| A, s16 | 3.7″ | 12.70 ± 0.08% | 12.2% | 10.8% |
| B, s76 | 2.4″ | 8.59 ± 0.04% | 8.3% | 7.3% |

  Depth falls off with distance from the target, and the largest detection inside the 3×3 box is well above anything outside it (163σ vs 77σ, and 210σ vs 48σ).
- **Dilution:** no Gaia neighbour within 60″ is brighter than G 14.40. That is at least 2.95 mag fainter than the target, so a neighbour would need a dip of at least 13.2% × 10^(0.4×2.95) ≈ 200%, which is impossible. The nearest source is G 19.55 at 4.8″, and its required dip is far above 100%.
- **Uncovered windows:** TESS covered no other eclipse window.
  - B in s56 at 2824.84: egress ends at 2825.13, but the data start at 2825.26.
  - A in s76 at 3364.75: before the sector starts.
  - A in s83 at 3586.58: after the sector ends.

## 5. Physics
`physics.py` → `physics.txt`.
- **Mass function:** f(M) = 0.1273 Msun.
- **Companion mass:** m2 = 0.80, 0.83, 0.87, 0.90 and 0.94 Msun for M1 = 1.2, 1.3, 1.4, 1.5 and 1.6 Msun (i = 88.7°, the same as at 90°).
- **Separation and radii:** a = 77–84 Rsun, giving R1 = 2.2–2.4 Rsun (TIC says 2.52, which is slightly inflated by the companion's light) and R2 = 0.85–0.92 Rsun.
- **Durations:** the central T14 would be 14.4 h at A and 16.7 h at B. The observed 12.0 h and 13.4 h fit impact parameters of 0.63 and 0.73, in the ratio the eccentric geometry predicts (separation 0.795a at A and 0.920a at B).
- **Which star is in front:**
  - At A (ν = 90° − ω), the companion passes in front of the RV primary, which is the deeper eclipse.
  - At B, the primary covers the companion.
- **Consistency:** J = 0.79 implies the companion is about 5600–5700 K. A dwarf of about 0.9 Msun and 0.9 Rsun at that temperature contributes about 11% of the TESS light, which fits the 9% partial B depth. It also fits the 13% A depth (k² ≈ 0.15 diluted by L2) and an SB1 at K1 = 30 km/s. One geometry explains all depths, durations and shapes.

## 6. Verdict: CONFIRMED
**Deciding numbers:**
- Three eclipses of two kinds, confirmed by independent pipelines and located on the target by pixel regression.
- The LD-fit e and ω agree with Gaia to within 0.2σ.
- The B−A phase agrees to 0.2σ.
- The period is 55.46045 d, Gaia's +1.3σ.

**Next predicted eclipses** (BTJD; ±2–3 min, from the period error, assuming the 30-cycle count):
- **A:** 4363.011, 4418.471, 4473.932, 4529.392
- **B:** 4377.727, 4433.188, 4488.648, 4544.108

**What would settle it further:**
- One more eclipse would pin the period without relying on the 30-cycle count.
- A spectrum could look for the companion's lines (an SB2 at about 5700 K).
- The ExoFOP CTOI check should be redone when the service is back.
