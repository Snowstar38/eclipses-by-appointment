> Historical report: superseded by the current reconciliation at ../../../reports/255077215/REPORT.md. Its original bytes are preserved in the source archive; this public copy is sanitized.

# TIC 255077215 (HD 327543): adversarial check

Gaia DR3 SB1, P 26.2703 ± 0.0640 d, e 0.341 ± 0.143, ω 191.5 ± 24.6°, K1 27.28 ± 3.77 km/s. G 11.09, BP−RP 0.75, parallax 1.78 mas (about 560 pc), RUWE 1.08, Teff ~7400 K, R 2.62 R☉ (TIC). Checked by an Opus checker for Fable 5.1, 2026-10-22 (chunk-3 wave 4, 19:11–19:18). Saved from the checker's final message by Fable 5.1; the file tool refused REPORT.md. Scripts and outputs are in this folder, step-by-step numbers in `progress.md`; cutouts and second-pipeline light curves in `[local path omitted]

## Verdict: CONFIRMED

The primary eclipse is solid. The secondary at phase 0.303 is real, and it is not the s065 common-mode dip: it shows unflagged in s39 in two pipelines, unflagged in TESS-SPOC s12, and on the target in a pixel-level fit. Gaia's own orbit predicts a separation of 0.29–0.31 between the two eclipses. One anomaly is unresolved: the s65 secondary arrives 31–42 min late.

## 1. Archives
- **Gaia DR3** (`gaia_q.py`, `arch2.py`):
  - G 11.09, BP−RP 0.75, parallax 1.78 mas (about 560 pc), RUWE 1.08.
  - The orbit (NSS) is a single-lined spectroscopic binary: P 26.2703 ± 0.0640 d, e 0.341 ± 0.143, ω 191.5 ± 24.6°, t_periastron at BTJD 381.82 ± 1.66, K1 27.28 ± 3.77 km/s.
  - `vari_summary` and `vari_eclipsing_binary` both return 0 rows.
- **VizieR TAP:** VSX, SB9 and WDS return 0 rows.
- **VizieR cone sweep** (`viz.py`, 60″):
  - 0 rows from VSX, Prša+2022, IJspeert+2024, Kostov tables 3 and 4, ASAS-SN II/366, SB9, WDS, ATLAS, Gaia vclassre and ASAS ACVS.
  - Kostov table 2 (the unvetted machine-learning list) contains only the neighbour TIC 255077217 (T 13.19, 29.8″ away). That is most likely our eclipse leaking into its aperture; it is not prior art.
  - The 441 rows labelled "Mowlavi" come from the synthetic-photometry table, as the brief warns, so they are not prior art either.
- **`cats.py`:** no VSX or ASAS-SN entry. SIMBAD lists HD 327543 as `[SB*]` (spectroscopic binary), not as an eclipsing binary.
- **ExoFOP** returned HTTP 503 (both the script and a direct curl), so **CTOIs are unchecked**. The NASA Exoplanet Archive TOI table has 0 rows for this TIC.
- **Web search** for "HD 327543" eclipsing binary found nothing about this star.
- **MAST** (`archives.py`) has QLP s12/39/65/103, TESS-SPOC s12/s39 and eleanor-lite s12. There is no SPOC 2-min or TARS product.

## 2. Eclipses
Measured with trapezoid fits on raw SAP flux (`ecl.py` → `ecl.txt`, `ecl_fits.png`).

**Primary (A):** flat-bottomed, T14 12.7–12.9 h, ingress 2.5–2.7 h, flat part 7.5–7.9 h.

| Sector | Mid-time (BTJD) | Pipelines / notes |
|---|---|---|
| s12 | 1637.3433 ± 2.5 min | TESS-SPOC, QLP, eleanor agree within 4 min; 30-min cadence, next to a gap |
| s39 | 2372.6850 ± 1 min | QLP and TESS-SPOC agree to 0.1 min |
| s65 | 3081.7607 ± 1.5 min | QLP; all cadences carry flag bits common to the whole sector |
| s103 | 4158.5019 ± 1.5 min | QLP, unflagged |

Depth is 5.6% in QLP s39/s65, 4.7% in TESS-SPOC and QLP s103, and 5.0% in eleanor. The differences are aperture effects and are constant within each pipeline.

**Secondary (B):** flat-bottomed, T14 9.6–10.5 h, ingress 1.7–2.1 h, flat part about 6 h.

| Sector | Mid-time (BTJD) | Depth | Notes |
|---|---|---|---|
| s12 | 1645.3026 ± 6 min | 0.39–0.48% | TESS-SPOC unflagged, eleanor 0.40–0.44%; QLP flagged |
| s39 | 2380.6383 ± 4 min | 0.71–0.90% | QLP and TESS-SPOC |
| s65 | 3089.737–3089.745 | 0.63–0.81% | QLP |
| s103 | — | — | unusable: scattered-light ramps, background +9.7e3 (sd 1.7e4) |

**Common mode** (`commonmode.py`, `cmfix.py`, `cm_panel.png`):
- s39 at 2380.64: the target dips 8426 ppm. The other 471 sector stars have median +379 ppm (sd 521), and the 16 stars on the same CCD +723 ppm (sd 801).
- s65 at 3089.745: the target dips 6239 ppm against a sector median of +1222 ppm (sd 783). The common-mode sag peaks at only −0.15%, and dividing it out leaves a 0.77% dip with sharp ingress and egress that the stack of other stars does not have.

**Background and centroids:** no excursion at any unflagged event; centroid shifts are ≤0.009 px.

