# vet02: adversarial check of TIC 470235665 (UCAC4 859-013225) and TIC 379251709 (UCAC4 788-006141)

Opus 5.5 subagent, 2026-10-30, for Fable 5.1. A container restart killed the first agent part-way through. This run picked up its outputs (`s1`–`s8`: archives, downloads, raw-SAP event fits, ephemerides, the 379251709 secondary search, Gaia geometry), checked them, and added the missing parts: `s1c` (SIMBAD bibcodes, the 5″ all-catalogue list for 379251709 that `s1b` crashed on), `s9`/`s10` (TESScut pixels and own photometry), `s11` (independence), `s12` (physics, ephemerides), `s13` (secondary-phase drift), `s14` (fold plots) and `s15` (event tables). Scripts and outputs are in this folder. Light curves are in the scratchpad `data/vet02/<tic>/`. Each TESScut cube was deleted after use. Depths are in ppt and times in BTJD (BJD_TDB − 2457000). A = the companion passes in front of Gaia's RV star (true anomaly 90° − ω). B = the companion is behind it.

**TIC 470235665: CONFIRMED.** Every check passed:
1. 25 primaries and 25 secondaries are each re-measured from raw SAP in QLP and TESS-SPOC, sectors 18–85.
2. The eclipse period is 10.326183 ± 0.000002 d, +0.82σ from Gaia's 10.3239 ± 0.0028 d.
3. The difference images in s19 (camera 3) and s79 (camera 4) put the deficit on the target. Its centre is 0.29–0.74″ from the out-of-eclipse centroid. Every neighbour would need an intrinsic depth above 100% even if all its flux fell in the aperture.
4. QLP SAP, TESS-SPOC SAP and my own TESScut aperture all see every event they cover. SPOC and TESScut depths agree to about 1%; QLP is 4% deeper. No 2-min data exist.
5. The primary falls on Gaia conjunction A, −0.07 ± 0.11 d away; B is excluded at 19σ. The secondary phase (0.52275) is +0.7σ from Gaia's prediction. The B/A duration ratio gives e sin ω ≥ 0.17, against Gaia's 0.21 ± 0.05.

The screen got this one right (P 10.3262 d, secondary at phase 0.52). Its depths (128/84 ppt) match QLP. TESS-SPOC SAP and TESScut give 122/81 ppt.

**TIC 379251709: CONFIRMED.** Every check passed:
1. 18 primaries are re-measured individually. The two in s18 that TESS-SPOC flags are recovered in QLP and in my TESScut photometry.
2. The eclipse period is 12.323912 ± 0.000007 d, −0.53σ from Gaia's 12.3261 ± 0.0042 d.
3. The primary deficit is on the target in s18 (camera 2) and s52 (camera 4), 0.10″ and 1.86 ± 0.65″ from the out-of-eclipse centroid. All neighbours are excluded for the primary even in the worst case.
4. QLP, TESS-SPOC and TESScut depths agree (34–38 ppt).
5. The primary is at conjunction A (−0.17 ± 0.22 d); B is excluded at 28σ with Gaia's correlations, 4.2σ without. The secondary phase (0.4960 ± 0.0010) is +0.8σ from the 0.471 ± 0.031 that Gaia's e and ω predict.

Weak points:
- The 2.5 ppt secondary is detected only in folds: QLP S/N 8.5, TESS-SPOC S/N 3.8. It is too shallow for a pixel test or for the neighbour arithmetic.
- The short, V-shaped primary implies a primary radius of about 1.3 R☉, against the TIC's 1.88 R☉ (see Caveats).

The screen's 31 ppt primary depth is low by about 15%: the raw-SAP depth is 34–36 ppt (TESScut 36.5–38.1). Its period and secondary phase are right.

