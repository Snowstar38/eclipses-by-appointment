# TIC 284613090 — PROBABLE

Bounded full physical review: **COMPLETE**. Review ID R694. Four deep same-kind eclipses repeat, with two consecutive sector 33 cycles. Deep opposite half-phase events are also measured; unequal depths support the full 23.1095-day photometric branch. The target-centered difference image has no capable Gaia neighbor, but Gaia SB2 period and conjunction differ materially at formal precision.

## Raw SAP and timing

The sealed SOURCE-SNAPSHOT.json identifies the Gaia source, screening branch, and exact QLP FITS receipts. `measure_raw.py` verified every QLP SHA-256 before extracting quality-zero raw SAP_FLUX. Individual event centers were free trapezoid fits, with realized depth `d × min(1,w/(2k))` recorded separately from fitted model amplitude. Representative raw panels are in `raw-events.png`. The screening predictions only located windows; they are not timing points. 4 identifiable same-kind centers give **P = 23.109521095 ± 0.000040511 d**, epoch **BTJD 1510.16157922 ± 0.00346708 d** for the selected repeating eclipse. This is not automatically the deeper primary. Median realized QLP depth is 251.99 ppt. Linear same-kind event fit, individual max(formal center covariance, half cadence), scatter-inflated covariance if reduced chi square > 1; excludes uncalibrated model/pipeline systematics. Reduced chi-square is 0.007; formal values are conditional on the chosen event family and timing model.

| Sector | Same-kind cycle | Measured midpoint BTJD | Conservative center error d | Realized depth ppt |
|---|---:|---:|---:|---:|
| 7 | 0 | 1510.16188272 | 0.010417 | 261.82 |
| 33 | 30 | 2203.44691040 | 0.003472 | 250.77 |
| 33 | 31 | 2226.55698932 | 0.003472 | 253.21 |
| 87 | 94 | 3682.45656348 | 0.001157 | 240.50 |

The independent `coverage_alias.py` samples clean main and opposite half-phase windows from the measured ephemeris. Main-window median core deficits and local robust scatter (ppt) are below. Missing or flagged windows are retained in `coverage-alias.json` and never treated as clean nulls.

| Sector | Cycle | Clean core samples | Core deficit ppt | OOT scatter ppt |
|---|---:|---:|---:|---:|
| 7 | 0 | 13 | 218.41 | 2.03 |
| 33 | 30 | 37 | 208.43 | 3.72 |
| 33 | 31 | 33 | 209.37 | 0.77 |
| 87 | 94 | 109 | 196.78 | 1.14 |

Clean opposite half-phase windows test the half-period alias. A near-zero deficit is evidence against equal-depth P/2 recurrence; the deep half-phase events for TIC 284613090 are an observed second eclipse kind, not same-kind recurrences.



| Sector | Cycle | Clean core samples | Core deficit ppt |
|---|---:|---:|---:|
| 7 | -1 | 12 | 216.98 |
| 87 | 93 | 112 | 198.58 |

## Pixel source and alternate reduction

The helper's independent background-subtracted TESScut difference extraction uses the **same TESS FFI photons** as QLP sector 33; it checks pipeline/aperture robustness, not a second observation. The positive deficit centroid is 0.097 pixel from the target in that sector, with 5×5 aperture depth 205.51 ppt. This offset is descriptive, not a calibrated localization likelihood; see `batch-shared/helper-pixels/284613090/difference.png` and the pixel JSON for the full image and apertures. The Gaia DR3 60-arcsec neighbor cone and optimistic G-band/full-throughput capability screen find:

| Capable Gaia source | Separation arcsec | G | Minimum intrinsic eclipse fraction proxy |
|---|---:|---:|---:|
| None | | | |

Capability uses the smaller QLP/TESScut representative loss as a conservative screen. A neighbor's required **intrinsic** eclipse loss cannot be equated to its **diluted pixel** loss. Color, aperture throughput, unresolved companions, and subpixel crowding limit attribution.

## Gaia orbit and physical interpretation

Gaia DR3 source 3141008470891945856 has a SB2 solution with P = 23.098407181 ± 0.001641237 d, eccentricity 0.06314, ω = 212.989°, and mass function 1.4372 M☉. The closest edge-on conjunction (A) differs from the measured eclipse epoch by +0.7883 d (+0.03413 phase); source-specific Gaia full-covariance linear timing uncertainty at that epoch is 0.1074 d. The photometric minus Gaia period is +0.011114 d. `gaia-geometry.json` retains both conjunctions, the correlation order, and the exact orbital inputs; `helper-geometry.json` is an independent calculation. Linear covariance is descriptive, not a sigma veto; an RV orbit or component assignment may need revisiting where mismatch is large. Median fitted eclipse duration is about 9.59 h, physically plausible for stellar-size eclipses in a 20–23 d orbit, but no fitted stellar radii or masses are claimed.

## Outcome and next observation

Physical outcome is **PROBABLE** after completed bounded review. Catalogue novelty is a separate shared-catalogue decision; a failed query is unknown, not a non-match. Limits: Four deep same-kind eclipses repeat, with two consecutive sector 33 cycles. Deep opposite half-phase events are also measured; unequal depths support the full 23.1095-day photometric branch. The target-centered difference image has no capable Gaia neighbor, but Gaia SB2 period and conjunction differ materially at formal precision. Next decisive check: New radial velocities and eclipse timing to reconcile the Gaia spectroscopic and photometric orbits.
