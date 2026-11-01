# TIC 163946960: CONFIRMED

**Full bounded review: COMPLETE.** Physical outcome and catalogue novelty are separate; historical screening was a queue label.

1. **Raw repeated events.** 4 measured, timing-usable raw QLP SAP_FLUX events in representative sectors [10, 99, 101]. Each local trapezoid has a free center, depth, duration and baseline. Predicted windows guided inspection; unobserved or flagged windows are not negative detections. See `measurements.json`, `raw-windows.csv` and `raw-events.png`.
2. **Timing and alias.** Same-kind midpoint fit gives P = 17.6318158711 ± 0.0005396857 d and epoch BTJD 1577.24863847 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; no persistent unequal alternating pattern seen in representative events. Within-sector recurrences and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive period search.
3. **Pixel attribution.** The alternative cutout sector 10 deficit centroid is about 5.50 arcsec from the Gaia target coordinate; this is not a calibrated localization uncertainty. 2 Gaia neighbors within 60 arcsec are bright enough under the approximate flux-budget test to produce the selected event. Neighbor intrinsic eclipse requirements are not compared directly with blended pixel fractional losses. Source: `[local path omitted] 5\made\sb1-scale\diffimg\163946960\diff_s10.json`.
4. **Alternative reduction.** Separately extracted, target-centered TESScut aperture photometry recovers 2 stacked events at 3x3 depth 51.83 ppt, versus median selected raw QLP fit depth 61.61 ppt. The extraction and representative QLP raw measurement share TESS photons in this sector; aperture dilution limits depth comparison.
5. **Gaia geometry.** DR3 source 6078495037379889408: orbital P = 17.629414377 d, e = 0.2481. Closest edge-on conjunction offset at the measured epoch is +0.2046 d (+0.0116 phase); linear full-NSS-covariance timing scale 0.2688 d. Approximate central duration 15.88 h versus measured median 12.71 h. This is a plausibility check using assumed TIC radius/minimum-mass companion, not a fitted eclipse model or sigma veto.

**Deciding interpretation and limitation:** S10/99/101 raw repeats and the S10 alternative extraction support the eclipse. The deficit lies about 0.26 pixel from the target, away from two capable Gaia neighbors at 15.8 and 29.7 arcsec; those require about 60% and 44% intrinsic losses. Localization is descriptive, without a calibrated uncertainty.

**Next check:** Resolved eclipse photometry would strengthen host attribution.

Catalogue novelty: central seven-group coverage is in `../../shared-catalogues/coverage-matrix.csv`. A cone-source entry alone does not settle exact counterpart identity or priority.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Depth ppt |
|---:|---:|---:|---:|---:|
| 10 | 0 | 1577.2451240 | 0.010417 | 65.60 |
| 10 | 1 | 1594.8691131 | 0.010417 | 53.68 |
| 99 | 141 | 4063.3590968 | 0.001933 | 57.62 |
| 101 | 144 | 4116.2215510 | 0.001157 | 71.16 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../alias-audit.json`, `../gaia-geometry.json`, `../download-receipts.json`, `[local path omitted] 5\made\sb1-scale\diffimg\163946960\diff_s10.json`, its PNG and Gaia-neighbor table; source and artifact hashes are in `../SHA256SUMS.json`.


Stable review key: R526. Public evidence files: [measurements.json](../../evidence/163946960/measurements.json), [raw-events.png](../../evidence/163946960/raw-events.png), [raw-windows.csv](../../evidence/163946960/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch02/INDEX.md). 