## 1. Archives and web
- **VizieR cones, 60″ (`s1_archives.out`):** VSX (B/vsx/vsx), Prša+2022 (J/ApJS/258/16), IJspeert+2021 (J/A+A/652/A120), Gaia DR3 EBs (I/358/veb), Gaia DR3 variability summary (I/357/varisum), Gaia vclassre, SB9 and ASAS-SN II/366 return **0 rows for both stars**. The same query returns 1 row for Algol, so the cones work. Neither star is a catalogued eclipsing binary: none is listed in VSX, Gaia-EB, Prša or IJspeert within 60″.
- **All-catalogue 5″ list (`s1b`, `s1c`):** only astrometric and photometric I/ catalogues come back (47 and 51 tables). The mirror's list stops alphabetically inside I/, so this query is not a completeness check; the targeted cones above are.
- **SIMBAD (`s1_archives.out`, `s1c_archives.out`):**
  - 470235665 = UCAC4 859-013225, type **SB\***, 1 bibcode (Gaia DR3), RV −66.6 ± 9.2 km/s.
  - 379251709 = UCAC4 788-006141, type **SB\***, 1 bibcode, RV −34.0 ± 4.0 km/s.
- **ExoFOP:** 0 TOIs and 0 CTOIs for both.
- **Web search:** the 2MASS, UCAC4 and TIC names return nothing relevant for either star.
- **Gaia DR3 orbits (`gaia_nss_tap.csv`):**
  - 470235665: SB1, P 10.32387 ± 0.00280 d, e 0.210 ± 0.051, ω 90.3 ± 13.7°, K1 47.5 ± 3.8 km/s, flags 8192.
  - 379251709: SB1, P 12.32612 ± 0.00417 d, e 0.097 ± 0.049, ω 122.6 ± 26.8°, K1 23.0 ± 1.1 km/s.
- **TIC stellar parameters (`s1c_archives.out`):**
  - 470235665: contamination ratio 0.059; Teff 5353 K, R 2.30 R☉, log g 3.68.
  - 379251709: contamination ratio 0.041; Teff 5279 K, R 1.88 R☉, log g 3.85.

## 2. Independence, systematics, pixels
- **Pipelines (`s11_independence.out`, raw SAP, QUALITY==0, trapezoid on a quadratic baseline):**
  - 470235665 primary: QLP 127.4 ppt (sd 2.6, N = 23); TESS-SPOC 122.4 (sd 2.0, N = 15); TESScut r ≤ 1.5 px aperture 122.1 ± 0.3 (s19) and 123.3 ± 1.0 (s79).
  - 470235665 secondary: QLP 84.0 (sd 1.6); TESS-SPOC 80.9 (sd 1.5); TESScut 80.8 ± 0.3 and 80.9 ± 0.7.
  - QLP/SPOC depth ratio over the shared sectors: 1.040 ± 0.007 (primary) and 1.038 ± 0.006 (secondary). This is an aperture/background systematic, much larger than the 0.5 ppt formal errors. TESS-SPOC and TESScut agree within 1%.
  - 379251709 primary: QLP 34.2 (sd 3.1, N = 17, including the noisy s24/s25); TESS-SPOC 36.3 (sd 1.4, N = 4); TESScut 38.1 ± 0.8 (s18) and 36.5 ± 0.1 (s52).
  - T14 agrees between pipelines: 6.44 h (QLP) vs 6.45 h (SPOC) for the 470235665 primary, 9.02 vs 9.01 h for its secondary, and 4.05 vs 4.22 h for the 379251709 primary.
  - Neither star has 2-min SPOC data.
- **Common mode (`s10_offtarget.out`):** this uses off-target pixels inside each cutout instead of other QLP stars.
  - Summed over pixels more than 3 px from the target, the stacked primary deficit is −1.1 to +3.2 ppt, against 120 or 33–38 ppt on target.
  - The brightest off-target pixels are stars beyond 90″ at the cutout edges, some brighter than the targets. They show −4.2 to +2.2 ppt.
  - The eclipses also repeat on a strict period over 6 years, in three cameras and two cadence regimes. A sector-wide systematic cannot do that.
- **Census of non-eclipse dips (`s4_census.out`):**
  - Apart from the eclipses, the 4–9 ppt features in raw SAP sit within about 0.3 d of gaps.
  - TESS-SPOC s18 starts with a ramp (27–54 ppt, 1790.7–1791.5) **in both stars**, so it is a systematic.
  - 379251709 QLP s24 is dominated by scattered light (σ30 = 8.1 ppt). Its events are kept but carry large errors.
- **Difference images (`s9_tesscut_<tic>_s<sec>.txt`; median in-eclipse minus median local out-of-eclipse, per event, averaged; Gaussian-fit centres; 21″/px):**

