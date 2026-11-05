# T034 - TIC 14949343

**Physical verdict:** REFUTED. **Bounded review:** COMPLETE. **Catalogue novelty:** UNKNOWN; four VizieR gates remained unavailable after failed positive controls in the shared catalogue work. The successful scoped primary-table nonmatches do not clear novelty.

## Raw flux, timing, and coverage

The s81 raw aperture divides into two widely separated flux branches throughout the selected window, and the full sector shows a large decline, gap and recovery. Its 0.06 d candidate dip is a few points on the changing upper branch while the lower branch persists outside it. That pattern is positive extraction/contamination evidence against an isolated eclipse.

- s81 screen 3510.588: raw core deficit 1.1 ppt, side scatter 7.5 ppt, quality-zero core 25, local max gap 0.002 d; exploratory fit midpoint 3510.580.

Cached QLP raw-SAP spans: s14 [1683.36, 1710.18], s15 [1711.38, 1737.39], s41 [2419.99, 2446.58], s55 [2797.10, 2824.26], s81 [3506.55, 3533.18], s82 [3533.39, 3559.25]. Actual finite-cadence and quality-zero counts, endpoints and gaps are in [numeric evidence](lead-numeric.json) and [helper coverage](../helper-coverage.json). Screening times and trapezoid fits are exploratory, not automatically accepted eclipse midpoints. Full-sector and local plots are in this target folder.

## Source, alternative reduction, and Gaia geometry

The Gaia DR3 SB1 orbit has P=43.943597 d. At the screening time 3510.588, the closest edge-on conjunction differs by -2.026 d; linear Gaia covariance gives 6.820 d. This comparison uses a screening time, except where a measured event is separately described, and cannot turn a raw artifact into an eclipse.

Gaia neighbors within 25 arcsec: 16.5 arcsec G=20.82; 16.9 arcsec G=19.98; 17.1 arcsec G=21.06; 17.7 arcsec G=17.84; 19.4 arcsec G=20.42; 20.0 arcsec G=20.35; 20.8 arcsec G=21.15; 20.9 arcsec G=21.12; plus 4 additional crowded-field rows in the shared cone. Target positions and all neighbors to 120 arcsec are in the shared Gaia neighbor receipt; flux ratios alone do not localize a dip. An additional pipeline is not required to refute the selected flags where their raw time-series gaps, inconsistent spacings or extraction behavior provide positive contrary evidence.

The current MAST footprint lists sectors through 82, no later than cached s82. The footprint response is in [current-sector receipt](../lead-current-sectors.json).

## Limit and next check

No unique astrophysical deficit or timing center is supported. A future clean aperture could test for independent periodic dips.

Source packet SHA-256: `35245d735837678030dab72e67a4282d34f11700e17f1ad9aef39c17eb1bb46c`. Every QLP FITS read by the numeric script matched the bulk packet SHA-256; paths and hashes are in lead-numeric.json and batch SOURCE-HASHES.json. This is a bounded physical review, not a literature priority claim.
