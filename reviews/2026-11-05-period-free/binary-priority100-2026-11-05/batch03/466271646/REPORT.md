# T023 — TIC 466271646

**Physical verdict:** REFUTED. **Full bounded review:** COMPLETE. **Catalogue novelty:** UNKNOWN; shared catalogue checks lack four VizieR gates (VSX, ASAS-SN, Kostov 2025 tables 3 and 4) after failed positive controls. This is not a negative catalogue match.

## Raw event and timing evidence

s101 falls toward BTJD 4113.2, ends at a 1.13 d gap, then resumes 13.9 ppt higher. s102 and s103 show the same falling-into-gap/rising-after-gap pattern around 4139 and 4165 despite no same-kind eclipse timing. The recurring downlink-edge shape is positive instrumental evidence.

Measured eclipse period: none supported. Epoch BTJD: none supported. Depth: none supported. Screening times in the source packet are not measured centers. See [numeric review](lead-numeric.json), [raw panels](lead-raw-01.png), [sector panels](lead-sector-01.png), and batch [gap evidence](../lead-gap-evidence.json).

## Attribution, reduction and orbit

Gaia DR3 6429348270091433344 has a spectroscopic orbit P=28.813649 d. At the evaluated event/screen epoch, the closest edge-on conjunction offset is -2.938 d, with a 8.749 d linear Gaia-covariance uncertainty. This geometry comparison is supportive only if the raw feature is an eclipse. Gaia neighbors inside 10 arcsec: none within 10 arcsec. Neighbor flux ratios alone cannot assign a source.

QLP alternate flux follows the same-photon data and cannot turn these gap-terminated segments into a measured clock.

The MAST Tesscut footprint query lists 6 sectors, latest 104. Its response is in [current-sector receipt](../lead-current-sectors.json).

## Limits and next test

The s101 flagged ingress is truncated; repeated sector-edge resets explain similar later shapes. A future isolated event away from a data gap would warrant a new review.

Source packet SHA-256: `f0deb09d167aed75466eb4960801408874058a25fa4b400b1f4a3bf16dbc4dbb`. Every QLP FITS read by the numeric script was checked against its bulk packet hash; individual source paths and hashes are in `lead-numeric.json`. The shared Gaia neighbor and NSS catalogues were reused without new catalogue queries.