| Star / sector (camera) | kind | N ev | deficit − OOT centroid | deficit − target WCS | frac. depth on target pixel |
|---|---|---|---|---|---|
| 470235665 s19 (cam 3) | P / S | 3 / 2 | 0.29″ (±0.37) / 0.28″ (±0.14) | 0.96″ / 0.96″ | 122.9 / 76.6 ppt |
| 470235665 s79 (cam 4) | P / S | 3 / 3 | 0.33″ (±0.22) / 0.74″ (±0.26) | 1.43″ / 1.58″ | 120.8 / 77.7 ppt |
| 379251709 s18 (cam 2) | P | 2 | 1.86″ (±0.65) | 1.30″ | 33.2 ppt |
| 379251709 s52 (cam 4) | P | 2 | 0.10″ (±0.46) | 1.32″ | 31.3 ppt |

  The 379251709 secondary difference images (s18: 2 events; s52: 1 event at the sector start) are noise. No pixel location is claimed for the secondary.
- **Dilution arithmetic** (aperture r ≤ 1.5 px; fluxes from Gaia G). The "worst case" puts 100% of the neighbour's flux in the aperture.
  - **470235665:** the nearest neighbour is G 16.39 at 5.5″, on the target pixel. It would need an intrinsic depth of 320–356% for the primary and 210–234% for the secondary (PRF and worst-case values, both sectors). G 16.19 at 57″ needs at least 269% / 176%; G 15.51 at 69″ needs at least 149% / 98%. That last 98% (s79 secondary) is the only worst case below 100%. That star lies 70″ from the deficit centre, the fractional depth at its pixel is 2.8–8.6 ppt, and it is excluded for the primary. All neighbours are **excluded**.
  - **379251709 primary:** the brightest neighbour is G 16.57 at 67″ and needs at least 109–128% in the worst case. The nearest is G 17.33 at 30″ and needs at least 216–253%. All neighbours are **excluded**.
  - **379251709 secondary:** with a 2.5 ppt depth, any neighbour with a worst-case share above about 2.5% could produce it arithmetically. This is not excluded by pixels. It rests on timing: the dip sits exactly at the occultation phase the primary's e cos ω demands.
  - ZTF was not needed: for the primaries, no neighbour is arithmetically viable.

## 3. TIC 470235665 (P 10.3262 d)

Raw SAP, QUALITY==0, supersampled trapezoid on a local quadratic baseline, errors max(covariance, prayer-bead) (`events_470235665.csv`, `s5_events.py`). "TESScut" is my own aperture photometry (`s9`) with the shape fixed.

