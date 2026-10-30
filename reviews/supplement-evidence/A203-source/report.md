# TIC 315849332: per-object vet (sb1-scale, G 11-11.5 subsample)

Opus subagent, sb1-scale pervet wave 6, 2026-10-21. (Saved by the parent session; the file-write tool refused REPORT.md for the subagent.)

**Verdict: CONFIRMED.** This is a grazing, double-eclipsing binary on the target, and it is the Gaia SB1. Gaia's orbit predicts both conjunctions, and both eclipses fall on them.

Batch row: 27.5 ppt, P 5.49211 d, n = 20, diffimg offset 3.13″.
Star: TYC 8972-1194-1 = Gaia DR3 5336005937706167808. G 11.18, Tmag 10.68, Teff 5499 K, R 1.86 R☉, logg 3.88 (a subgiant). It sits at b = +0.7°, and the TIC contamination ratio is 1.10.

## Deciding numbers
- **Primary eclipses.** 21 primaries, all individually detected at S/N 14–115. The batch said 20; the extra one is E5, s011 1600.363. All six QLP sectors (s010/011/037/064/099/100) have them. None falls on a listed sector-wide systematic time. Odd and even depths agree (29.12 vs 29.24 ppt). The in−out background is −0.6 ppt-equivalent (234 e⁻/s would be needed to fake the eclipse). Centroid shifts are about 1 mpix.
- **Secondary eclipse.** It is found at the ephemeris, not at a free-scan peak. The fixed-shape control at phase 0.5 gives +6.8 ppt with 24/24 events at S/N > 3. All other control phases are within ±0.4 ppt. Individual secondaries show up as census peaks at S/N 6–26. The fold gives 7.6 ± 0.16 ppt at phase 0.50020 ± 0.00019.
- **Ephemeris (timing.py, raw SAP).**
  - Primary: P = 5.4921244 ± 0.0000015 d, T0 = 2753.70951 ± 0.00034 BTJD; O−C rms 2.3 min.
  - Secondary: P = 5.4921159 ± 0.0000048 d (−0.74 ± 0.43 s per cycle relative to the primary, not significant).
  - e cos ω = +0.0003 ± 0.0003.
