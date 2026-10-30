# TIC 63858295 (TYC 1429-565-1, Gaia DR3 3982492520952574336): per-object vet

Opus 5.5 subagent, 2026-10-21, wave 5. Fresh folder; protocol VET-BRIEF + BRIEF-ADAPT (through wave 4). (Saved by the parent session; the file-write tool refused REPORT.md for the subagent.)

## Verdict: CONFIRMED. A detached, grazing G + M-dwarf EB on a spotted, near-synchronous primary, with both eclipses detected. The M dwarf transits the primary at Gaia conjunction A, and the orbit is circular.

Deciding numbers:
- **Primary eclipses:** 23 events with clean cadences in s022/s045/s046/s072, plus 3 recovered from flagged cadences: 1899.512 (26.4 ± 0.7 ppt), 1916.678 (27.5 ± 1.1) and 3283.083 (27.0 ± 0.4). That makes **26, not the row's 18**.
  - Depth 26.42 ± 0.10 ppt, T14 1.86 h, T12/T14 0.40.
- **Period:** P = 3.4331770 ± 0.0000009 d against Gaia's 3.433232 ± 0.000273 d (−0.20σ).
- **Attribution:** the primary sits on Gaia conjunction A at −0.02σ (s022) to −0.15σ (s072). Conjunction B is 7σ to 14σ away.
- **NEW secondary eclipse:** 2.53 ± 0.10 ppt, S/N 17.6, at phase **0.50020 ± 0.00028**.
  - Look-elsewhere test: 55 random phases give a maximum S/N of 3.5; none reaches the secondary's S/N.
- **Eccentricity:** **e cos ω = +0.0003 ± 0.0004**, against Gaia's +0.030 ± 0.027 (1.1σ). Gaia's predicted B − A separation is 0.519 ± 0.017 (1.1σ).
  - Gaia's e of 0.052 ± 0.039 is not significant, and the orbit is circular. This is the usual wave-4 small-e pattern and is harmless here.
- **On target:**
  - Difference images from 120-s SPOC (s045, s046) and 200-s TESS-SPOC (s072): the max-loss pixel is the target pixel at S/N 60–75, and the target fit gives implied dips of 20.3–21.6 ppt.
  - The only Gaia source within 60″ is G 19.31 at 50.2″, which would need a 43,000 ppt dip.

## 1. Archives
- **cats.py --r 60:**
  - VSX: none. ASAS-SN: none.
  - Prša+2022, IJspeert+2024, Kostov tables: no hits.
  - **SIMBAD was unreachable** (connection timeouts on 2026-10-21, also via SIMBAD TAP on both hosts). Re-check when it is back.
- **Gaia DR3:**
  - vari_summary and vari_eclipsing_binary: both empty.
  - NSS SB1 orbit: P 3.433232, e 0.052 ± 0.039, ω 322 ± 35°, K1 38.43 ± 0.87 km/s, significance 44.
  - RUWE 1.12; gspphot Teff 5715 K, logg 4.32.
- **SB9, WDS, J/AJ/160/111:** no entries.
- **ExoFOP:** no TOI, CTOI, imaging, spectra or companions.
- **VizieR cones at 30″:** ATLAS, ZTF, WISE variables, GCVS, VSX, ROSAT, 2RXS, 4XMM, ASAS-SN, APOGEE and Prša all empty, and the controls returned rows.
  - LAMOST DR7 LRS has two spectra. 2015-01-11: class STAR, subclass **G1**, z gives about +20 km/s at one epoch. 2017-02-14: S/N ≤ 2.6, unusable. No stellar parameters are in the catalogue.
- **Web search** on the TYC, TIC and Gaia IDs: no relevant hits.
- **Prior art to disclose:** the star was a 2-min SPOC target in s045/s046, and SPOC DV produced detections (TCEs) in:
  - the s042–s046 multi-sector run: TCE_1 P 3.43325 d, 25.9 ppt, MES 158; TCE_2 at phase ~0.50, 2.24 ppt, MES 15;
  - single-sector s045 and s046;
  - TESS-SPOC s045, s046 and s072.
  The pipeline saw both eclipses repeatedly, but it never became a TOI or CTOI (dvcheck-out.txt).
- **Batch receipts:**
  - c4-vetsum: dphi +0.004/+0.478, ATTR.
  - diffrun-c4 s045: peak on target; deficit 0.41″ from the light centroid.

## 2. Measurements (QLP SAP_FLUX, QUALITY==0, no trimming)
- **Per-sector primary depth:** 26.2–26.6 ppt; depth-constancy χ²/dof 33.6/22.
- **Odd vs even:** 26.24 ± 0.17 vs 26.52 ± 0.13 ppt (1.3σ).
- **Background:** the unit-free regression implies at most 0.08 ppt of fake dip in any sector.
  - s072 has a −226-unit background change in eclipse, but the regression slope turns it into only −0.08 ppt.
  - vet.py's dBKG column is ignored, per the wave-3 lesson.
- **Centroids:** dX +0.08 ± 0.10 mpix, dY +0.01 ± 0.10 mpix.
- **Momentum dumps:** 4 events have a bit-32 cadence in their window; with 26 events, none of them matters. None falls near a listed sector-wide systematic time.
- **Blind dip census:**
  - 43 dips at S/N ≥ 4: 23 are primaries and 17 are the secondary (phases ±0.498–0.500).
  - Two other dips are 1.4–1.9 ppt at S/N ~4.2–4.4.
  - One 16.5 ppt "dip" at 3272.913 sits 0.13 d after the primary at 3272.783, inside the matched filter's ±0.15 d window. It is the primary leaking into the filter (S/N 6.3 against the primary's 54), the same artefact as in 423927429, and it does not repeat.
