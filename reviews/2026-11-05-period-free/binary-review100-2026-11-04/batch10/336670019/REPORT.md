# H097 — TIC 336670019

Physical verdict for the selected fold: **REFUTED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; central catalogue gates remain unavailable.

Gaia DR3 4538298294501513728 is an SB1 with spectroscopic period 36.84994 d. This is selection context, not a measured eclipse clock. The screening solution is P=36.95790 d, duration 0.320 d, z=4.54, depth 2828 ppm; its P/2 test is 18.38727 d, z=1.86. Neither screening period is adopted as a photometric measurement.

## Raw evidence and interpretation

The 3.9 ppt s74 predicted core is in a dramatic post-gap recovery: the full sector rises by tens of ppt. The s80 predicted core is fully sampled and flat; s26/s40 have one-sided coverage. The narrow folded minimum is an alignment of the s74 recovery, not evidence for repeated eclipses.

All cached sectors were inspected in raw QLP SAP flux with QUALITY=0. Actual sector coverage (BTJD): s026 [2010.74,2035.10], n=410, cadence=30.0 min; s040 [2390.84,2418.82], n=2396, cadence=10.0 min; s053 [2744.05,2768.95], n=1685, cadence=10.0 min; s054 [2769.99,2796.08], n=2256, cadence=10.0 min; s074 [3312.94,3339.51], n=9924, cadence=3.3 min; s080 [3479.91,3506.33], n=8658, cadence=3.3 min; s081 [3506.57,3533.12], n=9304, cadence=3.3 min. The P-screened occasions, with observed core and separate left/right baseline counts, are: s026 2021.59: core 14, L/R 16/0, -0.1 ppt; s040 2391.17: core 22, L/R 0/39, -0.1 ppt; s053 2760.75: core 25, L/R 47/22, 1.3 ppt; s074 3315.12: core 139, L/R 90/207, 3.9 ppt; s080 3499.91: core 110, L/R 207/207, 0.0 ppt. These local medians are diagnostics, not fitted eclipse depths. Missing cadences and internal gaps are recorded in [raw-fold.json](raw-fold.json); [raw-fold.png](raw-fold.png) shows every full sector and both folds. P/2 windows and available KSPSAP measurements are in the numeric artifact. Predicted times are search windows, not measured event centers.

## Limits and next check

Characterize the sector-edge recovery separately if scientifically useful. This verdict refutes the selected repeating eclipse signal, not every possible binary configuration of the star. An alternate extraction of the same TESS photons tests processing, not recurrence.

## Provenance

The frozen [source packet](../../source-packets/336670019/sources.json) binds FITS paths, source hashes, Gaia metadata and original bulk/fold receipts. [SOURCE-HASHES.json](../SOURCE-HASHES.json) and [SHA256SUMS.json](../SHA256SUMS.json) seal the review artifacts.
