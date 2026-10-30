# TIC 404715740 (TYC 629-1389-1): adversarial check report

Opus 5.5 (subagent of Fable 5.1's session), 2026-10-17. Scripts, outputs and figures are in this folder. Downloads are in `C:\Home\sky\data\qlp-sb-p20-60\vet20261017\404715740\`.

## Verdict: CONFIRMED (new eclipsing SB1; the Gaia period is 3.5 sigma too long)

## Archives (what was queried and what came back)
- cats.py --r 60: the VSX TAP returned HTTP 503 twice, so VSX is unchecked. ASAS-SN: none. SIMBAD: TYC 629-1389-1 [SB*] only.
- VizieR cones (archives_out.txt):
  - WDS 60": nothing
  - Hipparcos main, new reduction, variability annexes: nothing
  - SB9: nothing
  - Gaia DR3 vari_classifier, vari_eclipsing_binary: nothing
  - CCDM: nothing
- Gaia DR3 within 60": the target, plus two stars at G 18.7 and 18.8 (39-41").
- ExoFOP JSON: no TOI, no CTOI, no files, imaging or spectroscopy. The TOI list has no row.
- Web search for "TYC 629-1389-1": no pages about the star.
- MAST (mast_inventory.txt): QLP, TESS-SPOC and TARS for s42, s43, s70 and s71. SPOC also has a 2-min light curve and target pixel file for s42.

## Eclipses (trapezoid + quadratic baseline, prayer-bead errors; trap.json, trap.png, zoom_events.png)
| kind | sector / product | mid-time BTJD | depth | T14 | flat bottom | ingress |
|---|---|---|---|---|---|---|
| A primary | s42 SPOC 2-min SAP (bit 4096 only) | 2456.3406 +- 0.0007 | 20.97% | 6.90 h | 2.1 h | 2.4 h |
| A primary | s43 QLP (TESS-SPOC) | 2492.87984 +- 0.00013 (2492.87952) | 21.36% (21.07%) | 6.96 h | 2.0 h | 2.46 h |
| A primary | s70 QLP (TESS-SPOC) | 3223.68303 +- 0.00010 (same) | 21.55% (21.01%) | 6.95 h | 2.1 h | 2.43 h |
| B secondary | s71 QLP (TESS-SPOC) | 3240.97563 +- 0.00054 (3240.97524) | 3.26% (3.18%) | 9.23 h | 2.55 h | 3.34 h |

- QLP flags the s42 primary (scattered light). SPOC 2-min and TESS-SPOC both record it cleanly, carrying only quality bit 4096. That makes it a third primary.
- Background and centroids are flat through all four events. TARS shows them too.
- Blind dip census (census.txt; QLP and TESS-SPOC q==0, plus SPOC 2-min): nothing else deeper than 0.2%, apart from two things that are not eclipses:
  - TESS-SPOC s71 3253.09 (0.31%) is common-mode: 81% of 102 s71 stars dip by more than 1000 ppm there (s6_common.py, all cadences).
  - The s42 2-min 4096-flagged scattered-light stretches.
- With this ephemeris, no other eclipse of either kind falls in the data:
  - The secondary at 2473.63 falls in the s42/s43 gap.
  - The secondary at 3204.43 falls before s70 starts.
  - The primary at 3260.22 falls after s71 ends.

## Ephemeris (ephem_out.txt)
- Primary: P = 36.54015 +- 0.00003 d, T0 = 2492.88004 +- 0.00038 BTJD (N = -1, 0, 20). O-C is +1.1 / -0.3 / 0.0 min.
- The consecutive s42 to s43 pair alone gives 36.539 d. Counting 19 or 21 cycles across the 731-d gap would give 38.46 or 34.80 d instead, so the cycle count is unambiguous.
- Gaia P = 36.6007 +- 0.0172 d, so the difference is -0.0605 d, or -3.5 sigma.
- Running Gaia's t_peri, e and w with the eclipse period predicts A 0.38 d late (0.5 sigma of t_peri) and B 0.08 d late.
- So the consistent 4-5 d earliness is entirely a Gaia period error, built up over 58-78 cycles from the Gaia epoch. It is not a T_peri error and not a wrong e cos w.
- Secondary phase is 0.47325, i.e. A to B is 17.293 d. Gaia predicts 17.02 +- 0.37 d, so the observed spacing is +0.7 sigma.
- Exact Kepler gives e cos w = -0.0416 (Gaia -0.053 +- 0.016).
- The duration ratio gives e sin w = 0.142 to first order (Gaia 0.140).

## Independence and position
- TESS-SPOC, SPOC 2-min (s42) and TARS all show the eclipses at the same times and depths.
- TESScut difference images (diff_*_s43/s70, difflin_*_s71) put the maximum on the target pixel:
  - primary 20.5% (s43) and 20.3% (s70) per-pixel depth at the target;
  - secondary 3.25% at the target pixel (per-pixel linear baseline across the pre-ingress gap).
- Neighbours: only the G 18.7/18.8 stars at 40". Either would need to dim by 21% x 10^(0.4 x 8.9), far more than 100%, so they are excluded.

## Physics (s8_model.py; model.png, model_out.txt)
- Joint Keplerian two-sphere model with limb darkening, fitted to the s43 and s70 primaries and the s71 secondary. P is fixed. chi2 = 600 for 1171 points.
- Fit results:
  - r1 = R1/a = 0.02264, r2 = 0.01029, k = 0.455
  - i = 89.39 deg; impact parameter b_A = 0.40, b_B = 0.54 (the occultation is just total)
  - central surface-brightness ratio J = 0.174
  - e cos w = -0.0416, e sin w = +0.148, so e = 0.153 and w = 105.7 deg (Gaia 0.150 +- 0.011, 110.7 +- 6.4)
- Fixing e sin w at Gaia's 0.140 costs only delta chi2 = 19 and changes nothing else.
- Mass function f(m) = 0.0605 Msun. With M1 = 1.25 Msun, m2 = 0.589 Msun (0.55-0.63 for M1 = 1.1-1.4) and a = 56.8 Rsun.
- That gives R1 = 1.29 Rsun (TIC 1.41), log g1 = 4.32, and R2 = 0.58 Rsun, a normal main-sequence radius for 0.59 Msun.
- J gives T2 of about 4070 K, a K7-M0 dwarf contributing 3.3% of the TESS light.
- Deep eclipse (A, nu = 90 - w): the dwarf transits the F star, U-shaped from limb darkening. Shallow eclipse (B): the F star occults the dwarf, flat-bottomed.
- Depths, durations, shapes, the timing-derived e and w, the RV mass function and the TIC radius all fit one geometry.

## Next eclipses (BTJD; uncertainty under 0.1 h)
- Primary (A): 4356.428, 4392.968, 4429.508, 4466.048, 4502.588, 4539.128 (T0 2492.88004 + 36.54015 N)
- Secondary (B): 4337.180, 4373.720, 4410.260, 4446.801, 4483.341, 4519.881 (phase 0.47325; based on a single event, so about 0.01 d)

## What would settle it further
- It is already settled as an EB.
- A second secondary would pin e cos w beyond one event.
- Ground photometry of a primary (21%, mid-time 4356.43 BTJD = JD 2461356.43) would check the period.
- RVs at quadrature would give an SB1 orbit with the corrected P. Gaia DR4 epoch RVs should show the 36.540-d period.
- Retry VSX when its TAP is up.
