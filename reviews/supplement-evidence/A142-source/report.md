# TIC 98952099 (TYC 2971-946-1, Gaia DR3 926025430401990528): per-object vet
Opus 5.5 subagent for Fable 5, 2026-10-19. A first subagent died after running vet.py; this one resumed from its files on disk. Batch row: G 11.46, P 5.95570 d, 10.4 ppt, 11 events, dphi +0.023.

**VERDICT: CONFIRMED.** A late-M dwarf transits an F subgiant at Gaia conj A. NEW: its occultation is detected at phase 0.5012 (0.65 ppt, S/N 6.1). The G 14.23 neighbour 9.5" away is excluded by in-eclipse centroids in all three sectors.

**Star and orbit**
- G 11.46, Tmag 11.06. TIC: Teff 6070 K, R 2.23 ± 0.12, M 1.13, d 543 pc, contratio 0.085. RUWE 1.08. GSP-Phot logg 3.83.
- Gaia NSS SB1 (full archive row with corr_vec, `gaia.json`): P 5.956743 ± 0.000662 d, e 0.033 ± 0.044, ω 3 ± 58°, Tp −0.394 ± 0.947, K1 16.03 ± 0.61 km/s, significance 26.5.

**1. Archives**
- `cats.py` (`cats-out.txt`): VSX, ASAS-SN, Prša, IJspeert and Kostov all none. SIMBAD lists TYC 2971-946-1 as [SB*] only.
- `morecats-out.txt`: no SB9 or WDS entry. ExoFOP: no TOI or CTOI.
- Gaia vari tables are empty.
- Web search on the TYC, TIC and Gaia ids: nothing.
- MAST CAOM lists two SDSS/eBOSS spectra at this position (plates 3676 and 8276, MJD 55186 and 57067). Those are possible extra RV epochs, not EB prior art.
- Not previously catalogued as an eclipsing binary.

**2. Eclipses** (raw QLP SAP, QUALITY == 0; `vet-out.txt`, `events.png`, `fold_oc.png`)
- **Primaries:** 11 measured (s020 ×4, s047 ×4, s060 ×3), each S/N 28–37.
  - Weighted depth 11.05 ± 0.10 ppt. Constancy χ² 17.3/10. Per sector 10.73 / 10.99 / 11.49.
  - Odd 11.00 ± 0.15 vs even 11.08 ± 0.14.
- **Shape:** trapezoid T14 3.72 h, T12 1.30 h (T12/T14 0.35), flat 1.12 h. Fully V is worse by Δχ² +128, so the bottom is flat.
- **Systematics:**
  - One event window (s047 E124) contains a bit-32 cadence; its depth of 10.38 ppt is in family.
  - No event near a listed sector-wide systematic.
  - Background regression: the largest fake dip background could produce is 0.05 ppt.
  - QLP centroids in eclipse: dX 0.00 ± 0.19, dY −0.14 ± 0.30 mpix.
- **Controls:** off-eclipse phases within ±0.15 ppt. The one exception is phase 0.5, at +0.67 ± 0.10 ppt: the secondary.
- **Blind census:** 14 dips at S/N ≥ 4. 11 are the primaries. The other three are ≤ 1.95 ppt.
- **Jackknife** (`sec-out.txt`):
  - Dropping any one event moves P by ≤ 5.4 ppm-d, and each dropped event's O−C sits within 2σ of the rest.
  - Dropping a whole sector leaves P in 5.955673–5.955684.
- **Secondary — NEW** (own fixed-shape test `sec2.py`; `sec2-out-0.500-3.7h.txt`, `sec2_0.500_3.7h.png`):
  - Depth 0.647 ± 0.105 ppt (S/N 6.1) at phase 0.5012 ± 0.0008, measured from a fine scan.
  - The look-elsewhere scan reaches S/N 6.1 at 0 of 39 control centres (95th percentile 1.98). Random-phase S/N rms is 1.02.
  - 9 of 10 events are positive. Per sector: s020 0.75 ± 0.17, s047 0.44 ± 0.19, s060 0.73 ± 0.19. Constancy χ² 4.4/9.
  - `sec.py`'s free-shape global fit had wandered to a 12.8 h template and missed it. Do not cite that file's "no secondary".

**3. Ephemeris and Gaia**
- P = 5.955676 ± 0.000004 d, T0 = 2444.81721 ± 0.00034 BTJD (E = 100). χ² 10.6/9. O−C rms 1.6 min.
- vs Gaia P: −0.001066 d = −1.61σ.
- Gaia conjunctions (Monte Carlo with the full covariance): the eclipses sit on **conj A**, at −1.04σ (s020), −1.32σ (s047) and −1.39σ (s060). In phase that is −0.027, −0.051 and −0.063. The growing offset comes from the −1.6σ P difference.
- Gaia predicts phase(B) − phase(A) = 0.516 ± 0.021. Observed: 0.5012 ± 0.0008.
- Photometric **e cos ω = +0.0019 ± 0.0013**, against Gaia's +0.026 ± 0.033 (0.7σ). The orbit is circular to within ~0.002 in e cos ω.
- e sin ω is not measurable from durations at this S/N.

