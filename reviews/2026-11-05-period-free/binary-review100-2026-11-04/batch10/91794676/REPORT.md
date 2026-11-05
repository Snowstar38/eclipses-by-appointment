# H096 — TIC 91794676

Physical verdict for the selected fold: **REFUTED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; central catalogue gates remain unavailable.

Gaia DR3 5348137467915602304 is an SB1 with spectroscopic period 28.56339 d. This is selection context, not a measured eclipse clock. The screening solution is P=28.53230 d, duration 0.320 d, z=3.40, depth 953 ppm; its P/2 test is 14.27472 d, z=4.30. Neither screening period is adopted as a photometric measurement.

## Raw evidence and interpretation

The s90 predicted depression is on a multi-day fading tail and local sides differ by about 10.2 ppt. S63 and s64 have densely sampled, nearly flat predicted cores (about 0.1 ppt). S99 and s100 predictions fall in coverage gaps. The selected 28.532 d fold is driven by the s90 trend rather than a recurrent eclipse.

All cached sectors were inspected in raw QLP SAP flux with QUALITY=0. Actual sector coverage (BTJD): s010 [1571.72,1595.64], n=870, cadence=30.0 min; s037 [2309.21,2332.33], n=2751, cadence=10.0 min; s063 [3014.48,3039.58], n=10478, cadence=3.3 min; s064 [3041.18,3067.62], n=10673, cadence=3.3 min; s090 [3747.41,3774.97], n=11185, cadence=3.3 min; s099 [4046.25,4071.00], n=7195, cadence=3.3 min; s100 [4074.54,4098.28], n=8007, cadence=3.3 min. The P-screened occasions, with observed core and separate left/right baseline counts, are: s010 1576.85: core 10, L/R 23/24, 1.0 ppt; s037 2318.69: core 45, L/R 68/0, -0.1 ppt; s063 3031.99: core 138, L/R 208/208, 0.1 ppt; s064 3060.53: core 136, L/R 208/168, 0.1 ppt; s090 3773.83: core 126, L/R 202/185, 5.0 ppt; s099 4059.16: core 0, L/R 0/0, unmeasurable; s100 4087.69: core 0, L/R 0/207, unmeasurable. These local medians are diagnostics, not fitted eclipse depths. Missing cadences and internal gaps are recorded in [raw-fold.json](raw-fold.json); [raw-fold.png](raw-fold.png) shows every full sector and both folds. P/2 windows and available KSPSAP measurements are in the numeric artifact. Predicted times are search windows, not measured event centers.

## Limits and next check

Pixel or independent aperture data could characterize the long s90 excursion, which is separate from the rejected fold. This verdict refutes the selected repeating eclipse signal, not every possible binary configuration of the star. An alternate extraction of the same TESS photons tests processing, not recurrence.

## Provenance

The frozen [source packet](../../source-packets/91794676/sources.json) binds FITS paths, source hashes, Gaia metadata and original bulk/fold receipts. [SOURCE-HASHES.json](../SOURCE-HASHES.json) and [SHA256SUMS.json](../SHA256SUMS.json) seal the review artifacts.
