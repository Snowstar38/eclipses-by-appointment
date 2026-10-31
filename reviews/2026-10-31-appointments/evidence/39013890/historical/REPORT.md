> Historical report: superseded by the current reconciliation at ../../../reports/39013890/REPORT.md. Its original bytes are preserved in the source archive; this public copy is sanitized.

# TIC 39013890 (TYC 2964-953-1, Gaia DR3 920642015314267008): adversarial check

Checker: Opus 5.5, 2026-10-22 (chunk-3 wave 2 for Fable 5.1). Saved from the checker's final message by Fable 5.1; the file tool refused REPORT.md.

## Verdict: CONFIRMED

This is a detached, eccentric eclipsing binary: a G dwarf with an early-M dwarf companion. I found seven eclipses (3 primary, 4 secondary). Both eclipse kinds fall on Gaia's two conjunctions. Three pipelines (QLP, TESS-SPOC, TARS) show the same events. The light loss sits on the target pixel. One two-sphere geometry, with physically sensible radii, reproduces both eclipses' depths and durations. The deciding numbers:
- **Period.** TESS P = 20.923529 ± 0.000003 d against Gaia's 20.92633 ± 0.00604 (−0.46σ).
- **Conjunction offsets.** Every primary falls −0.55σ from Gaia conjunction A and every secondary −0.63σ to −0.71σ from B. These offsets use this star's own corr_vec.
- **Secondary phase.** Measured 0.43166 ± 0.00003, against Gaia's 0.4344 ± 0.0129.
- **e cos ω.** Measured −0.1049 to −0.1058, against Gaia's −0.102 ± 0.020.
- **An independent RV check.** A single APOGEE visit in 2015 (73 cycles before the first TESS eclipse) measured RV −0.81 km/s. The TESS ephemeris plus Gaia's K and γ predict −1.1 to −1.5 ± 0.5 km/s at that epoch.

**Correction to the classifier.** s20 holds a **third primary eclipse at BTJD 1859.073** (15.7% deep). The classifier listed only secondaries in s20. The bottom cadences are flagged 4096 in QLP, but TESS-SPOC (unflagged) and TARS show the same eclipse. Their durations were also short: the primary is 4.9 h by trapezoid and 5.25 h in the model, not 4.1 h. The secondary is 6.7–7.3 h.

## 1. Archives and web
- **cats.py --r 60.** VSX returned 503 (service down); ASAS-SN none; SIMBAD has TYC 2964-953-1 as type SB*.
- **VizieR cones at 60"** (arch3.py, asu-tsv; this route worked while TAP was down). Zero rows in:
  - EB catalogues: Prša+2022, IJspeert+2024, Kostov+2025 t2/t3/t4, Justesen+2021, the Southworth OBA table.
  - Variable-star and binary catalogues: VSX, SB9, WDS, ZTF periodic, ATLAS, ASAS-SN, WISE, ASAS ACVS, KELT.
  - Mowlavi+2023 (Gaia DR3 EBs): only other sources, at 41.6"–52.2".
- **Gaia DR3.** vari_summary, vari_eclipsing_binary, vari_classifier and the rotation/LPV tables are all empty; phot_variable_flag is NOT_AVAILABLE.
- **ZTF.** The DR light-curve query returned 0 rows.
- **SIMBAD.** Other identifiers: 2MASS J07534610+4006015 and GSC 02964-00953. Its bibliography is surveys only:
  - Ting+2019 (LAMOST)
  - APOGEE DR16/DR17 (2020AJ160,120; 2022ApJS259,35)
  - 2022AJ163,152
  - Gaia DR3 (2023A&A674A34)

  No variability or EB paper.
- **Spectroscopic surveys** (arch4.py):
  - APOGEE DR17: one visit, RV −0.81 km/s at JD 2457339.942, Teff 5903 K, logg 4.28, [M/H] +0.08.
  - LAMOST LRS/MRS: RVs of −28.0, about +30 (sub-exposures 29–33), about +7 (6.8–7.8) and +34.8 km/s. I did not retrieve their epochs. The range fits Gaia's γ 5.9 ± K 27.2.
- **ExoFOP: UNCHECKED.** HTTP 503 from the script and from a direct fetch (Retry-After 3600). The VizieR TAP service also returned 503, which is why I used the asu-tsv cones above.
- **Web search** on "TYC 2964-953-1", "TIC 39013890" and "J07534610+4006015": nothing about this star.
- **MAST** (archives.txt): QLP, TARS and TESS-SPOC light curves for s20 (1800 s), s47 (600 s) and s60 (200 s). No SPOC 2-min data.
- **Prior art: none.** The star was not known to eclipse.
- **Gaia astrometry flags.** RUWE is 1.55 and ipd_frac_multi_peak is **69**, meaning double-peaked image windows in 69% of scans. That hints at an unresolved companion closer than about 1" (see the caveat under the physics).

