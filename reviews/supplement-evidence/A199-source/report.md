Adversarial check: TIC 391925531 (TYC 9380-1063-1, Gaia DR3 5212819506717573504)
Second vet run, resumed 2026-10-21. I read and re-used the inherited Gaia, MAST, archives2 and ExoFOP results; dvlist and dvparse were run here.
Scripts and outputs are in this folder; downloads are in sky\data\qlp-sb-p20-60\vet391925531\.
Labels: the observed eclipse is at Gaia conjunction B (nu = 270 - w, the RV primary in front). In ecl/ephem files it is kind "P"; see progress.md.

VERDICT: CONFIRMED (eclipsing binary on the target)
- It is a grazing occultation of the companion by the RV primary at conjunction B: 2.02% deep, about 6.7 h long, V-shaped, seen 23 times from s1 to s98.
- There is no eclipse at conjunction A (< about 110 ppm), which the geometry requires.
- "Really uncatalogued?" Not in any EB or variable-star catalogue, but the signal itself is NOT unknown:
  - SPOC 2-min TCE since the s1-s36 multi-sector run (2021);
  - ExoFOP CTOI TIC 391925531.01, disposition PC (Taaki et al., in prep., created 2022-12-09, P 43.95(5) d, epoch BTJD 2078.97(5), duration 6(2) h).
  Both treat it as a planet candidate. The new result is the identification: the Gaia SB1 orbit (f(M) = 0.12 Msun) puts the eclipse at the stellar companion's conjunction, so it is an EB and the CTOI should be re-dispositioned.
- The phase-0.225 dip is an artefact (s98 scattered light at a data gap).

1. ARCHIVES (what was queried and what came back)
- cats.py: VSX, ASAS-SN, Prsa+2022, IJspeert+2024 and Kostov+2025 t2/t3/t4 have nothing within 5". SIMBAD has only "SB*".
- Gaia DR3: vari_eclipsing_binary, vari_summary and vari_classifier_result return 0 rows.
  NSS SB1: P 43.99434(1699) d, e 0.3818(257), w 232.14(3.27) deg, K1 32.16(1.63) km/s, gamma 12.34(55), corr(w, Tp) 0.902.
  GSP-Phot: Teff 6338, logg 3.82, R 2.66 Rsun. FLAME: M 1.63 Msun. RUWE 1.01.
