TIC 74965330 (TYC 7686-1190-1, Gaia DR3 5427324157900849408): adversarial check
Checker: Opus 5.5, 2026-10-20/21. This run resumed after a usage-limit kill; earlier receipts were spot-checked and the measurements were made fresh.

VERDICT: CONFIRMED.
This is an eccentric (e ~ 0.34), detached, totally eclipsing binary at the Gaia SB1 period. Both conjunctions eclipse.
The A/B labelling agrees with the Gaia omega:
- Timing: both kinds land within 0.35 sigma of their predictions, and swapping the labels would put each eclipse about 11.5 d off.
- Durations: the T14 ratio has the sign and size that e sin w predicts.
B is deeper than A because the occulted companion, a ~1 Msun dwarf, has a higher TESS surface brightness than the cooler, larger RV star (R ~ 3.6 Rsun). That is physics, not a labelling error. Prior art is Kostov+2025 table2 only (an unvetted ML flag), so this is effectively new.

DECIDING NUMBERS

Measurements
- 6 eclipses measured from raw SAP_FLUX (trapezoid x quadratic baseline, prayer-bead errors).
    A x4 (the companion transits the RV star):
      s9  1545.7711 +- 2.1 min (missed by the classifier)
      s36 2290.5566 +- 1.1
      s62 2996.1396 +- 2.2
      s89 3740.9213 +- 1.4
      Depth 6.63-6.99%, T14 16.82-17.15 h, ingress 4.8-5.1 h, bottom 7.0-7.2 h.
    B x2 (the companion is occulted):
      s89 3729.4361 +- 1.2 min. Depth 10.41%, T14 18.99 h, ingress 5.20 h, flat bottom 8.60 h.
      s35 2279.0682 +- 2.5 min. The egress is on q=4096 stray-light cadences, so the shape was fixed to s89.
        Including the flagged egress and freeing the shape gives 2279.0695, and the depth there is 11.1%.
- The predicted B in s8 (1534.6) falls in the orbit gap.

Ephemeris
- A-only fit: P = 39.199084 +- 0.000036, O-C at most 2.9 min (chi2 3.5/2).
- B-only fit: P = 39.199131 +- 0.000052 (2 points).
- Joint fit: P = 39.199094 +- 0.000029 d, T0_A = BTJD 2643.34748 +- 0.00062, T0_B = BTJD 2671.06029 +- 0.00105 (chi2 4.1/3).
- Against the Gaia period: Gaia P 39.19755 +- 0.0105, a difference of +0.15 sigma.

A/B labelling against omega (the check that was asked for)
- Conjunctions: observed A lands +0.15 to +0.23 d from the Gaia A (within 0.25 sigma), and B lands -0.23/-0.29 d from the Gaia B (within 0.35 sigma).
- Separation: B precedes A by 11.486 d. Gaia predicts A->B 28.175 +- 0.558 d, observed 27.713 (-0.8 sigma).
- Duration ratio: T14_B/T14_A = 1.122 +- 0.010, giving e sin w = +0.058 +- 0.004 (Gaia +0.068 +- 0.024).
    The eclipse solution is e = 0.336, w = 10.2 deg (e cos w 0.331), against Gaia e 0.357 +- 0.024, w 11.0 +- 3.9 (-0.9 and -0.2 sigma).
- Geometry: with z = r sin(nu+w) sin i and RV = dz/dt, the RV star is behind at A (nu+w = 90) and in front at B.
    The flat bottom of B is a total occultation of the smaller companion by the larger RV star.
    B is longer because B is the slower conjunction (1 + e cos nu smaller), and that matches the e sin w > 0 that Gaia gives.
- If the labels were swapped (omega + 180), every eclipse would sit about 11.5 d from its prediction and the duration ratio would invert. Neither happens.

Physics
- f(M) = 0.177 Msun. m2(i=90) = 0.93 / 1.05 / 1.23 Msun for M1 = 1.2 / 1.5 / 2.0. a = 62-72 Rsun.
- Contact-duration geometry at both conjunctions, with e and w from the eclipses:
    Durations alone allow k = 0.27-0.44, R1/a = 0.044-0.056, i > 88 deg.
    The A depth (k^2 L1/Ltot x limb darkening = 0.068) narrows this to k = 0.25-0.28, giving:
      R1/a ~ 0.054, i ~ 88.2 deg, b_A ~ 0.47, b_B ~ 0.53
      R1 ~ 3.6 Rsun (TIC 3.47) and R2 ~ 0.96 Rsun
