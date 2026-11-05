# T028 — TIC 289008887

**Physical verdict:** REFUTED. **Full bounded review:** COMPLETE. **Catalogue novelty:** UNKNOWN; shared catalogue checks lack four VizieR gates (VSX, ASAS-SN, Kostov 2025 tables 3 and 4) after failed positive controls. This is not a negative catalogue match.

## Raw event and timing evidence

The s34/s61/s88 selected V shapes sit against continuous multi-day waves; each encounters a nearby gap and +16–23 ppt post-gap step. Their spacings 734.8 and 714.5 d cannot both follow a 33.73 d same-kind clock. New s108 TESScut shows strong continuous waves in a target-containing 3x3 aperture over 10,999 quality-zero cadences, corroborating non-eclipse variability.

Measured eclipse period: none supported. Epoch BTJD: none supported. Depth: none supported. Screening times in the source packet are not measured centers. See [numeric review](lead-numeric.json), [raw panels](lead-raw-01.png), [sector panels](lead-sector-01.png), and batch [gap evidence](../lead-gap-evidence.json).

## Attribution, reduction and orbit

Gaia DR3 3029185222067707648 has a spectroscopic orbit P=33.725707 d. At the evaluated event/screen epoch, the closest edge-on conjunction offset is -3.886 d, with a 3.761 d linear Gaia-covariance uncertainty. This geometry comparison is supportive only if the raw feature is an eclipse. Gaia neighbors inside 10 arcsec: none within 10 arcsec. Neighbor flux ratios alone cannot assign a source.

s108 target 3x3 holds 15,236 counts (32% of positive cutout flux). Older s7 cutout has near-zero target flux and is explicitly not used as a null.

The MAST Tesscut footprint query lists 5 sectors, latest 108. Its response is in [current-sector receipt](../lead-current-sectors.json).

## Limits and next test

Strong variable flux is present, but no isolated eclipse clock follows the 33.73 d Gaia orbit. Classify the smooth stellar/field variability separately if useful; search future data for isolated eclipses only on new evidence.

Source packet SHA-256: `1fd074c2287ee742f58b23c1cc358b52307e015930e8ba54af440ccbbf3e823f`. Every QLP FITS read by the numeric script was checked against its bulk packet hash; individual source paths and hashes are in `lead-numeric.json`. The shared Gaia neighbor and NSS catalogues were reused without new catalogue queries.

The s108 cutout diagnostic is [here](lead-cutout-s108.png), with [numeric receipt](../lead-t028-cutout.json).
