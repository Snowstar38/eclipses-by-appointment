# TIC 441257677: CONFIRMED

**Full bounded review: COMPLETE.** Physical outcome and catalogue novelty are separate; historical screening was a queue label.

1. **Raw repeated events.** 10 measured, timing-usable raw QLP SAP_FLUX events in representative sectors [13, 27, 67]. Each local trapezoid has a free center, depth, duration and baseline. Predicted windows guided inspection; unobserved or flagged windows are not negative detections. See `measurements.json`, `raw-windows.csv` and `raw-events.png`.
2. **Timing and alias.** Same-kind midpoint fit gives P = 6.5448839250 ± 0.0000106057 d and epoch BTJD 1660.21194066 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; no persistent unequal alternating pattern seen in representative events. Within-sector recurrences and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive period search.
3. **Pixel attribution.** The alternative cutout sector 13 deficit centroid is about 4.75 arcsec from the Gaia target coordinate; this is not a calibrated localization uncertainty. 0 Gaia neighbors within 60 arcsec are bright enough under the approximate flux-budget test to produce the selected event. Neighbor intrinsic eclipse requirements are not compared directly with blended pixel fractional losses. Source: `[local path omitted] 5\made\sb1-scale\diffimg\441257677\diff_s13.json`.
4. **Alternative reduction.** Separately extracted, target-centered TESScut aperture photometry recovers 4 stacked events at 3x3 depth 100.87 ppt, versus median selected raw QLP fit depth 98.56 ppt. The extraction and representative QLP raw measurement share TESS photons in this sector; aperture dilution limits depth comparison.
5. **Gaia geometry.** DR3 source 6739664574967468800: orbital P = 6.545173049 d, e = 0.1154. Closest edge-on conjunction offset at the measured epoch is +0.1321 d (+0.0202 phase); linear full-NSS-covariance timing scale 0.6016 d. Approximate central duration 8.15 h versus measured median 6.54 h. This is a plausibility check using assumed TIC radius/minimum-mass companion, not a fitted eclipse model or sigma veto.

**Deciding interpretation and limitation:** S13/27/67 raw events recur with no persistent odd/even depth split. The S13 alternative extraction shows four events and a target-centered deficit with no capable Gaia neighbor within 60 arcsec.

**Next check:** Optional precision characterization.

Catalogue novelty: central seven-group coverage is in `../../shared-catalogues/coverage-matrix.csv`. A cone-source entry alone does not settle exact counterpart identity or priority.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Depth ppt |
|---:|---:|---:|---:|---:|
| 13 | 0 | 1660.2126763 | 0.010417 | 93.32 |
| 13 | 1 | 1666.7572200 | 0.010417 | 94.30 |
| 13 | 2 | 1673.3017353 | 0.010417 | 92.44 |
| 13 | 3 | 1679.8466357 | 0.010417 | 92.41 |
| 27 | 58 | 2039.8154346 | 0.003472 | 98.05 |
| 27 | 59 | 2046.3602493 | 0.003472 | 100.29 |
| 27 | 60 | 2052.9051908 | 0.003472 | 99.68 |
| 27 | 61 | 2059.4490443 | 0.003472 | 99.18 |
| 67 | 225 | 3132.8110855 | 0.001157 | 100.29 |
| 67 | 227 | 3145.9003392 | 0.001157 | 99.07 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../alias-audit.json`, `../gaia-geometry.json`, `../download-receipts.json`, `[local path omitted] 5\made\sb1-scale\diffimg\441257677\diff_s13.json`, its PNG and Gaia-neighbor table; source and artifact hashes are in `../SHA256SUMS.json`.


Stable review key: R523. Public evidence files: [measurements.json](../../evidence/441257677/measurements.json), [raw-events.png](../../evidence/441257677/raw-events.png), [raw-windows.csv](../../evidence/441257677/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch02/INDEX.md). 
