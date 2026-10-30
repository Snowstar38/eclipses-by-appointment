# TIC 55214475 (TYC 4104-606-1, Gaia DR3 1008430975045858048): per-object vet

Opus 5.5 subagent, 2026-10-21, wave 5. Fresh folder; protocol VET-BRIEF + BRIEF-ADAPT (through wave 4). (Saved by the parent session; the file-write tool refused REPORT.md for the subagent.)

## Verdict: CONFIRMED. A detached, grazing F/G + M-dwarf EB with both eclipses detected. The M dwarf transits the primary at Gaia conjunction A, and the orbit is slightly but measurably eccentric.

Deciding numbers:
- **Primary eclipses:** 15 events with clean (Q0) cadences in s019/s059/s060/s073, plus 2 recovered from flagged cadences: 1829.029 (23.1 ± 0.6 ppt) and 3287.573 (26.4 ± 0.5 ppt). That makes **17, not the row's 12**.
  - Depth 25.97 ± 0.08 ppt, T14 1.92 h, T12/T14 0.40.
- **Period:** P = 4.8136773 ± 0.0000007 d against Gaia's 4.813799 ± 0.000164 d (−0.74σ).
- **Timing:** O−C rms 0.4 min; χ²/dof 18/13.
- **Attribution:** the primary sits on Gaia conjunction A at −0.94σ (s019, the sector nearest the Gaia epoch) to −0.87σ (s073). Conjunction B is 25σ to 52σ away.
- **NEW secondary eclipse:** 1.54 ± 0.07 ppt, S/N 19.9, at phase **0.49681 ± 0.00017**.
  - The four sectors agree (χ²/dof 2.4/3).
  - Look-elsewhere test: 55 random phases give a maximum S/N of 2.8; none reaches the secondary's S/N.
- **Eccentricity:** **e cos ω = −0.00502 ± 0.00026**, against Gaia's −0.0108 ± 0.0075 (0.8σ). Gaia's predicted B − A separation is 0.4931 ± 0.0048 (0.8σ).
  - The light-travel-time delay is about 30 s, against the observed 22-min offset, so the eccentricity is real (e ≥ 0.005).
- **On target:**
  - TESS-SPOC difference images (s060, s073) put the best fit on the target, with implied own dips of 21.3 and 18.5 ppt. The other star in the fit is worse by Δχ² 4,500–5,750.
  - No Gaia source within 60″ is brighter than G 17.21, so every neighbour would need a dip larger than 100% of its own flux.

## 1. Archives
- **cats.py --r 60:**
  - VSX: "Gaia DR3 1008430975045858048", type **ROT**, P 3.97154 d, at 0″. This is the Gaia DR3 rotation-modulation classification, a non-eclipsing type, so it is a **type revision, not prior art**.
  - ASAS-SN: none.
  - SIMBAD: TYC 4104-606-1, type [SB*].
  - Prša+2022, IJspeert+2024, Kostov tables 2–4: no hits.
- **Gaia DR3:**
  - vari_eclipsing_binary: empty.
  - vari_summary: in_vari_rotation_modulation = true; G range 0.029 mag; phot_variable_flag VARIABLE.
  - NSS SB1 orbit: P 4.813799, e 0.019 ± 0.008, ω 129 ± 21°, K1 39.99 ± 0.33 km/s, significance 122. The full row with corr_vec is in gaia.json.
  - RUWE 1.16; gspphot Teff 5909 K, logg 4.29.
- **SB9, WDS, J/AJ/160/111:** no entries.
- **ExoFOP:** no TOI, CTOI, imaging, spectra or companions.
- **VizieR cones at 30″** (extracats-out.txt): ATLAS, ZTF, WISE variables, GCVS, ROSAT, 2RXS, 4XMM, ASAS-SN, LAMOST DR7, APOGEE DR17 and Prša all empty, and every control cone returned rows. The only hit is the VSX ROT row.
- **Web search** on the TYC, TIC and Gaia IDs: no relevant hits.
- **Prior art to disclose: SPOC DV from the TESS-SPOC full-frame-image pipeline produced detections (TCEs) in s060 and s073.**
  - TCE_1: P 4.81379 d, 26.6 ppt, 2.01 h, MES 147.
  - TCE_2: phase ~0.497, 1.75–1.80 ppt, MES 9–10.
  - The pipeline saw both eclipses, but it never became a TOI or CTOI (dvcheck-out.txt).
- **Batch receipts:**
  - c3-vetsum: dphi −0.010/+0.497, ATTR.
  - diffrun s059: peak on target; the deficit is 0.58″ from the light centroid.

## 2. Measurements (vet-out.txt, sec2-out.txt, sectime-out.txt; QLP SAP_FLUX, QUALITY==0, no trimming)
- **Per-sector primary depth:** 25.4–26.5 ppt. The depth-constancy χ²/dof of 53/14 is mild.
- **Odd vs even:** 25.84 ± 0.11 vs 26.15 ± 0.13 ppt (1.8σ).
- **Background:** the unit-free regression (bkgreg-out.txt) implies at most 0.023 ppt of fake dip in any sector.
- **Centroids:** dX +0.15 ± 0.13 mpix, dY +0.20 ± 0.11 mpix.
- **Quality flags and known systematics:** no event touches a momentum-dump cadence (QUALITY bit 32), and none falls near a listed sector-wide systematic time.
- **Flagged cadences:** two more full-depth events, at 1829.029 (s019) and 3287.573 (s073, an orbit that QLP flagged with bit 30 but which is clean).
- **Blind dip census:**
  - 33 dips at S/N ≥ 4: 14 are primaries and 12 are the secondary (phases 0.494–0.498).
  - The remaining dips are 0.6–1.2 ppt with S/N ≤ 4.7.
  - Nothing off-ephemeris is deeper than 2.1 ppt.