## 2. Eclipse measurements (raw SAP_FLUX, no trimming)

Per-event mid-times and depths come from evt.py: the joint-model template is fitted with a free shift, a depth scale and a linear baseline, with prayer-bead errors. The trapezoid columns come from ecl.py.

| event | BTJD mid | ± | depth (QLP) | trapezoid T14 / T12 / flat | notes |
|---|---|---|---|---|---|
| P s20 E0 | 1859.07340 | 0.2 min | 15.7% | 4.94 h / 1.69 / 1.56 | 5 of 10 in-eclipse cadences flagged 4096; TESS-SPOC 1859.07342–53 |
| P s47 E35 | 2591.39704 | 0.15 min | 15.44% | 4.88 / 1.65 / 1.58 | q==0 |
| P s60 E52 | 2947.09688 | 0.15 min | 15.21% | 4.89 / 1.65 / 1.60 | no flags |
| S s20 E−1 | 1847.18245 | 2.5 min | 1.34% | 7.28 / 2.96 / 1.36 | 7 flagged (4096) |
| S s20 E0 | 1868.10487 | 1.7 min | 1.29% | (QLP fit fails: 64 of 92 flagged) | TESS-SPOC 1868.1053, 6.9–7.0 h |
| S s47 E35 | 2600.42832 | 2.0 min | 1.27% | 6.75 / 2.54 / 1.67 | q==0 (allq: 31 points clipped in a scattered-light stretch) |
| S s60 E52 | 2956.12943 | 1.9 min | 1.29% | 7.00 / 2.81 / 1.37 | ends about 0.2 d before a data gap |

Checks through each event:
- **Background.** Changes are below 0.9σ of the out-of-eclipse SAP_BKG scatter, in BKG's own units.
- **Centroids.** SAP_X/Y shifts are at most 2 mpx for the primaries. The s60 secondary shows −12.7 mpx, but that is the steep post-gap X drift (look.png). The pixel regression puts that event on target.
- **Missing event.** The s47 secondary at about 2579.5 falls before the data start (2579.81).
- **Blind census** (census.py, q==0): with the eclipses masked, nothing deeper than 0.15% in any sector (1-h scatter 0.33–0.35 ppt). Unmasked at 0.6%, it finds only these events.
- **The trapezoid "flat" is not totality.** In the LD model the primary is a full transit with a short near-flat bottom (about 0.3 h within 0.2% of the depth). The secondary is a partial occultation and has no true T23.

## 3. Ephemerides and orbit shape (ephem2.py)

| kind | P (d) | T0 (BTJD) | χ²/dof |
|---|---|---|---|
| Primary (at Gaia A) | 20.923529 ± 0.000003 | 1859.07343 ± 0.00012 | 1.4/1 |
| Secondary (at Gaia B) | 20.923537 ± 0.000030 | 1868.10513 ± 0.00096 | 0.55/2 |
| Joint (common P) | 20.923529 ± 0.000003 | P 1859.07343 ± 0.00010; S 1868.10531 ± 0.00069 | 2.0/4 |

- **O−C.** Primary O−C is within ±0.14 min; secondary within ±1.2 min.
- **Period vs Gaia.** −0.46σ.
- **Offsets from Gaia's conjunctions** (conjmc.py, full covariance from this star's corr_vec):

  | eclipse | at Gaia | offset |
  |---|---|---|
  | P s20 | A | −0.31 d (−0.57σ) |
  | P s47 | A | −0.41 d (−0.55σ) |
  | P s60 | A | −0.46 d (−0.54σ) |
  | S s20 | B | −0.36 / −0.37 d (−0.71σ) |
  | S s47 | B | −0.47 d (−0.65σ) |
  | S s60 | B | −0.51 d (−0.63σ) |

  The offsets grow with time because Gaia's period is slightly long.