**Blind dip census** (`census.py`): in s39 and s65 the B dip is the deepest feature apart from the primary; everything else is ≤0.44%.

**Caveat on the secondary depth:** it spreads from 0.4% (s12) to 0.9% (s39), while the primary stays constant within each pipeline. The star has 0.2–0.4% slow variability, so this is probably a baseline effect, but it is not resolved.

## 3. Ephemeris and the Gaia comparison
From `ephem.py` and `conjmc.py`, which uses this star's own Gaia covariance (corr_vec).

- **Primary:** T0 1637.34736 ± 1.3 min, P 26.262038 ± 0.000016 d. O−C is −5.8, +0.8, +1.8 and −1.6 min.
- **Joint fit, both eclipse kinds:** P 26.262040 ± 0.000016 d, T0A 1637.34726, T0B 1645.30306 ± 3.3 min.
  - s12 and s39 secondaries: O−C of −0.7 and −2.7 min.
  - **s65 secondary: O−C +42 min** (+31 min after dividing out the common mode), against formal errors of 4–7 min. The primary shows no such shift. This is unexplained: the common mode alone moves the time by only about 5 min. It could be the star's variability or the residual systematic; apsidal motion would need Δ(e cos ω) of about 0.002.
- **Against Gaia:**
  - P differs by −0.008 d, which is −0.13σ.
  - Gaia's predicted primary conjunctions are off by −0.75 to −1.59 d (−0.16 to −0.19σ); the secondary conjunctions by −0.79 to −1.29 d (−0.23 to −0.37σ).
- **Geometry from timing:** the phase separation is 0.30294 ± 0.00009. Gaia's Monte Carlo gives 0.305 ± 0.083 (0.291 at the nominal values).
  - First-order e cos ω is −0.3095.
  - An exact Kepler solve with the duration ratio gives e cos ω −0.312, e sin ω −0.131, e 0.338, ω 202.8°.
- **Limb-darkened two-sphere fit** (`ebfit3.py`, QLP s39+s65, all cadences):
  - e cos ω −0.3113 ± 0.0004, e sin ω −0.137 ± 0.009, so e 0.340 and ω 203.8°.
  - i 89.71°, r1 0.0501, r2 0.0113 (k 0.226), surface-brightness ratio J 0.128, impact parameters 0.10 (A) and 0.08 (B). Neither eclipse is grazing; reduced χ² is 1.14.
  - Against Gaia: e is 0.0σ off, ω +0.5σ, e sin ω 0.6σ (Gaia's −0.05 ± 0.14).

## 4. Independence
- **Other pipelines:** the primary appears in TESS-SPOC s12/s39 and eleanor s12; the secondary in TESS-SPOC s12 (unflagged) and s39, and in eleanor s12.
- **Per-pixel regression of the s39 TESScut cutout** (`pixreg.py` → `pixreg.txt`, `pix_s39A.png`, `pix_s39B.png`):
  - Primary: deficit centroid 4.9″ from the target, 1.9″ from the light centroid; target pixel 5.21 ± 0.04%.
  - Secondary: deficit centroid 3.0″ from the target; target pixel 0.87 ± 0.11% (about 10σ). The strongest signal outside the central 3×3 pixels is 5.4σ, against 10.4σ inside.
- **Dilution table** (fraction each neighbour would need to dim):

| Neighbour | Separation | Primary (5.6%) needs | Secondary (0.8%) needs |
|---|---|---|---|
| G 14.90 | 18″ | 187% | 27% |
| G 14.49 | 30″ | 129% | 18% |
| G 15.85 | 35″ | 455% | 65% |
| G 15.35 | 56″ | 284% | 41% |

No neighbour can produce the primary. A neighbour could in principle produce the secondary, but the pixel centroid rules it out (the neighbours sit 0.9 px and 1.5 px away), and so does the secondary's timing at Gaia's own phase.

## 5. Physics
- **Mass function:** 0.0459 Msun.
- **Companion mass at i = 90°:** 0.58, 0.63 and 0.67 Msun for M1 = 1.5, 1.7 and 1.9 Msun. With i at 89.7°, these are effectively the true masses.
- **Separation:** a = 47.5–50.9 Rsun.
- **Radii:** R1 = 2.4–2.55 Rsun (TIC gives 2.62); R2 = 0.54–0.58 Rsun, right for a 0.6 Msun dwarf.
- **Temperature:** J 0.128 implies T2 ≈ 4100 K against T1 7400 K (a Planck estimate at 0.8 µm gives 0.116 at 4000 K), consistent with a K7–M0 dwarf.
- **Which star is in front:**
  - Primary eclipse (true anomaly ν = 90° − ω) is the companion transiting the 7400 K star: model depth 5.9%, T14 13.4 h.
  - Secondary eclipse is a total occultation of the companion: model depth 0.62%, T14 10.2 h, 6.45 h flat.

Depths, durations, shapes, companion light and Gaia's e and ω all fit one geometry.

## 6. Next eclipses and what would settle the rest
**Next predicted eclipses (BTJD, joint ephemeris):**
- **Primary (A):** 4421.1235, 4447.3855, 4473.6476, 4499.9096, 4526.1717 (each ± 1.6 min).
- **Secondary (B):** 4402.8173, 4429.0793, 4455.3414, 4481.6034, 4507.8654 (each ± 3.8 min).

**What would settle it further:**
- A clean, unflagged secondary in a future sector, to decide whether the s65 +31–42 min offset is real and to pin down the depth spread.
- Radial velocities of the secondary star (SB2), which would give the masses.
- Checking CTOIs on ExoFOP once it is back up.
