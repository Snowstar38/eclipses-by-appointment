# T035 - TIC 253889547

**Physical verdict:** REFUTED. **Bounded review:** COMPLETE. **Catalogue novelty:** UNKNOWN; four VizieR gates remained unavailable after failed positive controls in the shared catalogue work. The successful scoped primary-table nonmatches do not clear novelty.

## Raw flux, timing, and coverage

The s94 broad trough around 3874.6 is accompanied by a 0.25 d spacecraft gap and long raw baseline drift. The same s94 depression appears at nearly the same time in T032, T038 and T039, which have different sky positions and Gaia periods. The common timing is supporting context; the actual broad raw shape and gap supply the contrary evidence.

- s94 screen 3874.628: raw core deficit 3.5 ppt, side scatter 5.1 ppt, quality-zero core 170, local max gap 0.248 d; exploratory fit midpoint 3874.871.

Cached QLP raw-SAP spans: s13 [1653.97, 1682.35], s67 [3126.64, 3154.40], s94 [3856.26, 3882.11]. Actual finite-cadence and quality-zero counts, endpoints and gaps are in [numeric evidence](lead-numeric.json) and [helper coverage](../helper-coverage.json). Screening times and trapezoid fits are exploratory, not automatically accepted eclipse midpoints. Full-sector and local plots are in this target folder.

## Source, alternative reduction, and Gaia geometry

The Gaia DR3 SB1 orbit has P=45.581466 d. At the screening time 3874.628, the closest edge-on conjunction differs by -8.020 d; linear Gaia covariance gives 3.214 d. This comparison uses a screening time, except where a measured event is separately described, and cannot turn a raw artifact into an eclipse.

Gaia neighbors within 25 arcsec: 13.8 arcsec G=20.20; 16.4 arcsec G=17.03; 16.8 arcsec G=20.73; 17.9 arcsec G=18.25; 17.9 arcsec G=19.72; 19.9 arcsec G=19.13; 19.9 arcsec G=18.55; 20.7 arcsec G=18.71; plus 6 additional crowded-field rows in the shared cone. Target positions and all neighbors to 120 arcsec are in the shared Gaia neighbor receipt; flux ratios alone do not localize a dip. An additional pipeline is not required to refute the selected flags where their raw time-series gaps, inconsistent spacings or extraction behavior provide positive contrary evidence.

The current MAST footprint lists sectors through 94, no later than cached s94. The footprint response is in [current-sector receipt](../lead-current-sectors.json).

## Limit and next check

Only one disrupted window exists; no measured eclipse clock. Revisit an isolated event away from the spacecraft gap.

Source packet SHA-256: `340b2bddb23f713e0c03d186ffa1552fd32801be046f229b2b3309fa8a37396f`. Every QLP FITS read by the numeric script matched the bulk packet SHA-256; paths and hashes are in lead-numeric.json and batch SOURCE-HASHES.json. This is a bounded physical review, not a literature priority claim.
