# TIC 95623701 — PLAUSIBLE

Bounded full physical review: **COMPLETE**. Review ID R696. The deep sharp sector 12 and 103 events have similar shape at an assumed 112-cycle alias, but sector 39 is much weaker and a fully covered quality-zero sector 65 predicted window is a clean null for that alias. The helper TESScut 3×3 extraction independently finds 93.06, 13.81, 0.124, and 126.81 ppt in sectors 12/39/65/103; aperture size alone does not explain the null. A 16.81-arcsec Gaia neighbor is capable only under a very deep intrinsic eclipse and remains unresolved at the pixel scale. The assumed alias also disagrees strongly with Gaia. The repeated-looking signal has no secure persistent orbital clock or source ownership.

## Raw SAP and timing

The sealed SOURCE-SNAPSHOT.json identifies the Gaia source, screening branch, and exact QLP FITS receipts. `measure_raw.py` verified every QLP SHA-256 before extracting quality-zero raw SAP_FLUX. Individual event centers were free trapezoid fits, with realized depth `d × min(1,w/(2k))` recorded separately from fitted model amplitude. Representative raw panels are in `raw-events.png`. The screening predictions only located windows; they are not timing points. The selected events can be fit under an **assumed 112-cycle alias** with P=22.413385024 d and reference BTJD 1648.01635309; conditional fit errors 0.000147632 d and 0.01567046 d are retained in measurements.json. The clean sector-65 null refutes an uncomplicated constant-depth interpretation, and alternative integer aliases and source ownership remain open. **No secure period or reference epoch is reported.** The selected-event median realized depth is 154.30 ppt; reduced chi-square for the conditional fit is 12.562.

| Sector | Same-kind cycle | Measured midpoint BTJD | Conservative center error d | Realized depth ppt |
|---|---:|---:|---:|---:|
| 12 | 0 | 1648.04978105 | 0.010416 | 165.80 |
| 39 | 32 | 2365.23947386 | 0.003472 | 20.52 |
| 103 | 112 | 4158.31564090 | 0.001157 | 154.30 |

The independent `coverage_alias.py` samples clean main and opposite half-phase windows from the conditional 112-cycle fit. Main-window median core deficits and local robust scatter (ppt) are below. Missing or flagged windows are retained in `coverage-alias.json` and never treated as clean nulls.

| Sector | Cycle | Clean core samples | Core deficit ppt | OOT scatter ppt |
|---|---:|---:|---:|---:|
| 12 | 0 | 5 | 109.00 | 1.15 |
| 39 | 32 | 14 | 16.20 | 1.74 |
| 65 | 64 | 52 | 0.21 | 0.56 |
| 103 | 112 | 52 | 120.02 | 0.77 |

Clean opposite half-phase windows test the half-period alias. A near-zero deficit is evidence against equal-depth P/2 recurrence; the deep half-phase events for TIC 284613090 are an observed second eclipse kind, not same-kind recurrences.



| Sector | Cycle | Clean core samples | Core deficit ppt |
|---|---:|---:|---:|
| 12 | -1 | 4 | 0.49 |
| 39 | 32 | 14 | -1.80 |
| 65 | 63 | 52 | -0.11 |
| 65 | 64 | 52 | -0.05 |
| 103 | 112 | 51 | -0.36 |

## Pixel source and alternate reduction

The helper's independent background-subtracted TESScut difference extraction uses the **same TESS FFI photons** as QLP sector 103; it checks pipeline/aperture robustness, not a second observation. The positive deficit centroid is 0.304 pixel from the target in that sector, with 5×5 aperture depth 131.44 ppt. This offset is descriptive, not a calibrated localization likelihood; see `batch-shared/helper-pixels/95623701/difference.png` and the pixel JSON for the full image and apertures. The Gaia DR3 60-arcsec neighbor cone and optimistic G-band/full-throughput capability screen find:

| Capable Gaia source | Separation arcsec | G | Minimum intrinsic eclipse fraction proxy |
|---|---:|---:|---:|
| 6022994340434249728 | 16.81 | 11.321 | 82.4% |

Capability uses the smaller QLP/TESScut representative loss as a conservative screen. A neighbor's required **intrinsic** eclipse loss cannot be equated to its **diluted pixel** loss. Color, aperture throughput, unresolved companions, and subpixel crowding limit attribution.

## Gaia orbit and physical interpretation

Gaia DR3 source 6022994237355035264 has a SB2 solution with P = 22.435516302 ± 0.001515561 d, eccentricity 0.47522, ω = 271.245°, and mass function 0.65844 M☉. The closest edge-on conjunction (A) differs from the conditional alias-fit reference epoch by +1.5763 d (+0.07026 phase); source-specific Gaia full-covariance linear timing uncertainty at that epoch is 0.1227 d. Conditional assumed-alias minus Gaia period is -0.022131 d. `gaia-geometry.json` retains both conjunctions, the correlation order, and the exact orbital inputs; `helper-geometry.json` is an independent calculation. Linear covariance is descriptive, not a sigma veto; an RV orbit or component assignment may need revisiting where mismatch is large. Median fitted eclipse duration is about 3.75 h, physically plausible for stellar-size eclipses in a 20–23 d orbit, but no fitted stellar radii or masses are claimed.

## Outcome and next observation

Physical outcome is **PLAUSIBLE** after completed bounded review. Catalogue novelty is a separate shared-catalogue decision; a failed query is unknown, not a non-match. Limits: The deep sharp sector 12 and 103 events have similar shape at an assumed 112-cycle alias, but sector 39 is much weaker and a fully covered quality-zero sector 65 predicted window is a clean null for that alias. The helper TESScut 3×3 extraction independently finds 93.06, 13.81, 0.124, and 126.81 ppt in sectors 12/39/65/103; aperture size alone does not explain the null. A 16.81-arcsec Gaia neighbor is capable only under a very deep intrinsic eclipse and remains unresolved at the pixel scale. The assumed alias also disagrees strongly with Gaia. The repeated-looking signal has no secure persistent orbital clock or source ownership. Next decisive check: Resolved multi-source photometry and new clean epochs to test recurrence and source ownership.
