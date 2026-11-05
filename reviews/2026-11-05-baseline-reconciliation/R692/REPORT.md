# TIC 184398115 — PROBABLE

Bounded full physical review: **COMPLETE**. Review ID R692. Four very deep repeated eclipses include consecutive sector 97 cycles, and the deficit is target-centered with no capable Gaia neighbor in the 60-arcsec cone. The measured eclipse period and phase are materially inconsistent with the formal Gaia SB2 orbit; a distinct eclipsing binary in a multiple system or a problematic Gaia orbit remains possible.

## Raw SAP and timing

The sealed SOURCE-SNAPSHOT.json identifies the Gaia source, screening branch, and exact QLP FITS receipts. `measure_raw.py` verified every QLP SHA-256 before extracting quality-zero raw SAP_FLUX. Individual event centers were free trapezoid fits, with realized depth `d × min(1,w/(2k))` recorded separately from fitted model amplitude. Representative raw panels are in `raw-events.png`. The screening predictions only located windows; they are not timing points. 4 identifiable same-kind centers give **P = 21.075640444 ± 0.000229351 d**, epoch **BTJD 1385.18468435 ± 0.02732858 d** for the selected repeating eclipse. This is not automatically the deeper primary. Median realized QLP depth is 330.88 ppt. Linear same-kind event fit, individual max(formal center covariance, half cadence), scatter-inflated covariance if reduced chi square > 1; excludes uncalibrated model/pipeline systematics. Reduced chi-square is 38.365; formal values are conditional on the chosen event family and timing model.

| Sector | Same-kind cycle | Measured midpoint BTJD | Conservative center error d | Realized depth ppt |
|---|---:|---:|---:|---:|
| 3 | 0 | 1385.26279578 | 0.010417 | 332.62 |
| 30 | 35 | 2122.81971547 | 0.003472 | 390.60 |
| 97 | 122 | 3956.41529753 | 0.001157 | 329.15 |
| 97 | 123 | 3977.48639171 | 0.001157 | 325.11 |

The independent `coverage_alias.py` samples clean main and opposite half-phase windows from the measured ephemeris. Main-window median core deficits and local robust scatter (ppt) are below. Missing or flagged windows are retained in `coverage-alias.json` and never treated as clean nulls.

| Sector | Cycle | Clean core samples | Core deficit ppt | OOT scatter ppt |
|---|---:|---:|---:|---:|
| 3 | 0 | 8 | 145.50 | 0.22 |
| 30 | 35 | 26 | 290.94 | 0.38 |
| 97 | 122 | 77 | 238.72 | 0.49 |
| 97 | 123 | 77 | 237.21 | 1.84 |

Clean opposite half-phase windows test the half-period alias. A near-zero deficit is evidence against equal-depth P/2 recurrence; the deep half-phase events for TIC 284613090 are an observed second eclipse kind, not same-kind recurrences.



| Sector | Cycle | Clean core samples | Core deficit ppt |
|---|---:|---:|---:|
| 30 | 35 | 24 | 0.08 |
| 97 | 121 | 78 | -0.02 |
| 97 | 122 | 76 | -0.39 |
| 97 | 123 | 74 | -0.83 |

## Pixel source and alternate reduction

The helper's independent background-subtracted TESScut difference extraction uses the **same TESS FFI photons** as QLP sector 3; it checks pipeline/aperture robustness, not a second observation. The positive deficit centroid is 0.090 pixel from the target in that sector, with 5×5 aperture depth 280.61 ppt. This offset is descriptive, not a calibrated localization likelihood; see `batch-shared/helper-pixels/184398115/difference.png` and the pixel JSON for the full image and apertures. The Gaia DR3 60-arcsec neighbor cone and optimistic G-band/full-throughput capability screen find:

| Capable Gaia source | Separation arcsec | G | Minimum intrinsic eclipse fraction proxy |
|---|---:|---:|---:|
| None | | | |

Capability uses the smaller QLP/TESScut representative loss as a conservative screen. A neighbor's required **intrinsic** eclipse loss cannot be equated to its **diluted pixel** loss. Color, aperture throughput, unresolved companions, and subpixel crowding limit attribution.

## Gaia orbit and physical interpretation

Gaia DR3 source 4956598319231891328 has a SB2 solution with P = 21.084638298 ± 0.001569015 d, eccentricity 0.16417, ω = 274.972°, and mass function 0.1844 M☉. The closest edge-on conjunction (A) differs from the measured eclipse epoch by -1.3772 d (-0.06532 phase); source-specific Gaia full-covariance linear timing uncertainty at that epoch is 0.0874 d. The photometric minus Gaia period is -0.008998 d. `gaia-geometry.json` retains both conjunctions, the correlation order, and the exact orbital inputs; `helper-geometry.json` is an independent calculation. Linear covariance is descriptive, not a sigma veto; an RV orbit or component assignment may need revisiting where mismatch is large. Median fitted eclipse duration is about 6.25 h, physically plausible for stellar-size eclipses in a 20–23 d orbit, but no fitted stellar radii or masses are claimed.

## Outcome and next observation

Physical outcome is **PROBABLE** after completed bounded review. Catalogue novelty is a separate shared-catalogue decision; a failed query is unknown, not a non-match. Limits: Four very deep repeated eclipses include consecutive sector 97 cycles, and the deficit is target-centered with no capable Gaia neighbor in the 60-arcsec cone. The measured eclipse period and phase are materially inconsistent with the formal Gaia SB2 orbit; a distinct eclipsing binary in a multiple system or a problematic Gaia orbit remains possible. Next decisive check: New radial-velocity orbit and clean eclipse timings to establish whether the Gaia and eclipse clocks belong to the same pair.
