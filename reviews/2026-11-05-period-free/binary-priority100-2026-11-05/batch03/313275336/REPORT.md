# T024 — TIC 313275336

**Physical verdict:** PLAUSIBLE. **Full bounded review:** COMPLETE. **Catalogue novelty:** UNKNOWN; shared catalogue checks lack four VizieR gates (VSX, ASAS-SN, Kostov 2025 tables 3 and 4) after failed positive controls. This is not a negative catalogue match.

## Raw event and timing evidence

s26 raw SAP contains a shallow trough around 2033.5 with apparent recovery, while another much weaker depression about one day earlier does not match a 39.14 d same-kind clock. Eight sectors are already cached, through s74; the current footprint query adds no sector beyond that cached coverage. This leaves eclipse interpretation insecure, with no measured period.

Measured eclipse period: none supported. Epoch BTJD: none supported. Depth: 6 ppt. Screening times in the source packet are not measured centers. See [numeric review](lead-numeric.json), [raw panels](lead-raw-01.png), [sector panels](lead-sector-01.png), and batch [gap evidence](../lead-gap-evidence.json).

## Attribution, reduction and orbit

Gaia DR3 1124063932878885888 has a spectroscopic orbit P=39.143907 d. At the evaluated event/screen epoch, the closest edge-on conjunction offset is 1.643 d, with a 1.337 d linear Gaia-covariance uncertainty. This geometry comparison is supportive only if the raw feature is an eclipse. Gaia neighbors inside 10 arcsec: none within 10 arcsec. Neighbor flux ratios alone cannot assign a source.

In the same s26 samples, the raw SAP core deficit is ~7.1 ppt and QLP KSPSAP is about -0.3 ppt. Detrending suppression is recorded as a limitation rather than artifact proof.

The MAST Tesscut footprint query lists 8 sectors, latest 74. Its response is in [current-sector receipt](../lead-current-sectors.json).

## Limits and next test

The s26 ~6 ppt dip near 2033.5 is shallow on a changing baseline; a second nearby screen dip does not establish recurrence. KSPSAP suppresses it, which alone is not a refutation. Acquire an independent event or useful later-sector coverage and a pixel-level source check.

Source packet SHA-256: `94ebc256948334c0f57ef934d46c3a00f4b49c25ec14fd013e26170202e7d12b`. Every QLP FITS read by the numeric script was checked against its bulk packet hash; individual source paths and hashes are in `lead-numeric.json`. The shared Gaia neighbor and NSS catalogues were reused without new catalogue queries.