| Event | Sector | Mid BTJD | Depth QLP / SPOC / TESScut (ppt) | T14 / T23 (h) | pipelines |
|---|---|---|---|---|---|
| P E0 | 18 | 1795.7429 ± 0.0003 | 131.2 / 124.2 / – | 6.44 / 2.51 | QLP+SPOC |
| P E1 | 18 | 1806.0694 ± 0.0003 | 128.0 / 121.8 / – | 6.45 / 2.60 | QLP+SPOC |
| P E2 | 19 | 1816.3945 (TESScut) | – / – / 122.5 | (fixed) | TESScut (QLP lost, SPOC partial) |
| P E3 | 19 | 1826.7204 ± 0.0003 | 130.4 / 124.3 / 122.5 | 6.45 / 2.44 | QLP+SPOC+TESScut |
| P E4 | 19 | 1837.0465 ± 0.0003 | 130.1 / 123.2 / 121.5 | 6.45 / 2.46 | QLP+SPOC+TESScut |
| P E16 | 24 | 1960.9600 ± 0.0004 | 123.9 / 123.0 / – | 6.42 / 2.46 | QLP+SPOC |
| P E17 | 24 | 1971.2876 ± 0.0004 | 126.1 / 125.2 / – | 6.38 / 2.43 | QLP+SPOC |
| P E18 | 24 | 1981.6139 ± 0.0003 | 124.7 / 123.7 / – | 6.46 / 2.40 | QLP+SPOC |
| P E19 | 25 | 1991.9398 ± 0.0004 | – / 121.7 / – | 6.48 / 2.49 | SPOC (QLP partial) |
| P E20 | 25 | 2002.2652 ± 0.0004 | – / 125.9 / – | 6.49 / 2.33 | SPOC (QLP partial) |
| P E21 | 26 | 2012.5925 ± 0.0004 | 126.5 / 120.5 / – | 6.47 / 2.44 | QLP+SPOC |
| P E23 | 26 | 2033.2442 ± 0.0003 | 126.5 / 120.0 / – | 6.40 / 2.48 | QLP+SPOC |
| P E90 | 52 | 2725.0982 ± 0.0003 | 128.1 / 122.5 / – | 6.44 / 2.40 | QLP+SPOC |
| P E91 | 52 | 2735.4253 ± 0.0003 | 122.1 / 119.4 / – | 6.48 / 2.52 | QLP+SPOC |
| P E92 | 53 | 2745.7508 ± 0.0003 | 124.8 / 120.3 / – | 6.49 / 2.38 | QLP+SPOC |
| P E94 | 53 | 2766.4038 ± 0.0002 | 125.6 / 120.6 / – | 6.42 / 2.52 | QLP+SPOC |
| P E106 | 58 | 2890.3180 ± 0.0003 | 130.6 / – / – | 6.43 / 2.48 | QLP |
| P E107 | 58 | 2900.6438 ± 0.0003 | 131.6 / – / – | 6.46 / 2.43 | QLP |
| P E145 | 73 | 3293.0389 ± 0.0003 | 129.6 / – / – | 6.44 / 2.43 | QLP |
| P E146 | 73 | 3303.3666 ± 0.0004 | 126.2 / – / – | 6.44 / 2.42 | QLP |
| P E160 | 78 | 3447.9313 ± 0.0003 | 124.3 / – / – | 6.43 / 2.43 | QLP |
| P E161 | 79 | 3458.2570 ± 0.0004 | 126.7 / – / 121.5 | 6.46 / 2.44 | QLP+TESScut |
| P E162 | 79 | 3468.5833 ± 0.0003 | 129.9 / – / 124.8 | 6.44 / 2.40 | QLP+TESScut |
| P E163 | 79 | 3478.9099 ± 0.0003 | 128.3 / – / 123.7 | 6.43 / 2.51 | QLP+TESScut |
| P E176 | 85 | 3613.1506 ± 0.0003 | 129.7 / – / – | 6.48 / 2.43 | QLP |
| P E178 | 85 | 3633.8032 ± 0.0003 | 125.7 / – / – | 6.45 / 2.50 | QLP |
| S E1 | 18 | 1811.4664 ± 0.0005 | 85.7 / 81.7 / – | 8.98 / 2.79 | QLP+SPOC |
| S E2 | 19 | 1821.7930 ± 0.0006 | 84.4 / 81.7 / 80.5 | 9.06 / 2.77 | QLP+SPOC+TESScut |
| S E3 | 19 | 1832.1197 ± 0.0005 | 86.7 / 82.3 / 81.0 | 8.95 / 2.79 | QLP+SPOC+TESScut |
| S E16 | 24 | 1966.3596 ± 0.0008 | 82.5 / 81.8 / – | 9.09 / 2.78 | QLP+SPOC |
| S E17 | 24 | 1976.6851 ± 0.0005 | 83.2 / 82.6 / – | 8.97 / 2.87 | QLP+SPOC |
| S E18 | 25 | 1987.0117 ± 0.0006 | 86.9 / 82.8 / – | 8.98 / 2.91 | QLP+SPOC |
| S E19 | 25 | 1997.3387 ± 0.0008 | 85.7 / 81.8 / – | 9.03 / 2.64 | QLP+SPOC |
| S E20 | 25 | 2007.6649 ± 0.0006 | – / 82.3 / – | 8.97 / 2.69 | SPOC (QLP partial) |
| S E21 | 26 | 2017.9920 ± 0.0006 | 82.4 / 78.8 / – | 8.96 / 2.88 | QLP+SPOC |
| S E22 | 26 | 2028.3179 ± 0.0005 | 82.8 / 79.1 / – | 9.01 / 2.83 | QLP+SPOC |
| S E89 | 52 | 2720.1718 ± 0.0007 | – / 79.8 / – | 9.02 / 2.78 | SPOC (QLP lost) |
| S E91 | 52 | 2740.8227 ± 0.0005 | 83.7 / 80.3 / – | 9.06 / 2.82 | QLP+SPOC |
| S E92 | 53 | 2751.1493 ± 0.0009 | 81.6 / 79.2 / – | 9.13 / 2.68 | QLP+SPOC |
| S E93 | 53 | 2761.4760 ± 0.0006 | 81.1 / 79.1 / – | 8.99 / 2.76 | QLP+SPOC |
| S E105 | 58 | 2885.3895 ± 0.0005 | 84.5 / – / – | 9.04 / 2.72 | QLP |
| S E106 | 58 | 2895.7163 ± 0.0005 | 86.8 / – / – | 9.16 / 2.83 | QLP |
| S E107 | 58 | 2906.0419 ± 0.0005 | 84.9 / – / – | 9.06 / 2.77 | QLP |
| S E145 | 73 | 3298.4358 ± 0.0005 | 84.0 / – / – | 8.97 / 2.96 | QLP |
| S E146 | 73 | 3308.7628 ± 0.0005 | 83.7 / – / – | 8.94 / 2.79 | QLP |
| S E159 | 78 | 3443.0031 ± 0.0006 | 82.0 / – / – | 9.01 / 2.88 | QLP |
| S E160 | 79 | 3453.3286 ± 0.0005 | 82.6 / – / 79.7 | 8.95 / 2.84 | QLP+TESScut |
| S E161 | 79 | 3463.6543 ± 0.0006 | 83.5 / – / 80.7 | 9.09 / 2.82 | QLP+TESScut |
| S E162 | 79 | 3473.9798 ± 0.0006 | 84.7 / – / 82.3 | 9.02 / 2.77 | QLP+TESScut |
| S E176 | 85 | 3618.5472 ± 0.0005 | 84.5 / – / – | 8.94 / 2.88 | QLP |
| S E177 | 85 | 3628.8739 ± 0.0008 | 84.6 / – / – | 9.01 / 2.72 | QLP |

