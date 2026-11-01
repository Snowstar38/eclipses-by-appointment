# TIC 99493790: CONFIRMED

Full bounded review: **COMPLETE**. Actual Gaia DR3 G = 12.170427. The screening period and depth are historical selection values. Physical outcome and central catalogue novelty are separate.

1. **Raw repeated morphology.** Quality-zero QLP SAP_FLUX in representative downloaded sectors [1, 28, 92] contains 7 selected timing events. Local trapezoids fit free midpoint, depth, duration and baseline; historical predictions only select windows. Numeric windows and a raw event plot accompany this report. Flagged intervals are never clean nulls.
2. **Measured timing and aliases.** Same-kind midpoint regression gives P = 7.7646935289 ± 0.0000090716 d and epoch BTJD 1332.9819065, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Within-sector same-kind measured cycle pairs: [[28, 94, 95], [28, 95, 96], [92, 319, 320], [92, 320, 321]]. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This bounded alias check does not claim an exhaustive all-period search.
3. **Target attribution.** Historical sector 28 TESScut difference image has deficit peak [7, 7] and target pixel [7, 7]; deficit centroid is 3.68 arcsec from the target coordinate. Image-model fractional residual 0.999 and centroid offset are descriptive, not calibrated localization uncertainties. Every brightness-capable Gaia neighbor within 60 arcsec under the historical screen: None under the approximate G-band brightness budget. The intrinsic-loss budget is approximate and cannot be compared directly with blended pixel loss.
4. **Alternative reduction.** Background-subtracted TESScut 1×1/3×3/5×5 aperture depths are 21.8/21.2/18.7 ppt from 3 stacked events, versus median selected raw QLP depth 21.9 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Dilution and mixed eclipse kinds can change depths. Original cutout identity and SHA256 are in ../source-hashes.json.
5. **Gaia geometry.** Matched DR3 NSS source 6804708139515008640 has P = 7.7653086675 d and e = 0.08951; the closer edge-on conjunction differs from the measured epoch by 0.05671 d (0.00730 phase). Its linearly propagated full source-specific NSS-covariance timing error is 0.33323 d, descriptive rather than a veto threshold. An approximate radius/minimum-mass central duration is 3.89 h against 3.26 h observed median; it is not a complete binary model.

**Decision and limitation.** The target-centered deficit and absence of a brightness-capable Gaia neighbor favor attribution; the image-model residual is high. The available checks favor the target, subject to the stated pixel and timing limits.

**Next check.** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty is determined by the central seven-group and NSS coverage matrix at ../../shared-catalogues/coverage-matrix.csv; this physical review does not assert exhaustive literature priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Used in period fit |
|---|---:|---:|---:|---:|---|
| 1 | 0 | 1332.9829705 | 0.010417 | 21.3 | yes |
| 28 | 94 | 2062.8634721 | 0.003472 | 19.9 | yes |
| 28 | 95 | 2070.6273013 | 0.003472 | 23.3 | yes |
| 28 | 96 | 2078.3924097 | 0.003472 | 23.3 | yes |
| 92 | 319 | 3809.9196418 | 0.001158 | 21.9 | yes |
| 92 | 320 | 3817.6833970 | 0.001158 | 23.3 | yes |
| 92 | 321 | 3825.4484769 | 0.001158 | 21.4 | yes |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s28.json, historical/diff_s28.png, historical/gaia.json, ../pixel-contact.png, ../source-hashes.json and ../helper-audit.md. Original TESScut FITS: [local path omitted] File hashes are frozen in ../SHA256SUMS.json.


Stable review key: R474. Public evidence files: [diff_s28.json](../../evidence/99493790/historical/diff_s28.json), [diff_s28.png](../../evidence/99493790/historical/diff_s28.png), [gaia.json](../../evidence/99493790/historical/gaia.json), [measurements.json](../../evidence/99493790/measurements.json), [raw-events.png](../../evidence/99493790/raw-events.png), [raw-windows.csv](../../evidence/99493790/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch07/INDEX.md). 
