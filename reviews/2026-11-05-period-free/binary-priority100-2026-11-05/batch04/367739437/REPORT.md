# T031 - TIC 367739437

**Physical verdict:** REFUTED. **Bounded review:** COMPLETE. **Catalogue novelty:** UNKNOWN; four VizieR gates remained unavailable after failed positive controls in the shared catalogue work. The successful scoped primary-table nonmatches do not clear novelty.

## Raw flux, timing, and coverage

The s25 millimagnitude fluctuations near 1985.45, 2006.53 and 2007.55 sit in an irregular, gently varying raw baseline; their shallow few-point troughs do not have stable isolated ingress/egress and two are only 1.02 d apart. The larger s86 selected windows lie on a pronounced ramp, step and an interrupted baseline, with no return to a stable local level. The actual raw shapes and discontinuities positively refute these selected eclipse flags; incompatible spacings are supporting context, not a blanket exclusion of other eclipses.

- s25 screen 2006.530: raw core deficit 4.5 ppt, side scatter 2.7 ppt, quality-zero core 10, local max gap 0.042 d; exploratory fit midpoint 2006.519.
- s25 screen 2007.551: raw core deficit 4.4 ppt, side scatter 2.3 ppt, quality-zero core 9, local max gap 0.062 d; exploratory fit midpoint 2007.527.
- s25 screen 1985.447: raw core deficit 3.5 ppt, side scatter 1.2 ppt, quality-zero core 6, local max gap 0.083 d; exploratory fit midpoint 1985.458.
- s86 screen 3636.841: raw core deficit 40.6 ppt, side scatter 12.3 ppt, quality-zero core 103, local max gap 0.002 d; exploratory fit midpoint 3636.848.
- s86 screen 3638.459: raw core deficit 5.1 ppt, side scatter 15.1 ppt, quality-zero core 103, local max gap 0.005 d; exploratory fit midpoint 3638.442.
- s86 screen 3650.167: raw core deficit 44.2 ppt, side scatter 42.0 ppt, quality-zero core 146, local max gap 0.498 d; exploratory fit midpoint 3650.179.
- s86 screen 3652.438: raw core deficit 7.5 ppt, side scatter 14.1 ppt, quality-zero core 103, local max gap 0.005 d; exploratory fit midpoint 3652.430.

Cached QLP raw-SAP spans: s14 [1683.37, 1710.18], s15 [1711.39, 1737.39], s18 [1790.68, 1815.01], s19 [1816.10, 1841.14], s20 [1842.51, 1868.80], s21 [1870.45, 1897.76], s25 [1983.66, 2009.28], s26 [2010.28, 2035.11], s40 [2390.65, 2418.85], s41 [2419.99, 2446.57], s47 [2579.80, 2606.94], s48 [2607.94, 2635.98], s52 [2718.63, 2743.07], s53 [2744.00, 2768.97], s55 [2797.10, 2824.26], s59 [2910.26, 2936.69], s60 [2936.90, 2962.58], s73 [3285.80, 3312.65], s74 [3312.86, 3339.57], s75 [3339.78, 3367.48], s78 [3434.26, 3449.51], s79 [3452.53, 3479.67], s81 [3506.55, 3533.17], s82 [3533.39, 3559.24], s86 [3636.26, 3662.83]. Actual finite-cadence and quality-zero counts, endpoints and gaps are in [numeric evidence](lead-numeric.json) and [helper coverage](../helper-coverage.json). Screening times and trapezoid fits are exploratory, not automatically accepted eclipse midpoints. Full-sector and local plots are in this target folder.

## Source, alternative reduction, and Gaia geometry

The Gaia DR3 SB1 orbit has P=49.290211 d. At the screening time 2006.530, the closest edge-on conjunction differs by -4.733 d; linear Gaia covariance gives 3.030 d. This comparison uses a screening time, except where a measured event is separately described, and cannot turn a raw artifact into an eclipse.

Gaia neighbors within 25 arcsec: 16.7 arcsec G=18.80; 20.0 arcsec G=20.62; 22.2 arcsec G=19.61. Target positions and all neighbors to 120 arcsec are in the shared Gaia neighbor receipt; flux ratios alone do not localize a dip. An additional pipeline is not required to refute the selected flags where their raw time-series gaps, inconsistent spacings or extraction behavior provide positive contrary evidence.

The current MAST footprint lists sectors through 86, no later than cached s86. The footprint response is in [current-sector receipt](../lead-current-sectors.json).

## Limit and next check

No secure isolated eclipse center or period can be measured from these flags. Reopen if a clean isolated same-kind event appears in future data.

Source packet SHA-256: `0f4a012dfcd406077ea6007fb6d0d62a2b912972bba02bce13dd3eb9ae82b5f5`. Every QLP FITS read by the numeric script matched the bulk packet SHA-256; paths and hashes are in lead-numeric.json and batch SOURCE-HASHES.json. This is a bounded physical review, not a literature priority claim.
