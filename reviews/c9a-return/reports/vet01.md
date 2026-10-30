# vet01: adversarial check of TIC 195865529 (ATO J310.7264+43.3062) and TIC 468181994 (UCAC4 023-009594)

Opus 5.5 subagent, 2026-10-30, for Fable 5.1. A first agent ran `s1`–`s8a` and was killed by a container restart. This run kept its downloads and outputs, checked its logs and continued with `s8`–`s17`. Everything is in `[local path omitted]`. Downloads are in the scratchpad at `data/vet01/<tic>/`; the TESScut cubes were deleted after use. Depths are in ppt, times in BTJD (BJD_TDB − 2457000), durations in hours. A = conjunction at ν = 90° − ω, when the companion is in front of Gaia's RV star. B = ν = 270° − ω.

**TIC 195865529: CONFIRMED.** A detached F-star + K-dwarf eclipsing binary at the Gaia period. It is already a catalogued EB in ASAS-SN (II/366, EA, P = 3.8310 d) and ATLAS (class DBH at P/2), though not in VSX.
- (1) Individual events: 48 primaries and 49 secondaries were re-measured one by one from raw QLP SAP (QUALITY==0). Another 3 primaries were fitted but excluded as partial.
- (2) Period: P_ecl = 3.8310456 ± 0.0000009 d, which is −0.15σ from Gaia's.
- (3) Pixels: the deficit is on the target in all 8 sectors, across 4 camera/CCD orientations. Every Gaia neighbour within 90″ is excluded by the pixels. The dilution arithmetic alone excludes all but one: the G 13.46 star at 36″ would need ≈ 100%.
- (4) Independence: QLP SAP, my TESScut aperture and TASOC agree after correcting for each aperture's dilution: undiluted primary 183 / 192 / 196 ppt, secondary 48 / 51 / 47 ppt.
- (5) Geometry: the primary is conjunction A (A within 0.18σ, B excluded at 3.3–3.9σ). The secondary sits at phase 0.49999 ± 0.00007; Gaia's e and ω predict 0.479 ± 0.024 (+0.87σ).
- The screen was right about depths (≈ 185 / 48 ppt), phases and period. Those depths are on QLP's apparently deblended scale, though. Raw apertures see the same eclipse diluted: 127–144 ppt in my r = 1.5 px aperture and 71 ppt in TASOC, whose header gives 64% contamination.

**TIC 468181994: CONFIRMED.** This is the weaker of the two; see the caveats. A late-F/G star with an M-dwarf-mass companion (m2 sin i ≈ 0.21–0.24 M☉). It is not in VSX, Gaia-EB, Prša or IJspeert within 60″.
- (1) Individual events: 37 primaries were re-measured individually in QLP SAP (one more was excluded as partial), plus 7 in TESScut sector 66, which QLP does not cover. The 1.3 ppt secondary was measured at fixed shape in 39 windows: 37 are positive and 28 are above 2σ.
- (2) Period: P_ecl = 3.9969190 ± 0.0000006 d, which is **−2.31σ** from Gaia's 3.999219 ± 0.000996 d. This is the weakest link.
- (3) Pixels: the 2.85″ neighbour (G 16.75) cannot be excluded by arithmetic (it would need 73% primary and 4.1% secondary depths). The difference images reject it: the mean centroid over 8 sectors lies 0.51″ from the target and 3.2″ from the neighbour (≈ 16σ), and the PSF χ² prefers the target in every sector. Every other G < 18 neighbour is excluded by arithmetic.
- (4) Independence: QLP SAP, my TESScut aperture and ELEANOR-lite agree, at 21–24 ppt per sector.
- (5) Geometry: the secondary sits at phase 0.4956 ± 0.0012, and Gaia predicts 0.534 ± 0.040 (A) or 0.466 ± 0.040 (B), both within 1σ. Propagated forward with Gaia's P, the primary's absolute phase does not decide between A and B (1.2σ vs 0.7σ). Propagated back with the eclipse P, A is preferred (0.01σ vs 2.2σ).
- The screen was right (≈ 23 ppt, ≈ 1.5 ppt near 0.5, P 3.9969 d). The secondary is measurably *before* phase 0.5, at 0.4956. Its depth is 1.24–1.41 ppt.
- Gaia shows RUWE 12.6 and ipd_frac_multi_peak = 39%: probably an unresolved sub-arcsecond companion, which TESS pixels cannot test.