- **Gaia attribution (MC 20k draws with this star's own corr_vec).**
  - Gaia P = 5.492272 ± 0.000409 d, which is Δ −0.36σ from TESS.
  - At the Gaia epoch: conjunction A vs the TESS primary is +0.80 h (+0.9σ); conjunction B vs the TESS secondary is +0.45 h (+0.6σ).
  - In TESS sectors, conjunction A matches the primary to between −0.01 and −0.29σ in every sector.
  - Gaia's predicted phase(B) − phase(A) is 0.5036 ± 0.011; measured 0.5002. Gaia e cos ω is +0.006 ± 0.018 (−0.3σ from the TESS value).
- **Independence: both eclipses appear in every other pipeline.**

  | Pipeline | Sectors | Primary (ppt) | Secondary (ppt) |
  |---|---|---|---|
  | TARS | s10/11/37/64 | 26.7–28.3 | 6.5–7.4 |
  | TESS-SPOC SAP | s10/11/37 | 20.5–22.6 | 5.2–5.4 |
  | TESS-SPOC PDCSAP (CROWDSAP 0.53–0.62) | s10/11/37 | 36.9–40.2 | 9.3–9.7 |
  | TGLC PSF photometry at the Gaia position | s10/11 | 32.1–34.2 | 7.5–8.6 |

  The dilution-free secondary/primary depth ratio is 0.23–0.26 in every pipeline and sector. Sector-to-sector depth changes in QLP (s010 30.9 → s064 33.6 → s100 27.2 ppt, χ² 424/20) are aperture dilution in a crowded field.
- **Neighbours (neighbours-out.txt).** The only neighbour bright enough to matter is G 11.80 (BP−RP 2.48, T ≈ 10.72) at 41″, which would need a 3.0% dip. The 66.7″ and 85″ stars at G 12.2–12.5 would need 6.2%. Every other star within 30″ would need ≥ 17.9%, mostly > 100%. The VSX EA star at 27″ (P 0.915 d) is G 16.63 and would need > 100%.
- **Localization.**
  - Batch s064 diffimg: deficit−target 3.13″, deficit−light 5.17″, peak_on_target true.
  - Own locate.py on the TESS-SPOC TPFs:
    - s010: the target is the best fixed-position source by Δχ² 3254. It implies a 5.8% dip of the target model, which is crowding-diluted.
    - s011: the WCS calibration failed. The calibration shift was 10.8″ and the target model flux only 138 e⁻/s, so this sector is not usable.
    - s037: the best fixed position is the G 13.39 star at 11.7″, ahead of the target by Δχ² 388. That star would need a 157% dip, which is impossible.
  - The 41″ star (2 px away, inside the fit radius) is not in the top six positions in any sector.
  - Wave-4/5 lesson: the PSF-model WCS shifts are 6–11″ and unstable (reduced χ² ≈ 20, 71 model stars in an 11×11 stamp). Moment light−target offsets (4.9–7.8″) are as large as deficit−target offsets (4.6–8.3″). So the few-arcsecond offsets are the calibration/crowding artefact, not a displaced source.
  - Taken together: TGLC's PSF photometry at the Gaia position recovers the full depth, no catalogued neighbour can make the dip except at > 100% or at 2 px, and the Gaia orbit times both conjunctions. The signal is on target.

## Physics
- Mass function f(m) = 0.0735 M☉. That gives m2 = 0.557 M☉ for M1 = 0.96 (TIC) and 0.618 M☉ for M1 = 1.15, with i ≈ 82.5°.
- Separation a = 15.05 R☉ = 8.09 R1.
- A 0.56 M☉ dwarf (R2 ≈ 0.56, k ≈ 0.30) would make a central transit of about 100 ppt. The observed eclipse is grazing, with b_A ≈ 1.04–1.09 R1. The predicted grazing T14 is 3.85–4.3 h against a measured 3.70–3.78 h. The trapezoid flat (0.76 h) is not totality.
- Conjunction A has the companion in front, so it is the deeper eclipse of the G subgiant. Conjunction B is the occultation of the companion.
- The depth ratio of 0.258, in a limb-darkened two-sphere model (twosphere.py), gives J(TESS) ≈ 0.25, so T2 ≈ 3900–3930 K. That is a K7/M0 dwarf of about 0.55–0.6 M☉, matching the mass function.
- physics.py's built-in main-sequence relation gives T2 4300 K and overpredicts the secondary (13 ppt at e sin ω = 0). That relation runs too hot; it is not a tension in the data.
- e sin ω from the two-sphere duration solve is +0.007 (1σ +0.001..+0.013); the T14 ratio sec/prim is 0.981 ± 0.017. Gaia gives e sin ω = −0.036 ± 0.0125 and e = 0.041 ± 0.012. That is about 3σ in the circular (Lucy–Sweeney) direction, the seventh case of the wave-4 pattern. It is soft, because trapezoid T14s of grazing V-shapes are biased.
- The out-of-eclipse fold shows about ±3 ppt orbital-phase modulation (asymmetric hump, s1 −1.8 ppt, c2 −2.0 ppt). This looks like ellipsoidal variation plus spots or reflection. It was not modelled further.
- One loose end in the blind census: a 17.9-ppt, S/N 8.9 peak at 4088.051 (s100) lies 0.245 d before the 4088.296 primary, at the window edge. It is the matched filter catching that primary's ingress, not a separate event. No other off-ephemeris dip reaches half the eclipse depth.

## Prior art
- cats.py (r 60″): no VSX entry at the target. VSX has neighbours only: an EA star with P 0.91475 d at 27″ (G 16.63) and another at 55″ (G 16.76). ASAS-SN: none. SIMBAD lists it as SB* with one reference, Gaia DR3 2023A&A...674A..34G.
- SB9, WDS and J/AJ/160/111: none.
- Gaia DR3: vari_summary and vari_eclipsing_binary have no rows; phot_variable_flag is NOT_AVAILABLE.
- ExoFOP was down tonight: HTTP 503, maintenance page via both urllib and curl. So TOI/CTOI was not re-checked here; the batch sweep covered it.
- A web search on the TIC, TYC and Gaia DR3 ids found nothing.
- **No eclipsing prior art found. The eclipses are new; the SB1 is Gaia's.**

## Row fixes
- P = **5.4921244 ± 0.0000015 d** (batch 5.49211). T0 = 2753.70951 ± 0.00034 BTJD (primary).
- Depth: QLP-SAP weighted **29.2 ± 0.1 ppt** (sector range 27.2–33.6; batch 27.5 was the median of the batch estimator). Crowding-corrected PDCSAP is 37–40 ppt.
- Secondary: **7.6 ± 0.2 ppt** (QLP) at phase **0.50020 ± 0.00019**.
- Event count: **21** primaries (batch 20) and 21 secondaries.
- dphi: the primary sits on conjunction A, +0.006 phase at the Gaia epoch (+0.9σ) and −0.0001..−0.013 in TESS sectors. The secondary sits on conjunction B, +0.003 phase at the Gaia epoch (+0.6σ). Equivalently B − A = 0.5002 vs Gaia's 0.5036 ± 0.011. The batch's +0.002/+0.498 is confirmed, and the 0.498 is now an eclipse.
- Diffimg 3.13″: a calibration/crowding artefact, not an offset source.
- T14 3.70–3.78 h, grazing.

## Next predicted eclipses (BTJD, linear ephemerides)
- Primary: 4335.4413, 4340.9335, 4346.4256, 4351.9177 (±1 min).
- Secondary: 4338.1861, 4343.6782, 4349.1703, 4354.6624 (±2.5 min).

## What would settle it further
- An RV spectrum to check for SB2 lines of a 3900 K companion. In the red, the K7/M0 is about 3–5% of the light.
- A proper limb-darkened light-curve fit with a dilution prior, to get e sin ω and i without trapezoid bias.
- A WCS-calibrated PRF (not Gaussian) difference image in s064/s099, to drive the residual offset down. This is a nicety, not a doubt.

## Files
- Output: vet-out.txt, fold_oc.png, events.png, timing-out.txt, shapes-out.txt, twosphere-out.txt, physics-out.txt, neighbours-out.txt, indep-out.txt, locate-s00{10,11,37}-out.txt, gaiatap-out.txt, cats-out.txt, morecats-out.txt, mastlc-out.txt.
- Downloaded products are in C:\Home\sky\data\qlp-sb-p20-60\vet315849332\.
