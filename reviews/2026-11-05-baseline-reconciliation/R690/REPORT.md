# TIC 387268955 — CONFIRMED

Bounded full physical review: **COMPLETE**. Review ID R690. Fourteen usable broad same-kind eclipses across many sectors; sector 60 is shallower at an edge window. Two additional fitted windows are excluded for incomplete/unidentifiable timing.

## Raw SAP and timing

The sealed SOURCE-SNAPSHOT.json identifies the Gaia source, screening branch, and exact QLP FITS receipts. `measure_raw.py` verified every QLP SHA-256 before extracting quality-zero raw SAP_FLUX. Individual event centers were free trapezoid fits, with realized depth `d × min(1,w/(2k))` recorded separately from fitted model amplitude. Representative raw panels are in `raw-events.png`. The screening predictions only located windows; they are not timing points. 14 identifiable same-kind centers give **P = 22.766660808 ± 0.000031387 d**, epoch **BTJD 1805.48913997 ± 0.00197563 d** for the selected repeating eclipse. This is not automatically the deeper primary. Median realized QLP depth is 48.16 ppt. Linear same-kind event fit, individual max(formal center covariance, half cadence), scatter-inflated covariance if reduced chi square > 1; excludes uncalibrated model/pipeline systematics. Reduced chi-square is 0.024; formal values are conditional on the chosen event family and timing model.

| Sector | Same-kind cycle | Measured midpoint BTJD | Conservative center error d | Realized depth ppt |
|---|---:|---:|---:|---:|
| 18 | 0 | 1805.48881683 | 0.010417 | 47.96 |
| 20 | 2 | 1851.02237887 | 0.010416 | 48.52 |
| 24 | 7 | 1964.85576309 | 0.010417 | 48.46 |
| 25 | 8 | 1987.62252945 | 0.010417 | 45.01 |
| 26 | 10 | 2033.15502961 | 0.010417 | 48.16 |
| 52 | 41 | 2738.92177768 | 0.003472 | 48.09 |
| 53 | 42 | 2761.68909059 | 0.003472 | 48.42 |
| 58 | 48 | 2898.28895631 | 0.001157 | 48.82 |
| 59 | 49 | 2921.05577821 | 0.001157 | 48.59 |
| 60 | 50 | 2943.82197006 | 0.001157 | 25.27 |
| 73 | 66 | 3308.08866806 | 0.001157 | 47.84 |
| 78 | 72 | 3444.68832919 | 0.001157 | 48.15 |
| 79 | 73 | 3467.45560024 | 0.001157 | 47.25 |
| 85 | 80 | 3626.82215309 | 0.001157 | 48.49 |

The independent `coverage_alias.py` samples clean main and opposite half-phase windows from the measured ephemeris. Main-window median core deficits and local robust scatter (ppt) are below. Missing or flagged windows are retained in `coverage-alias.json` and never treated as clean nulls.

| Sector | Cycle | Clean core samples | Core deficit ppt | OOT scatter ppt |
|---|---:|---:|---:|---:|
| 18 | 0 | 13 | 39.70 | 0.24 |
| 20 | 2 | 12 | 40.19 | 0.20 |
| 24 | 7 | 12 | 40.72 | 0.31 |
| 25 | 8 | 7 | 37.33 | 0.25 |
| 26 | 10 | 10 | 36.85 | 0.18 |
| 52 | 41 | 38 | 38.83 | 0.73 |
| 53 | 42 | 37 | 39.56 | 0.38 |
| 58 | 48 | 112 | 39.77 | 0.67 |
| 59 | 49 | 113 | 39.00 | 0.75 |
| 60 | 50 | 19 | 18.25 | 0.80 |
| 73 | 66 | 113 | 39.38 | 0.54 |
| 78 | 72 | 110 | 39.61 | 0.71 |
| 79 | 73 | 113 | 39.09 | 0.76 |
| 85 | 80 | 113 | 40.10 | 0.62 |
| 86 | 81 | 53 | 37.57 | 1.09 |

Clean opposite half-phase windows test the half-period alias. A near-zero deficit is evidence against equal-depth P/2 recurrence; the deep half-phase events for TIC 284613090 are an observed second eclipse kind, not same-kind recurrences.



| Sector | Cycle | Clean core samples | Core deficit ppt |
|---|---:|---:|---:|
| 18 | -1 | 12 | -0.03 |
| 19 | 1 | 8 | 0.15 |
| 20 | 2 | 6 | 0.22 |
| 24 | 7 | 13 | 0.02 |
| 25 | 8 | 12 | -0.10 |
| 40 | 26 | 38 | -0.14 |
| 52 | 40 | 38 | 0.16 |
| 53 | 41 | 38 | -0.36 |
| 58 | 47 | 113 | 0.17 |
| 58 | 48 | 113 | 0.19 |
| 59 | 49 | 112 | -0.05 |
| 73 | 65 | 113 | 0.09 |
| 79 | 72 | 113 | -0.11 |
| 79 | 73 | 112 | 0.00 |
| 85 | 79 | 112 | -0.25 |
| 86 | 80 | 109 | -0.12 |
| 86 | 81 | 112 | -0.24 |

## Pixel source and alternate reduction

The helper's independent background-subtracted TESScut difference extraction uses the **same TESS FFI photons** as QLP sector 26; it checks pipeline/aperture robustness, not a second observation. The positive deficit centroid is 0.045 pixel from the target in that sector, with 5×5 aperture depth 42.53 ppt. This offset is descriptive, not a calibrated localization likelihood; see `batch-shared/helper-pixels/387268955/difference.png` and the pixel JSON for the full image and apertures. The Gaia DR3 60-arcsec neighbor cone and optimistic G-band/full-throughput capability screen find:

| Capable Gaia source | Separation arcsec | G | Minimum intrinsic eclipse fraction proxy |
|---|---:|---:|---:|
| None | | | |

Capability uses the smaller QLP/TESScut representative loss as a conservative screen. A neighbor's required **intrinsic** eclipse loss cannot be equated to its **diluted pixel** loss. Color, aperture throughput, unresolved companions, and subpixel crowding limit attribution.

## Gaia orbit and physical interpretation

Gaia DR3 source 2297343582469410688 has a SB1 solution with P = 22.766954260 ± 0.002642240 d, eccentricity 0.11826, ω = 344.754°, and mass function 0.062434 M☉. The closest edge-on conjunction (A) differs from the measured eclipse epoch by +0.0142 d (+0.00062 phase); source-specific Gaia full-covariance linear timing uncertainty at that epoch is 0.1944 d. The photometric minus Gaia period is -0.000293 d. `gaia-geometry.json` retains both conjunctions, the correlation order, and the exact orbital inputs; `helper-geometry.json` is an independent calculation. Linear covariance is descriptive, not a sigma veto; an RV orbit or component assignment may need revisiting where mismatch is large. Median fitted eclipse duration is about 8.15 h, physically plausible for stellar-size eclipses in a 20–23 d orbit, but no fitted stellar radii or masses are claimed.

## Outcome and next observation

Physical outcome is **CONFIRMED** after completed bounded review. Catalogue novelty is a separate shared-catalogue decision; a failed query is unknown, not a non-match. Limits: Fourteen usable broad same-kind eclipses across many sectors; sector 60 is shallower at an edge window. Two additional fitted windows are excluded for incomplete/unidentifiable timing. Next decisive check: Optional new clean events to refine ephemeris.
