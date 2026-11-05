# H098 — TIC 341854405

Physical verdict for the selected fold: **REFUTED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; central catalogue gates remain unavailable.

Gaia DR3 5291612949507707392 is an SB1 with spectroscopic period 43.98962 d. This is selection context, not a measured eclipse clock. The screening solution is P=43.91324 d, duration 0.320 d, z=4.30, depth 914 ppm; its P/2 test is 21.92595 d, z=2.15. Neither screening period is adopted as a photometric measurement.

## Raw evidence and interpretation

The s88 predicted core overlaps a broad positive excursion and strong local slope (7.3 ppt left/right mismatch); s90 has a densely covered flat core. Several other predicted windows intersect sector edges or gaps. The selected 43.913 d fold does not have repeatable eclipse morphology.

All cached sectors were inspected in raw QLP SAP flux with QUALITY=0. Actual sector coverage (BTJD): s008 [1518.10,1541.93], n=683, cadence=30.0 min; s009 [1544.39,1568.41], n=990, cadence=30.0 min; s010 [1571.20,1595.41], n=925, cadence=30.0 min; s034 [2229.31,2253.27], n=3002, cadence=10.0 min; s035 [2256.32,2279.85], n=2072, cadence=10.0 min; s036 [2283.23,2305.59], n=2532, cadence=10.0 min; s037 [2311.30,2332.33], n=2679, cadence=10.0 min; s061 [2963.81,2987.91], n=9394, cadence=3.3 min; s062 [2989.50,3013.91], n=9662, cadence=3.3 min; s063 [3014.41,3039.66], n=10529, cadence=3.3 min; s088 [3690.18,3717.88], n=11546, cadence=3.3 min; s089 [3718.18,3746.92], n=11235, cadence=3.3 min; s090 [3747.41,3774.93], n=11124, cadence=3.3 min. The P-screened occasions, with observed core and separate left/right baseline counts, are: s009 1553.03: core 11, L/R 22/23, 0.6 ppt; s035 2255.64: core 0, L/R 0/35, unmeasurable; s036 2299.56: core 40, L/R 66/69, 0.8 ppt; s062 3002.17: core 0, L/R 0/208, unmeasurable; s088 3704.78: core 138, L/R 87/207, 3.1 ppt; s090 3748.69: core 138, L/R 207/207, -0.3 ppt. These local medians are diagnostics, not fitted eclipse depths. Missing cadences and internal gaps are recorded in [raw-fold.json](raw-fold.json); [raw-fold.png](raw-fold.png) shows every full sector and both folds. P/2 windows and available KSPSAP measurements are in the numeric artifact. Predicted times are search windows, not measured event centers.

## Limits and next check

A fresh search could test whether any unrelated isolated dip in the long time series warrants follow-up. This verdict refutes the selected repeating eclipse signal, not every possible binary configuration of the star. An alternate extraction of the same TESS photons tests processing, not recurrence.

## Provenance

The frozen [source packet](../../source-packets/341854405/sources.json) binds FITS paths, source hashes, Gaia metadata and original bulk/fold receipts. [SOURCE-HASHES.json](../SOURCE-HASHES.json) and [SHA256SUMS.json](../SHA256SUMS.json) seal the review artifacts.
