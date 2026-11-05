# T039 - TIC 280866822

**Physical verdict:** REFUTED. **Bounded review:** COMPLETE. **Catalogue novelty:** UNKNOWN; four VizieR gates remained unavailable after failed positive controls in the shared catalogue work. The successful scoped primary-table nonmatches do not clear novelty.

## Raw flux, timing, and coverage

The sole s94 3875.1 trough is broad and interrupted by a 0.25 d gap, matching the timing and morphology of the s94 depression in unrelated T032, T035 and T038. The local raw baseline changes across the window rather than making a stable isolated eclipse.

- s94 screen 3875.119: raw core deficit 5.0 ppt, side scatter 1.7 ppt, quality-zero core 177, local max gap 0.255 d; exploratory fit midpoint 3874.980.

Cached QLP raw-SAP spans: s4 [1410.93, 1436.82], s11 [1596.78, 1623.87], s12 [1624.97, 1652.53], s13 [1653.93, 1682.35], s27 [2036.28, 2060.64], s31 [2144.52, 2169.94], s34 [2228.75, 2254.06], s38 [2333.86, 2360.55], s39 [2361.78, 2389.71], s61 [2962.79, 2988.22], s64 [3041.11, 3068.03], s65 [3068.74, 3096.59], s66 [3097.67, 3126.43], s67 [3126.64, 3154.40], s88 [3690.15, 3717.92], s93 [3829.85, 3856.05], s94 [3856.26, 3882.12]. Actual finite-cadence and quality-zero counts, endpoints and gaps are in [numeric evidence](lead-numeric.json) and [helper coverage](../helper-coverage.json). Screening times and trapezoid fits are exploratory, not automatically accepted eclipse midpoints. Full-sector and local plots are in this target folder.

## Source, alternative reduction, and Gaia geometry

The Gaia DR3 SB1 orbit has P=50.140145 d. At the screening time 3875.119, the closest edge-on conjunction differs by 8.220 d; linear Gaia covariance gives 4.030 d. This comparison uses a screening time, except where a measured event is separately described, and cannot turn a raw artifact into an eclipse.

Gaia neighbors within 25 arcsec: 14.3 arcsec G=18.88; 17.5 arcsec G=21.18. Target positions and all neighbors to 120 arcsec are in the shared Gaia neighbor receipt; flux ratios alone do not localize a dip. An additional pipeline is not required to refute the selected flags where their raw time-series gaps, inconsistent spacings or extraction behavior provide positive contrary evidence.

The current MAST footprint lists sectors through 94, no later than cached s94. The footprint response is in [current-sector receipt](../lead-current-sectors.json).

## Limit and next check

There is no measured same-kind return at the 50.14 d Gaia period. Reopen if a future sector shows a fully bracketed event.

Source packet SHA-256: `2d4fe84daec1029469f2113b28fb965a869f26d393c87ccb2236cd294aef5d7c`. Every QLP FITS read by the numeric script matched the bulk packet SHA-256; paths and hashes are in lead-numeric.json and batch SOURCE-HASHES.json. This is a bounded physical review, not a literature priority claim.
