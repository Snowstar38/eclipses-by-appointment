# TIC 65660608 (TYC 6528-895-1), adversarial check, 2026-10-17

**Verdict: CONFIRMED.** It is an eclipsing binary on the target:
- Three grazing eclipses with identical shapes, all on one exact linear ephemeris, P = 41.56002 d.
- The eclipses sit at the A conjunction of Gaia's SB2 orbit.
- The other kind of eclipse cannot occur at any stellar size, given Gaia's e and ω.

**Open problem:** with Gaia's K1 and K2, an eclipsing inclination makes the two stars 0.78 and 0.85 M☉. The colour (about 6100 K) says roughly 1.15 M☉ each. Gaia's K amplitudes would have to be about 14% low (about 3.5σ), possibly because a third star's light is mixed into the spectrum (RUWE 38). The catalogue checks below found no prior eclipsing-binary classification.

## Archives and web
- cats.py: ASAS-SN none; EB tables none; SIMBAD TYC 6528-895-1 [SB*]. VSX returned 503 there; through the VizieR cone it has nothing at the target. Within 120" VSX has only four faint Gaia variables, at 104–118" and G 14.0–17.7 (two EAs, a DSCT|GDOR, an RS).
- SB9, WDS, TESS-EB catalogue, Gaia vari_summary and vari_eclipsing_binary: none. ExoFOP: no TOI or CTOI, no spectra, no imaging.
- A web search on TYC 6528-895-1, TIC 65660608 and 2MASS J07134548-2606443 found nothing.
- Gaia DR3: RUWE 38.4, parallax 7.28 ± 0.56 mas (probably corrupted), bp_rp 0.71, GSP-Phot Teff 6136 K, logg 4.37.
- A Gaia source 3.1" away has no G magnitude: RP 15.68, parallax 0.01 mas, so it is a background star. To fake a 9% dip it would need a >100% dip, as would every neighbour within 90" (G 13.8–16).

## Eclipses (raw QLP SAP, q==0; fits_poly.json, graze_k1.0_J1.0.json)
| sector | mid (BTJD) | QLP depth (quadratic / cubic baseline) | own TESScut 5×5 depth | trapezoid T14 | T12 |
|---|---|---|---|---|---|
| s034 | 2230.72321 ± 0.0010 | 9.22 / 9.37% | 9.43 ± 0.07% | 4.18 h | 1.67 h |
| s061 | 2978.80354 ± 0.0010 | 9.09 / 9.02% | 9.30 ± 0.03% | 4.19 h | 1.68 h |
| s087 | 3685.32395 ± 0.0010 | 8.62 / 8.55% | 9.45 ± 0.02% | 4.17 h | 1.65 h |

