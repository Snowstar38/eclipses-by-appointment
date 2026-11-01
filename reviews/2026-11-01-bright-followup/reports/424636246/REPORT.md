# TIC 424636246: CONFIRMED

**Full bounded review: COMPLETE.** Physical outcome and catalogue novelty are separate; historical screening was a queue label.

1. **Raw repeated events.** 6 measured, timing-usable raw QLP SAP_FLUX events in representative sectors [14, 55, 84]. Each local trapezoid has a free center, depth, duration and baseline. Predicted windows guided inspection; unobserved or flagged windows are not negative detections. See `measurements.json`, `raw-windows.csv` and `raw-events.png`.
2. **Timing and alias.** Same-kind midpoint fit gives P = 10.9608574269 ± 0.0000279668 d and epoch BTJD 1686.72848166 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; no persistent unequal alternating pattern seen in representative events. Within-sector recurrences and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive period search.
3. **Pixel attribution.** The alternative cutout sector 14 deficit centroid is about 3.21 arcsec from the Gaia target coordinate; this is not a calibrated localization uncertainty. 3 Gaia neighbors within 60 arcsec are bright enough under the approximate flux-budget test to produce the selected event. Neighbor intrinsic eclipse requirements are not compared directly with blended pixel fractional losses. Source: `[local path omitted] 5\made\sb1-scale\diffimg\424636246\diff_s14.json`.
4. **Alternative reduction.** Separately extracted, target-centered TESScut S14 aperture photometry recovers 3 stacked events at 3x3 depth 64.40 ppt, versus median selected raw QLP fit depth 65.48 ppt. TESScut S14 and representative QLP S14 are reductions of the same TESS observations and share photons. Aperture dilution limits depth comparison.
5. **Gaia geometry.** DR3 source 2139000984511908864: orbital P = 10.961251824 d, e = 0.0115. Closest edge-on conjunction offset at the measured epoch is -0.0947 d (-0.0086 phase); linear full-NSS-covariance timing scale 0.2147 d. Approximate central duration 8.37 h versus measured median 6.53 h. This is a plausibility check using assumed TIC radius/minimum-mass companion, not a fitted eclipse model or sigma veto.

**Deciding interpretation and limitation:** S14/55/84 raw repeats and target-centered deficit. Capable catalogued neighbors are at least 50.6 arcsec away and need large intrinsic losses; no nearby source is favored by the deficit image.

**Next check:** Optional precision characterization.

Catalogue novelty: central seven-group coverage is in `../../shared-catalogues/coverage-matrix.csv`. A cone-source entry alone does not settle exact counterpart identity or priority.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Depth ppt |
|---:|---:|---:|---:|---:|
| 14 | 0 | 1686.7241028 | 0.010417 | 65.82 |
| 14 | 2 | 1708.6482791 | 0.010417 | 64.77 |
| 55 | 102 | 2804.7383553 | 0.003472 | 69.30 |
| 55 | 103 | 2815.6960722 | 0.003472 | 70.29 |
| 84 | 174 | 3593.9174280 | 0.001157 | 64.93 |
| 84 | 175 | 3604.8786671 | 0.001157 | 65.13 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../alias-audit.json`, `../gaia-geometry.json`, `../download-receipts.json`, `[local path omitted] 5\made\sb1-scale\diffimg\424636246\diff_s14.json`, its PNG and Gaia-neighbor table; source and artifact hashes are in `../SHA256SUMS.json`.


Stable review key: R513. Public evidence files: [measurements.json](../../evidence/424636246/measurements.json), [raw-events.png](../../evidence/424636246/raw-events.png), [raw-windows.csv](../../evidence/424636246/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch01/INDEX.md). [424636246.png](../../analysis/continuation/batch01/helper/424636246.png)
