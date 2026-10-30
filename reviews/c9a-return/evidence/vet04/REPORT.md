# vet04: adversarial check of TIC 283532878 (UCAC4 740-075601) and TIC 407877153 (UCAC4 054-021425)

Opus 5.5 subagent, 2026-10-30, for Fable 5.1. This run resumed the work of an earlier agent that a container restart killed part-way through. I re-read its scripts and outputs `s01`–`s11` and kept what they had measured. I re-ran the archive step it had not finished (`s12`), and found that the first VizieR pass gave false empty results (see §1). New steps: a difference-image test with real noise weighting (`s13`, `s13b`), because the `s11` "chi2" values were unweighted sums of squares. Also new: ZTF (`s14`), plots (`s15`), a common-mode test (`s16`), extra geometry, physics and ephemeris (`s17`), and a merged event table (`s18`). All of these are in `[local path omitted]`. The downloads are in the scratchpad at `.../scratchpad/data/vet04/<tic>/`. I deleted the TESScut cubes after `s13`. Notation: **A** = the companion passes in front of Gaia's RV star (true anomaly ν = 90° − ω); **B** = the RV star passes in front of the companion. Depths are in ppt, times in BTJD = BJD_TDB − 2457000, durations in hours.

**TIC 283532878: CONFIRMED.**
- (1) Each event fitted on its own in raw QLP SAP flux, QUALITY==0: 11 primaries and 9 full secondaries, plus 1 partial secondary. One more primary (s16, 1744.53) is visible only in TESScut.
- (2) The eclipses give P = 17.446019 ± 0.000019 d. Gaia's 17.4298 ± 0.0089 d is +1.83σ away.
- (3) Difference images in all 8 sectors (cameras 2, 3 and 4) put both the primary and the secondary on the target. Primary offsets are 0.4–1.5″. Secondary offsets are 1.0–5.3″, each within ~2σ. Every Gaia neighbour is rejected by Δχ² ≥ 1119 for the primary and Δχ² ≥ 41.7 for the secondary in every sector. The dilution arithmetic alone excludes every neighbour for the primary (each would need ≥ 218%). For the 10 ppt secondary it does **not** exclude three neighbours (G 14.50 at 37″, G 14.93 at 28″, G 15.74 at 29.5″, each needing 30–47%); the pixels do.
- (4) QLP SAP and my own TESScut photometry agree on the secondary (9–10 ppt in both). For the primary, QLP gives 70–79 ppt and the TESScut aperture 65–72 ppt, with 13–20% of that aperture's light from neighbours. The PSF-deblended depth is 71–77 ppt. No TESS-SPOC or 2-min data exist.
- (5) The secondary is at phase 0.67812 ± 0.00030; Gaia's e and ω predict 0.712 ± 0.024 (−1.4σ). The primary falls 0.20 d from Gaia's conjunction A (0.4–0.7σ); B is excluded at > 11σ.
- **Screen check:** the screen was right. The "~9 ppt dip near 0.675" is the eccentric secondary. It is not a one-sector glitch: it appears in all 8 sectors and 4 seasons at constant phase (0.6775–0.6795). Its depth is 9–10 ppt; 10–11 ppt deblended.

