# TIC 376799355: PROBABLE

**Full bounded review: COMPLETE.** Physical outcome and catalogue novelty are separate; historical screening was a queue label.

1. **Raw repeated events.** 11 measured, timing-usable raw QLP SAP_FLUX events in representative sectors [10, 63, 90]. Each local trapezoid has a free center, depth, duration and baseline. Predicted windows guided inspection; unobserved or flagged windows are not negative detections. See `measurements.json`, `raw-windows.csv` and `raw-events.png`.
2. **Timing and alias.** Same-kind midpoint fit gives P = 6.0309715740 ± 0.0000063815 d and epoch BTJD 1573.52342898 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; no persistent unequal alternating pattern seen in representative events. Within-sector recurrences and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive period search.
3. **Pixel attribution.** The alternative cutout sector 10 deficit centroid is about 3.49 arcsec from the Gaia target coordinate; this is not a calibrated localization uncertainty. 6 Gaia neighbors within 60 arcsec are bright enough under the approximate flux-budget test to produce the selected event. Neighbor intrinsic eclipse requirements are not compared directly with blended pixel fractional losses. Source: `[local path omitted] 5\made\sb1-scale\diffimg\376799355\diff_s10.json`.
4. **Alternative reduction.** Separately extracted, target-centered TESScut S10 aperture photometry recovers 4 stacked events at 3x3 depth 36.28 ppt, versus median selected raw QLP fit depth 87.69 ppt. TESScut S10 and representative QLP S10 are reductions of the same TESS observations and share photons. Aperture dilution limits depth comparison.
5. **Gaia geometry.** DR3 source 5252574583035692416: orbital P = 6.030792509 d, e = 0.1048. Closest edge-on conjunction offset at the measured epoch is +0.0241 d (+0.0040 phase); linear full-NSS-covariance timing scale 0.3152 d. Approximate central duration 7.35 h versus measured median 7.30 h. This is a plausibility check using assumed TIC radius/minimum-mass companion, not a fitted eclipse model or sigma veto.

**Deciding interpretation and limitation:** Raw eclipses repeat in S10/63/90 and the alternative 3x3 aperture also shows a deficit, diluted from roughly 88 ppt QLP to 36 ppt. The field is crowded: capable Gaia sources at 17.4 and 32.0 arcsec remain; the deficit centroid is only approximately target-centered and has no calibrated error. Attribution is unresolved.

**Next check:** Resolved photometry across an eclipse or an independent high-resolution centroid.

Catalogue novelty: central seven-group coverage is in `../../shared-catalogues/coverage-matrix.csv`. A cone-source entry alone does not settle exact counterpart identity or priority.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Depth ppt |
|---:|---:|---:|---:|---:|
| 10 | 0 | 1573.5245981 | 0.010417 | 85.30 |
| 10 | 2 | 1585.5854685 | 0.010417 | 83.45 |
| 10 | 3 | 1591.6168476 | 0.010417 | 86.74 |
| 63 | 239 | 3014.9283389 | 0.001157 | 93.41 |
| 63 | 240 | 3020.9555063 | 0.001157 | 95.32 |
| 63 | 241 | 3026.9862304 | 0.001157 | 93.19 |
| 63 | 242 | 3033.0181715 | 0.001157 | 93.14 |
| 90 | 361 | 3750.7045114 | 0.001157 | 89.07 |
| 90 | 362 | 3756.7359506 | 0.001157 | 86.28 |
| 90 | 363 | 3762.7659660 | 0.001157 | 87.69 |
| 90 | 364 | 3768.7961714 | 0.001157 | 86.08 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../alias-audit.json`, `../gaia-geometry.json`, `../download-receipts.json`, `[local path omitted] 5\made\sb1-scale\diffimg\376799355\diff_s10.json`, its PNG and Gaia-neighbor table; source and artifact hashes are in `../SHA256SUMS.json`.


Stable review key: R515. Public evidence files: [measurements.json](../../evidence/376799355/measurements.json), [raw-events.png](../../evidence/376799355/raw-events.png), [raw-windows.csv](../../evidence/376799355/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch01/INDEX.md). [376799355.png](../../analysis/continuation/batch01/helper/376799355.png)
