TIC 233640767 (TYC 3481-179-1) - adversarial check - VERDICT: CONFIRMED (the B offset is not significant)
Checked by Opus 5.5, 2026-10-20/21. I resumed a run that a usage limit had cut short, re-ran or spot-checked
every earlier output, and finished the rest. Scripts and outputs are in this folder; downloads are in
sky\data\qlp-sb-p20-60\vet233640767\.

WHAT IT IS
A detached, eccentric eclipsing binary on the target: the Gaia SB1 orbit seen edge-on.
- Primary eclipse (A): a 0.73 Msun K dwarf crosses a 1.2 Msun, R 1.6 Rsun F star near apastron
  (separation 1.32 a). Depth 15%, T14 about 13-14 h.
- Secondary eclipse (B): a total occultation of the K dwarf near periastron (separation 0.53 a).
  Depth 5.5%, T14 about 5.8 h, flat for 2.5 h.

DECIDING NUMBERS
- The B offset is one phase offset, not five independent ones. The secondary sits at phase 0.34680, against
  Gaia's B-A of 0.3256 +- 0.0137 (+1.55 sigma). The five B events at +1.75 to +1.87 sigma all come from that
  single e cos w offset (0.2184 eclipses vs 0.2511 +- 0.0209 Gaia, +1.56 sigma) and the period.
- Against Gaia's full covariance (gaiacomp.py):
    P +1.58 sigma, tA -0.18, phase +1.55, e sin w -0.67, e cos w +1.56.
    Joint (P, tA, phase): d2 = 4.82 for 3 dof, p = 0.19.
    Adding e sin w: d2 = 5.93 for 4 dof, p = 0.20.
  So the Gaia orbit agrees with the eclipses at about 1.3 sigma overall.
- Eclipse-derived elements: e = 0.489, w = 243.5 deg, against Gaia's e 0.4958 +- 0.0142 and
  w 239.5 +- 2.6 deg (-0.45 and +1.5 sigma).
- The star is isolated. The brightest Gaia source within 60" is G 19.36, which would need a depth of about 22000%.
  The difference images put the deficit on the light centroid to within 0.8".
- TESS-SPOC and TARS reproduce the timing to within about 1 min, except at the gap-affected events.

1. ARCHIVES (re-run 2026-10-21)
- cats.py --r 60: VSX none; ASAS-SN none; no hits in Prsa+2022, IJspeert+2024 or Kostov+2025 t2/t3/t4;
  SIMBAD lists the star as SB*.
- Gaia DR3 vari_summary and vari_eclipsing_binary: 0 rows. The NSS solution is SB1: P 30.29790 +- 0.00510,
  e 0.4958 +- 0.0142, w 239.54 +- 2.60 deg, K1 36.80 +- 0.62 km/s, RUWE 1.18, Teff_gspphot 6089 K,
  logg 4.09.
- SB9: 0 rows. WDS: 0 rows.
- ExoFOP: yesterday's run found no TOI or CTOI and a contamination ratio of 0.00055. Today the connection was
  refused, so that result is unverified.
- Web search for "TYC 3481-179-1" OR "TIC 233640767": nothing on the star.
- MAST light curves: QLP, TARS and TESS-SPOC each have s16/23/24/50/51/77.
- Status: not catalogued as an eclipsing binary anywhere I checked.

2. ECLIPSES (raw QLP SAP, no trimming; trapezoid x quadratic baseline; P window +-1.0 d, S window +-0.5 d)
  sec kind  E   t0 BTJD       +-min  depth   T14h   T12h  flat h  note
  16   P    0  1752.76493     0.7   15.08%  13.04  5.08  2.88
  23   P    6  1934.60028     0.6   15.90%  13.21  5.28  2.66   all-cadence fit; 19/27 in-eclipse cadences
                                                                  carry QUALITY 4096, but the flux is smooth
  24   P    7  1964.90697     0.7   15.24%  13.11  5.23  2.65
  77   P   55  3419.59200     0.4   15.05%  13.11  5.17  2.76
  23   S    6  1945.11126     0.3    5.79%   5.79  1.63  2.52
  24   S    7  1975.41581     0.3    5.53%   5.97  1.73  2.52
  50   S   30  2672.4562      0.7    5.6%   (shape fixed)        ingress lost in gap 2672.249-2672.430;
                                                                  egress-only fit, error inflated to 2 min
  51   S   31  2702.76057     0.3    5.61%   5.67  1.54  2.58
  77   S   54  3399.79717     0.4    5.48%   5.65  1.50  2.65
  Unusable: s16 S (1763.27; all flagged, at sector end) and s50/51 P (2692.25; between sectors).
- Common mode (156-425 stars per sector, at 4 S and 2 P events): median dip under 0.02%. The target ranks
  1st or 2nd among the q==0 stars every time.
- SAP_BKG drops during the eclipses (strongest in the s77 primary), which is consistent with the target's own
  light reaching the background annulus. A drop cannot fake a dip.
- Centroid shifts are 0-2 mpx, as expected for an unblended star. The exception is s50 S, which is post-gap.
- Blind census (1-h bins, eclipses masked): nothing deeper than 0.4% in any sector. At the 0.2% level there
  are only short 0.2-0.35% noise excursions, mostly in the noisier s50 and s51; none is eclipse-like.

3. EPHEMERIDES
- Primary: BTJD 1752.76490(29) + 30.305947(8) E. O-C +0.04, -0.43, +0.64, -0.00 min; chi2 1.3/2.
- Secondary: BTJD 1763.27493(56) + 30.305976(21) E. O-C +0.69, -1.36, +2.87, +0.55, -0.67 min; chi2 30.4/3.
  The 30-min-cadence errors are underestimated: including flagged cadences moves s24 S by 1 min, and SPOC
  PDCSAP puts it +1.2 min later. The errors are scaled accordingly.
