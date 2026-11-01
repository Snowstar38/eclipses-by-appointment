# TIC 330469458: CONFIRMED

Full bounded review: **COMPLETE**. Actual Gaia DR3 G = 12.182403. The screening period and depth are historical selection values. Physical outcome and central catalogue novelty are separate.

1. **Raw repeated morphology.** Quality-zero QLP SAP_FLUX in representative downloaded sectors [16, 83] contains 5 selected timing events. Local trapezoids fit free midpoint, depth, duration and baseline; historical predictions only select windows. Numeric windows and a raw event plot accompany this report. Flagged intervals are never clean nulls.
2. **Measured timing and aliases.** Same-kind midpoint regression gives P = 7.1007431519 ± 0.0000403912 d and epoch BTJD 1742.5447026, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Within-sector same-kind measured cycle pairs: [[83, 256, 257], [83, 257, 258], [83, 258, 259]]. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This bounded alias check does not claim an exhaustive all-period search.
3. **Target attribution.** Historical sector 83 TESScut difference image has deficit peak [7, 8] and target pixel [7, 8]; deficit centroid is 5.88 arcsec from the target coordinate. Image-model fractional residual 0.717 and centroid offset are descriptive, not calibrated localization uncertainties. Every brightness-capable Gaia neighbor within 60 arcsec under the historical screen: Gaia 1906480221138868736 (46.3 arcsec, G 12.790, intrinsic loss needed ~0.37). The intrinsic-loss budget is approximate and cannot be compared directly with blended pixel loss.
4. **Alternative reduction.** Background-subtracted TESScut 1×1/3×3/5×5 aperture depths are 136.4/123.7/73.9 ppt from 4 stacked events, versus median selected raw QLP depth 145.7 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Dilution and mixed eclipse kinds can change depths. Original cutout identity and SHA256 are in ../source-hashes.json.
5. **Gaia geometry.** Matched DR3 NSS source 1906480289858343040 has P = 7.1014333035 d and e = 0.03164; the closer edge-on conjunction differs from the measured epoch by -0.13985 d (-0.01969 phase). Its linearly propagated full source-specific NSS-covariance timing error is 0.16156 d, descriptive rather than a veto threshold. An approximate radius/minimum-mass central duration is 5.78 h against 4.11 h observed median; it is not a complete binary model.

**Decision and limitation.** Five deep raw events in S16/S83 recur at the measured period. A capable neighbor 46.3 arcsec away is distinct from the target-centered deficit. The available checks favor the target, subject to the stated pixel and timing limits.

**Next check.** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty is determined by the central seven-group and NSS coverage matrix at ../../shared-catalogues/coverage-matrix.csv; this physical review does not assert exhaustive literature priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Used in period fit |
|---|---:|---:|---:|---:|---|
| 16 | 0 | 1742.5446985 | 0.010416 | 131.1 | yes |
| 83 | 256 | 3560.3350331 | 0.001157 | 146.5 | yes |
| 83 | 257 | 3567.4355511 | 0.001157 | 145.7 | yes |
| 83 | 258 | 3574.5364814 | 0.001157 | 143.8 | yes |
| 83 | 259 | 3581.6371914 | 0.001157 | 148.0 | yes |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s83.json, historical/diff_s83.png, historical/gaia.json, ../pixel-contact.png, ../source-hashes.json and ../helper-audit.md. Original TESScut FITS: [local path omitted] File hashes are frozen in ../SHA256SUMS.json.


Stable review key: R477. Public evidence files: [diff_s83.json](../../evidence/330469458/historical/diff_s83.json), [diff_s83.png](../../evidence/330469458/historical/diff_s83.png), [gaia.json](../../evidence/330469458/historical/gaia.json), [measurements.json](../../evidence/330469458/measurements.json), [raw-events.png](../../evidence/330469458/raw-events.png), [raw-windows.csv](../../evidence/330469458/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch07/INDEX.md). 
