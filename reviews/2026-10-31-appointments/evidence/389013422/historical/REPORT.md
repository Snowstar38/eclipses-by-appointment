> Historical report: superseded by the current reconciliation at ../../../reports/389013422/REPORT.md. Its original bytes are preserved in the source archive; this public copy is sanitized.

# TIC 389013422 (TYC 9506-2715-1): adversarial check

Gaia DR3 5194904540995596544, SB1, P = 39.540 ± 0.033 d, e = 0.138 ± 0.038, ω = 103 ± 29°, K1 = 11.90 ± 0.77 km/s. G 11.00, Tmag 10.58, Teff 6091 K, R 1.053 R☉, M 1.14 M☉ (TIC), d 197 pc, dec −84.0°. Checked by Opus 5.5 for Fable 5.1, 2026-10-22 (chunk-3 wave 2). Saved from the checker's final message by Fable 5.1; the file tool refused REPORT.md. Scripts, outputs, figures and a `progress.md` mapping every number to its script are in this folder; downloads in `[local path omitted]

## Verdict: CONFIRMED (eclipsing binary; primary eclipses at Gaia's conjunction A). The secondary is not detected.

What decides it:
- **Seven primary eclipses** in seven sectors over 2254 d, all at Gaia conjunction A. The classifier listed five. Two more are in flagged data: s93 at 3842.071 (scattered-light flag) and s94 at 3881.613 (sector end).
- Six clean eclipses give a linear ephemeris with χ² = 6.1 for 4 degrees of freedom and every O−C within 1.1 min. **P = 39.542578 ± 0.000010 d**, which is 0.07σ from Gaia's P.
- **Depth 5.5–5.7%** with the same shape every time, confirmed in independent pixel data: SPOC 2-min s12 (5.45%), TESS-SPOC (5.3–5.5%), eleanor, TARS, and my own TESScut photometry.
- **On target.** The difference-image centroid is within 0.7″ of the target, and no Gaia source brighter than G 15 lies within 60″.
- **Physically consistent.** The depth and shape give k = 0.265. That matches the radius of the 0.23 M☉ companion that Gaia's mass function implies at i ≈ 89°.

## 1. Archives and web: what was queried and what came back
| Query | Result |
|---|---|
| `cats.py --r 60` (VSX, ASAS-SN, Prša+2022, IJspeert+2024, Kostov+2025 t2/t3/t4, SIMBAD) | VSX none; ASAS-SN none; SIMBAD has TYC 9506-2715-1 [SB*] at 0.0″ |
| VizieR 60″ cones (`arch3.py`): Prša, IJspeert, Kostov t2/t3/t4, ZTF, ATLAS, ASAS-SN II/366, WISE, ACVS, VSX, SB9, WDS, Justesen+2021 and others | 0 rows each. The J/A+A/674/A16 call returned a mis-parsed multi-table dump, so I used the direct Gaia TAP query below instead. |
| Gaia DR3 TAP: vari_summary, vari_eclipsing_binary, vari_classifier_result, vari_rotation_modulation, vari_long_period_variable | 0 rows each. phot_variable_flag is NOT_AVAILABLE. |
| Gaia DR3 gaia_source | RUWE 1.21, non_single_star 2, rv_amplitude_robust 22.3 km/s, rv_chisq_pvalue 0 |
| SB9, WDS (VizieR) | 0 rows |
| SIMBAD | IDs: TIC 389013422, TYC 9506-2715-1, 2MASS J09033388-8400457, Gaia DR1/2/3. Object type SB*. One reference: 2023A&A...674A..34G (Gaia DR3 NSS). |
| ExoFOP target page | HTTP 503 (maintenance page). Not retried. |
| NASA Exoplanet Archive TOI table | No row for this TIC, so it is not a TOI. CTOIs could not be checked while ExoFOP was down. |
| Web search on the TYC, TIC, Gaia and 2MASS names | No page mentions the star (the only hits, arXiv 2207.00505 and Wikipedia NGC 388, were unrelated objects). |

The star is not catalogued as an eclipsing binary or variable anywhere I could reach. Its only prior identification is the Gaia SB1 orbit.

## 2. Data and eclipse measurements
- QLP sectors: s11, s12, s13 (30 min), s38, s39 (10 min), s65, s66, s93, s94 (200 s).
- SPOC 2-min: s11, s12. TESS-SPOC: s11–13, 38, 39, 65, 66. TARS: all nine sectors. eleanor-lite: s11–13. TGLC: s11.
- TESScut also lists s67, but that cutout starts at CCD column 19, in the collateral pixels, and holds zero flux. **The target is off silicon in s67**, so there are no s67 data.

