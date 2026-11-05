# TIC 56912737 — CONFIRMED

Bounded full physical review: **COMPLETE**. Review ID R697. Three compact dips in sectors 21 and 47 give two adjacent sector 47 cycles; measuring the individual centers resolves the apparent phase displacement of the earlier sector 47 window. Timing agrees with the Gaia period within stated errors and the deficit is target-centered.

## Raw SAP and timing

The sealed SOURCE-SNAPSHOT.json identifies the Gaia source, screening branch, and exact QLP FITS receipts. `measure_raw.py` verified every QLP SHA-256 before extracting quality-zero raw SAP_FLUX. Individual event centers were free trapezoid fits, with realized depth `d × min(1,w/(2k))` recorded separately from fitted model amplitude. Representative raw panels are in `raw-events.png`. The screening predictions only located windows; they are not timing points. 3 identifiable same-kind centers give **P = 20.682911296 ± 0.000309586 d**, epoch **BTJD 1877.64999670 ± 0.01039693 d** for the selected repeating eclipse. This is not automatically the deeper primary. Median realized QLP depth is 6.88 ppt. Linear same-kind event fit, individual max(formal center covariance, half cadence), scatter-inflated covariance if reduced chi square > 1; excludes uncalibrated model/pipeline systematics. Reduced chi-square is 0.040; formal values are conditional on the chosen event family and timing model.

| Sector | Same-kind cycle | Measured midpoint BTJD | Conservative center error d | Realized depth ppt |
|---|---:|---:|---:|---:|
| 21 | 0 | 1877.64986911 | 0.010417 | 8.01 |
| 47 | 34 | 2580.86947700 | 0.003472 | 6.87 |
| 47 | 35 | 2601.55141000 | 0.003472 | 6.88 |

The independent `coverage_alias.py` samples clean main and opposite half-phase windows from the measured ephemeris. Main-window median core deficits and local robust scatter (ppt) are below. Missing or flagged windows are retained in `coverage-alias.json` and never treated as clean nulls.

| Sector | Cycle | Clean core samples | Core deficit ppt | OOT scatter ppt |
|---|---:|---:|---:|---:|
| 21 | 0 | 6 | 6.52 | 0.33 |
| 47 | 34 | 15 | 5.29 | 0.61 |
| 47 | 35 | 17 | 6.06 | 0.35 |

Clean opposite half-phase windows test the half-period alias. A near-zero deficit is evidence against equal-depth P/2 recurrence; the deep half-phase events for TIC 284613090 are an observed second eclipse kind, not same-kind recurrences.



| Sector | Cycle | Clean core samples | Core deficit ppt |
|---|---:|---:|---:|
| 21 | 0 | 6 | 0.01 |
| 47 | 34 | 17 | 0.22 |

## Pixel source and alternate reduction

The helper's independent background-subtracted TESScut difference extraction uses the **same TESS FFI photons** as QLP sector 21; it checks pipeline/aperture robustness, not a second observation. The positive deficit centroid is 0.131 pixel from the target in that sector, with 5×5 aperture depth 7.16 ppt. This offset is descriptive, not a calibrated localization likelihood; see `batch-shared/helper-pixels/56912737/difference.png` and the pixel JSON for the full image and apertures. The Gaia DR3 60-arcsec neighbor cone and optimistic G-band/full-throughput capability screen find:

| Capable Gaia source | Separation arcsec | G | Minimum intrinsic eclipse fraction proxy |
|---|---:|---:|---:|
| None | | | |

Capability uses the smaller QLP/TESScut representative loss as a conservative screen. A neighbor's required **intrinsic** eclipse loss cannot be equated to its **diluted pixel** loss. Color, aperture throughput, unresolved companions, and subpixel crowding limit attribution.

## Gaia orbit and physical interpretation

Gaia DR3 source 1011698964121167104 has a SB1 solution with P = 20.683790633 ± 0.001622228 d, eccentricity 0.42982, ω = 195.181°, and mass function 0.04257 M☉. The closest edge-on conjunction (B) differs from the measured eclipse epoch by -0.3352 d (-0.01621 phase); source-specific Gaia full-covariance linear timing uncertainty at that epoch is 0.2342 d. The photometric minus Gaia period is -0.000879 d. `gaia-geometry.json` retains both conjunctions, the correlation order, and the exact orbital inputs; `helper-geometry.json` is an independent calculation. Linear covariance is descriptive, not a sigma veto; an RV orbit or component assignment may need revisiting where mismatch is large. Median fitted eclipse duration is about 3.56 h, physically plausible for stellar-size eclipses in a 20–23 d orbit, but no fitted stellar radii or masses are claimed.

## Outcome and next observation

Physical outcome is **CONFIRMED** after completed bounded review. Catalogue novelty is a separate shared-catalogue decision; a failed query is unknown, not a non-match. Limits: Three compact dips in sectors 21 and 47 give two adjacent sector 47 cycles; measuring the individual centers resolves the apparent phase displacement of the earlier sector 47 window. Timing agrees with the Gaia period within stated errors and the deficit is target-centered. Next decisive check: Optional additional clean timing epoch.
