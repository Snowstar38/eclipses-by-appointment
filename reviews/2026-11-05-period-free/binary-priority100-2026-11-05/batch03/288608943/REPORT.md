# T027 — TIC 288608943

**Physical verdict:** REFUTED. **Full bounded review:** COMPLETE. **Catalogue novelty:** UNKNOWN; shared catalogue checks lack four VizieR gates (VSX, ASAS-SN, Kostov 2025 tables 3 and 4) after failed positive controls. This is not a negative catalogue match.

## Raw event and timing evidence

s81 flux slides downward for days into gaps near 3518 and 3531, 13.4 d apart; the gaps are 1.49 and 0.82 d, followed by +58 and +38 ppt resets. s73 has a similar disturbed region. The two s81 structures track TESS downlink spacing, not the Gaia 53.46 d same-kind orbit.

Measured eclipse period: none supported. Epoch BTJD: none supported. Depth: none supported. Screening times in the source packet are not measured centers. See [numeric review](lead-numeric.json), [raw panels](lead-raw-01.png), [sector panels](lead-sector-01.png), and batch [gap evidence](../lead-gap-evidence.json).

## Attribution, reduction and orbit

Gaia DR3 2296723183033595392 has a spectroscopic orbit P=53.459473 d. At the evaluated event/screen epoch, the closest edge-on conjunction offset is -4.146 d, with a 1.858 d linear Gaia-covariance uncertainty. This geometry comparison is supportive only if the raw feature is an eclipse. Gaia neighbors inside 10 arcsec: none within 10 arcsec. Neighbor flux ratios alone cannot assign a source.

Gap-resets and pre-gap long slopes are positive counterevidence to treating the two window statistics as eclipses.

The MAST Tesscut footprint query lists 21 sectors, latest 86. Its response is in [current-sector receipt](../lead-current-sectors.json).

## Limits and next test

The largest sector81 dips are on orbital-gap boundaries; no secure isolated eclipse is timed. Reassess if an independent, fully observed eclipse-shaped event appears.

Source packet SHA-256: `c999491b5947ec61e4b7ff021c39f77344353a6ddec02f725f12d3f3c0c14114`. Every QLP FITS read by the numeric script was checked against its bulk packet hash; individual source paths and hashes are in `lead-numeric.json`. The shared Gaia neighbor and NSS catalogues were reused without new catalogue queries.
