# H092 — TIC 307119823

Physical verdict for the selected fold: **REFUTED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; central catalogue gates remain unavailable.

Gaia DR3 402994410562917504 is an SB1 with spectroscopic period 32.03847 d. This is selection context, not a measured eclipse clock. The screening solution is P=31.85734 d, duration 0.072 d, z=4.52, depth 2053 ppm; its P/2 test is 16.13164 d, z=3.82. Neither screening period is adopted as a photometric measurement.

## Raw evidence and interpretation

The s18 window is at a sector level transition; the s58 2.1 ppt local median is on the decay of a much larger bright excursion (left/right baselines differ by 4.0 ppt). The fully sampled s85 predicted window is a 1.5 ppt brightening relative to its sides. These opposite, slope-contaminated occasions refute the selected 31.857 d repeating dip.

All cached sectors were inspected in raw QLP SAP flux with QUALITY=0. Actual sector coverage (BTJD): s017 [1766.49,1787.87], n=675, cadence=30.0 min; s018 [1792.04,1814.91], n=993, cadence=30.0 min; s058 [2882.38,2910.02], n=11024, cadence=3.3 min; s085 [3610.58,3636.02], n=8360, cadence=3.3 min. The P-screened occasions, with observed core and separate left/right baseline counts, are: s017 1769.23: core 0, L/R 12/18, unmeasurable; s018 1801.08: core 4, L/R 19/19, 1.8 ppt; s058 2884.23: core 31, L/R 173/173, 2.1 ppt; s085 3616.95: core 29, L/R 123/173, -1.5 ppt. These local medians are diagnostics, not fitted eclipse depths. Missing cadences and internal gaps are recorded in [raw-fold.json](raw-fold.json); [raw-fold.png](raw-fold.png) shows every full sector and both folds. P/2 windows and available KSPSAP measurements are in the numeric artifact. Predicted times are search windows, not measured event centers.

## Limits and next check

A pixel comparison could identify the origin of the sector transitions if the variability itself is pursued. This verdict refutes the selected repeating eclipse signal, not every possible binary configuration of the star. An alternate extraction of the same TESS photons tests processing, not recurrence.

## Provenance

The frozen [source packet](../../source-packets/307119823/sources.json) binds FITS paths, source hashes, Gaia metadata and original bulk/fold receipts. [SOURCE-HASHES.json](../SOURCE-HASHES.json) and [SHA256SUMS.json](../SHA256SUMS.json) seal the review artifacts.
