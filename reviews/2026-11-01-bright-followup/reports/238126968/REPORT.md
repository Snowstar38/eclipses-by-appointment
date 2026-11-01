# TIC 238126968: CONFIRMED

Full bounded review: **COMPLETE**. Actual Gaia DR3 G = 12.183063. The screening period and depth are historical selection values. Physical outcome and central catalogue novelty are separate.

1. **Raw repeated morphology.** Quality-zero QLP SAP_FLUX in representative downloaded sectors [6, 34, 88] contains 5 selected timing events. Local trapezoids fit free midpoint, depth, duration and baseline; historical predictions only select windows. Numeric windows and a raw event plot accompany this report. Flagged intervals are never clean nulls.
2. **Measured timing and aliases.** Same-kind midpoint regression gives P = 9.8959493292 ± 0.0000245311 d and epoch BTJD 1481.3039577, kind: Deeper repeating eclipse; even half-period cycles. Within-sector same-kind measured cycle pairs: [[34, 154, 156], [88, 450, 452]]. Only the deep even historical cycles enter the orbital fit; odd cycles are the shallower kind. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This bounded alias check does not claim an exhaustive all-period search.
3. **Target attribution.** Historical sector 88 TESScut difference image has deficit peak [8, 7] and target pixel [8, 7]; deficit centroid is 1.14 arcsec from the target coordinate. Image-model fractional residual 0.380 and centroid offset are descriptive, not calibrated localization uncertainties. Every brightness-capable Gaia neighbor within 60 arcsec under the historical screen: Gaia 5508449115088643712 (39.7 arcsec, G 14.211, intrinsic loss needed ~0.39); Gaia 5508448840210743424 (43.6 arcsec, G 14.129, intrinsic loss needed ~0.36). The intrinsic-loss budget is approximate and cannot be compared directly with blended pixel loss.
4. **Alternative reduction.** Background-subtracted TESScut 1×1/3×3/5×5 aperture depths are 43.9/38.6/32.0 ppt from 5 stacked events, versus median selected raw QLP depth 57.6 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Dilution and mixed eclipse kinds can change depths. Original cutout identity and SHA256 are in ../source-hashes.json.
5. **Gaia geometry.** Matched DR3 NSS source 5508448904633378560 has P = 9.8961317032 d and e = 0.04783; the closer edge-on conjunction differs from the measured epoch by -0.04622 d (-0.00467 phase). Its linearly propagated full source-specific NSS-covariance timing error is 0.13469 d, descriptive rather than a veto threshold. An approximate radius/minimum-mass central duration is 10.68 h against 10.48 h observed median; it is not a complete binary model.

**Decision and limitation.** Shallow and deep eclipses alternate at the historical 4.94798-day search interval. Five deep even-cycle midpoints give the 9.89595-day orbital period; shallow odd cycles support the alternating pattern. The available checks favor the target, subject to the stated pixel and timing limits.

**Next check.** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty is determined by the central seven-group and NSS coverage matrix at ../../shared-catalogues/coverage-matrix.csv; this physical review does not assert exhaustive literature priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Used in period fit |
|---|---:|---:|---:|---:|---|
| 6 | 1 | 1476.3505764 | 0.010417 | 31.5 | no: other kind or timing failure |
| 6 | 2 | 1481.2972292 | 0.010417 | 56.3 | yes |
| 6 | 3 | 1486.2477423 | 0.010417 | 30.8 | no: other kind or timing failure |
| 34 | 154 | 2233.4000168 | 0.005811 | 61.8 | yes |
| 34 | 155 | 2238.3421474 | 0.003472 | 29.8 | no: other kind or timing failure |
| 34 | 156 | 2243.2914492 | 0.005204 | 63.7 | yes |
| 88 | 449 | 3693.0496143 | 0.001157 | 34.9 | no: other kind or timing failure |
| 88 | 450 | 3697.9966498 | 0.001571 | 55.8 | yes |
| 88 | 451 | 3702.9451069 | 0.006515 | 31.3 | no: other kind or timing failure |
| 88 | 452 | 3707.8919600 | 0.003507 | 57.6 | yes |
| 88 | 453 | 3712.8416212 | 0.004982 | 26.7 | no: other kind or timing failure |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s88.json, historical/diff_s88.png, historical/gaia.json, ../pixel-contact.png, ../source-hashes.json and ../helper-audit.md. Original TESScut FITS: [local path omitted] File hashes are frozen in ../SHA256SUMS.json.


Stable review key: R478. Public evidence files: [diff_s88.json](../../evidence/238126968/historical/diff_s88.json), [diff_s88.png](../../evidence/238126968/historical/diff_s88.png), [gaia.json](../../evidence/238126968/historical/gaia.json), [measurements.json](../../evidence/238126968/measurements.json), [raw-events.png](../../evidence/238126968/raw-events.png), [raw-windows.csv](../../evidence/238126968/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch07/INDEX.md). 
