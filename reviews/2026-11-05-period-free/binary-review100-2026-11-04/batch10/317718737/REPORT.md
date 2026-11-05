# H094 — TIC 317718737

Physical verdict for the selected fold: **PLAUSIBLE**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; central catalogue gates remain unavailable.

Gaia DR3 2991561068038075904 is an SB1 with spectroscopic period 41.88212 d. This is selection context, not a measured eclipse clock. The screening solution is P=41.84028 d, duration 0.120 d, z=4.40, depth 1142 ppm; its P/2 test is 20.92146 d, z=3.37. Neither screening period is adopted as a photometric measurement.

## Raw evidence and interpretation

Two shallow local depressions coincide with P-screened windows: 1.4 ppt in s33 and 1.4 ppt in s87. S33 is also about 1.2 ppt in KSPSAP, an alternative extraction of the same photons. The s6 core has only six cadences and no right baseline after a gap, so it is not a sensitive null. A newly fetched sector-108 3x3 TESScut aperture has 52 core and 129/130 flank samples around the exact P-screening prediction at 4316.47026 and is flat (-0.02 ppt), but the individual flank MAD is about 1.2 ppt and time-correlated noise is not calibrated; this challenges rather than decisively excludes a 1.4 ppt event. WCS places the target at pixel (2.79, 2.26), inside that aperture, whose median total flux is 6815 e/s. Sector 107 is 0.54 ppt amid a slope; sector 98 has only about 7 e/s in the central 3x3 despite WCS placement and is unusable as a target measurement. The weak earlier profiles could be genuine dips at another integer alias or be variability. Their centers, source and cycle count remain insecure.

All cached sectors were inspected in raw QLP SAP flux with QUALITY=0. Actual sector coverage (BTJD): s006 [1468.62,1490.02], n=888, cadence=30.0 min; s033 [2201.80,2227.33], n=3378, cadence=10.0 min; s087 [3664.37,3689.71], n=10166, cadence=3.3 min. The P-screened occasions, with observed core and separate left/right baseline counts, are: s006 1471.33: core 6, L/R 19/0, -0.3 ppt; s033 2224.46: core 18, L/R 57/57, 1.4 ppt; s087 3688.87: core 35, L/R 145/91, 1.4 ppt. These local medians are diagnostics, not fitted eclipse depths. Missing cadences and internal gaps are recorded in [raw-fold.json](raw-fold.json); [raw-fold.png](raw-fold.png) shows every full sector and both folds. P/2 windows and available KSPSAP measurements are in the numeric artifact. The new sector cutout measurements and archive hashes are in [helper-newsectors.txt](helper-newsectors.txt), [wcs-placement.json](wcs-placement.json) and [helper-newsectors.png](helper-newsectors.png). Predicted times are search windows, not measured event centers.

## Limits and next check

Localize the s33/s87 depressions, measure their centers and test integer aliases against newer coverage before assigning an orbital period. No binary period, primary epoch or depth is promoted from these insecure occasions. An alternate extraction of the same TESS photons tests processing, not recurrence.

## Provenance

The frozen [source packet](../../source-packets/317718737/sources.json) binds FITS paths, source hashes, Gaia metadata and original bulk/fold receipts. [SOURCE-HASHES.json](../SOURCE-HASHES.json) and [SHA256SUMS.json](../SHA256SUMS.json) seal the review artifacts.
