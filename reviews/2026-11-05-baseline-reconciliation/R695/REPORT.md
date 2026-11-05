# TIC 128720791 — PROBABLE

Bounded full physical review: **COMPLETE**. Review ID R695. Three clean narrow same-kind dips in sectors 16/56/83; the earlier sector 56 predicted cycle lies at the sector boundary and is not a clean null. Explicit 15–30 d integer-cycle enumeration found a 16.2798 d alias, but three additional clean predicted windows have near-zero loss and refute that equal-depth branch. The Gaia-near 21.7064 d branch has no contradictory clean window. The signal is reproduced by separate TESScut extraction and a target-centered difference image; Gaia phase/period differences remain a limitation.

## Raw SAP and timing

The sealed SOURCE-SNAPSHOT.json identifies the Gaia source, screening branch, and exact QLP FITS receipts. `measure_raw.py` verified every QLP SHA-256 before extracting quality-zero raw SAP_FLUX. Individual event centers were free trapezoid fits, with realized depth `d × min(1,w/(2k))` recorded separately from fitted model amplitude. Representative raw panels are in `raw-events.png`. The screening predictions only located windows; they are not timing points. 3 identifiable same-kind centers give **P = 21.706415188 ± 0.000047235 d**, epoch **BTJD 1740.08940285 ± 0.00327218 d** for the selected repeating eclipse. This is not automatically the deeper primary. Median realized QLP depth is 8.18 ppt. Linear same-kind event fit, individual max(formal center covariance, half cadence), scatter-inflated covariance if reduced chi square > 1; excludes uncalibrated model/pipeline systematics. Reduced chi-square is 0.000; formal values are conditional on the chosen event family and timing model.

| Sector | Same-kind cycle | Measured midpoint BTJD | Conservative center error d | Realized depth ppt |
|---|---:|---:|---:|---:|
| 16 | 0 | 1740.08921351 | 0.010417 | 8.18 |
| 56 | 51 | 2847.11658341 | 0.001157 | 8.18 |
| 83 | 84 | 3563.42827506 | 0.001157 | 8.46 |

The independent `coverage_alias.py` samples clean main and opposite half-phase windows from the measured ephemeris. Main-window median core deficits and local robust scatter (ppt) are below. Missing or flagged windows are retained in `coverage-alias.json` and never treated as clean nulls.

| Sector | Cycle | Clean core samples | Core deficit ppt | OOT scatter ppt |
|---|---:|---:|---:|---:|
| 16 | 0 | 6 | 3.81 | 0.45 |
| 56 | 51 | 52 | 4.61 | 0.81 |
| 83 | 84 | 52 | 4.58 | 0.70 |

Clean opposite half-phase windows test the half-period alias. A near-zero deficit is evidence against equal-depth P/2 recurrence; the deep half-phase events for TIC 284613090 are an observed second eclipse kind, not same-kind recurrences.

The near-Gaia period alias for TIC 128720791 was separately enumerated in `batch-shared/alias-128720791.json`; the 16.2798 d branch has three clean, near-zero predicted windows.

| Sector | Cycle | Clean core samples | Core deficit ppt |
|---|---:|---:|---:|
| 56 | 50 | 46 | 0.12 |
| 83 | 84 | 52 | -0.15 |

## Pixel source and alternate reduction

The helper's independent background-subtracted TESScut difference extraction uses the **same TESS FFI photons** as QLP sector 16; it checks pipeline/aperture robustness, not a second observation. The positive deficit centroid is 0.095 pixel from the target in that sector, with 5×5 aperture depth 8.19 ppt. This offset is descriptive, not a calibrated localization likelihood; see `batch-shared/helper-pixels/128720791/difference.png` and the pixel JSON for the full image and apertures. The Gaia DR3 60-arcsec neighbor cone and optimistic G-band/full-throughput capability screen find:

| Capable Gaia source | Separation arcsec | G | Minimum intrinsic eclipse fraction proxy |
|---|---:|---:|---:|
| None | | | |

Capability uses the smaller QLP/TESScut representative loss as a conservative screen. A neighbor's required **intrinsic** eclipse loss cannot be equated to its **diluted pixel** loss. Color, aperture throughput, unresolved companions, and subpixel crowding limit attribution.

## Gaia orbit and physical interpretation

Gaia DR3 source 1932564828836775424 has a SB2 solution with P = 21.708922852 ± 0.000877998 d, eccentricity 0.52540, ω = 280.801°, and mass function 0.33886 M☉. The closest edge-on conjunction (B) differs from the measured eclipse epoch by -0.2326 d (-0.01072 phase); source-specific Gaia full-covariance linear timing uncertainty at that epoch is 0.0430 d. The photometric minus Gaia period is -0.002508 d. `gaia-geometry.json` retains both conjunctions, the correlation order, and the exact orbital inputs; `helper-geometry.json` is an independent calculation. Linear covariance is descriptive, not a sigma veto; an RV orbit or component assignment may need revisiting where mismatch is large. Median fitted eclipse duration is about 2.32 h, physically plausible for stellar-size eclipses in a 20–23 d orbit, but no fitted stellar radii or masses are claimed.

## Outcome and next observation

Physical outcome is **PROBABLE** after completed bounded review. Catalogue novelty is a separate shared-catalogue decision; a failed query is unknown, not a non-match. Limits: Three clean narrow same-kind dips in sectors 16/56/83; the earlier sector 56 predicted cycle lies at the sector boundary and is not a clean null. Explicit 15–30 d integer-cycle enumeration found a 16.2798 d alias, but three additional clean predicted windows have near-zero loss and refute that equal-depth branch. The Gaia-near 21.7064 d branch has no contradictory clean window. The signal is reproduced by separate TESScut extraction and a target-centered difference image; Gaia phase/period differences remain a limitation. Next decisive check: Additional clean event and independent Gaia-orbit comparison.
