# TIC 49901727: CONFIRMED

**Full bounded review: COMPLETE.** Physical outcome and catalogue novelty are separate; historical screening was a queue label.

1. **Raw repeated events.** 4 measured, timing-usable raw QLP SAP_FLUX events in representative sectors [31]. Each local trapezoid has a free center, depth, duration and baseline. Predicted windows guided inspection; unobserved or flagged windows are not negative detections. See `measurements.json`, `raw-windows.csv` and `raw-events.png`.
2. **Timing and alias.** Same-kind midpoint fit gives P = 4.7891053447 ± 0.0010980248 d and epoch BTJD 2147.21701942 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; no persistent unequal alternating pattern seen in representative events. Within-sector recurrences and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive period search.
3. **Pixel attribution.** The alternative cutout sector 31 deficit centroid is about 2.74 arcsec from the Gaia target coordinate; this is not a calibrated localization uncertainty. 0 Gaia neighbors within 60 arcsec are bright enough under the approximate flux-budget test to produce the selected event. Neighbor intrinsic eclipse requirements are not compared directly with blended pixel fractional losses. Source: `[local path omitted] 5\made\sb1-scale\diffimg\49901727\diff_s31.json`.
4. **Alternative reduction.** Separately extracted, target-centered TESScut S31 aperture photometry recovers 4 stacked events at 3x3 depth 54.10 ppt, versus median selected raw QLP fit depth 55.27 ppt. TESScut S31 and representative QLP S31 are reductions of the same TESS observations and share photons. Aperture dilution limits depth comparison.
5. **Gaia geometry.** DR3 source 3266000059384203136: orbital P = 4.788914677 d, e = 0.0281. Closest edge-on conjunction offset at the measured epoch is +0.1153 d (+0.0241 phase); linear full-NSS-covariance timing scale 0.3693 d. Approximate central duration 3.65 h versus measured median 3.15 h. This is a plausibility check using assumed TIC radius/minimum-mass companion, not a fitted eclipse model or sigma veto.

**Deciding interpretation and limitation:** Four same-sector raw eclipses establish recurrence and a photometric period, but the short single-sector baseline leaves a comparatively broad period error. No capable Gaia neighbor within 60 arcsec; target-centered difference image.

**Next check:** Additional-sector timing would refine the period.

Catalogue novelty: central seven-group coverage is in `../../shared-catalogues/coverage-matrix.csv`. A cone-source entry alone does not settle exact counterpart identity or priority.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Depth ppt |
|---:|---:|---:|---:|---:|
| 31 | 0 | 2147.2173324 | 0.003472 | 55.07 |
| 31 | 1 | 2152.0058502 | 0.003472 | 55.33 |
| 31 | 3 | 2161.5839073 | 0.003472 | 55.50 |
| 31 | 4 | 2166.3738305 | 0.003472 | 55.22 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../alias-audit.json`, `../gaia-geometry.json`, `../download-receipts.json`, `[local path omitted] 5\made\sb1-scale\diffimg\49901727\diff_s31.json`, its PNG and Gaia-neighbor table; source and artifact hashes are in `../SHA256SUMS.json`.


Stable review key: R512. Public evidence files: [measurements.json](../../evidence/49901727/measurements.json), [raw-events.png](../../evidence/49901727/raw-events.png), [raw-windows.csv](../../evidence/49901727/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch01/INDEX.md). [49901727.png](../../analysis/continuation/batch01/helper/49901727.png)
