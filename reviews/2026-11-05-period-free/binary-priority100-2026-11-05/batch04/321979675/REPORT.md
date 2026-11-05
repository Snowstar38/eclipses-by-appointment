# T040 - TIC 321979675

**Physical verdict:** REFUTED. **Bounded review:** COMPLETE. **Catalogue novelty:** UNKNOWN; four VizieR gates remained unavailable after failed positive controls in the shared catalogue work. The successful scoped primary-table nonmatches do not clear novelty.

## Raw flux, timing, and coverage

The s29 selected six-point decline occurs on the edge of a large flare-like excursion and before a 3.54 d interruption; it is not an isolated eclipse against a stable baseline. The s96 broad shallow trough occurs beside a 0.22 d gap and sector-scale reset, 1825 d later with no supported same-kind clock. These actual raw shapes positively refute the selected eclipse interpretation.

- s29 screen 2099.744: raw core deficit 64.7 ppt, side scatter 3.5 ppt, quality-zero core 6, local max gap 0.028 d; exploratory fit midpoint 2099.743.
- s96 screen 3926.346: raw core deficit 4.3 ppt, side scatter 1.9 ppt, quality-zero core 579, local max gap 0.220 d; exploratory fit midpoint 3924.963.

Cached QLP raw-SAP spans: s2 [1354.12, 1381.49], s29 [2088.24, 2114.43], s69 [3182.35, 3208.14], s96 [3907.77, 3933.45], s103 [4152.03, 4178.37], s104 [4178.58, 4205.20]. Actual finite-cadence and quality-zero counts, endpoints and gaps are in [numeric evidence](lead-numeric.json) and [helper coverage](../helper-coverage.json). Screening times and trapezoid fits are exploratory, not automatically accepted eclipse midpoints. Full-sector and local plots are in this target folder.

## Source, alternative reduction, and Gaia geometry

The Gaia DR3 SB1 orbit has P=45.610259 d. At the screening time 3926.346, the closest edge-on conjunction differs by 13.009 d; linear Gaia covariance gives 2.602 d. This comparison uses a screening time, except where a measured event is separately described, and cannot turn a raw artifact into an eclipse.

Gaia neighbors within 25 arcsec: 18.1 arcsec G=20.98. Target positions and all neighbors to 120 arcsec are in the shared Gaia neighbor receipt; flux ratios alone do not localize a dip. An additional pipeline is not required to refute the selected flags where their raw time-series gaps, inconsistent spacings or extraction behavior provide positive contrary evidence.

The current MAST footprint lists s106 beyond cached s104; this review has not treated that sector as a null. The footprint response is in [current-sector receipt](../lead-current-sectors.json).

## Limit and next check

Neither flagged occasion supports a precise center or physical eclipse depth. Require an isolated repeat independent of flare or sector boundary.

Source packet SHA-256: `037f2b83367d7c19cf269b8bc045df0e20f14c7eb24aba356130342489e01ec5`. Every QLP FITS read by the numeric script matched the bulk packet SHA-256; paths and hashes are in lead-numeric.json and batch SOURCE-HASHES.json. This is a bounded physical review, not a literature priority claim.
