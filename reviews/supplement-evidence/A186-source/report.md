# TIC 252806416 (TYC 3444-504-1, Gaia DR3 783315899231853056): adversarial check

**Verdict: CONFIRMED.** This is an eclipsing SB1. A K giant (Teff 4920 K, logg 3.4, R about 3.4-3.8 Rsun) is transited and occulted by a companion of about 0.55-0.6 Msun, on a 42.4423 d orbit with e about 0.35. Both eclipse kinds are on the target, both have the same period, and the timing matches the Gaia orbit and the 2015-2018 APOGEE RVs once Gaia's period is corrected. The "A lag" was a Gaia period error.

Checker: Opus 5.5 subagent, 2026-10-21. It resumed and verified the 2026-10-20 checker's step 1. All numbers come from scripts in this folder.

## 1. Archives
- `cats.py --r 60`: no entry in VSX, ASAS-SN, Prsa+2022, IJspeert+2024 or Kostov+2025 t2/t3/t4. SIMBAD lists it as SB* only.
- Gaia DR3 (rerun on 2026-10-21; it reproduces 10-20): vari_summary 0 rows, vari_eclipsing_binary 0 rows. NSS SB1 gives P 42.4205 +- 0.0125 d, e 0.374 +- 0.011, w 69.3 +- 2.9 deg, K1 25.81 +- 0.40 km/s, gamma -8.93.
- VizieR SB9, WDS and VSX (60") return nothing. ExoFOP has no TOI or CTOI. A web search on the TYC and TIC names finds nothing.
- The binarity was already known from APOGEE: Price-Whelan+2018 (J/AJ/156/18) lists it as a high-K binary, and SoS sets flagBinary. **The eclipses appear unreported.**
- MAST holds QLP s21/s48/s75 and TESS-SPOC s75.

## 2. Eclipses (raw QLP SAP_FLUX, untrimmed)
| event | mid-time BTJD | depth | T14 | T12 | flat |
|---|---|---|---|---|---|
| B s21 | 1894.16853 +- 3.8 min | 0.76% | 27.65 h | 3.69 h | 20.3 h |
| B s48 | 2615.68798 +- 3.3 min | 0.75% | 27.70 h | 3.69 h | 20.3 h |
| A s48 | 2633.95598 +- 1.5 min | 2.87% | 13.99 h | 2.78 h | (U-shaped) |
| A s75 | 3355.47474 +- 1.7 min | 2.97% | 13.9 h | 2.6 h | (U-shaped) |

- The s75 A egress runs into cadences flagged for scattered light (bit 2^30). A fixed-shape fit gives t0 3355.4735-3355.4756 depending on how many flagged cadences are included, about 3 min of spread.
- A in s21 (predicted 1869.995) ends before the sector starts at 1870.45, and the flat start of s21 is consistent with that.
- Background and centroids are smooth through every event.
- Blind census (q==0, 1-h bins, scatter 0.35-0.39 ppt): no other dip deeper than 0.15% in any sector.
- Common mode: the target is the deepest of 280-309 stars at each s21/s48 event. On its s75 CCD it shows 3.02% while 12 other stars show -0.10% to +0.02%.

## 3. Ephemeris
- A alone gives P 42.44228(9) and B alone gives 42.44232(21), so the two kinds agree.
- Joint fit: **P = 42.44229 +- 0.00008 d, T0_A = 2633.95593 +- 0.00099, T0_B = 2658.13002 +- 0.00188 BTJD**, chi2 0.03/1, all O-C under 0.5 min.
- P_TESS - P_Gaia = +0.0218 d (+1.74 sigma).
- Measured minus Gaia-predicted conjunction, unconditional: A +1.46 and +1.83 d (+1.75 sigma each); B +0.23 and +0.60 d. Conditioned on P = P_TESS: **A +0.02 d (+0.2 sigma), B -0.27 d (-0.9 sigma).** So the lag the classifier saw is entirely Gaia's period error.
- B-A phase is 0.56958(5), against Gaia's 0.5897 +- 0.0116 (-1.7 sigma).
- Duration ratio T_B/T_A is 1.99 +- 0.05, against 2.07 +- 0.06 for b=0 from Gaia (-1.1 sigma).
- Eclipse-derived e 0.344, w 72.5 deg: e cos w +0.103 (Gaia +0.133, -1.6 sigma). The b=0 e sin w of +0.328 is a lower limit, against Gaia's +0.350.

## 4. Independence
- **TESS-SPOC s75 SAP** (all cadences up to tc+0.45 d, because SPOC flags the egress): t0 3355.47575 (+1.4 min from QLP), depth 2.78%, T14 13.71 h. PDCSAP is NaN across the egress.
- **TESScut difference images** (s21 B, s48 A and B, s75 A): the deficit peaks on the target pixel every time. For s48 A the deficit centroid sits 0.4" from the light centroid, and the 1x1/3x3/5x5 depths are 2.9/2.8/2.8%. The G 15.02 star at 83" shows no deficit.
- **Neighbours.** The only Gaia source within 60" brighter than G 17 is a **G 14.89 star 3.7" away**, inside the same pixel. It would need a 73% A dip and a 19% B dip. Its parallax is 1.252 +- 0.030 mas against the target's 1.898 +- 0.025 and its proper motion differs, so it is unrelated.
  - Centroid regression on the QLP SAP_X/Y: if the neighbour produced A, the centroid would move -4.9 mpx (s48) and -5.1 mpx (s75) in x. Measured: -0.06 +- 0.16 and +1.39 +- 0.44 mpx. **Ruled out at chi2 894 and 230.**
  - For B, s48 favours the target (chi2 0.1 against 11.0). s21, at 30-min cadence with a trend, is ambiguous.
- **APOGEE DR17 visit RVs** (2015 and 2018, 61 orbits before s48), modelled on the eclipse ephemeris with Gaia's K and the eclipse e, w: rms 0.34 km/s, gamma -8.89, best shift of T_A +0.02 d. Using Gaia's P instead gives rms 5.9 km/s. This confirms the period and that A is the conjunction with the companion in front.

## 5. Physics
- f(M) = 0.0603 Msun, a1 sin i = 20.07 Rsun.
- With M1 about 1.2-1.4 (from logg 3.41 and R): m2(i=90) is 0.58-0.63 Msun and a is 62-65 Rsun.
- At A (r = 0.637a) the giant is behind and the companion transits it, which explains the limb-darkened U shape. At B (r = 1.323a) the giant is in front and the companion is totally occulted, which explains the flat bottom.
- One geometry fits T14_A, T14_B and T23_B (chi2 about 0.7): R1/a 0.052-0.058 (R1 3.3-3.7 Rsun), k = R2/R1 0.11-0.17 (R2 about 0.5 Rsun), i 89-90 deg, b_A <= 0.2.
- Depth A of 2.9% is about k^2 times limb darkening. `geom2.py` fits depth and durations together, with quadratic limb darkening (u1 0.5, u2 0.2) and Gaia's e sin w as a prior: chi2 0.66, k 0.152, b_A 0.12, b_B 0.24, e sin w 0.345 (Gaia 0.350).
- Depth B of 0.75% equals L2/(L1+L2). At k = 0.15 this needs a TESS-band surface-brightness ratio of 0.34, i.e. T2 about 3850 K, which fits a main-sequence companion of about 0.55-0.6 Msun.
- Everything is consistent with one system.

## 6. Next eclipses (BTJD; formal 1-sigma, plus about 3 min systematic from the s75 egress)
- A (2.9%, 13.9 h): **4374.0897 +- 4.3 min**, 4416.5320 +- 4.4, 4458.9743 +- 4.5, 4501.4166 +- 4.6.
- B (0.75%, 27.7 h, flat): **4355.8215 +- 6.4 min**, 4398.2638 +- 6.5, 4440.7061 +- 6.6, 4483.1484 +- 6.7.

## What would settle it further
- A third epoch of either kind, to test linearity. There are only two of each now, so the joint fit has 1 dof.
- High-resolution spectroscopy or a combined RV + light-curve solution would give the masses and radii (an SB2 detection of the M dwarf is unlikely at a 0.8% flux ratio).
- Speckle or AO imaging is not needed for the 3.7" star, because the centroid test excludes it.
