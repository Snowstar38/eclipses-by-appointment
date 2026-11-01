# TIC 61462126: CONFIRMED

**Full bounded review: COMPLETE.** Physical outcome and catalogue novelty are separate; historical screening was a queue label.

1. **Raw repeated events.** 6 measured, timing-usable raw QLP SAP_FLUX events in representative sectors [13, 67, 104]. Each local trapezoid has a free center, depth, duration and baseline. Predicted windows guided inspection; unobserved or flagged windows are not negative detections. See `measurements.json`, `raw-windows.csv` and `raw-events.png`.
2. **Timing and alias.** Same-kind midpoint fit gives P = 9.8867660303 ± 0.0000104175 d and epoch BTJD 1664.35061007 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; no persistent unequal alternating pattern seen in representative events. Within-sector recurrences and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive period search.
3. **Pixel attribution.** The alternative cutout sector 27 deficit centroid is about 3.03 arcsec from the Gaia target coordinate; this is not a calibrated localization uncertainty. 0 Gaia neighbors within 60 arcsec are bright enough under the approximate flux-budget test to produce the selected event. Neighbor intrinsic eclipse requirements are not compared directly with blended pixel fractional losses. Source: `[local path omitted] 5\made\sb1-scale\diffimg\61462126\diff_s27.json`.
4. **Alternative reduction.** Separately extracted, target-centered TESScut aperture photometry recovers 2 stacked events at 3x3 depth 70.42 ppt, versus median selected raw QLP fit depth 67.80 ppt. This historical TESScut sector is a separate observing occasion on the same instrument from the representative QLP sectors; extraction and aperture differences limit depth comparison.
5. **Gaia geometry.** DR3 source 6712693348579620608: orbital P = 9.884078396 d, e = 0.0419. Closest edge-on conjunction offset at the measured epoch is +0.2430 d (+0.0246 phase); linear full-NSS-covariance timing scale 0.2641 d. Approximate central duration 11.28 h versus measured median 9.20 h. This is a plausibility check using assumed TIC radius/minimum-mass companion, not a fitted eclipse model or sigma veto.

**Deciding interpretation and limitation:** S13/67/104 raw eclipses repeat. The S27 alternative extraction recovers two events with a target-centered deficit; no Gaia neighbor within 60 arcsec passes the approximate flux-budget test.

**Next check:** Optional precision characterization.

Catalogue novelty: central seven-group coverage is in `../../shared-catalogues/coverage-matrix.csv`. A cone-source entry alone does not settle exact counterpart identity or priority.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Depth ppt |
|---:|---:|---:|---:|---:|
| 13 | 0 | 1664.3478919 | 0.010417 | 68.05 |
| 13 | 1 | 1674.2337609 | 0.010417 | 67.55 |
| 67 | 148 | 3127.5924308 | 0.001157 | 72.35 |
| 67 | 150 | 3147.3652395 | 0.001157 | 72.66 |
| 104 | 255 | 4185.4766718 | 0.001157 | 61.42 |
| 104 | 256 | 4195.3618949 | 0.001157 | 62.18 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../alias-audit.json`, `../gaia-geometry.json`, `../download-receipts.json`, `[local path omitted] 5\made\sb1-scale\diffimg\61462126\diff_s27.json`, its PNG and Gaia-neighbor table; source and artifact hashes are in `../SHA256SUMS.json`.


Stable review key: R521. Public evidence files: [measurements.json](../../evidence/61462126/measurements.json), [raw-events.png](../../evidence/61462126/raw-events.png), [raw-windows.csv](../../evidence/61462126/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch02/INDEX.md). 
