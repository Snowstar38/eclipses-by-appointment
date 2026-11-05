# T036 - TIC 237212952

**Physical verdict:** PLAUSIBLE. **Bounded review:** COMPLETE. **Catalogue novelty:** UNKNOWN; four VizieR gates remained unavailable after failed positive controls in the shared catalogue work. The successful scoped primary-table nonmatches do not clear novelty.

## Raw flux, timing, and coverage

s85 has an approximately 12 ppt broad depression around 3625.1 with an extended low interval and recovery. Other s85 troughs near 3611, 3617 and 3630 differ in shape, and several lie beside gaps; their 5-14 d intervals do not establish same-kind 54.23 d eclipses. The main broad event remains an insecure eclipse interpretation, so the other troughs do not justify refuting all astrophysical dips.

- s85 screen 3625.140: raw core deficit 12.1 ppt, side scatter 2.8 ppt, quality-zero core 691, local max gap 0.510 d; exploratory fit midpoint 3625.141.
- s85 screen 3630.292: raw core deficit 4.2 ppt, side scatter 2.0 ppt, quality-zero core 207, local max gap 0.220 d; exploratory fit midpoint 3630.203.
- s85 screen 3611.294: raw core deficit 7.8 ppt, side scatter 6.6 ppt, quality-zero core 207, local max gap 0.002 d; exploratory fit midpoint 3611.627.
- s85 screen 3616.878: raw core deficit 7.0 ppt, side scatter 2.4 ppt, quality-zero core 117, local max gap 0.220 d; exploratory fit midpoint 3616.838.

Cached QLP raw-SAP spans: s14 [1683.36, 1710.18], s15 [1711.39, 1737.39], s16 [1738.66, 1763.30], s17 [1764.70, 1789.68], s18 [1790.68, 1815.01], s19 [1816.10, 1841.14], s20 [1842.51, 1868.80], s22 [1899.32, 1926.47], s23 [1928.11, 1954.86], s24 [1955.80, 1982.26], s25 [1983.66, 2009.28], s40 [2390.66, 2418.85], s41 [2419.99, 2446.57], s47 [2579.80, 2606.93], s48 [2607.93, 2635.98], s49 [2637.48, 2664.31], s50 [2665.27, 2691.50], s52 [2718.63, 2743.07], s53 [2744.00, 2768.98], s54 [2769.90, 2796.12], s55 [2797.10, 2824.26], s56 [2825.25, 2853.14], s57 [2853.35, 2882.11], s59 [2910.26, 2936.69], s60 [2936.90, 2962.58], s73 [3285.80, 3312.65], s74 [3312.86, 3339.57], s75 [3339.78, 3367.48], s76 [3367.69, 3394.78], s77 [3395.48, 3423.55], s78 [3434.26, 3449.51], s79 [3452.53, 3479.67], s80 [3479.89, 3506.34], s82 [3533.39, 3559.25], s83 [3559.42, 3584.37], s84 [3584.59, 3610.34], s85 [3610.55, 3636.04], s86 [3636.26, 3662.83]. Actual finite-cadence and quality-zero counts, endpoints and gaps are in [numeric evidence](lead-numeric.json) and [helper coverage](../helper-coverage.json). Screening times and trapezoid fits are exploratory, not automatically accepted eclipse midpoints. Full-sector and local plots are in this target folder.

## Source, alternative reduction, and Gaia geometry

The Gaia DR3 SB1 orbit has P=54.226342 d. At the screening time 3625.140, the closest edge-on conjunction differs by -9.180 d; linear Gaia covariance gives 17.080 d. This comparison uses a screening time, except where a measured event is separately described, and cannot turn a raw artifact into an eclipse.

Gaia neighbors within 25 arcsec: none within 25 arcsec in the shared Gaia cone. Target positions and all neighbors to 120 arcsec are in the shared Gaia neighbor receipt; flux ratios alone do not localize a dip. Raw SAP morphology was checked against the available QLP alternate flux where present; no alternative reduction establishes a recurring eclipse. This missing check is retained in the limitation rather than used as refutation.

The current MAST footprint lists sectors through 86, no later than cached s86. The footprint response is in [current-sector receipt](../lead-current-sectors.json).

## Limit and next check

One sector contains several broad changing-baseline troughs but no supported Gaia-period timing or secure repeat. The quick TESScut has a cropped zero-valued half; its aperture statistic is invalid and cannot act as an independent null or source localization. Obtain a fully bracketed same-kind return and a valid spatial difference image with a stable local baseline.

Source packet SHA-256: `88bb0a79c878edafe8273f3c01cd4218bbf40b0d2741c6d890832034238d6e73`. Every QLP FITS read by the numeric script matched the bulk packet SHA-256; paths and hashes are in lead-numeric.json and batch SOURCE-HASHES.json. This is a bounded physical review, not a literature priority claim.