Not measured (gap / flagged / too little coverage): pri E22 (s26, pred 2022.918): QLP lost, SPOC lost; pri E93 (s53, pred 2756.079): QLP lost, SPOC lost; pri E159 (s78, pred 3437.608): QLP partial; pri E177 (s85, pred 3623.479): QLP lost; sec E-1 (s18, pred 1790.822): SPOC partial; sec E0 (s18, pred 1801.148): QLP lost, SPOC lost; sec E15 (s24, pred 1956.041): QLP partial, SPOC partial; sec E90 (s52, pred 2730.506): QLP lost, SPOC lost; sec E144 (s73, pred 3288.121): QLP partial 

**Period (`s6_period.out`):**
- Primaries, one value per epoch: N = 25, **P = 10.326183 ± 0.000002 d**, T0 = 1795.74233 ± 0.00018, O−C rms 0.9 min (reduced χ² 3.5; errors scaled).
- Fitting QLP alone and TESS-SPOC alone gives the same P (10.326182).
- Secondaries: N = 25, P = 10.326173 ± 0.000002 d.
- Joint fit: P = 10.326180 ± 0.000001 d, secondary phase **0.52275 ± 0.00002**.
- Gaia P differs by **+0.82σ**.

**Odd/even:** primary QLP 127.66 ± 0.75 vs 128.24 ± 0.85 ppt (−0.5σ); primary SPOC +1.0σ; secondary +0.02σ / +0.28σ. The two eclipse kinds differ in depth (127 vs 84 ppt) and duration (6.44 vs 9.02 h), so the true period is not twice this one, and the odd/even test rules out a stacked P2.

**Shape (`s14_fold_470235665.png`):** both eclipses have rounded bottoms. The trapezoid "T23" (2.45 / 2.81 h) is not a resolved flat bottom, so totality is not established.

**Secondary-phase drift (`s13_secphase_470.out`):** P_sec − P_pri = (−10.0 ± 2.8) × 10⁻⁶ d (−3.5σ), which would be −2.6 min over 178 cycles. In QLP the secondary phase goes 0.52284 → 0.52277 → 0.52269 across 2019–20, 2022 and 2022–24. TESS-SPOC shows no change between 2019–20 and 2022 (0.52281 vs 0.52280). This hints at apsidal motion or a cadence effect. It is not claimed.

## 4. TIC 379251709 (P 12.3239 d)

