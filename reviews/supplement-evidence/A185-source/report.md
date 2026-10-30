TIC 427657329 (TYC 4478-554-1, Gaia DR3 2214685184515156224) - adversarial check

VERDICT: CONFIRMED. It is a detached, near-circular eclipsing binary on the target: a spotted G/K giant (TIC R 8.8 Rsun, Teff 5120 K)
with a hotter dwarf companion. The two eclipses are half an orbit apart. At B the giant totally occults the companion: flat-bottomed,
2.5% deep (QLP; PDCSAP 2.55-2.68%), 38.7 h long. At A the companion transits the giant: 1.3-1.6% deep, 39.3 h long. The "mid-eclipse
bump" is spot crossings. Structured residuals of 1.5-3 ppt appear only in the A (transit) bottoms, identically in QLP and TESS-SPOC.
The B (occultation) bottoms are as quiet as the out-of-eclipse light. The VSX "ROT P=53.5 d" (ASASSN-V J231724.84+682816.3,
amplitude 0.11 mag g) is the giant's spot modulation. The eclipses are new: this is a type revision to EA+ROT with P = 47.5288 d,
not prior art. Its only listing is Kostov+2025 table 2, the unvetted ML flag list.

1. ARCHIVES
- cats.py --r 60: VSX ROT P 53.5 d (0.5"). ASAS-SN catalogue: none. Kostov+2025 table 2 (does not count). SIMBAD lists it as SB* only.
  It is not in Prsa+2022 or IJspeert+2024.
- Gaia DR3: vari_summary and vari_eclipsing_binary return 0 rows. NSS gives SB1 with P 47.5479 +- 0.0091 d, e 0.018 +- 0.009,
  w 311 +- 24 deg, K1 28.4 km/s. RUWE 0.98.
- SB9 and WDS return 0 rows. ExoFOP (2026-10-20) has no TOI and no CTOI; it refused connections on 2026-10-21. A web search on the TYC,
  ASASSN-V, TIC and 2MASS names found nothing.
- SPOC DV (s56-69, s85): its TCEs are at 26.5, 11.7 and 9.0 d, detrending aliases. SPOC did not detect the eclipses at the true period.

2. ECLIPSES (raw QLP SAP, q==0, 10 sectors: s17/18/24/25/57/58/77/78/84/85)
The previous checker's receipts were re-verified. The shape-fixed rerun is identical, and a from-scratch free rerun reproduces every
event with two covered edges within 0.3 min. Model-free mirror timing agrees within 0.1-0.7 min for B and 4-10 min for A.
- B (7 events: s17, s18, s24, s25, s57, s58, s85; three with both edges): T14 38.7 h, T12 3.7 h, flat bottom 31 h (total). Depth
  2.44-2.58% in QLP; SPOC SAP 2.35-2.40%; PDCSAP (CROWDSAP 0.91) 2.55-2.68%.
- A (4 events: s24, s58, s77, s84): T14 39.3 h, T12 5.9 h, depth 1.1-1.6% in QLP. The s84 event is cut by a flagged stretch in QLP,
  and SPOC SAP recovers it at 3596.117 +- 0.003. Another A event (1790.0) falls in the s17/s18 gap.
- With flagged cadences included, B s17 (1766.261) and B s18 (1813.798) fit the ephemeris; the flagged s25 ingress is junk.
- Background and centroids (diag.txt): clean in the s57/58/85 events (dBKG within 3 ppt, centroid shift 2 mpix). A s58 sits at the
  sector start, where the background ramps (z 57); the same event is clean in SPOC.
- Census of 10 sectors (threshold 0.4%): nothing outside the two families, apart from a 0.5% wiggle at s17 1775.4.

3. EPHEMERIDES (myephem_loose.txt: events with at least one full edge; the strict two-edge fit gives the same P)
- B: P = 47.52876 +- 0.00004 d, T0 = 2574.2519 +- 0.0005 BTJD (7 events, rms 2.0 min).
- A: P = 47.52895 +- 0.00052 d, T0 = 2740.5971 +- 0.0069 BTJD (4 events, rms 17 min, 16 min spot jitter). A and B agree (+0.35 sigma).
- Joint P 47.52876 +- 0.00004 d. Gaia P 47.5479 +- 0.0091 d, so the difference is -2.1 sigma, a bit large but acceptable.
- Phase of B after A: 0.50012 +- 0.00014. Gaia predicts 0.5064 +- 0.0052 (-1.2 sigma). T14B/T14A 0.986; Gaia predicts 0.977 +- 0.016.
- Eclipses give e cos w = +0.0002 +- 0.0002 and |e sin w| <~ 0.01, i.e. essentially circular. Gaia gives +0.012 and -0.014
  (e 0.018 +- 0.009, so consistent with 0 at 2 sigma).
- Gaia conjunctions (sigma 4.5-4.6 d, because t_periastron is poorly defined at e~0): A is -0.35 to -0.98 d off and B -0.59 to -1.33 d,
  all within 0.3 sigma. The drift follows the 2.1-sigma P difference.

4. INDEPENDENCE
- TESS-SPOC FFI SAP gives the same times: B s57 +2.0 min, s58 +0.7, s85 -2.1; A s77 +1.5 min. A s84 is recovered (QLP partial).
- SPOC TPF pixels (s57/58/85 B, s77 A): the deficit peaks on the target pixel, with equal fractional depth in 1x1 and 3x3 apertures
  (2.5%). The deficit is more concentrated than the light: 77-82% of the deficit sits in the 3x3, against 59-64% of the light. In
  single-source PSF fits the target alone is favoured: chi2 304 vs >= 1716 (B s58), 433 vs >= 1757 (B s85), 846 vs >= 1874 (B s57),
  270 vs >= 894 (A s77).
- Neighbours within 60": the only one that could do it is G 13.74 at 43.2", which would need a 15% A dip and a 26% B dip. Its pixel
  shows only 0.7-1.0% (target PSF wing) against 2.5% on the target, so it is excluded. G 15.52 at 7.2" would need 79% and 136%,
  so it is impossible.

5. PHYSICS
- f(m) = 0.113 Msun. For M1 1.2-2.0, m2(i=90) = 0.76-1.0 Msun and a = 69-80 Rsun.
- Geometry: A is at nu = 90 - w, so the giant is behind and the companion transits it (spot crossings, slightly rounded edges). At B
  the giant is in front and the companion is totally occulted (flat). The orbit is circular, so the durations are equal (observed
  ratio 0.986).
- Durations: with TIC R1 8.8 and b=0, T14 would be 45-53 h, against 39 h observed. The B ingress (T12/T14 = 0.097) gives k ~ 0.107
  at b ~ 0, which needs R1 ~ 7.2-7.8 Rsun (15% below TIC). Alternatively b ~ 0.6, but that would lengthen the B ingress to ~5.8 h.
  The likeliest reading is a TIC radius about 15% too large; a modest discrepancy, not a refutation.
- Light: L2/L1 = 0.027 and k 0.106-0.117 give a companion of ~0.8-1.0 Rsun at ~6300-6700 K (blackbody estimate), which is a little
  hot for m2 0.8-1.0 Msun. The same mild tension appears in TIC 220461013, which suggests a systematic in the giant's TESS-band
  surface brightness from the crude blackbody.

6. NEXT ECLIPSES (BTJD)
- A (transit, 39.3 h): 4356.581, 4404.110, 4451.639, 4499.168 (formal +-0.47 h, realistic +-0.6 h).
- B (total occultation, 38.7 h): 4380.345, 4427.874, 4475.402, 4522.931 (formal +-0.04 h, realistic +-0.1 h).

WHAT WOULD SETTLE IT FURTHER: a physical light-curve model with limb darkening and spots (k, b, R1/a; it would test the TIC radius);
spectroscopy for SB2 lines and the companion's temperature; a VSX type revision to EA+ROT.