## 1. Archives and web
- **Cones** (`s2_archives.out`, `s2b_archives.out`; the VizieR mirror was sanity-checked on Algol, which returned β Per):
  - 195865529:
    - VSX (60″): only `Gaia DR3 2066587835904958592`, type YSO, 15.34–15.39 mag, at **35.76″**. That is the G 15.36 neighbour, not the target.
    - Not in Prša+2022, IJspeert+2021, Gaia DR3 VEB (I/358/veb), Gaia varisum (10″) or SB9.
    - **ASAS-SN II/366 at 0.16″: ASASSN-V J204254.34+431822.5, Type EA, Per 3.8310 d, Amp 0.12 mag, Prob 1.000.**
    - **ATLAS J/AJ/156/241 at 0.09″: class DBH (P(DBH) = 0.98), period 1.915571 d (= P/2).**
    - **So it is already a catalogued eclipsing binary**, though not in VSX.
  - 468181994: no rows in VSX, J/ApJS/258/16, J/A+A/652/A120, I/358/veb, I/357/varisum, B/sb9, ATLAS or ASAS-SN II/366 (radii 10–60″, as listed in the scripts).
  - The all-catalogue 5″ query returned only astrometric/photometric tables (I/…) for both stars.
- **SIMBAD (harvard mirror, 10″ cone):** both are type SB*, with 1 bibcode each: ATO J310.7264+43.3062 and UCAC4 023-009594. "TIC <id>" is not a SIMBAD identifier for either star (`s2c_simbad_raw.out`).
- **ExoFOP:** tois = [], ctois = [] for both.
- **WebSearch** on all names: nothing mentions either star (`s15_websearch.out`).
- **Gaia DR3 extras** (`s10_gaia_extra.out`):
  - 195865529: RUWE 0.94, ipd_frac_multi_peak 0, rv_amplitude_robust 147 km/s (2K1 = 132), Teff_gspphot 6608 K, FLAME R = 2.03 R☉, M = 1.50 M☉.
  - 468181994: **RUWE 12.57, astrometric_excess_noise 1.53 mas (sig 2803), ipd_frac_multi_peak 39**, rv_amplitude_robust 52.9 km/s (2K1 = 44.7), Teff_gspphot 5775 K, logg 4.08, FLAME R = 2.91 R☉ (FLAME uses the gspphot distance of 608 pc; the parallax distance is 1044 pc).
  - The 2.85″ neighbour 6342991943947141504: G 16.75, BP−RP 1.51, parallax 1.717 ± 0.048 mas, RUWE 1.10.
  - The NSS orbit rows match targets.csv. conf_spectro_period = 1.0 for both.

## 2. Independence, systematics, pixels
- **Pipelines available.** Neither star has TESS-SPOC FFI light curves or 2-min SPOC data (`s1_download_lc.out`).
  - 195865529: QLP s15/41/55/56/75/76/82/83, plus TASOC for s15.
  - 468181994: QLP s12/13/27/39/67/93/94, plus GSFC-ELEANOR-LITE for s12/13. TESScut covers s66, where QLP has nothing.
  - My own photometry: an 11×11 TESScut cube per sector. Background = per-cadence median of the faintest 20% of pixels; aperture r = 1.5 px (6–8 px); QUALITY == 0 (`s8_pixels.py`).
- **Depth method.** One method for every pipeline (`s11_depths.out`): ephemeris and shape fixed, a quadratic baseline per event, and an exposure-supersampled trapezoid amplitude.

