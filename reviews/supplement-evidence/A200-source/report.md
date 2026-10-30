# TIC 374560569: per-object vet (sb1-scale wave 6)

Opus subagent, 2026-10-21. Standard: `Fable 5.1\made\appointments\VET-BRIEF.md` + `pervet\BRIEF-ADAPT.md`. (Saved by the parent session; the file-write tool refused REPORT.md for the subagent.)
Star: TYC 3697-940-1 = Gaia DR3 505449450965010176. G 11.32, Tmag 10.87, Teff 6102 K, R 2.37 ± 0.11 R☉, M 1.15 M☉ (TIC), d 503 pc, contratio 0.081.
Gaia SB1: P 13.894558 ± 0.001888 d, e 0.017 ± 0.011, ω 31 ± 49°, K1 31.60 ± 0.48 km/s, RUWE 1.39.
Batch row: 25.3 ppt, P 13.89323 d, n = 3, diffimg offset 2.13″.

## Verdict: CONFIRMED

The 28 ppt primary eclipse is real, sits on the target, and belongs to the Gaia SB1 orbit. The worry was n = 3. It goes away for a reason the batch did not see: **a secondary eclipse at phase 0.4995 shows up on its own in all four secondary windows covered** (4.17 ± 0.31 ppt, S/N 14 folded, S/N 6.3–6.8 in each window). That makes 7 eclipse events, not 3. No single event owns the verdict or the period.

What decides it:
- **Timing.** The TESS primary, extrapolated back to the Gaia epoch, lands 0.37 h from Gaia conjunction A: +0.29σ, using this star's own corr_vec, with ω–T_p correlation +1.000. At the TESS epochs the offset is −0.64σ and −0.65σ. P_TESS − P_Gaia = −0.68σ. The secondary phase of 0.49948 ± 0.00031 matches Gaia's predicted B − A phase of 0.5070 ± 0.0070 (−1.1σ).
- **Localization.** Difference image fitted with a WCS-calibrated PSF. The flux deficit lies 0.6″ from the target in s058 (2 eclipses) and 0.4″ in s085 (1 eclipse), with a 1σ radius of 0.9″. A fit fixed on the target beats every neighbour by Δχ² > 1500. Deficit/target is 2.6%. The batch figures (2.13″ deficit to target, 6.42″ deficit to light) belong to the wave-4 class of centroiding artefacts.
- **Second pipeline.** Own TESScut aperture photometry recovers E0, E1 and E52 at 27.5–28.9 ppt. The times agree with QLP to 0–1.4 min.
- **Physics.** f(m) = 0.0454 M☉, so m2 = 0.50–0.57 M☉ for M1 = 1.15–1.45. The depth ratio gives a TESS surface-brightness ratio J = 0.133, which implies T_eff2 ≈ 3720 K (blackbody): an early-M dwarf of about 0.5 M☉, as the mass function requires. The joint limb-darkened fit allows R2 ≈ 0.46–0.50 R☉ (k 0.22–0.24, b 0.93–0.96), a main-sequence 0.5 M☉ star.

Confidence in the event count: 3 primaries in raw Q0 data and 4 secondaries. All seven come from only **two sectors** (s058, s085), which TESScut confirms are the only sectors that observed the star. Within that limit the solution is overdetermined: leaving out each event in turn moves nothing (below).

## Archives and web (step 1)
- `cats.py --r 60`: no VSX, ASAS-SN, Prša+2022, IJspeert+2024, Kostov+2025 t2/t3/t4 entries (the silent tables returned no rows and no errors). SIMBAD has TYC 3697-940-1 [SB*], whose only variability measure is the Gaia DR3 SB1 period of 13.894558 d. SIMBAD's parent is Cl Stock 2 with membership 0 (Cantat-Gaudin+2018), so it is a non-member: Stock 2 is at about 370–400 pc and the star at about 515 pc.
- Gaia DR3 vari_summary and vari_eclipsing_binary: no rows. SB9, WDS, J/AJ/160/111: none.
- ExoFOP returned HTTP 503 twice, so the TOI/CTOI check is **unverified**. The batch-wise review has no TOI here.
- Web search on TIC, TYC and Gaia ids: nothing about this star.
- MAST CAOM: only the QLP s058/s085 light curves, plus SPOC and TICA FFIs. There are no SPOC, TESS-SPOC, TGLC or eleanor light curves.
- **Prior art: none found.** It is a known Gaia SB1, not a known eclipser.

