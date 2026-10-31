> Historical report: superseded by the current reconciliation at ../../../reports/4808224/REPORT.md. Its original bytes are preserved in the source archive; this public copy is sanitized.

# TIC 4808224 (TYC 7165-816-1): adversarial check

Gaia DR3 5437063563176055552, SB1, P = 25.1533 ± 0.0300 d, e = 0.11 ± 0.07, K1 = 22.4 km/s. G ≈ 11.3, Teff 7308 K, R 2.13 R☉, M 1.65 M☉ (TIC). Checked by an Opus checker for Fable 5.1, 2026-10-22 (chunk-3 wave 3, 18:50–19:01). Saved from the checker's final message by Fable 5.1; the file tool refused REPORT.md. Scripts and outputs are in this folder, checkpoints in `progress.md`; the earlier stopped checker's archive scripts were rerun (`cats_rerun.txt`, `rerun\`); downloads in `[local path omitted]

## Verdict: CONFIRMED

This is a detached eclipsing binary, P = 25.08349 d, with the primary eclipse at Gaia conjunction **A** and a **secondary eclipse at phase 0.608**, which the classifier did not see. Both eclipses are on the target at the pixel level.

## 1. Archives: what was queried and what came back
- **cats.py, r = 60″:**
  - VSX: only Gaia DR3 5437060608240413568, 35″ away, G 14.47, type ROT. Nothing at the target.
  - ASAS-SN: none.
  - SIMBAD: TYC 7165-816-1, type SB* (GALAH, Gaia DR3 NSS refs). No eclipse literature.
  - Prša+2022, IJspeert+2024, Kostov+2025 t3/t4: 0 rows.
  - Kostov t2 (unvetted): two neighbours only, TIC 4808211 at 31″ and TIC 4808222 at 34″. Not the target.
- **Gaia DR3 (arch2.py, rerun):** vari_summary 0 rows, vari_eclipsing_binary 0 rows, all other vari_* tables 0 rows.
  - Target: RUWE 1.01, ipd_frac_multi_peak 0, Teff_gspphot 7034, logg 3.89, rv_amplitude_robust 61 km/s.
  - SB9 0 rows, WDS 0 rows.
- **arch3.py "Gaia DR3 EB (Mowlavi+2023) J/A+A/674/A16":** 515 rows within 60″ with RGB synthetic magnitudes. That is a synthetic-photometry table, so the script's label is wrong. It is not prior art.
- **ExoFOP:** HTTP 503 at about 18:53 (and in arch2). It was down, so CTOIs are unchecked. NASA Exoplanet Archive TOI table: no TOI for TIC 4808224.
- **MAST CAOM:**
  - QLP: s8, 9, 35, 62, 89, 99.
  - TESS-SPOC: s8, 9, 35.
  - TGLC: s8, 9.
  - GSFC-ELEANOR-LITE: s8, 9.
  - T16: s8, 9.
  - No SPOC 2-min data.
- **Web search** for "TYC 7165-816-1" / "TIC 4808224": nothing relevant ([arxiv 2510.27470](http[local path omitted]), [arxiv 1910.08706](http[local path omitted]) and others came back, none mentioning the star).
- **Conclusion:** no prior eclipse classification. The VSX ROT entry belongs to the neighbour, not the target.

## 2. Eclipses measured
Method (`ecl.py`): raw SAP_FLUX, all finite cadences, trapezoid plus a quadratic baseline over ±1 d. Errors come from a cyclic-residual bootstrap.

**Primary (A):**

| Sector | tc (BTJD) | ± | Depth | T14 (h) | T12 (h) | Flat (h) | Flagged cadences in eclipse |
|---|---|---|---|---|---|---|---|
| 008 | 1526.8246 | 0.0036 | 5.6 ± 0.6% | 6.6 ± 0.3 | 1.8 ± 0.6 | 3.0 | 1 (4128) |
| 009 | 1551.9143 | 0.0071 | 4.4 ± 0.8% | 7.4 ± 0.4 | 2.7 ± 0.5 | 2.1 | 0 |
| 035 | 2279.3376 | 0.0015 | 5.08 ± 0.14% | 7.71 ± 0.09 | 2.89 ± 0.05 | 1.9 | 11 (4, 132, 4096, 16512) |
| 062 | 3006.7564 | 0.0022 | 5.09 ± 0.15% | 7.73 ± 0.11 | 2.92 ± 0.07 | 1.9 | 6 (128, 2^30) |
| 089 | 3734.1746 | 0.0027 | 5.02 ± 0.18% | 7.84 ± 0.17 | 2.95 ± 0.09 | 1.9 | 0 |

- The shape is V-like: the ingress is long and the "flat" part is not totality (see section 5).
- **Background:** SAP_BKG in-minus-out is within 1σ of the out-of-eclipse scatter at all five events.
- **Systematics:** the s062 event sits at the known s062 ~3007 common-mode time. It is 5% deep and on the ephemeris to 1 minute, so it is not that systematic.
- **Centroids:** QLP centroids shift by 0.001–0.004 px in eclipse. That is the expected size for the target dimming with ~4% neighbour light 1.6 px away.
- **s099:** the predicted primary (4060.26) falls in the 4055.74–4063.02 data gap.
- **Blind dip census** (`census.py`, 0.15 and 0.32 d boxes, QUALITY == 0):
  - Nothing else deeper than 0.5% apart from the five primaries.
  - Single-box depth scatter is 0.16%, set by ~0.5% short-period pulsation (the star is a 7000 K F star).
- **Secondary (B), new** (`secsig.py`, `secfit.py`, `secwin2.png`):
  - At phase 0.608 all four covered epochs dip by at least 0.37% (0.15 d box).
  - Its epoch-averaged depth is the single highest of about 920 trial phases, 5.7σ above the phase-to-phase scatter, and no other phase reaches 0.8× of it.
  - Joint fit: **phase 0.60793 ± 0.00064, depth 0.51 ± 0.13%, T14 8.0 ± 1.7 h, T12 3.0 ± 1.0 h.**
  - Per-epoch times: 1567.1665, 2996.8823, 3724.3684, 4050.4303 (O−C under 1 h). Per-epoch depths range 0.3–0.9% because of pulsation contamination.
  - Two windows are unusable: s035 E29 (2269.5) is in flagged scattered light, and the s008 one (1542.08) falls after the sector ends.

## 3. Ephemeris and the Gaia comparison
Scripts: `ephem.py` and `avb.py`. The Gaia covariance is this star's own corr_vec (`conjmc.py` / `avb.py`); the w–Tp correlation is 0.995.

- **Primary ephemeris: T0 = 1526.8302 ± 0.0027, P = 25.083485 ± 0.000057 d.**
  - χ² = 3.7 for 3 degrees of freedom; O−C of −8.2, +0.8, +4.1, +0.8 and −3.3 min.
  - The cycle count is unambiguous, because s008 and s009 are consecutive cycles (a ±1-cycle alias would give 24.80 or 25.37 d).
- **Against Gaia's period:** Gaia P = 25.1533 ± 0.0300, so the difference is −0.0699 d = **−2.33σ**. This is mild tension. The eclipse period is definitive; the most likely explanation is a 2.3σ fluctuation or underestimated error in Gaia's ~41-cycle RV period.
- **A vs B at the Gaia epoch**, where Gaia's errors are smallest:
  - Eclipse minus A = **−1.27 d** (68% range −2.11 to −0.48; MC sd 1.6 d).
  - Eclipse minus B = **+10.6 d**.
  - No Monte Carlo draw puts B within 0.5 d of the eclipse. **The primary eclipse is at A**: the companion passes in front of the Gaia primary.
- **Secondary phase:** the B−A separation is 0.6079 observed vs Gaia's 0.534 nominal (MC 0.525 ± 0.052), i.e. +1.6σ.
- **e cos ω:** exact Kepler from the phase gives ≈ 0.17 (0.137–0.173 over all e sin ω at 3σ). Gaia's is 0.038 ± 0.081, so +1.6σ.
- **e sin ω:** from the duration ratio, B/A = 1.04 ± 0.22 gives **+0.02 ± 0.11**. This is a crude trapezoid estimate, not a limb-darkened fit; Gaia's is −0.061 ± 0.073 (+0.6σ).
- **e ≈ 0.17**, against Gaia's 0.11 ± 0.07. No real tension anywhere.

## 4. Independence tests
- **Other pipelines** (`second.py`):
  - TESS-SPOC SAP and PDCSAP: primaries at 1526.836, 1551.915 and 2279.338 (O−C ≤ 0.15 h, depth 4.1–5.0%). The s035 primary is unflagged in SPOC.
  - TESS-SPOC also shows the secondary at 1567.166 (0.86–0.99%).
  - TGLC s8/s9: primaries at 1526.810 and 1551.913; secondary at 1567.169 / 1567.166 (1.0–1.2%).
- **Pixel test** (`pix.py`, `pix_s089.png`): a per-pixel regression (trend plus eclipse template) on an 11×11 TESScut cutout from s089.

| | Peak S/N | Dip-amplitude centroid (px) | Target (px) | G 14.47 neighbour (px) |
|---|---|---|---|---|
| Primary | 141 | (5.70, 5.11) | (5.87, 5.10) | (7.32, 5.79) |
| Secondary | 10.8 | (5.72, 5.06) | (5.87, 5.10) | (7.32, 5.79) |

  Both eclipses sit on the target.
- **Dilution:** no Gaia star brighter than G 15 within 60″ could host the primary.

| Neighbour | Separation | Dip needed to make the primary | Dip needed to make the secondary |
|---|---|---|---|
| G 14.47 | 34″ | 121% | 12% |
| G 14.96 | 31″ | 190% | 19% |

  Everything else within 60″ is fainter than G 15.7. The secondary is phase-locked to the primary and centred on the target, so it is the same system.
- **Other conjunction:** both kinds are now detected, so no B-window upper limit was needed.

## 5. Physics (`physics.py`)
- **Mass function:** f(m) = 0.0286 ± 0.0065 M☉ (K1 22.4, e 0.11).
- **Companion mass:** m2(i = 90°) = 0.48 / 0.51 / 0.54 M☉ for M1 = 1.5 / 1.65 / 1.8 M☉ (TIC gives M1 1.65 M☉, R1 2.13 R☉, Teff 7308 K).
- **Orbit size:** a ≈ 46.6 R☉ (0.217 AU).
- **Durations and inclination:**
  - A central transit of R1 + R2 ≈ 2.63 R☉ would last about 10.5 h at A and 10.8 h at B.
  - The observed ~7.75 h means an impact parameter of about 0.83 R1 and i ≈ 87.7°, so the primary is near-grazing (b + k ≈ 1.06). That explains the V shape and the long ingress.
  - Same caveat as the e sin ω estimate: the trapezoid "flat" part is not totality.
- **Which star is in front:**
  - At A, a ~0.5 M☉, ~0.5 R☉ early-M dwarf transits the F primary: k² ≈ 5.5%, about 5% observed with limb darkening and a high impact parameter.
  - At B the M dwarf is occulted. A depth ratio of 0.101 ± 0.026 means T2 ≈ 3800 K in the TESS band. Its expected TESS light fraction is about 0.56%, against the 0.51% secondary depth observed.
  - Depths, durations, shapes, the mass function and the companion's light all fit one geometry.

## 6. Verdict and predictions
**CONFIRMED.** The deciding numbers:
- Five primaries at 5.1%, recovered by three pipelines.
- O−C under 8 min over 88 cycles.
- The primary falls at Gaia conjunction A (−1.3 d) and is excluded from B (+10.6 d).
- A secondary at phase 0.608 is significant at 5.7σ against all other phases and is on the target in pixels.
- It is consistent with a 0.5 M☉ M-dwarf companion.
- Gaia's P is 2.3σ off and its e cos ω 1.6σ off; neither is a real conflict.

**Next predicted eclipses (BTJD):**
- **Primary:** 4386.347, 4411.431, 4436.514, 4461.598, 4486.681, 4511.765, 4536.848, 4561.932, 4587.015, 4612.099, 4637.182, 4662.266, 4687.349 (±6–7 min).
- **Secondary:** 4401.596, 4426.680, 4451.763, 4476.847, 4501.930, 4527.014, 4552.097, 4577.181, 4602.264, 4627.348, 4652.431, 4677.515, 4702.598 (±0.4 h).

**What would settle it further:**
- A limb-darkened two-sphere fit of the 200 s primaries and the stacked secondary, to pin down i, k and e sin ω (the trapezoid values above are crude).
- A pulsation model removed before fitting the secondary, which would tighten its depth.
- ExoFOP CTOI check once the site is back up.
- A VSX submission as a new EA.

## Caveats
- ExoFOP was down, so CTOIs are unchecked.
- e sin ω and the "flat" durations come from trapezoids, which the brief warns against for near-grazing eclipses. They are quoted with wide errors and no tension is claimed from them.
- Only s089 was used for the pixel test.
- `physics.py` prints an approximate-formula line that uses π/4 where it should be π/2. The exact Kepler-grid result of 0.17 is the one quoted.
- Nothing was committed and no file outside the folder was edited.
