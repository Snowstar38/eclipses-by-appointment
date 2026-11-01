# TIC 220410034: CONFIRMED

Full bounded review: **COMPLETE**. Actual Gaia DR3 G = 12.185472. The screening period and depth are historical selection values. Physical outcome and central catalogue novelty are separate.

1. **Raw repeated morphology.** Quality-zero QLP SAP_FLUX in representative downloaded sectors [36, 98] contains 6 selected timing events. Local trapezoids fit free midpoint, depth, duration and baseline; historical predictions only select windows. Numeric windows and a raw event plot accompany this report. Flagged intervals are never clean nulls.
2. **Measured timing and aliases.** Same-kind midpoint regression gives P = 9.2219086085 ± 0.0000134411 d and epoch BTJD 2282.9417514, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Within-sector same-kind measured cycle pairs: [[98, 285, 286]]. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This bounded alias check does not claim an exhaustive all-period search.
3. **Target attribution.** Historical sector 97 TESScut difference image has deficit peak [7, 8] and target pixel [7, 8]; deficit centroid is 2.28 arcsec from the target coordinate. Image-model fractional residual 0.209 and centroid offset are descriptive, not calibrated localization uncertainties. Every brightness-capable Gaia neighbor within 60 arcsec under the historical screen: None under the approximate G-band brightness budget. The intrinsic-loss budget is approximate and cannot be compared directly with blended pixel loss.
4. **Alternative reduction.** Background-subtracted TESScut 1×1/3×3/5×5 aperture depths are 54.9/54.8/54.3 ppt from 4 stacked events, versus median selected raw QLP depth 48.7 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Dilution and mixed eclipse kinds can change depths. Original cutout identity and SHA256 are in ../source-hashes.json.
5. **Gaia geometry.** Matched DR3 NSS source 4777341154688327424 has P = 9.2219102799 d and e = 0.08597; the closer edge-on conjunction differs from the measured epoch by -0.21615 d (-0.02344 phase). Its linearly propagated full source-specific NSS-covariance timing error is 0.40158 d, descriptive rather than a veto threshold. An approximate radius/minimum-mass central duration is 4.68 h against 2.82 h observed median; it is not a complete binary model.

**Decision and limitation.** S98 contains measured eclipses in both parity classes of the historical period, excluding a simple double-period alias. No brightness-capable Gaia neighbor appears within 60 arcsec. The available checks favor the target, subject to the stated pixel and timing limits.

**Next check.** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty is determined by the central seven-group and NSS coverage matrix at ../../shared-catalogues/coverage-matrix.csv; this physical review does not assert exhaustive literature priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Used in period fit |
|---|---:|---:|---:|---:|---|
| 36 | 97 | 2282.9418398 | 0.003472 | 54.7 | yes |
| 36 | 99 | 2301.3854303 | 0.003472 | 57.7 | yes |
| 98 | 283 | 3998.2166875 | 0.001157 | 48.4 | yes |
| 98 | 285 | 4016.6611258 | 0.001157 | 49.0 | yes |
| 98 | 286 | 4025.8823212 | 0.001157 | 48.0 | yes |
| 98 | 288 | 4044.3259673 | 0.001157 | 47.7 | yes |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s97.json, historical/diff_s97.png, historical/gaia.json, ../pixel-contact.png, ../source-hashes.json and ../helper-audit.md. Original TESScut FITS: [local path omitted] File hashes are frozen in ../SHA256SUMS.json.


Stable review key: R479. Public evidence files: [diff_s97.json](../../evidence/220410034/historical/diff_s97.json), [diff_s97.png](../../evidence/220410034/historical/diff_s97.png), [gaia.json](../../evidence/220410034/historical/gaia.json), [measurements.json](../../evidence/220410034/measurements.json), [raw-events.png](../../evidence/220410034/raw-events.png), [raw-windows.csv](../../evidence/220410034/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch07/INDEX.md). 
