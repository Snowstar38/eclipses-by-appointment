TIC 160300523 (TYC 5939-78-1) - adversarial check - VERDICT: CONFIRMED
Checked by Opus 5.5, 2026-10-20/21. I resumed a run that a usage limit had cut short, re-ran or spot-checked
every earlier output, and finished the rest. Scripts and outputs are in this folder; downloads are in
sky\data\qlp-sb-p20-60\vet160300523\.

WHAT IT IS
A detached, eccentric, grazing eclipsing binary on the target: the Gaia SB1 orbit seen edge-on. A 0.69 Msun
K dwarf orbits a 1.12 Msun F/G star at i = 88.3 deg, and both eclipses are partial.

DECIDING NUMBERS
- Primary (deep) eclipse = Gaia conjunction A. Depth 11.1-11.6% in QLP SAP (9.4% in s98, where the aperture
  dilution differs) and 11.3-11.4% in TESS-SPOC PDCSAP. T14 5.15 h, T12 2.05 h, V/U-shaped. Seen at all 4 epochs.
- Secondary (shallow) eclipse = conjunction B. Depth 0.94-1.14%, T14 4.75-5.02 h. 3 clean events, plus s98 E67,
  which falls across a data gap and is consistent with the ephemeris.
- Period: 37.312955 +- 0.000007 d from the eclipses, against Gaia 37.3106 +- 0.0092 d (-0.26 sigma).
- Secondary phase: 0.774030 +- 0.000036, against Gaia's B-A of 0.7741 +- 0.0077 (0.0 sigma).
- Every eclipse falls +0.08 to +0.19 d after the Gaia-predicted conjunction (0.14-0.22 sigma).
- Difference images put the deficit on the target to within 0.6" in all 4 (P and S, in s33 and s87).
- The 12.9" neighbour (G 12.50) is 0.6 px from the deficit. It is a background star (parallax 1.30 vs 3.52 mas),
  so WDS ARA 337 is an optical pair.
- Five other pipelines time the eclipses within 2 min of QLP. TGLC's PSF photometry, which deblends the
  neighbour, gives the deepest eclipse (15.3%), which points to the target.

1. ARCHIVES (re-run 2026-10-21)
- cats.py: VSX none; ASAS-SN none; no hits in Prsa+2022, IJspeert+2024 or Kostov+2025 t2/t3/t4; SIMBAD lists
  the star as SB*.
- Gaia DR3 vari_summary and vari_eclipsing_binary: 0 rows. The NSS solution is SB1: P 37.31057 +- 0.00921,
  e 0.4584 +- 0.0121, omega 15.0 +- 1.8 deg, K1 33.14 +- 0.53 km/s, RUWE 1.91.
- SB9: 0 rows. WDS ARA 337 is the 12.9" field star.
- ExoFOP: yesterday's run found no TOI or CTOI and a TIC contamination ratio of 0.276. Today the connection was
  refused twice, so that result is unverified.
- Web search for "TYC 5939-78-1" OR "TIC 160300523": nothing on the star.
- MAST light curves: QLP 6/33/87/98, TARS 6/33/87, TESS-SPOC 6/33, TGLC 6, eleanor-lite 6, TASOC 6.
- Status: not catalogued as an eclipsing binary anywhere I checked.

2. ECLIPSES (raw QLP SAP, q==0, no trimming; trapezoid x quadratic baseline over +-0.6 d; the all-cadence
   fit is identical)
  sec kind  E   t0 BTJD       +-min  depth   T14h  T12h  flat h
   6   P    0  1473.96702     0.3   11.07%  5.16  2.07  1.02
  33   P   20  2220.22666     0.2   11.60%  5.14  2.05  1.04
  87   P   59  3675.43198     0.1   11.40%  5.14  2.05  1.05
  98   P   68  4011.24813     0.1    9.37%  5.16  2.06  1.04
  33   S   19  2211.79445     1.3    1.09%  4.77  1.84  1.10
  87   S   58  3666.99942     1.4    1.14%  4.75  1.89  0.96
  98   S   68  4040.12790     1.4    0.94%  5.02  2.14  0.73
  98   S   67  4002.8131      3.0   (shape fixed, ingress only; gap 4002.797-4003.010 and a post-gap ramp)
                                    O-C +1.6 min; left out of the ephemeris
- Common mode (about 400 stars per sector, at three secondaries and one primary): median dip 0.01% or less.
  The target ranks 1st or 2nd and is the only star above 5 sigma in 3 of the 4 tests.
- SAP_BKG excursions in eclipse are small and mostly negative, which would raise the flux rather than fake a dip.
- The x-centroid shifts 7-17 mpx in the primaries and about 1 mpx in the secondaries, in proportion to depth,
  as a fixed blend does when the target dims.
