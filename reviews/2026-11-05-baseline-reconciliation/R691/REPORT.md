# TIC 342060048 — PROBABLE

Bounded full physical review: **COMPLETE**. Review ID R691. Four narrow deep events repeat, including consecutive sector 40 cycles. The 17.52-arcsec capable Gaia neighbor lies less than one TESS pixel away; target-centered difference imaging favors the target but does not resolve the blend. Gaia period and conjunction are modestly discrepant at formal error scale.

## Raw SAP and timing

The sealed SOURCE-SNAPSHOT.json identifies the Gaia source, screening branch, and exact QLP FITS receipts. `measure_raw.py` verified every QLP SHA-256 before extracting quality-zero raw SAP_FLUX. Individual event centers were free trapezoid fits, with realized depth `d × min(1,w/(2k))` recorded separately from fitted model amplitude. Representative raw panels are in `raw-events.png`. The screening predictions only located windows; they are not timing points. 4 identifiable same-kind centers give **P = 21.732760955 ± 0.000051543 d**, epoch **BTJD 2396.19248167 ± 0.00224622 d** for the selected repeating eclipse. This is not automatically the deeper primary. Median realized QLP depth is 127.02 ppt. Linear same-kind event fit, individual max(formal center covariance, half cadence), scatter-inflated covariance if reduced chi square > 1; excludes uncalibrated model/pipeline systematics. Reduced chi-square is 0.058; formal values are conditional on the chosen event family and timing model.

| Sector | Same-kind cycle | Measured midpoint BTJD | Conservative center error d | Realized depth ppt |
|---|---:|---:|---:|---:|
| 40 | 0 | 2396.19214652 | 0.003472 | 127.47 |
| 40 | 1 | 2417.92486727 | 0.003472 | 129.53 |
| 53 | 17 | 2765.65048310 | 0.003472 | 109.02 |
| 80 | 50 | 3482.83049003 | 0.001157 | 126.57 |

The independent `coverage_alias.py` samples clean main and opposite half-phase windows from the measured ephemeris. Main-window median core deficits and local robust scatter (ppt) are below. Missing or flagged windows are retained in `coverage-alias.json` and never treated as clean nulls.

| Sector | Cycle | Clean core samples | Core deficit ppt | OOT scatter ppt |
|---|---:|---:|---:|---:|
| 40 | 0 | 12 | 68.54 | 0.96 |
| 40 | 1 | 13 | 70.31 | 1.34 |
| 53 | 17 | 9 | 37.59 | 0.57 |
| 80 | 50 | 52 | 79.86 | 0.96 |

Clean opposite half-phase windows test the half-period alias. A near-zero deficit is evidence against equal-depth P/2 recurrence; the deep half-phase events for TIC 284613090 are an observed second eclipse kind, not same-kind recurrences.



| Sector | Cycle | Clean core samples | Core deficit ppt |
|---|---:|---:|---:|
| 40 | 0 | 12 | 0.81 |
| 53 | 16 | 10 | 1.17 |
| 79 | 49 | 51 | 0.84 |
| 80 | 50 | 51 | -0.39 |

## Pixel source and alternate reduction

The helper's independent background-subtracted TESScut difference extraction uses the **same TESS FFI photons** as QLP sector 80; it checks pipeline/aperture robustness, not a second observation. The positive deficit centroid is 0.045 pixel from the target in that sector, with 5×5 aperture depth 54.05 ppt. This offset is descriptive, not a calibrated localization likelihood; see `batch-shared/helper-pixels/342060048/difference.png` and the pixel JSON for the full image and apertures. The Gaia DR3 60-arcsec neighbor cone and optimistic G-band/full-throughput capability screen find:

| Capable Gaia source | Separation arcsec | G | Minimum intrinsic eclipse fraction proxy |
|---|---:|---:|---:|
| 4576082942870779776 | 17.52 | 10.078 | 11.6% |

Capability uses the smaller QLP/TESScut representative loss as a conservative screen. A neighbor's required **intrinsic** eclipse loss cannot be equated to its **diluted pixel** loss. Color, aperture throughput, unresolved companions, and subpixel crowding limit attribution.

## Gaia orbit and physical interpretation

Gaia DR3 source 4576082977230517248 has a SB2 solution with P = 21.725152000 ± 0.001739894 d, eccentricity 0.50713, ω = 70.618°, and mass function 0.31345 M☉. The closest edge-on conjunction (A) differs from the measured eclipse epoch by +0.5515 d (+0.02539 phase); source-specific Gaia full-covariance linear timing uncertainty at that epoch is 0.1320 d. The photometric minus Gaia period is +0.007609 d. `gaia-geometry.json` retains both conjunctions, the correlation order, and the exact orbital inputs; `helper-geometry.json` is an independent calculation. Linear covariance is descriptive, not a sigma veto; an RV orbit or component assignment may need revisiting where mismatch is large. Median fitted eclipse duration is about 2.91 h, physically plausible for stellar-size eclipses in a 20–23 d orbit, but no fitted stellar radii or masses are claimed.

## Outcome and next observation

Physical outcome is **PROBABLE** after completed bounded review. Catalogue novelty is a separate shared-catalogue decision; a failed query is unknown, not a non-match. Limits: Four narrow deep events repeat, including consecutive sector 40 cycles. The 17.52-arcsec capable Gaia neighbor lies less than one TESS pixel away; target-centered difference imaging favors the target but does not resolve the blend. Gaia period and conjunction are modestly discrepant at formal error scale. Next decisive check: Resolved-source photometry or multi-source PSF localization, and new timing to test Gaia-orbit identity.
