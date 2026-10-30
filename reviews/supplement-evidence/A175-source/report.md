# REPORT — TIC 269504659 (TYC 4674-364-1, 2MASS J00551372-0007541, Gaia DR3 2536832294627315072)

Opus 5.5 subagent, 2026-10-21, wave 5. Fresh folder; no earlier session worked this star. (Saved by the parent session; the file-write tool refused REPORT.md for the subagent.)

## Verdict: CONFIRMED. A detached SB1 with an M-dwarf companion; the M dwarf transits a G subgiant/dwarf. Secondary eclipse detected; APOGEE RVs independently phase the orbit to the eclipses.

Deciding numbers:
- **Primary eclipses:** 6 individual events in s042, s043 and s070, each at S/N 61–117. This is one more than the batch's 5: the 3221.515 event has a bit-32 cadence in its window. Depth 23.57 ± 0.10 ppt, T14 4.44 h, T12/T14 0.35.
- **Period:** P = 11.391807 ± 0.000015 d against Gaia's 11.390958 ± 0.001045 d, a difference of **+0.81σ**.
- **Which conjunction:** the primary sits on Gaia conjunction A at **+0.06σ to +0.26σ** (+0.3 h to +1.7 h). Conjunction B is 21σ to 27σ away.
- **Secondary eclipse (new):**
  - In a fixed-shape test inside ±3σ of Gaia's predicted phase (0.5177 ± 0.0122), the best window is at phase 0.5361 with 1.47 ± 0.12 ppt, S/N 12.2.
  - In 35 look-elsewhere control windows the best S/N has median 2.0 and maximum 5.9; none reaches ours.
  - Per event: 4 events at S/N 5.4–8.4, depths 1.24, 1.41, 1.48 and 1.60 ppt (weighted 1.45 ± 0.11, χ² 1.5/3). T14 4.92 h (range 4.68–5.22).
  - It is also present in TESS-SPOC and SPOC 2-min light curves at 1.35–1.89 ppt.
- **Eccentricity:** phase separation 0.53566 ± 0.00031 gives **e cos ω = +0.0560 ± 0.0005** (Rømer delay ~1 min, negligible).
  - Against Gaia's +0.028 ± 0.019 that is +1.4σ; against Gaia's predicted B−A phase it is +1.5σ.
  - The duration ratio gives e sin ω ≈ +0.05 ± 0.03, against Gaia's −0.015 ± 0.016. This is soft, per the wave-4 lesson.
- **APOGEE DR17 (independent RVs):** three visits (BTJD 2079.94, 2080.92, 2083.89) at +2.51, −3.29 and −33.78 km/s.
  - Phased on the eclipse ephemeris alone, with Gaia's K and γ, the model matches with rms 0.30 km/s after a constant +1.76 km/s zero-point offset.
  - A free circular fit gives K = 20.9 km/s (Gaia 21.34 ± 0.57). The RV descending node falls within +0.004 phase of the deep eclipse.
  - So the luminous RV star is the one eclipsed at the deep eclipse. (With three points and three free parameters the free fit itself is exact, not a test.)

## 1. Archives
- **cats.py --r 60:** no VSX or ASAS-SN entry, and no EB-table hits. SIMBAD has only TYC 4674-364-1, typed [SB*].
- **Gaia DR3:** vari tables are empty; RUWE 1.29, ipd_frac_multi_peak 0.
- **SB9, WDS, J/AJ/160/111:** none.
- **ExoFOP:** no TOI or CTOI, and no imaging, spectra or companions. The SPOC 2-min light curve exists for s070.
- **Extra VizieR cones at 30″:** no variability or X-ray rows (ATLAS, ZTF, WISE, GCVS, ROSAT, 2RXS, 4XMM, ASAS-SN, LAMOST, Prša+2022), and the control cones returned rows. APOGEE DR17 has the star (Teff 5770 K, logg 4.03), which is the source of the RVs above.
- **Web search** ("TYC 4674-364-1" OR "TIC 269504659" eclipsing binary): no page mentions the star.
- **Batch receipts:**
  - c3-vetsum: dphi +0.001/+0.483, ATTR.
  - c3-sapdepth: 5 events at 21.6–23.9 ppt.
  - diffrun s043: peak on target, deficit−light 0.44″.
- **No prior art.** This is a new EB.

## 2. Measurements (QLP SAP, Q==0, no trimming)
- **Primary depth per sector:** s042 23.58, s043 24.39, s070 23.02 ppt. χ²/dof of depth constancy is 46/5, consistent with sector-to-sector dilution.
- **Odd vs even:** 23.45 ± 0.14 vs 23.70 ± 0.15 ppt.
- **Shape:** a box is worse by Δχ² 4,700 and a V by Δχ² 490. There is a flat bottom of about 1.3 h.
- **Timing:** O−C is within ±2 min of the linear ephemeris. The formal 0.4-min errors sit at the fit's grid floor (0.72-min steps).
- **Background:**
  - Primary: the regression implies |ΔF| ≤ 0.06 ppt per sector against 15–16 ppt dips in the same windows. The large dBKG on 3221.515 is the known broken-unit column.
  - Secondary: s042 0.000 and s070 0.002 ppt. In s043 the background could account for up to 0.33 ppt of a 1.1-ppt dip, and the other sectors carry the detection anyway.
