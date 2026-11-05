# H093 — TIC 118207666

Physical verdict for the selected fold: **REFUTED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; central catalogue gates remain unavailable.

Gaia DR3 5703377580206903680 is an SB1 with spectroscopic period 54.77115 d. This is selection context, not a measured eclipse clock. The screening solution is P=54.32887 d, duration 0.500 d, z=4.78, depth 823 ppm; its P/2 test is 27.45720 d, z=3.72. Neither screening period is adopted as a photometric measurement.

## Raw evidence and interpretation

The well-covered s35 predicted core is 0.3 ppt brighter than its local sides. S61 sits on a broad rising trend and s99 on the recovery from a gap/level change; their 2.4 and 2.0 ppt local medians are not repeated isolated eclipses. The P2 result reuses the same s99 feature.

All cached sectors were inspected in raw QLP SAP flux with QUALITY=0. Actual sector coverage (BTJD): s008 [1517.93,1541.79], n=747, cadence=30.0 min; s034 [2229.22,2253.24], n=2974, cadence=10.0 min; s035 [2256.33,2279.91], n=2000, cadence=10.0 min; s061 [2964.04,2987.95], n=9329, cadence=3.3 min; s088 [3690.19,3717.91], n=11484, cadence=3.3 min; s099 [4049.70,4070.52], n=5589, cadence=3.3 min. The P-screened occasions, with observed core and separate left/right baseline counts, are: s035 2275.24: core 58, L/R 69/90, -0.3 ppt; s061 2981.51: core 179, L/R 322/260, 2.4 ppt; s099 4068.09: core 216, L/R 257/322, 2.0 ppt. These local medians are diagnostics, not fitted eclipse depths. Missing cadences and internal gaps are recorded in [raw-fold.json](raw-fold.json); [raw-fold.png](raw-fold.png) shows every full sector and both folds. P/2 windows and available KSPSAP measurements are in the numeric artifact. Predicted times are search windows, not measured event centers.

## Limits and next check

Investigate broad variability with an independent aperture if it becomes a separate target of interest. This verdict refutes the selected repeating eclipse signal, not every possible binary configuration of the star. An alternate extraction of the same TESS photons tests processing, not recurrence.

## Provenance

The frozen [source packet](../../source-packets/118207666/sources.json) binds FITS paths, source hashes, Gaia metadata and original bulk/fold receipts. [SOURCE-HASHES.json](../SOURCE-HASHES.json) and [SHA256SUMS.json](../SHA256SUMS.json) seal the review artifacts.