- VizieR 60" cones (archives2.txt) returned 0 rows in VSX, ASAS-SN, Prsa, IJspeert, GCVS, SB9, WDS, ZTF, ATLAS, KELT, Justesen, Rowan, Fetherolf, IJspeert+2021 and RAVE/LAMOST/GALAH.
- Non-empty but not prior art:
  - Kostov+2025 table2 lists TIC 391925540 (Tmag 14.06, 48.7"), not the target.
  - Green+2023 gives the target a score of 0.000.
  - The cone on "J/A+A/674/A16" returned a different table; Gaia TAP is the authoritative source here.
- APOGEE DR17: 1 visit (LCO, JD 2458146.644), vhelio -15.04 km/s, Teff 5981, logg 3.66, [M/H] -0.10, vsini 11.6.
- ExoFOP (exofop.json): no TOI. CTOI TIC 391925531.01 as above. No imaging or spectroscopy entries. TIC contamination ratio 0.028.
- SPOC DV (dv.txt), s1-s96 run:
  - P 43.977843(13), epoch 2079.03902(29), depth 20301(87) ppm, duration 6.98 h, b 0.945(19);
  - odd/even significance 0.22; suspectedEclipsingBinary false;
  - weak secondary maximum MES 3.5 at +22.48 d (phase 0.511), 167(45) ppm, which is not significant.
  The same TCE appears in the s1-s36 and s1-s39 runs. The TESS-SPOC s56-s69 TCE (29.3 d, 309 ppm) is unrelated noise.
- Web search on the TIC/TYC names and the Taaki method found nothing. Tarrants & Mendes 2023 (arXiv 2310.12380, Gaia NSS vs planet candidates) uses TOIs and K2 only; this star is not in it.

2. ECLIPSE MEASUREMENTS
Method: raw QLP SAP, q==0, no trimming; a trapezoid times a quadratic baseline.
- Events: 22 q==0 fits, plus s39 from the flagged-cadence (all-q) fit, gives 23. No events were dropped.
- Shape: depth 2.02% (median, sd 0.10), T14 6.70 h (sd 0.08), T12 2.59 h, flat 1.51 h. V/U-shaped, with ingress about 0.39 of the total, i.e. grazing.
- Depth stability: QLP s96, s97 and s98 give 1.91, 1.73 and 1.72%. This is a QLP artefact:
  - SPOC 2-min s96 gives 2.09% (SAP) and 2.01% (PDCSAP);
  - my TESScut photometry gives 1.9% (1x1 aperture) in both s93 and s98.
- Background: the in-eclipse change is -0.41% of the target flux, against +0.02% and +0.22% at control phases. The sign is the wrong way for a background-made dip.
- Centroids: dx/dy = +0.3/+0.5 mpx (event sd 1.5/3.2), with controls at about 0. No motion.
- A-conjunction slot (phase +0.6546 after B):
  - all 24 per-cycle fits give <= 0.04%;
  - a fold of 15 cycles over +-3 d (which covers +-4.5 sigma of Gaia's A-timing error of 0.67 d) has a deepest 6-h box of 33 +- 35 ppm. So depth_A < about 110 ppm (3 sigma).
  - A fold at phase 0.5 shows nothing (the SPOC weak secondary is not confirmed).
- Phase-0.225 dip (phasedip_0225.txt, look_s98_0225.png): the classifier's fold zero, 1341.32, is B + 0.225 P.
  - In the 25 covered cycles, the q==0 depth at that phase is -0.05 to +0.06% (+-0.01%).
  - The 0.5% feature is s98 4023.8-4024.3: the q==0 tail of a mostly flagged low segment, under strong, falling scattered light (SAP_BKG 50000 -> 15000 e/s). It ends at a data gap, with a centroid jump across the gap.
  - Verdict: artefact.
- Blind census (thr 0.3%): nothing outside the eclipses, except the known s94 3875 common-mode dip and s98 scattered light.

3. EPHEMERIS AND ORBIT
- B: T0 = BTJD 2079.03934 +- 0.00018, P = 43.977834 +- 0.000008 d. chi2 14.4/21 (1-min floor); rms 0.85 min; no quadratic term.
- SPOC DV agrees: 43.977843(13), 2079.03902(29).
- The TESS period minus Gaia's is -0.0165 d = -0.97 sigma.
- Measured minus Gaia-predicted B conjunction: -0.20 d (s1) drifting to -1.21 d (s98) because of the period difference; that is -0.39 to -0.86 sigma.
- Only one eclipse kind is seen, so e cos w and e sin w cannot be measured from timing. Gaia predicts A - B = 0.6544 +- 0.0153 in phase.
- Instead, Gaia's e and w were tested by the forward model (section 5): r_B = 0.656a near periastron and r_A = 1.223a. So b_A = 1.86 b_B, and a grazing B with no A is exactly what Gaia's e and w predict.
- APOGEE: the 2018 RV, phased on the TESS ephemeris with the eclipse as B, matches the Gaia orbit (O-C +1.5 km/s). If the eclipse were A, O-C would be -39.7 km/s. This independently confirms the conjunction identification.

4. INDEPENDENCE
- Other pipelines (secondpipe.txt):
  - SPOC 2-min SAP/PDCSAP s28, s93, s96; TESS-SPOC s1, s28; GSFC-ELEANOR-lite s1; TGLC s1 (aperture and PSF).
  - All recover the eclipse. Mid-times agree with QLP to within 0.1-2.3 min; T14 6.6-7.0 h; depth 1.92-2.39%.
- Difference images (TESScut s93 and s98; diff.txt):
  - The deficit is centred on the target pixel; depth is 1.9 / 1.8 / 1.7% in 1x1 / 3x3 / 5x5 apertures, in both sectors.
  - The pixels of the G 14.56 (48.8") and G 15.85 (47.3") neighbours show only 0.3-1.1%, which is the target's wings.
- Neighbours (neighbours.txt): within 60", the only source brighter than G 17 besides the target is G 14.56 at 48.8". It would need a 49% eclipse, which is excluded by the difference image and by the absence of centroid motion (expected about 40 mpx, observed 0.3 +- 0.3). G 15.85 would need 162%, which is impossible. Gaia RUWE is 1.01 and ipd_frac_multi_peak is 0.

5. PHYSICS
- f(M) = 0.1196 [0.102, 0.139] Msun; a1 sin i = 25.8 Rsun.
- For M1 = 1.25-1.65 Msun: m2(i about 86 deg) = 0.79-0.93 Msun (a K/G dwarf, R2 0.75-0.89 Rsun, Teff 5000-5500 K); a = 66-72 Rsun.
- Which star is in front:
  - At B (nu + w = 270), the RV primary (F/G subgiant, R about 2.7-3.0) passes in front of the companion. This is the observed eclipse: a partial occultation of the companion.
  - At A, the companion would transit, but only at 1.86 times the projected separation.
- b=0 durations would be 12.6-13.3 h at B and 23-25 h at A; the observed 6.7 h at B means a high impact parameter.
- Forward model (graze.txt; MS companion, limb darkening, blackbody J):
  - i = 86.2-86.6 deg reproduces depth_B = 2.02% with b_B = 0.72-0.82 (in units of R1+R2), T14 6.9-9.2 h (first-to-last contact), and depth_A = 0.000%.
  - The Gaia-FLAME-like case (M1 1.65, R1 2.7) gives T14 6.85 h, against 6.70 observed.
- Depth, duration, the V shape, the missing A eclipse, the RV phase and the SB1 nature (L2/L1 about 0.05) all fit one geometry.
- A planet is excluded by K1 = 32 km/s at this period.

6. NEXT EVENTS (BTJD)
- B eclipse (2.0%, about 6.7 h, grazing occultation of the companion): 4365.8867, 4409.8646, 4453.8424, 4497.8202 (+-0.7 min formal; allow +-3 min).
- General: T_B = 2079.03934 + 43.977834 E.
- A conjunction (no eclipse expected; < 110 ppm observed): 4350.69, 4394.67, 4438.64, 4482.62 (+-0.67 d).

WHAT WOULD SETTLE IT FURTHER
1. Tell ExoFOP: CTOI 391925531.01 is an EB (a stellar companion with f(M) = 0.12 Msun), via a CTOI comment or a disposition update.
2. A few high-resolution RVs to refine K1, e and w and search for the secondary's lines (L2/L1 about 0.05 in TESS, more in the red). Combined with the eclipse they would fix i, about 86.4 deg.
3. A proper grazing-EB fit (with ld and J free) to the 2-min SPOC data, to bound R2/R1 and L2/L1.
4. Optional: report it to VSX as an EA with the ephemeris above, noting that only one eclipse per orbit exists.
