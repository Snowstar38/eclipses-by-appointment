TIC 220461013 (UCAC2 5492112, Gaia DR3 4762087153135575040) - adversarial check

VERDICT: CONFIRMED. It is a detached, eccentric eclipsing binary on the target: a spotted K giant (TIC R 6.84 Rsun, Teff 4550 K)
with a G-dwarf companion. Each conjunction gives a different kind of eclipse. At A the companion transits the giant: rounded,
1.5-2.0% deep, 31.7 h long, with spot-crossing bumps. At B the giant totally occults the companion: flat-bottomed, 3.8-3.9% deep
(crowding-corrected), 53.4 h long. Both repeat across 42 TESS sectors (2018-2025). The VSX/ASAS-SN classification "ROT P=54.57 d"
describes the giant's spot modulation correctly, but the eclipses are missing from it. The type should be revised to EA+ROT
(or EA/RS), with P = 50.8532 d. That is a type revision, not prior art.

1. ARCHIVES (queried 2026-10-20/21)
- cats.py --r 60: VSX ASASSN-V J045855.35-594135.5 (0.1"), type ROT, P 54.57 d, amplitude 0.22 mag (g). ASAS-SN gives ROT with P 55.8 d.
  SIMBAD lists it as SB* only. It is not in Prsa+2022, IJspeert+2024, or Kostov+2025 tables 2/3/4.
- Gaia DR3: vari_summary and vari_eclipsing_binary return 0 rows. NSS gives SB1 with P 50.8547 +- 0.0163 d, e 0.301 +- 0.011,
  w 121.7 +- 3.1 deg, K1 34.0 km/s. RUWE 1.03.
- VizieR SB9 (30") and WDS (30") return 0 rows. ExoFOP (2026-10-20 run) has no TOI and no CTOI; it refused connections on 2026-10-21.
- Web search on the TIC number, the ASASSN-V name, UCAC2 and 2MASS found nothing about this star.
- MAST: the TESS-SPOC multi-sector DV report for s56-s69 contains TCE_4: P 50.8545 d, T0 2995.354, 16.9k ppm, 13.8 h, MES 7.9
  (dvt_tces.txt). This is SPOC's automated pickup of the A eclipses (TCEs 1-3 are aliases). It was never made a TOI, and an automated
  TCE is not a catalogue classification. It is worth citing as an independent detection.

2. ECLIPSES (raw QLP SAP_FLUX, QUALITY==0, no trimming)
The previous checker's fits were re-verified. A shape-fixed rerun gave identical numbers. A from-scratch free rerun reproduced every
two-edge event to within 0.1 min. A separate model-free mirror-symmetry timing (mirror.py) agrees within 0.5-4 min for B and 1-9 min
for clean A events (33 min for A s98, which has a spot bump).
- A (19 events, 12 with both edges): T14 31.7 h, T12 4.7 h, QLP depth 1.2-2.3% (median 1.7%). The bottom is rounded, with ~0.5%
  bumps inside the eclipse: spot crossings on the giant.
- B (23 events, 10 with both edges): T14 53.4 h, T12 5.3 h, flat bottom 42.8 h (total). QLP depth 3.1-4.4% (median 3.8%; 3.1-3.3%
  in s94-98, consistent with aperture/dilution differences).
- Flagged cadences do not contradict anything: B s29 (2099.030) and B s97 (3980.604) fit; the flagged data in s68/s98 are junk.
- Background and centroids (diag.txt): in clean events dBKG is within +-10 ppt of the star's flux (z<3), and the centroid shift is
  0-2 mpix. Excursions occur only in scattered-light sectors, where the eclipse shape is unchanged.
- Excluded events: B+31 s87 3675.5 (on the s087 ~3676 downturn, egress in the gap) and B+21 s68 (flagged).
- Census of all 42 sectors (threshold 0.4%): nothing >= 0.9% deep outside the two eclipse families.

3. EPHEMERIDES (myephem.txt)
- B: P = 50.85313 +- 0.00006 d, T0 = 2760.1247 +- 0.0011 BTJD (10 events, rms 4.9 min).
- A: P = 50.85407 +- 0.00030 d, T0 = 2791.5637 +- 0.0049 BTJD (12 events, rms 22.7 min, 20.6 min spot jitter). The A/B periods
  differ at 3.0 sigma, most likely from spot-distorted A timings.
- Joint P 50.85317 +- 0.00006 d. Gaia P 50.85471 +- 0.01629 d, so the difference is -0.09 sigma.
- Phase of B after A: 0.38177 +- 0.00010. Gaia predicts 0.3965 +- 0.0096 (-1.5 sigma). T14B/T14A is 1.684; Gaia predicts 1.686 +- 0.045.
- Eclipses give e cos w = -0.1807 and e sin w ~ +0.255 (e ~ 0.31, w ~ 125). Gaia gives -0.158 +- 0.015 and +0.256.
- Against Gaia's conjunctions: A is +0.13 to +0.21 d late (+0.1 to +0.3 sigma); B is -0.54 to -0.61 d early (-0.4 to -0.6 sigma).

4. INDEPENDENCE
- TESS-SPOC SAP gives the same mid-times as QLP: A s62 -2.4 min, s64 +7.5, s69 +6.4; B s64 +0.7, s66 +1.0 min. PDCSAP B depth is
  3.86-3.92% (CROWDSAP 0.92).
- SPOC TPF pixels: the deficit peaks on the target pixel, with equal depth in 1x1, 3x3 and 5x5 apertures. In single-source PSF fits
  the target alone is favoured over the best neighbour: chi2 188 vs 1536 (B s64), 1716 vs 4415 (B s66), 60 vs 459 (A s64),
  30 vs 434 (A s62), 336 vs 393 (A s69).
- Neighbours: G 14.61 at 10.7" would need a 33% A dip and a 74% B dip; G 14.89 at 26.2" would need 43% and 95%; all others more
  than 100%. Both are rejected by the pixels and by the Gaia orbit tie.

5. PHYSICS (physics.txt)
- f(m) = 0.179 Msun. For M1 = 1.0-1.2, m2 = 0.85-0.94 Msun and a = 71-74 Rsun. Predicted b=0 T14 is A 31-32 h (observed 31.7) and
  B 52-54 h (observed 53.4).
- At A the giant is behind and the companion transits it (rounded, spot bumps). At B the giant is in front and the companion is
  totally occulted (flat).
- L2/L1 = 0.041 and k = 0.11-0.13 give a companion of ~0.75-0.87 Rsun at ~5900-6450 K: a G dwarf.

6. NEXT ECLIPSES (BTJD)
- A: 4368.040, 4418.894, 4469.748, 4520.602 (formal +-0.26 h, realistic +-0.5 h).
- B: 4336.572, 4387.425, 4438.278, 4489.131 (formal +-0.06 h, realistic +-0.15 h).

WHAT WOULD SETTLE IT FURTHER: a limb-darkened, spot-aware model fit (k, b, T2); spectroscopy for SB2 lines; more A timings to settle
the A/B period difference; a VSX type revision to EA+ROT.
