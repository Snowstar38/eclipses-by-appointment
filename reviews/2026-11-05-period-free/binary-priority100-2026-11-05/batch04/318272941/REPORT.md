# T038 - TIC 318272941

**Physical verdict:** REFUTED. **Bounded review:** COMPLETE. **Catalogue novelty:** UNKNOWN; four VizieR gates remained unavailable after failed positive controls in the shared catalogue work. The successful scoped primary-table nonmatches do not clear novelty.

## Raw flux, timing, and coverage

The sole s94 candidate is the same broad, gap-adjacent ~3875 depression seen in several unrelated s94 targets. Its raw trough extends across a 0.25 d gap and lacks an isolated stable baseline; no second event follows the 57.16 d Gaia orbit. The actual gap/shape supports a spacecraft-origin false flag.

- s94 screen 3874.943: raw core deficit 4.3 ppt, side scatter 1.4 ppt, quality-zero core 188, local max gap 0.248 d; exploratory fit midpoint 3874.905.

Cached QLP raw-SAP spans: s12 [1624.97, 1652.53], s13 [1653.93, 1682.35], s27 [2036.28, 2060.64], s39 [2361.78, 2389.71], s67 [3126.64, 3154.40], s93 [3829.86, 3856.05], s94 [3856.26, 3882.12]. Actual finite-cadence and quality-zero counts, endpoints and gaps are in [numeric evidence](lead-numeric.json) and [helper coverage](../helper-coverage.json). Screening times and trapezoid fits are exploratory, not automatically accepted eclipse midpoints. Full-sector and local plots are in this target folder.

## Source, alternative reduction, and Gaia geometry

The Gaia DR3 SB1 orbit has P=57.158215 d. At the screening time 3874.943, the closest edge-on conjunction differs by -5.523 d; linear Gaia covariance gives 11.146 d. This comparison uses a screening time, except where a measured event is separately described, and cannot turn a raw artifact into an eclipse.

Gaia neighbors within 25 arcsec: none within 25 arcsec in the shared Gaia cone. Target positions and all neighbors to 120 arcsec are in the shared Gaia neighbor receipt; flux ratios alone do not localize a dip. An additional pipeline is not required to refute the selected flags where their raw time-series gaps, inconsistent spacings or extraction behavior provide positive contrary evidence.

The current MAST footprint lists sectors through 94, no later than cached s94. The footprint response is in [current-sector receipt](../lead-current-sectors.json).

## Limit and next check

One disrupted window only; no reliable eclipse center. Seek a clean repeat in a later sector.

Source packet SHA-256: `1a380424129b719f450966bd68618980cf4ed4a19a70d204d41a88f756c96fc1`. Every QLP FITS read by the numeric script matched the bulk packet SHA-256; paths and hashes are in lead-numeric.json and batch SOURCE-HASHES.json. This is a bounded physical review, not a literature priority claim.