| TIC 195865529 primary / secondary (ppt) | s15 | s41 | s55 | s56 | s75 | s76 | s82 | s83 |
|---|---|---|---|---|---|---|---|---|
| QLP SAP | 182.0 / 49.2 | 186.2 / 48.2 | 182.5 / 46.7 | 182.2 / 46.9 | 184.3 / 49.2 | 183.8 / 48.3 | 182.4 / 48.4 | 181.9 / 47.6 |
| TESScut ap., raw | 141.2 / 38.6 | 134.7 / 36.0 | 143.1 / 37.4 | 127.4 / 33.5 | 140.9 / 38.1 | 143.0 / 38.8 | 129.6 / 34.3 | 143.5 / 38.0 |
| TESScut ÷ target fraction | 183.3 / 50.2 | 188.1 / 50.3 | 194.4 / 50.8 | 197.4 / 51.9 | 187.2 / 50.6 | 186.0 / 50.5 | 204.2 / 54.1 | 197.5 / 52.3 |
| TASOC raw (AP_CONT 0.637) | 71.3 / 16.9 → undiluted 196.2 / 46.5 | | | | | | | |

  - Typical errors are 0.3–0.9 ppt.
  - In `s12_dilution.out`, the target's flux fraction in my aperture is 0.635–0.770 from TIC Tmag and the fitted PSF width, and 0.585–0.803 from the fitted scene.
  - Undiluted TESScut depths: mean primary 192.3 (sd 7.2), secondary 51.3 (sd 1.4), S/P 0.267. QLP: 183.2 (sd 1.5) / 48.1 (sd 0.9), S/P 0.262.
  - So QLP SAP behaves as if it were deblended with the TIC contamination ratio (0.367). The TESScut and TASOC numbers agree with it to ≈ 5%, which is the accuracy of my Gaussian-PSF dilution model. Depth *ratios* agree to 2%.
  - Note: the raw aperture depths of this star are not comparable across pipelines without that correction.
- **TIC 468181994 primary (ppt):**
  - QLP SAP: 21.0, 22.3, 23.7, 23.2, —, 23.0, 23.3, 21.2.
  - TESScut: 22.3, 21.8, 21.9, 22.3, 22.3 (s66), 22.4, 22.8, 22.0.
  - ELEANOR-lite raw: 24.3 (s12), 22.7 (s13). ELEANOR-lite corr: 23.4, 22.4.
  - These are sectors 12, 13, 27, 39, 66, 67, 93, 94. The target fraction in my aperture is 0.952–0.960.
  - Secondary per sector: QLP 1.07–1.55, TESScut 0.96–2.28 (s67 ± 0.98), ELEANOR-lite 0.94–1.61, all with errors of 0.16–0.46.
  - All pipelines agree within about 2σ.
- **Difference images** (`s8_pixels_*.out`, `s9_pixsummary.out`). Each is the median out-of-eclipse frame minus the median in-eclipse frame, primaries only. 50 primaries per star went into the stacks, covering all 8 sectors of each. A free-position Gaussian PSF was fitted, and the zero point is a scene model of the out-of-eclipse image (TIC stars with T < 17). Errors come from bootstrapping over events. Two single-event difference images per sector are also listed.
  - **195865529:**
    - Per-sector offsets from the target: 1.2–4.3″. Single events: 1.0–4.3″. Sector mean (+0.20 ± 0.57, +1.37 ± 0.91)″.
    - The nearest G < 18 neighbour is 18.9″ away. The difference centroid lies 17–23″ from it (≥ 101σ in every sector) and 32–40″ from the 33–36″ group.
    - PSF hypothesis χ²: the target is best in all 8 sectors. The next best, the 18.8″ star, is worse by Δχ² ≥ 16,096.
    - Arithmetic, as the depth each star would need: the G 13.46 star at 36.0″ has a maximum flux fraction of 18.0%, so it would need 101.6% (primary) and 26.5% (secondary). It is excluded only marginally by arithmetic, but cleanly by pixels. Every other G < 18 neighbour within 90″ would need ≥ 393%.
    - The TIC's T 18.3 star at 10.7″ (G 19.5) contributes about 0.1% and is irrelevant.
  - **468181994:**
    - Per-sector offsets: 0.41–1.53″. Mean (+0.50 ± 0.20, −0.12 ± 0.19)″, error from the scatter between sectors.
    - The 2.85″ neighbour is at (−1.67, +2.22)″. Per sector, the difference centroid is 2.3–3.8″ from it (7–24σ); the mean is ≈ 3.2″, or ≈ 16σ.
    - PSF hypothesis Δχ² (neighbour minus target): +119, +190, +184, +230, +58, +14, +44, +256, so the target is preferred in all 8 sectors.
    - Arithmetic: the neighbour's flux fraction is 3.0–3.1%, so it would need **73.3% / 4.1%**, which arithmetic cannot exclude. All others (44–86″) would need ≥ 293% for the primary.
    - Figures: `fig_468181994.png` and `fig_195865529.png` (out-of-eclipse image, difference image, raw fold). In both, the difference image peaks on the target pixel.