**4. Independence**
- **TESS-SPOC PDCSAP** (`indep-out.txt`): s20 10.47 ± 0.16, s47 10.31 ± 0.13, s60 9.82 ± 0.17 ppt. SPOC-SAP: 9.4–9.7 ppt.
- **Ellipsoidal A2** is +0.16 to +0.31 ppt in SPOC. QLP c2 is −0.285 ppt (minima at the conjunctions).
- **TESS-SPOC TPF difference images**, s20/s47/s60 (`tpfdiff-out.txt`):
  - The target is favoured over the G 14.23 neighbour at 9.5" by Δχ² 1180 / 1030 / 1960.
  - The loss-weighted centroid lands on the target pixel position in s20 and s47, and within 0.13 px of it in s60.
  - The neighbour would need a 66–124 ppt dip of its own.
- **Own centroid-shift test** (`censhift.py`, `censhift-out.txt`): this is the decisive test for the 9.5" neighbour.
  - Measured in-eclipse shifts: s20 (+0.40 ± 0.13, −0.03 ± 0.13), s47 (+0.45 ± 0.10, −0.16 ± 0.13), s60 (+0.34 ± 0.16, +0.08 ± 0.14) mpix.
  - Predicted if the target owns the dip: (+0.40, +0.44), (+0.40, −0.78), (+0.40, −0.14) mpix, giving χ² 12, 22 and 2.5.
  - Predicted if the G 14.23 neighbour owns it: (−3.9, −0.7), (−3.8, −1.7), (−3.9, −1.3) mpix, giving **χ² 1069, 1956 and 844**.
- **Batch diffimg** (s020): peak on target. The offset of 2.6" is a fraction of the 9.5" separation.
- **Neighbours** (fractional dip each would need = 11.05 ppt × 10^(0.4 Δm)):
  - G 14.23 @ 9.5": 141 ppt (excluded above)
  - G 15.73 @ 35": 565 ppt (centroid χ² ≥ 11,700)
  - G 16.69 / 16.70 @ 83" / 72": > 100% (impossible)

**5. Physics** (`phys-out.txt`, `transfit-out.txt`, `transfit-out-contam.txt`)
- f(M) = 0.00254 Msun. With M1 1.13, m2(i = 90°) = 0.162 Msun; m2 = 0.164 at the fitted i ≈ 82°. a = 15.1 Rsun.
- Circular orbit: central T14 would be 7.3 h; observed 3.72 h.
- **Limb-darkened eclipse fit** (v_t 15.93 Rsun/d, LD 0.33/0.23), with no dilution correction:
  - Best R1 1.90, k 0.120 (R2 0.23 Rsun), b 0.90. The 2σ range is R1 1.90–2.20, R2 ≥ 0.23.
  - The TIC R1 of 2.23 is Δχ² +8 worse.
  - With the TIC contratio of 0.085 applied, the grid runs to a k = 0.49 deep graze at the k edge. That solution is unphysical for f(M) (a ~1 Rsun companion would be about a solar mass and bright). It shows the k–b degeneracy, not a competing answer.
  - An R2 of about 0.23 Rsun for a 0.16–0.18 Msun dwarf means ~15% inflation, or R1 nearer 1.9: normal-sized tension.
- **Secondary as a test of the companion:**
  - The depth ratio 0.65 / 11.05 corrected for limb darkening gives a TESS-band surface-brightness ratio of about 0.047.
  - That implies **T2 ≈ 3000 K** (Planck at 0.8 µm, T1 6070 K). This is exactly what a 0.16–0.18 Msun M dwarf should be.
  - The occulted fraction is ~0.9 of its disc, consistent with the same chord at B (circular orbit, same impact parameter).
- **Ellipsoidal:** predicted 0.58 ppt at R1 2.23, or about 0.36 ppt at R1 1.9. Observed 0.16–0.31 ppt. Same star, same order.
- **Which star is in front:** conj A, so the M dwarf transits the F subgiant. Conj B, at phase 0.5012, is the M dwarf's occultation.
- **Heartbeat:** irrelevant. e ≈ 0, the dip is flat-bottomed and 3.7 h long, and SPOC reproduces it.

**6. Verdict and predictions**
- **CONFIRMED.** Deciding numbers:
  1. The in-eclipse centroids exclude the 9.5" G 14.23 neighbour at χ² 844–1956 in each of three sectors, and the difference images agree.
  2. Secondary at phase 0.5012 ± 0.0008 (S/N 6.1, look-elsewhere false-alarm rate 0/39). It gives e cos ω +0.0019 ± 0.0013, matching Gaia's near-circular orbit, and its depth gives T2 ≈ 3000 K, matching f(M).
  3. P within 1.6σ of Gaia, with the eclipses on conj A at about −1.2σ. QLP, TESS-SPOC PDCSAP and SPOC-SAP agree (9.4–11.5 ppt).
- **Paper row fixes:**
  - depth 10.4 → **11.05 ppt** (QLP trapezoid; TESS-SPOC PDCSAP 9.8–10.5).
  - P → **5.955676(4) d**.
  - **Add the secondary: 0.65 ± 0.11 ppt at phase 0.5012.**
  - n stays 11 primaries; 10 secondary windows are covered.
  - The dphi sign is **negative**: the eclipse is 0.027–0.063 in phase earlier than Gaia's conj A, growing with time from the P offset.
  - Note the 9.5" neighbour as excluded, so it must not be catalogued as an eclipser itself.
- **Next primaries** (±2 min): BTJD **4404.235, 4410.190, 4416.146**.
- **Next secondaries** (±7 min): BTJD **4407.220, 4413.175, 4419.131**.
- **To settle further:** RVs from the two archival eBOSS spectra against the Gaia orbit, and a spectroscopic R1 (TIC 2.23 vs eclipse ~1.9 Rsun).