## Eclipse measurements (step 2): raw SAP_FLUX, QUALITY = 0, no trimming

The shared primary trapezoid is T14 5.57 h, T12 2.12 h. Point σ is 1.8 ppt per 200-s cadence. Red-noise β at T14 binning is 2.12.

| event | BTJD mid | ± (min) | depth (ppt) | notes |
|---|---|---|---|---|
| pri E0 s058 | 2892.25800 | 0.7 | 28.09 ± 0.30 | bkg +0.26 sd; y centroid −0.006 px |
| pri E1 s058 | 2906.15203 | 0.9 | 27.76 ± 0.33 | bkg +0.10 sd; y centroid −0.006 px |
| pri E52 s085 | 3614.70846 | 0.7 | 27.94 ± 0.31 | bkg −0.34 sd; y centroid −0.006 px |
| pri E53 s085 | (3628.602) | – | **unusable** | QUALITY 2048 throughout |
| sec s058 | 2885.3087 | 12 | 4.08 ± 0.62 | |
| sec s058 | 2899.1994 | 13 | 4.30 ± 0.65 | |
| sec s085 | 3621.6451 | 12 | 4.07 ± 0.61 | |
| sec s085 | 3635.5384 | 12 | 4.23 ± 0.63 | |

- Flagged-cadence mining: the only extra epoch is E53 (3628.60). QLP flags all of it with 2048 (scattered light). SAP scatter there is 1.25 (relative), and TESScut plane-background photometry gives 57 ppt point-to-point scatter, against 1.7 ppt at E52. It cannot be recovered and **is not counted**. A nominally negative core there (−44 to −83 ppt) is not evidence. No other primary or secondary epoch was missed.
- Background through each event is flat in its own units (sd). Every event falls outside the sector-systematic times: E52 at 3614.71 is 1.8 d before the s085 feature at 3616.5. No QUALITY-32 slide falls inside any eclipse.
- The y centroid shift of −0.006 px is identical in all three events. That is what an on-target 28 ppt dip looks like given about 8% contaminating light.
- Blind census of both sectors (box width T14/2, > 4 ppt or S/N > 6): it finds exactly the 3 primaries and the 4 secondaries and nothing else. Outside the Gaia window, the strongest control phase in the secondary scan reaches S/N 1.9.
- Depths: primary 27.9 ± 0.2 ppt (trapezoid maximum; box depth 25.3, matching the batch). Secondary 4.17 ± 0.31 ppt. Both are constant across events (secondary χ² 0.10/3).

## Ephemeris, O−C, jackknife (step 3)
- 3 primaries: **P = 13.893272 ± 0.000012 d**, T0 = 2892.25831 ± 0.00039 BTJD (corr −0.62), χ² 0.95/1. O−C is −0.4, +0.7 and −0.0 min. Gaia P differs by −0.68σ.
- 4 secondaries alone: P 13.893162 ± 0.000161, χ² 0.04/2. Their phase relative to the primary is **0.49948 ± 0.00031** (−10.5 ± 6.2 min), so **e cos ω = −0.0008 ± 0.0005**. Gaia gives +0.011 ± 0.011, a −1.1σ difference. Light-travel time is about 1 min, negligible.
- Jackknife over all 7 events (primaries and secondaries with a free secondary offset): joint P 13.893272 ± 0.000012, χ² 1.45/4. Leaving out E0 gives 13.893262, E1 gives 13.893277, any one secondary gives 13.893272. Leaving out **E52**, the only long-baseline primary, gives P 13.893197 ± 0.000158 from the s058 pair plus the 4 secondaries. That predicts E52 at 3614.7046, against 3614.7085 measured (about 1σ). The secondaries recover the s085 primary independently.
- Cycle count: the s058 pair alone gives P 13.89403 ± 0.00078, which predicts E52 to ±0.04 d. The 51- or 53-cycle aliases sit ±13.9 d away, so the count is unambiguous.
- e sin ω: the trapezoid duration ratio T14s/T14p is 1.013 (0.970–1.078), giving roughly +0.006 (−0.015 to +0.037). Both eclipses are partial (grazing), so a duration ratio is a soft constraint here. It agrees with Gaia's +0.006 ± 0.012. Per the wave-4 lesson, Gaia's small e is a soft prior. The timing (P, conjunction A at the Gaia epoch, e cos ω) is the attribution evidence, and it is clean.
- Gaia conjunctions (own corr_vec MC, ω–T_p corr +1.000):

