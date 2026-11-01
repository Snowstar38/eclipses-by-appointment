# TIC 348773879: CONFIRMED

Full bounded review: **COMPLETE**. Actual Gaia DR3 G = 12.169457. The screening period and depth are historical selection values. Physical outcome and central catalogue novelty are separate.

1. **Raw repeated morphology.** Quality-zero QLP SAP_FLUX in representative downloaded sectors [5, 32, 98] contains 8 selected timing events. Local trapezoids fit free midpoint, depth, duration and baseline; historical predictions only select windows. Numeric windows and a raw event plot accompany this report. Flagged intervals are never clean nulls.
2. **Measured timing and aliases.** Same-kind midpoint regression gives P = 7.2243136689 ± 0.0000079385 d and epoch BTJD 1458.0924122, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Within-sector same-kind measured cycle pairs: [[32, 102, 103], [32, 103, 104]]. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This bounded alias check does not claim an exhaustive all-period search.
3. **Target attribution.** Historical sector 98 TESScut difference image has deficit peak [8, 8] and target pixel [8, 8]; deficit centroid is 2.72 arcsec from the target coordinate. Image-model fractional residual 0.535 and centroid offset are descriptive, not calibrated localization uncertainties. Every brightness-capable Gaia neighbor within 60 arcsec under the historical screen: Gaia 2987292965757749376 (17.0 arcsec, G 11.841, intrinsic loss needed ~0.11). The intrinsic-loss budget is approximate and cannot be compared directly with blended pixel loss.
4. **Alternative reduction.** Background-subtracted TESScut 1×1/3×3/5×5 aperture depths are 49.9/32.8/30.9 ppt from 8 stacked events, versus median selected raw QLP depth 68.6 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Dilution and mixed eclipse kinds can change depths. Original cutout identity and SHA256 are in ../source-hashes.json.
5. **Gaia geometry.** Matched DR3 NSS source 2987292862678534144 has P = 7.2246361222 d and e = 0.04277; the closer edge-on conjunction differs from the measured epoch by -0.09908 d (-0.01371 phase). Its linearly propagated full source-specific NSS-covariance timing error is 0.12913 d, descriptive rather than a veto threshold. An approximate radius/minimum-mass central duration is 5.95 h against 3.98 h observed median; it is not a complete binary model.

**Decision and limitation.** The capable 17.0-arcsec neighbor is about a pixel away; the deficit core falls much closer to the target. Attribution favors the target at TESS resolution, with uncalibrated subpixel precision. The available checks favor the target, subject to the stated pixel and timing limits.

**Next check.** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty is determined by the central seven-group and NSS coverage matrix at ../../shared-catalogues/coverage-matrix.csv; this physical review does not assert exhaustive literature priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Used in period fit |
|---|---:|---:|---:|---:|---|
| 5 | 2 | 1458.0902329 | 0.010417 | 64.7 | yes |
| 32 | 102 | 2180.5237896 | 0.003472 | 72.0 | yes |
| 32 | 103 | 2187.7480351 | 0.003472 | 73.9 | yes |
| 32 | 104 | 2194.9728229 | 0.003472 | 75.0 | yes |
| 98 | 354 | 4001.0507308 | 0.001157 | 68.6 | yes |
| 98 | 356 | 4015.4991851 | 0.001157 | 68.6 | yes |
| 98 | 358 | 4029.9484542 | 0.001157 | 67.6 | yes |
| 98 | 360 | 4044.3966744 | 0.001157 | 66.7 | yes |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s98.json, historical/diff_s98.png, historical/gaia.json, ../pixel-contact.png, ../source-hashes.json and ../helper-audit.md. Original TESScut FITS: [local path omitted] File hashes are frozen in ../SHA256SUMS.json.


Stable review key: R473. Public evidence files: [diff_s98.json](../../evidence/348773879/historical/diff_s98.json), [diff_s98.png](../../evidence/348773879/historical/diff_s98.png), [gaia.json](../../evidence/348773879/historical/gaia.json), [measurements.json](../../evidence/348773879/measurements.json), [raw-events.png](../../evidence/348773879/raw-events.png), [raw-windows.csv](../../evidence/348773879/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch07/INDEX.md). 
