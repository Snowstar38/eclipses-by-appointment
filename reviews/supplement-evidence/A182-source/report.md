# TIC 200222789 (UCAC4 667-109998; Gaia DR3 1981914793343154944) -- adversarial check

Checkers: Opus 5.5 (steps 1-3 and the difference images, 2026-10-20; killed by a usage limit) and a second Opus 5.5 session that resumed on 2026-10-21. The second session re-checked steps 1-3 and did steps 4-6.
Gaia SB1: P 43.90099 +- 0.00732 d, e 0.3505 +- 0.0085, w 332.23 +- 1.52 deg, K1 38.54 km/s. TIC: Tmag 10.86, Teff 5071, R 5.39 (giant), d 816 pc.

## Verdict: CONFIRMED
This is a long-period eclipsing binary made of a K giant and a hotter, smaller companion. The deeper eclipse (B) is a total occultation of the companion behind the giant. The shallower eclipse (A) is the companion transiting the giant.

## 1. Archives (what was queried, what came back)
- cats.py --r 60 (run twice: 10-20 and again 10-21): VSX none; ASAS-SN none; Prsa+2022, IJspeert+2024 and Kostov+2025 t2/t3/t4 none within 5"; SIMBAD has UCAC4 667-109998 as [SB*], with one reference (the Gaia DR3 multiplicity paper).
- Gaia DR3 vari_summary 0 rows, vari_eclipsing_binary 0 rows, phot_variable_flag NOT_AVAILABLE. SB9 0; WDS 0; ExoFOP has no TOI or CTOI.
- VizieR within 30": ZTF Chen+2020 0; GCVS 0; WISE Chen+2018 0; ASAS-SN II/366 0; Gaia veb 0; APOGEE, GALAH, LAMOST and RAVE 0. ATLAS Heinze+2018 lists J337.8834+43.3708 with class "dubious" and long-fit period 79.9 d. That is not an eclipsing-binary classification and so not prior art.
- Web search on the UCAC4, TIC and Gaia DR3 ids: no page mentions the star.
- MAST CAOM (10"): QLP s16, s56, s83, s84 only. There are no SPOC, TESS-SPOC, TGLC, ELEANOR or other HLSP products.
- Gaia DR3 astrometry: RUWE 1.18, ipd_frac_multi_peak 0, rv_amplitude_robust 75.8 km/s, GSP-Phot Teff 5696 and logg 3.31. That Teff is a blend, pulled up by the hot companion.
- No prior art. The eclipses are new.

## 2. Eclipses (raw QLP SAP_FLUX, QUALITY==0, no trimming; flagged cadences inspected separately)
- B s16: 1741.61314 +- 0.4 min, depth 14.55%. Clean, flat bottom.
- B s56: 2839.09539 +- 0.5 min (fit error; the real error is larger), depth 14.29%. Ingress falls in the orbit gap, so the time rests on the egress plus late ingress. A flux-level step across the gap is handled by per-segment baselines.
- B s83: no eclipse; the sector ends 0.2 d before ingress.
- B s84: 3585.39085 +- 1.6 min, depth 13.52%. The bottom sits on a scattered-light swell up to about 1.7x the star's flux, giving a tilted floor.
- A s16: 1755.14825 +- 2.2 min, depth 6.22%. U-shaped.
- A s56: 2852.618, depth about 6.1%. Egress cut off by the sector end; one-sided, not used.
- A s84: 3598.9072 +- 7 min, depth 7.0%. The background swell peaks near mid-eclipse.
- Trapezoid fits: B has T14 24.2 h, ingress 4.7 h and a flat bottom of 14.9 h. A has T14 31.3 h and an ingress of 9.2 h (rounded, limb-darkened).
- Re-timing with my own code (mirror symmetry, block bootstrap): B s16 1741.61350 +- 8.5 min, B s84 3585.39700 +- 2.9 min, A s16 1755.14775 +- 8.2 min, A s84 3598.90350 +- 7.5 min. All agree with the list above to within 9 min.
- Blind dip census of all four sectors (1-h bins): nothing deeper than 0.5% outside the eclipses. The only dips deeper than 0.3% are background-swell residuals in s84.
- Centroids: s16 shows shifts of +18/+10 mpx during B. The difference image (step 4) resolves this as on-target.

## 3. Ephemeris
- Joint linear fit (common P; errors scaled x4.6, driven by s84): P = 43.89933 +- 0.00007 d; T0_B = BTJD 1741.61295 +- 1.8 min; T0_A = BTJD 1755.14708 +- 9.6 min. O-C: B +0.3, -1.3, +8.5 min; A +1.7, -17.1 min.
- Against Gaia: P differs by -0.0017 d, which is -0.23 sigma. The observed B time is 0.16 d earlier than Gaia's predicted conjunction (-0.5 sigma), and A is 0.06-0.12 d later (+0.2 to +0.7 sigma).
- The A-B separation is 13.534 d (phase 0.3083), against Gaia's prediction of 13.31 +- 0.23 d (+0.95 sigma).
- e cos w = +0.302 from the separation (Gaia +0.310). From the physical model (step 5): e 0.335, w 334.7, e sin w -0.143. Gaia has e 0.3505 and e sin w -0.163, so e is -1.8 sigma and w +1.6 sigma from Gaia.
- Possible small signal: in s84, B is 8 min late and A 17 min early, so A-B shrank by about 26 min over 42 cycles. Both s84 events sit on a large scattered-light swell, so I do not claim apsidal motion. Future eclipses would test it.

## 4. Independence
- No second pipeline exists for this star, so I did my own aperture photometry on TESScut 15x15 cutouts (1x1, 3x3 and 5x5 apertures).
  - B: s16 1741.6137 (13.4%), s56 2839.0952 (13.5%), s84 3585.381 (13.4%).
  - A: s16 1755.1490 (6.1%), s84 3598.9033 (5.6%).
  - These times are within 1 min of QLP in s16 and s56, and within 6-14 min in s84 (the swell). The depth is the same in 1x1, 3x3 and 5x5 apertures to within about 1% absolute, so the signal is not diluted by anything off-target.
- Difference images (s16 A, s16 B, s56 B, s84 B):
  - In s16 B, the centroid of the flux deficit lies 0.04 px (0.8") from the target.
  - 84% of the deficit falls in the 3x3 box on the target, compared with 52-55% of the light.
  - The two bright stars in the cutout, both more than 60" away, lose no flux.
- Neighbour dilution: within 60" the brightest Gaia neighbour is G 15.39 (42.8"). To fake A it would need a 238% dip, and B would need 532%; the others need 347-1600%. All impossible.

## 5. Physics (deeper-B question)
- Mass function f(m) = 0.214 Msun; a1 sin i = 31.3 Rsun. For M1 = 1.5 / 2.0 / 2.5 Msun: m2(i = 88 deg) = 1.14 / 1.34 / 1.51 Msun and a = 72 / 78 / 83 Rsun.
- Which star is in front: the SB1 w is the giant's, in the RV convention. So at B (nu = 270 - w = 297.8 deg) the giant is in front, and at A (nu = 117.8 deg) the companion is in front. The shapes match this: B is flat-bottomed (a total occultation of the small star), and A is rounded (a transit across a limb-darkened giant).
- One geometry fits both s16 eclipses. I fitted a two-sphere eccentric model with the giant's quadratic limb darkening fixed at 0.45/0.20:
  - k = R2/R1 = 0.2545; companion light share in TESS L2 = 0.146; R1/a = 0.0764; i = 87.95 deg.
  - Impact parameter b_B = 0.36, which is below 1 - k = 0.75, so the occultation is total, as observed. b_A = 0.48.
  - Residual rms is 0.66 ppt for B, which is white. For A it is 1.07 ppt, with +-3 ppt structure across the bottom: spot crossings or a limb-darkening mismatch, not a geometry problem.
  - The duration ratio comes out right without being forced. B happens near periastron (sky speed x1.24) and A near apastron (x0.89), and the larger A impact parameter partly offsets the difference.
- Why B is deeper: B depth equals L2 (14.6%). A depth is about k^2 (1 - L2) times limb darkening, about 6%. So per unit area the companion is 2.64x brighter than the giant in the TESS band. As blackbodies, that means T2 is about 6950 K for T1 = 5071 K: an early-F or late-A dwarf.
- Sizes and masses: R2 = 1.41 / 1.52 / 1.62 Rsun and R1 = 5.5 / 6.0 / 6.4 Rsun for M1 = 1.5 / 2.0 / 2.5. A main-sequence star near 7000 K with R about 1.6 Rsun should have about 1.5 Msun, which needs M1 about 2.5 Msun. That gives logg1 = 3.23, against Gaia's 3.31, and R1 6.4 against TIC's 5.4. TIC assumed a single star; with 15% of the light from the companion and a blended Teff, its radius would come out low, so this is consistent.
- Depths, durations, shapes, the timing of both eclipse kinds, and the companion's light all fit one geometry.

## 6. Next predicted eclipses (BTJD; linear ephemeris; formal errors in brackets; allow +-30 min given the s84 O-C)
- A (transit, ~6%, 31 h): 4345.208 (11 min), 4389.107, 4433.006, 4476.906, 4520.805, 4564.704
- B (total occultation, ~14.5%, 24 h, flat 15 h): 4375.573 (5 min), 4419.472, 4463.372, 4507.271, 4551.170, 4595.070

## What would settle it further
- Spectroscopy: a few spectra near quadrature should show a second set of lines from a ~7000 K star, with K2 of about 30-38 km/s. That would give an SB2 and dynamical masses. The prediction is M1 about 2.5 and M2 about 1.5 Msun.
- More eclipse timings (TESS, or ground-based for the 14.5% B eclipse at V about 11.5) to test the apparent shrinking of the A-B separation, which could be apsidal motion.
- A multi-band B eclipse would directly give the companion's colour and temperature.

Files: progress.md, verify.py/txt, zoom.py/zoom_B.png, photcut*.npz/png, cutfit.py/txt, diff_*.png/json, neighbours.txt, physics.py/txt, ebfit.py, ebfit_s16.json and ebfit_s16_fit.json/png, ephem_final.py/json/_out.json/txt.