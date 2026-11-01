# TIC 97649150: CONFIRMED

**Full bounded review: COMPLETE.** Physical outcome and catalogue novelty are separate; historical screening was a queue label.

1. **Raw repeated events.** 4 measured, timing-usable raw QLP SAP_FLUX events in representative sectors [7, 34, 87]. Each local trapezoid has a free center, depth, duration and baseline. Predicted windows guided inspection; unobserved or flagged windows are not negative detections. See `measurements.json`, `raw-windows.csv` and `raw-events.png`.
2. **Timing and alias.** Same-kind midpoint fit gives P = 12.9285082280 ± 0.0000582502 d and epoch BTJD 1497.82197689 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; no persistent unequal alternating pattern seen in representative events. Within-sector recurrences and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive period search.
3. **Pixel attribution.** The alternative cutout sector 7 deficit centroid is about 2.44 arcsec from the Gaia target coordinate; this is not a calibrated localization uncertainty. 6 Gaia neighbors within 60 arcsec are bright enough under the approximate flux-budget test to produce the selected event. Neighbor intrinsic eclipse requirements are not compared directly with blended pixel fractional losses. Source: `[local path omitted] 5\made\sb1-scale\diffimg\97649150\diff_s07.json`.
4. **Alternative reduction.** Separately extracted, target-centered TESScut S7 aperture photometry recovers 2 stacked events at 3x3 depth 5.75 ppt, versus median selected raw QLP fit depth 5.63 ppt. TESScut S7 and representative QLP S7 are reductions of the same TESS observations and share photons. Aperture dilution limits depth comparison.
5. **Gaia geometry.** DR3 source 5603413453346701184: orbital P = 12.927076847 d, e = 0.2541. Closest edge-on conjunction offset at the measured epoch is +0.3231 d (+0.0250 phase); linear full-NSS-covariance timing scale 0.3629 d. Approximate central duration 11.53 h versus measured median 7.02 h. This is a plausibility check using assumed TIC radius/minimum-mass companion, not a fitted eclipse model or sigma veto.

**Deciding interpretation and limitation:** S7/34/87 raw eclipses agree. The closest capable neighbor is G17.24 at 13.7 arcsec and would need roughly 54% intrinsic loss; deficit is within 0.12 pixel of target. Faint close-source ambiguity remains below calibrated pixel precision.

**Next check:** Optional resolved time-series photometry.

Catalogue novelty: central seven-group coverage is in `../../shared-catalogues/coverage-matrix.csv`. A cone-source entry alone does not settle exact counterpart identity or priority.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Depth ppt |
|---:|---:|---:|---:|---:|
| 7 | 0 | 1497.8258819 | 0.010417 | 5.29 |
| 7 | 1 | 1510.7514174 | 0.014168 | 4.82 |
| 34 | 57 | 2234.7309255 | 0.016170 | 5.98 |
| 87 | 169 | 3682.7404985 | 0.005530 | 7.16 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../alias-audit.json`, `../gaia-geometry.json`, `../download-receipts.json`, `[local path omitted] 5\made\sb1-scale\diffimg\97649150\diff_s07.json`, its PNG and Gaia-neighbor table; source and artifact hashes are in `../SHA256SUMS.json`.


Stable review key: R510. Public evidence files: [measurements.json](../../evidence/97649150/measurements.json), [raw-events.png](../../evidence/97649150/raw-events.png), [raw-windows.csv](../../evidence/97649150/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch01/INDEX.md). [97649150.png](../../analysis/continuation/batch01/helper/97649150.png)
