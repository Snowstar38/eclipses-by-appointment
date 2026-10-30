# REPORT — TIC 348784186 (TYC 5452-573-1, Gaia DR3 5736614545403168512)

Opus 5.5 subagent, 2026-10-21, wave 5. Fresh folder; no earlier session worked this star. (Saved by the parent session; the file-write tool refused REPORT.md for the subagent.)

## Verdict: CONFIRMED. A detached, circular, grazing SB1 with both eclipse kinds strong and on target.

Deciding numbers:
- **Primary eclipses:** 23 individual events in 5 sectors (s008, s035, s061, s088, s099), each at S/N 63–149. Depth 26.41 ± 0.05 ppt, T14 3.00 h, T12/T14 0.40 (V-ish, grazing).
- **Secondary eclipses:** 23 individual events, each at S/N 28–73. Depth 11.61 ± 0.04 ppt, T14 2.94 h.
- **Period:** 4.0868675 ± 0.0000004 d from the primaries and 4.0868686 ± 0.0000007 d from the secondaries. Gaia's is 4.086794 ± 0.000064 d, so the difference is **+1.14σ**.
- **Which conjunction:** the deeper eclipse sits on Gaia conjunction A (primary eclipsed) at **+0.61σ to +1.01σ** in every sector. The drift across sectors comes from Gaia's P being short. The shallow eclipse sits on conjunction B at +1.5σ to +1.8σ.
- **Phase separation** 0.50012 ± 0.00004 gives e cos ω ≈ +0.0001 ± 0.0001, i.e. circular.
  - Gaia has e cos ω −0.0095 (e 0.0097 ± 0.0073), and Gaia's predicted B−A phase of 0.4953 ± 0.0038 is 1.2σ away.
  - This is the wave-4 small-e pattern, but mild here.
- **Same source for both eclipse kinds:** the primary/secondary depth ratio is 2.23–2.36 in every sector. In s099 both depths drop together (26.9→23.8 and 11.9→10.5 ppt), which is a sector dilution change.
- **On target:** TESS-SPOC difference images in s035 and s061 have their max-loss pixel on the target at S/N 65 and 109. The target fit beats every neighbour by Δχ² > 9,000. The s061 secondary difference image is also on target (S/N 42).

## 1. Archives
- **cats.py --r 60:** no VSX or ASAS-SN entry, and no EB-table hits. SIMBAD has only TYC 5452-573-1, typed [SB*].
- **Gaia DR3:** vari_summary and vari_eclipsing_binary are empty; RUWE 1.10.
- **SB9, WDS, J/AJ/160/111:** none.
- **ExoFOP:** no TOI or CTOI, and no imaging, spectra or companions.
- **Extra VizieR cones at 30″** (ATLAS, ZTF, WISE variables, GCVS, VSX, ROSAT, 2RXS, 4XMM, ASAS-SN, LAMOST, APOGEE, Prša+2022): no rows, and the control cones returned rows. J/A+A/674/A16 is not an EB table.
- **Web search** ("TYC 5452-573-1" OR "TIC 348784186" eclipsing binary): no page mentions the star.
- **Batch receipts:**
  - c3-vetsum: dphi +0.002/−0.492, ATTR.
  - c3-sapdepth: alternating ~25/~11 ppt.
  - **diffrun s088: peak_on_target false, deficit−target 3.51″, n_possible 1 (the G 13.71 at 34.7″). The TPFs in §4 contradict this.** The likely cause is stacking at P/2 (mixing the 26- and 12-ppt eclipses) plus the wave-4 centroiding artefact; deficit−light is only 1.9″.
- **No prior art.** This is a new EB.

## 2. Measurements (QLP SAP, Q==0, no trimming)
- **Per-sector depths:** primary 27.02, 26.89, 27.16, 26.95 and 23.82 ppt. Secondary 11.44, 11.82, 12.17, 11.93 and 10.53 ppt.
- **Odd vs even primaries:** 26.35 ± 0.06 vs 26.46 ± 0.06 ppt.
- **Shape:** a pure V is worse by Δχ² 700 and a box by Δχ² 18,700.
- **Harmonics (ppt):** cos 2φ −1.10 (ellipsoidal, correct sign); cos φ −0.42 (reflection, brightest at phase 0.5); sin φ +0.56 ± 0.48 (beaming sign, weak).
- **Background:** the unit-free regression implies |ΔF| ≤ 0.11 ppt per sector, against 14–17 ppt (primary) and 6.5–7.4 ppt (secondary) in the same windows. vet.py's dBKG column has the known broken units and is ignored.
- **Centroids:** QLP centroid shifts are under 1 mpix.
- **Quality flags:**
  - 4 primaries touch a bit-32 cadence, and none sits at a listed systematic time.
  - Where flagged cadences cover an eclipse they show the same dip (27.4–28.3 ppt).
- **Control phases** 0.125–0.875 (excluding 0.5): |depth| ≤ 0.07 ppt, n 20–23 each.
- **Blind dip census:** 47 dips at S/N ≥ 4: 23 primaries, 22 secondaries, and two 1.5–1.8-ppt dips at S/N < 5. One of those two is at the s061 systematic (2981.9). Nothing off-ephemeris reaches half the eclipse depth.

