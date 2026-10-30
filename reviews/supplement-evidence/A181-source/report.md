# TIC 124856476 (TYC 7081-350-1, Gaia DR3 2891700638862696576): adversarial check

Checker: Opus 5.5, 2026-10-21. This resumes checker #1 (killed by a usage limit after steps 1-4). I re-verified steps 1-4 with new code (`verify.py`) and added a TESScut s98 pixel check. Step 5 uses a reproduced ebfit, a bootstrap of its errors, and `physics2.py`.

## Verdict: CONFIRMED (secure)
This is a detached, eccentric, double-eclipsing binary at P = 21.680622 d.
- The deep eclipse is a grazing transit of the G-type primary by an M dwarf of about 0.5 Msun. The shallow eclipse is the total occultation of that M dwarf.
- Five full A eclipses and six B eclipses span 2018-2025 and were measured in three pipelines (QLP, TESS-SPOC, TGLC) plus two TESScut sectors. They sit on the target pixel.
- One geometry reproduces the depths, durations and phase, and it agrees with Gaia's SB1 orbit and the TIC primary.
- Prior art: Kostov+2025 table2 only (unvetted ML flags), so the star is uncatalogued as an EB.

## Deciding numbers
- **A eclipses:** s6 1473.1146, s7 1494.7947 (TESS-SPOC; QLP has only part of it), s33 2210.2552, s87 3684.5375, s98 4009.7477 and 4031.4276. Depth is 9.6-10.0% (s6, s33, s87). Trapezoid T14 is 6.4 h; it is V/U-shaped.
- **B eclipses:** s7 1499.7869, s87 3667.8488 and 3689.5279, s98 3993.0577 (flagged), 4014.7393, and 4036.4205 (flagged). Depth is 1.73-1.80% (s7, s87); T14 is 5.1-5.3 h, with a flat bottom of about 1.4 h in the model.
- **My own refit** (`verify.txt`, raw SAP, all cadences) agrees within 0.7 min. Two half- or all-flagged B eclipses differ by 2.2 min.
- **s98 depths.** QLP has A at 8.4% and B at 1.49% in s98. In the s98 TESScut pixels, A is 8.9-9.2% and B is 1.6-1.7%, the same in 1x1, 3x3 and 5x5 apertures, with the deficit on the target pixel (`diff_s98.txt`). The A/B ratio is 5.6 in both sectors. So the shallowing is mostly the QLP s98 aperture/background, not physics.
- **Ephemeris A:** T0 = BTJD 2210.25550 +- 0.00040, P = 21.680622 +- 0.000006 d, chi2 1.2/3, rms O-C 0.48 min.
- **Ephemeris B:** T0 = BTJD 2215.24730 +- 0.00060, P = 21.680621 +- 0.000008 d, chi2 6.0/4. B-A phase is 0.23024.
- **Against Gaia.**
  - Period: Gaia's 21.68101 +- 0.00324 d differs from TESS by +0.12 sigma.
  - Conjunction times: every measured eclipse lies within 0.44 sigma of Gaia's predicted conjunction. A runs about -0.15 d and B about +0.06 d.
  - B-A phase: Gaia predicts 0.2202 +- 0.0066; I measure 0.23024 (+1.5 sigma).
- **Eclipse-model fit** (s87, two LD spheres, Keplerian; chi2/N 1.00, rms 0.73 ppt). I reproduced checker #1's fit exactly. It needs start values near e cos(omega) = -0.43; the default start finds a wrong minimum. The Hessian errors were NaN, so I replaced them with a 30-sample block bootstrap, which probably underestimates them.
  - e = 0.4643 [0.4614, 0.4663]; omega = 201.6 [200.5, 202.4] deg; i = 88.35 deg.
  - k = R2/R1 = 0.357; J = 0.139; L2/L1 (TESS) = 0.0178.
  - Compared with Gaia: e 0.4764 +- 0.0103 (-1.2 sigma); omega 198.88 +- 2.66 (+1.0 sigma).
  - ebfit.py prints "primary omega 21.7". That is a label slip, the same as for TIC 39307147: its Z>0 axis points toward the observer, and the correct value is 201.7 deg.
- **Pixels and neighbours.** In the s87 and s98 difference images, the deficit is 0.4-1.4" (A) and 2.5-3.0" (B) from the light centroid, and the peak is on the target pixel. Nothing within 60" is brighter than G 16.29 (Delta G 5.2), so a neighbour would need a dip above 200% for B and above 1100% for A.
- **Census.** Nothing above 0.3% outside the eclipses, except the s87 sector-start ramp at 3663.3 and an s98 pre-gap offset at 4038.4-4038.6. That offset is common-mode: 25 of 202 stars dip there.

