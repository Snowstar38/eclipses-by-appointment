# TIC 285926385: CONFIRMED

**Full bounded review: COMPLETE.** Physical outcome and catalogue novelty are separate; historical screening was a queue label.

1. **Raw repeated events.** 5 measured, timing-usable raw QLP SAP_FLUX events in representative sectors [9, 63, 90]. Each local trapezoid has a free center, depth, duration and baseline. Predicted windows guided inspection; unobserved or flagged windows are not negative detections. See `measurements.json`, `raw-windows.csv` and `raw-events.png`.
2. **Timing and alias.** Same-kind midpoint fit gives P = 17.5553255431 ± 0.0000265567 d and epoch BTJD 1560.40143870 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; no persistent unequal alternating pattern seen in representative events. Within-sector recurrences and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive period search.
3. **Pixel attribution.** The alternative cutout sector 63 deficit centroid is about 3.07 arcsec from the Gaia target coordinate; this is not a calibrated localization uncertainty. 0 Gaia neighbors within 60 arcsec are bright enough under the approximate flux-budget test to produce the selected event. Neighbor intrinsic eclipse requirements are not compared directly with blended pixel fractional losses. Source: `[local path omitted] 5\made\sb1-scale\diffimg\285926385\diff_s63.json`.
4. **Alternative reduction.** Separately extracted, target-centered TESScut S63 aperture photometry recovers 2 stacked events at 3x3 depth 246.47 ppt, versus median selected raw QLP fit depth 247.49 ppt. TESScut S63 and representative QLP S63 are reductions of the same TESS observations and share photons. Aperture dilution limits depth comparison.
5. **Gaia geometry.** DR3 source 3589729714627304192: orbital P = 17.554087545 d, e = 0.4756. Closest edge-on conjunction offset at the measured epoch is +0.2965 d (+0.0169 phase); linear full-NSS-covariance timing scale 0.7498 d. Approximate central duration 8.01 h versus measured median 6.09 h. This is a plausibility check using assumed TIC radius/minimum-mass companion, not a fitted eclipse model or sigma veto.

**Deciding interpretation and limitation:** Deep S9/63/90 raw eclipses recur at the measured period. Difference image favors the target and lists no capable Gaia neighbor within 60 arcsec.

**Next check:** Optional precision characterization.

Catalogue novelty: central seven-group coverage is in `../../shared-catalogues/coverage-matrix.csv`. A cone-source entry alone does not settle exact counterpart identity or priority.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Depth ppt |
|---:|---:|---:|---:|---:|
| 9 | 0 | 1560.4031478 | 0.010417 | 235.41 |
| 63 | 83 | 3017.4937647 | 0.001157 | 250.18 |
| 63 | 84 | 3035.0484007 | 0.001157 | 250.80 |
| 90 | 125 | 3754.8174316 | 0.001157 | 244.80 |
| 90 | 126 | 3772.3722138 | 0.001157 | 247.49 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../alias-audit.json`, `../gaia-geometry.json`, `../download-receipts.json`, `[local path omitted] 5\made\sb1-scale\diffimg\285926385\diff_s63.json`, its PNG and Gaia-neighbor table; source and artifact hashes are in `../SHA256SUMS.json`.


Stable review key: R514. Public evidence files: [measurements.json](../../evidence/285926385/measurements.json), [raw-events.png](../../evidence/285926385/raw-events.png), [raw-windows.csv](../../evidence/285926385/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch01/INDEX.md). [285926385.png](../../analysis/continuation/batch01/helper/285926385.png)
