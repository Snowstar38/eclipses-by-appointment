# TIC 95247597: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate. This report reviews the frozen batch04 target; historical screening is not an admission verdict.

1. **Raw events.** Quality-zero QLP SAP_FLUX shows 3 timing-selected measured eclipses in sectors [61, 88]. Local trapezoid fits allow free centers and baseline. Predicted windows are search guides only; flagged or sparsely sampled windows are not null detections. Numeric windows and the raw plot retain the evidence.
2. **Timing and aliases.** Measured same-kind centers give P=14.3768729995 d, fit error=0.0000280654 d, epoch BTJD 2977.8070390 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). There are 1 consecutive within-sector same-kind cycle pairs. The inventory period was 14.37681 d and the historical SAP search branch was 14.3768112970 d. All selected historical photometric cycles used; no systematic alternating depth pattern requiring a double-period fit in representative data. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. The fit error is not calibrated total uncertainty. This bounded alias check is not an exhaustive blind period search.
3. **Pixel attribution: favors target at TESS resolution.** Historical S7 TESScut deficit core is 1.48 arcsec from the target coordinate; peak pixel [8, 7] and target pixel [8, 7]. Fractional PSF model residual is 0.250, not a localization uncertainty. Capable Gaia neighbors: none under the approximate G-band flux budget. The full list and flux-budget calculation are in historical/diff_s07.json; the original cutout and stacked image are retained and hashed.
4. **Alternative reduction.** A target-centered, background-subtracted TESScut extraction gives 1x1/3x3/5x5 stacked depths 79.56/76.84/68.07 ppt from 2 selected windows. Median selected QLP raw fit depth is 90.89 ppt. Aperture dilution, event-kind mixing and model residuals limit direct depth comparisons. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument.
5. **Gaia orbit.** The matched DR3 NSS source 3042854243248092928 has P=14.3765198811 d and e=0.11457. Closest edge-on conjunction differs from the measured epoch by -0.02690 in phase (-0.38667 d); linear propagation of the source-specific full SB1 covariance gives 0.41907 d as a descriptive timing scale. The rough central-duration estimate is 6.15 h versus trapezoid median 3.63 h; these assume a TIC radius and minimum-mass main-sequence companion and are not a full geometry fit or a sigma gate.

**Deciding interpretation and limitation.** S88 has a consecutive 14.376 d same-kind recurrence and S61 adds a long baseline. Earlier S7 windows have only five quality-zero points each, so they are not clean nulls. Current MAST QLP availability includes S7/34/61/88; availability alone is not an eclipse detection.

**Next check.** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty is evaluated centrally against seven scoped groups in ../../shared-catalogues/coverage-matrix.csv. This physical review does not assert exhaustive literature priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 61 | 103 | 2977.8070316 | 0.001157 | 93.18 | used |
| 88 | 153 | 3696.6510671 | 0.001157 | 88.62 | used |
| 88 | 154 | 3711.0271913 | 0.001157 | 90.89 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s07.json, historical/diff_s07.png, historical/gaia.json, original TESScut [local path omitted] and ../helper-audit.md. The original cutout and source files are SHA-256 recorded in ../source-hashes.json and ../SHA256SUMS.json.


Stable review key: R442. Public evidence files: [diff_s07.json](../../evidence/95247597/historical/diff_s07.json), [diff_s07.png](../../evidence/95247597/historical/diff_s07.png), [gaia.json](../../evidence/95247597/historical/gaia.json), [measurements.json](../../evidence/95247597/measurements.json), [raw-events.png](../../evidence/95247597/raw-events.png), [raw-windows.csv](../../evidence/95247597/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch04/INDEX.md). 
