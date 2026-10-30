Adversarial check: TIC 233606058 (TYC 4216-238-1, Gaia DR3 2156722539268511360)
Second vet run, resumed 2026-10-21 from the run killed on 2026-10-20. I re-verified the inherited Gaia, MAST and cats queries.
Scripts and outputs are in this folder; downloads are in sky\data\qlp-sb-p20-60\vet233606058\.

VERDICT: CONFIRMED
This is a detached, slightly eccentric eclipsing binary on the target, at the Gaia SB1 period. It shows a transit (A, 17.7%) and a total occultation (B, 17.1%) at every covered conjunction from 2019 to 2024. I found it in no EB catalogue I could query; ExoFOP could not be checked.

1. ARCHIVES (what was queried and what came back)
- cats.py --r 60 (rerun): no VSX, ASAS-SN, Prsa+2022, IJspeert+2024, or Kostov+2025 t2/t3/t4 entry. SIMBAD has only "SB*".
- Gaia DR3 TAP: vari_eclipsing_binary, vari_summary and vari_classifier_result return 0 rows; phot_variable_flag is NOT_AVAILABLE.
  The NSS SB1 solution: P 21.73575(313) d, e 0.0826(116), w 135.7(6.3) deg, K1 42.02(44) km/s, corr(w, Tp) = 0.995.
- VizieR 60" cones (archives2.txt) on about 28 catalogues returned 0 rows in each of these:
    Variable-star catalogues: VSX, GCVS, ASAS-SN II/366, Hipparcos/Tycho var, NSVS, ZTF (Chen+2020), ATLAS (Heinze+2018), WISE vars
    Eclipsing-binary catalogues: Prsa+2022, IJspeert+2021, IJspeert+2024, Justesen+2021, Rowan+2022
    Other TESS / survey variability: Fetherolf+2023
    Gaia DR3 variability: I/358
    Binary / multiple-star catalogues: SB9, WDS
    Spectroscopic surveys: RAVE, LAMOST, GALAH
  Exact-TIC lookups in Prsa+2022 and IJspeert+2024 also returned 0.
- Non-empty but not prior art:
  - Kostov+2025 table2, the unvetted ML list, contains the 37" neighbour TIC 233606060 (Tmag 12.8), not the target. The likely cause is our eclipses leaking into that star's aperture.
  - Green+2023 lists the target with score 0.0075, a non-detection.
  - KELT (Oelkers+2018) lists only rms statistics.
  - The cone on "J/A+A/674/A16" returned a non-EB table and is not the Mowlavi EB catalogue; the Gaia TAP result above is the authoritative one.
  - APOGEE DR17 has 2 visits, used in section 4.
- ExoFOP: connection refused, both from Python and from WebFetch. NOT CHECKED.
- Web search on "TYC 4216-238-1", "TIC 233606058", the Gaia id and 2MASS J18512734+6120136 found nothing relevant.

2. ECLIPSE MEASUREMENTS
Method: raw QLP SAP_FLUX, q==0, no trimming; a trapezoid times a quadratic baseline over +-1 d. Flagged cadences were fitted too (ecl_allq).
I fitted 84 events in 39 sectors (s14-s86) and dropped four:
- s55 A E52 (scattered light)
- s59 A E57 (partial)
- s84 A E88 (no ingress)
- s57 B E54 (no ingress)
I added s17 A E4 and s21 A E9, which can only be measured with the flagged cadences. That leaves 80 events: 36 A and 44 B.

  Kind  Depth              T14                 T12     Flat    Shape
  A     17.66% (sd 0.30)   10.85 h (sd 0.05)   3.57 h  3.72 h  rounded bottom (transit)
  B     17.12% (sd 0.28)   12.06 h (sd 0.07)   3.60 h  4.87 h  flat bottom (total occultation)

- Background: the in-eclipse change is -0.3% (A) and -1.5% (B) of the target flux, against -0.04% and -0.15% at control phases. The background is not the cause; the small drop fits target light falling in the background annulus.
- Centroids: SAP_X/Y move by 15-20 millipixels in eclipse and about 0 at control phases. The difference image explains this: the light centroid is pulled toward the G 13.5 neighbour when the target dims.
- Blind census of all sectors (outside +-0.4 d of both eclipses, threshold 0.3%): nothing, apart from scattered-light noise in s54/s55 (maximum 4.4%) and one 0.33% wiggle in s22. There is no third family of dips.

3. EPHEMERIDES AND ORBIT
  Kind  T0 (BTJD)               P (d)                    chi2/dof (1-min floor)  rms
  A     1691.30913 +- 0.00020   21.737275 +- 0.000004    32.3/34                 0.98 min
  B     1701.00795 +- 0.00020   21.737274 +- 0.000004    42.8/42                 1.00 min

