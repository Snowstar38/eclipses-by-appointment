# TIC 234413494: PROBABLE

**Full bounded review: COMPLETE.** Physical outcome and catalogue novelty are separate; historical screening was a queue label.

1. **Raw repeated events.** 11 measured, timing-usable raw QLP SAP_FLUX events in representative sectors [7, 46, 72]. Each local trapezoid has a free center, depth, duration and baseline. Predicted windows guided inspection; unobserved or flagged windows are not negative detections. See `measurements.json`, `raw-windows.csv` and `raw-events.png`.
2. **Timing and alias.** Same-kind midpoint fit gives P = 5.5028598185 ± 0.0000251813 d and epoch BTJD 1493.93985587 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; no persistent unequal alternating pattern seen in representative events. Within-sector recurrences and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive period search.
3. **Pixel attribution.** The alternative cutout sector 44 deficit centroid is about 4.75 arcsec from the Gaia target coordinate; this is not a calibrated localization uncertainty. 3 Gaia neighbors within 60 arcsec are bright enough under the approximate flux-budget test to produce the selected event. Neighbor intrinsic eclipse requirements are not compared directly with blended pixel fractional losses. Source: `[local path omitted]
4. **Alternative reduction.** Separately extracted S44 TESScut aperture photometry recovers 4 events at nominal 3x3 depth 14.03 ppt. The cutout is truncated, so this establishes a repeated signal in another extraction but cannot settle attribution or precise depth. TESScut S44 and representative QLP sectors [7, 46, 72] are separate TESS observing occasions on the same instrument; their photons are distinct.
5. **Gaia geometry.** DR3 source 3161704273321832064: orbital P = 5.503171903 d, e = 0.1043. Closest edge-on conjunction offset at the measured epoch is +0.0729 d (+0.0133 phase); linear full-NSS-covariance timing scale 0.1654 d. Approximate central duration 6.85 h versus measured median 4.76 h. This is a plausibility check using assumed TIC radius/minimum-mass companion, not a fitted eclipse model or sigma veto.

**Deciding interpretation and limitation:** Raw eclipses repeat in S7/46/72. A separate S44 TESScut extraction recovers four events, but the available cutout is truncated and its peak/residual panel is corrupted. Capable neighbors at 19.3 and 30.4 arcsec remain, so attribution is unresolved.

**Next check:** Acquire a complete cutout or resolved eclipse photometry.

Catalogue novelty: central seven-group coverage is in `../../shared-catalogues/coverage-matrix.csv`. A cone-source entry alone does not settle exact counterpart identity or priority.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Depth ppt |
|---:|---:|---:|---:|---:|
| 7 | 0 | 1493.9326038 | 0.010417 | 93.63 |
| 7 | 1 | 1499.4446516 | 0.010417 | 108.71 |
| 7 | 3 | 1510.4347053 | 0.010417 | 98.86 |
| 46 | 193 | 2555.9900823 | 0.004631 | 127.18 |
| 46 | 194 | 2561.4981707 | 0.006435 | 120.13 |
| 46 | 196 | 2572.4953342 | 0.007194 | 167.97 |
| 46 | 197 | 2578.0196107 | 0.005541 | 169.36 |
| 72 | 322 | 3265.8641418 | 0.003535 | 126.10 |
| 72 | 323 | 3271.3688033 | 0.004662 | 124.62 |
| 72 | 324 | 3276.8594444 | 0.002925 | 152.48 |
| 72 | 325 | 3282.3703365 | 0.005247 | 129.75 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../alias-audit.json`, `../gaia-geometry.json`, `../download-receipts.json`, `[local path omitted], its PNG and Gaia-neighbor table; source and artifact hashes are in `../SHA256SUMS.json`.


Stable review key: R516. Public evidence files: [measurements.json](../../evidence/234413494/measurements.json), [raw-events.png](../../evidence/234413494/raw-events.png), [raw-windows.csv](../../evidence/234413494/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch01/INDEX.md). [diff_s44.json](../../analysis/continuation/batch01/helper/diff_s44.json) [diff_s44.png](../../analysis/continuation/batch01/helper/diff_s44.png) [gaia.json](../../analysis/continuation/batch01/helper/gaia.json)
