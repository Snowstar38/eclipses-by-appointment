TIC 320805993 (TYC 8787-921-1, Gaia DR3 6447155071357750400) - adversarial check, 2026-10-21

VERDICT: CONFIRMED. A detached eccentric EB, P = 56.17388 d, e = 0.31, w = 109 deg, i = 89.5 deg. It is an F8/G0
primary (~1.1 Msun, ~1.4 Rsun, Teff 5900) and a K-dwarf companion (~0.66 Msun, ~0.65 Rsun, 5.7% of TESS light).
- The eclipses are on the target, and the orbit agrees with Gaia SB1 to within 0.8 sigma in e cos w, e sin w, e and w.
- No prior art found: not in any EB or variable catalogue, and the Gaia DR3 vari tables are empty.
- One new finding: QLP under-reports the B depth in s101/s103 (4.6/3.5%). Own TESScut photometry gives a constant
  5.3-5.4% in all three B events, and the B depth does not vary.

1 ARCHIVES (2026-10-21)
- cats.py (60"): nothing in VSX, ASAS-SN, Prsa22, IJspeert24 or Kostov25 t2/t3/t4. SIMBAD has SB* only; its only
  reference is Gaia DR3 2023A&A...674A..34G.
- VizieR cones (60"): 0 rows in ZTF-periodic, ATLAS, ASAS-SN II/366, WISE vars, VSX, SB9, WDS, ASAS ACVS, KELT,
  Justesen21 and the TESS OBA EBs. The J/A+A/674/A16 cone hit an unrelated X-ray table.
- Gaia DR3 vari_classifier/summary/eclipsing_binary/rotation/LPV: all empty. phot_variable_flag NOT_AVAILABLE.
- NSS SB1: P 56.168 +- 0.029, e 0.343 +- 0.038, w 111.3 +- 3.8, K1 26.78 +- 0.77 km/s, significance 35.
- RUWE 1.52, ipd_frac_multi_peak 1. Only mildly elevated; the photocentre orbit could cause it.
- ExoFOP: no TOI or CTOI. The TIC contamination ratio is 0.006.
- No ZTF (dec -58.7).
- Web search on the TYC, TIC and 2MASS names: nothing.

2 ECLIPSES
Six events: P (deeper) x3 at A, S x3 at B.
- QLP SAP q==0 (trapezoid ecl.py, mirror ecl2.py):
  s13 P 1676.76567 21.8%; s67 P 3137.28746 22.6%; s94 P (egress flagged in QLP, so own photometry is used);
  s27 S 2038.14965 5.27%; s101 S 4116.58093 4.56%; s103 S 4172.75443 3.54%.
- Own TESScut photometry (r=1.5 px aperture, local background, q==0; cutfit.py), used for the ephemeris:
 sec kind  t0 BTJD      +-min  depth   T14trap  T12    flat
 13  P  1676.76578  0.3  22.70%  7.53h  2.57h  2.39h
 67  P  3137.28727  0.8  22.45%  7.61   2.62   2.36   (allq: same t0)
 94  P  3867.54726  0.6  22.65%  7.55   2.59   2.38
 27  S  2038.15009  0.4   5.37%  13.44  5.08   3.28
 101 S  4116.58283  0.3   5.36%  13.42  5.11   3.20
 103 S  4172.75761  0.6   5.31%  13.49  5.13   3.24   (allq: same)
- Depth check, 1x1 / 3x3 / 5x5 apertures on the cutouts: P 22.7-23.0% and S 5.2-5.5% in every sector. The QLP
  s101/s103 S depths (and the s94 P depth of ~20%) are diluted in QLP: a pipeline background/aperture issue, not
  astrophysical. TESS-SPOC SAP/PDCSAP: s13 P 22.3-22.6%, s27 S 5.24-5.31%.
- Timing across pipelines: S mid-times differ between pipelines by up to 2-5 min (shallow 13-h events). Treat the S
  timing error as ~2 min.
- Background and centroids: SAP_BKG is smooth through all six events (within +-1.9 sigma). The s67 eclipse sits
  ~0.3 d before a scattered-light ramp, not on a known common-mode time.
- Census: unmasked at 2%, it finds exactly the six events (plus a flagged spike at 3869.62). Masked at 0.3%, every hit
  is at a segment start right after heavily flagged scattered-light/momentum blocks (s94 3869.7, s101 4113-4114,
  s103 4153) or at a sector start. No other dips.
- Every covered A and B window contains its eclipse. There are no empty covered windows.

3 EPHEMERIDES AND ORBIT (TESScut timings)
- P(A): T0 = 1676.76580 +- 0.00021, P = 56.173887 +- 0.000011 d, chi2 0.6/1, O-C <= 0.6 min.
- S(B): T0 = 1701.10690 +- 0.00064, P = 56.173863 +- 0.000018 d, chi2 3.9/1 (errors scaled).
- With QLP S timings: P = 56.173816 +- 0.000013. The P-S difference is 1-2 sigma, i.e. the S timing systematics;
  there is no evidence of apsidal motion.
- Against Gaia: 56.16849 +- 0.02853, -0.2 sigma.
- Against the Gaia conjunctions (full covariance): A events -0.34/-0.20/-0.13 d (-0.33/-0.11/-0.06 sigma); B events
  +0.68/+0.85/+0.86 d (+1.06/+0.58/+0.57 sigma). S phase is 0.43331, against Gaia 0.4168 +- 0.0203 (+0.8 sigma).
- EB model (ebfit3 on own photometry; two LD spheres, Kepler orbit, u=0.45 fixed):
  ecosw -0.1002, esinw 0.297 (formal +-0.002; realistic +-~0.01), e 0.314, w 108.6 deg, i 89.50,
  R1/a 0.01855, R2/a 0.00869 (k 0.47), J 0.27, L2/L1 0.060. Model T14: A 8.3 h, B 14.4 h.
- Against Gaia: ecosw -0.124 +- 0.030 (+0.8 sigma), esinw 0.319 +- 0.032 (-0.7 sigma), e 0.343 +- 0.038 (-0.8 sigma),
  w 111.3 +- 3.8 (-0.7 sigma).
- The duration ratio B/A (T14 13.4/7.55 = 1.78) confirms the large positive e sin w: B occurs near apastron.

4 INDEPENDENCE
- TESS-SPOC SAP/PDCSAP: s13 P at 1676.76564-6 (same as QLP to 0.0 min); s27 S at 2038.1501 (+0.6 min against QLP).
- SPOC s67 flags the whole eclipse (scattered light), but the raw SAP shows it at 0.79.
- Own TESScut photometry of all six events (above).
- Difference images (s67 P, s94 P, s27 S, s101 S): the deficit peaks on the target pixel, centroid within 0.1 px
  (0.5-2"). Depth on the target pixel is 22.4-22.9% (P) and 5.3-5.4% (S). 81-85% of the deficit lies in the 3x3, versus
  75-77% of the light. The neighbour pixels show only the wings of the target PSF.
- Neighbour dilution: there is nothing brighter than G 19.1 within 60". Beyond that:

 neighbour  sep    dG    depth it would need for the 23% P
 G 13.74    71"    2.7   266%
 G 15.37    65.5"  4.3   1200%
 G 15.74    62"    4.7   1700%
 G 19.11    19"    8.0   >30000%

  Contamination is excluded.

5 PHYSICS
- f(m) = 0.093 +- 0.008 Msun.

 M1    m2(i=89.5)  a        R1    R2    K2
 1.0   0.63        72.6 Rs  1.35  0.63
 1.1   0.66        74.5 Rs  1.38  0.65  45 km/s
 1.3   0.72        78.1 Rs  1.45  0.68

- The primary has logg 4.2 (Gaia GSP-Phot 4.0, Teff 5940); the TIC gives 1.58 Rsun from blended light.
- J = 0.27 means T2 ~ 4100-4300 K: a K5 dwarf of ~0.65 Msun and R ~0.64 Rsun, consistent with the dynamical m2.
- At A (P, near periastron, r = 0.70 a) the K dwarf transits the primary, impact b ~ 0.33 R1: a full transit, 23%.
- At B (S, near apastron, r = 1.28 a) the primary occults the K dwarf with b ~ 0.60 R1, just short of total
  (1 - k = 0.53). The depth of 5.4-5.5% is close to the companion light fraction of 5.7%.
- Durations: the B/A ratio follows e sin w, and the model matches both shapes (rms 1.2 ppt, chi2/N 1.0).

6 NEXT ECLIPSES (BTJD; today ~ 4334.5)
- P (A, 23%, 7.6 h): 4373.1124, 4429.2863, 4485.4602, 4541.6341 (+-1 min)
- S (B, 5.4%, 13.4 h): 4341.2785, 4397.4523, 4453.6262, 4509.8001 (+-2 min realistic; formal 1.5)

FURTHER
- Already settled as an EB on the target.
- Double-lined spectroscopy, to get K2 and absolute masses.
- A fit with free LD and third light, to refine i and e sin w and decide whether B is total.
- The next S events at 4341.28 and 4397.45 would pin down the P(S) vs P(P) timing systematics.
- A note for Fable: QLP s101/s103 depths for this field are diluted by ~15-35%. Depth-based comparisons on those
  sectors need a check against another pipeline.
