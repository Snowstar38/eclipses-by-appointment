# T037 - TIC 309965535

**Physical verdict:** REFUTED. **Bounded review:** COMPLETE. **Catalogue novelty:** UNKNOWN; four VizieR gates remained unavailable after failed positive controls in the shared catalogue work. The successful scoped primary-table nonmatches do not clear novelty.

## Raw flux, timing, and coverage

The s73 SAP trough near 3300.9 begins after a 0.35 d gap with a roughly -21 ppt raw step. A target-containing TESScut 3x3 and 5x5 background-subtracted extraction lacks the QLP trough while the cutout background changes broadly. Together these spatial and gap facts positively support a background/extraction disturbance in the selected window; corrected-flux suppression alone is not the argument.

- s73 screen 3300.867: raw core deficit 32.0 ppt, side scatter 3.2 ppt, quality-zero core 610, local max gap 0.347 d; exploratory fit midpoint 3300.869.

Cached QLP raw-SAP spans: s14 [1683.37, 1710.18], s20 [1842.51, 1868.81], s26 [2010.28, 2035.11], s40 [2390.65, 2418.85], s47 [2579.81, 2606.94], s53 [2743.99, 2768.97], s60 [2936.90, 2962.59], s73 [3285.80, 3312.65], s74 [3312.86, 3339.57]. Actual finite-cadence and quality-zero counts, endpoints and gaps are in [numeric evidence](lead-numeric.json) and [helper coverage](../helper-coverage.json). Screening times and trapezoid fits are exploratory, not automatically accepted eclipse midpoints. Full-sector and local plots are in this target folder.

## Source, alternative reduction, and Gaia geometry

The Gaia DR3 SB1 orbit has P=54.673012 d. At the screening time 3300.867, the closest edge-on conjunction differs by -6.620 d; linear Gaia covariance gives 3.516 d. This comparison uses a screening time, except where a measured event is separately described, and cannot turn a raw artifact into an eclipse.

Gaia neighbors within 25 arcsec: 3.3 arcsec G=19.55. Target positions and all neighbors to 120 arcsec are in the shared Gaia neighbor receipt; flux ratios alone do not localize a dip. Terra04's target-containing TESScut extraction and background map provide the deciding alternative reduction and spatial contradiction; see helper pixel receipts and plots.

The current MAST footprint lists sectors through 74, no later than cached s74. The footprint response is in [current-sector receipt](../lead-current-sectors.json).

## Limit and next check

The local TESSCut background estimate is approximate, so the spatial test alone cannot exclude every physical signal; combined with the coincident gap/step, this selected trough does not support a target eclipse or clock. Test any future isolated raw target-aperture event away from a background transition.

Source packet SHA-256: `713d8e88d6bcfe2ba3472b86441dd881fc2c8cdd94f8f9654d9ff531a6396b03`. Every QLP FITS read by the numeric script matched the bulk packet SHA-256; paths and hashes are in lead-numeric.json and batch SOURCE-HASHES.json. This is a bounded physical review, not a literature priority claim.
