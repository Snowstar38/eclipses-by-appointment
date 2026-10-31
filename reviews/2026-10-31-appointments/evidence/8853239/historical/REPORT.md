> Historical report: superseded by the current reconciliation at ../../../reports/8853239/REPORT.md. Its original bytes are preserved in the source archive; this public copy is sanitized.

# TIC 8853239 (TYC 2494-40-1): adversarial check

Gaia DR3 SB1, P 24.6470 ± 0.0114 d, e 0.161 ± 0.028, ω 94.5 ± 21.7°, K1 21.28 km/s. G 11.45, BP−RP 0.83, parallax 2.913 mas (343 pc), RUWE 1.20, Teff 5738 K, logg 4.07; TIC R 1.576 R☉. Checked by an Opus checker for Fable 5.1, 2026-10-22 (chunk-3 wave 6, 19:37–19:41, under a 15-minute cap). Saved from the checker's final message by Fable 5.1; the file tool refused REPORT.md. Scripts and outputs are in this folder, every step in `progress.md`; downloads in `[local path omitted]

## Verdict: CONFIRMED (one eclipse; period from Gaia alone)

TIC 8853239 is a real eclipsing binary, and the eclipse is on the target star. It rests on one primary eclipse, measured by four independent sets of photometry, plus a pixel test. Because TESS saw only that one eclipse, TESS cannot give a period; the period comes from Gaia alone. The secondary eclipse is only tentative.

## 1. Archives and web: what was queried and what came back
- **ExoFOP** (`target.php?id=8853239&json`): HTTP 503, a maintenance page. CTOIs are **unchecked**.
- **NASA Exoplanet Archive TOI table** (tid=8853239): 0 rows.
- **Gaia DR3** (`gaia_q.py`, `arch2.py`):
  - Target: G 11.45, BP−RP 0.83, parallax 2.913 mas (343 pc), RUWE 1.20, Teff 5738 K, logg 4.07.
  - Radial velocities: rv_amplitude_robust 44.3 km/s, rv_chisq_pvalue 0.
  - Orbit solution (SB1): P 24.6470 ± 0.0114 d, e 0.161 ± 0.028, ω 94.5 ± 21.7°, K1 21.28 km/s.
  - No entry in vari_summary or vari_eclipsing_binary.
- **Catalogue sweeps** (`viz.py` cones at 60″, `arch2.py`, `cats.py`):
  - SB9 0, WDS 0, Prša+2022 0, IJspeert+2024 0, Kostov tables 2, 3 and 4 all 0, ASAS-SN none.
  - VSX has one row, and it is the neighbour Gaia DR3 697853849693309312 (G 14.45, 50″ away), typed RS. That is not the target and not prior art.
  - SIMBAD lists the target as TYC 2494-40-1 [SB*].
