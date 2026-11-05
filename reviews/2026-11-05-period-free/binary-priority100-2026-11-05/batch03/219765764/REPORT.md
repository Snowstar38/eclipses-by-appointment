# T025 — TIC 219765764

**Physical verdict:** PLAUSIBLE. **Full bounded review:** COMPLETE. **Catalogue novelty:** UNKNOWN; shared catalogue checks lack four VizieR gates (VSX, ASAS-SN, Kostov 2025 tables 3 and 4) after failed positive controls. This is not a negative catalogue match.

## Raw event and timing evidence

The s79 raw SAP trough near 3464.7 reaches ~8 ppt with a relatively level bottom, then a 0.25 d gap and +10.3 ppt step hide its egress. s40, s53 and s83 show similar gap-ended broad declines with 10–20 ppt post-gap steps; s80 has a different step. These cannot be counted as same-kind recurrences. A single real s79 event remains possible.

Measured eclipse period: none supported. Epoch BTJD: none supported. Depth: 8 ppt. Screening times in the source packet are not measured centers. See [numeric review](lead-numeric.json), [raw panels](lead-raw-01.png), [sector panels](lead-sector-01.png), and batch [gap evidence](../lead-gap-evidence.json).

## Attribution, reduction and orbit

Gaia DR3 1632993333840700032 has a spectroscopic orbit P=47.871032 d. At the evaluated event/screen epoch, the closest edge-on conjunction offset is 8.239 d, with a 4.873 d linear Gaia-covariance uncertainty. This geometry comparison is supportive only if the raw feature is an eclipse. Gaia neighbors inside 10 arcsec: none within 10 arcsec. Neighbor flux ratios alone cannot assign a source.

Terra independently extracted s79 TESScut target-centered 3x3 flux: bright target is present, but a broad decline and gap/step dominate; a local-window statistic is only 1.11 ppt and depends on the baseline. s77 has 0.00947 net counts; lead s86 has 0.53 counts (1.4% of positive cutout flux). Neither is a sensitive null. See helper-audit.txt and helper-pixels.json.

The MAST Tesscut footprint query lists 40 sectors, latest 86. Its response is in [current-sector receipt](../lead-current-sectors.json).

## Limits and next test

s79 has an ingress and flat bottom but egress is in a data gap. Other selected troughs often end at downlink gaps and do not form one Gaia-period clock. s77 and s86 current cutouts have negligible target flux, so neither supplies a recurrence null. Obtain a clean same-kind repeat and a higher-resolution source check.

Source packet SHA-256: `cc257ba06ab393be3328c8724259a3a52a915fe9a1d03425d20aacd8c255b74c`. Every QLP FITS read by the numeric script was checked against its bulk packet hash; individual source paths and hashes are in `lead-numeric.json`. The shared Gaia neighbor and NSS catalogues were reused without new catalogue queries.

The s86 cutout and extraction receipt are [here](lead-cutout-s86.png) and [here](../lead-t025-cutout.json); s77 and s79 helper diagnostics are [here](helper-pixels-s77.png), [here](helper-pixels-s79.png), with [numeric pixels](../helper-pixels.json).