- P_S - P_P = 0.041 +- 0.032 min/cycle, so no apsidal motion is detected.
- Against Gaia: P(eclipses) - P(Gaia) = +0.0081 d (+1.58 sigma). There are no aliases (P/2 and 2P are each
  more than 2900 sigma away).
- Observed minus Gaia-predicted conjunction:
    A: s16 -0.12 d (-0.37 sigma), s23 -0.07 (-0.21), s24 -0.07 (-0.19), s77 +0.32 (+0.67)
    B: s23 +0.57 (+1.87), s24 +0.58 (+1.86), s50 +0.77 (+1.80), s51 +0.78 (+1.80), s77 +0.96 (+1.75)
- Geometry from my own limb-darkened two-sphere Keplerian model, fitted to both s77 eclipses at 200-s
  cadence (ebfit.py): e cos w -0.2184, e sin w -0.4379 (e 0.489, w 243.5 deg), i 89.11 deg, R1/a 0.0314,
  R2/a 0.0130, J 0.34, L2/L1 0.059, rms 1.29 ppt.
  - The shapes do pin e sin w here: dchi2 is 25.7 at Gaia's -0.4269, about +-0.002 formally (red noise not
    included).
  - Profile dchi2: 453 at -0.39, 104 at -0.46, 867 at -0.50.
  - Model T14: 14.06 h (A) and 6.12 h (B). The trapezoid underestimates A's because of the limb-darkened
    ingress.

4. INDEPENDENCE
- Other pipelines, mid-time minus QLP:
    TESS-SPOC SAP/PDCSAP: s16 +0.3; s24 -0.3 to +1.2; s51 -0.4 to -0.5; s77 +0.1 min. PDCSAP depths are
    14.8-15.0% (P) and 5.35-5.5% (S).
    TARS: s16 +0.9; s23 -0.2 (P) and +0.8 (S); s24 0.0/-0.7; s51 -0.5; s77 +2.2 (P) and +0.6 (S) min.
- Exceptions:
    SPOC s23 P: -16 min. SPOC flags most of the in-eclipse cadences there; TARS agrees with QLP.
    s50 S: +7 to +19 min in every pipeline, because the ingress is in the data gap. Hence the 2-min error.
- Difference images (TESScut 15x15):
    P s77: 103 in-eclipse cadences; deficit centroid (7.69, 7.97) = light centroid (7.69, 7.97); depth 14.3%,
      14.1% and 14.0% in 1x1, 3x3 and 5x5 apertures.
    S s77: offset 0.8"; depth 5.4-5.5%, flat across apertures.
    P s24: offset 0.3"; 14.4/14.3/14.3%.
    S s24: offset 0.7".
  The deficit share inside 3x3 matches the light share (0.82 vs 0.81).
- Neighbour dilution (depth needed = 15% x 10^(0.4 dm)):
    G 19.36 at 49.5" -> about 22000%.
    G 20.07 at 40.5" -> about 43000%.
  Both impossible; nothing within 40".

5. PHYSICS
- f(M) = 0.1024 [0.0974, 0.1076] Msun; a1 sin i = 19.1 Rsun.
- For M1 = 1.22 Msun (TIC; Teff 6256 K, R 1.7 Rsun), m2 = 0.73 Msun at i = 89.1 deg, and a = 51.1 Rsun.
  For M1 from 1.1 to 1.35, m2 runs 0.69-0.77.
- The model gives R1 = 1.60 Rsun and R2 = 0.66 Rsun (main sequence 0.70). rho1 is about 0.30 solar, which fits
  a slightly evolved F star and Gaia's logg 4.09.
- J = 0.34, against a blackbody value of 0.32 for T2 of about 4500 K. L2/L1 = 0.059.
- A (separation 1.317 a, b = 0.46 in units of R1+R2): the K dwarf transits the F star, giving 15%. Central T14
  would be about 15.6 h; with b it is 13.8-14.1 h. Observed: 13.1 h by trapezoid, 14.06 h by the model.
- B (separation 0.528 a, b = 0.18): the F star totally occults the K dwarf, since 0.0082 a < R1-R2 = 0.0184 a.
  The predicted depth is L2/(L1+L2) = 5.6%; observed 5.5%. The flat bottom of 2.5-2.65 h is real totality.
- Everything fits one geometry, with Gaia's orbit agreeing at the 1.3-1.6 sigma level.

6. NEXT ECLIPSES (BTJD)
  Primary (A, 15%, about 14 h long): 4359.0764, 4389.3823, 4419.6883, 4449.9942, 4480.3002 (+-1.0-1.1 min)
  Secondary (B, 5.5%, total, about 6 h): 4339.2829, 4369.5889, 4399.8948, 4430.2008, 4460.5068 (+-2.6-2.8 min)
  Ephemerides: P 1752.76490(29) + 30.305947(8) E;  S 1763.27493(56) + 30.305976(21) E.

WHAT WOULD SETTLE IT FURTHER
- Gaia DR4 epoch RVs (or new RVs) fitted with e and w fixed to the eclipse values. This would test whether the
  1.5-sigma phase and period offsets are just Gaia DR3 noise; I expect they are.
- More 200-s TESS sectors, to tighten the secondary timing and test for apsidal motion.
- It is ready for a VSX submission as a new EA (P 30.30595 d, secondary at phase 0.3468).
