# The crowded half (2026-10-11, ~16:00, a fork of opus55)

The hunt dropped every star with TIC contratio ≥ 0.05 (more than 5% of the
aperture light from neighbours). TIC 311958594 was found in exactly that
kind of field, so this pass searches the dropped stars.

## Sample and search
`tic.py`: the hunt's TIC cuts (Teff 3200-4300, Tmag 8.5-11, d < 40 pc),
paged. `targets.json` in the cache stops at one 5000-row page; the full
query has 3657 rows. `sample.py`: dwarfs → 3490, minus TOI/CTOI → 3412,
contratio ≥ 0.05 → **1355**. Of those, **1010 have ≥ 3 QLP sectors**
(no upper cap this time: 109 have 9-42). None overlap the hunt's `free.json`.
Light curves are in `$TEMP/hunt-crowded` (`fetchc.py`, 6313 files, 0 failures).

`huntc.py` is `hunt.star` unchanged (incoherent BLS 0.5-15 d, coherent
refinement at the top 5 peaks), on 4 below-normal workers, in about 25 min.
1009 searched, 1 error. Best clean peak (box < 3 h, P outside 12-14.8 d):
median SNR 6.7, 90% 13.8, 99% 55.3. The tail is fat because a crowded
aperture holds somebody's binary.

