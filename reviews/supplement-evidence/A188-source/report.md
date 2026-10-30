TIC 176778312 (UCAC4 275-003209, Gaia DR3 5048026421933437696): adversarial check
Checker: Opus 5.5, 2026-10-20/21. This run resumed after a usage-limit kill; every earlier receipt was re-run before use.

VERDICT: CONFIRMED.
This is a new eccentric (e ~ 0.55), detached eclipsing binary at the Gaia SB1 period, and both conjunctions eclipse.
  A: a ~0.55 Msun companion transits the F star. The bottom is curved and the depth is 9.3%.
  B: the companion is totally occulted. The bottom is flat and the depth is 1.2%.
The difference images put both kinds of eclipse on the target. I found no prior record of it as an eclipsing binary.

DECIDING NUMBERS

Measurements
- 12 eclipses measured from raw SAP_FLUX with a trapezoid x quadratic-baseline model and prayer-bead errors. Every fit re-ran to better than 0.1 min.
    A x5: s4 1413.11 (missed by the classifier), s4 1435.47, s31 2150.97, s97 3939.72, s97 3984.44.
    B x7: s4 1431.62, s30 2124.79, s31 2147.15, s31 2169.52, s97 3935.88, s97 3958.24, s97 3980.61 (flagged cadences).
- A shape: depth 9.32-9.70% (s4/s31). T14 7.63+-0.04 h, ingress 1.85 h, curved bottom.
    QLP s97 reads 7.1%, but the TESScut pixels give 9.5%. That is a QLP flux-scale artefact, and it scales both kinds by the same factor.
- B shape: depth 1.20-1.25% (pixels at s97 give 1.1%). T14 8.07+-0.08 h, ingress 1.6-1.85 h, flat bottom 4.5-4.8 h.

Ephemeris
- A-only fit: P = 22.359367 +- 0.000006 d, T0 = BTJD 2575.79943 +- 0.00033. O-C at most 1.6 min (chi2 20.7/3).
- Joint fit (common P, errors scaled x10 because of the B anomaly below):
    P = 22.359363 +- 0.000023, T0_A = 2575.79945 +- 0.00127, T0_B = 2594.32784 +- 0.00456.
- Against Gaia's period: Gaia P 22.35707 +- 0.00356, so the difference is +0.0023 d = +0.64 sigma.
- Against Gaia's conjunction predictions:
    Observed A lands +0.29 to +0.57 d after the predicted A conjunction (+1.0 to +1.4 sigma).
    Observed B lands -0.20 to +0.09 d from the predicted B (within 0.9 sigma).
    So the A/B labelling agrees with Gaia's omega.

Orbit shape
- Separation: B precedes A by 3.831 d. Gaia's e and omega predict 3.35 +- 0.16 d, a -2.9 sigma tension.
    Holding omega = 3 deg, the eclipses need e = 0.545 (e cos w 0.544), against Gaia's e 0.585 +- 0.014 (-2.8 sigma).
    This is a modest tension with the SB1 solution, not a contradiction.
- Duration ratio: T14_B/T14_A = 1.063 +- 0.010, which gives e sin w = +0.030 +- 0.005.
    Gaia gives +0.013 +- 0.020 (omega 1.3 +- 2.0 deg), so the two are consistent.
- Which star is in front: take z_primary = r sin(nu+w) sin i, with RV = dz/dt.
    At nu+w = 90 deg (A) the primary is behind, so the companion transits.
    That matches what is seen: A is the limb-darkened U and B is the flat total occultation.

Physics
- f(M) = 0.0558 Msun. m2(i=90) = 0.50 / 0.545 / 0.58 Msun for M1 = 1.0 / 1.16 / 1.3. a = 38-41 Rsun.
- Durations: the predicted central T14 is 8.5-9.1 h; the observed 7.6-8.1 h gives b ~ 0.4.
- Radius ratio: the ingress/duration ratio of the total occultation gives k ~ 0.26-0.28, so R2 ~ 0.53 Rsun. That suits a 0.55 Msun dwarf.
- Brightness: the surface-brightness ratio is about 0.15, so Teff2 is about 3900 K.
    That predicts L2/(L1+L2) = 0.013, against the observed 0.012.
- One geometry accounts for all the depths, durations and shapes.

Independence
- I refit SPOC SAP and PDCSAP (s4/s30/s31), eleanor, TASOC and TGLC (s4).
    Every clean eclipse reproduces within 0-2.2 min in t0.
    Depths are 9.0-10.2% (A) and 1.15-1.4% (B). TASOC is shallower (7.0/0.9%) because its aperture is diluted.
