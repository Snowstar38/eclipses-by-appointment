# TIC 66072136: CONFIRMED

**Full bounded review: COMPLETE.** Physical outcome and catalogue novelty are separate; historical screening was a queue label.

1. **Raw repeated events.** 14 measured, timing-usable raw QLP SAP_FLUX events in representative sectors [16, 76, 84]. Each local trapezoid has a free center, depth, duration and baseline. Predicted windows guided inspection; unobserved or flagged windows are not negative detections. See `measurements.json`, `raw-windows.csv` and `raw-events.png`.
2. **Timing and alias.** Same-kind midpoint fit gives P = 4.5892005792 ± 0.0000108785 d and epoch BTJD 1742.29852360 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; no persistent unequal alternating pattern seen in representative events. Within-sector recurrences and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive period search.
3. **Pixel attribution.** The alternative cutout sector 76 deficit centroid is about 4.59 arcsec from the Gaia target coordinate; this is not a calibrated localization uncertainty. 0 Gaia neighbors within 60 arcsec are bright enough under the approximate flux-budget test to produce the selected event. Neighbor intrinsic eclipse requirements are not compared directly with blended pixel fractional losses. Source: `[local path omitted] 5\made\sb1-scale\diffimg\66072136\diff_s76.json`.
4. **Alternative reduction.** Separately extracted, target-centered TESScut S76 aperture photometry recovers 6 stacked events at 3x3 depth 72.67 ppt, versus median selected raw QLP fit depth 71.44 ppt. TESScut S76 and representative QLP S76 are reductions of the same TESS observations and share photons. Aperture dilution limits depth comparison.
5. **Gaia geometry.** DR3 source 1989520523290696832: orbital P = 4.589208060 d, e = 0.0502. Closest edge-on conjunction offset at the measured epoch is +0.0446 d (+0.0097 phase); linear full-NSS-covariance timing scale 0.0990 d. Approximate central duration 6.32 h versus measured median 4.58 h. This is a plausibility check using assumed TIC radius/minimum-mass companion, not a fitted eclipse model or sigma veto.

**Deciding interpretation and limitation:** S16/76/84 raw repeats and the alternative S76 aperture support a real target-centered eclipse. No capable Gaia neighbor within 60 arcsec. Central catalogue reconciliation identifies the close VSX EA V0693 Lac counterpart as the same object, so this is a known eclipsing-binary recovery, not a new-system addition. VSX lists 1.08916 d versus the measured same-kind 4.58920 d; the disagreement does not negate the measured raw eclipses.

**Next check:** Resolve the discordant VSX period for catalogue interpretation; no new-system count.

Catalogue novelty: central seven-group coverage is in `../../shared-catalogues/coverage-matrix.csv`. A cone-source entry alone does not settle exact counterpart identity or priority.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Depth ppt |
|---:|---:|---:|---:|---:|
| 16 | 0 | 1742.2954049 | 0.010417 | 67.44 |
| 16 | 3 | 1756.0651217 | 0.010417 | 66.89 |
| 16 | 4 | 1760.6516646 | 0.010417 | 74.77 |
| 76 | 355 | 3371.4642140 | 0.001157 | 78.54 |
| 76 | 356 | 3376.0541073 | 0.001157 | 73.67 |
| 76 | 357 | 3380.6440772 | 0.001157 | 72.33 |
| 76 | 358 | 3385.2334200 | 0.001157 | 73.42 |
| 76 | 359 | 3389.8217691 | 0.001157 | 74.56 |
| 76 | 360 | 3394.4095962 | 0.001157 | 74.35 |
| 84 | 402 | 3587.1568237 | 0.001157 | 70.55 |
| 84 | 403 | 3591.7464407 | 0.001157 | 68.86 |
| 84 | 405 | 3600.9241348 | 0.001157 | 70.36 |
| 84 | 406 | 3605.5144422 | 0.001157 | 69.97 |
| 84 | 407 | 3610.1028446 | 0.001157 | 69.45 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../alias-audit.json`, `../gaia-geometry.json`, `../download-receipts.json`, `[local path omitted] 5\made\sb1-scale\diffimg\66072136\diff_s76.json`, its PNG and Gaia-neighbor table; source and artifact hashes are in `../SHA256SUMS.json`.


Stable review key: R519. Public evidence files: [measurements.json](../../evidence/66072136/measurements.json), [raw-events.png](../../evidence/66072136/raw-events.png), [raw-windows.csv](../../evidence/66072136/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch01/INDEX.md). [66072136.png](../../analysis/continuation/batch01/helper/66072136.png)