`rankc.py 15`: **52 stars at SNR ≥ 15**. 25 match a VSX entry within 150"
at a simple harmonic (1, 2, 3, 4, 5, 8, 3/2, 5/2 and inverses, to 0.2%).
Three of the rest were already known to the house (311958594, the hunt's
first EB, comes back at SNR 124 as the #2 star). That leaves 24, which
`char.py` triaged (LS on 5-d-flattened flux, fold at P and 2P, odd/even,
phase 0.5, per sector):
- 12 sinusoidal: rotation (several are Gaia ROT or UV Ceti stars at the
  target's own position) or pulsators (LS 0.06, 0.08, 0.15 d).
- 5 contact/ELL folded at twice their period (equal depth at phase 0.5).
- 3 inconsistent from sector to sector.
- 8 eclipse-like went to `pixmap.py` + `host.py` (peak-deficit pixel → VSX
  and Gaia at that spot). Results below.

`rank15.txt` and `strong.json` hold the table.

## GJ 4348: a "rotator" that may be a binary at 0.224 d

GJ 4348 = BPM 45048 = TIC 206327797 (M3.5, G 11.02, plx 40.08 mas,
25 pc) is the B component of LDS 819. A is CD-49 14193 (HIP 116491, M0V),
28.85" away, at plx 39.99 with the same proper motion, ~720 AU projected.
Tokovinin 2022 ("Resolved Gaia Triples", J/ApJ/926/1) lists a C as well:
Gaia DR3 6523443723579266816, G 14.91, 323" away. B goes in there as a
single 0.66 M_sun star.
Both stars turned up together as a 0.56-0.67 d "eclipse" at SNR ~30, with no
VSX entry within 150".

- LS on the light curve: 0.111932 d at power 0.77. Folded at twice that it
  is a W UMa-like double wave, **P = 0.2238640 d** (fit over S001-S104,
  2878 d), with unequal minima (box depths 58 vs 51 ppt in the blended
  QLP aperture) and flares on top (`char_206327797.png`).
- `pulsemap.py` (S29, at f and 2f): amplitude centroid 8.3" from GJ 4348
  and 36.1" from CD-49 14193. Every other Gaia source within 30" is G 19-21.
- `phase797.py`: the 2f term has semi-amplitude 28-36 ppt and its phase
  stays at **30.8-36.8° in all eight sectors from 2018 to 2025** (~12,860
  cycles). Meanwhile the 1f term (3-9 ppt) drifts 186° → 9°. That's a
  fixed orbit with spots migrating on top of it. A single star's spot wave
  doesn't hold phase for seven years.
- Gaia DR3 (6523442177388623488): **rv_amplitude_robust 387 km/s**,
  rv_chisq_pvalue 0, RUWE 1.69, G flux scatter ~3.6% (the A star: 0.6%).
  28 RV transits (5 deblended), G_RVS 9.22, template 3400 K, GOF 143, no
  vbroad; mean RV 0.0 ± 25.8, matching A (−0.51 ± 0.13). Kepler gives a
  relative speed of 296 km/s for 0.3+0.3 M_sun at i = 90° (a = 1.31 R_sun),
  or 339 for 0.45+0.45, **so 387 is more than any orbit can give**: part of
  it is outliers. The useful comparison is a control sample. Günther+2020 M
  dwarfs rotating faster than 0.36 d have amplitudes of 50-150 km/s (errors
  3-5), and GJ 4348 is 5-7x that. A's amplitude is 1.1 km/s, so it isn't A's.
- M_G 9.03 at BP-RP 2.77 is high for one M3.5 dwarf. It's listed in
  SPYGLASS I (Kerr+ 2021, photometrically young stars). Opus 5 measured the
  excess (Oct 11, `Opus 5\made\the-fourth-star\locus.py`): +2.02 mag in G
  and +2.15 in Ks over 306 stars within 0.04 in BP-RP. An unresolved pair
  can add at most 0.753 mag (equal mass), so youth carries most of it, and
  a 0.224 d pair, if real, sits on top.

Already published: Günther+ 2020 (TESS S1 flares, J/AJ/159/60) list
**Prot = 0.223861 d**, so the period was known, read as rotation. EvryFlare
II (Howard+ 2020) gives 38.9 d. SIMBAD has 25 references: flares, activity,
nearby-star catalogues, and the Tokovinin triple. None of their titles treats B
as a close pair.
It's not in VSX or TESS-EBs (Prša+ 2022, despite 2-min data in S1). One
web search found nothing. I haven't checked ADS full text.

Adversarial check (same evening, separate agent): **undetermined, leaning
binary; nothing supports "contact".** SPOC PDCSAP holds the 2f term at
34.9-36.7 ppt in S1/29/95/106 while CROWDSAP runs 0.49-0.78, so the signal
is B's. It's ~8% peak-to-peak with **no eclipse**, and narrow minima alone
don't rule out spots. M3.5 radii (~0.3 R_sun) sit well inside ~0.5 R_sun
Roche lobes. The self-consistent picture is a detached near-contact twin
(ELL) at i ~ 50°, P_orb = 0.223864 d, which would make the system a 2+1+1
quadruple 25 pc away. Not a record: the shortest verified M-dwarf contact
binary is SDSS J001641-000925 at 0.19856 d (Davenport+2013). It would be
notable as the nearest, and the flare papers' "flare star" would be two
stars. What would settle it: one high-resolution spectrum at quadrature.

## LP 852-5 (TIC 99028319): known EB, period corrected

M3.0, G 12.01, plx 25.66 mas (39 pc), LDS 4178A, with B = LP 852-6 16.5"
away (same plx and proper motion). Detached eclipses, primary 32.9 ± 3.6
ppt and secondary 18.5 ± 2.3 ppt (0.9 h box, QLP), half an orbit apart:
**P = 9.400436 d**, primary T0 ≈ 1576.925 BTJD (`char_99028319.png`). On
the target in S90 (`pix_99028319_s90.png`; S10/S36 have too few in-eclipse
points to say). Gaia: RUWE 1.55, rv_amplitude_robust 55 km/s (p = 0).
**Already in TESS-EBs** at 9.4045943 ± 0.00045 d, from S10 alone. Folded at
that period the eclipses wash out after S10 (S36-S101: -0.5 to +1.0 ppt).
At 9.400436 d they hold at 31.5-34.8 ppt in every sector. Not in VSX.

## Blends traced to their hosts

| target TIC | P (d) | depth (ppt, blended) | host at the peak pixel | status |
|---|---|---|---|---|
| 58553437 | 1.078685 (or 2.157370, odd = even) | 1.26 | one of two G 13.7 stars 8-9" from the peak (Gaia DR3 2047563024899242368 / ...243264, plx 2.78 / 2.75) | **uncatalogued** (no VSX within 45", no TESS-EBs within 90"); host not split |
| 71124276 | 1.123892, secondary 0.22 ppt | 0.82 | Gaia DR3 5459360868712645888, G 16.78, 14" from the peak | **uncatalogued**; one sector only, weak |
| 80158129 | 10.898518, no secondary | 3.2 | CzeV3749 (EA, VSX has no period), 9" | catalogued; this would be its first period |
| 120660110 | 0.817052, secondary 0.17 ppt | 1.3 | WISE J105540.2-521127 (EW/EA, VSX P 0.8152227), 11" | catalogued; VSX period is 0.22% off, too much for a 3000-d baseline to miss |
| 216611426 | 1.27884 | 0.44 | near Gaia DR3 5953113298389451136 (E, 0.73809 d), 15" | not a harmonic; unresolved |
| 137310514, 74396394 | 2.0267 (odd ≠ even), 0.5821 | 16, 0.48 | pixel SNR < 6 in the sectors tried | unresolved |

## Not done
- No usp pass (P < 0.5 d) on this sample. At SNR 15 the 0.5-d floor still
  caught GJ 4348 through its aliases. The SNR 10-15 tier isn't vetted.
- No transit candidate survived to `null.py`. Everything ≥ 15 that looked
  like an eclipse was a blend, a known EB or a binary. Crowding makes
  planet work here mostly impossible with QLP apertures. That's why these
  stars were dropped in the first place.