- Shape: nearly V, flat part 0.84 h. Contact-to-contact length in the physical model is 4.5 h.
- Depth changes: in my own fixed-aperture TESScut photometry the depth is constant, 9.3–9.45% (3×3: 9.45/9.23/9.38%). So the QLP decline (the classifier's 10.1 → 8.3%) is QLP dilution or background, not a real change.
- It is not the detrending against the pulsation: quadratic and cubic baselines agree to 0.15%, and the mid-times agree to 3e-5 d.
- Durations are constant to about 1 min. A real inclination drift big enough for the QLP depth change would have shortened T14 by about 4 min.
- TESS-SPOC s061 shows the eclipse at 8.6% (SAP) and 8.9% (PDCSAP), crude in/out estimate.
- None of the three times is on a listed systematic, and all are in clean data away from gaps.
- Blind dip census: only these three. The next-strongest dips, 0.6–0.7%, are pulsation minima or momentum-dump gaps (zoom_census.png).

## Ephemeris (ephem.txt)
- T0 = 2230.72319, P = 41.56002 ± 0.00006 d. O−C is 0.0, 0.0, 0.0 min (cycles 0, 18, 35).
- The cycle count is unique: the other counts give 39.4 or 44.0 d, against Gaia's 41.69 ± 0.09. Because cycle 35 is odd, the true period cannot be 83.1 d.
- P − P_Gaia = −0.130 d, which is −1.43σ.
- Conjunction kind, with Gaia's T_peri, e and ω drawn and P fixed at 41.560:
  - A (ν = 90° − ω = 21°, 0.8 d after periastron) is predicted at 2231.18 ± 1.02; the observed eclipse is −0.45σ from it.
  - B is +15.3 d away, which is +4.3σ.
- So these are A eclipses: Gaia component 1 (K1 = 42.8 km/s, the lower-mass one) is behind, and component 2 is in front.

## Independence
- TESS-SPOC s061 light curve: covered above.
- Per-pixel eclipse fits on TESScut s034, s061 and s087: in all three the eclipse-amplitude map has the shape of the target's PSF, and its centroid is 2–5" from the light centroid (pix_s0*E.png).
- The 1.2–2 d variability is also on the target. Its pixel map follows the target PSF (amplitude/light 1.04 / 1.00 / 0.97 in 1×1/3×3/5×5 in s087; var_s0*.png), so it is not the VSX GDOR star at 118".

## Physics (graze.py; graze_k1.txt)
**Orbit.** The Gaia SB2 orbit (K1 = 42.8 ± 2.2, K2 = 39.2 ± 2.3 km/s, e = 0.471, ω = 68.9°) gives:
- M1 sin³i = 0.78 [0.66, 0.90] M☉ and M2 sin³i = 0.85 [0.73, 0.97] M☉; q = M2/M1 = 1.09.
- a sin i = 59.4 R☉. The separation is 32.1 R☉ at A and 82.4 R☉ at B (ratio 2.57).

**Grazing fit.** Two equal limb-darkened disks (k = 1, J = 1) fit each event with an impact of 0.69–0.70 of (R1 + R2). With Gaia's a sin i this gives R1 = R2 = 0.95 R☉ and i = 87.6°. An eclipse at A needs i > 86.6°. So a 4.5-h, 9% V-shaped graze fits two known-mass stars at this period.

**Mass tension.** At i ≈ 88° the masses are 0.78 and 0.85 M☉, which is too low for 6100 K stars. Stars of about 1.15 M☉ would need sin³i = 0.68 (i ≈ 61°), and then there could be no eclipse.

The consistent picture is Gaia's K1 + K2 being about 14% low. That would give masses of about 1.15/1.26 M☉ and radii of about 1.08 R☉, both plausible. A third star's light diluting the RVS lines (and the eclipses), suggested by RUWE 38, is the likely cause. It needs checking. It is not a reason to doubt the eclipse.

**The missing other-kind eclipse.** It is not shallow; it cannot happen, and the argument does not depend on the stars' sizes:
- b_B = b_A × r_B/r_A = 0.69 × 2.57 = 1.77 (in units of R1 + R2), which is greater than 1.
- A B eclipse would need r_B/r_A < 1.45, i.e. e sin ω < 0.18, against Gaia's 0.44 ± 0.045 (5.7σ).

The B windows are consistent with this. The data at 1508.35 (s007), 2962.95 (s061, sector start), 3669.47 (s087) and 3711.03 (s088), each ±1.65 d, show only the pulsation and momentum-dump gaps. The 2214.87 window (s033) straddles the orbit gap.

## Next eclipses (BTJD)
- A, ±4–5 min: 4142.484, 4184.044, 4225.604, 4267.164, 4308.724, 4350.284, 4391.844, 4433.404, 4474.964, 4516.524.
- B: no eclipse expected. The conjunctions are at A + 25.70 ± 1.65 d: 4168.19, 4209.75, 4251.31, 4292.87, 4334.43.

## What would settle it further
- High-resolution RV spectra, two epochs near quadrature, to re-measure K1 and K2. This resolves the mass tension and tests for a third set of lines (a tertiary, RUWE 38).
- A ground-based light curve of one A eclipse, for example at 4142.48 or 4184.04, to refine the impact parameter.
- Gaia DR4 epoch astrometry and RVs, which will show whether a tertiary drives the RUWE.