Primary (A) eclipses, from QLP SAP_FLUX with all cadences, 5-MAD clipping, and a trapezoid with a local quadratic baseline over ±0.6 d (`ecl_clip.py`):

| Sector | t0 (BTJD) | O−C (min) | Depth | T14 (h) | T12 (h) | Notes |
|---|---|---|---|---|---|---|
| s12 | 1627.6877 ± 0.0003 | +1.1 | 5.48% | 4.53 | 1.77 | In SPOC 2-min the whole eclipse is flagged 8192 (scattered light). The SPOC SAP fit gives O−C +0.6 min, 5.45%, T14 4.49 h, T12 1.74 h. |
| s13 | 1667.2289 ± 0.0002 | −0.9 | 5.48% | 4.48 | 1.70 | clean |
| s38 | 2339.4532 ± 0.0002 | −0.3 | 5.56% | 4.46 | 1.69 | clean |
| s39 | 2378.9960 ± 0.0002 | 0.0 | 5.69% | 4.44 | 1.70 | clean |
| s65 | 3090.7625 ± 0.0002 | +0.3 | 5.69% | 4.44 | 1.70 | Comes after the known 3089.8 pre-gap dip and is a separate event with the full eclipse shape. |
| s93 | 3842.0712 ± 0.0003 | −0.1 | 5.58% | 4.50 | 1.72 | Every in-eclipse cadence is flagged (bit 2^30, scattered-light spike). Shape and depth are unchanged, and the fit is stable for windows of ±0.25 to ±0.6 d. |
| s94 | 3881.613 ± ~0.003 | −1.3 | 4.4–5.2% | ~4.5 | | Sector end, fully flagged, steep ramp. Used as a timing check only, not in the ephemeris fit. |

**The trapezoid's ~1 h "flat" bottom is not totality.** A joint limb-darkened two-sphere fit to the six clean eclipses, with exposure-time smearing (`ebfit.py`, `ldmodel.py`), gives:
- k = 0.265 ± 0.005, b = 0.825 ± 0.008, chord speed v = 9.75 ± 0.06 R1/d.
- Because b > 1 − k, the companion's disc is never wholly inside the primary's, so there is no T23. The model T14 is 4.72 h.
- Across four limb-darkening pairs (`ldsens.py`): k 0.261–0.274, b 0.81–0.85, v 9.71–9.79.

**Background and centroids** (`bkgcen.py`, `spoc12.py`):
- QLP SAP_X/Y shifts during eclipse are 0.0003–0.005 px, with signs that differ from sector to sector.
- The SPOC 2-min s12 centroid shift is −0.0005 ± 0.0005 px: a null result.
- QLP SAP_BKG falls during several eclipses. A lower background would raise the SAP flux, not lower it, and pipelines with independent backgrounds show the same depth. This looks like QLP's background annulus picking up the star's own light.

**Blind dip census** (`census.py`, 2 h and 4.5 h boxes, every sector):
- In unflagged data there is nothing deeper than 2 ppt at S/N > 6 except the A eclipses. A few weak 3–4 ppt events sit at gap edges (s93 at 3836.5 and 3849.8).
- Events in flagged cadences are momentum-dump drops (s11–13, about every 3.1 d), sector-end scattered light (s66 3125, s94 3869) and a single bad cadence (s94 3862.53).
- Nothing else repeats.

