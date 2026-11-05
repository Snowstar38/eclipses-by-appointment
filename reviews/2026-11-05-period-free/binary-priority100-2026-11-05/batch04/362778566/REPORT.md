# T033 - TIC 362778566

**Physical verdict:** PLAUSIBLE. **Bounded review:** COMPLETE. **Catalogue novelty:** UNKNOWN; four VizieR gates remained unavailable after failed positive controls in the shared catalogue work. The successful scoped primary-table nonmatches do not clear novelty.

## Raw flux, timing, and coverage

s80 contains a coherent roughly 6-8 ppt, roughly 2 d flat-bottomed deficit around BTJD 3501.945. A target-containing TESScut aperture reproduces it. s91 starts in a roughly 1% low state 0.434 d before the Gaia-period predicted center at 3775.870 and recovers over the following day; its target-containing TESScut apertures reproduce the partial occasion. The missing s91 ingress and baseline permit a sector-start reset alternative.

- s80 screen 3501.681: raw core deficit 6.6 ppt, side scatter 2.4 ppt, quality-zero core 691, local max gap 2.039 d; exploratory fit midpoint 3501.945.

Cached QLP raw-SAP spans: s80 [3479.89, 3506.34], s91 [3775.29, 3802.76], s92 [3802.97, 3829.65]. Actual finite-cadence and quality-zero counts, endpoints and gaps are in [numeric evidence](lead-numeric.json) and [helper coverage](../helper-coverage.json). Screening times and trapezoid fits are exploratory, not automatically accepted eclipse midpoints. Full-sector and local plots are in this target folder.

## Source, alternative reduction, and Gaia geometry

The Gaia DR3 SB1 orbit has P=54.785059 d. At the screening time 3501.681, the closest edge-on conjunction differs by -0.869 d; linear Gaia covariance gives 1.051 d. This comparison uses a screening time, except where a measured event is separately described, and cannot turn a raw artifact into an eclipse. The exploratory fitted s80 midpoint 3501.945 and conditional +5 Gaia cycles predict 3775.870 in s91; see lead-phase.json and lead-aliases.json. This is not a unique photometric period.

Gaia neighbors within 25 arcsec: 3.7 arcsec G=20.29; 3.8 arcsec G=20.18; 8.4 arcsec G=20.71; 9.6 arcsec G=20.24; 9.7 arcsec G=20.32; 10.6 arcsec G=19.98; 10.9 arcsec G=17.20; 11.2 arcsec G=20.25; plus 38 additional crowded-field rows in the shared cone. Target positions and all neighbors to 120 arcsec are in the shared Gaia neighbor receipt; flux ratios alone do not localize a dip. Terra04's background-subtracted TESScut 3x3/5x5 light curves reproduce the s80 dip and the s91 partial low state with real target flux; both reductions use the same TESS photons. The deficit peaks near the target in coarse pixels; the crowded field prevents a definitive unique-source claim.

The current MAST footprint lists sectors through 92, no later than cached s92. The footprint response is in [current-sector receipt](../lead-current-sectors.json).

## Limit and next check

The s80-to-s91 separation is conditional on five Gaia cycles; n=3/4/5 remain untested. s92 flat core coverage contradicts n=6/9 and disfavors n=8 under the assumed phase, duration and depth; n=8 has only partial core coverage (424 cadences, first offset -0.383 d for a +/-0.6 d core), n=7 falls in a gap, and n=10 is at a sector-start low state. The s80 WCS target has flux, but nearby sources remain a source-attribution limit. Capture a fully bracketed repeat in a future sector and resolve the 18.8 arcsec G=14.89 neighbor with event difference imaging or higher-resolution photometry.

Source packet SHA-256: `e24c4ef63f09be8f5e67a19d742851e2c886bb52ca0ff2294a883028dfbca764`. Every QLP FITS read by the numeric script matched the bulk packet SHA-256; paths and hashes are in lead-numeric.json and batch SOURCE-HASHES.json. This is a bounded physical review, not a literature priority claim.