**TIC 407877153: CONFIRMED.**
- (1) Each event fitted on its own: 9 full primaries and 9 secondaries in raw SAP, plus extra partial events (two primaries, two secondaries).
- (2) The eclipses give P = 17.089294 ± 0.000008 d. Gaia's 17.0902 ± 0.0063 d is −0.14σ away.
- (3) Difference images put the primary on the target in 6 sectors (Δχ² ≥ 337 against every neighbour). The secondary also fits best on the target in 6 sectors (Δχ² ≥ 7 per sector; ≥ 166 summed over sectors). The arithmetic needs ≥ 441% (primary) and ≥ 51% (secondary) on any neighbour.
- (4) Three pipelines: TESS-SPOC SAP (28.6–29.4 ppt), my own TESScut aperture (29.4–31.0 ppt) and QLP SAP. QLP gives 27–29.6 ppt in s12/s39 but only 24–27 ppt in s93–s102, a QLP dilution issue. The secondary is 2.6–4.2 ppt in all three.
- (5) The secondary is at phase 0.54690 ± 0.00017; the prediction is 0.559 ± 0.044 (−0.28σ). The primary is at conjunction A (0.16–0.64σ); B is excluded at ≥ 5σ.
- **Screen check:** the secondary is **3.0 ppt, not ~2 ppt** (stack 2.98 ± 0.13). The primary is ~29 ppt in SPOC and TESScut, not ~27 (27 is QLP's diluted value). The phase of 0.545 was right.

## 1. Archives and web
- **VizieR cones** (`s12d_recheck.out`, mirror vizier.idia.ac.za, run immediately after an Algol VSX control returned bet Per, EA/SD):
  - **TIC 283532878** is not in VSX, Gaia DR3 EB (I/358/veb), Prsa+2022, IJspeert+2021, Gaia varisum or SB9 within 60″ of the target. Both VSX and Gaia-EB list one row at **29.6″: Gaia DR3 2202301140233408128**, G 17.66 (the "VARIABLE" neighbour in `neighbours_90as.csv`). It is VSX type E, P = 1.79747 d, G 17.61–18.17; Gaia EB eclipse depths are 0.39 and 0.60 (`s12e_neighbour_eb.out`). It is excluded as the source below.
  - **TIC 407877153:** nothing in any of those six catalogues within 60″.
- **First-pass warning:** the first pass (`s12_archives.out`) returned 0 rows everywhere, including the EB above, and its Algol control failed later (`s12c_controls.out`: VSX 0 rows for Algol). The mirror was intermittently returning empty tables. The all-catalogue 5″ query is likewise unreliable here: its Algol control gave 0 tables (`s12b_archives.out`), so I do not use it.
- **SIMBAD** (sim-coo 10″, `s12b_archives.out`): both stars are type **SB\*** with 1 bibcode (2023A&A...674A..34G, the Gaia DR3 NSS paper). TIC 283532878 = UCAC4 740-075601 = 2MASS J21512860+5759057. TIC 407877153 = UCAC4 054-021425 = 2MASS J18230801-7921092.
- **ExoFOP:** no TOI. "CTOIs 0" on both pages.
- **Conclusion:** neither star is a catalogued eclipsing binary within 60″. Both are known only as Gaia SB1s.

## 2. Independence, systematics, pixels
- **Pipelines:**
  - 283532878: QLP SAP (8 sectors) plus my own TESScut aperture photometry (8 sectors). The two agree on the secondary. The primary is shallower in my aperture because it holds 13–20% neighbour light (`s11_pixels_283532878.out`: target fraction 0.796–0.873).
  - 407877153: QLP, TESS-SPOC (s12, s13, s39) and TESScut. SPOC and TESScut agree on the primary to about 1 ppt; QLP s93–s102 are ~10–15% shallower. No 2-min SPOC data exist for either star.
- **Difference images, noise-weighted (`s13_pixnoise_*.out`, `s13b_summary.out`):** in each sector I averaged the per-event (median out − median in) images. The per-pixel noise comes from 300 pseudo-events at random out-of-eclipse times with the same windows. I then fitted Gaussian-PSF single-source models for the target and for every Gaia neighbour with G < 18 within 90″. Results:
  - 283532878 P: S/N 40–154 per sector; least-rejected neighbour Δχ² = 73,292 summed (≥ 1119 in every sector); PSF-amplitude depth on target 70.6–77.3 ppt.
  - 283532878 S: S/N 8.6–14.9; Δχ² ≥ 41.7 in every sector, ≥ 977 summed; depth 9.8–12.9 ppt; free-fit offsets 1.0–5.3″ (1σ 1.3–2.9″).
  - 407877153 P: S/N 18.6–84; Δχ² ≥ 337; depth 30.0–35.3 ppt.
  - 407877153 S: S/N 2.8–8.7; Δχ² ≥ 7.1 per sector, ≥ 166 summed; offsets 3.6–9.9″ with 1σ 1.9–12″.
  - I looked at two of the images (`s15_diff_283532878_s57_S.png`, `s15_diff_407877153_s13_S.png`). In both, the deficit sits on the target pixel, away from the bright neighbours in the direct image.
- **Dilution arithmetic** (per-sector aperture flux fractions, `s11_pixels_*.out`):
  - **283532878 primary:** every neighbour needs ≥ 218% intrinsic depth, so all are excluded.
  - **283532878 secondary (10.2 ppt):** most neighbours are excluded arithmetically (≥ 82% needed; the G 17.66 Gaia EB at 29.7″ needs 181–240%). Three are **not**: G 14.50 at 37.0″ needs 29.6–100%, G 14.93 at 28.3″ needs 30–47%, and G 15.74 at 29.5″ needs 31.8–39%. The difference images reject them instead (Δχ² ≥ 41.7 each sector).
  - **407877153:** the primary needs ≥ 441% on any neighbour; the secondary needs ≥ 51.5% (G 14.68 at 60″, s13) and 61–135% for the G 17.23 star at 46″.
- **Same period and phase drift:** both secondaries share the primary's period (283532878: P_S − P_P = −0.00030 ± 0.00010 d; 407877153: +0.000013 ± 0.000059 d, `s05_ephem.out`) and sit at fixed phase over 4–5 seasons. A neighbour's EB would have to share the period exactly. The catalogued neighbour EB (P = 1.7975 d; 17.446/1.7975 = 9.71, not commensurate) would drift in phase.
- **ZTF (`s14_ztf.out`):** not informative. IRSA returns only 54–94 catflags==0 points per object for the target and the five closest bright neighbours, with 0–1 points inside any eclipse window.
- **Common mode (`s16_commonmode.out`):** not done. The MAST product queries kept failing (RemoteServiceError and proxy resets, `s16_commonmode.out`), and the coordinator then dropped this optional step. The pixel and two-pipeline evidence above stands without it.
- **Phase 0.5 of 283532878** (`s17_geometry2.out`, from 10 fixed-time fits in `s08`): +0.35 ± 0.30 ppt. There is no eclipse at phase 0.5. χ² = 45/9 shows red noise at the ~2–3 ppt level.

## 3. TIC 283532878 (P = 17.446 d, e = 0.35)
**Measurements** (`s18_event_table.out`, from `s04`/`s08`/`s11`; trapezoid with quadratic baseline, raw SAP QUALITY==0; "fixed" means the shape is fixed from the 200-s stack). There is no TESS-SPOC column because this star has no TESS-SPOC data.

| Event | Mid BTJD | Depth QLP SAP free / fixed (ppt) | Depth own TESScut ap. (ppt) | T14 / T23 (h) | Pipelines |
|---|---|---|---|---|---|
| P n=−1 s16 | 1744.5307 ± 0.0011 (TESScut) | QLP: 13 flagged cadences | 67.6 ± 1.0 | – | TESScut |
| S n=−1 s16 | 1756.3642 ± 0.0079 | 7.5 ± 1.2 / 7.6 ± 1.1 | 10.1 ± 0.8 | 5.53 / 3.45 | QLP, TESScut |
| P n=0 s16 | 1761.9800 ± 0.0015 | 70.8 ± 1.7 / 70.4 ± 1.4 | 66.9 ± 1.1 | 7.01 / 2.00 | QLP, TESScut |
| S n=0 s17 | 1773.8350 ± 0.0048 | 9.6 ± 0.7 / 9.8 ± 0.7 | 9.2 ± 0.8 | 8.21 / 3.43 | QLP, TESScut |
| P n=1 s17 | 1779.4207 ± 0.0007 | 73.6 ± 0.8 / 73.9 ± 0.9 | 69.6 ± 0.8 | 7.29 / 2.12 | QLP, TESScut |
| P n=61 s56 | 2826.1851 ± 0.0009 | 74.1 ± 1.1 / 74.1 ± 0.9 | 66.8 ± 0.6 | 7.20 / 2.05 | QLP, TESScut |
| S n=61 s56 | 2838.0248 ± 0.0037 (TESScut) | 12.8 ± 2.0 (egress in gap) | 10.7 ± 0.6 | – | QLP (partial), TESScut |
| P n=62 s56 | 2843.6288 ± 0.0010 | 75.5 ± 1.3 / 75.2 ± 1.0 | 66.8 ± 0.5 | 7.04 / 2.02 | QLP, TESScut |
| S n=62 s57 | 2855.4637 ± 0.0090 | 9.2 ± 1.5 / 8.6 ± 1.3 | 9.3 ± 0.5 | 6.08 / 2.19 | QLP, TESScut |
| P n=63 s57 | 2861.0760 ± 0.0010 | 73.5 ± 1.3 / 73.3 ± 1.2 | 68.4 ± 0.6 | 6.95 / 2.05 | QLP, TESScut |
| S n=63 s57 | 2872.9161 ± 0.0070 | 9.0 ± 1.0 / 9.2 ± 1.0 | 9.2 ± 0.5 | 6.87 / 3.03 | QLP, TESScut |
| P n=64 s57 | 2878.5193 ± 0.0005 | 79.2 ± 0.7 / 78.6 ± 0.6 | 69.6 ± 0.5 | 7.11 / 1.97 | QLP, TESScut |
| S n=92 s76 | 3378.8457 ± 0.0067 | 8.9 ± 1.1 / 9.4 ± 1.1 | 9.8 ± 0.5 | 6.34 / 3.85 | QLP, TESScut |
| P n=93 s76 | 3384.4553 ± 0.0007 | 76.4 ± 0.9 / 77.3 ± 0.8 | 68.8 ± 0.6 | 6.76 / 2.26 | QLP, TESScut |
| S n=93 s77 | 3396.2636 ± 0.0050 | 10.4 ± 0.7 / 10.1 ± 0.8 | 9.4 ± 0.5 | 8.89 / 2.96 | QLP, TESScut |
| P n=94 s77 | 3401.9005 ± 0.0008 | 75.4 ± 1.0 / 75.5 ± 0.8 | 71.8 ± 0.7 | 6.98 / 2.10 | QLP, TESScut |
| S n=94 s77 | (3413.73) | in the 3407.0–3417.2 data gap | – | – | none |
| P n=95 s77 | 3419.3449 ± 0.0008 | 74.9 ± 1.0 / 74.1 ± 0.9 | 70.9 ± 0.5 | 7.22 / 1.89 | QLP, TESScut |
| S n=103 s83 | 3570.7490 ± 0.0055 | 9.6 ± 1.0 / 9.9 ± 0.9 | 9.4 ± 0.7 | 6.33 / 3.35 | QLP, TESScut |
| P n=104 s83 | 3576.3613 ± 0.0011 | 74.6 ± 1.3 / 74.4 ± 1.1 | 68.3 ± 0.7 | 7.03 / 2.05 | QLP, TESScut |
| S n=104 s84 | 3588.1988 ± 0.0068 | 9.8 ± 1.3 / 9.9 ± 1.3 | 9.1 ± 0.7 | 5.67 / 3.36 | QLP, TESScut |
| P n=105 s84 | 3593.8100 ± 0.0005 | 76.4 ± 0.7 / 76.6 ± 0.6 | 65.5 ± 0.5 | 7.07 / 2.09 | QLP, TESScut |
| S n=105 s84 | 3605.6254 ± 0.0035 | 12.8 ± 0.7 / 12.6 ± 0.6 | 10.2 ± 0.4 | 7.32 / 2.48 | QLP, TESScut |

- **Stacked shape** (200-s QLP, `s08_shape_oddeven.out`):
  - Primary: 75.41 ± 0.39 ppt, T14 = 7.028 ± 0.034 h, T23 = 2.08 ± 0.05 h. This is a near-V shape: a grazing or partial eclipse.
  - Secondary: 10.24 ± 0.40 ppt, T14 = 6.66 ± 0.25 h, T23 = 2.78 ± 0.36 h.
- **Period** (`s05_ephem.out`):
  - 11 primaries alone: P = 17.446025 ± 0.000017 d (χ² = 56/9; O−C within ±7 min). 9 secondaries alone: 17.445724 ± 0.000099 d.
  - The joint fit gives P = 17.446019 ± 0.000019 d, +0.0162 d from Gaia's period = **+1.83σ_Gaia**.
  - The cycle count is unambiguous: consecutive primaries within s56, s57 and s77 are 17.44 d apart.
- **Odd/even** (QLP fixed shape): 76.25 ± 0.38 vs 75.36 ± 0.33 ppt. The difference is 1.8σ, smaller than the 1.5–2.6 ppt scatter between sectors. A secondary of different depth exists at phase 0.678, so 2P is ruled out, and phase 0.5 is empty, so P/2 is ruled out.
- **Secondary phase by season** (`s17_geometry2.out`): 0.67954 ± 0.00026 (s16–17), 0.67854 ± 0.00033 (s57), 0.67750 ± 0.00025 (s76–77), 0.67775 ± 0.00016 (s83–84).
- **Physics:** f(m) = 0.0334 M☉. With the TIC M1 = 1.35 M☉, m2 ≥ 0.48 M☉ and a = 34.6 R☉. The depth ratio S/P = 0.136 implies a TESS-band surface-brightness ratio ≈ T2 3830 K, consistent with an early-M companion with R2 ≳ 0.5 R☉. A central eclipse at conjunction A would last ~9.5 h; the observed 7.0 h and V shape mean a high impact parameter. The duration ratio S/P = 0.948 ± 0.036 gives e sin ω ≈ −0.03 ± 0.02, against Gaia −0.086 ± 0.044. The equal-b assumption behind that number is weak for grazing eclipses.

## 4. TIC 407877153 (P = 17.089 d, e = 0.13)
**Measurements** (`s18_event_table.out`). TESS-SPOC depths are fixed-shape fits where available.

| Event | Mid BTJD | Depth QLP SAP free / fixed (ppt) | Depth TESS-SPOC SAP (ppt) | Depth own TESScut (ppt) | T14 / T23 (h) | Pipelines |
|---|---|---|---|---|---|---|
| S n=−1 s12 | 1626.5135 ± 0.0171 (TESScut) | QLP: 17 flagged | – | 2.9 ± 0.7 | – | TESScut |
| P n=0 s12 | 1634.2635 ± 0.0017 | 27.5 ± 0.5 / 27.4 ± 0.6 | 29.2 ± 0.5 | 30.1 ± 0.7 | 9.44 / 6.10 | QLP, SPOC, TESScut |
| S n=0 s12 | 1643.5993 ± 0.0077 | 3.2 ± 0.6 / 2.9 ± 0.5 | 3.6 ± 0.5 | 2.9 ± 0.6 | 7.62 / 7.29 | QLP, SPOC, TESScut |
| P n=1 s12 | 1651.3509 ± 0.0012 | 27.5 ± 0.6 (partial) | 29.4 ± 0.5 | 29.9 ± 0.6 | 9.72 / 5.81 | QLP (partial), SPOC, TESScut |
| S n=1 s13 | 1660.7055 ± 0.0069 | 3.0 ± 0.5 | 2.9 ± 0.4 | 3.1 ± 0.4 | 7.46 / 6.61 | QLP, SPOC, TESScut |
| P n=2 s13 | (1668.43) | in the 1667.6–1668.7 gap | gap | – | – | none |
| S n=2 s13 | 1677.7897 ± 0.0079 | 2.9 ± 0.5 / 2.6 ± 0.4 | 3.0 ± 0.3 | 2.9 ± 0.4 | 7.81 / 7.10 | QLP, SPOC, TESScut |
| P n=43 s39 | 2369.1015 ± 0.0009 | 29.5 ± 0.4 / 29.0 ± 0.4 | 28.6 ± 0.4 | 29.5 ± 0.4 | 9.53 / 6.10 | QLP, SPOC, TESScut |
| S n=43 s39 | 2378.4374 ± 0.0064 | 3.8 ± 0.7 / 3.0 ± 0.4 | 2.9 ± 0.3 | 3.2 ± 0.3 | 8.62 / 6.29 | QLP, SPOC, TESScut |
| P n=44 s39 | 2386.1901 ± 0.0010 | 29.6 ± 0.5 / 29.3 ± 0.4 | 28.7 ± 0.4 | 29.4 ± 0.4 | 9.65 / 6.05 | QLP, SPOC, TESScut |
| S n=128 s93 | 3831.0358 ± 0.0104 | 4.2 ± 0.6 / 3.5 ± 0.4 | – | 3.0 ± 0.4 | 9.27 / 2.83 | QLP, TESScut |
| P n=129 s93 | 3838.7816 ± 0.0010 | 27.1 ± 0.4 / 27.3 ± 0.4 | – | 29.5 ± 0.4 | 9.38 / 6.55 | QLP, TESScut |
| S n=129 s93 | 3848.1399 ± 0.0053 | 2.9 ± 0.3 / 2.9 ± 0.4 | – | 3.7 ± 0.4 | 7.66 / 6.63 | QLP, TESScut |
| S n=130 s94 | 3865.2086 ± 0.0068 | 3.2 ± 0.3 / 3.2 ± 0.3 | – | 4.2 ± 0.4 | 9.56 / 5.54 | QLP, TESScut |
| P n=131 s94 | 3872.9595 ± 0.0013 | 24.7 ± 0.4 / 24.3 ± 0.4 | – | 29.6 ± 0.5 | 9.85 / 5.89 | QLP, TESScut |
| P n=143 s100 | 4078.0293 ± 0.0011 | 26.8 ± 0.4 / 26.7 ± 0.4 | – | 31.0 ± 0.5 | 9.45 / 6.20 | QLP, TESScut |
| S n=143 s100 | (4087.36) | 64 flagged cadences | – | – | – | none |
| P n=144 s100 | 4095.1193 ± 0.0010 | 24.7 ± 0.4 / 24.8 ± 0.3 | – | 29.4 ± 0.4 | 9.51 / 6.45 | QLP, TESScut |
| S n=144 s101 | 4104.4747 ± 0.0102 | 2.9 ± 0.3 / 2.6 ± 0.2 | – | no cube | 12.06 / 3.76 | QLP |
| P n=145 s101 | (4112.23) | 156 flagged cadences | – | no cube | – | none |
| S n=145 s101 | 4121.5442 ± 0.0073 | 3.0 ± 0.3 / 2.8 ± 0.3 | – | no cube | 8.90 / 4.73 | QLP |
| P n=146 s102 | 4129.2998 ± 0.0009 | 25.0 ± 0.3 / 24.9 ± 0.4 | – | 29.5 ± 0.4 | 9.37 / 6.28 | QLP, TESScut |
| S n=146 s102 | 4138.6654 ± 0.0176 (TESScut) | QLP: 155 flagged | – | 4.3 ± 1.1 | – | TESScut |
| P n=147 s102 | 4146.3904 ± 0.0024 | 23.7 ± 0.7 (ingress lost) | – | 25.0 ± 0.7 | 9.11 / 6.53 | QLP (partial), TESScut |

- **Stacked shape** (200-s QLP):
  - Primary: 25.53 ± 0.16 ppt (QLP-diluted), T14 = 9.459 ± 0.051 h, T23 = 6.38 ± 0.08 h. **Flat-bottomed**, a total transit.
  - Secondary: 2.98 ± 0.13 ppt, T14 = 8.46 ± 0.31 h, T23 = 5.71 ± 0.50 h. **Flat-bottomed**, an occultation.
- **Period:**
  - 9 primaries: P = 17.089294 ± 0.000006 d (χ² = 6.0/7; O−C within ±2.3 min). 9 secondaries: 17.089307 ± 0.000059 d.
  - Joint fit: P = 17.089294 ± 0.000008 d, **−0.14σ_Gaia**.
  - Secondary phase by season: 0.54630–0.54713, steady.
- **Odd/even:** TESS-SPOC 28.91 ± 0.31 vs 28.91 ± 0.30 ppt. The QLP odd/even difference (26.10 vs 26.91) comes from which sectors fall in each group: QLP s93+ are diluted. 2P and P/2 are excluded as for the other star.
- **Physics:**
  - f(m) = 0.0216 M☉. With the TIC M1 = 0.87 M☉, m2 ≥ 0.31 M☉ and a = 29.5 R☉.
  - The flat-bottom depth gives k ≈ 0.16, so R2 ≈ 0.31 R☉ with the TIC R1 = 1.91 R☉. That matches a 0.31 M☉ M dwarf.
  - The occultation/transit ratio of 0.117 gives T2 ≈ 3200 K (TESS-band Planck).
  - A central T14 at conjunction A would be 10.6 h; observed 9.46 h, so b is moderate.
  - The duration ratio S/P = 0.894 ± 0.033 gives e sin ω = −0.056 ± 0.018, against Gaia −0.078 ± 0.066.
  - Everything hangs together as a subgiant + M-dwarf SB1.

## Geometry vs Gaia
- **Method** (`s07_geometry.out`, `s17_geometry2.out`; 20,000 Monte Carlo draws): I propagated P, T_p, e and ω; conjunction A is at ν = 90° − ω and B at ν = 270° − ω. The ω–T_p correlation was taken either as 0 or as the last `corr_vec` element (0.927 and 0.985). That second case assumes the SB1 parameter order ends with (arg_periastron, t_periastron), which I have not verified; results are given both ways.
- **283532878:**
  - Predicted B−A separation: 0.7122 ± 0.0237. Measured secondary phase: 0.67812 ± 0.00030, **−1.44σ**. The other assignment (primary = B) is off by 16σ.
  - The measured phase implies e cos ω = 0.2823 ± 0.0012 (exact Kepler, Gaia e sin ω draws), against Gaia 0.338 ± 0.039 (−1.42σ).
  - Absolute timing, propagated with the TESS period: the primary is +0.0112 phase (+0.20 d) from conjunction A (0.37σ uncorrelated, 0.71σ correlated) and 0.30 phase from B (11.9σ / 23.7σ). Propagated with Gaia's period, A is still within 1.7–2.0σ.
  - **The deep eclipse is A:** the F-type RV star is eclipsed by its companion. **Pass.**
- **407877153:**
  - Predicted separation 0.5589 ± 0.0435; measured 0.54690 ± 0.00017, **−0.28σ**. The other assignment is off by 2.4σ.
  - Implied e cos ω = 0.0733 ± 0.0006, against Gaia 0.093 ± 0.068.
  - The primary is +0.0167 phase (+0.29 d) from A (0.16σ / 0.64σ) and 5.1σ / 18.9σ from B.
  - **The deep eclipse is A**, the subgiant RV star transited by an M dwarf. **Pass.**

## Ephemerides and next eclipses
From `s05_ephem_*.json` and `s17_geometry2.out`. UTC times are geocentric: I removed the barycentric light-time with astropy (offset given in brackets).
- **TIC 283532878:** T0 = BJD_TDB 2458761.97572 ± 0.00150 (BTJD 1761.97572), **P = 17.446019 ± 0.000019 d**. Secondary T0 = 1773.80624 ± 0.00535 (phase 0.67812).
  - Next primaries: BTJD 4343.9865 = 2026-10-30 11:36 UTC [+3.4 min]; 4361.4325 = 2026-11-16 22:18; 4378.8785 = 2026-12-04 09:02. Each ±2.3 min formal; T14 = 7.0 h.
  - Next secondaries: BTJD 4355.817, 4373.263, 4390.709. The secondary phase has moved by ~0.002 between seasons, so allow ±1 h.
- **TIC 407877153:** T0 = BJD_TDB 2458634.26184 ± 0.00084 (BTJD 1634.26184), **P = 17.089294 ± 0.000008 d**. Secondary T0 = 1643.60789 ± 0.00296 (phase 0.54690).
  - Next primaries: BTJD 4351.4596 = 2026-11-06 23:03 UTC [−3.1 min]; 4368.5489 = 2026-11-24 01:13; 4385.6382 = 2026-12-11 03:22. Each ±1.0 min; T14 = 9.5 h.
  - Next secondaries: BTJD 4343.716, 4360.806, 4377.895.

## Caveats
- **Secondary-phase drift in 283532878:** the phase falls 0.0018 between 2019 and 2024 (≈ 45 min, ~4σ formal), and the joint timing χ² is 132/17. GR plus tidal apsidal motion at a/R1 ≈ 18 would give far less (~2.5 × 10⁻⁴ rad over 105 cycles, against the ~0.03 rad needed). I therefore treat this as underestimated timing errors for the 10 ppt, red-noise-affected secondaries, not as physics. It does not affect the Gaia test, whose tolerance is ±0.024.
- **Catalogued EB 29.7″ from 283532878:** this is G 17.66, P = 1.7975 d, eclipses 40–60% deep in G. With 0.4–0.6% of the light in my apertures it can add dips of ≤ 3 ppt at unrelated phases. That may explain some event-to-event scatter in the secondary depths (for example S n=105, 12.6 ppt). It cannot produce the secondary: the period is wrong, the depth needed is 181–240%, and the pixels reject it.
- **Gaussian-PSF limits:** the pixel model uses a Gaussian PSF. Formal centroid offsets for the primaries (up to 1.5″ for 283532878; 5.1″ and 7.6″ in s93 and s102 for 407877153, the s102 stack including a partial event) exceed their noise-only errors. That is model systematics; every neighbour is ≥ 26″ away and rejected by Δχ² in the hundreds or more.
- **Deblended depths are model-dependent:** for 283532878, about 71–77 ppt (PSF amplitude) up to ~80 ppt (aperture depth ÷ target fraction). The TIC contamination ratio is 0.32. QLP's SAP depths for 407877153 in s93–s102 are diluted by ~10–15%.
- **Not used:** ZTF (too few epochs), 2-min SPOC (none exists), TESScut for s101 of 407877153 (not downloaded; QLP covers its two secondaries).
- **Correlation assumption:** the `corr_vec` ordering behind the correlated Monte Carlo case is assumed, not verified. The secondary-phase test does not use T_p at all.

## Files
All in `[local path omitted]`:
- **Shared code:** `common.py` (loader, Gaia constants), `fitlib.py` (trapezoid fitter).
- **Earlier agent, read and kept:**
  - `s01_download` (QLP/TESS-SPOC light curves); `s02_inventory` (sectors, gaps, flags); `s03_blind` (blind dip census); `s04_events` (+ `.json`, per-event free fits); `s05_ephem` (+ `s05_ephem_<tic>.json`); `s06_gaia_query` (+ `s06_gaia_nss.csv`, `s06_gaia_source.csv`); `s07_geometry` (Monte Carlo conjunctions); `s08_shape_oddeven` (+ `.json`, `s08_stack_*.npz`); `s10_tesscut_dl`; `s11_pixels` (+ `_<tic>.out/.json`, `s11_diff_*.npy`; aperture photometry, dilution).
- **This run:**
  - `s12_archives.out` (first pass, false negatives), `s12b_archives` (SIMBAD by coordinates, ExoFOP), `s12c_controls` (failed Algol control), `s12d_recheck` (cones with passing control), `s12e_neighbour_eb` (neighbour EB rows).
  - `s13_pixnoise` (+ `_<tic>.out/.json`, `s13_diff_*.npz`), `s13b_summary`.
  - `s14_ztf`, `s15_plot_diff` (+ `s15_diff_*.png`), `s16_commonmode`, `s17_geometry2`, `s18_event_table`.
- **Downloads:** `/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet04/` (TESScut cubes deleted).

TIC 283532878: CONFIRMED; P_ecl=17.446019±0.000019 d; depth1=75 ppt (QLP SAP; 71–77 deblended); depth2=10 ppt at phase 0.6781; pixel: on target; pipelines: 2 (QLP, own TESScut); Gaia geometry: pass
TIC 407877153: CONFIRMED; P_ecl=17.089294±0.000008 d; depth1=29 ppt (TESS-SPOC/TESScut; 25–27 QLP s93+); depth2=3.0 ppt at phase 0.5469; pixel: on target; pipelines: 3 (QLP, TESS-SPOC, own TESScut); Gaia geometry: pass