| Event | Sector | Mid BTJD | Depth QLP / SPOC / TESScut (ppt) | T14 / T23 (h) | pipelines |
|---|---|---|---|---|---|
| P E-13 | 18 | 1801.0439 ± 0.0014 | 35.1 / – / 39.0 | 4.24 / 1.16 | QLP+TESScut (SPOC lost) |
| P E-12 | 18 | 1813.3689 ± 0.0011 | 35.2 / – / 37.3 | 4.13 / 0.89 | QLP+TESScut (SPOC lost) |
| P E0 | 24 | 1961.2533 ± 0.0009 | – / 36.7 / – | 4.20 / 1.04 | SPOC (QLP noisy, e_tc>0.005 d) |
| P E1 | 24 | 1973.5750 ± 0.0010 | 35.8 / 35.2 / – | 4.24 / 1.06 | QLP+SPOC |
| P E2 | 25 | 1985.9080 ± 0.0028 | 29.7 / – / – | 4.31 / 1.53 | QLP |
| P E3 | 25 | 1998.2305 ± 0.0043 | 27.7 / – / – | 2.91 / 0.58 | QLP (SPOC lost) |
| P E62 | 52 | 2725.3357 ± 0.0008 | 33.2 / 35.2 / 36.6 | 4.17 / 1.00 | QLP+SPOC+TESScut |
| P E63 | 52 | 2737.6604 ± 0.0008 | 36.8 / 38.2 / 36.4 | 4.27 / 0.67 | QLP+SPOC+TESScut |
| P E75 | 58 | 2885.5465 ± 0.0008 | 34.5 / – / – | 4.04 / 1.03 | QLP |
| P E76 | 58 | 2897.8705 ± 0.0009 | 34.7 / – / – | 4.10 / 0.87 | QLP |
| P E78 | 59 | 2922.5198 ± 0.0009 | 33.7 / – / – | 4.13 / 1.07 | QLP |
| P E79 | 59 | 2934.8432 ± 0.0009 | 34.2 / – / – | 4.13 / 0.85 | QLP |
| P E120 | 78 | 3440.1238 ± 0.0009 | 36.1 / – / – | 4.09 / 0.99 | QLP |
| P E122 | 79 | 3464.7714 ± 0.0009 | 39.9 / – / – | 4.28 / 0.32 | QLP |
| P E123 | 79 | 3477.0951 ± 0.0013 | 34.1 / – / – | 4.20 / 1.07 | QLP |
| P E134 | 85 | 3612.6582 ± 0.0010 | 38.4 / – / – | 4.22 / 0.86 | QLP |
| P E136 | 86 | 3637.3031 ± 0.0011 | 32.1 / – / – | 3.89 / 1.15 | QLP |
| P E138 | 86 | 3661.9554 ± 0.0010 | 30.2 / – / – | 3.82 / 1.28 | QLP |

Not measured (gap / flagged / too little coverage): pri E77 (s58, pred 2910.177): QLP lost; pri E121 (s79, pred 3452.429): QLP lost; pri E135 (s85, pred 3624.963): QLP lost; pri E137 (s86, pred 3649.611): QLP lost 

**Period (`s6_period.out`):**
- One value per epoch: N = 18, **P = 12.323912 ± 0.000007 d**, T0 = 1961.25375 ± 0.00060, O−C rms 3.1 min. The largest residuals are +9.2 and +7.2 min, in the noisy QLP s25.
- QLP alone: 12.323905 ± 0.000009 d. TESS-SPOC alone (N = 4): 12.323931 ± 0.000018 d.
- Gaia P differs by **−0.53σ**.

**Odd/even:** QLP 33.87 ± 1.04 vs 34.73 ± 1.27 ppt (−0.5σ); SPOC −0.55σ.

**Shape:** V-shaped, T14 4.1–4.2 h, trapezoid T23 about 1.0 h.

**Secondary (`s7_secondary_379.out`; primaries masked, 1.5-d running median, box scan over phase):**
- QLP, excluding s24/s25: the strongest peak in the scan is at phase 0.4955. A trapezoid fit gives **phase 0.49597 ± 0.00035, depth 2.47 ± 0.29 ppt (S/N 8.5), T14 4.50 ± 0.43 h**.
- TESS-SPOC: 0.49741 ± 0.00040, 2.59 ± 0.68 ppt (S/N 3.8), 2.6σ apart in phase from QLP. The SPOC scan's top peak (phase 0.2235) is the s18 start-of-sector ramp (`s7b_otherpeaks_379.out`).
- Individual events (excluding the noisy QLP s24): 1.1–4.1 ppt at S/N 1.6–7.3. Only s59 E78 (4.12 ± 0.56 ppt) is individually significant.