- **Control phases:** |depth| ≤ 0.11 ppt.
- **Eclipse shapes:**
  - Primary: near-V graze. A flat-bottomed shape (T12/T14 0.1) is worse by Δχ² 5,300, and 0.25 by Δχ² 1,160.
  - Secondary: T14 1.80 ± 0.18 h, giving e sin ω ≈ −0.03 ± 0.05. That is uninformative but consistent with Gaia.
- **Out-of-eclipse variability** (rotper-out.txt): spot modulation with a 4.6–5.0 d peak and 1.7–4.9 ppt semi-amplitude, i.e. near-synchronous rotation.
  - This is Gaia's "3.97 d ROT" signal.
  - The cos φ ≈ −2.6 ppt term at the orbital period, with sector scatter 1.4–1.9 ppt, is spots, not reflection.

## 3. Ephemeris
- **Primary:** P = 4.8136773 ± 0.0000007 d; T0 = 2786.95100 ± 0.00008 BTJD (E = 201).
- **Secondary − primary, per sector:** s019 0.49628, s059 0.49686, s060 0.49697, s073 0.49717; weighted mean 0.49681 ± 0.00017.
- **Versus Gaia:**
  - The eclipse is 1.3 h before Gaia's conjunction A at s019 and 2.2 h before it at s073; this grows slowly because Gaia's P is 0.7σ long.
  - e cos ω agrees at 0.8σ.

## 4. Independence
- **Other pipelines:**
  - TARS: 25.5–26.7 ppt in all 4 sectors.
  - TESS-SPOC PDCSAP and SAP: 24.5–26.3 ppt in s019, s060 and s073.
- **Difference images** (TESS-SPOC 200-s target pixel files):
  - The pixel with the largest flux loss is the target pixel, at S/N 29.8 and 32.4.
  - The loss-weighted centroid is on the target.
  - s019 has only 30-min target pixel files, too coarse for the estimator.
- **Dilution table** (Gaia DR3 within 60″; needed dip = 26 ppt × 10^(0.4ΔG)): G 17.21 at 45.3″ → 10,250 ppt; G 18.93 at 8.9″ → 49,700 ppt; five stars at G 20.2–21.1 → over 160,000 ppt. None can produce the signal.

## 5. Physics (physics-out.txt, occfit-out.txt)
- **Companion:** f(M) = 0.0319 M☉. With M1 = 1.20 ± 0.19 M☉, m2(90°) = 0.44 M☉ (range 0.40–0.48), an early-to-mid M dwarf.
- **Orbit scale:** a = 14.1 R☉; tangential speed 18.7 R☉/d at conjunction A.
- **Grazing geometry:** a central eclipse would last 3.9 h, so the observed 1.92 h needs i ≈ 84.6° and a mid-eclipse separation of 0.87 × (R1 + R2).
- **Which star is in front** (limb-darkened physical fit, 12 events at 200 s):
  - Transit of the primary fits with k 0.285, b 1.02, and gives **R1 = 1.02 R☉, matching TIC's 1.05 R☉**.
  - The occultation alternative needs the companion to supply 22% of the light, which is impossible here (expected light ratio L2/L1 ≈ 0.03).
  - So the M dwarf is in front at conjunction A. Conjunction B is predicted to eclipse (margin 0.16 R☉), and it is seen.
- **Secondary depth:** the secondary/primary ratio of 0.059 implies T2 ≈ 3200 K (blackbody). That is a little cool for 0.44 M☉, but the treatment is crude, so there is no material tension.
- **Ellipsoidal and beaming:** predicted 0.19 and 0.53 ppt, buried under 2–5 ppt of spots.
- **Heartbeat:** not relevant here; the eclipses are short and sharp at both conjunctions.
- **Gaia eccentricity: a counter-example to the wave-4 small-e pattern.** Gaia's e of 0.019 is only 2.3σ, yet the eclipses independently require e cos ω = −0.0050, 19σ from zero. This is a real small eccentricity, not a Lucy–Sweeney artefact. Worth a sentence in the paper.

## 6. Next predicted times (BTJD; 2026-10-21 ≈ BTJD 4335)
- **Primary** (M dwarf transits the primary, conjunction A): **4336.9551, 4341.7688, 4346.5825**, ± 0.4 min formal (allow ~2 min); then every 4.8136773 d.
- **Secondary** (M dwarf occulted, conjunction B): **4339.3466, 4344.1603, 4348.9739**, ± 1.2 min.

## What would settle it further
Reality and attribution are settled. What remains open:
- Spectroscopic Teff for both stars.
- Chromospheric activity, which the near-synchronous spots predict.
- A joint RV + light-curve fit for i, R2 and e cos ω.

## Row fixes
- Events: 17 (15 clean + 2 from flagged cadences).
- Depth: 25.97 ppt.
- P: 4.8136773(7) d.
- Secondary: 1.54 ppt at phase 0.4968.
- VSX ROT entry is a type revision.
- Disclose the SPOC TCE detection.

## Files
- **Scripts:** vet.py, vetlib.py, sec2.py, sectime.py, bkgreg.py, rotper.py, missing.py, flagged.py, indep.py, tpfdiff.py, occfit.py, physics.py, phys_ecc.py, gaiatap.py, morecats.py, extracats.py, mastlc.py, dvcheck.py, simbad_lamost.py, nextecl.py.
- **Outputs:** the matching `*-out.txt` files, fold_oc.png, events.png, sec2.png, the tpfdiff images, gaia.json, nb60.json and vet-results.json.
- **Data:** `C:\Home\sky\data\qlp-sb-p20-60\pervet55214475\`.