## 3. Ephemerides
- **Primary (conjunction A):** T0 = 2978.32495 ± 0.00007 BTJD, P = 4.0868675 ± 0.0000004 d. χ²/dof 41/21, O−C rms 0.5 min.
- **Secondary (conjunction B):** T0 = 3143.84359 ± 0.00016 BTJD, P = 4.0868686 ± 0.0000007 d. χ²/dof 138/21, O−C rms 1.0 min; the scatter is from the 30-min and 10-min cadence sectors.
- **P_sec − P_pri** = +0.10 ± 0.07 s: no apsidal motion.
- **Secondary offset from phase 0.5:** +0.7 ± 0.25 min. The Rømer delay accounts for about 16 s of it, leaving e cos ω ≈ +0.0001.
- **e sin ω** from the duration ratio is −0.010 ± 0.010; Gaia gives −0.002.
- **Against Gaia** (Monte Carlo with corr_vec): conjunction A − observed primary runs from +0.27 h (s008) to +1.36 h (s099).

## 4. Independence
- **Other pipelines:** TESS-SPOC exists for s008, s035 and s061. GSFC-ELEANOR-LITE, T16, TGLC and TARS also exist and were not used.
- **TESS-SPOC primary depths:** PDCSAP 26.2–26.8 ppt and SPOC-SAP 24.6–25.5 ppt. Ellipsoidal amplitude 1.1–1.7 ppt.
- **Difference images:**
  - s061 primary: target χ² 5,932 (implied own dip 20.4 ppt), against 29,175 for the G 15.91 star and 41,189 for the G 13.71 star.
  - s035 primary: target χ² 2,817, against 9,683 or more for every neighbour.
  - s061 secondary: target χ² 785, against 4,335.
- **Neighbour dilution table** (needed dip = depth × 10^(0.4ΔG)):

  | Neighbour | Primary needs | Secondary needs |
  |---|---|---|
  | G 13.71 at 34.4″ | 595 ppt | 261 ppt |
  | G 15.04 at 45.9″ | ≈2,000 ppt | — |
  | G 15.91, 16.48, 16.53, 16.68 (20–49″) | >1,000 ppt | — |
  | G 14.08 at 68″ (outside 60″) | 835 ppt | — |

  Only the G 13.71 star is arithmetically possible, and the pixels exclude it by Δχ² +35,000 (s061) and +12,000 (s035).

## 5. Physics
- **Mass function** f(M) = 0.1126 M☉ (K1 64.31 ± 0.41 km/s). With M1 = 1.22 ± 0.19 M☉, m2(90°) = 0.76 M☉ (0.69–0.83), so a K dwarf. q ≈ 0.62, a ≈ 13.5 R☉.
- **Which star is in front:** the deeper eclipse is at conjunction A, the F star eclipsed, as Gaia's convention requires.
- **Companion temperature:** the depth ratio 0.44 gives the surface-brightness ratio J. Two-sphere fits to both folds give J = 0.39–0.47, so T2 ≈ 4750–5000 K. That is a K1–K2 dwarf of exactly the f(M) mass.
- **Geometry:** grazing, b ≈ 1–1.6 R1, i ≈ 80–84°. With third light fixed at the TIC contamination ratio, R1/a = 0.112, so R1 ≈ 1.5 R☉. The k–b–third-light degeneracy is strong; with free third light the fit runs off to an unphysical k = 1.2.
- **Ellipsoidal:** predicted ≈ 1.1 ppt for R1 1.5 R☉, observed 1.10–1.23 ppt. TIC's R1 of 2.0 R☉ would give 2.5 ppt.
- **Open item, radius tension:** the eclipse and ellipsoidal fits want R1 ≈ 1.5 R☉, against TIC 2.0 R☉ and ≈ 1.8 R☉ from Gaia logg. The companion's light inflates the single-star radius, which explains part of it. It does not affect the verdict.
- **Not a heartbeat:** the orbit is circular and both eclipses are short.

## 6. Next predicted eclipses (BTJD; formal errors 0.2–0.4 min, allow ±2 min)
- **Primary** (conjunction A, ~26 ppt): **4335.1650, 4339.2518, 4343.3387**, then every 4.0868675 d.
- **Secondary** (conjunction B, ~11.6 ppt): **4337.2092, 4341.2961, 4345.3830**, then every 4.0868686 d.

## What would settle it further
- A spectrum to detect the K dwarf. As an SB2 (K2 ≈ 100 km/s) it would give masses.
- A spectroscopic Teff and log g, for R1.
- High-resolution imaging for third light.

## Files in vet348784186
- **Scripts:** vet.py (patched: secondary mask, T14 ceiling, T14G mask width), vetlib.py, ecosw.py, ebfit.py, flagged.py, sec2.py, bkgreg.py, indep.py, tpfdiff.py, physics.py, gaiatap.py, mastlc.py, morecats.py, extracats.py.
- **Primary-eclipse outputs:** vet-out.txt, vet-results.json, fold_oc.png, events.png.
- **Secondary-eclipse outputs (secv\):** vet-out.txt, vet-results.json, fold_oc.png, events.png, tpfdiff-sec-out.txt, bkgreg-out.txt.
- **Analysis outputs:** ecosw-out.txt, sec2-out.txt, ebfit-out.txt, ebfit-dfix-out.txt, ebfit*.png, bkgreg-out.txt, flagged-out.txt, flagged-sec-out.txt, indep-out.txt, tpfdiff-out.txt, tpfdiff_35.png, tpfdiff_61.png, physics-out.txt.
- **Archive outputs:** cats-out.txt, gaiatap-out.txt, morecats-out.txt, extracats-out.txt, mastlc-list.txt, mastlc-dl.txt.
- **Data:** `C:\Home\sky\data\qlp-sb-p20-60\pervet348784186\`.
