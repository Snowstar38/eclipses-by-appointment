# H099 — TIC 470982003

Physical verdict for the selected fold: **REFUTED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; central catalogue gates remain unavailable.

Gaia DR3 986467955403305984 is an SB1 with spectroscopic period 32.49633 d. This is selection context, not a measured eclipse clock. The screening solution is P=32.53375 d, duration 0.320 d, z=4.42, depth 444 ppm; its P/2 test is 16.26716 d, z=4.01. Neither screening period is adopted as a photometric measurement.

## Raw evidence and interpretation

The s60 1.4 ppt local deficit falls in the relaxation from a large sector-opening bright excursion; its flanks differ by 3.3 ppt, so its contribution to the fold is a positive trend artifact. The s20 predicted core is near 0.1 ppt, while s47 is about 0.4 ppt, comparable to the weak screened depth but embedded in broad modulation rather than a clear local box. These data reject the selected stacked eclipse shape; s47 alone is too weak and insecure to establish an isolated event.

All cached sectors were inspected in raw QLP SAP flux with QUALITY=0. Actual sector coverage (BTJD): s020 [1842.81,1868.41], n=1000, cadence=30.0 min; s047 [2580.48,2606.90], n=3010, cadence=10.0 min; s060 [2938.39,2962.56], n=7835, cadence=3.3 min. The P-screened occasions, with observed core and separate left/right baseline counts, are: s020 1866.40: core 15, L/R 19/22, 0.1 ppt; s047 2582.14: core 44, L/R 62/66, 0.4 ppt; s060 2940.01: core 139, L/R 207/206, 1.4 ppt. These local medians are diagnostics, not fitted eclipse depths. Missing cadences and internal gaps are recorded in [raw-fold.json](raw-fold.json); [raw-fold.png](raw-fold.png) shows every full sector and both folds. P/2 windows and available KSPSAP measurements are in the numeric artifact. Predicted times are search windows, not measured event centers.

## Limits and next check

Inspect s47 with independent pixel photometry if its weak depression is pursued. This verdict refutes the selected repeating eclipse signal, not every possible binary configuration of the star. An alternate extraction of the same TESS photons tests processing, not recurrence.

## Provenance

The frozen [source packet](../../source-packets/470982003/sources.json) binds FITS paths, source hashes, Gaia metadata and original bulk/fold receipts. [SOURCE-HASHES.json](../SOURCE-HASHES.json) and [SHA256SUMS.json](../SHA256SUMS.json) seal the review artifacts.
