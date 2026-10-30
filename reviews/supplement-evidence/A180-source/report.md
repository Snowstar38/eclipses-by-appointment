# TIC 39307147 (TYC 2609-823-1, Gaia DR3 4600354696406809984): adversarial check

Checker: Opus 5.5, 2026-10-21. This resumes checker #1 (killed by a usage limit after steps 1-4). I reran or spot-checked steps 1-4 with new code (`verify.py`) and wrote step 5 (`physics2.py`).

## Verdict: CONFIRMED
This is a detached, eccentric, double-eclipsing binary at P = 23.421703 d. Both eclipse kinds repeat across 2020, 2022 and 2024, and two pipelines recover them. The eclipses sit on the target pixel. One geometry fits both eclipses, and that geometry agrees with Gaia's SB1 orbit (e, omega, K1, P) and with the TIC primary. Prior art: Kostov+2025 table2 only (an unvetted ML flag list), so the star is uncatalogued as an EB.

## Deciding numbers
- **Eclipses.** There are 6 A eclipses (s25, s26, s52, s53, s79, s80). Depth is 24.4-25.5% in QLP and 23.4-23.9% in TESS-SPOC; trapezoid T14 is 6.8-7.0 h. There are 5 usable B eclipses (s25, s26, s52, and two in s80) at 9.8-10.2% and T14 7.8-8.0 h. A sixth B in s79 is recovered in all-flagged data at 3458.562 +- 9.5 min and is consistent with the ephemeris, but it was not used.
- **My own refit** (`verify.txt`, all cadences, raw SAP) matches checker #1 to within 0.6 min in time and 0.3% in depth.
- **Ephemeris A** (deep): T0 = BTJD 1989.52348 +- 0.00059, P = 23.421703 +- 0.000013 d, chi2 2.0/4, rms O-C 0.76 min.
- **Ephemeris B**: T0 = BTJD 2006.41760 +- 0.00116, P = 23.421703 +- 0.000025 d, chi2 12/3, rms 1.8 min. The s52 B eclipse is 2.9 min early, in a half-flagged segment. B-A phase is 0.72130.
- **Against Gaia.** Gaia gives P = 23.41591 +- 0.00396, which differs from TESS by -0.0058 d (-1.5 sigma). That difference is the whole reason Gaia's conjunctions run 0.56 to 0.93 d early, growing with epoch. Every measured eclipse lies within +1.5 sigma of its Gaia-predicted conjunction.
  - Gaia's e and omega predict a B-A phase of 0.7274 +- 0.0073; I measure 0.72130 (-0.8 sigma).
- **Eclipse-model fit** (two LD spheres, Keplerian; chi2/N 1.00, rms 1.16 ppt): e = 0.3595, omega = 9.45 deg, i = 89.06 deg, R1/a = 0.0333, R2/a = 0.0168, J_TESS = 0.429.
  - Compared with Gaia: e 0.368 +- 0.012 (-0.7 sigma) and omega 6.16 +- 3.63 (+0.9 sigma).
  - Checker #1's ebfit.py prints "primary omega 189.45". That is a label slip: the model's Z>0 axis points toward the observer, which already absorbs the 180 deg. The value is 9.45 deg in Gaia's convention. e cos(omega) +0.3546 and the phase both have the same sign as Gaia's.
- **Pixels and neighbours.**
  - TESScut s80 difference images: the deficit centroid is 0.3" (A) and 0.7" (B) from the light centroid, the peak deficit is on the target pixel, and the depth is the same in 1x1, 3x3 and 5x5 apertures.
  - No Gaia source within 60" is brighter than G 17.4 (Delta G >= 6.2). Every neighbour would need a dip above 2900%. The nearest bright star (G 15.1, 65.7") shows only spill-over.
- **Census.** Nothing above 0.3% outside the eclipses in s25, s53, s79 or s80. The only features are short 0.3-0.7% wiggles in the noisy, partly flagged s26 and s52 segments.

