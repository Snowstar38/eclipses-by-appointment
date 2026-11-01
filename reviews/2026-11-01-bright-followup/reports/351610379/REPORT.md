# TIC 351610379: CONFIRMED

**Full bounded review: COMPLETE.** Physical outcome and catalogue novelty are separate; historical screening was a queue label.

1. **Raw repeated events.** 6 measured, timing-usable raw QLP SAP_FLUX events in representative sectors [58, 86]. Each local trapezoid has a free center, depth, duration and baseline. Predicted windows guided inspection; unobserved or flagged windows are not negative detections. See `measurements.json`, `raw-windows.csv` and `raw-events.png`.
2. **Timing and alias.** Same-kind midpoint fit gives P = 8.9418500033 ± 0.0000117888 d and epoch BTJD 2882.74512557 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; no persistent unequal alternating pattern seen in representative events. Within-sector recurrences and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive period search.
3. **Pixel attribution.** The alternative cutout sector 58 deficit centroid is about 4.80 arcsec from the Gaia target coordinate; this is not a calibrated localization uncertainty. 3 Gaia neighbors within 60 arcsec are bright enough under the approximate flux-budget test to produce the selected event. Neighbor intrinsic eclipse requirements are not compared directly with blended pixel fractional losses. Source: `[local path omitted] 5\made\sb1-scale\diffimg\351610379\diff_s58.json`.
4. **Alternative reduction.** Separately extracted, target-centered TESScut aperture photometry recovers 4 stacked events at 3x3 depth 22.03 ppt, versus median selected raw QLP fit depth 29.46 ppt. The extraction and representative QLP raw measurement share TESS photons in this sector; aperture dilution limits depth comparison.
5. **Gaia geometry.** DR3 source 536070020862283648: orbital P = 8.942678782 d, e = 0.0901. Closest edge-on conjunction offset at the measured epoch is -0.1852 d (-0.0207 phase); linear full-NSS-covariance timing scale 0.3265 d. Approximate central duration 4.19 h versus measured median 2.36 h. This is a plausibility check using assumed TIC radius/minimum-mass companion, not a fitted eclipse model or sigma veto.

**Deciding interpretation and limitation:** S58/86 raw repeats and the S58 deficit favor the target. The nearest capable G15.21 neighbor is 20.3 arcsec away and would require about 42% intrinsic eclipse depth; a brighter capable source at 54.1 arcsec is spatially separate. Pixel localization has no calibrated error.

**Next check:** Optional resolved eclipse photometry.

Catalogue novelty: central seven-group coverage is in `../../shared-catalogues/coverage-matrix.csv`. A cone-source entry alone does not settle exact counterpart identity or priority.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Depth ppt |
|---:|---:|---:|---:|---:|
| 58 | 121 | 2882.7441056 | 0.001157 | 28.59 |
| 58 | 122 | 2891.6868359 | 0.001157 | 29.35 |
| 58 | 123 | 2900.6290141 | 0.001157 | 32.68 |
| 58 | 124 | 2909.5716717 | 0.001157 | 29.56 |
| 86 | 207 | 3651.7452785 | 0.001157 | 30.69 |
| 86 | 208 | 3660.6849982 | 0.001157 | 27.67 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../alias-audit.json`, `../gaia-geometry.json`, `../download-receipts.json`, `[local path omitted] 5\made\sb1-scale\diffimg\351610379\diff_s58.json`, its PNG and Gaia-neighbor table; source and artifact hashes are in `../SHA256SUMS.json`.


Stable review key: R520. Public evidence files: [measurements.json](../../evidence/351610379/measurements.json), [raw-events.png](../../evidence/351610379/raw-events.png), [raw-windows.csv](../../evidence/351610379/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch02/INDEX.md). 
