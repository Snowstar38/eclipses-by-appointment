# H100 — TIC 390853987

Physical verdict for the selected fold: **PLAUSIBLE**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; central catalogue gates remain unavailable.

Gaia DR3 466214478035295744 is an SB1 with spectroscopic period 35.06746 d. This is selection context, not a measured eclipse clock. The screening solution is P=35.05200 d, duration 0.072 d, z=4.16, depth 5187 ppm; its P/2 test is 17.45430 d, z=2.35. Neither screening period is adopted as a photometric measurement.

## Raw evidence and interpretation

A distinct s86 dip near BTJD 3640.16 reaches about 6.8 ppt against local flanks and survives in DET and SYS_RM columns. SAP_X shifts by roughly 0.025 pixel over the dip, exactly returning at egress; this may indicate an aperture response or an off-target eclipsing source. A crude s86 TESScut difference is dominated by spatially broad background change and does not localize the deficit. The well-covered s58 predicted core is flat, contradicting an exact 35.052 d recurrence, while s19 has only three core cadences and lacks a left baseline. Current sector-footprint follow-up found s59 ends at BTJD 2936.690, 2.43 d before its screened prediction, and s85 ends at 3636.048, 4.11 d before the s86 prediction; neither supplies another expected occasion. A real isolated event remains possible; the fold period is not a measured eclipse period.

All cached sectors were inspected in raw QLP SAP flux with QUALITY=0. Actual sector coverage (BTJD): s018 [1792.04,1814.91], n=993, cadence=30.0 min; s019 [1817.33,1840.97], n=903, cadence=30.0 min; s058 [2882.39,2910.01], n=11515, cadence=3.3 min; s086 [3636.51,3662.76], n=5553, cadence=3.3 min. The P-screened occasions, with observed core and separate left/right baseline counts, are: s019 1817.46: core 3, L/R 0/18, 0.0 ppt; s058 2904.07: core 31, L/R 81/173, -0.2 ppt; s086 3640.16: core 29, L/R 113/157, 6.8 ppt. These local medians are diagnostics, not fitted eclipse depths. Missing cadences and internal gaps are recorded in [raw-fold.json](raw-fold.json); [raw-fold.png](raw-fold.png) shows every full sector and both folds. P/2 windows and available KSPSAP measurements are in the numeric artifact. The s86 reduction and pixel checks are in [helper-detail-086.png](helper-detail-086.png), [helper-pixel.txt](helper-pixel.txt) and [helper-pixel-difference.png](helper-pixel-difference.png); current s59/s85 coverage is in [followup-newsectors.json](followup-newsectors.json). Predicted times are search windows, not measured event centers.

## Limits and next check

Localize the s86 deficit with background-controlled difference pixels and capable neighbors, then seek another observing occasion and test integer-cycle aliases. No binary period, primary epoch or depth is promoted from the insecure single event. An alternate extraction of the same TESS photons tests processing, not recurrence.

## Provenance

The frozen [source packet](../../source-packets/390853987/sources.json) binds FITS paths, source hashes, Gaia metadata and original bulk/fold receipts. [SOURCE-HASHES.json](../SOURCE-HASHES.json) and [SHA256SUMS.json](../SHA256SUMS.json) seal the review artifacts.