- **Common mode:** not done with other QLP stars. A dip that repeats strictly on one ephemeris across 8 sectors over 6 years, and whose per-pixel difference image follows the target PSF only, is not a sector-wide systematic.
- **Blind period search** on raw SAP (`s4_period_search.out`, BLS 0.5–20 d): the best peaks are 3.83107 d and 3.99694 d. The other peaks are aliases (P/2, 2P, 3P, 4P).

## 3. TIC 195865529 (P 3.831 d)
Raw QLP SAP, QUALITY==0. Each event is fitted with a trapezoid times a quadratic baseline, with red-noise β-scaled errors (`s6_events.out`). Summary per sector (`s17_tables.out`); every event is listed in `events_table_195865529.md`.

| Event | Mid BTJD (range) | Depth (ppt, mean / sd) | T14 / T23 (h) | pipelines |
|---|---|---|---|---|
| P s15 ×4 (lost: 1721.87, 1733.36, 1737.19 flagged) | 1714.199–1729.524 | 182.0 / 0.6 | 5.19 / 2.18 | QLP, TESScut, TASOC |
| P s41 ×6 (lost 2442.10) | 2422.946–2445.932 | 186.4 / 1.1 | 5.23 / 2.15 | QLP, TESScut |
| P s55 ×6 (lost 2809.88) | 2798.388–2821.374 | 182.5 / 0.9 | 5.23 / 2.16 | QLP, TESScut |
| P s56 ×7 (lost 2825.21) | 2829.037–2852.023 | 181.7 / 1.0 | 5.23 / 2.18 | QLP, TESScut |
| P s75 ×6 (partial 3346.23) | 3342.396–3365.382 | 184.1 / 2.4 | 5.20 / 2.16 | QLP, TESScut |
| P s76 ×6 (partial 3388.37) | 3369.213–3392.199 | 183.2 / 1.5 | 5.22 / 2.17 | QLP, TESScut |
| P s82 ×6 (partial 3545.44) | 3533.948–3556.934 | 182.4 / 0.7 | 5.24 / 2.15 | QLP, TESScut |
| P s83 ×7 | 3560.766–3583.752 | 181.8 / 1.0 | 5.20 / 2.15 | QLP, TESScut |
| S s15 ×4 (3 flagged) | 1712.285–1731.440 | 48.9 / 1.2 | 5.34 / 2.53 | QLP, TESScut, TASOC |
| S s41 ×6, s55 ×7, s56 ×6 | 2421.033–2850.108 | 48.0, 46.4, 46.8 | 5.23–5.29 / 2.44–2.53 | QLP, TESScut |
| S s75 ×8, s76 ×7, s82 ×6, s83 ×5 | 3340.481–3581.835 | 49.4, 48.0, 48.4, 47.3 | 5.22–5.29 / 2.42–2.53 | QLP, TESScut |

- **Ephemeris and O−C** (`s7_ephem.out`): 48 primaries give P = 3.8310456 ± 0.0000009 d and T0 = 3346.226971 ± 0.000140. Red. χ² is 9.43 (errors scaled) and the O−C rms is 1.31 min; sector means lie between −3.4 and +1.8 min.
- **Secondaries:** P = 3.8310460 ± 0.0000013 (P_sec − P_prim = +0.0000004 ± 0.0000015). Phase **0.49999 ± 0.00007**, so e cos ω = −0.00002 ± 0.00010. The durations are equal (T14 5.22 vs 5.25 h), so e sin ω ≈ 0 as well. The orbit is circular.
- **Comparison with Gaia:** P_ecl − P_Gaia = −0.000058 d = −0.15σ.
- **Odd/even primaries:**
  - Raw: 182.72 ± 0.21 vs 183.04 ± 0.24 ppt. Sector-normalised: 0.9985 ± 0.0011 vs 1.0021 ± 0.0013 (−2.0σ, driven by the depth differences between sectors).
  - Odd/even secondaries: 47.81 ± 0.19 vs 47.60 ± 0.18.
  - A distinct 48 ppt secondary at phase 0.5 rules out 2P and P/2.