## Physics (step 5)
- **Masses.** f(M) = 0.107 [0.102, 0.112] Msun (K1 37.87 km/s). With the TIC M1 = 1.07 Msun and i = 89.06 deg, m2 = 0.69 Msun and a = 41.6 Rsun.
- **Primary.** R1 = 0.0333a = 1.39 Rsun. That gives logg1 = 4.18; Gaia GSP-Phot says 4.14, and TIC R is 1.50.
- **Companion.** R2 = 0.70 Rsun, as expected for a 0.69 Msun dwarf (about 0.66-0.68). The surface-brightness ratio gives T2 of about 4690 K (blackbody, T1 = 5888 K), slightly warmer than a 0.69 Msun dwarf (about 4400-4500 K). That is within the crudeness of the blackbody approach.
- **Light ratio.** L2/L1 = 0.11 in the TESS band. Gaia's SB1 classification is still plausible at that ratio, but light from the companion may slightly dilute K1.
- **A eclipse** (nu = 90 deg - omega): the companion passes in front of the primary. Separation 0.822a, b = 0.41, a full transit, model T14 7.61 h.
- **B eclipse:** the primary passes in front, and the companion is totally occulted (b = 0.46 < 1-k = 0.495). Separation 0.925a, model T14 8.48 h, flat 1.1 h. Depth is L2/(L1+L2) = 9.87%.
- **Consistency.** The B/A duration ratio follows from e sin(omega) > 0. Depth A is consistent with k^2 = 0.255 diluted by the companion's light, after limb darkening. Gaia's rv_amplitude_robust of 78.4 km/s is close to 2K1 = 75.7 km/s.
- **Trapezoid versus model.** The trapezoid T14 values are shorter than the model contact-to-contact values (A 6.9 vs 7.6 h, B 7.85 vs 8.5 h). This is the usual trapezoid bias on limb-darkened or occultation ingress, not a tension in the data.

## Next predicted eclipses (BTJD; linear ephemeris, propagated 1-sigma)
- A (deep, ~25%, about 7.6 h contact to contact): 4355.1155 +- 2.0 min, 4378.5372 +- 2.0 min, 4401.9589 +- 2.1 min, 4425.3806 +- 2.1 min
- B (~10%, about 8.5 h): 4348.5879 +- 4.0 min, 4372.0096 +- 4.0 min, 4395.4313 +- 4.0 min, 4418.8530 +- 4.1 min
- General formulas: A = 1989.52348 + 23.421703 E; B = 2006.41760 + 23.421703 E.

## What would settle it further
- An SB2 spectrum, possibly in the red or IR, where L2/L1 rises. The companion's K2 of about 59 km/s would give true masses with i = 89.06 deg.
- Any further TESS sector, or one ground-based eclipse at the times above, to tighten P and check for apsidal motion. The B O-C chi2 of 12/3 hints at extra scatter, but it is driven by one half-flagged s52 point.
- Gaia DR4 epoch RVs, which would check the 0.0058 d period offset directly.

## Archives queried (step 1)
- **cats.py --r 60** (rerun today): VSX none, ASAS-SN none, Prsa+2022 none, IJspeert+2024 none, Kostov+2025 t3/t4 none. The only hits are Kostov t2 at 0.001" and SIMBAD "TYC 2609-823-1" typed SB*.
- **Gaia DR3** vari_summary and vari_eclipsing_binary: 0 rows. phot_variable_flag is NOT_AVAILABLE.
- **VSX** 60", **SB9** 30" and **WDS** 30": 0.
- **ExoFOP:** no TOI or CTOI, contamination ratio 0.0037.
- **Web search** on "TYC 2609-823-1" / "TIC 39307147": nothing about this star.
- **MAST products:** QLP, TARS, TESS-SPOC (s25, s26, s52, s53, s79, s80) and TASOC (s26).

Files: verify.py/.txt, verify_spoc.txt, physics2.py/.txt (new). Checker #1's ecl*, ephem*, ecc*, secondpipe*, diff*, neighbours*, ebfit*, physics*, predict* are all re-verified.