| epoch | Gaia conj A | TESS primary | Δ |
|---|---|---|---|
| near BTJD 389 (Gaia) | 391.4538 ± 0.0538 | 391.4693 ± 0.0025 | +0.37 h, +0.29σ |
| near 2900 | 2906.3711 ± 0.343 | 2906.1516 | −0.64σ |
| near 3620 | 3614.9957 ± 0.439 | 3614.7085 | −0.65σ |

  Conjunction A (ν + ω = 90°, primary farthest from us) is the companion in front of the F star. That is the deep eclipse, as expected for an M-dwarf companion.

## Independence (step 4)
- Second pipeline (`phot.py`, own TESScut aperture photometry with r = 1.5 and 2.5 px and an annulus background): E0 28.35/27.48, E1 28.62/27.84, E52 28.82/28.85 ppt. Mid-times agree with QLP to within 0–1.4 min.
- Difference image (`locate.py`, TESScut s058/s085, PSF model with WCS calibrated on all Gaia G < 17 stars; calibration shift 0.8″ and 1.2″): the free single-PSF deficit is 0.6″ and 0.4″ from the target, 1σ radius 0.9″. Fixed-position fits: the target has χ² 822 (s058) and 88 (s085). The next best is G 16.04 at 26″, at Δχ² 8332 and 1523, and it would need a 31–33% dip. The light-centroid to catalogue mismatch is 1.6–2.2″ with the uncalibrated WCS, which is where the batch's 2.13″ / 6.42″ come from.
- Neighbour dilution table, as the depth each neighbour would need (25.3 ppt × 10^(0.4Δm)):

| neighbour | sep | needs |
|---|---|---|
| G 13.48 | 53.6″ | 185 ppt |
| G 14.11 | 81″ | 330 ppt |
| G 14.21 | 68″ | 360 ppt |
| G 14.99 | 64″ | 740 ppt |
| G 15.96 | 38″ | 1.8 (impossible) |
| G 16.04 | 26″ | 1.9 (impossible) |

  The three brightest are excluded by the PSF localization (Δχ² > 1500, and the deficit is within 0.6″ of the target). A blend inside 1″ is not excluded by imaging, but it would have to copy the Gaia SB1 period and conjunction phase to 0.3σ. Not credible.