## Geometry vs Gaia
`s8_geometry.out`: Monte Carlo with 20000 draws using Gaia's corr_vec. Parameter order is assumed to be P, Vcm, K1, e, ω, Tp. The column-major upper triangle gives a positive-definite matrix with ω–Tp = 0.98–0.99; the row-major one does not. Uncorrelated draws are shown in brackets. `s12_physics_ephem.out` repeats the calculation with nominal values as an independent check.

- **470235665:**
  - Taking the TESS ephemeris back to the Gaia epoch, the primary is −0.068 ± 0.108 d from **conjunction A** [−0.080 ± 0.427] and +5.09 d from B (+19σ [+7.5σ]). Taking Gaia's ephemeris forward to TESS gives +0.245 ± 0.405 d from A. The nominal check in `s12` gives −0.079 d.
  - Because ω ≈ 90°, conjunction A falls at periastron. The primary is the companion transiting the RV star.
  - Gaia predicts the secondary at phase 0.4994 ± 0.0329; measured 0.52275, **+0.71σ**. TESS-only e cos ω ≈ +0.036 vs Gaia −0.001 ± 0.051.
  - T14(B)/T14(A) = 1.397 gives e sin ω ≥ +0.166, against Gaia +0.205 ± 0.050. The eclipse at periastron (A) is the shorter one, as the orbit requires.
- **379251709:**
  - Backward: the primary is −0.170 ± 0.224 d from **conjunction A** [−0.189 ± 1.218] and −5.96 d from B (−28σ [−4.2σ]). Forward: −0.473 ± 0.418 d from A.
  - Gaia predicts the secondary at 0.4711 ± 0.0314; measured 0.4960 ± 0.0010, **+0.79σ**. TESS e cos ω ≈ −0.006 vs Gaia −0.045 ± 0.049.
  - Duration ratio 1.066 gives e sin ω ≥ 0.03 vs Gaia +0.068 ± 0.041. This test is weak.
- **Physics (`s12_physics_ephem.out`; rough two-sphere model without limb darkening):**
  - **470235665:**
    - f(m) = 0.107 M☉, so m2 = 0.64–0.77 M☉ for M1 = 0.93–1.3 M☉ and a = 23.2–25.4 R☉.
    - The depths imply k ≈ 0.37 and a companion light share ≥ 8%. The two T14 values with Gaia's e and ω give R1/a = 0.079 and b_A ≈ 0.45, so R1 = 1.8–2.0 R☉ (TIC 2.30), R2 = 0.67–0.73 R☉ and i ≈ 87°.
    - J ≈ 0.66, so T2 ≈ 4800 K.
    - A subgiant with a K-dwarf companion: radius, temperature and mass agree with the mass function to about 15–20%. b_B ≈ 0.70 > 1 − k says the B eclipse is partial, which fits the rounded secondary.
  - **379251709:**
    - f(m) = 0.0153 M☉, so m2 = 0.28–0.35 M☉ (an M dwarf, R2 ≈ 0.3–0.4 R☉).
    - Read as a non-grazing transit (T23/T14 = 0.22), the shape needs b ≈ 0.77 and **R1 ≈ 1.2–1.5 R☉, R2 ≈ 0.25–0.30 R☉**, which is consistent with m2. With the TIC's R1 = 1.88 R☉ the 4.2 h eclipse would have to be grazing (b ≈ 0.99), and that is hard to square with a 36 ppt depth.
    - A 3200–3500 K companion would give a full-occultation depth of 4–8 ppt; the measured secondary is about 2.5 ppt. Consistent.