- Surface brightness: J = (L2/L1)/k^2 = 1.5-1.9 in the TESS band.
    That puts the companion about 0.6-1 kK hotter than the RV star, e.g. a ~5200 K subgiant plus a ~6100 K, ~1.05 Msun dwarf (TIC composite Teff 5588).
- The companion supplies ~11% of the light. A ~1 Msun dwarf beside a 3.6 Rsun subgiant/giant fits that.
- Depths, durations and shapes fit one geometry. The trapezoid underestimates the T23 of A (7.1 h vs a model 8.0 h), which is the expected limb-darkening bias.

Independence
- Same model, other pipelines:
    A s9: eleanor RAW/CORR -1.7/-0.9 min from QLP; TGLC aperture/PSF +1.8/+3.5 min.
    A s62: SPOC SAP/PDCSAP -2.6/-1.0 min.
    Depths range 4.2-7.8% with aperture dilution; the crowding-corrected PDCSAP gives 7.18%.
- Difference images: SPOC TPF s62 (A); TESScut s89 (A and B) and s35 (B).
    The brightest deficit pixel is the target pixel every time, and the deficit centroid sits 0.09-0.21 px (<= 4.4 arcsec) from the target.
    The target pixel shows A 6.1-6.4% and B 9.2-9.4%.
- Neighbours within 60 arcsec: four could in principle make the dips:
    G 12.17 at 29.2 arcsec (needs A 14% / B 22%)
    G 12.30 at 49.5 arcsec
    G 13.34 at 40.1 arcsec
    G 13.39 at 38.2 arcsec
  The difference images exclude all four. Their pixels show only 0.7-5.4%, the wings of the target, and the deficit centroid is more than 1 px from each.

Census
- Outside the predicted eclipses there is no dip deeper than 0.35% in any sector (1-h scatter 0.63-0.74 ppt).
- The s062 blips at 3006.9-3007.2 are the known s062 3007 common mode.
- Every predicted eclipse inside the data was seen.

PRIOR ART (queried 2026-10-20, spot-checked 2026-10-21)
- cats.py --r 60: VSX none, ASAS-SN none, Prsa+2022 none, IJspeert+2024 none.
    Kostov+2025 table2 (J/ApJS/279/50) lists TIC 74965330 at 0.001 arcsec. That is an unvetted ML flag list and does not count as catalogued; t3/t4 have nothing.
    SIMBAD lists TYC 7686-1190-1 as [SB*].
- Gaia DR3: vari_summary and vari_eclipsing_binary have no rows, and phot_variable_flag is NOT_AVAILABLE.
    NSS SB1: P 39.198, e 0.357, K1 37.7. RUWE 0.95, rv_amplitude_robust 64 km/s.
- SB9 and WDS: nothing.
- ExoFOP: no TOI or CTOI.
- Web search on TIC/TYC/2MASS names: no hits.
=> Effectively new. The first characterisation is here, including both eclipse kinds, the ephemeris and the orbit check.

EPHEMERIDES
A (companion transits the RV star): T0 = BTJD 2643.34748 +- 0.00062, P = 39.199094 +- 0.000029 d.
B (companion totally occulted): T0 = BTJD 2671.06029 +- 0.00105, same P. B precedes A by 11.486 d.

NEXT PREDICTED ECLIPSES (BTJD)
A: 4368.108, 4407.307, 4446.506, 4485.705, each +-0.0015 (about 2 min).
B: 4356.621, 4395.820, 4435.020, 4474.219, each +-0.0017 (about 2.4 min).
Duration ~17 h (A) and ~19 h (B), so a ground campaign needs long nights or several sites.

WHAT WOULD SETTLE IT FURTHER
1. A spectrum (SB2 cross-correlation) would confirm a hotter ~6000 K dwarf beside a cooler subgiant, and with the Gaia K1 it would give K2 and absolute masses.
2. A full eclipse model with limb darkening would pin k, b and J. Even now, the flat bottom of the B occultation directly measures L2/Ltot = 0.104-0.111.
3. A second B with full coverage would firm up the B period on its own; the s35 egress is on flagged cadences.

FILES (in vet74965330\; downloads in C:\Home\sky\data\qlp-sb-p20-60\vet74965330\)
- Fits: fits_74965330*.json, fits_use.json, fit_*.png
- Ephemeris, physics, census: ephem.txt, physics.txt, census.txt
- Independence and difference images: indep.txt, diff.txt, diff_*.png
- Neighbours and archive queries: neighbours.txt, archives.txt, arch2.txt, cats.txt