- P_B - P_A = -0.002 +- 0.007 min per cycle, so no apsidal motion is detected over 6 years. A quadratic term is not needed.
- The TESS period minus Gaia's is +0.0015 d, which is +0.49 sigma.
- QLP s80 runs +3 min late for all three of its events. TESS-SPOC s80 is on the ephemeris, so this is a QLP timing artefact.
- The "+0.3 d A offset":
  - Measured minus Gaia-predicted conjunction is A +0.24 to +0.38 d and B -0.11 to +0.03 d. With independent errors that is at most 0.54 sigma; with corr(w, Tp) = 0.995 it is 0.8-1.2 sigma.
  - The cause is the B-A phase: measured 0.44618, Gaia-predicted 0.4627 +- 0.0067 (-2.5 sigma). That gives e cos w = -0.0845 against Gaia's -0.059 +- 0.011 (-2.4 sigma).
  - The duration ratio T_B/T_A is 1.1117 +- 0.0013, against Gaia's 1.121 +- 0.023 (-0.4 sigma).
  - My own two-sphere EB fit (ebfit.txt: s56/58/80/81, rms 0.91 ppt, chi2/N 1.00) gives:
      e cos w   -0.08448
      e sin w   +0.0488 +- 0.0004
      e         0.0975 (Gaia 0.083 +- 0.012)
      w         150.0 deg (Gaia 135.7 +- 6.3)
      i         88.99 deg
      R1/a      0.0535
      R2/a      0.0234
      J         1.07
      L2/L1     0.205
  - The APOGEE RVs prefer the eclipse values (section 4). Gaia's e and w are about 2 sigma off, most likely from blending with the companion's lines (L2/L1 = 0.2 at nearly equal Teff). This is a refinement, not a problem.

4. INDEPENDENCE
- Other pipelines (secondpipe.txt):
  - TESS-SPOC SAP (s14/26/80/84/85) and TASOC (s14/26) reproduce both kinds with the same T14 and T12. Mid-times agree with QLP to within 0.2-4 min.
  - TESS-SPOC SAP depths are 15.3-16.4%. That is QLP's depth times CROWDSAP (0.90-0.95), i.e. 17.1-17.5% undiluted.
- Difference images (TESScut s80 at 200 s, and s14; diff.txt and diff_*.png):
  - The flux deficit centres on the target: 0.02 px off in s80, 0.15 px in s14. The brightest deficit pixel is the target pixel, at 17.0% (A) and 16.6% (B).
  - The G 13.52 neighbour's pixel loses only 4-7%, which is the target's wings.
- Neighbours (neighbours.txt): all 15 Gaia sources within 60" would need dips above 100%. The brightest, G 13.52 at 36.5", would need 128% (A) and 124% (B). Unresolved companions are unlikely: RUWE 0.83, ipd_frac_multi_peak 0.
- Spectroscopy (apogee_rv.txt): APOGEE DR17 has 2 visits in 2018, 1.5 years before TESS: RV -71.25 and -58.28 km/s, Teff 5783, logg 4.00, vsini 8.7.
  - Phased on the TESS A ephemeris, the SB1 orbit predicts them to within -1.1 / +0.7 km/s with the eclipse e and w, and +1.2 / +3.5 km/s with Gaia's.
  - Swapping A and B gives +14 / +20 km/s, which is ruled out.
  - This independently ties the eclipses to the RV primary's orbit and confirms that A is the companion passing in front of the primary.

5. PHYSICS
- f(M) = 0.1654 +- 0.005 Msun; a1 sin i = 17.99 Rsun; i = 89.0 deg from the light curve.
- For M1 = 1.1-1.5 Msun:
    m2      0.86-1.02 Msun
    a       41-45 Rsun
    R1      2.19-2.38 Rsun
    R2      0.96-1.04 Rsun
    logg1   3.80-3.86
- The TIC radius of 2.53 Rsun, de-blended by sqrt(1 + L2/L1) = sqrt(1.205), gives 2.30 Rsun, which matches. The picture is a G subgiant (about 1.3 Msun, 2.3 Rsun, 5800 K) with a roughly 1 Msun G dwarf of the same surface brightness (J = 1.07).
- Which star is in front:
  - At A (nu = 90 - w), the companion transits the primary. That gives the deeper, limb-darkened, rounded eclipse.
  - At B, the primary covers the companion completely. That gives the flat bottom, with depth = L2/(L1+L2) = 17.0%.
- Separations are 0.939a at A and 1.054a at B, so B should be longer by a factor of 1.12; 1.11 is observed. The b=0 durations from the TIC radius are 12.6-14.6 h; the observed ones are shorter, consistent with b of about 0.4 (in units of R1+R2).
- Depths, durations, the flat-bottomed B, the near-equal depths (J about 1) and the light ratio needed for an SB1 (a companion about 1.7 mag fainter) all fit one geometry.

6. NEXT ECLIPSES (BTJD; 1-sigma from the ephemeris is about 0.7 min, allow +-3 min)
- A (transit, 17.7%, T14 10.9 h): 4343.2567, 4364.9940, 4386.7312, 4408.4685
- B (total occultation, 17.1%, T14 12.1 h, flat): 4352.9553, 4374.6926, 4396.4299, 4418.1672
- General: T_A = 1691.30913 + 21.737275 E; T_B = 1701.00795 + 21.737274 E.

WHAT WOULD SETTLE IT FURTHER
1. ExoFOP (TOI/CTOI or notes), checked from a machine that can reach it.
2. Spectra at quadrature to detect the secondary's lines (expected K2 of about 50-60 km/s, L2/L1 about 0.2) and get absolute masses. With i = 89 deg, this is a well-detached G subgiant + G dwarf benchmark.
3. A proper EB model with fitted limb darkening, to tighten J and k and set the w difference from Gaia.
4. Report it as new: it is not in VSX or the TESS EB catalogues.
