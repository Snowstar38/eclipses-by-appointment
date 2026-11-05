# T032 - TIC 466098039

**Physical verdict:** REFUTED. **Bounded review:** COMPLETE. **Catalogue novelty:** UNKNOWN; four VizieR gates remained unavailable after failed positive controls in the shared catalogue work. The successful scoped primary-table nonmatches do not clear novelty.

## Raw flux, timing, and coverage

The s94 trough around 3875 follows the same spacecraft-orbit gap morphology as independent targets T035, T038 and T039, with a 0.25 d local gap. The s101 and s102 candidate minima terminate and begin at 1.71 and 1.89 d missing intervals; s104 is another broad baseline/gap variation. Their spacings do not form one 48.47 d same-kind clock. This is positive gap and raw-shape evidence against the selected eclipses.

- s94 screen 3875.050: raw core deficit 3.8 ppt, side scatter 3.5 ppt, quality-zero core 181, local max gap 0.248 d; exploratory fit midpoint 3874.958.
- s101 screen 4112.914: raw core deficit 5.7 ppt, side scatter 2.0 ppt, quality-zero core 341, local max gap 1.708 d; exploratory fit midpoint 4112.931.
- s102 screen 4140.088: raw core deficit 5.3 ppt, side scatter 2.9 ppt, quality-zero core 341, local max gap 1.891 d; exploratory fit midpoint 4140.130.
- s104 screen 4197.354: raw core deficit 5.1 ppt, side scatter 3.9 ppt, quality-zero core 153, local max gap 0.236 d; exploratory fit midpoint 4197.322.

Cached QLP raw-SAP spans: s13 [1653.93, 1682.35], s27 [2036.29, 2060.64], s67 [3126.64, 3154.40], s94 [3856.26, 3882.12], s101 [4100.69, 4126.80], s102 [4127.02, 4151.78], s103 [4152.03, 4178.37], s104 [4178.58, 4205.20]. Actual finite-cadence and quality-zero counts, endpoints and gaps are in [numeric evidence](lead-numeric.json) and [helper coverage](../helper-coverage.json). Screening times and trapezoid fits are exploratory, not automatically accepted eclipse midpoints. Full-sector and local plots are in this target folder.

## Source, alternative reduction, and Gaia geometry

The Gaia DR3 SB1 orbit has P=48.468734 d. At the screening time 4112.914, the closest edge-on conjunction differs by -3.065 d; linear Gaia covariance gives 2.069 d. This comparison uses a screening time, except where a measured event is separately described, and cannot turn a raw artifact into an eclipse.

Gaia neighbors within 25 arcsec: 17.5 arcsec G=20.28. Target positions and all neighbors to 120 arcsec are in the shared Gaia neighbor receipt; flux ratios alone do not localize a dip. An additional pipeline is not required to refute the selected flags where their raw time-series gaps, inconsistent spacings or extraction behavior provide positive contrary evidence.

The current MAST footprint lists sectors through 104, no later than cached s104. The footprint response is in [current-sector receipt](../lead-current-sectors.json).

## Limit and next check

All four retained windows are interrupted or broad; none supports a measured center. Reassess only with a fully observed isolated return to baseline.

Source packet SHA-256: `0f9b03483ab28e33bd17bf530b87871c38c913239f5a222cdef6066616f347b0`. Every QLP FITS read by the numeric script matched the bulk packet SHA-256; paths and hashes are in lead-numeric.json and batch SOURCE-HASHES.json. This is a bounded physical review, not a literature priority claim.