## 4. TIC 468181994 (P 3.997 d)
Same method (`s6_events.out`). Every primary is listed in `events_table_468181994.md`; the individual secondaries at fixed phase and shape are in `s7b_sec468.out`.

| Event | Mid BTJD (range) | Depth (ppt, mean / sd) | T14 / T23 (h) | pipelines |
|---|---|---|---|---|
| P s12 ×4 (lost 1624.89 gap, 1628.89 and 1640.88 flagged) | 1632.882–1648.870 | 21.1 / 0.5 | 3.73 / 2.40 | QLP, TESScut, ELEANOR-lite |
| P s13 ×5 (1660.86, 1664.86 partial) | 1656.865–1680.846 | 22.1 / 1.6 | 3.68 / 2.32 | QLP, TESScut, ELEANOR-lite |
| P s27 ×5 (2048.56 gap, 2060.55 partial) | 2036.572–2056.556 | 24.0 / 1.4 | 3.66 / 2.39 | QLP, TESScut |
| P s39 ×6 (2368.32 flagged in QLP; clean in TESScut) | 2364.320–2388.300 | 23.2 / 1.8 | 3.66 / 2.42 | QLP, TESScut |
| P s66 ×7 (TESScut only) | 3099.752–3123.734 (predicted) | 21.5–23.2 each, 22.27 ± 0.22 | shape fixed | TESScut |
| P s67 ×5 (3139.72 flagged, 3147.72 partial) | 3127.731–3151.712 | 23.3 / 1.0 | 3.60 / 2.54 | QLP, TESScut |
| P s93 ×6 (3843.18 flagged) | 3831.188–3855.169 | 23.2 / 1.1 | 3.70 / 2.40 | QLP, TESScut |
| P s94 ×6 | 3859.167–3879.151 | 20.8 / 1.0 | 3.73 / 2.43 | QLP, TESScut |
| S, 39 windows s12–s94, phase fixed at 0.4956 | 1630.867–3877.136 | weighted mean 1.24 ± 0.07 (χ²r 2.54) | primary shape | QLP (TESScut and ELEANOR per sector, §2) |

- **Ephemeris** (`s7_ephem.out`): 37 primaries give P = 3.9969190 ± 0.0000006 d and T0 = 2384.303949 ± 0.000146. Red. χ² 0.75, O−C rms 1.07 min.
- **Comparison with Gaia:** P_ecl − P_Gaia = −0.002300 d = **−2.31σ**.
- **Odd/even:** raw 22.18 ± 0.16 vs 22.55 ± 0.17 ppt; sector-normalised −1.79σ.
- **Secondary:**
  - Fold fit: phase 0.4953 ± 0.0006, depth 1.41 ± 0.09 ppt. With the shape free: 0.4952 ± 0.0005, 1.39 ± 0.09 ppt, T14 3.57 ± 0.21 h (`s7_ephem.out`).
  - **Null boxes** at phases 0.25 and 0.75: −0.25 ± 0.09 and −0.01 ± 0.09 ppt. The formal errors therefore understate the systematics by up to ≈ 3×. Even so, the secondary stands at ≈ 5σ against the worst null.
  - It is present in both halves: s12–39 phase 0.4951, 1.27 ± 0.11 ppt; s67–94 phase 0.4956, 1.25 ± 0.11 ppt.
  - Per-sector phases run from 0.4881 to 0.4970: mean 0.4941, standard error 0.0012 (`s13_geometry.out`).
- **The by-eye screen did not resolve** that the secondary is ≈ 25 min early, nor that it is ≈ 1.3 ppt rather than 1.5.

