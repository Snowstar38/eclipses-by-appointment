# TIC 265436769: PROBABLE

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate. This report reviews the frozen batch04 target; historical screening is not an admission verdict.

1. **Raw events.** Quality-zero QLP SAP_FLUX shows 4 timing-selected measured eclipses in sectors [95, 104]. Local trapezoid fits allow free centers and baseline. Predicted windows are search guides only; flagged or sparsely sampled windows are not null detections. Numeric windows and the raw plot retain the evidence.
2. **Timing and aliases.** Measured same-kind centers give P=15.4747037950 d, fit error=0.0000777982 d, epoch BTJD 3889.2835333 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). There are 2 consecutive within-sector same-kind cycle pairs. The inventory period was 15.47493 d and the historical SAP search branch was 15.4749291199 d. All selected historical photometric cycles used; no systematic alternating depth pattern requiring a double-period fit in representative data. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. The fit error is not calibrated total uncertainty. This bounded alias check is not an exhaustive blind period search.
3. **Pixel attribution: unresolved at TESS resolution.** Historical S67 TESScut deficit core is 4.64 arcsec from the target coordinate; peak pixel [8, 7] and target pixel [8, 7]. Fractional PSF model residual is 0.870, not a localization uncertainty. Capable Gaia neighbors: 22.6 arcsec, G=16.71, intrinsic-loss requirement ~0.42; 32.1 arcsec, G=11.32, intrinsic-loss requirement ~0.01; 36.8 arcsec, G=17.48, intrinsic-loss requirement ~0.84; 59.2 arcsec, G=12.94, intrinsic-loss requirement ~0.02. The full list and flux-budget calculation are in historical/diff_s67.json; the original cutout and stacked image are retained and hashed.
4. **Alternative reduction.** A target-centered, background-subtracted TESScut extraction gives 1x1/3x3/5x5 stacked depths 8.63/6.38/3.66 ppt from 2 selected windows. Median selected QLP raw fit depth is 6.24 ppt. Aperture dilution, event-kind mixing and model residuals limit direct depth comparisons. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument.
5. **Gaia orbit.** The matched DR3 NSS source 6403358774444776960 has P=15.4729899462 d and e=0.21828. Closest edge-on conjunction differs from the measured epoch by 0.02964 in phase (0.45867 d); linear propagation of the source-specific full SB1 covariance gives 0.48556 d as a descriptive timing scale. The rough central-duration estimate is 4.96 h versus trapezoid median 1.36 h; these assume a TIC radius and minimum-mass main-sequence companion and are not a full geometry fit or a sigma gate.

**Deciding interpretation and limitation.** Four shallow raw events in S95 and S104 include same-sector consecutive cycles. The S67 difference core favors the target, yet a capable source 22.6 arcsec away and a high image-model residual (0.87) leave attribution unresolved. Early S1 windows are sparse or flagged, not clean nulls.

**Next check.** Resolved eclipse photometry or multi-source PRF localization for source attribution.

Catalogue novelty is evaluated centrally against seven scoped groups in ../../shared-catalogues/coverage-matrix.csv. This physical review does not assert exhaustive literature priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 95 | 165 | 3889.2831391 | 0.001679 | 6.78 | used |
| 95 | 166 | 3904.7584970 | 0.001422 | 8.38 | used |
| 104 | 184 | 4183.3039144 | 0.001691 | 5.71 | used |
| 104 | 185 | 4198.7770617 | 0.001266 | 5.19 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s67.json, historical/diff_s67.png, historical/gaia.json, original TESScut [local path omitted] and ../helper-audit.md. The original cutout and source files are SHA-256 recorded in ../source-hashes.json and ../SHA256SUMS.json.


Stable review key: R447. Public evidence files: [diff_s67.json](../../evidence/265436769/historical/diff_s67.json), [diff_s67.png](../../evidence/265436769/historical/diff_s67.png), [gaia.json](../../evidence/265436769/historical/gaia.json), [measurements.json](../../evidence/265436769/measurements.json), [raw-events.png](../../evidence/265436769/raw-events.png), [raw-windows.csv](../../evidence/265436769/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch04/INDEX.md). 