- Blind census (0.2% threshold, 1-h bins): s6, s33 and s87 are clean. s98 has only dips 0.1-0.2 d before data
  gaps (3995.5 at 0.45%; 4009.7, 4024.2 and 4038.5 at 0.2-0.33%). At 3995.5, 27 unrelated stars also dip at
  more than 5 sigma, so this is a sector systematic.

3. EPHEMERIDES
- Primary: BTJD 1473.96743(35) + 37.312955(7) E. O-C -0.59, +0.19, +0.32, -0.32 min. chi2 15.4/2, so the errors
  are scaled. A quadratic term gives chi2 1.8, but pipelines differ by about 1 min at 30-min cadence, so this is
  not significant.
- Secondary: BTJD 1502.84878(131) + 37.312934(26) E. O-C -0.11, +0.69, -0.55 min; chi2 0.4/1.
- Observed minus Gaia-predicted conjunction:
    A: s33 +0.08 d (0.18 sigma), s87 +0.17 d (0.22 sigma), s98 +0.19 d (0.22 sigma)
    B: s33 +0.08 d (0.14 sigma), s87 +0.17 d (0.19 sigma), s98 +0.19 d (0.20 sigma)
- e cos w from the timing is 0.4425-0.4456, against Gaia's 0.4426 +- 0.0138 (0.0-0.2 sigma).
- e sin w from my own limb-darkened two-sphere Keplerian fit to both s87 eclipses (ebfit.py) is 0.115, against
  Gaia's 0.1187 +- 0.0132. The profile is flat: dchi2 is 0.0 at -0.05, 4.4 at 0, 0.5 at 0.05, 0.2 at 0.1187 and
  1.2 at 0.17, so the shapes barely constrain e sin w and Gaia's value fits.
- Best fit: e 0.457, w 14.6 deg, i 88.26 deg, R1/a 0.0201, R2/a 0.0123, J 0.30, L2/L1 0.114, rms 0.92 ppt.
- A uniform-disk model that reads the trapezoid flat as T23 (geom.py) gave e sin w -0.015, 9 sigma from Gaia.
  That is an artefact: both eclipses are grazing and limb-darkened, so there is no true T23.

4. INDEPENDENCE
- Other pipelines, mid-time minus QLP: TESS-SPOC SAP/PDCSAP (s6, s33) -0.1 to -0.3 min; TGLC aperture/PSF (s6)
  -0.8/-1.1 min; TASOC (s6) +0.1 min; eleanor-lite (s6) -0.1 min; TARS (s6, s33, s87) -1.3 to +2.1 min.
  PDCSAP depths are 11.3-11.4% (P) and 1.14% (S).
- Difference images (TESScut 15x15): the deficit centroid sits within 0.01-0.03 px of the target; the
  out-of-eclipse light centroid is pulled about 0.2 px toward the neighbour. The brightest deficit pixel is the
  target pixel in 3 of 4 images, and the pixel next to it in S s33.
- Neighbour dilution (depth needed = 11.4% x 10^(0.4 dm)):
    G 12.50 at 12.9" -> 35.6%, excluded by the difference image and the TGLC PSF depth.
    G 15.16 at 43.2" -> 417%, impossible.
  Everything else within 60" is fainter than G 17.

5. PHYSICS
- f(M) = 0.0987 [0.0941, 0.1035] Msun. With M1 = 1.118 Msun (TIC), m2 = 0.685 Msun at i = 88.3 deg, and
  a = 57.2 Rsun.
- The model gives R1 = 1.15 Rsun (TIC 1.24) and R2 = 0.70 Rsun (main sequence about 0.66).
- J = 0.30, against a blackbody value of 0.33 for T2 of about 4400 K.
- At A (separation 0.706 a) the K dwarf is in front of the primary; at B (0.896 a) the primary is in front.
- Central T14 would be 7.45 h (A) and 9.46 h (B). The observed 5.15 and 4.85 h follow from b_A 0.66 and b_B 0.84,
  whose ratio is fixed by the orbit.
- Both eclipses are partial. A total occultation would be about 8% deep; B is 1.1%.
- All of this is one consistent geometry.

6. NEXT ECLIPSES (BTJD)
  Primary (A, about 11%): 4347.0649, 4384.3779, 4421.6909, 4459.0038, 4496.3168 (+-0.9 min each)
  Secondary (B, about 1.1%): 4338.6318, 4375.9447, 4413.2576, 4450.5706, 4487.8835 (+-3.4 min each)

WHAT WOULD SETTLE IT FURTHER
- Near-IR SB2 RVs or multi-colour primary-eclipse photometry, to pin e sin w and the radii.
- More TESS sectors, to tell whether the primary-timing chi2 of 15/2 is systematics or a real ETV.
- It is ready for a VSX submission as a new EA.
