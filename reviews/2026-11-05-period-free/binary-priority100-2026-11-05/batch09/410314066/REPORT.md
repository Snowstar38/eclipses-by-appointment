# T089 / TIC 410314066: CONFIRMED

Queue stratum: repeat_sector_dip. Bounded physical review: complete. Catalogue novelty: UNKNOWN.

## Deciding evidence

Six same-kind raw events in sectors 13, 27, 67, 94, 101 and 103 fit 29.749050 d over cycles 0, 13, 50, 74, 82 and 84 (largest residual 0.002 d). Covered P/2 alternate windows in s13, s67, s94 and s101 are flat, including fully covered s67. This agrees with Gaia SB1 29.749180 +/- 0.006943 d. The selected s13 event is about 39 ppt in QLP raw SAP and 40 ppt in the independent valid TESSCut aperture, with a target-region difference deficit and no nominal capable Gaia neighbor. Gaia-covariance propagation places the measured epoch 0.092 d from a predicted conjunction with sigma 0.329 d.

## Measurement and scope

Gaia source 6448639343335797888; selection orbit 29.74918011805926 d; Gaia G 9.810264. The raw QLP SAP analysis inspected 7 hash-verified FITS sectors and 11 retained dip windows, including actual quality and time coverage. Local trapezoid centers, event depths, sectors, and source hashes are in [lead-numeric.json](lead-numeric.json); representative profiles are in lead-raw-*.png. These retained detector windows were not taken as verdicts.
Source packet SHA-256: c5fef94a79e8f055583564eda7bac1a0bea18b92140858970cc52171a2fabd07. Bulk-result SHA-256: a9ce9ce5cb60bc379467e57ed7ad3d7344274c3e7380593de90c16360097ba75.

Selected same-kind fit: P = 29.749050 d; T0 = 1663.771312 BTJD; conditional formal period error = 3.375656e-05 d.
Cycle numbers, chosen eclipse kind and residuals: [lead-timing.json](../lead-timing.json).

The helper independently extracted the strongest event from TESSCut with a positive-flux target aperture and checked the difference pixels; see [helper audit](../helper-audit.md), [numeric pixel audit](../helper-pixel-audit.json), and helper-difference.png. It is a second reduction of the same TESS photons.

Actual half-period opposite-kind coverage: [lead-half-alias.json](../lead-half-alias.json).

## Limits and next check

The current TESSCut aperture reuses TESS photons; its depth is not an independent observation. The local TESSCut check covers one representative event, and the period error is conditional on selected cycles and trapezoid fits. Four VizieR novelty gates remain unavailable.

Acquire an independent pipeline time series and complete the unavailable catalogue gates before any novelty claim.

Catalogue status uses the [shared queue-wide audit](../../shared-catalogues/REPORT.md). Its four unavailable VizieR gates are unknown, not negative matches.
