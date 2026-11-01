# TIC 219399648: CONFIRMED

**Full bounded review: COMPLETE.** Physical outcome and catalogue novelty are separate; historical screening was a queue label.

1. **Raw repeated events.** 5 measured, timing-usable raw QLP SAP_FLUX events in representative sectors [32, 98]. Each local trapezoid has a free center, depth, duration and baseline. Predicted windows guided inspection; unobserved or flagged windows are not negative detections. See `measurements.json`, `raw-windows.csv` and `raw-events.png`.
2. **Timing and alias.** Same-kind midpoint fit gives P = 9.3314205089 ± 0.0000110733 d and epoch BTJD 2181.15076257 (Deeper repeating eclipse; even historical half-period cycles). Even historical half-period cycles only: deeper same-kind eclipses; odd cycles show shallower secondary. Within-sector recurrences and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive period search.
3. **Pixel attribution.** The alternative cutout sector 98 deficit centroid is about 3.27 arcsec from the Gaia target coordinate; this is not a calibrated localization uncertainty. 0 Gaia neighbors within 60 arcsec are bright enough under the approximate flux-budget test to produce the selected event. Neighbor intrinsic eclipse requirements are not compared directly with blended pixel fractional losses. Source: `[local path omitted] 5\made\sb1-scale\diffimg\219399648\diff_s98.json`.
4. **Alternative reduction.** Separately extracted, target-centered TESScut aperture photometry recovers 11 stacked events at 3x3 depth 14.53 ppt, versus median selected raw QLP fit depth 18.29 ppt. The extraction and representative QLP raw measurement share TESS photons in this sector; aperture dilution limits depth comparison. The historical S98 stack mixes deeper and shallower half-period events, so its depth is not a same-kind depth comparison.
5. **Gaia geometry.** DR3 source 4797773555362406144: orbital P = 9.330097946 d, e = 0.0079. Closest edge-on conjunction offset at the measured epoch is +0.3396 d (+0.0364 phase); linear full-NSS-covariance timing scale 0.3330 d. Approximate central duration 6.49 h versus measured median 2.58 h. This is a plausibility check using assumed TIC radius/minimum-mass companion, not a fitted eclipse model or sigma veto.

**Deciding interpretation and limitation:** Alternating S32/98 raw depths show that the 4.66571-day SAP search branch is half the orbital eclipse cycle. Deeper even events give the 9.33142-day same-kind period consistent with Gaia. The S98 difference image favors the target with no capable Gaia neighbor within 60 arcsec.

**Next check:** Optional secondary-eclipse characterization.

Catalogue novelty: central seven-group coverage is in `../../shared-catalogues/coverage-matrix.csv`. A cone-source entry alone does not settle exact counterpart identity or priority.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Depth ppt |
|---:|---:|---:|---:|---:|
| 32 | 164 | 2181.1505425 | 0.003472 | 18.86 |
| 32 | 166 | 2190.4819811 | 0.003472 | 18.59 |
| 32 | 168 | 2199.8140342 | 0.003472 | 18.01 |
| 98 | 554 | 4000.7777232 | 0.001157 | 18.29 |
| 98 | 560 | 4028.7720610 | 0.001157 | 16.98 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../alias-audit.json`, `../gaia-geometry.json`, `../download-receipts.json`, `[local path omitted] 5\made\sb1-scale\diffimg\219399648\diff_s98.json`, its PNG and Gaia-neighbor table; source and artifact hashes are in `../SHA256SUMS.json`.


Stable review key: R528. Public evidence files: [measurements.json](../../evidence/219399648/measurements.json), [raw-events.png](../../evidence/219399648/raw-events.png), [raw-windows.csv](../../evidence/219399648/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch02/INDEX.md). 