## Physics (step 5)
- f(m) = 0.0454 M☉. For M1 = 1.15, 1.30, 1.45 M☉, m2(i ≈ 86°) = 0.498, 0.535, 0.571 M☉ and a = 28.7, 29.8, 30.8 R☉.
- Joint limb-darkened two-sphere fit (`physics.py`, `kprof.py`), circular orbit, quadratic LD (0.32, 0.22 for the primary; 0.35, 0.30 for the companion). a/R1 = 14.0–14.5, robust. i ≈ 85.6–86°. Both eclipses are partial (b > 1 − k). The usual grazing k–b degeneracy leaves χ² flat for k 0.20–0.38. The best coarse point is k 0.24, b 0.96, giving R2 ≈ 0.50 R☉ for M1 1.3, which suits a 0.5 M☉ dwarf. k ≤ 0.16 is excluded. Third light of 0.08 (TIC contratio) changes almost nothing (a/R1 14.3, J 0.132).
- Surface-brightness ratio J = 0.133, so T_eff2 ≈ 3720 K. L2/L1 (TESS band) ≈ 0.015. A 0.50–0.57 M☉ M dwarf fits mass, temperature and radius together. Its light is too small to matter for Gaia's SB1 classification.
- Mild tension: a/R1 ≈ 14.1 implies R1 = 2.05–2.20 R☉ (ρ1 ≈ 0.19 ρ☉), against TIC R 2.37 ± 0.11 (ρ 0.086). That is about 1.5–2.5σ depending on M1 and LD. It is not decisive in a grazing, LD-sensitive fit, and it does not touch attribution. Spectroscopic R1 or log g would settle it.
- Predicted central T14 for TIC R1 would be 11–11.6 h. The observed 5.6 h is consistent with the high impact parameter.

## Row fixes
- **P** = 13.893272 ± 0.000012 d (batch 13.89323). T0 = 2892.25831 ± 0.00039 BTJD (batch 2892.2614 was 4.5 min late).
- **Depth**: primary 27.9 ± 0.2 ppt (trapezoid maximum; the box depth of 25.3 ppt is a box statistic, not a fix). **Secondary 4.17 ± 0.31 ppt at phase 0.49948 ± 0.00031**, new.
- **Event count**: 3 → **7** (3 primaries + 4 secondaries). E53 (3628.60) was observed but is unusable (scattered light).
- **dphi**: primary −0.014 phase from Gaia conj A at the TESS epoch (−0.64σ). The well-measured comparison is the Gaia epoch: +0.0011 phase, +0.29σ. Conj B at +0.477 in the batch convention; the measured secondary is at 0.4995 against Gaia 0.507 ± 0.007.
- **Diffimg offset**: 2.13″ → **0.4–0.6″ ± 0.9″** after WCS calibration (artefact class).

## Next predicted eclipses (BTJD)

| E | primary | ± (min) | secondary | ± (min) |
|---|---|---|---|---|
| 105 | 4351.0519 | 1.6 | 4357.9913 | 6.4 |
| 106 | 4364.9452 | 1.6 | 4371.8845 | 6.4 |
| 107 | 4378.8384 | 1.6 | 4385.7778 | 6.4 |
| 108 | 4392.7317 | 1.6 | 4399.6711 | 6.4 |
| 109 | 4406.6250 | 1.6 | 4413.5643 | 6.4 |
| 110 | 4420.5183 | 1.7 | 4427.4576 | 6.4 |

## What would settle it further
1. One more TESS sector or a ground-based primary. At V 11.4 a 28 ppt, 5.6 h eclipse is easy.
2. A spectroscopic log g or R1, to resolve the R1 2.1 vs 2.37 tension.
3. An ExoFOP TOI/CTOI re-check when the site is back (503 tonight).
4. RVs or a double-lined spectrum in the red, to detect the M dwarf (expected K2 ≈ 70 km/s).

## Files (all in this folder)
- gaiatap.py → gaia.json, gaiatap-out.txt
- cats-out.txt, morecats.py → morecats-out.txt, mastlc.py → mastlc-out.txt
- look.py
- vet.py → vet-out.txt, vet-results.json, events.png
- locate.py → locate-out.txt, locate_s058/s085.png
- phot.py → phot-out.txt, phot.png
- e53.py → e53-out.txt, e53.png
- conj.py → conj-out.txt, ephem.json
- sec.py → sec-out.txt, sec.png
- sec2.py → sec2-out.txt, sec2.json, sec2.png
- physics.py → physics-out.txt, physics.json, physics.png
- kprof.py → kprof-out.txt
- next.py → next-out.txt
- TESScut cubes: `C:\Home\sky\data\qlp-sb-p20-60\vet374560569\`
