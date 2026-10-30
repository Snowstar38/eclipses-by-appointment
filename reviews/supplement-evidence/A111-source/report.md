# TIC 20379300 (CD-28 8698, TYC 6661-930-1), adversarial check, 2026-10-17

**Verdict: CONFIRMED.** It is an eccentric eclipsing binary on the target: a K-type subgiant with an M-dwarf companion, P = 32.60569 d. Both kinds of eclipse are present and on target, and both follow one ephemeris. Separately, the timing and the durations give the same e and ω as the Gaia SB1 orbit, within 1σ. It is not in any catalogue I checked.

## Archives and web
- cats.py: ASAS-SN none; Prša+2022, IJspeert+2024 and Kostov+2025 t2/t3/t4 none; SIMBAD CD-28 8698 [SB*]. VSX returned 503 in cats.py, so I re-ran it through the VizieR cone (archive2.py; the query was checked on Algol): no VSX entry within 120". SB9, WDS and the TESS-EB catalogue (J/ApJS/258/16): none. Gaia DR3 vari_summary and vari_eclipsing_binary: none. ExoFOP: no TOI or CTOI, no spectroscopy, no imaging. A web search on the three names found nothing.
- Gaia DR3: RUWE 2.30, GSP-Phot Teff 5453 K, logg 4.0, R 2.28; FLAME R 2.39, M 1.30. No neighbour brighter than G 18.2 within 60". There is one G 11.92 star at 67.5". To fake the dips it would need a 19% dip (A) or a 2.3% dip (B).

## Eclipses (raw QLP SAP; trapezoid × quadratic baseline; fits_20379300.json)
| kind | sector | mid (BTJD) | depth | T14 | T12 | notes |
|---|---|---|---|---|---|---|
| A | s036 | 2291.9080 ± 0.0010 | 5.07% | 7.91 h | 1.62 h | every QLP cadence flagged; TESS-SPOC SAP/PDCSAP has it unflagged at 4.9/5.0%, TARS at 5.3% |
| A | s090 | 3759.1651 ± 0.0010 | 4.89% | 7.91 h | 1.63 h | TARS 5.1% |
| A | s100 | 4085.2209 ± 0.0010 | 4.32% | 7.91 h | 1.56 h | egress cadences flagged; q==0-only fit gives 4.41%, 7.85 h |
| B | s009 | 1553.6547 ± 0.0020 | 0.54% | 17.1 h | 2.8 h | 30-min cadence, sits on a baseline step; lower weight |
| B | s036 | 2303.5856 ± 0.0032 | 0.60% | 18.1 h | 3.5 h | TESS-SPOC 0.55%, TARS 0.67% |
| B | s063 | 3020.9093 ± 0.0021 | 0.62% | 17.7 h | 3.4 h | egress falls in a short gap |
| B | s090 | 3770.8426 ± 0.0014 | 0.62% | 17.8 h | 3.5 h | TARS 0.56% |
| B | s100 | 4096.8968 ± 0.0015 | 0.50% | 17.5 h | 3.2 h | |

- A dips are flat-bottomed with limb-darkening curvature. B dips are flat boxes about 11 h long, which means a total occultation.
- In s100 both kinds are 10–18% shallower. The A/B depth ratio stays at 7.9–8.8 in every sector, so the change is dilution and one source makes both.
- None of the times is on a listed sector-wide systematic, and none sits at a gap edge.
- Blind dip census (census.py): nothing else deeper than 0.2% except edge and steep-trend artefacts.
- Background is smooth through every event. The s090 A shows a −0.015 px shift in SAP_X/Y; the pixel-level map below shows the light is lost on the target.

