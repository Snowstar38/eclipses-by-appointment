# TIC 24524336: CONFIRMED

Full bounded review: **COMPLETE**. Actual Gaia DR3 G = 12.159077. The screening period and depth are historical selection values. Physical outcome and central catalogue novelty are separate.

1. **Raw repeated morphology.** Quality-zero QLP SAP_FLUX in representative downloaded sectors [32, 98] contains 6 selected timing events. Local trapezoids fit free midpoint, depth, duration and baseline; historical predictions only select windows. Numeric windows and a raw event plot accompany this report. Flagged intervals are never clean nulls.
2. **Measured timing and aliases.** Same-kind midpoint regression gives P = 7.5496432496 ± 0.0000103723 d and epoch BTJD 2179.2995260, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Within-sector same-kind measured cycle pairs: []. Flagged intervening cycles are not negative detections; cross-sector parity and within-sector spacing discriminate the alias. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This bounded alias check does not claim an exhaustive all-period search.
3. **Target attribution.** Historical sector 33 TESScut difference image has deficit peak [8, 8] and target pixel [8, 8]; deficit centroid is 4.73 arcsec from the target coordinate. Image-model fractional residual 0.349 and centroid offset are descriptive, not calibrated localization uncertainties. Every brightness-capable Gaia neighbor within 60 arcsec under the historical screen: Gaia 2901581709342471552 (44.6 arcsec, G 13.129, intrinsic loss needed ~0.45). The intrinsic-loss budget is approximate and cannot be compared directly with blended pixel loss.
4. **Alternative reduction.** Background-subtracted TESScut 1×1/3×3/5×5 aperture depths are 141.0/137.2/117.4 ppt from 4 stacked events, versus median selected raw QLP depth 123.3 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Dilution and mixed eclipse kinds can change depths. Original cutout identity and SHA256 are in ../source-hashes.json.
5. **Gaia geometry.** Matched DR3 NSS source 2901581915500902912 has P = 7.5496902503 d and e = 0.03847; the closer edge-on conjunction differs from the measured epoch by 0.04453 d (0.00590 phase). Its linearly propagated full source-specific NSS-covariance timing error is 0.12718 d, descriptive rather than a veto threshold. An approximate radius/minimum-mass central duration is 4.40 h against 3.01 h observed median; it is not a complete binary model.

**Decision and limitation.** S32 cycles 98/100 and S98 cycles 339/341/343/345 have opposite half-period parity. Intervening windows are quality-flagged, not clean nulls. The within-sector 15.099-day spacing together with cross-sector parity excludes a constant doubled period. The available checks favor the target, subject to the stated pixel and timing limits.

**Next check.** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty is determined by the central seven-group and NSS coverage matrix at ../../shared-catalogues/coverage-matrix.csv; this physical review does not assert exhaustive literature priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Used in period fit |
|---|---:|---:|---:|---:|---|
| 32 | 98 | 2179.2996811 | 0.003472 | 137.4 | yes |
| 32 | 100 | 2194.3986515 | 0.003472 | 135.5 | yes |
| 98 | 339 | 3998.7636658 | 0.001157 | 121.5 | yes |
| 98 | 341 | 4013.8628696 | 0.001157 | 122.6 | yes |
| 98 | 343 | 4028.9617662 | 0.001157 | 122.5 | yes |
| 98 | 345 | 4044.0616145 | 0.001157 | 124.1 | yes |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s33.json, historical/diff_s33.png, historical/gaia.json, ../pixel-contact.png, ../source-hashes.json and ../helper-audit.md. Original TESScut FITS: [local path omitted] File hashes are frozen in ../SHA256SUMS.json.


Stable review key: R470. Public evidence files: [diff_s33.json](../../evidence/24524336/historical/diff_s33.json), [diff_s33.png](../../evidence/24524336/historical/diff_s33.png), [gaia.json](../../evidence/24524336/historical/gaia.json), [measurements.json](../../evidence/24524336/measurements.json), [raw-events.png](../../evidence/24524336/raw-events.png), [raw-windows.csv](../../evidence/24524336/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch07/INDEX.md). 
