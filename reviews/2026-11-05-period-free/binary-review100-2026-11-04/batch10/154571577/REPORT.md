# H091 — TIC 154571577

Physical verdict for the selected fold: **REFUTED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; central catalogue gates remain unavailable.

Gaia DR3 1692108645225929984 is an SB1 with spectroscopic period 28.24938 d. This is selection context, not a measured eclipse clock. The screening solution is P=28.41817 d, duration 0.200 d, z=4.18, depth 971 ppm; its P/2 test is 14.06820 d, z=2.97. Neither screening period is adopted as a photometric measurement.

## Raw evidence and interpretation

The apparent s15 deficit at 1727.26 is embedded in a large positive post-gap excursion: the two local flanks differ by 20.2 ppt. Well-covered predicted windows in s14, s40, s41 and s60 are flat to about 0.2 ppt, and s75 is only 0.4 ppt. The selected 28.418 d eclipse fold is thus produced by a discontinuous excursion rather than repeated box-shaped eclipses.

All cached sectors were inspected in raw QLP SAP flux with QUALITY=0. Actual sector coverage (BTJD): s014 [1683.66,1710.16], n=1149, cadence=30.0 min; s015 [1711.39,1736.87], n=951, cadence=30.0 min; s020 [1842.78,1868.47], n=1011, cadence=30.0 min; s040 [2390.83,2418.82], n=3809, cadence=10.0 min; s041 [2420.88,2446.47], n=3431, cadence=10.0 min; s048 [2609.85,2635.95], n=3181, cadence=10.0 min; s060 [2938.34,2962.55], n=7932, cadence=3.3 min; s074 [3312.90,3339.55], n=11124, cadence=3.3 min; s075 [3339.81,3367.48], n=10343, cadence=3.3 min. The P-screened occasions, with observed core and separate left/right baseline counts, are: s014 1698.84: core 10, L/R 18/19, -0.1 ppt; s015 1727.26: core 9, L/R 16/19, 6.7 ppt; s020 1869.35: core 0, L/R 0/0, unmeasurable; s040 2409.29: core 29, L/R 57/56, 0.2 ppt; s041 2437.71: core 28, L/R 58/58, 0.1 ppt; s048 2636.64: core 0, L/R 2/0, unmeasurable; s060 2949.24: core 86, L/R 173/85, 0.1 ppt; s074 3318.67: core 76, L/R 168/117, 1.2 ppt; s075 3347.09: core 86, L/R 172/173, 0.4 ppt. These local medians are diagnostics, not fitted eclipse depths. Missing cadences and internal gaps are recorded in [raw-fold.json](raw-fold.json); [raw-fold.png](raw-fold.png) shows every full sector and both folds. P/2 windows and available KSPSAP measurements are in the numeric artifact. Predicted times are search windows, not measured event centers.

## Limits and next check

A genuine unrelated eclipse elsewhere on this star is outside this selected-fold conclusion. This verdict refutes the selected repeating eclipse signal, not every possible binary configuration of the star. An alternate extraction of the same TESS photons tests processing, not recurrence.

## Provenance

The frozen [source packet](../../source-packets/154571577/sources.json) binds FITS paths, source hashes, Gaia metadata and original bulk/fold receipts. [SOURCE-HASHES.json](../SOURCE-HASHES.json) and [SHA256SUMS.json](../SHA256SUMS.json) seal the review artifacts.