- **Centroids:** secondary dX +0.02 ± 0.19 mpix, dY −1.7 ± 1.1 mpix.
- **Quality flags:** 2 primaries and 2 secondaries touch a bit-32 cadence; none is near a listed systematic time.
- **Controls:** primary-run control phases give |depth| ≤ 0.27 ppt. Phase 0.500 gives +0.27 ± 0.10 ppt, which is wing leakage from the 0.536 secondary.
- **Blind dip census:** 14 dips at S/N ≥ 4.
  - 6 are the primaries.
  - 4 are the 1.2–1.6-ppt dips at phase −0.465 (= 0.535), i.e. the secondary.
  - 3208.92 (1.7 ppt, phase 0.895) has a large s070 background excursion, and its next-cycle repeat measures 0.08 ± 0.22 ppt.
  - 3221.94 sits on the post-eclipse shoulder.
  - The rest are under 1 ppt.

## 3. Ephemerides
- **Primary (conjunction A):** T0 = 2800.01713 ± 0.00049 BTJD, P = 11.391807 ± 0.000015 d (χ² scaled ×4.5).
- **Secondary (conjunction B):** T0 = 2863.07833 ± 0.00347 BTJD, P = 11.391710 ± 0.000105 d, consistent with the primary's P. χ²/dof 0.6/2.
- **Against Gaia** (Monte Carlo with corr_vec):
  - Conjunction A − observed primary: +0.32 h (s042), +0.37 h (s043), +1.72 h (s070), i.e. 0.06σ–0.26σ.
  - Conjunction B − observed secondary: +5.1 to +6.3 h, about +1.0σ.

## 4. Independence
- **Other pipelines** (TESS-SPOC s042, s043, s070 and SPOC 2-min s070): primary depth PDCSAP 22.2–22.9 ppt and SAP 22.9–23.1 ppt; secondary 1.35–1.89 ppt in all of them.
- **Difference images** (four TPFs: TESS-SPOC s042, s043, s070 and SPOC s070): the max-loss pixel is on or adjacent to the target at S/N 23–34, the loss-weighted centroid is within about 0.4 px of the target, and the implied own dip is 19.2–20.6 ppt.
- **Neighbours:** Gaia DR3 has no source brighter than G 20.14 within 60″; the six there are G 20.1–21.3 at 25–49″. The brightest would need a 116,000-ppt dip for the primary and 7,000 ppt for the secondary, so all are impossible.

## 5. Physics
- **Mass function** f(M) = 0.0114 M☉. With M1 = 1.05 ± 0.14 M☉, m2 = 0.27 M☉ (0.25–0.29), an M dwarf. q ≈ 0.26, a ≈ 23.4 R☉.
- **Transit geometry:** depth 23.6 ppt gives k ≈ 0.16, and T14 4.44 h with T12/T14 0.35 gives b ≈ 0.8. Then R1/a ≈ 0.061, so **R1 ≈ 1.4–1.6 R☉** and R2 ≈ 0.23–0.26 R☉. That is the size of an M dwarf with the f(M) mass.
  - TIC gives R1 = 1.79 ± 0.09 R☉.
  - log g gives R1 ≈ 1.55 R☉ (Gaia 4.08) and ≈ 1.64 R☉ (APOGEE 4.03).
  - So the mild tension is with TIC only.
  - occfit.py's free fits are degenerate (transit R1 1.31 at amplitude 0.45; occultation R1 1.55) and are not used.
- **Secondary depth:** a total occultation of an M dwarf with k² ≈ 0.025 needs J ≈ 0.06, i.e. T2 ≈ 3100–3300 K for a G primary (TIC 5839 K, APOGEE 5770 K). That is the expected temperature for 0.27 M☉. Observed 1.45 ppt against roughly 1.5–2.2 ppt predicted.
- **Ellipsoidal and beaming:** predicted 0.15 and 0.28 ppt, below the noise (measured harmonics ≤ 0.17 ppt), and the measured cos 2φ term has the wrong sign. Not detected.
- **Not a heartbeat:** the orbit is low-e, and the eclipse is a flat-bottomed transit.

## 6. Next predicted eclipses (BTJD)
- **Primary** (M dwarf transits, conjunction A, ~23.6 ppt, T14 4.4 h): **4337.9111, 4349.3029, 4360.6947** (± 3 min), then every 11.391807 d.
- **Secondary** (M dwarf occulted, conjunction B, ~1.45 ppt, T14 ~4.9 h): **4344.0132, 4355.4050, 4366.7968** (± 6 min).

## What would settle it further
- A few more RVs, ideally from Gaia DR4 epoch RVs or new APOGEE/HARPS visits, for a joint RV + eclipse fit of e and ω.
- More TESS sectors, to firm up the 1.45-ppt secondary's phase and duration (e sin ω).
- A spectroscopic R1.

## Files in vet269504659
- **Scripts:** vet.py (patched as for 348784186), vetlib.py, secA.py, bkgreg.py, indep.py, tpfdiff.py, occfit.py, physics.py, apogee.py, nb60.py, gaiatap.py, mastlc.py, morecats.py, extracats.py.
- **Primary-eclipse outputs:** vet-out.txt, vet-results.json, fold_oc.png, events.png, oc-out.txt.
- **Secondary-eclipse outputs:** secA-out.txt; secv\vet-out.txt, vet-results.json, events.png, bkgreg-out.txt, indep-sec-out.txt.
- **Analysis outputs:** bkgreg-out.txt, indep-out.txt, tpfdiff-out.txt, tpfdiff_*.png, occfit-out.txt, physics-out.txt, apogee-out.txt.
- **Archive outputs:** nb60-out.txt, cats-out.txt, gaiatap-out.txt, morecats-out.txt, extracats-out.txt, mastlc-list.txt, mastlc-dl.txt.
- **Data:** `C:\Home\sky\data\qlp-sb-p20-60\pervet269504659\`.
