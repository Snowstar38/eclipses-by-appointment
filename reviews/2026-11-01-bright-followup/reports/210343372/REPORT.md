# TIC 210343372: CONFIRMED

**Full bounded review: COMPLETE.** Physical outcome and catalogue novelty are separate; historical screening was a queue label.

1. **Raw repeated events.** 8 measured, timing-usable raw QLP SAP_FLUX events in representative sectors [41, 82]. Each local trapezoid has a free center, depth, duration and baseline. Predicted windows guided inspection; unobserved or flagged windows are not negative detections. See `measurements.json`, `raw-windows.csv` and `raw-events.png`.
2. **Timing and alias.** Same-kind midpoint fit gives P = 5.4946996557 ± 0.0000125202 d and epoch BTJD 2422.69788125 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; no persistent unequal alternating pattern seen in representative events. Within-sector recurrences and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive period search.
3. **Pixel attribution.** The alternative cutout sector 55 deficit centroid is about 4.07 arcsec from the Gaia target coordinate; this is not a calibrated localization uncertainty. 10 Gaia neighbors within 60 arcsec are bright enough under the approximate flux-budget test to produce the selected event. Neighbor intrinsic eclipse requirements are not compared directly with blended pixel fractional losses. Source: `[local path omitted] 5\made\sb1-scale\diffimg\210343372\diff_s55.json`.
4. **Alternative reduction.** Separately extracted, target-centered TESScut S55 aperture photometry recovers 5 stacked events at 3x3 depth 5.84 ppt, versus median selected raw QLP fit depth 7.04 ppt. TESScut S55 and representative QLP sectors [41, 82] are separate TESS observing occasions on the same instrument; their photons are distinct. Aperture dilution limits depth comparison.
5. **Gaia geometry.** DR3 source 1842372749004992000: orbital P = 5.493566815 d, e = 0.0368. Closest edge-on conjunction offset at the measured epoch is +0.2292 d (+0.0417 phase); linear full-NSS-covariance timing scale 0.2725 d. Approximate central duration 8.20 h versus measured median 3.10 h. This is a plausibility check using assumed TIC radius/minimum-mass companion, not a fitted eclipse model or sigma veto.

**Deciding interpretation and limitation:** S41/82 provide consecutive raw repeats. The closest capable G16.03 source lies 17.8 arcsec away and would require about 22% intrinsic loss; deficit is within 0.20 pixel of target. The Gaia phase offset is descriptive and within its large propagated orbital uncertainty.

**Next check:** Optional resolved time-series photometry.

Catalogue novelty: central seven-group coverage is in `../../shared-catalogues/coverage-matrix.csv`. A cone-source entry alone does not settle exact counterpart identity or priority.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Depth ppt |
|---:|---:|---:|---:|---:|
| 41 | 134 | 2422.6987727 | 0.003472 | 7.53 |
| 41 | 135 | 2428.1929206 | 0.003472 | 8.10 |
| 41 | 137 | 2439.1798373 | 0.003472 | 6.50 |
| 41 | 138 | 2444.6774781 | 0.003472 | 8.89 |
| 82 | 337 | 3538.1280403 | 0.002663 | 6.23 |
| 82 | 338 | 3543.6152633 | 0.002550 | 6.55 |
| 82 | 339 | 3549.1081336 | 0.002577 | 9.30 |
| 82 | 340 | 3554.6042030 | 0.003268 | 6.18 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../alias-audit.json`, `../gaia-geometry.json`, `../download-receipts.json`, `[local path omitted] 5\made\sb1-scale\diffimg\210343372\diff_s55.json`, its PNG and Gaia-neighbor table; source and artifact hashes are in `../SHA256SUMS.json`.


Stable review key: R511. Public evidence files: [measurements.json](../../evidence/210343372/measurements.json), [raw-events.png](../../evidence/210343372/raw-events.png), [raw-windows.csv](../../evidence/210343372/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch01/INDEX.md). [210343372.png](../../analysis/continuation/batch01/helper/210343372.png)
