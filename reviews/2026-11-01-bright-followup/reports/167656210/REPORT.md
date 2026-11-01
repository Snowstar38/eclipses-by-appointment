# TIC 167656210: PROBABLE

Full bounded review: **COMPLETE**. Actual Gaia DR3 G = 12.166932. The screening period and depth are historical selection values. Physical outcome and central catalogue novelty are separate.

1. **Raw repeated morphology.** Quality-zero QLP SAP_FLUX in representative downloaded sectors [36, 98] contains 22 selected timing events. Local trapezoids fit free midpoint, depth, duration and baseline; historical predictions only select windows. Numeric windows and a raw event plot accompany this report. Flagged intervals are never clean nulls.
2. **Measured timing and aliases.** Same-kind midpoint regression gives P = 2.2517814962 ± 0.0000017527 d and epoch BTJD 2284.0975046, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Within-sector same-kind measured cycle pairs: [[36, 412, 413], [36, 413, 414], [36, 414, 415], [36, 420, 421], [98, 1172, 1173], [98, 1173, 1174], [98, 1174, 1175], [98, 1179, 1180], [98, 1180, 1181], [98, 1185, 1186], [98, 1186, 1187], [98, 1187, 1188], [98, 1191, 1192], [98, 1192, 1193], [98, 1193, 1194]]. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This bounded alias check does not claim an exhaustive all-period search.
3. **Target attribution.** Historical sector 97 TESScut difference image has deficit peak [8, 8] and target pixel [8, 8]; deficit centroid is 4.63 arcsec from the target coordinate. Image-model fractional residual 0.652 and centroid offset are descriptive, not calibrated localization uncertainties. Every brightness-capable Gaia neighbor within 60 arcsec under the historical screen: Gaia 5480019042928976896 (2.9 arcsec, G 14.551, intrinsic loss needed ~0.24). The intrinsic-loss budget is approximate and cannot be compared directly with blended pixel loss.
4. **Alternative reduction.** Background-subtracted TESScut 1×1/3×3/5×5 aperture depths are 21.2/21.7/21.5 ppt from 23 stacked events, versus median selected raw QLP depth 23.1 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Dilution and mixed eclipse kinds can change depths. Original cutout identity and SHA256 are in ../source-hashes.json.
5. **Gaia geometry.** Matched DR3 NSS source 5480019038632380288 has P = 2.2517090090 d and e = 0.03953; the closer edge-on conjunction differs from the measured epoch by 0.04866 d (0.02161 phase). Its linearly propagated full source-specific NSS-covariance timing error is 0.09510 d, descriptive rather than a veto threshold. An approximate radius/minimum-mass central duration is 4.78 h against 2.22 h observed median; it is not a complete binary model.

**Decision and limitation.** A 2.9-arcsec capable Gaia neighbor shares the TESS core. The recurring eclipses are real, but these pixels cannot uniquely assign them to the selected Gaia star. Attribution remains unresolved after the completed pixel check.

**Next check.** Resolved time-series photometry or multi-source PRF fitting of the 2.9-arcsec pair.

Catalogue novelty is determined by the central seven-group and NSS coverage matrix at ../../shared-catalogues/coverage-matrix.csv; this physical review does not assert exhaustive literature priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Used in period fit |
|---|---:|---:|---:|---:|---|
| 36 | 412 | 2284.0978758 | 0.003472 | 25.4 | yes |
| 36 | 413 | 2286.3495175 | 0.003472 | 25.4 | yes |
| 36 | 414 | 2288.6013787 | 0.003472 | 23.9 | yes |
| 36 | 415 | 2290.8530233 | 0.003472 | 24.8 | yes |
| 36 | 418 | 2297.6081832 | 0.003472 | 26.0 | yes |
| 36 | 420 | 2302.1110686 | 0.003472 | 24.3 | yes |
| 36 | 421 | 2304.3631005 | 0.003472 | 25.4 | yes |
| 98 | 1172 | 3995.4520614 | 0.001157 | 23.0 | yes |
| 98 | 1173 | 3997.7025415 | 0.001157 | 22.1 | yes |
| 98 | 1174 | 3999.9547706 | 0.001157 | 22.0 | yes |
| 98 | 1175 | 4002.2074201 | 0.001157 | 21.9 | yes |
| 98 | 1179 | 4011.2131845 | 0.001157 | 23.9 | yes |
| 98 | 1180 | 4013.4668097 | 0.001157 | 22.9 | yes |
| 98 | 1181 | 4015.7173665 | 0.001157 | 23.3 | yes |
| 98 | 1185 | 4024.7241694 | 0.001157 | 24.1 | yes |
| 98 | 1186 | 4026.9757790 | 0.001157 | 23.3 | yes |
| 98 | 1187 | 4029.2286132 | 0.001157 | 21.9 | yes |
| 98 | 1188 | 4031.4798496 | 0.001157 | 22.7 | yes |
| 98 | 1191 | 4038.2353658 | 0.001157 | 21.5 | yes |
| 98 | 1192 | 4040.4869257 | 0.001157 | 21.9 | yes |
| 98 | 1193 | 4042.7383739 | 0.001157 | 22.2 | yes |
| 98 | 1194 | 4044.9912545 | 0.001157 | 21.2 | yes |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s97.json, historical/diff_s97.png, historical/gaia.json, ../pixel-contact.png, ../source-hashes.json and ../helper-audit.md. Original TESScut FITS: [local path omitted] File hashes are frozen in ../SHA256SUMS.json.


Stable review key: R472. Public evidence files: [diff_s97.json](../../evidence/167656210/historical/diff_s97.json), [diff_s97.png](../../evidence/167656210/historical/diff_s97.png), [gaia.json](../../evidence/167656210/historical/gaia.json), [measurements.json](../../evidence/167656210/measurements.json), [raw-events.png](../../evidence/167656210/raw-events.png), [raw-windows.csv](../../evidence/167656210/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch07/INDEX.md). 