- Difference images: SPOC TPF s4 (A x2), s31 (A), s30 (B), s31 (B), plus TESScut s97 (A, B).
    The deficit peaks on the target pixel, and its centroid is within 0.1-0.3 px of the target.
    The target pixel has the deepest fractional dip: A 9.4-9.6%, B 1.1-1.4%.
- Neighbours within 60": the only one bright enough is G 13.19 at 58.4".
    It would need a 45% dip for A and 6% for B, and the difference images exclude it.

Census
- With predicted eclipses masked, s4/s30/s31 have no other dip deeper than 0.15% (1-h scatter 0.3-0.4 ppt).
- The one s97 census flag, at 3952.5, is not present in the raw cadences.
- Every predicted eclipse with q==0 coverage was seen.
- Three fall only on flagged cadences: A s30 2128.61, A s97 3962.08 and B s97 3980.61. I fit the last one anyway and it agrees.

ANOMALY WORTH FOLLOWING: THE B TIMES WANDER AGAINST A
A is linear to within 1.6 min, but B is not. The interval from each B to the next A:
  s4      3.8507 d
  s30/31  3.8180, 3.8168, 3.8155 d
  s97     3.8394, 3.8406 d (3.8308 on flagged data)
That is a 47-min drop over two years, then a 35-min rise. Each B time has a 1.4-1.7 min error, and a linear fit to B gives chi2 849/5.
The wander is in the data, not the method:
- SPOC, eleanor and TGLC reproduce the B times to within 2 min.
- It is independent of fit window, baseline order and a fixed eclipse shape (variants B1-B3).
Possible causes:
- Apsidal motion: ruled out. It is monotonic, and at omega ~ 0 it barely moves the separation (6 min/deg).
- Light-travel time from a third body: ruled out. It would shift A and B together.
- Still open:
    A tertiary perturbing e dynamically. The separation changes by -12 d per unit e, so this needs delta-e ~ +-0.0015.
    Spot-distorted occultation profiles of the M-dwarf companion. This would need a large asymmetry.
This does not affect the verdict, but B predictions should carry about +-40 min of systematic error.

PRIOR ART (queried 2026-10-20, re-run 2026-10-21)
- cats.py --r 60: nothing in VSX, ASAS-SN, Prsa+2022, IJspeert+2024 or Kostov+2025 t2/t3/t4.
    SIMBAD lists UCAC4 275-003209 as [SB*], which comes from the Gaia SB1 alone.
- Gaia DR3: vari_summary and vari_eclipsing_binary have no rows, and phot_variable_flag is NOT_AVAILABLE.
    NSS SB1: P 22.357, e 0.585, K1 35.6. RUWE 1.15, rv_amplitude_robust 72 km/s.
- SB9 and WDS: nothing.
- ExoFOP: no TOI or CTOI. TIC contamination ratio 0.049.
- Web search for "TIC 176778312", "UCAC4 275-003209" and "2MASS J03114308-3502457": no hits.
=> A new eclipsing binary.

EPHEMERIDES
A (companion transits the primary): T0 = BTJD 2575.79945 +- 0.00127, P = 22.359363 +- 0.000023 d.
   The A-only fit gives 2575.79943 +- 0.00033 and P 22.359367 +- 0.000006.
B (companion occulted): T0 = BTJD 2594.32784 +- 0.00456, same P.
   B precedes A by 3.831 d, and the interval wanders by up to about 0.02 d.

NEXT PREDICTED ECLIPSES (BTJD)
A: 4342.189, 4364.549, 4386.908, 4409.267, each +-0.002.
B: 4338.358, 4360.718, 4383.077, 4405.436, each +-0.005 formal, plus about +-0.03 d (+-40 min) systematic from the B wander.

WHAT WOULD SETTLE IT FURTHER
1. An RV pair near the two conjunctions would give absolute masses. Infrared spectroscopy is the best chance for an SB2, since lines from the 3900 K companion will be faint.
2. More TESS sectors with B coverage would map the B-A separation over time and test for a tertiary. Gaia DR4 epoch RVs and astrometry could show an outer orbit.
3. A proper eclipsing-binary light-curve model (limb darkening, b, k, J) should replace the trapezoids.

FILES (in vet176778312\; downloads in C:\Home\sky\data\qlp-sb-p20-60\vet176778312\)
- Fits: fits_176778312*.json, fit_*.png
- Ephemeris and physics: ephem_176778312.json, betv.txt, physics.txt
- Independence and difference images: indep.txt, diff.txt, diff_s97.txt, diff_*.png
- Census and neighbours: census*.txt, neighbours.txt
- Archive queries: archives.txt, arch2.txt, cats.txt
