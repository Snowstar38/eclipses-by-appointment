# TIC 169318948: CONFIRMED

**Full bounded review: COMPLETE.** Physical outcome and catalogue novelty are separate; historical screening was a queue label.

1. **Raw repeated events.** 6 measured, timing-usable raw QLP SAP_FLUX events in representative sectors [32, 98]. Each local trapezoid has a free center, depth, duration and baseline. Predicted windows guided inspection; unobserved or flagged windows are not negative detections. See `measurements.json`, `raw-windows.csv` and `raw-events.png`.
2. **Timing and alias.** Same-kind midpoint fit gives P = 13.8955158737 ± 0.0000190968 d and epoch BTJD 2181.25859625 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; no persistent unequal alternating pattern seen in representative events. Within-sector recurrences and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive period search.
3. **Pixel attribution.** The alternative cutout sector 98 deficit centroid is about 1.05 arcsec from the Gaia target coordinate; this is not a calibrated localization uncertainty. 0 Gaia neighbors within 60 arcsec are bright enough under the approximate flux-budget test to produce the selected event. Neighbor intrinsic eclipse requirements are not compared directly with blended pixel fractional losses. Source: `[local path omitted] 5\made\sb1-scale\diffimg\169318948\diff_s98.json`.
4. **Alternative reduction.** Separately extracted, target-centered TESScut aperture photometry recovers 4 stacked events at 3x3 depth 17.95 ppt, versus median selected raw QLP fit depth 17.89 ppt. The extraction and representative QLP raw measurement share TESS photons in this sector; aperture dilution limits depth comparison.
5. **Gaia geometry.** DR3 source 2986427856265439488: orbital P = 13.896444944 d, e = 0.3989. Closest edge-on conjunction offset at the measured epoch is -0.2784 d (-0.0200 phase); linear full-NSS-covariance timing scale 0.4091 d. Approximate central duration 3.58 h versus measured median 1.76 h. This is a plausibility check using assumed TIC radius/minimum-mass companion, not a fitted eclipse model or sigma veto.

**Deciding interpretation and limitation:** S32/98 raw repeated eclipses and the S98 alternative extraction agree. The difference image favors the target and lists no capable Gaia neighbor within 60 arcsec.

**Next check:** Optional precision characterization.

Catalogue novelty: central seven-group coverage is in `../../shared-catalogues/coverage-matrix.csv`. A cone-source entry alone does not settle exact counterpart identity or priority.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Depth ppt |
|---:|---:|---:|---:|---:|
| 32 | 53 | 2181.2586438 | 0.003472 | 16.31 |
| 32 | 54 | 2195.1541875 | 0.003472 | 18.70 |
| 98 | 184 | 4001.5705969 | 0.001157 | 18.15 |
| 98 | 185 | 4015.4662752 | 0.001157 | 17.64 |
| 98 | 186 | 4029.3629551 | 0.001157 | 17.30 |
| 98 | 187 | 4043.2579572 | 0.001157 | 18.85 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../alias-audit.json`, `../gaia-geometry.json`, `../download-receipts.json`, `[local path omitted] 5\made\sb1-scale\diffimg\169318948\diff_s98.json`, its PNG and Gaia-neighbor table; source and artifact hashes are in `../SHA256SUMS.json`.


Stable review key: R522. Public evidence files: [measurements.json](../../evidence/169318948/measurements.json), [raw-events.png](../../evidence/169318948/raw-events.png), [raw-windows.csv](../../evidence/169318948/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch02/INDEX.md). 