## Ephemeris (ephem.txt)
- A alone: P = 32.60570 ± 0.00005 d. B alone: P = 32.60568 ± 0.00003 d.
- Joint fit: T_A = 3759.1644 ± 0.0012, T_B = 3770.8411 ± 0.0011, P = 32.60569 ± 0.00003 d. χ² = 1.4 for 5 dof; every O−C is under 2.5 min, including the flagged s036 primary (−0.7 min).
- P − P_Gaia = +0.0123 d, which is +0.93σ. Against the Gaia-predicted conjunctions, the A eclipses fall +0.95 to +1.63 d late (+1.1σ) and the B eclipses +0.3 to +1.2 d late (+0.3 to +0.7σ). Most of that drift is the period difference.
- Coverage: every predicted eclipse that falls inside the data is seen. The s009 A (1541.98) and the s063 A (3041.89) fall just outside their sectors.
- B − A separation = 11.677 d (phase 0.3581); Gaia's orbit predicts 12.07 ± 0.82 d.
- Duration ratio T14_B/T14_A = 2.25; Gaia's orbit implies 2.36 [2.10, 2.66].
- These give e sin ω ≈ 0.384 and e cos ω = −0.208, so e = 0.437 and ω = 118°. Gaia has e = 0.446 ± 0.053 and ω = 114.9 ± 3.8°: −0.6σ in e cos ω, −0.4σ in e sin ω. Gaia's orbit is not contradicted.

## Independence
- TESS-SPOC s036 (SAP and PDCSAP), TARS s036 and TARS s090 all show both kinds at the same depths (indep_20379300.png).
- Difference image, TESScut s090 15×15:
  - A, plain difference (diff_s090A.png): 4.8% at the target pixel; deficit centroid 2" from the light centroid; −0.3% at the G 11.9 neighbour's pixel.
  - The plain difference for B is dominated by a pointing-drift dipole, so I fitted each pixel separately (pixfit.py: quadratic + centroid-drift terms + a fixed-shape trapezoid).
  - Per-pixel result: A depth 4.45/4.82/4.61% and B depth 0.58/0.59/0.56% in 1×1/3×3/5×5 apertures. Both eclipse maps have the shape of the target's PSF (pix_s090A.png, pix_s090B.png). The neighbour's pixel shows +0.05% at B.

## Physics (physics.txt)
- Mass function f(m) = 0.0363 M☉. For M1 = 0.95 / 1.1 / 1.25 / 1.4 M☉ that gives m2 (i = 90°) = 0.41 / 0.44 / 0.48 / 0.51 M☉.
- Fitting the durations (T14A, T14B, T23B, with e and ω from the timing) gives R1/a = 0.039–0.041, i = 89.5–90°, b_A ≤ 0.11 and b_B ≤ 0.26.
- The solution consistent with the depths has k = 0.21 and i ≈ 89.6°. That gives R1 = 1.9–2.1 R☉ and R2 = 0.42–0.44 R☉, about what a 0.45 M☉ M dwarf should have, consistent with m2.
- Mild tension: Gaia's radius is 2.3–2.4 R☉. A star that large would need b_A ≈ 0.6 to keep the 7.9-h primary, and then there could be no B eclipse at all. So the eclipses prefer R1 ≈ 2.0 R☉.
- Which star is in front: A is at ν = 90° − ω, where the primary is farther from us, so the M dwarf transits the subgiant. This is near periastron, so it is the short event. B, near apastron, is the total occultation of the M dwarf.
- The B depth gives a TESS-band surface-brightness ratio J = 0.11, so T2 ≈ 3300–3500 K. Depths, durations and shapes all fit one geometry.

## Next eclipses (BTJD, ±2 min)
- A: 4150.433, 4183.038, 4215.644, 4248.250, 4280.855, 4313.461, 4346.067, 4378.672
- B: 4162.109, 4194.715, 4227.321, 4259.926, 4292.532, 4325.138, 4357.743, 4390.349

## What would settle it further
It is already settled as an EB. For masses and radii:
- RV follow-up to tie Gaia's γ, K1 and phase to the eclipse ephemeris. Here K1 = 24.7 km/s and ω should come out near 118°.
- A ground-based light curve of an A eclipse, in a bluer band, to get the limb-darkened k and b and resolve the R1 tension.
- Spectroscopy to look for the M dwarf in the IR, which would make it SB2.
