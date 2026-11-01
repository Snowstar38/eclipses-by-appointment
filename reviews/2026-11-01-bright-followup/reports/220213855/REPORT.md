# TIC 220213855: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate. This report reviews the frozen batch04 target; historical screening is not an admission verdict.

1. **Raw events.** Quality-zero QLP SAP_FLUX shows 4 timing-selected measured eclipses in sectors [87]. Local trapezoid fits allow free centers and baseline. Predicted windows are search guides only; flagged or sparsely sampled windows are not null detections. Numeric windows and the raw plot retain the evidence.
2. **Timing and aliases.** Measured same-kind centers give P=5.4751727504 d, fit error=0.0005176080 d, epoch BTJD 3670.5164102 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). There are 3 consecutive within-sector same-kind cycle pairs. The inventory period was 5.47591 d and the historical SAP search branch was 5.4759094123 d. All selected historical photometric cycles used; no systematic alternating depth pattern requiring a double-period fit in representative data. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. The fit error is not calibrated total uncertainty. This bounded alias check is not an exhaustive blind period search.
3. **Pixel attribution: favors target at TESS resolution.** Historical S87 TESScut deficit core is 2.58 arcsec from the target coordinate; peak pixel [7, 7] and target pixel [7, 7]. Fractional PSF model residual is 0.608, not a localization uncertainty. Capable Gaia neighbors: 38.8 arcsec, G=15.53, intrinsic-loss requirement ~0.99. The full list and flux-budget calculation are in historical/diff_s87.json; the original cutout and stacked image are retained and hashed.
4. **Alternative reduction.** A target-centered, background-subtracted TESScut extraction gives 1x1/3x3/5x5 stacked depths 41.78/40.53/35.53 ppt from 4 selected windows. Median selected QLP raw fit depth is 41.58 ppt. Aperture dilution, event-kind mixing and model residuals limit direct depth comparisons. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument.
5. **Gaia orbit.** The matched DR3 NSS source 3326997734678765696 has P=5.4759465374 d and e=0.03177. Closest edge-on conjunction differs from the measured epoch by 0.01870 in phase (0.10240 d); linear propagation of the source-specific full SB1 covariance gives 0.34526 d as a descriptive timing scale. The rough central-duration estimate is 5.81 h versus trapezoid median 3.46 h; these assume a TIC radius and minimum-mass main-sequence companion and are not a full geometry fit or a sigma gate.

**Deciding interpretation and limitation.** Four consecutive raw eclipses in S87 establish recurrence across 16.43 d. S6 is available but its candidate windows have at most four quality-zero cadences inside half the search duration; no clean null is claimed. The fitted period error is limited by one sector and is not total ephemeris uncertainty.

**Next check.** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty is evaluated centrally against seven scoped groups in ../../shared-catalogues/coverage-matrix.csv. This physical review does not assert exhaustive literature priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 87 | 402 | 3670.5167841 | 0.001157 | 39.88 | used |
| 87 | 403 | 3675.9914259 | 0.001157 | 42.23 | used |
| 87 | 404 | 3681.4659477 | 0.001157 | 40.94 | used |
| 87 | 405 | 3686.9425194 | 0.001157 | 42.30 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s87.json, historical/diff_s87.png, historical/gaia.json, original TESScut [local path omitted] and ../helper-audit.md. The original cutout and source files are SHA-256 recorded in ../source-hashes.json and ../SHA256SUMS.json.


Stable review key: R446. Public evidence files: [diff_s87.json](../../evidence/220213855/historical/diff_s87.json), [diff_s87.png](../../evidence/220213855/historical/diff_s87.png), [gaia.json](../../evidence/220213855/historical/gaia.json), [measurements.json](../../evidence/220213855/measurements.json), [raw-events.png](../../evidence/220213855/raw-events.png), [raw-windows.csv](../../evidence/220213855/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch04/INDEX.md). 