- **e cos ω.** The secondary phase is 0.43166 ± 0.00003 (Gaia MC: 0.4344 ± 0.0129). Solving the Sterne relation exactly gives e cos ω = −0.1049 (for e sin ω = 0.22) to −0.1058 (for 0.18), ± 0.0001. Gaia: −0.102 ± 0.020 (0.2σ).
- **e sin ω** (ebfit3.py, own two-sphere limb-darkened model, supersampled, all 7 events jointly).
  - Free fit: e sin ω = 0.220 ± 0.004 (statistical), giving e = 0.244 and ω = 115.5°.
  - Fixed at Gaia's 0.18: Δχ² = +20 at reduced χ² 0.83.
  - With third light L3 = 0.2: the free fit returns e sin ω = 0.180.

  So e sin ω lies between 0.18 and 0.22 depending on third light and limb darkening. Gaia's 0.180 ± 0.021 (e 0.208 ± 0.020, ω 119.5 ± 5.8°) is at most 1.9σ from the L3 = 0 value.

## 4. Independence

**Second pipelines** (secondpipe.py). All 7 events appear in TESS-SPOC SAP and PDCSAP and in TARS.

| | TESS-SPOC (SAP / PDCSAP) | TARS |
|---|---|---|
| Primary times | agree with QLP within 0.1–0.8 min | agree within 0.1–0.2 min |
| Secondary times | within the errors | within the errors |
| Primary depth (trapezoid) | 14.4–14.5% | 13.8–14.7% |
| Secondary depth | 1.17–1.31% | 1.28–1.57% |
| Durations | same | same |

TESS-SPOC CROWDSAP is 0.991–0.994. QLP primary depths (14.9–15.4%) run about 5% (relative) deeper than SPOC; none of these sectors is on the QLP-low list. The depth is therefore pipeline-dependent at the 5% level, and the event itself is not.

**Pixels** (TESScut 15×15 for s20/s47/s60; pixreg.py fits each pixel as a quadratic plus the eclipse template).

| event | deficit centroid vs light centroid | target-pixel fractional depth | 3×3 aperture depth |
|---|---|---|---|
| s20 P | 0.4" | 14.70 ± 0.09% | 14.68% |
| s47 P | 0.5" | 14.58 ± 0.06% | 14.66% |
| s60 P | 0.6" | 14.78 ± 0.07% | 14.70% |
| s20 S | 1.7" | 1.33 ± 0.24% | 1.29% |
| s47 S | 1.0" | 1.24 ± 0.06% | 1.21% |
| s60 S | 2.5" | 1.11 ± 0.11% | 1.26% |

At the neighbours' pixels: the G 13.60 star (87.5") shows 0.1–0.4%. The G 15.42 star (73.9") shows 1–5%, which is the target's PSF wing. The plain median difference image (diffimg.py) agrees for P but is unreliable for s60 S, whose out-of-eclipse windows straddle a gap with pointing drift.

**Neighbour dilution** (Gaia DR3, gaia_q.txt). Required dip = depth × 10^(0.4 ΔG):

