# TIC 141923153: CONFIRMED

Full bounded review: **COMPLETE**. Actual Gaia DR3 G = 12.162264. The screening period and depth are historical selection values. Physical outcome and central catalogue novelty are separate.

1. **Raw repeated morphology.** Quality-zero QLP SAP_FLUX in representative downloaded sectors [7, 34] contains 7 selected timing events. Local trapezoids fit free midpoint, depth, duration and baseline; historical predictions only select windows. Numeric windows and a raw event plot accompany this report. Flagged intervals are never clean nulls.
2. **Measured timing and aliases.** Same-kind midpoint regression gives P = 6.4308327985 ± 0.0000546344 d and epoch BTJD 1499.2038780, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Within-sector same-kind measured cycle pairs: [[7, 1, 2], [7, 2, 3], [34, 115, 116], [34, 116, 117], [34, 117, 118]]. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This bounded alias check does not claim an exhaustive all-period search.
3. **Target attribution.** Historical sector 34 TESScut difference image has deficit peak [8, 8] and target pixel [8, 8]; deficit centroid is 1.01 arcsec from the target coordinate. Image-model fractional residual 0.811 and centroid offset are descriptive, not calibrated localization uncertainties. Every brightness-capable Gaia neighbor within 60 arcsec under the historical screen: Gaia 5710669575691823360 (51.6 arcsec, G 13.425, intrinsic loss needed ~0.64). The intrinsic-loss budget is approximate and cannot be compared directly with blended pixel loss.
4. **Alternative reduction.** Background-subtracted TESScut 1×1/3×3/5×5 aperture depths are 159.4/137.3/101.6 ppt from 4 stacked events, versus median selected raw QLP depth 162.5 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Dilution and mixed eclipse kinds can change depths. Original cutout identity and SHA256 are in ../source-hashes.json.
5. **Gaia geometry.** Matched DR3 NSS source 5710669537024684416 has P = 6.4302209846 d and e = 0.11073; the closer edge-on conjunction differs from the measured epoch by 0.05310 d (0.00826 phase). Its linearly propagated full source-specific NSS-covariance timing error is 0.11745 d, descriptive rather than a veto threshold. An approximate radius/minimum-mass central duration is 5.55 h against 3.89 h observed median; it is not a complete binary model.

**Decision and limitation.** Consecutive raw eclipses in S7 and S34 support recurrence; the capable 51.6-arcsec neighbor is separated from the target-centered deficit despite substantial image-model residual. The available checks favor the target, subject to the stated pixel and timing limits.

**Next check.** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty is determined by the central seven-group and NSS coverage matrix at ../../shared-catalogues/coverage-matrix.csv; this physical review does not assert exhaustive literature priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Used in period fit |
|---|---:|---:|---:|---:|---|
| 7 | 1 | 1499.2038586 | 0.010417 | 143.7 | yes |
| 7 | 2 | 1505.6327667 | 0.010417 | 135.6 | yes |
| 7 | 3 | 1512.0675010 | 0.010417 | 154.3 | yes |
| 34 | 115 | 2232.3188695 | 0.003472 | 162.5 | yes |
| 34 | 116 | 2238.7498281 | 0.003472 | 167.0 | yes |
| 34 | 117 | 2245.1802637 | 0.003472 | 165.3 | yes |
| 34 | 118 | 2251.6113041 | 0.003472 | 167.5 | yes |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s34.json, historical/diff_s34.png, historical/gaia.json, ../pixel-contact.png, ../source-hashes.json and ../helper-audit.md. Original TESScut FITS: [local path omitted] File hashes are frozen in ../SHA256SUMS.json.


Stable review key: R471. Public evidence files: [diff_s34.json](../../evidence/141923153/historical/diff_s34.json), [diff_s34.png](../../evidence/141923153/historical/diff_s34.png), [gaia.json](../../evidence/141923153/historical/gaia.json), [measurements.json](../../evidence/141923153/measurements.json), [raw-events.png](../../evidence/141923153/raw-events.png), [raw-windows.csv](../../evidence/141923153/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch07/INDEX.md). 