## Geometry vs Gaia
(`s13_geometry.out`: 20,000 draws of P, Tp, e, ω; e truncated at 0.)
- **195865529** (Gaia e = 0.074 ± 0.040, ω = 235 ± 33°, K1 = 66.18):
  - Primary minus conjunction A: −0.029 ± 0.161 phase with Gaia's P propagated forward over 771.6 cycles; −0.016 ± 0.141 with the eclipse P propagated back.
  - Primary minus B: +0.496 ± 0.149 and −0.490 ± 0.127, i.e. 3.3σ and 3.9σ.
  - **So the primary is conjunction A:** the hotter RV star is eclipsed by the companion.
  - Predicted secondary phase 0.479 ± 0.024, observed 0.49999 (+0.87σ). Gaia's e cos ω = −0.033 ± 0.040 vs 0.0000 ± 0.0001 observed. Gaia's e is a 1.8σ detection, and the eclipses show the orbit is circular.
  - **Physics:**
    - f(m) = 0.1141 M☉, so m2 = 0.84–0.86 M☉ for M1 = 1.43–1.50, and a = 13.5–13.7 R☉.
    - The flat-bottom trapezoid solution (no limb darkening) gives R1 ≈ 1.72 R☉, R2 ≈ 0.71 R☉, k = 0.41, ρ1 ≈ 0.46 ρ☉. That agrees with FLAME's 2.03 R☉; TIC's 2.83 R☉ looks too large.
    - The depth ratio S/P = 0.267 equals a Planck (800 nm) surface-brightness ratio for T2 ≈ 4500 K against 6600 K. A 0.85 M☉ dwarf would be about 5000–5200 K (ratio 0.40–0.46). This crude check ignores limb darkening and the partial-eclipse geometry; it is roughly consistent, not exact.
    - The light-time shift of the secondary is 16–17 s.
- **468181994** (Gaia e = 0.085 ± 0.084, ω = 20 ± 49°, K1 = 22.35):
  - Gaia's P error alone amounts to 0.497 d over the 498.9 cycles to TESS.
  - Primary minus A: forward −0.286 ± 0.233 (1.23σ), back −0.001 ± 0.192 (0.01σ). Primary minus B: forward +0.163 ± 0.240 (0.68σ), back +0.447 ± 0.202 (2.2σ).
  - **Undecided with Gaia's own P. With the eclipse period, A is preferred at about 2σ.**
  - Predicted secondary phase 0.534 ± 0.040 if the primary is A, 0.466 ± 0.040 if B; observed 0.4956 ± 0.0012 (−0.96σ or +0.74σ).
  - Observed e cos ω ≈ −0.0069 ± 0.0019. Gaia gives +0.053 ± 0.066.
  - The light-time (Rømer) delay is only 39–43 s (0.0001 phase), so the ≈ 25 min offset points to a small real eccentricity. Template or systematic error at the 1.3 ppt level cannot be excluded.
  - **Physics:**
    - f(m) = 0.0046 M☉, so m2 = 0.21–0.24 M☉ and a = 11.9–12.7 R☉.
    - The trapezoid solution gives R1 ≈ 1.47 R☉, R2 ≈ 0.22 R☉, k = 0.152, b ≈ 0.50, ρ1 ≈ 0.54 ρ☉. R2 suits a 0.2 M☉ M dwarf.
    - S/P = 0.062 vs a Planck ratio of 0.077 for 3200 K against 5800 K, consistent with occultation of an M dwarf.
    - Tension: Gaia's photometric size for the primary (FLAME 2.91 R☉; logg 4.08 implies ≈ 1.8 R☉) is larger than the eclipse-implied 1.47 R☉. Light from the suspected sub-arcsecond companion would inflate the photometric radius and dilute the depths.

