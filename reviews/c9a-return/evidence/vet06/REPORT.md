# vet06: adversarial check of TIC 468827621 (UCAC4 796-015685) and TIC 416285595 (UCAC4 571-080398)

Opus 5.5 subagent, 2026-10-30, for Fable 5.1. This is a reduced-depth run: the coordinator cut the budget mid-task. It covers the five protocol checks only; physics, next-eclipse lists, the common-mode test and the literature search were skipped.

Light curves were fetched from MAST's `Download/file` endpoint (`s2`), because `lightkurve.search_lightcurve` hung at MAST and archive.stsci.edu serves an incomplete TLS chain. Data are in `scratchpad/data/vet06/<tic>/`. Each TESScut cube was deleted after use.

Depths are in ppt. Times are BTJD (BJD_TDB − 2457000). A = the companion passes in front of Gaia's RV star (ν = 90° − ω); B = the companion is behind it.

**TIC 468827621: CONFIRMED.** All five checks pass:
1. **Individual events.** 10 primary and 9 secondary epochs are fitted individually from raw SAP (QUALITY==0) in QLP s19, 20, 59, 60, 73 and TESS-SPOC s19, 20.
2. **Period.** The eclipse period is 11.041067 ± 0.000001 d (primaries, O−C rms 0.5 min). It is −0.16σ from Gaia's 11.04138 ± 0.00196 d. The secondaries alone give 11.041068 ± 0.000005 d.
3. **Pixels.** The primary deficit is 1.42″ (s19) and 1.50″ (s59) from the target's WCS position. The only neighbour bright enough in principle is G 13.40 at 70.6″. With its PRF share of my aperture it would need a 4800–7800% intrinsic eclipse, and the fractional deficit at its pixel is only 1–4 ppt. Both other neighbours need more than 100% even in the worst case.
4. **Pipelines.** QLP, TESS-SPOC and my TESScut aperture all see the primary: 192, 184 and 192 ppt.
5. **Geometry.** The primary is at conjunction A (−0.14 ± 0.09 d); B is excluded at 31σ (20σ without Gaia's correlations). The secondary phase, **0.72649 ± 0.00003**, is +0.56σ from Gaia's predicted 0.718 ± 0.015 (from e = 0.355, ω = 350°). The eclipse at A, nearer periastron, is the longer one: 6.0 h against 5.05 h. That is the direction e sin ω = −0.06 requires.

The screen was right on P, on both depths (QLP) and on the secondary phase: 0.7265 measured against its by-eye 0.72. TESS-SPOC SAP depths are about 4% shallower than QLP (184/29.6 against 192/31.5 ppt).

**TIC 416285595: CONFIRMED.** All five checks pass, with weak points below:
1. **Individual events.** 21 primary and 19 secondary epochs are fitted individually: QLP s14, 40, 54, 80, 81 and TESS-SPOC s40.
2. **Period.** P = 4.615357 ± 0.000003 d (O−C rms 2.4 min), −0.37σ from Gaia's 4.615565 ± 0.000559 d.
3. **Pixels.** The primary deficit is 2.16″ (s40, camera 1) and 0.58″ (s80, camera 2) from the target. Every one of the 43 neighbours needs more than 100% with its PRF share; the minimum is 126%, for G 14.75 at 37.9″ in s40. The neighbours that pass only in the unphysical worst case (100% of their flux in my aperture) all lie 37″ or more away, at least 1.8 px from a deficit centre that sits within 0.1 px of the target. So the primary is on the target, and the screen's contamination concern (ratio 0.27) does not change the attribution of the primary.
4. **Pipelines.** QLP and TESS-SPOC see every event at the same times and durations. Depth agreement is the weakest part (see the weak points).
5. **Geometry.** The primary is at conjunction A (−0.04 ± 0.08 d); B is excluded at 29σ with correlations, but only 3.3σ without. The secondary phase, 0.50011 ± 0.00027, is +0.28σ from Gaia's 0.49 ± 0.03.

Weak points:
- **Depths disagree between pipelines.** QLP is deeper than TESS-SPOC in s40: 61.7 against 54.7 ppt, about 12% and about 4σ apart. My TESScut aperture gives 70 (s40) and 89 ppt (s80), but its background (median of pixels ≥ 4 px away) is unreliable in this crowded field. I attribute the spread to crowding and background, since none of these is a crowding-corrected depth. Strict agreement within errors fails.
- **The secondary is not tested in pixels.** At 12.9 ppt, G 14.75 at 37.9″ could produce it arithmetically (it would need about 26%). Only the exact phase 0.5001 and the matching period tie it to the target.
- **The geometry test is weak.** e ≈ 0.08, so phase 0.5 is the generic expectation, and the A/B decision rests on Gaia's ω–Tp correlation of 0.998.

The screen was right on P and on the secondary phase. Its 59 ppt primary depth matches QLP but not TESS-SPOC (54.7). Its 11 ppt secondary is low: QLP and TESS-SPOC both give 12.9 ppt. The primary is near-V: T14 3.6 h, trapezoid T23 about 0.7 h.

## 1. Archives and web
- **VizieR mirror cones (`s1_archives.out`, `s1b_archives.out`):** both stars return 0 rows within 60″ in VSX, Prša+2022, IJspeert+2021, Gaia DR3 veb / vclassre / vari (10″), SB9, ASAS-SN II/366 and J/AJ/162/170. Algol returns 1 VSX row, so the cones work.
  - Neither star is a catalogued eclipsing binary: none is listed in VSX, Gaia-EB, Prša or IJspeert within 60″.
  - 468827621 is in the Gaia DR3 short-timescale table I/358/vst (amplitude 0.044 mag) and is flagged VARIABLE in gaia_source.
- **SIMBAD:** both are SB\*, with 2 bibcodes (468827621) and 1 bibcode (416285595), all Gaia DR3. The SIMBAD lookup by TIC ID fails; the 10″ coordinate cone finds both.
- **ExoFOP:** 0 TOIs and 0 CTOIs for both.
- **Gaia SB1 rows (`gaia_tbosb1.tsv`, with corvec):**
  - 468827621: e 0.3555 ± 0.0239, ω 350.13 ± 3.87°, K1 42.03 km/s.
  - 416285595: e 0.078 ± 0.044, ω 104 ± 36°, K1 46.4 km/s.

## 2. Independence, systematics, pixels
- **Pipeline depths (`s3_events.out`, per-event means):**
  - 468827621 primary: QLP 191.9 (sd 3.6, N = 10); TESS-SPOC 184.5 (sd 5.0, N = 4); TESScut 191.9 (s19) and 191.7 (s59).
  - 468827621 secondary: QLP 31.5 (sd 1.0); TESS-SPOC 29.6 (sd 1.2).
  - 416285595 primary: QLP 58.6 (sd 3.3, N = 20); TESS-SPOC 54.7 (sd 1.3, N = 6); TESScut 69.8 (s40) and 89.4 (s80), background-limited.
  - 416285595 secondary: QLP 12.9 (sd 2.5); TESS-SPOC 12.9 (sd 1.4).
  - Neither star has 2-min SPOC data.
- **Odd/even (primaries):** 468827621 +0.38σ (QLP) and −0.09σ (SPOC); 416285595 −1.2σ (QLP) and +1.1σ (SPOC). The two eclipse kinds differ in depth (and, for 468827621, in duration), so there is no hidden P/2 or 2P.
- **Difference images (`s4_tesscut_<tic>_s<sec>.txt/.png`; mean over primaries of median in-eclipse minus local out-of-eclipse; Gaussian-fit centre):**

| Star / sector (cam) | N ev | deficit − target WCS | frac. depth, target pixel | aperture share of target |
|---|---|---|---|---|
| 468827621 s19 (cam 2) | 2 | 1.42″ (deficit − OOT 1.17 ± 0.33″) | 158 ppt | 0.962 |
| 468827621 s59 (cam 2) | 3 | 1.50″ (deficit − OOT 1.62 ± 0.35″) | 117 ppt | 0.957 |
| 416285595 s40 (cam 1) | 4 | 2.16″ | 34 ppt | 0.826 |
| 416285595 s80 (cam 2) | 5 | 0.58″ | 48 ppt | 0.854 |

  - For 416285595 the out-of-eclipse Gaussian locked onto a brighter star at the cutout edge, so only the WCS offset is quoted.
  - Both 468827621 sectors are in camera 2. That is the only camera available.

## 3. TIC 468827621 (P 11.041067 d)
`events_468827621.csv`: trapezoid on a quadratic baseline; errors are the covariance scaled to the rms, inflated by a 10-shift prayer bead.

| Event | Mid BTJD | Depth QLP / SPOC (ppt) | T14 / T23 (h) | pipelines |
|---|---|---|---|---|
| P E0 s19 | 1819.85379 ± 0.00025 | 196.9 / 189.9 | 6.00 / 2.33 | QLP+SPOC+TESScut |
| P E1 s19 | 1830.89477 ± 0.00025 | 196.6 / 188.9 | 5.99 / 2.34 | QLP+SPOC+TESScut |
| P E3 s20 | 1852.97691 ± 0.00024 | 186.4 / 179.4 | 6.02 / 2.33 | QLP+SPOC |
| P E4 s20 | 1864.01807 ± 0.00027 | 187.5 / 179.6 | 6.00 / 2.36 | QLP+SPOC |
| P E99 s59 | 2912.91944 ± 0.00020 | 195.2 / – | 6.03 / 2.31 | QLP+TESScut |
| P E101 s59 | 2935.00116 ± 0.00019 | 194.2 / – | 5.99 / 2.39 | QLP+TESScut |
| P E102 s60 | 2946.04227 ± 0.00038 | 187.8 / – | 6.03 / 2.33 | QLP |
| P E103 s60 | 2957.08343 ± 0.00018 | 190.3 / – | 6.02 / 2.31 | QLP |
| P E133 s73 | 3288.31654 ± 0.00045 | 191.6 / – | 5.96 / 2.35 | QLP |
| P E135 s73 | 3310.39800 ± 0.00018 | 192.1 / – | 5.99 / 2.36 | QLP |
| S E−1 s19 | 1816.83466 ± 0.00143 | – / 30.8 | 5.04 / 2.27 | SPOC |
| S E1 s19 | 1838.91713 ± 0.00110 | 31.9 / 30.3 | 5.14 / 2.17 | QLP+SPOC |
| S E2 s20 | 1849.95666 ± 0.00095 | 29.1 / 27.8 | 5.01 / 2.51 | QLP+SPOC |
| S E3 s20 | 1860.99765 ± 0.00098 | 31.3 / 29.6 | 4.99 / 2.31 | QLP+SPOC |
| S E99 s59 | 2920.94045 ± 0.00089 | 32.4 / – | 5.12 / 2.21 | QLP |
| S E100 s59 | 2931.98226 ± 0.00096 | 32.2 / – | 5.04 / 2.47 | QLP |
| S E101 s60 | 2943.02108 ± 0.00108 | 31.2 / – | 4.87 / 2.49 | QLP |
| S E133 s73 | 3296.33725 ± 0.00087 | 32.2 / – | 5.07 / 2.29 | QLP |
| S E134 s73 | 3307.37832 ± 0.00080 | 31.4 / – | 5.00 / 2.48 | QLP |

- **Lost events:** P E100 (s59), P E134 (s73), S E0 (s19) and S E102 (s60) fall in gaps or flagged data.
- **Ephemerides:**
  - Primaries: P = 11.041067 ± 0.000001 d, O−C within ±1.3 min.
  - Secondaries: P = 11.041068 ± 0.000005 d, O−C rms 1.0 min.
- **SPOC secondary odd/even:** +2.5σ, from only 4 events. The s20 SPOC depths are uniformly low, so this is a sector systematic, not two eclipse kinds.

## 4. TIC 416285595 (P 4.615357 d)
`events_416285595.csv` has all 40 fitted events plus the lost ones. A representative subset:

| Event | Mid BTJD | Depth QLP / SPOC (ppt) | T14 / T23 (h) | pipelines |
|---|---|---|---|---|
| P E0 s14 | 1687.52122 ± 0.00101 | 52.9 / – | 3.46 / 0.91 | QLP |
| P E153 s40 | 2393.67735 ± 0.00069 | 56.4 / 54.6 | 3.64 / 0.66 | QLP+SPOC+TESScut |
| P E154 s40 | 2398.29120 ± 0.00056 | 60.4 / 53.1 | 3.51 / 0.90 | QLP+SPOC |
| P E155 s40 | 2402.90615 ± 0.00051 | 64.2 / 56.8 | 3.74 / 0.60 | QLP+SPOC+TESScut |
| P E156 s40 | 2407.52291 ± 0.00075 | 63.5 / 54.2 | 3.55 / 0.90 | QLP+SPOC+TESScut |
| P E158 s40 | 2416.75340 ± 0.00049 | 64.0 / 55.8 | 3.70 / 0.70 | QLP+SPOC+TESScut |
| P E236 s54 | 2776.75002 ± 0.00096 | 59.9 / – | 3.41 / 0.89 | QLP |
| P E392 s80 | 3496.74568 ± 0.00070 | 57.9 / – | 3.58 / 0.82 | QLP+TESScut |
| P E398 s81 | 3524.43758 ± 0.00072 | 55.4 / – | 3.62 / 0.77 | QLP |
| S E152 s40 | 2391.37357 ± 0.00232 | – / 10.7 | 2.98 / 1.42 | SPOC (QLP fit degenerate) |
| S E156 s40 | 2409.82774 ± 0.00208 | 9.9 / 14.0 | 3.15 / 0.30 | QLP+SPOC |
| S E157 s40 | 2414.44236 ± 0.00167 | 13.6 / 14.7 | 3.50 / 0.20 | QLP+SPOC |
| S E395 s81 | 3512.89836 ± 0.00325 | 11.8 / – | 3.22 / 1.18 | QLP |
| S E397 s81 | 3522.13865 ± 0.00319 | 12.3 / – | 3.39 / 0.95 | QLP |

- **Primary ephemeris:** N = 21 epochs, O−C rms 2.4 min. The two s14 events (30-min cadence) are at −7 min.
- **Secondaries:** P = 4.615370 ± 0.000009 d, O−C rms 8.7 min. Some single-event depth errors are degenerate (T23 → 0); see the csv.

## Geometry vs Gaia
`s0_gaia_predict.out`, `s5_geometry.out` and `s5b_unwrap.out`. The Monte Carlo uses 20000 draws with Gaia's corvec, ordered P, Vcm, K1, e, ω, Tp (column-major upper triangle, positive-definite for both stars). Uncorrelated values are in brackets. "Backward" means the TESS primary ephemeris taken back to the Gaia epoch.
- **468827621:**
  - Backward: primary − A = −0.142 ± 0.087 d (−1.6σ) [−0.142 ± 0.170]; primary − B = +2.97 ± 0.10 d (+31σ) [+20σ].
  - Forward (Gaia ephemeris taken to TESS): −0.18 ± 0.28 d from A.
  - The deep eclipse is conjunction A.
  - Secondary phase: observed 0.72649 against predicted 0.7182 ± 0.0149, **+0.56σ**. If the deep eclipse were B, the shallow one would be predicted at 0.282.
- **416285595:**
  - Backward: primary − A = −0.043 ± 0.075 d [−0.05 ± 0.62]; primary − B = ±2.31 ± 0.08 d (29σ) [±0.70, 3.3σ].
  - Secondary phase: observed 0.50011 against predicted 0.4915 ± 0.0304, +0.28σ.
  - Because e is small, the secondary-phase test is weak.

## Ephemerides
Errors are formal (`s3_events.out`); TESS-pipeline times are already barycentric.
- **TIC 468827621 primary:** T0 = BTJD 1819.85371 ± 0.00010 (BJD_TDB 2458819.85371), P = 11.041067 ± 0.000001 d, T14 6.0 h. Secondary at phase 0.72649 ± 0.00003, T14 5.05 h.
- **TIC 416285595 primary:** T0 = BTJD 1687.52620 ± 0.00067 (BJD_TDB 2458687.52620), P = 4.615357 ± 0.000003 d, T14 3.6 h. Secondary at phase 0.50011 ± 0.00027.

## Caveats
- **SAP depths are not crowding-corrected.** The QLP/SPOC offsets are 4% (468827621) and about 12% (416285595).
- **TESScut photometry** uses a crude background: the median of pixels ≥ 4 px away. In the crowded 416285595 field it gives depths of 70–89 ppt, so it is used for location, not for depth.
- **Secondaries were not pixel-tested** for either star. For 468827621, the G 16.17 star at 24.6″ could arithmetically produce the 31 ppt secondary in the worst case, and for 416285595 the G 14.75 star at 37.9″ could produce the 12.9 ppt one. For both stars only timing ties the secondary to the target.
- **Dilution uses a Gaussian PRF** (σ 0.75 px) with G-band fluxes, not the TESS PRF.
- **The 468827621 difference images** are both from camera 2; no other orientation was available in the sectors used.
- **Not done:** common-mode test, ZTF, physics sanity check, next-eclipse lists.

## Files
`s0_gaia_predict.py/.out`, `s1_archives.py/.out`, `s1b_archives.py/.out`, `gaia_tbosb1.tsv`, `s2_download.py/.out`, `s3_events.py/.out`, `events_468827621.csv`, `events_416285595.csv`, `s3_ephem_<tic>.npy`, `s4_tesscut.py`, `s4_tesscut_<tic>_s<sec>.txt/.npz/.png` (468827621 s19, s59; 416285595 s40, s80), `s5_geometry.py/.out`, `s5b_unwrap.py/.out`, `REPORT.md`.

**Summary**
- TIC 468827621: CONFIRMED; P_ecl=11.041067 d; depth1=184–192 ppt; depth2=29.6–31.5 ppt at phase 0.72649; pixel: on target (primary); pipelines: 3; Gaia geometry: pass
- TIC 416285595: CONFIRMED; P_ecl=4.615357 d; depth1=55–59 ppt (QLP s40 62); depth2=12.9 ppt at phase 0.50011; pixel: on target (primary; secondary untested); pipelines: 3 (depths agree only to ~12%); Gaia geometry: pass (weak, e≈0)