## 3. Ephemerides and the B windows
**Primary (A)** (`ephem.py`):
- **T0 = BTJD 1627.68696 ± 0.00030** (epoch n = 0; 2497.62367 ± 0.00019 at the reference epoch n = 22).
- **P = 39.542578 ± 0.000010 d.**
- Against Gaia, ΔP = +0.0024 d, which is +0.07σ.
- Observed minus Gaia-predicted A time (`conjmc.py`, using this star's own corr_vec) is −0.79 to −0.64 d, or −0.68σ to −0.21σ.

**Secondary (B): not detected, so it has no ephemeris.**
- Gaia's B−A phase separation is 0.4818 ± 0.0402, so B falls 19.05 ± 1.59 d after each A.
- Unflagged QLP data cover every 0.005 bin of phase from 0.30 to 0.70.
- Six B windows were observed (`bepoch.py`). The table gives the largest 4.5 h box depth in each Gaia 1σ window:

| Epoch | Sector | BTJD window | Window covered | Max box depth |
|---|---|---|---|---|
| n = −1 | s11 | 1605.6–1608.8 | 47% | +0.38 ppt |
| n = 0 | s12 | 1645.2–1648.3 | 100% | +0.49 ppt |
| n = 18 | s38 | 2356.9–2360.1 | 100% | +0.36 ppt |
| n = 36 | s65 | 3068.7–3071.9 | 94% | +0.42 ppt |
| n = 37 | s66 | 3108.2–3111.4 | 91% | +0.55 ppt |
| n = 56 | s94 | 3859.5–3862.7 | 97% | +0.33 ppt |

  The scatter of box depths within each epoch is 0.17–0.35 ppt.
- B windows not observed: 1686.3 (after s13 ended), 2398.8 (after s39 ended), 3822.3 (before s93 began) and 3150 (s67, off silicon). Gaia's own absolute B windows fall on the same six observed epochs.
- **Combined over all epochs** (`bnull.py`, 369 trial phases, empirical S/N scatter 1.23):
  - **3σ upper limit on a secondary in the Gaia 1σ window: 0.46 ppt for a 4.5 h box, 0.66 ppt for a 2 h box.**
  - Anywhere in the Gaia 3σ window (phase 0.36–0.60) the limit is 0.72 ppt.
- **A hint I am not counting.** The strongest combined feature at any phase is at phase 0.535: 0.44 ± 0.07 ppt. That is 6.2σ formally and about 5σ against the empirical scatter.
  - It comes from four epochs: s11 +0.55 ppt (at an orbit edge, on a starspot slope), s12 +0.24, s65 +0.64 and s94 +0.33 ppt.
  - TESS-SPOC and SPOC 2-min reproduce it at +0.3 to +0.7 ppt.
  - No single epoch shows an eclipse shape by eye, and it is the same size as the 5–8 d starspot wiggles.

**e cos ω and e sin ω**
- **e cos ω:** TESS cannot measure it without a secondary. Gaia gives −0.028 ± 0.063. If the 0.535 hint were real it would mean about +0.055.
- **e sin ω from the primary's chord speed:** +0.18 using the TIC radius R1 = 1.053 and a/R1 = 51.6. This is very sensitive to R1, moving by about 0.11 per 0.1 R☉ (R1 = 0.95 gives +0.06).
- **e sin ω from the missing secondary:** keeping the secondary below about 0.5 ppt requires e sin ω ≳ 0.16–0.17, assuming a 3100–3250 K M dwarf.
- **Gaia:** e sin ω = 0.120 ± 0.043, about 1–1.4σ from both TESS constraints, so there is no real tension.
- The duration-ratio method needs a secondary duration, so it could not be used. No trapezoid flat was treated as totality.

## 4. Independence, pixels and neighbours
**Other pipelines** give the same times (within 2 min) and depths:

| Pipeline | Sectors | Depth |
|---|---|---|
| SPOC 2-min SAP | s12 | 5.45% |
| TESS-SPOC SAP | s13, 38, 39, 65 | 5.32–5.46% |
| TESS-SPOC PDCSAP | s13, 38, 39, 65 | 5.40–5.55% |
| eleanor-lite | s12, 13 | 5.49–5.57% |
| TARS | s12, 13, 38, 39, 65, 93 | 5.37–5.85% |
| My own 3×3 TESScut photometry | s65 | 5.31% |

QLP runs 2–4% (relative) deeper than TESS-SPOC, and its depth is steady across sectors. In s93, QLP's 5.58% agrees with TARS's 5.75%, so the known low-QLP-depth problem in recent sectors does not show up here.

**Difference images** (TESScut s65 and s39):
- The pixel losing the most flux is the target pixel in both sectors.
- The centroid of the lost flux is 0.7″ from the centroid of the star's light.
- Depth by aperture size (1×1 / 3×3 / 5×5): 5.8 / 5.6 / 5.5% in s65 and 5.3 / 5.4 / 5.4% in s39.
- 82% of the lost flux falls in the 3×3 around the target, against 77–78% of the light.

**Neighbours** (Gaia DR3): none brighter than G 15 within 60″. The dip each would need is the depth × 10^(0.4Δm):

| Neighbour | Separation | Dip it would need |
|---|---|---|
| G 16.92 (brightest within 60″) | 22.2″ | ≈ 1280% |
| G 14.69 | 70.2″ | 165% |
| G 14.98 | 76.7″ | 215% |

All of these are impossible, and every other source within 90″ is fainter than G 17.6.

## 5. Physics (`physics.py`)
- **Mass function** f(m) = 0.00671 M☉.
- **Companion mass** at i = 90°: 0.233 M☉ (0.216–0.250) for M1 = 1.14; 0.215 for M1 = 1.0 and 0.241 for M1 = 1.2.
- **Orbit:** a = 54.3 R☉ (0.2525 AU), a/R1 = 51.6. The fitted b gives i ≈ 89.0°, so sin i ≈ 1 and the companion is an **M dwarf of about 0.23 M☉**.
- **Radius:** k = 0.265 gives R2 = 0.279 R☉ for R1 = 1.053, about 10% larger than a typical 0.23 M☉ dwarf. R1 = 0.95 would give R2 = 0.25 and e sin ω = +0.06. The same unknown, R1, controls both.
- **Which star is in front:** at A (primary farthest from us) the M dwarf transits the G star, which is the observed 5.5% eclipse. At B the G star occults the M dwarf.
- **Durations:** a central (b = 0) eclipse would last 6.55 h at A and 8.34 h at B for e sin ω = 0.12 (7.34 h at both for e sin ω = 0). The observed 4.7 h at A fits b = 0.83.
- **Expected secondary:**
  - A 3250 K M dwarf has about 7% of the primary's surface brightness in the TESS band (blackbody). That makes it about 0.5% of the light, so a total occultation would be 4.9 ppt (3.8 ppt at 3100 K, 6.2 ppt at 3400 K).
  - At B the impact parameter is larger by a factor (1 + e sin ω)/(1 − e sin ω). The expected depth falls with e sin ω:

| e sin ω | Expected secondary depth | Duration at B |
|---|---|---|
| 0 | 4.3 ppt | |
| 0.125 | 1.6 ppt | |
| 0.15 | 1.0 ppt | 4.0 h |
| 0.175 | 0.49 ppt | 3.3 h |
| ≥ 0.22 | none (the stars miss) | |

  - The measured limit therefore needs e sin ω ≳ 0.16–0.17. That agrees with the chord-speed value and is about 1σ from Gaia.
  - **The missing secondary is what this geometry predicts, not a problem.** At that e sin ω the secondary would be a ~0.5 ppt, ~3 h grazing occultation, about the size of the phase-0.535 hint.
- **Overall:** one geometry fits everything: a G0 dwarf with a ~0.23 M☉ M dwarf on a 39.54 d orbit, e ≈ 0.14–0.2, seen at i ≈ 89°. Depth, shape, seven years of constant depth, the period and the conjunction timing all agree with it. No dilution or blend is needed.

## 6. Next predicted eclipses (BTJD; 2026-10-22 = BTJD 4335.5)
| Epoch | Primary A (±1σ) | Secondary B at Gaia phase 0.482 (±1.59 d) | Phase-0.535 hint |
|---|---|---|---|
| n = 69 | 4356.1248 ± 0.0005 | 4375.18 | 4377.28 |
| n = 70 | 4395.6674 ± 0.0005 | 4414.72 | 4416.82 |
| n = 71 | 4435.2100 ± 0.0005 | 4454.26 | 4456.37 |
| n = 72 | 4474.7526 ± 0.0006 | 4493.80 | 4495.91 |
| n = 73 | 4514.2951 ± 0.0006 | 4533.35 | 4535.45 |

In general, A = 1627.68696 + 39.542578 n.

## 7. What would settle it further
1. **Secondary:** photometry good to about 0.2 ppt at phases 0.44–0.56, from more TESS sectors at B or from CHEOPS. That would turn the 0.535 hint into a detection or a limit and give e cos ω directly. A firm null below about 0.2 ppt would push e sin ω above about 0.19.
2. **Primary star:** a spectroscopic R1 and Teff, or a radius from Gaia SED fitting. That pins a/R1, hence e sin ω from the chord speed, and tests whether R2 really is 0.28 rather than about 0.25 R☉.
3. **Orbit:** Gaia DR4 epoch RVs, or 3–4 ground-based RVs (the TESS ephemeris already fixes P and the A phase), to pin e and ω.
4. **CTOI check:** query ExoFOP again once it is back up.

Figures: `overview.png`, `zoom.png`, `ebfit.png`, `bwin.png`, `bnull.png`, `sec535.png`, `spoc12.png`, `diff_s65A.png`, `diff_s39A.png`, `phot_s65.png`, `phot_s67.png`.