| neighbour | sep | needed for P (15%) | needed for S (1.3%) |
|---|---|---|---|
| G 18.72 | 22.7" | ~16 000% | ~1 400% |
| G 19.01 | 27.9" | ~21 000% | ~1 800% |
| G 17.86 (brightest within 60") | 52.5" | ~7 100% | ~620% |
| G 17.96 | 55.6" | ~7 800% | ~680% |
| G 15.42 (outside 60") | 73.9" | 770% | 66% (its pixel shows no S signal) |
| G 13.60 (outside 60") | 87.5" | 145% | 12% (its pixel: 0.19–0.35%) |

No neighbour can produce either eclipse.

## 5. Physics (phys.py)

**Masses.** Gaia SB1 mass function f(m) = 0.0409 ± 0.0024 M☉. With i = 88.8° (eclipse fit):

| M1 | m2 | a |
|---|---|---|
| 0.95 | 0.426 | 35.6 R☉ |
| **1.07 (TIC)** | **0.457** | **36.8 R☉** |
| 1.20 | 0.489 | 38.1 R☉ |

The companion's predicted K2 is about 64 km/s.

**Radii from the eclipse fit** (r1 = 0.0321, r2 = 0.0122, k = 0.380):

| e sin ω | R1 | R2 | ρ1 |
|---|---|---|---|
| free (0.22) | 1.18 R☉ | 0.45 R☉ | 0.65 ρ☉ |
| fixed 0.18 | 1.14 R☉ | 0.43 R☉ | 0.73 ρ☉ |

Independent checks on R1:
- From Gaia luminosity: M_G = 4.12 at 254 pc, L ≈ 1.67 L☉, so R ≈ 1.24 R☉ at 5900 K.
- From APOGEE logg 4.28 with M1 = 1.07: R ≈ 1.24 R☉.

TIC's 1.35 R☉ is high. R2 of 0.43–0.45 R☉ is what a 0.46 M☉ M dwarf should have.

**Companion's light.** The fitted surface-brightness ratio J = 0.10–0.11 in the TESS band corresponds to T2 ≈ 3500 K (blackbody ratio: 0.094 at 3400 K, 0.118 at 3550 K), as expected for m2 ≈ 0.46. L2/L1 (TESS) = 0.015, which makes the system effectively an SB1 in Gaia's spectra, consistent with its SB1 solution.

**Which star is in front where:**
- **At A** (ν = 90° − ω, near periastron, separation 0.77–0.81 a): the M dwarf transits the G star. That gives the 15% primary, a full transit at b = 0.49 R1 (1 − k = 0.62).
- **At B** (separation 1.17–1.21 a): the G star occults the M dwarf. That gives the 1.3% secondary, a partial occultation at b = 0.71–0.77 R1.

This is the brief's key question, and the answer is yes: one geometry fits both. Depth ratio, durations and shapes all follow from it.
- A 15% transit with k = 0.38 at b = 0.49 is what limb darkening gives.
- The secondary depth is about L2/(L1 + L2) times the occulted fraction.
- The duration ratio follows from the separations: model T14 is A 5.26 h and B 7.0–7.3 h, against observed 4.9–5.3 h and 6.7–7.3 h.
- The residuals show no structure. In-eclipse residual means per sector are within ±1 ppt.
- The 1.44× larger separation at B is why the secondary is longer yet only grazing-partial. That is consistent, not a tension.
- For comparison, Gaia's e and ω with b = 0 would give the maximum central durations, 5.9 h at A and 8.5 h at B. The observed values sit below those, as a non-zero impact parameter requires.

**Phase checks:**
- Periastron from the eclipses lands 0.35 d (e sin ω free) or 0.09 d (fixed 0.18) from Gaia's t_periastron, whose error is ±0.36 d.
- The APOGEE RV check, described in the verdict, ties the phase back to 2015.

**Caveat.** ipd_frac_multi_peak = 69 and RUWE = 1.55 suggest a possible companion within about 1". That would add third light. L3 = 0.2 moves e sin ω to Gaia's value but shrinks R1 to about 1.08 R☉, below the luminosity radius, so L3 ≈ 0 fits the radii better. Either way, it changes the derived radii and e sin ω by about 10%, and does not change the verdict.

## 6. Next predicted eclipses (BTJD, joint linear ephemeris)
- **Primary (15%, about 5.3 h):**
  - 4348.9734 ± 0.5 min (2026-11-04 ≈ 11:20 UTC)
  - 4369.8969
  - 4390.8205
  - General: 1859.07343 + 20.923529 E
- **Secondary (1.3%, about 7.0 h):**
  - 4337.0818 ± 1.1 min (2026-10-23 ≈ 13:58 UTC)
  - 4358.0053
  - 4378.9288
  - General: 1868.10531 + 20.923529 E

## What would settle it further
- **High-resolution imaging** (speckle or AO), to test the ipd_frac_multi_peak hint of a close companion and so pin down the third light. That would fix e sin ω and the radii.
- **SB2 spectroscopy**, best in the near-IR, where an M dwarf is relatively bright. K2 is about 64 km/s, and an SB2 solution would give model-independent masses: a well-detached G+M benchmark at P = 20.9 d. The APOGEE spectrum might already show the secondary.
- **Retry ExoFOP** once it is back up, and VSX via cats.py.
- **Future TESS sectors.** I did not check whether TESS will observe this star again. One more sector would confirm the 20.923529 d period to about 10⁻⁶ d.
- **Ground photometry** of the 2026-11-04 primary, if wanted, is easy: 15% deep on a V ≈ 11.5 star.

---

Files are in `[local path omitted] 5.1\made\appointments\vet39013890\`; downloads are in `[local path omitted] The useful plots are `look.png`, `ebfit3_allq_L0.png` and `pix_*.png`. The new scripts are `ebfit3.py`, `evt.py`, `ephem2.py`, `pixreg.py`, `phys.py`, `arch4.py` and `look.py`. Two fixes to copied scripts: `ecl.py` no longer crashes when there are no unflagged in-eclipse cadences, and `secondpipe.py` now reads TARS files, which have no quality column.

The web search found nothing about this star; the results it returned were all about other stars (arXiv 2310.12380, 2302.06985, 1405.1559, 1607.04207, 1206.5514; var.astro.cz TYC 2652-329-1; amp.wdrc.org TYC 3564-2971-1).
