# TIC 311398753: PROBABLE

**Full bounded review: COMPLETE.** Physical outcome and catalogue novelty are separate; historical screening was a queue label.

1. **Raw repeated events.** 3 measured, timing-usable raw QLP SAP_FLUX events in representative sectors [93, 103]. Each local trapezoid has a free center, depth, duration and baseline. Predicted windows guided inspection; unobserved or flagged windows are not negative detections. See `measurements.json`, `raw-windows.csv` and `raw-events.png`.
2. **Timing and alias.** Same-kind midpoint fit gives P = 15.0445006706 ± 0.0001120670 d and epoch BTJD 3839.52974390 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; no persistent unequal alternating pattern seen in representative events. Within-sector recurrences and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive period search.
3. **Pixel attribution.** The alternative cutout sector 13 deficit centroid is about 1.04 arcsec from the Gaia target coordinate; this is not a calibrated localization uncertainty. 3 Gaia neighbors within 60 arcsec are bright enough under the approximate flux-budget test to produce the selected event. Neighbor intrinsic eclipse requirements are not compared directly with blended pixel fractional losses. Source: `[local path omitted] 5\made\sb1-scale\diffimg\311398753\diff_s13.json`.
4. **Alternative reduction.** Separately extracted, target-centered TESScut aperture photometry recovers 2 stacked events at 3x3 depth 28.84 ppt, versus median selected raw QLP fit depth 34.43 ppt. This historical TESScut sector is a separate observing occasion on the same instrument from the representative QLP sectors; extraction and aperture differences limit depth comparison.
5. **Gaia geometry.** DR3 source 5804147301198863744: orbital P = 15.047545491 d, e = 0.0457. Closest edge-on conjunction offset at the measured epoch is -0.6848 d (-0.0455 phase); linear full-NSS-covariance timing scale 0.3346 d. Approximate central duration 21.27 h versus measured median 12.50 h. This is a plausibility check using assumed TIC radius/minimum-mass companion, not a fitted eclipse model or sigma veto.

**Deciding interpretation and limitation:** S93/103 raw eclipses repeat and the S13 alternative extraction recovers two. A capable G15.36 source lies only 9.65 arcsec from the target and shares the bright pixel; further capable sources lie at 20.8 and 38.2 arcsec. The target-near deficit cannot distinguish the closest host at uncalibrated pixel precision. Gaia conjunction offset is −0.685 d at the observed epoch versus a 0.335 d linear orbital timing scale; a projection near Gaia2016 gives +0.012 d with only a 0.026 d photometric period allowance, so phase agreement remains descriptive.

**Next check:** Resolved time-series photometry across an eclipse, plus refined Gaia-orbit comparison.

Catalogue novelty: central seven-group coverage is in `../../shared-catalogues/coverage-matrix.csv`. A cone-source entry alone does not settle exact counterpart identity or priority.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Depth ppt |
|---:|---:|---:|---:|---:|
| 93 | 146 | 3839.5306153 | 0.001157 | 34.43 |
| 93 | 147 | 3854.5730555 | 0.001319 | 35.00 |
| 103 | 167 | 4155.4643587 | 0.001760 | 31.94 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../alias-audit.json`, `../gaia-geometry.json`, `../download-receipts.json`, `[local path omitted] 5\made\sb1-scale\diffimg\311398753\diff_s13.json`, its PNG and Gaia-neighbor table; source and artifact hashes are in `../SHA256SUMS.json`.


Stable review key: R529. Public evidence files: [measurements.json](../../evidence/311398753/measurements.json), [raw-events.png](../../evidence/311398753/raw-events.png), [raw-windows.csv](../../evidence/311398753/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch02/INDEX.md). 
