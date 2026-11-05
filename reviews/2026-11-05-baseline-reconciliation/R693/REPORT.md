# TIC 64701575 — CONFIRMED

Bounded full physical review: **COMPLETE**. Review ID R693. Four clean rounded eclipses across sectors 33/34/87/88; sector 7 contains a partial predicted window. The timing and target-centered difference image support the Gaia-orbit eclipse identification.

## Raw SAP and timing

The sealed SOURCE-SNAPSHOT.json identifies the Gaia source, screening branch, and exact QLP FITS receipts. `measure_raw.py` verified every QLP SHA-256 before extracting quality-zero raw SAP_FLUX. Individual event centers were free trapezoid fits, with realized depth `d × min(1,w/(2k))` recorded separately from fitted model amplitude. Representative raw panels are in `raw-events.png`. The screening predictions only located windows; they are not timing points. 4 identifiable same-kind centers give **P = 21.162030376 ± 0.000038311 d**, epoch **BTJD 2222.48391953 ± 0.00247265 d** for the selected repeating eclipse. This is not automatically the deeper primary. Median realized QLP depth is 46.85 ppt. Linear same-kind event fit, individual max(formal center covariance, half cadence), scatter-inflated covariance if reduced chi square > 1; excludes uncalibrated model/pipeline systematics. Reduced chi-square is 0.023; formal values are conditional on the chosen event family and timing model.

| Sector | Same-kind cycle | Measured midpoint BTJD | Conservative center error d | Realized depth ppt |
|---|---:|---:|---:|---:|
| 33 | 34 | 2222.48415769 | 0.003472 | 46.55 |
| 34 | 35 | 2243.64572454 | 0.003472 | 47.15 |
| 87 | 103 | 3682.66389113 | 0.001157 | 44.92 |
| 88 | 104 | 3703.82631924 | 0.001726 | 48.32 |

The independent `coverage_alias.py` samples clean main and opposite half-phase windows from the measured ephemeris. Main-window median core deficits and local robust scatter (ppt) are below. Missing or flagged windows are retained in `coverage-alias.json` and never treated as clean nulls.

| Sector | Cycle | Clean core samples | Core deficit ppt | OOT scatter ppt |
|---|---:|---:|---:|---:|
| 33 | 0 | 26 | 39.55 | 0.48 |
| 34 | 1 | 26 | 40.03 | 0.34 |
| 87 | 69 | 75 | 39.38 | 1.11 |
| 88 | 70 | 40 | 46.19 | 1.72 |

Clean opposite half-phase windows test the half-period alias. A near-zero deficit is evidence against equal-depth P/2 recurrence; the deep half-phase events for TIC 284613090 are an observed second eclipse kind, not same-kind recurrences.



| Sector | Cycle | Clean core samples | Core deficit ppt |
|---|---:|---:|---:|
| 7 | -35 | 9 | -0.07 |
| 7 | -34 | 9 | 0.11 |
| 33 | -1 | 26 | 0.02 |
| 34 | 0 | 26 | -0.02 |
| 87 | 68 | 78 | 0.18 |
| 88 | 69 | 78 | -0.12 |
| 88 | 70 | 77 | 0.07 |

## Pixel source and alternate reduction

The helper's independent background-subtracted TESScut difference extraction uses the **same TESS FFI photons** as QLP sector 33; it checks pipeline/aperture robustness, not a second observation. The positive deficit centroid is 0.064 pixel from the target in that sector, with 5×5 aperture depth 37.53 ppt. This offset is descriptive, not a calibrated localization likelihood; see `batch-shared/helper-pixels/64701575/difference.png` and the pixel JSON for the full image and apertures. The Gaia DR3 60-arcsec neighbor cone and optimistic G-band/full-throughput capability screen find:

| Capable Gaia source | Separation arcsec | G | Minimum intrinsic eclipse fraction proxy |
|---|---:|---:|---:|
| None | | | |

Capability uses the smaller QLP/TESScut representative loss as a conservative screen. A neighbor's required **intrinsic** eclipse loss cannot be equated to its **diluted pixel** loss. Color, aperture throughput, unresolved companions, and subpixel crowding limit attribution.

## Gaia orbit and physical interpretation

Gaia DR3 source 5610990909531532160 has a SB2 solution with P = 21.164016663 ± 0.001408841 d, eccentricity 0.18807, ω = 55.441°, and mass function 0.35364 M☉. The closest edge-on conjunction (A) differs from the measured eclipse epoch by -0.1649 d (-0.00779 phase); source-specific Gaia full-covariance linear timing uncertainty at that epoch is 0.1122 d. The photometric minus Gaia period is -0.001986 d. `gaia-geometry.json` retains both conjunctions, the correlation order, and the exact orbital inputs; `helper-geometry.json` is an independent calculation. Linear covariance is descriptive, not a sigma veto; an RV orbit or component assignment may need revisiting where mismatch is large. Median fitted eclipse duration is about 6.54 h, physically plausible for stellar-size eclipses in a 20–23 d orbit, but no fitted stellar radii or masses are claimed.

## Outcome and next observation

Physical outcome is **CONFIRMED** after completed bounded review. Catalogue novelty is a separate shared-catalogue decision; a failed query is unknown, not a non-match. Limits: Four clean rounded eclipses across sectors 33/34/87/88; sector 7 contains a partial predicted window. The timing and target-centered difference image support the Gaia-orbit eclipse identification. Next decisive check: Optional clean sector 7 counterpart or future timing.