## Ephemerides and next eclipses
(`s14_ephem_next.out`.) BJD_TDB is converted to geocentric UTC with the barycentric light-time correction **removed** (astropy, builtin ephemeris); the uncorrected times differ by ≤ 2.5 min.
- **TIC 195865529:**
  - P = 3.8310456 ± 0.0000009 d; T0 = BTJD 3346.22697 ± 0.00014 = BJD_TDB 2460346.22697.
  - Next primaries (geocentric UTC): **2026-11-01 15:04, 2026-11-05 11:00, 2026-11-09 06:57** (BTJD 4346.1299, 4349.9609, 4353.7920; ± 0.4 min formal). T14 ≈ 5.2 h, depth ≈ 18% (on QLP's scale).
  - Secondaries: 2026-11-03 13:02, 2026-11-07 08:59, 2026-11-11 04:56.
- **TIC 468181994:**
  - P = 3.9969190 ± 0.0000006 d; T0 = BTJD 2384.30395 ± 0.00015 = BJD_TDB 2459384.30395.
  - Next primaries (geocentric UTC): **2026-11-02 07:00, 2026-11-06 06:55, 2026-11-10 06:51** (BTJD 4346.7912, 4350.7881, 4354.7850; ± 0.5 min). T14 ≈ 3.7 h, depth ≈ 2.3%.
  - Secondaries (phase 0.4956, ± 7 min): 2026-11-04 06:32, 2026-11-08 06:28, 2026-11-12 06:24.

## Caveats
- **468181994:**
  - RUWE 12.6 and ipd_frac_multi_peak 39% point to a companion within about 1″. The 2.85″ neighbour is probably not the cause, since Gaia resolves it as a separate source; this is my inference, not a measurement. TESS pixels cannot separate a sub-arcsecond companion. The case for the eclipses being on the RV star is that the eclipse period equals the SB1 period to 0.06%.
  - That period agreement is only at 2.3σ given Gaia's quoted error. With a 3σ threshold this is a pass; with a 2σ threshold it would make the star PROBABLE.
  - Speckle or AO imaging and a few RVs at quadrature (K1 ≈ 22 km/s) would settle it.
- **195865529:** depth comparisons across pipelines depend on my Gaussian-PSF dilution model (≈ 5%). The 36″ G 13.46 star is excluded by the pixels, not by arithmetic.
- **Not done:** the common-mode test with other stars; any light-curve model with limb darkening (the physics above is trapezoid-level). No TESS-SPOC or 2-min data exist for either star.
- **The `s8` pixel analysis cannot be re-run** without downloading the cubes again (`s3_tesscut_dl.py`), because they were deleted per the brief. Its outputs are saved in `pix/`.
- **Inherited fits:** `s6` marked four primaries and one secondary "ok" although their covariance had failed (partial coverage). `s7` and `s17` exclude them from timing; they are labelled partial above.

## Files
- **Scripts and logs:**
  - `s1_download_lc`, `s1b_download_other`, `s2_archives`, `s2b_archives`, `s3_tesscut_dl`, `s4_period_search`, `s5_fold_scan`, `s6_events`, `s7_ephem`, `s7b_sec468`, `s8a_tic_neighbours`: from the first agent, checked and reused.
  - `s8_pixels`, `s9_pixsummary`, `s10_gaia_extra`, `s11_depths`, `s12_dilution`, `s13_geometry`, `s14_ephem_next`, `s15_websearch` (log only), `s16_plots`, `s17_tables`: this run. Each `.py` has a matching `.out`; s8 has `s8_pixels_<tic>.out`.
- **Data products:** `lcio.py`, `events_qlp.csv`, `events_table_<tic>.md`, `ephem.json`, `s11_depths.json`, `fold_<tic>.txt`, `tic_neighbours_<tic>.csv`, `pix/` (aperture light curves, difference and scene images, per-sector JSON), `fig_<tic>.png`.

TIC 195865529: CONFIRMED; P_ecl=3.8310456±0.0000009 d; depth1=183 ppt (QLP, ≈deblended; 192±7 TESScut undiluted); depth2=48 ppt at phase 0.49999±0.00007; pixel: on target; pipelines: 3 (QLP, own TESScut, TASOC); Gaia geometry: pass (primary = conjunction A at 0.1–0.2σ, B excluded at 3.3–3.9σ; circular orbit)
TIC 468181994: CONFIRMED (weaker: P_ecl vs Gaia at −2.3σ; suspected sub-arcsec companion); P_ecl=3.9969190±0.0000006 d; depth1=22.5 ppt (QLP) / 23.2 (TESScut); depth2=1.24–1.41 ppt at phase 0.4956±0.0012; pixel: on target (2.85″ G16.75 neighbour rejected at ≈16σ); pipelines: 3 (QLP, own TESScut, ELEANOR-lite); Gaia geometry: pass (secondary phase within 1σ; A vs B undecided with Gaia P, A preferred at ~2σ with eclipse P)
