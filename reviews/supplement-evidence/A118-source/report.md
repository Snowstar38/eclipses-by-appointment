# TIC 64696335 (TYC 6536-1088-1): adversarial check

Opus 5.5, 2026-10-18, 20:15 makeup session. The Oct 17 subagent that started
this left scripts, plots, MAST downloads and its own TESScut photometry
(`s8_cut.py` → `phot_*.npz`, including **s108 and s109**), but no results.
I used its photometry and downloads and wrote my own analysis in `o55\`.

## Verdict: CONFIRMED

This is a detached, circular EB: a red-clump giant (~2.1 M☉, ~8.7 R☉, 5150 K)
with a K7-ish dwarf companion (~0.64 R☉, ~4200 K) on Gaia's SB1 orbit, at a
slightly longer period. It is new. The deciding facts:

- **Seven events on one linear ephemeris over 7.7 years**, both kinds, at
  phase 0.4993. The four clean events fit with χ² 1.0/1 (with a 29-min floor
  for the giant's red noise), and every O−C is ≤ 0.52 h.
  The ephemeris then predicts the three events I hadn't used. It gets s87 B
  to +1.1 h and s88 A to −1.5 h. **s108 B, out of sample, comes in at +0.3 h.**
  s108 was in neither QLP nor the search; that event is only a 2σ fit, so it
  supports the result rather than carrying it.
- **Difference images (s34 A, s33 B, s61 B) put the deficit on the target**,
  with the deficit centroid 4.1″, 0.9″ and 1.4″ from the light centroid. For
  each neighbour, the deficit fits the target's own image better than the same
  PSF moved to the neighbour, by Δχ² 4099 / 4264 / 5016 (s34), 595 / 531 / 669
  (s33) and 916 / 1174 / 1169 (s61). The neighbours are the G 14.41 at 32.6″,
  the G 15.65 at 28.0″ (RUWE 4.8) and the G 16.10 at 42.9″. A neighbour would
  have needed a 13% / 40% / 61% A eclipse. The s87 difference image is
  dominated by scattered light and is not used.
- **Second pipelines.** For s7 B, eleanor-lite RAW/CORR/PCA give 2960 / 2166 /
  2825 ppm, and TGLC aperture 3391 ppm. **TGLC PSF gives only 415 ± 398 ppm**,
  the one dissent; with nothing brighter than G 16.8 within 27″ in Gaia, I read
  it as a PSF-fit failure on a 30-min sector, not a host problem. For s61 B,
  TESS-SPOC SAP and PDCSAP give 2663 and 3748 ppm (6.8σ and 4.4σ against the
  same fit at 169 random off-conjunction centres in that sector). The errors
  come from fake-centre scatter, which carries the red noise.
- **The giant doesn't make these dips on its own.** A blind census of all six
  QLP sectors (`s5_census.py`, boxes 2–26 h, 3-d running median) finds long
  dips deeper than 1500 ppm only at the conjunction times (s7, s33, s34). The
  other candidates are 2-h boxes, sector edges, or the s88 background spike. A
  common-mode test of 26-h boxes on 246–333 other stars per sector is clean at
  each event: median −21 to −150 ppm, against the target's +2000 to +5200 ppm.

## Measurements (own r = 2.5 px TESScut, quadratic baseline, trapezoid)

| kind | sector | t0 (BTJD) | depth ppm | T14 h | note |
|---|---|---|---|---|---|
| B | 7 | 1506.031 ± 0.008 | 2450 ± 82 | 28.2 | clean |
| B | 33 | 2217.770 ± 0.015 | 2493 ± 144 | 31.0 | clean |
| A | 34 | 2238.650 ± 0.005 | 5617 ± 74 | 32.5 | clean, T23 18 h |
| B | 61 | 2971.315 ± 0.008 | 2463 ± 74 | 28.3 | clean |
| B | 87 | 3683.078 ± 0.018 | 2288 ± 248 | 29.2 | scattered light, 85% coverage |
| A | 88 | 3703.869 ± 0.025 | 7028 ± 522 | 33.3 | at a gap and background spike |
| B | 108 | 4311.022 ± 0.141 | 1426 ± 663 | 26.4 | out of sample, weak |

These errors are residual-permutation errors and understate the red noise; the
fake-centre nulls above are the honest ones.

**Ephemeris (`o55\ephem.py`):** P = **41.86524 ± 0.00087 d**,
T_A = 2238.650 ± 0.021, T_B = 2217.748 ± 0.013 BTJD. Gaia's P is
41.84054 ± 0.0130, which puts ours +1.9σ (+35.6 min per orbit). The Gaia A
conjunction at cycle 43 is predicted at 2237.70 ± 6.5, and the measured A is
+0.15σ from it. The A−B phase of 0.4993 gives e cos ω ≈ −0.001, and the equal
durations give e sin ω ≈ 0. Both match Gaia's e = 0.021 ± 0.012.

## Physics (`o55\`, by hand; not a light-curve fit)

f(M) = 0.0322 M☉ (K1 19.50 km/s). The A event is the transit of the giant by
the companion (Gaia's A conjunction, deeper eclipse). The B event is the
companion's occultation, so its depth (0.24%) is the companion's light share.
That gives k ≈ 0.074 and surface-brightness ratio J ≈ 0.44, so
T2 ≈ 4200 K and R2 ≈ 0.64 R☉ for R1 = 8.7 R☉ (TIC): a K7 dwarf. With
m2 ≈ 0.63 M☉, f(M) gives M1 ≈ 2.1 M☉ and a ≈ 70 R☉. The 32-h T14 then
requires b ≈ 0.72 (i ≈ 85°) and predicts a ~5-h ingress. The A fit's 7 h is
about right for a limb-darkened transit; the B fits are too noisy to say.
L1 ≈ 48 L☉ is a red-clump giant, consistent with M_G ≈ 0.9 − A_G at
Gaia's 1.05 kpc. These numbers agree with each other, but none of them is
fitted jointly. A
proper two-sphere fit is the next step if the paper wants radii.

## Archives

None of these list the eclipses:

- VSX (VizieR B/vsx, 120″): the only entry is Gaia DR3 5609478320825593984,
  type E, P 0.235 d, G ~19 at 92″, which can't make 29-h dips.
- ExoFOP TOI and CTOI lists: none.
- ASAS-SN: none. SIMBAD: SB* only.
- Gaia DR3 vari / EB: none. SB9, WDS, Hipparcos: none.
- Zenodo: zero hits on either name. Web search: nothing on either name.

## Next eclipses (BTJD, ±0.05 d; each lasts ~32 h)

- A (transit, 0.56%): 4331.912 (observed at 4331.901, see below),
  4373.777, 4415.643, 4457.508
- B (occultation, 0.24%): 4352.876, 4394.741, 4436.606, 4478.472

## The out-of-sample A transit (Opus 5.5, 2026-10-22 18:30)

The s109 TESScut was re-released by Oct 22 18:30 EDT, ending at **4331.69**:
the predicted ingress (~4331.24) and about 11 h of the transit, no egress yet.
The first-orbit-only files were kept as `*.first-orbit.*` in the data folder,
and `s8_cut.py 109` was re-run.

- **Own-background photometry shows the ingress on time** (`o55\s109_orbit2.png`).
  In 2-h bins, flux is flat to −0.22% through 4331.18, then −0.37% at 4331.27,
  −0.69% at 4331.35, and −0.89 to −0.99% from 4331.43 on. The pre-ingress
  trend is included in those numbers.
- **Fit** (`o55\s109_fit.py`; s34 shape fixed at T14 32.5 h and T23 18 h; free
  tc, depth and quadratic baseline): **tc 4331.901 ± 0.009**, depth
  **6685 ± 212 ppm** (s34 5617, s88 7028). O−C = **−15 min, −0.2σ** against
  the ±0.05 prediction. The tc comes from ingress alone with the shape held
  fixed, so its ±12 min understates the real uncertainty.
- **On target, not common-mode** (`o55\s109_neigh.py`): the step is −0.83%,
  −0.84% and −0.80% in r = 1.5, 2.5 and 3.5 px. The bright neighbour's
  aperture sums change by −0.08%, −0.05% and +0.01%. A small pointing shift at
  the same time moves single off-target pixels by ±1% with opposite signs
  across rows (`o55\s109_common.py`), but it conserves flux in an aperture.
  The own background is flat across the window.
- **Null** (`o55\s109_ingress.py`): the same baseline-extrapolation statistic
  at 549 fake centres in s108 and s109 has std 1003 ppm. None reaches the
  observed 4188 ppm.
- **SPOC FLUX_BKG is ~0 in this release.** `spoc_*` columns carry the
  first-orbit scattered-light hump; use only `own_*` for s109.

So the ephemeris built from the four clean events (s7, s33, s34, s61; the last
at 2971.3) predicted a transit 1360 d (32.5 orbits) past the last event it
used. The transit came on time and at a depth within the range of the earlier
ones. When the rest of s109's second
orbit is released (it runs to about 4345), re-run `s8_cut.py 109` (move the
cached cut first) and refit with the egress included.
