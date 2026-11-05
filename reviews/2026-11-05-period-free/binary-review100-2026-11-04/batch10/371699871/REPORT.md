# H095 — TIC 371699871

Physical verdict for the selected fold: **REFUTED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; central catalogue gates remain unavailable.

Gaia DR3 1799097581944489856 is an SB1 with spectroscopic period 35.70154 d. This is selection context, not a measured eclipse clock. The screening solution is P=36.03639 d, duration 0.500 d, z=4.02, depth 1180 ppm; its P/2 test is 17.66331 d, z=2.85. Neither screening period is adopted as a photometric measurement.

## Raw evidence and interpretation

The only well-sampled P occasion in s82 lies on a broad drop with a 5.3 ppt difference between left and right local baselines; the core itself is only 0.1 ppt below the combined sides. S55 is near the sector endpoint with no right baseline. The fold minimum is a slope/coverage mixture, not a repeated eclipse.

All cached sectors were inspected in raw QLP SAP flux with QUALITY=0. Actual sector coverage (BTJD): s015 [1711.38,1733.26], n=735, cadence=30.0 min; s055 [2797.15,2824.21], n=3594, cadence=10.0 min; s056 [2825.30,2853.12], n=11482, cadence=3.3 min; s082 [3533.42,3558.21], n=10361, cadence=3.3 min. The P-screened occasions, with observed core and separate left/right baseline counts, are: s055 2823.96: core 71, L/R 108/0, 0.3 ppt; s082 3544.68: core 212, L/R 324/208, 0.1 ppt. These local medians are diagnostics, not fitted eclipse depths. Missing cadences and internal gaps are recorded in [raw-fold.json](raw-fold.json); [raw-fold.png](raw-fold.png) shows every full sector and both folds. P/2 windows and available KSPSAP measurements are in the numeric artifact. Predicted times are search windows, not measured event centers.

## Limits and next check

A different period search would be needed to assess unrelated variability. This verdict refutes the selected repeating eclipse signal, not every possible binary configuration of the star. An alternate extraction of the same TESS photons tests processing, not recurrence.

## Provenance

The frozen [source packet](../../source-packets/371699871/sources.json) binds FITS paths, source hashes, Gaia metadata and original bulk/fold receipts. [SOURCE-HASHES.json](../SOURCE-HASHES.json) and [SHA256SUMS.json](../SHA256SUMS.json) seal the review artifacts.