- **Web search** for "TYC 2494-40-1" or "TIC 8853239": no relevant hits.
- **MAST light curves** (`archives.py`): QLP s48, TARS s21 and s48, TESS-SPOC s48. There is no SPOC 2-min data. TESScut has s21 and s48.
- **Gaia-predicted conjunctions** (`conjmc.py`, using this star's own corr_vec):

  | | Sector 21 | Sector 48 |
  |---|---|---|
  | A | 1889.438 ± 0.927 | 2628.844 ± 1.193 |
  | B | 1876.931 ± 0.691 | 2616.332 ± 1.004 |

  The B−A phase is 0.4921 ± 0.037; Gaia's e cos ω is −0.012 ± 0.058 and e sin ω is +0.151 ± 0.031.
- **No prior art found.**

## 2. Eclipses (`ecl.py` → `ecl.txt`; `tc21.py` → `tc_s48.txt`)
Only sector 48 has data. In sector 21 the star falls off the edge of the CCD: the TESScut cutout is zero-filled from column 7 onward, with the target at pixel 7.7. That is also why the TARS s21 light curve is noise. **The s21 A window (1889.44) was never observed.**

The A eclipse in sector 48, from raw SAP flux with QUALITY = 0 and no trimming:

| Light curve | Mid-time (BTJD) | Depth | Total duration | Ingress | Flat bottom |
|---|---|---|---|---|---|
| QLP | 2629.07021 ± 0.6 min | 6.13% | 6.89 h | 1.41 h | 4.06 h |
| TESS-SPOC | 2629.06967 ± 0.6 min | 5.93% | 6.97 h | 1.48 h | 4.00 h |
| TARS | 2629.07093 | 6.05% | 6.93 h | — | — |
| Own TESScut photometry | 2629.06987 ± 0.7 min | 6.00% | 6.97 h | 1.49 h | 4.00 h |

- **Quality flags:** none of the cadences in the event are flagged.
- **Background:** the change in eclipse is −44 e/s against a scatter of 465 (QLP) and −47 against 83 (TESS-SPOC), so nothing there.
- **Centroid:** shifts by +0.007 px in QLP (3.9σ) and +0.001 px in TESS-SPOC (1.4σ). Both are small.
- **Blind census** (`look.py` → `census.txt`): nothing deeper than 1% in the unflagged data apart from A. The flagged runs at 2608.3–2608.8 and 2623.1–2624.5 are scattered light or zeroed cadences, not dips. Wiggles of 0.2–0.32% at 2613.5, 2616.1, 2620.1, 2628.0, 2630.0, 2631.5, 2633.1 and 2634.8 are the star's own low-level variability.
- **Classifier's "asteroid at 2617.5":** not examined.
- **B eclipse** (`bphys.py` → `bphys.txt`):
  - TESS-SPOC covers all of the ±3σ B window (2613.3–2619.3); QLP's unflagged data cover 4.4 of those 6 days.
  - TESS-SPOC finds a 7-hour box of 0.386 ± 0.014% at 2616.13 and a 9.5-hour box of 0.41% at 2617.15. QLP gives 0.34% at 2616.10.
  - But 2–3% of times outside the window give a box at least as deep, so this cannot be told apart from the variability. **The B eclipse is tentative.**
  - The 3σ upper limit is about 0.61% (TESS-SPOC).

## 3. Ephemeris and the Gaia comparison
- There is one A event, so TESS gives no period and no B-kind ephemeris.
- Observed A minus Gaia-predicted A = 2629.0699 − 2628.844 ± 1.193 = **+0.226 d, +0.19σ**.
- If the B at 2616.13 is real, the phase is 0.475 and e cos ω ≈ −0.039. Gaia's value is −0.012 ± 0.058, so they agree, but this is tentative.
- e sin ω cannot be measured from duration ratios without a measured B. Gaia predicts the B eclipse should last 1.38 times as long as A, about 9.6–11 h.

## 4. Independence tests
- **Other pipelines:** TESS-SPOC, TARS and my own TESScut photometry all reproduce the A eclipse to within 1.8 minutes and 0.2% in depth.
- **Pixel test** (`pixreg_trap.py` on the s48 TESScut cutout → `pixreg.txt`):
  - Depth in the target pixel is 5.98 ± 0.04%; the 3×3 aperture gives 5.98% and 5.78% for 5×5.
  - The flux-loss centroid sits 1.6″ from the light centroid and 3.6″ from the target, and the brightest pixel of lost flux is next to the target pixel.
- **Neighbour dilution:** the only Gaia neighbour within 60″ brighter than G 15 is the G 14.45 star at 50″ (Δm 3.0). To fake this eclipse it would need a 6.0% × 10^(0.4×3.0) ≈ 95% dip, and its own pixel shows only 2.3%, which is the target's light spilling over. The other neighbours (G 20.97 and G 20.87 within 60″, plus G 17.64 at 70″) cannot produce a 6% dip.
- **B-window coverage and upper limit:** given in section 2.

## 5. Physics (`bphys.py`)
- **Mass function:** f(M) = 0.0236 M☉. With M1 between 0.95 and 1.10, the companion at i = 90° is m2 = 0.34–0.37 M☉, and the separation a is 39.5 R☉.
- **Which star is in front:** at A (ν = 90° − ω, near periastron, separation 33.2 R☉) the companion passes in front of the G star. At B (separation 45.9 R☉) the G star passes in front of the companion.
- **A eclipse:** with R1 = 1.576 R☉, a central eclipse would last 7.95 h; the observed 6.95 h gives an impact parameter b² of about 0.07. The depth gives a radius ratio of 0.245, so R2 ≈ 0.39 R☉. That fits a dwarf of about 0.35 M☉.
- **Primary radius:** the duration implies R1 ≈ 1.41 R☉, against 1.576 R☉ in the TIC.
- **B eclipse:** predicted to be total, lasting about 11 h, with a depth of 0.4–0.7% from the dwarf's light (blackbody estimate). That agrees with the tentative 0.39% and with the 0.61% limit.
- **Overall:** depth, duration and the flat bottom all fit one geometry.
- **Caveat:** I did not fit a limb-darkened model. A transit with limb darkening should not be perfectly flat, so the trapezoid's "flat 4.0 h" is approximate.

## 6. Verdict
**CONFIRMED.** It is an on-target eclipse by a companion of about 0.35 M☉ in front of the G star, and it lands 0.19σ from Gaia's predicted A conjunction. The deciding numbers:
- Four independent sets of photometry agree on mid-time and depth.
- The pixel fit puts the flux loss within 1.6″ of the target's light.
- The only bright neighbour would need a 95% dip.
- Depth and duration fit Gaia's mass function and an M-dwarf companion.

Two weaknesses remain: there is only one event, so no TESS period, and the B eclipse is unconfirmed.

**Next predicted eclipses (BTJD; Gaia P with the observed A as T0):**
- A: 4354.36 ± 0.80, 4379.01 ± 0.81, 4403.65 ± 0.82
- B: 4341.84, 4366.49, 4391.14, each ± 1.2

**What would settle it further:** a second A eclipse in any future TESS sector, or from the ground at the times above. That would give the period and test Gaia's 24.647 d. A detection of a B eclipse lasting about 11 h at 0.4–0.6% depth would give e sin ω.

**Dropped for time:**
- Limb-darkened two-sphere fit
- Unrelated-star common-mode test of the B window (none of the known systematic times falls in s48)
- The classifier's asteroid at 2617.5
