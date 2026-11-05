# T021 — TIC 260625051

**Physical verdict:** REFUTED. **Full bounded review:** COMPLETE. **Catalogue novelty:** UNKNOWN; shared catalogue checks lack four VizieR gates (VSX, ASAS-SN, Kostov 2025 tables 3 and 4) after failed positive controls. This is not a negative catalogue match.

## Raw event and timing evidence

The s65 flagged deficit sits on a nearly monotonic ~90% sector-scale decline. The s99 flags are opposing 259 and 245 ppt steps across 0.25 d gaps, and s93 falls through a gap on a sloping baseline. These shapes change sign and amplitude across sectors and do not furnish repeatable same-kind eclipses.

Measured eclipse period: none supported. Epoch BTJD: none supported. Depth: none supported. Screening times in the source packet are not measured centers. See [numeric review](lead-numeric.json), [raw panels](lead-raw-01.png), [sector panels](lead-sector-01.png), and batch [gap evidence](../lead-gap-evidence.json).

## Attribution, reduction and orbit

Gaia DR3 5798924900162485760 has a spectroscopic orbit P=28.256128 d. At the evaluated event/screen epoch, the closest edge-on conjunction offset is -1.504 d, with a 3.234 d linear Gaia-covariance uncertainty. This geometry comparison is supportive only if the raw feature is an eclipse. Gaia neighbors inside 10 arcsec: 3.32 arcsec G=17.21; 7.67 arcsec G=17.98; 9.41 arcsec G=18.92. Neighbor flux ratios alone cannot assign a source.

Raw morphology and measured gap steps positively identify the selected windows as extraction/baseline artifacts; another pipeline is unnecessary to refute those windows.

The MAST Tesscut footprint query lists 10 sectors, latest 102. Its response is in [current-sector receipt](../lead-current-sectors.json).

## Limits and next test

Retained windows are dominated by gross sector trends and discontinuities; no eclipse clock can be measured. If an independent future light curve is obtained, search it afresh for isolated events.

Source packet SHA-256: `1ae53ba1acd806a647471b9e5d269cfe7b8cf19124203055ec1ea3c42bdfe1c2`. Every QLP FITS read by the numeric script was checked against its bulk packet hash; individual source paths and hashes are in `lead-numeric.json`. The shared Gaia neighbor and NSS catalogues were reused without new catalogue queries.