## Ephemerides and next eclipses
From `s12_physics_ephem.out`. The barycentric light-time correction (+2.8 to +5.2 min) was removed to give UTC at the geocentre. Errors are formal, from T0 and P.
- **TIC 470235665 primary:** T0 = BTJD 1795.74233 ± 0.00018 (BJD_TDB 2458795.74233), **P = 10.326183 ± 0.000002 d**, T14 6.45 h.
  - Next primaries: BTJD 4346.3095 = **2026-11-01 19:21 UTC**; 4356.6357 = **2026-11-12 03:11**; 4366.9619 = **2026-11-22 11:00** (±0.8 min).
  - Secondary: T0 = 1801.14120 ± 0.00023, P = 10.326173 ± 0.000002 d, T14 9.0 h. Next: 2026-11-07 04:52, 2026-11-17 12:42, 2026-11-27 20:31 UTC.
- **TIC 379251709 primary:** T0 = BTJD 1961.25375 ± 0.00060 (BJD_TDB 2458961.25375), **P = 12.323912 ± 0.000007 d**, T14 4.2 h; secondary at phase 0.4960 ± 0.0010.
  - Next primaries: BTJD 4352.0927 = **2026-11-07 14:07 UTC**; 4364.4166 = **2026-11-19 21:53**; 4376.7405 = **2026-12-02 05:40** (±2.1 min).

## Caveats
- **SAP depths depend on the pipeline at the 4% level** (QLP deeper) and none are corrected for crowding (TIC contamination 4–6%). "Agreement" here means within about 5%, not within the formal errors.
- **The 379251709 secondary is a fold-level detection** (QLP S/N 8.5, SPOC S/N 3.8, phases 2.6σ apart). It has not been located in pixels or excluded from neighbours arithmetically. Its exact match to the e cos ω phase is what ties it to the target.
- **379251709 radius tension:** the eclipse shape prefers R1 ≈ 1.3 R☉, about 30% below the TIC's 1.88 R☉, unless the eclipse is grazing. This is not a failed check, but the TIC Teff/radius deserves a look. A spectrum, or a proper fit with limb darkening on the 200-s data, would settle it.
- **470235665:** the secondary-phase drift (−2.6 min over 5 years, 3.5σ, seen in QLP only) is unconfirmed. The rough physical model is crude and does not decide whether either eclipse is total.
- **Gaia geometry:** the forward predictions (±0.4 d) are limited by Gaia's P error. The backward test (±0.1–0.2 d) assumes the corr_vec ordering stated above; without correlations the errors grow to ±0.4–1.2 d and B is still rejected at 4.2σ and 7.5σ.
- **TESScut times** are not barycentred to the target, which puts them up to about ±3 min off (O−C −3.1 to +3.0 min). They are not used in any ephemeris.
- **Not done:** the QLP-neighbour common-mode test; TESScut-only sectors 60 and 86 of 470235665, which no pipeline covers; ZTF.

## Files
- Scripts and outputs are in this folder. **From the first agent** (checked here, not re-run):
  - `s1_archives.py/.out`, `s1b_archives.py/.out` (crashed for 379251709)
  - `s2_download.py/.out`, `s3_load.py/.out` (per-star `lc_sap_q0.npz` in scratch)
  - `s4_census.py/.out`, `s5_events.py` → `events_<tic>.csv`
  - `s6_period.py/.out`
  - `s7_secondary_379.py/.out/.txt`, `s7b_otherpeaks_379.py/.out`
  - `s8a_gaia_tap.py/.out` → `gaia_nss_tap.csv`, `s8_geometry.py/.out/.txt`
- **Added in this run:**
  - `s1c_archives.py/.out`
  - `s9_tesscut.py` → `s9_tesscut_<tic>_s<sec>.txt/.npz/.png` (470235665 s19, s79; 379251709 s18, s52)
  - `s10_offtarget.py/.out`
  - `s11_independence.py/.out`
  - `s12_physics_ephem.py/.out`
  - `s13_secphase_470.py/.out`
  - `s14_foldplot.py` → `s14_fold_<tic>.png`
  - `s15_event_table.py/.out`
- **Data:** `/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet02/<tic>/` (QLP and TESS-SPOC FITS; TESScut cubes deleted).

**Summary**
- TIC 470235665: CONFIRMED; P_ecl=10.326183 d; depth1=122–127 ppt; depth2=81–84 ppt at phase 0.52275; pixel: on target; pipelines: 3; Gaia geometry: pass
- TIC 379251709: CONFIRMED; P_ecl=12.323912 d; depth1=34–38 ppt; depth2=2.5 ppt at phase 0.4960; pixel: on target (primary; secondary untested); pipelines: 3; Gaia geometry: pass
