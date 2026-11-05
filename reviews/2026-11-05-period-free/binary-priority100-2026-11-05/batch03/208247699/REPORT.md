# T030 — TIC 208247699

**Physical verdict:** REFUTED. **Full bounded review:** COMPLETE. **Catalogue novelty:** UNKNOWN; shared catalogue checks lack four VizieR gates (VSX, ASAS-SN, Kostov 2025 tables 3 and 4) after failed positive controls. This is not a negative catalogue match.

## Raw event and timing evidence

s65 has a >300 ppt recovery along a large slope; s99 windows sit on long rising/falling trends separated by gaps, including an ~11 ppt step; s102 shows a nearly monotonic rise and a ~20 ppt local reset. Fitted trapezoid centers move with arbitrary local span and do not form an orbital clock.

Measured eclipse period: none supported. Epoch BTJD: none supported. Depth: none supported. Screening times in the source packet are not measured centers. See [numeric review](lead-numeric.json), [raw panels](lead-raw-01.png), [sector panels](lead-sector-01.png), and batch [gap evidence](../lead-gap-evidence.json).

## Attribution, reduction and orbit

Gaia DR3 5870898415961768064 has a spectroscopic orbit P=31.007352 d. At the evaluated event/screen epoch, the closest edge-on conjunction offset is -2.782 d, with a 1.135 d linear Gaia-covariance uncertainty. This geometry comparison is supportive only if the raw feature is an eclipse. Gaia neighbors inside 10 arcsec: 2.53 arcsec G=19.71; 4.09 arcsec G=20.54; 4.16 arcsec G=15.52; 5.38 arcsec G=19.79; 6.23 arcsec G=19.94; 7.00 arcsec G=20.14; 7.53 arcsec G=20.24; 9.40 arcsec G=20.64. Neighbor flux ratios alone cannot assign a source.

The observed long slopes and discontinuities are positive instrumental/baseline explanations for the selected flags.

The MAST Tesscut footprint query lists 7 sectors, latest 102. Its response is in [current-sector receipt](../lead-current-sectors.json).

## Limits and next test

All retained windows are steep trends or baseline discontinuities; no repeatable eclipse center. Reopen only for an isolated new event supported by raw and spatial data.

Source packet SHA-256: `104b0032d242812fd5e1b4a80e39811b398da6acd9d12262f5fee23bcad6f844`. Every QLP FITS read by the numeric script was checked against its bulk packet hash; individual source paths and hashes are in `lead-numeric.json`. The shared Gaia neighbor and NSS catalogues were reused without new catalogue queries.
