# TIC 159060569 — CONFIRMED

Bounded full physical review: **COMPLETE**. Review ID R689. Six raw SAP eclipses are visibly repeated across four sectors, though two gap-shaped fits have unidentifiable center covariance and are excluded from the timing fit. Sector 98 is shallower, consistent with sector-dependent aperture dilution.

## Raw SAP and timing

The sealed SOURCE-SNAPSHOT.json identifies the Gaia source, screening branch, and exact QLP FITS receipts. `measure_raw.py` verified every QLP SHA-256 before extracting quality-zero raw SAP_FLUX. Individual event centers were free trapezoid fits, with realized depth `d × min(1,w/(2k))` recorded separately from fitted model amplitude. Representative raw panels are in `raw-events.png`. The screening predictions only located windows; they are not timing points. 4 identifiable same-kind centers give **P = 21.742024655 ± 0.000038896 d**, epoch **BTJD 2204.95724592 ± 0.00308119 d** for the selected repeating eclipse. This is not automatically the deeper primary. Median realized QLP depth is 50.69 ppt. Linear same-kind event fit, individual max(formal center covariance, half cadence), scatter-inflated covariance if reduced chi square > 1; excludes uncalibrated model/pipeline systematics. Reduced chi-square is 1.557; formal values are conditional on the chosen event family and timing model.

| Sector | Same-kind cycle | Measured midpoint BTJD | Conservative center error d | Realized depth ppt |
|---|---:|---:|---:|---:|
| 33 | 33 | 2204.95719734 | 0.003472 | 53.84 |
| 33 | 34 | 2226.69947717 | 0.003472 | 53.80 |
| 98 | 116 | 4009.54384031 | 0.001157 | 43.01 |
| 98 | 117 | 4031.28875140 | 0.001157 | 47.58 |

The independent `coverage_alias.py` samples clean main and opposite half-phase windows from the measured ephemeris. Main-window median core deficits and local robust scatter (ppt) are below. Missing or flagged windows are retained in `coverage-alias.json` and never treated as clean nulls.

| Sector | Cycle | Clean core samples | Core deficit ppt | OOT scatter ppt |
|---|---:|---:|---:|---:|
| 6 | -33 | 7 | 54.81 | 0.35 |
| 33 | 0 | 38 | 54.34 | 0.21 |
| 33 | 1 | 34 | 54.34 | 0.28 |
| 87 | 68 | 75 | 54.98 | 0.70 |
| 98 | 83 | 112 | 43.39 | 0.79 |
| 98 | 84 | 70 | 43.84 | 1.13 |

Clean opposite half-phase windows test the half-period alias. A near-zero deficit is evidence against equal-depth P/2 recurrence; the deep half-phase events for TIC 284613090 are an observed second eclipse kind, not same-kind recurrences.



| Sector | Cycle | Clean core samples | Core deficit ppt |
|---|---:|---:|---:|
| 87 | 67 | 113 | 0.11 |
| 98 | 82 | 113 | 0.06 |
| 98 | 84 | 112 | 0.03 |

## Pixel source and alternate reduction

The helper's independent background-subtracted TESScut difference extraction uses the **same TESS FFI photons** as QLP sector 33; it checks pipeline/aperture robustness, not a second observation. The positive deficit centroid is 0.177 pixel from the target in that sector, with 5×5 aperture depth 50.47 ppt. This offset is descriptive, not a calibrated localization likelihood; see `batch-shared/helper-pixels/159060569/difference.png` and the pixel JSON for the full image and apertures. The Gaia DR3 60-arcsec neighbor cone and optimistic G-band/full-throughput capability screen find:

| Capable Gaia source | Separation arcsec | G | Minimum intrinsic eclipse fraction proxy |
|---|---:|---:|---:|
| None | | | |

Capability uses the smaller QLP/TESScut representative loss as a conservative screen. A neighbor's required **intrinsic** eclipse loss cannot be equated to its **diluted pixel** loss. Color, aperture throughput, unresolved companions, and subpixel crowding limit attribution.

## Gaia orbit and physical interpretation

Gaia DR3 source 3315856318930628096 has a SB1 solution with P = 21.741090401 ± 0.009054969 d, eccentricity 0.17966, ω = 240.616°, and mass function 0.018445 M☉. The closest edge-on conjunction (A) differs from the measured eclipse epoch by +0.0289 d (+0.00133 phase); source-specific Gaia full-covariance linear timing uncertainty at that epoch is 0.8020 d. The photometric minus Gaia period is +0.000934 d. `gaia-geometry.json` retains both conjunctions, the correlation order, and the exact orbital inputs; `helper-geometry.json` is an independent calculation. Linear covariance is descriptive, not a sigma veto; an RV orbit or component assignment may need revisiting where mismatch is large. Median fitted eclipse duration is about 10.64 h, physically plausible for stellar-size eclipses in a 20–23 d orbit, but no fitted stellar radii or masses are claimed.

## Outcome and next observation

Physical outcome is **CONFIRMED** after completed bounded review. Catalogue novelty is a separate shared-catalogue decision; a failed query is unknown, not a non-match. Limits: Six raw SAP eclipses are visibly repeated across four sectors, though two gap-shaped fits have unidentifiable center covariance and are excluded from the timing fit. Sector 98 is shallower, consistent with sector-dependent aperture dilution. Next decisive check: Additional clean sectors to monitor the aperture-dependent depth.
