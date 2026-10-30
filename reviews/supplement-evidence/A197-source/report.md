# TIC 300202855 (TYC 7612-1193-1, Gaia DR3 2884556351606337920): adversarial check

**Verdict: CONFIRMED.** It is an eccentric detached eclipsing binary on target, with P = 25.762668 d. The F-type Gaia RV primary is eclipsed at conjunction A, giving a 6.9% primary with a flat bottom, 5.9 h long. The secondary is a 0.75% flat-bottomed occultation of an early-M companion (about 0.57 Msun) at phase 0.2792.

**On the period.** The period difference from Gaia is not real tension: P_TESS - P_Gaia = +0.0155 d is 0.79 sigma of Gaia's 0.0197 d error.

**On the CTOI.** ExoFOP CTOI TIC 300202855.01 (TSTPC single transit, PC, 2024-08-28; epoch BTJD 2193.078 +- 0.12, 7.85 ppt, 5.3 h) is this binary's secondary eclipse in s32 (ours: 2193.0730). It is not a planet. The CTOI should be re-dispositioned as an EB, P 25.7627 d.

## Deciding numbers
- **Period.** Two consecutive s98 primaries give P = 25.76247 directly. With s33 that fixes the cycle count (N = 71). The neighbouring counts would need 26.131 d or 25.405 d, which is impossible.
- **Ephemeris fit.** Four primaries fit a linear ephemeris with rms 0.10 min. Five secondaries (s7 to s98, 2019 to 2025) give P_S - P_P = -0.010 +- 0.049 min/cycle.
- **Gaia timing.** Conjunction A, predicted at the deep eclipse: obs - pred = -0.24 +- 0.52 d (TESS P) or +0.86 +- 1.49 d (Gaia P). Conjunction B: +0.04 +- 0.57 d or +1.14 +- 1.51 d. The swapped assignment is 13-23 sigma off.
- **Geometry against Gaia.** The constrained model at Gaia-like e sin w gives e 0.359 and w 170.4. Gaia SB1 has e 0.378 +- 0.032 and w 171.2 +- 4.7: agreement within 0.6 sigma. e cos w from the eclipse phase is -0.354 (Gaia -0.373).
- **On target.** In the TESScut s87 difference image the deficit centroid is 0.4" from the light centroid for the primary and 2.2" for the secondary (pixel 21"). Deficit share in the 3x3 is 0.76/0.83, against a light share of 0.75/0.74.
- **Neighbours.** The only Gaia neighbours within 60" brighter than G 18.5:
  - G 16.07 at 34.4" (x68): primary would need 470%, impossible; secondary 51%.
  - G 17.15 at 21.2" (x181): impossible for both.
- **Independent pipeline.** SPOC 2-min (s87, s98) and TESS-SPOC (s32, s33) SAP:
  - Primaries at QLP times within -0.5..-0.1 min, depth 6.39-6.47% in every sector. The QLP s98 depth of 5.3% is QLP dilution.
  - Secondaries within -1.7..+2.0 min, depth 0.67-0.78%.
  - SPOC recovers a secondary flagged in QLP: s98 E70 at 4022.2272 +- 3.0 min, O-C +1.9 min.

## Archives (step 1, previous checker; ExoFOP rechecked)
- VSX, ASAS-SN, SB9, WDS and the EB catalogues (Prsa, IJspeert, Kostov) have nothing.
- SIMBAD lists TYC 7612-1193-1 as SB* only. Gaia vari tables have no rows.
- Web search: nothing.
- **ExoFOP has the CTOI above**, the only prior flag. It was raised as a single transit and has no period.
- **Gaia:** G 11.50, BP-RP 0.69, plx 2.295 mas, Teff 6160 K (gspphot; TIC 6433 K, R 1.65 Rsun, M 1.3 Msun), RUWE 0.98.
- **Gaia NSS SB1:** P 25.7471 +- 0.0197, e 0.378 +- 0.032, w 171.2 +- 4.7, K1 28.91 km/s.

## Eclipses (step 2; raw QLP SAP, quality==0, untrimmed trapezoid with quadratic baseline)
- **Primary.** Measured at s33 2211.64639, s87 3680.11844, s98 4015.03324 and 4040.79571 (each +- 0.3 min).
  - T14 5.91-5.93 h, T12 2.24-2.31 h, flat 1.31-1.44 h.
  - Depth 6.9% (5.3-5.4% in QLP s98).
- **Secondary.** Measured at s7 1497.486 (+- 4.6 min), s32 2193.0730 (3.3), s33 2218.8423 (3.1), s87 3687.3127 (2.6) and s98 3996.4625 (2.2).
  - Depth 0.64-0.79% (0.30% in 30-min s7).
  - T14 5.6-6.1 h, flat 0.6-2.3 h.
- **Flagged-only windows** also dip on time: s32 P 2185.88 (~6%, scattered light), s98 P 3989.27 (~4.5%), s98 S 4022.21, s6 S 1471.72 and s7 P 1516.06 (ingress).
- **Background and centroids.** No background rise that could make the dips; centroids move under 1 mpx except in the noisy s87.
- **Census.** Nothing else, apart from the s7 sector-start ramp (1492.45-1492.87, 0.5%, not at any conjunction) and the s98 4003.0 gap edge (also present in TIC 307361219: common mode).

## Ephemerides (step 3)
- **Primary (A, F star eclipsed):** BTJD 2211.64639 +- 0.00020 + E x 25.762668 +- 0.0000034 d.
- **Secondary (B):** BTJD 2218.83963 +- 0.00172 + E x 25.762661 +- 0.000034 d.
- **Secondary phase:** 0.27921 +- 0.00007. Gaia predicts 0.2677.
- **e sin w.** The duration ratio is T_A/T_B = 1.00. e sin w is not separable from the radius ratio in the light curve alone: e sin w 0 and +0.06 give the same chi2. Gaia's e sin w (+0.058) selects the physical branch.

## Physics (step 5)
- **Mass function.** f(M) = 0.0525 Msun. M1 1.2-1.4 gives m2 = 0.54-0.59 Msun and a = 44-46 Rsun.
- **Model at e sin w +0.06.** R1/a 0.0374, R2/a 0.0110, giving R1 = 1.69 Rsun (TIC 1.65) and R2 = 0.50 Rsun. i 87.75 deg, L2/L1 (TESS) 0.014.
- **Companion light.** The expected L2/L1 for a 0.57 Msun M0V against a 6200-6400 K F star is about 0.015-0.02. The flat-bottomed secondary is a total occultation whose depth equals the companion's light share.
- **The other branch is excluded.** At e sin w 0 the model needs a 1.3 Rsun companion with L2/L1 0.10, which an SB1 with m2 about 0.57 cannot be.
- Everything (depths, durations, shapes, the companion's light, the Gaia orbit) fits one geometry.

## Next predicted eclipses (BTJD)
| Kind | Epoch | BTJD | Error | UTC |
|---|---|---|---|---|
| Primary | E83 | 4349.9478 | 0.5 min | 2026-11-05 10:44 |
| Primary | E84 | 4375.7105 | 0.5 min | |
| Primary | E85 | 4401.4732 | 0.5 min | |
| Primary | E86 | 4427.2358 | 0.5 min | |
| Secondary | E83 | 4357.1405 | 4.8 min | 2026-11-12 15:22 |
| Secondary | E84 | 4382.9032 | 4.8 min | |
| Secondary | E85 | 4408.6658 | 4.8 min | |
| Secondary | E86 | 4434.4285 | 4.9 min | |

## What would settle it further
- An RV spectrum to detect the M companion (K2 ~ 65 km/s): that gives masses directly.
- Reporting to ExoFOP that CTOI 300202855.01 is the secondary eclipse of a 25.763-d EB.
- A light-curve fit with a mass-radius prior to pin k and i.
