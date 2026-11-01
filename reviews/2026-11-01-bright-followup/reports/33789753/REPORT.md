# TIC 33789753: CONFIRMED

Full bounded review: **COMPLETE**. Actual Gaia DR3 G = 12.174696. The screening period and depth are historical selection values. Physical outcome and central catalogue novelty are separate.

1. **Raw repeated morphology.** Quality-zero QLP SAP_FLUX in representative downloaded sectors [6, 33, 87] contains 5 selected timing events. Local trapezoids fit free midpoint, depth, duration and baseline; historical predictions only select windows. Numeric windows and a raw event plot accompany this report. Flagged intervals are never clean nulls.
2. **Measured timing and aliases.** Same-kind midpoint regression gives P = 13.1035976171 ± 0.0000219313 d and epoch BTJD 1475.8796596, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Within-sector same-kind measured cycle pairs: [[6, 0, 1], [33, 56, 57]]. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This bounded alias check does not claim an exhaustive all-period search.
3. **Target attribution.** Historical sector 6 TESScut difference image has deficit peak [7, 8] and target pixel [7, 8]; deficit centroid is 0.63 arcsec from the target coordinate. Image-model fractional residual 0.947 and centroid offset are descriptive, not calibrated localization uncertainties. Every brightness-capable Gaia neighbor within 60 arcsec under the historical screen: None under the approximate G-band brightness budget. The intrinsic-loss budget is approximate and cannot be compared directly with blended pixel loss.
4. **Alternative reduction.** Background-subtracted TESScut 1×1/3×3/5×5 aperture depths are 153.5/148.6/104.3 ppt from 2 stacked events, versus median selected raw QLP depth 160.9 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Dilution and mixed eclipse kinds can change depths. Original cutout identity and SHA256 are in ../source-hashes.json.
5. **Gaia geometry.** Matched DR3 NSS source 2993617253561277056 has P = 13.1020129210 d and e = 0.41294; the closer edge-on conjunction differs from the measured epoch by 0.17799 d (0.01359 phase). Its linearly propagated full source-specific NSS-covariance timing error is 0.22281 d, descriptive rather than a veto threshold. An approximate radius/minimum-mass central duration is 10.15 h against 6.59 h observed median; it is not a complete binary model.

**Decision and limitation.** Five raw events in S6/S33/S87 agree in timing and shape. No brightness-capable Gaia neighbor appears within 60 arcsec. The available checks favor the target, subject to the stated pixel and timing limits.

**Next check.** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty is determined by the central seven-group and NSS coverage matrix at ../../shared-catalogues/coverage-matrix.csv; this physical review does not assert exhaustive literature priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Used in period fit |
|---|---:|---:|---:|---:|---|
| 6 | 0 | 1475.8797672 | 0.010417 | 158.8 | yes |
| 6 | 1 | 1488.9828743 | 0.010417 | 151.3 | yes |
| 33 | 56 | 2209.6814606 | 0.003472 | 163.4 | yes |
| 33 | 57 | 2222.7844323 | 0.003472 | 163.7 | yes |
| 87 | 168 | 3677.2840579 | 0.001157 | 160.9 | yes |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s06.json, historical/diff_s06.png, historical/gaia.json, ../pixel-contact.png, ../source-hashes.json and ../helper-audit.md. Original TESScut FITS: [local path omitted] File hashes are frozen in ../SHA256SUMS.json.


Stable review key: R476. Public evidence files: [diff_s06.json](../../evidence/33789753/historical/diff_s06.json), [diff_s06.png](../../evidence/33789753/historical/diff_s06.png), [gaia.json](../../evidence/33789753/historical/gaia.json), [measurements.json](../../evidence/33789753/measurements.json), [raw-events.png](../../evidence/33789753/raw-events.png), [raw-windows.csv](../../evidence/33789753/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch07/INDEX.md). 