## Physics (step 5)
- **Masses.** f(M) = 0.0533 [0.0505, 0.0563] Msun (K1 32.15 km/s). With the TIC M1 = 1.06 and i = 88.35 deg, m2 = 0.51 Msun and a = 38.0 Rsun.
- **Primary.** R1 = 0.0347a = 1.32 Rsun (TIC 1.318). logg1 = 4.22 (Gaia GSP-Phot 4.18).
- **Companion.** R2 = 0.47 Rsun, as expected for a 0.5 Msun dwarf (about 0.47). The surface-brightness ratio gives T2 of about 3650 K (blackbody), close to a 0.5 Msun dwarf (about 3750 K).
- **Predicted occultation depth.** L2/(L1+L2) = 1.74%; observed 1.73-1.80%.
- **A eclipse** (nu = 90 deg - omega): the companion passes in front of the primary. Separation 0.947a, b_A = 0.78 > 1-k = 0.64, so the transit is grazing/partial. That explains why A (about 10%) is shallower than k^2 = 12.8% and why it is V/U-shaped. Model T14 is 6.81 h; trapezoid 6.4 h.
- **B eclipse:** the primary passes in front, and the companion is totally occulted (b_B = 0.55 < 0.64 in 100% of bootstrap resamples). Separation 0.669a, so the eclipse is faster. Model T14 5.38 h, T23 1.41 h; trapezoid T14 5.2 h, flat about 1.9 h.
- **Durations.** The B/A duration ratio of 0.81 is larger than Gaia's b=0 value of 0.73 (+2.5 sigma). The non-zero impact parameters explain the difference fully.
- **RV amplitude.** Gaia's rv_amplitude_robust of 67.3 km/s is close to 2K1 = 64.3 km/s.
- **Caveat: RUWE 2.22.** The inner orbit's photocentre wobble is only about 0.21 mas. TIC 39307147 has a similar wobble (about 0.18 mas) at a similar G and RUWE 1.02. So RUWE 2.2 hints at an unresolved further companion (ipd_frac_multi_peak = 0). Any third light would dilute both eclipses equally. It cannot be large, because the fitted R1 matches the TIC radius. It does not affect the verdict.

## Next predicted eclipses (BTJD; linear ephemeris, propagated 1-sigma)
- A (about 10%, about 6.8 h contact to contact): 4334.9565 +- 1.1 min (2026-10-21, about 11 UT), 4356.6371 +- 1.1, 4378.3177 +- 1.1, 4399.9983 +- 1.1 min
- B (about 1.75%, about 5.4 h): 4339.9482 +- 1.5 min, 4361.6288 +- 1.5, 4383.3094 +- 1.5, 4404.9900 +- 1.5 min
- General formulas: A = 2210.25550 + 21.680622 E; B = 2215.24730 + 21.680621 E.

## What would settle it further
- An SB2 or IR spectrum to measure K2 (expected about 67 km/s) and the true masses. A partial transit makes i well constrained.
- High-resolution imaging or Gaia DR4 astrometry to explain RUWE 2.2, which would test for third light.
- Further TESS sectors to test apsidal motion. With e = 0.46 and P = 21.7 d it should be slow.

## Archives queried (step 1)
- **cats.py --r 60** (rerun today): VSX none, ASAS-SN none, Prsa+2022 none, IJspeert+2024 none, Kostov t3/t4 none. The only hits are Kostov t2 at 0.001" and SIMBAD "TYC 7081-350-1" typed SB*.
- **Gaia DR3** vari_summary and vari_eclipsing_binary: 0 rows (phot_variable_flag NOT_AVAILABLE).
- **VSX** 60", **SB9** 30" and **WDS** 30": 0.
- **ExoFOP:** no TOI or CTOI, contamination 0.0026.
- **Web search** on "TYC 7081-350-1" / "TIC 124856476": nothing about this star.
- **MAST:** QLP (s6, s7, s33, s87, s98), TESS-SPOC (s6, s7, s33), TGLC/T16/ELEANOR-LITE (s6, s7), TARS (s6, s7, s33, s87) and TASOC (s6).

Files: verify.py/.txt, verify_spoc.txt, diff_s98.txt + diff_*_s98_*.png/json, ebfit_s87_rerun.txt, ebfit_boot.py/.txt/.npy, physics2.py/.txt (new). ebfit.json was regenerated identically, and checker #1's copy is kept as ebfit_checker1.json. Checker #1's other files are re-verified.
