# TIC 384744266: CONFIRMED

**Full bounded review: COMPLETE.** Physical outcome and catalogue novelty are separate; historical screening was a queue label.

1. **Raw repeated events.** 4 measured, timing-usable raw QLP SAP_FLUX events in representative sectors [12, 39, 102]. Each local trapezoid has a free center, depth, duration and baseline. Predicted windows guided inspection; unobserved or flagged windows are not negative detections. See `measurements.json`, `raw-windows.csv` and `raw-events.png`.
2. **Timing and alias.** Same-kind midpoint fit gives P = 19.4326891330 ± 0.0000338018 d and epoch BTJD 1629.23687168 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; no persistent unequal alternating pattern seen in representative events. Within-sector recurrences and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive period search.
3. **Pixel attribution.** The alternative cutout sector 12 deficit centroid is about 3.65 arcsec from the Gaia target coordinate; this is not a calibrated localization uncertainty. 3 Gaia neighbors within 60 arcsec are bright enough under the approximate flux-budget test to produce the selected event. Neighbor intrinsic eclipse requirements are not compared directly with blended pixel fractional losses. Source: `[local path omitted] 5\made\sb1-scale\diffimg\384744266\diff_s12.json`.
4. **Alternative reduction.** Separately extracted, target-centered TESScut aperture photometry recovers 2 stacked events at 3x3 depth 20.23 ppt, versus median selected raw QLP fit depth 20.27 ppt. The extraction and representative QLP raw measurement share TESS photons in this sector; aperture dilution limits depth comparison.
5. **Gaia geometry.** DR3 source 5776380960403754624: orbital P = 19.433184428 d, e = 0.2022. Closest edge-on conjunction offset at the measured epoch is -0.1733 d (-0.0089 phase); linear full-NSS-covariance timing scale 0.4624 d. Approximate central duration 10.72 h versus measured median 5.40 h. This is a plausibility check using assumed TIC radius/minimum-mass companion, not a fitted eclipse model or sigma veto.

**Deciding interpretation and limitation:** S12/39/102 raw repeats agree. The S12 deficit is near the target. Three nominally capable neighbors lie 29–60 arcsec away, each requiring about 78–100% intrinsic loss, and none is favored by the observed deficit.

**Next check:** Optional resolved eclipse photometry.

Catalogue novelty: central seven-group coverage is in `../../shared-catalogues/coverage-matrix.csv`. A cone-source entry alone does not settle exact counterpart identity or priority.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Depth ppt |
|---:|---:|---:|---:|---:|
| 12 | 0 | 1629.2354465 | 0.010417 | 19.28 |
| 12 | 1 | 1648.6715529 | 0.010417 | 19.92 |
| 39 | 38 | 2367.6789719 | 0.003472 | 23.80 |
| 102 | 129 | 4136.0537725 | 0.001157 | 20.63 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../alias-audit.json`, `../gaia-geometry.json`, `../download-receipts.json`, `[local path omitted] 5\made\sb1-scale\diffimg\384744266\diff_s12.json`, its PNG and Gaia-neighbor table; source and artifact hashes are in `../SHA256SUMS.json`.


Stable review key: R525. Public evidence files: [measurements.json](../../evidence/384744266/measurements.json), [raw-events.png](../../evidence/384744266/raw-events.png), [raw-windows.csv](../../evidence/384744266/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch02/INDEX.md). 
