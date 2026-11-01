# TIC 153972241: CONFIRMED

**Full bounded review: COMPLETE.** Physical outcome and catalogue novelty are separate; historical screening was a queue label.

1. **Raw repeated events.** 11 measured, timing-usable raw QLP SAP_FLUX events in representative sectors [14, 41, 76]. Each local trapezoid has a free center, depth, duration and baseline. Predicted windows guided inspection; unobserved or flagged windows are not negative detections. See `measurements.json`, `raw-windows.csv` and `raw-events.png`.
2. **Timing and alias.** Same-kind midpoint fit gives P = 5.0419880702 ± 0.0000086825 d and epoch BTJD 1686.76961209 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; no persistent unequal alternating pattern seen in representative events. Within-sector recurrences and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive period search.
3. **Pixel attribution.** The alternative cutout sector 75 deficit centroid is about 0.91 arcsec from the Gaia target coordinate; this is not a calibrated localization uncertainty. 0 Gaia neighbors within 60 arcsec are bright enough under the approximate flux-budget test to produce the selected event. Neighbor intrinsic eclipse requirements are not compared directly with blended pixel fractional losses. Source: `[local path omitted] 5\made\sb1-scale\diffimg\153972241\diff_s75.json`.
4. **Alternative reduction.** Separately extracted, target-centered TESScut aperture photometry recovers 6 stacked events at 3x3 depth 243.75 ppt, versus median selected raw QLP fit depth 235.59 ppt. This historical TESScut sector is a separate observing occasion on the same instrument from the representative QLP sectors; extraction and aperture differences limit depth comparison.
5. **Gaia geometry.** DR3 source 1666322761092269568: orbital P = 5.041663243 d, e = 0.0256. Closest edge-on conjunction offset at the measured epoch is +0.0466 d (+0.0092 phase); linear full-NSS-covariance timing scale 0.0912 d. Approximate central duration 4.55 h versus measured median 3.87 h. This is a plausibility check using assumed TIC radius/minimum-mass companion, not a fitted eclipse model or sigma veto.

**Deciding interpretation and limitation:** Deep S14/41/76 raw eclipses repeat; the S75 extraction recovers six events. Its target-centered difference image lists no capable Gaia neighbor within 60 arcsec.

**Next check:** Optional precision characterization.

Catalogue novelty: central seven-group coverage is in `../../shared-catalogues/coverage-matrix.csv`. A cone-source entry alone does not settle exact counterpart identity or priority.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Depth ppt |
|---:|---:|---:|---:|---:|
| 14 | 0 | 1686.7733724 | 0.010416 | 232.37 |
| 14 | 1 | 1691.8152417 | 0.010416 | 232.32 |
| 14 | 3 | 1701.8963232 | 0.010416 | 232.36 |
| 41 | 146 | 2422.8992728 | 0.003472 | 246.28 |
| 41 | 147 | 2427.9416130 | 0.003472 | 246.21 |
| 41 | 149 | 2438.0255926 | 0.003472 | 248.01 |
| 41 | 150 | 2443.0673221 | 0.003472 | 246.34 |
| 76 | 334 | 3370.7935552 | 0.001157 | 236.10 |
| 76 | 335 | 3375.8355668 | 0.001157 | 235.59 |
| 76 | 336 | 3380.8776017 | 0.001157 | 234.76 |
| 76 | 338 | 3390.9617784 | 0.001157 | 235.52 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../alias-audit.json`, `../gaia-geometry.json`, `../download-receipts.json`, `[local path omitted] 5\made\sb1-scale\diffimg\153972241\diff_s75.json`, its PNG and Gaia-neighbor table; source and artifact hashes are in `../SHA256SUMS.json`.


Stable review key: R524. Public evidence files: [measurements.json](../../evidence/153972241/measurements.json), [raw-events.png](../../evidence/153972241/raw-events.png), [raw-windows.csv](../../evidence/153972241/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch02/INDEX.md). 