- **Control phases:** |depth| ≤ 0.21 ppt.
- **Eclipse shapes:**
  - Primary: near-V graze. A flat-bottomed shape (T12/T14 0.1) is worse by Δχ² 494.
  - Secondary: T14 1.88 ± 0.07 h, giving e sin ω ≈ +0.011 ± 0.019, consistent with Gaia's −0.033 ± 0.036.
- **Timing scatter:** O−C rms 0.8 min, with χ²/dof 120/21 (errors scaled ×2.4). This fits spot-crossing and spot-baseline distortion on an active star rather than ETVs; the s046 offset is +0.6 min.
- **Out-of-eclipse variability** (rotper-out.txt): strong spot modulation, peak 3.34–3.40 d against P_orb 3.433 (equal within the periodogram resolution, about 0.45 d), semi-amplitude 3.7 → 10.1 ppt from s022 to s072. A near-synchronous, increasingly active primary.

## 3. Ephemeris
- **Primary:** P = 3.4331770 ± 0.0000009 d; T0 = 2599.88038 ± 0.00012 BTJD (E = 203).
- **Secondary − primary, per sector:** s022 0.49962, s045 0.49980, s046 0.50076, s072 0.50023; weighted mean 0.50020 ± 0.00028 (χ²/dof 4.9/3).
- **Versus Gaia:**
  - The eclipse lies −0.06 h from Gaia's conjunction A at s022 and −0.84 h at s072 (σ about 3–5 h).
  - The A−B separation agrees at 1.1σ.

## 4. Independence
- **Other pipelines:**
  - SPOC 2-min PDCSAP / SAP: 25.8–25.9 ppt (s045, s046).
  - TESS-SPOC PDCSAP: 24.9–26.1 ppt (4 sectors).
  - TARS: 24.7–26.0 ppt (4 sectors).
- **Difference images:**
  - SPOC 120-s s045: max-loss pixel S/N 69.5; target fit gives 20.6 ppt.
  - SPOC 120-s s046: S/N 75.0; 20.3 ppt.
  - TESS-SPOC 200-s s072: S/N 60.6; 21.6 ppt.
  - In each case the loss-weighted centroid is on the target.
- **Dilution:** the only Gaia DR3 source within 60″ is G 19.31 at 50.2″ (needed dip 43,000 ppt). The TIC contamination ratio is 0.0003.

## 5. Physics (physics-out.txt, occfit-out.txt)
- **Companion:** f(M) = 0.0201 M☉. With M1 = 1.07 ± 0.13 M☉, m2(90°) = 0.34 M☉ (range 0.32–0.37), an M dwarf.
- **Orbit scale:** a = 10.75 R☉; tangential speed 19.1 R☉/d at conjunction A.
- **Grazing geometry:** a central eclipse would last 3.7–3.8 h, so the observed 1.86 h needs i ≈ 83.1° and a mid-eclipse separation of 0.87 × (R1 + R2).
- **Which star is in front** (limb-darkened physical fit, 18 events):
  - Transit of the primary fits with k 0.285, b 1.02, and gives **R1 = 1.00 R☉** (TIC 1.13, LAMOST G1, consistent).
  - The occultation alternative needs the companion to supply 9.4% of the light, against an expected light ratio of about 0.008. Impossible.
  - So the M dwarf is in front at conjunction A. Conjunction B is predicted to eclipse (margin 0.27 R☉), and it is seen.
- **Secondary depth:** the secondary/primary ratio of 0.095 implies T2 ≈ 3350 K for T1 ≈ 5900 K (blackbody), consistent with a 0.34 M☉ dwarf.
- **Ellipsoidal and beaming:** predicted 0.47 / 0.51 ppt. The measured cos 2φ (+0.8 ppt) and sin φ terms are dominated by the spot modulation (sector scatter 1.5–4.8 ppt) and are unusable.
- **Heartbeat:** not relevant; the orbit is circular with sharp eclipses at both conjunctions.

## 6. Next predicted times (BTJD; 2026-10-21 ≈ BTJD 4335)
- **Primary** (M dwarf transits the primary, conjunction A): **4337.0679, 4340.5011, 4343.9343**, ± 0.7 min formal (allow ~2–3 min given the spot-driven timing excess); then every 3.4331770 d.
- **Secondary** (M dwarf occulted, conjunction B): **4335.3520, 4338.7852, 4342.2184**, ± 1.5 min.

## What would settle it further
- A SIMBAD re-check once the service is back.
- A higher-S/N spectrum (the LAMOST one is low-resolution) for Teff and an RV point.
- A spot-corrected eclipse-timing analysis to confirm the 0.8-min O−C excess is activity, not a third body.

## Row fixes
- Events: 26 (23 clean + 3 from flagged cadences).
- Depth: 26.42 ppt.
- P: 3.4331770(9) d.
- Secondary: 2.53 ppt at phase 0.5002.
- Disclose the SPOC TCE detection (2-min target, s042–s046 multi-sector run, both eclipses).

## Files
- **Scripts:** the same set as 55214475.
- **Outputs:** the matching `*-out.txt` files, fold_oc.png, events.png, sec2.png, the tpfdiff images, gaia.json, nb60.json and vet-results.json.
- **Data:** `C:\Home\sky\data\qlp-sb-p20-60\pervet63858295\`.
