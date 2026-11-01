# TIC 191634144: CONFIRMED

**Full bounded review: COMPLETE.** Physical outcome and catalogue novelty are separate; historical screening was a queue label.

1. **Raw repeated events.** 10 measured, timing-usable raw QLP SAP_FLUX events in representative sectors [57, 84]. Each local trapezoid has a free center, depth, duration and baseline. Predicted windows guided inspection; unobserved or flagged windows are not negative detections. See `measurements.json`, `raw-windows.csv` and `raw-events.png`.
2. **Timing and alias.** Same-kind midpoint fit gives P = 4.5575080623 ± 0.0000060351 d and epoch BTJD 2854.77452990 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; no persistent unequal alternating pattern seen in representative events. Within-sector recurrences and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive period search.
3. **Pixel attribution.** The alternative cutout sector 57 deficit centroid is about 3.11 arcsec from the Gaia target coordinate; this is not a calibrated localization uncertainty. 3 Gaia neighbors within 60 arcsec are bright enough under the approximate flux-budget test to produce the selected event. Neighbor intrinsic eclipse requirements are not compared directly with blended pixel fractional losses. Source: `[local path omitted] 5\made\sb1-scale\diffimg\191634144\diff_s57.json`.
4. **Alternative reduction.** Separately extracted, target-centered TESScut aperture photometry recovers 5 stacked events at 3x3 depth 9.50 ppt, versus median selected raw QLP fit depth 10.47 ppt. The extraction and representative QLP raw measurement share TESS photons in this sector; aperture dilution limits depth comparison.
5. **Gaia geometry.** DR3 source 375375060725718912: orbital P = 4.557098972 d, e = 0.0402. Closest edge-on conjunction offset at the measured epoch is +0.2181 d (+0.0479 phase); linear full-NSS-covariance timing scale 0.1720 d. Approximate central duration 6.73 h versus measured median 2.48 h. This is a plausibility check using assumed TIC radius/minimum-mass companion, not a fitted eclipse model or sigma veto.

**Deciding interpretation and limitation:** S57/84 raw shallow eclipses recur. Odd/even fitted depths vary at roughly the local noise level without a stable half-period interpretation. The S57 difference image favors the target over capable neighbors at 23.9, 34.4 and 53.6 arcsec.

**Next check:** Additional-sector timing and resolved photometry could tighten this shallow case.

Catalogue novelty: central seven-group coverage is in `../../shared-catalogues/coverage-matrix.csv`. A cone-source entry alone does not settle exact counterpart identity or priority.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Depth ppt |
|---:|---:|---:|---:|---:|
| 57 | 238 | 2854.7755006 | 0.001157 | 10.47 |
| 57 | 239 | 2859.3293846 | 0.001316 | 9.61 |
| 57 | 241 | 2868.4473010 | 0.001556 | 10.92 |
| 57 | 242 | 2873.0054339 | 0.001722 | 11.73 |
| 57 | 243 | 2877.5638528 | 0.002082 | 10.48 |
| 84 | 399 | 3588.5336664 | 0.001462 | 9.21 |
| 84 | 400 | 3593.0908072 | 0.001500 | 12.34 |
| 84 | 401 | 3597.6494571 | 0.001157 | 9.88 |
| 84 | 402 | 3602.2053858 | 0.001671 | 11.23 |
| 84 | 403 | 3606.7609465 | 0.001728 | 9.71 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../alias-audit.json`, `../gaia-geometry.json`, `../download-receipts.json`, `[local path omitted] 5\made\sb1-scale\diffimg\191634144\diff_s57.json`, its PNG and Gaia-neighbor table; source and artifact hashes are in `../SHA256SUMS.json`.


Stable review key: R527. Public evidence files: [measurements.json](../../evidence/191634144/measurements.json), [raw-events.png](../../evidence/191634144/raw-events.png), [raw-windows.csv](../../evidence/191634144/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch02/INDEX.md). 
