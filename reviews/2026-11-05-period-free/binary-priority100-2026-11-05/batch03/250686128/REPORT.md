# T022 — TIC 250686128

**Physical verdict:** REFUTED. **Full bounded review:** COMPLETE. **Catalogue novelty:** UNKNOWN; shared catalogue checks lack four VizieR gates (VSX, ASAS-SN, Kostov 2025 tables 3 and 4) after failed positive controls. This is not a negative catalogue match.

## Raw event and timing evidence

The s85 screen time 3623.76 is immediately after a data gap; flux then rises monotonically by roughly 50 ppt over the next day without an eclipse egress. The s18 and s58 raw curves show no corresponding dip. This is a gap-edge/baseline feature, not a timed eclipse.

Measured eclipse period: none supported. Epoch BTJD: none supported. Depth: none supported. Screening times in the source packet are not measured centers. See [numeric review](lead-numeric.json), [raw panels](lead-raw-01.png), [sector panels](lead-sector-01.png), and batch [gap evidence](../lead-gap-evidence.json).

## Attribution, reduction and orbit

Gaia DR3 455216539958057088 has a spectroscopic orbit P=48.957936 d. At the evaluated event/screen epoch, the closest edge-on conjunction offset is -9.994 d, with a 4.738 d linear Gaia-covariance uncertainty. This geometry comparison is supportive only if the raw feature is an eclipse. Gaia neighbors inside 10 arcsec: 5.52 arcsec G=17.14. Neighbor flux ratios alone cannot assign a source.

The opposite post-gap trend in the same raw window is positive contrary evidence to an isolated eclipse.

The MAST Tesscut footprint query lists 3 sectors, latest 85. Its response is in [current-sector receipt](../lead-current-sectors.json).

## Limits and next test

One selected window; no independent astrophysical eclipse remains after raw-shape inspection. Revisit only if a future light curve shows an isolated return to baseline at a consistent phase.

Source packet SHA-256: `3361d3a2728c67afb52f104524068c23aa4ef6e2b7292c58a1d40696eae06ff4`. Every QLP FITS read by the numeric script was checked against its bulk packet hash; individual source paths and hashes are in `lead-numeric.json`. The shared Gaia neighbor and NSS catalogues were reused without new catalogue queries.
