# TIC 170312515 (UCAC4 240-011387, Gaia DR3 5563236508191080576): adversarial check

**Verdict: CONFIRMED.** This is an eclipsing SB1 on a 52.3110 d orbit with e about 0.33-0.37. A G/K giant (R about 4.5 Rsun) is transited and occulted by a companion of about 0.6-0.7 Msun. There are four primaries and two flat-bottomed (total) secondaries, all on one ephemeris, which matches Gaia's period (-0.4 sigma) and Gaia's conjunction phase (+0.3 sigma). The signal sits on the target pixel and is reproduced by three other pipelines.

Checker: Opus 5.5 subagent, 2026-10-21. It resumed and verified the 2026-10-20 checker's step 1.

## 1. Archives
- `cats.py --r 60`: no entry in VSX, ASAS-SN, Prsa+2022, IJspeert+2024 or Kostov+2025. SIMBAD lists it as SB* only.
- Gaia DR3 (rerun on 2026-10-21): vari_summary 0, vari_eclipsing_binary 0. NSS SB1 gives P 52.3189 +- 0.0188 d, e 0.372 +- 0.012, w 91.4 +- 2.2 deg, K1 24.46 +- 0.37 km/s, gamma 15.03.
- SB9 and WDS return nothing. The nearest VSX entry is 101" away (ROT, G 15.3). ExoFOP has no TOI or CTOI.
- The VizieR all-catalogue 5" cone finds no variability, EB or orbit catalogue other than Gaia. Web searches on the UCAC4, TIC and 2MASS names find nothing.
- **The eclipses appear unreported.**

## 2. Eclipses (raw QLP SAP_FLUX, q==0, untrimmed; fixed-shape refits agree within 1.5 min)
| event | mid-time BTJD | depth | T14 | T12 | flat |
|---|---|---|---|---|---|
| A s7 | 1499.98113 +- 2.8 min | 1.79% | 19.28 h | 3.13 h | U-shaped |
| B s33 | 2205.97845 +- 3.2 min | 0.90% | 35.10 h | 4.77 h | 25.6 h |
| A s34 | 2232.33376 +- 2.4 min | 1.87% | 19.30 h | 3.23 h | U |
| A s61 | 2964.68859 +- 2.8 min | 1.84% | 19.13 h | 2.93 h | U (pre-ingress flagged for scattered light) |
| B s87 | 3670.68483 +- 3.0 min | 0.89% | 34.90 h | 4.47 h | 26.0 h |
| A s88 | 3697.04224 +- 2.0 min | 1.83% | 19.09 h | 2.99 h | U (data gap and pointing jump in the ingress) |

- Every conjunction that falls in the six sectors shows its eclipse, and no other conjunction is covered.
- Background is flat through every event. In s61 and s88 the centroids jump only at the data gaps.
- Blind census (q==0, 1-h bins, scatter 0.33-0.40 ppt): no other dip deeper than 0.15%, apart from a single 0.15% bin in s7.
- Common mode: same-CCD stars have a median dip of about 0 at every event. The few other stars dipping at those times are variables 2-50 deg away (e.g. TIC 174797643, an unrelated 24% EB, at s88).

## 3. Ephemeris
- A alone (4 events) gives P 52.31099(5), chi2 0.27/2. B alone (2 events) gives 52.31094(11).
- Joint fit: **P = 52.31098 +- 0.00005 d, T0_A = 2232.33454 +- 0.00097, T0_B = 2258.28885 +- 0.00165 BTJD**, chi2 0.44/3, all O-C under 1.2 min.
- P_TESS - P_Gaia = -0.0079 d (-0.42 sigma).
- Measured minus Gaia conjunction: A -0.21 to -0.55 d (-0.5 to -0.6 sigma), B -0.19 and -0.41 d (-0.3 sigma). Conditioned on P = P_TESS: A -0.07 d (-0.55 sigma), B +0.08 d (+0.18 sigma).
- B-A phase is 0.49615(3), against Gaia's 0.4935 +- 0.0100 (+0.27 sigma). That gives e cos w = -0.0058, against Gaia's -0.0094.
- Duration ratio T_B/T_A = 1.82, against 2.18 for b=0 from Gaia. The difference comes from the impact parameter: b_B = 2.2 b_A, so B is shortened more (see section 5).

## 4. Independence
- **TESS-SPOC s61 SAP**: A at 2964.68981 (+1.8 min from QLP), 1.72%, T14 19.11 h. PDCSAP gives +6.1 min and 1.69%.
- **GSFC-ELEANOR-LITE s7 RAW**: A at 1499.98008 (-1.5 min), 1.81%, 19.27 h.
- **TGLC s7**: aperture flux +0.0 min, 1.99%. The PSF flux, which fits the target's own Gaia PSF, gives +1.9 min, 1.64%, 19.27 h. TGLC's cal_* fluxes are detrended and flatten the eclipse, so they were not used.
- **TESScut difference images** (s34 A, s61 A, s33 B, s87 B): the deficit peaks on the target pixel every time. The 3x3/5x5 depths are 1.8-1.9% (A) and 0.8-0.9% (B). The deficit is more concentrated on the target (74-82% inside the 3x3) than the light is (61-67%).
- **Neighbours**: nothing within 60" is brighter than G 18.35, and each such source would need a dip over 1000%. Further out:
  - G 14.99 at 62" would need a 49% A dip; its pixel shows only +0.1 to +0.9% (the wing of the target's PSF).
  - G 12.59 at 77" would need a 5.4% A dip; its pixel shows -0.5 to +0.3%.
  - Both are excluded.

## 5. Physics
- f(M) = 0.0634 Msun, a1 sin i = 23.46 Rsun.
- For M1 1.2-1.6: m2(i=90) is 0.59-0.69 Msun and a is 71-78 Rsun.
- At A (r = 0.628a) the giant is behind and the companion transits it (U-shaped, limb-darkened). At B (r = 1.372a) the companion is totally occulted (flat bottom).
- One geometry fits all three durations and the A depth (quadratic limb darkening), chi2 0.13: R1/a 0.061, so R1 is 4.3-4.7 Rsun (TIC gives 4.45); k 0.122, so R2 is about 0.55 Rsun; b_A 0.22, b_B 0.44, i about 88.5-89 deg; e sin w 0.32 [0.295, 0.34].
- With Gaia's e sin w (0.372 +- 0.012) as a prior, chi2 rises to 7.0, which is about 2-2.5 sigma of tension. That is small enough to be the simplified trapezoid and limb-darkening model; it is not a contradiction.
- B depth 0.90% = L2/(L1+L2). This needs a surface-brightness ratio of 0.61, i.e. T2 about 4400 K, which fits a dwarf of about 0.7 Msun (m2 for M1 about 1.6).
- There are no APOGEE or LAMOST RVs, so no independent RV phase test was possible.

## 6. Next eclipses (BTJD, 1-sigma)
- A (1.8%, 19.2 h): **4377.0848 +- 2.4 min**, 4429.3958 +- 2.4, 4481.7067 +- 2.5, 4534.0177 +- 2.6.
- B (0.9%, 35 h, flat): **4350.7281 +- 2.8 min**, 4403.0391 +- 2.9, 4455.3501 +- 2.9, 4507.6611 +- 3.0.

## What would settle it further
- A light-curve model with proper limb darkening, or a few epochs of ground or space RVs, to pin down e sin w (eclipse durations give 0.32, Gaia gives 0.372) and to get absolute masses and radii.
- A spectroscopic logg/R for the giant would fix M1.
- Nothing more is needed to establish that the target is the eclipser.
