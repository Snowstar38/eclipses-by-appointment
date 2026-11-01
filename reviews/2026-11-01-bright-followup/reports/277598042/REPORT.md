# TIC 277598042: CONFIRMED

**Full bounded review: COMPLETE.** Physical outcome, catalogue novelty and historical screening label are separate.

1. **Repeated raw morphology.** 14 timing-usable measured eclipses in quality-zero QLP SAP_FLUX across representative sectors [13, 92, 94]. The local fit has a free center, depth, width and baseline. Predicted centers select inspection windows; flagged and uncovered windows are not clean nulls. Raw points are preserved in `raw-windows.csv` and `raw-events.png`.
2. **Measured timing and aliases.** P = 4.4364264100 ± 0.0000120101 d, reference BTJD 1665.9805449 (Selected repeating eclipse; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; deeper/secondary identity not independently established. Adjacent-cycle and parity summaries are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive all-period search.
3. **Pixel attribution.** The S94 TESScut deficit centroid is 4.11 arcsec from the target coordinate. Peak deficit pixel [7, 7]; target pixel [7, 7]. Image-model fractional residual 0.279 is not a calibrated centroid error. The table below lists every Gaia neighbor in the 60-arcsec screen that can supply the selected depth under an approximate flux-budget calculation. Required intrinsic eclipse depth is not a blended pixel loss.
4. **Alternative reduction.** Target-centered, background-subtracted cutout apertures combining 6 predicted event windows give 1x1/3x3/5x5 depths 138.22/120.70/109.60 ppt; median selected QLP raw fit depth is 151.33 ppt. The stack does not by itself prove each cutout window contains an eclipse. The cutout and selected QLP observations use the same TESS sector and share photons; this is an alternative reduction, not an independent observing occasion. Aperture dilution and selected-event differences limit depth equality.
5. **Gaia geometry.** Source 6732852653768547840 has orbital P = 4.435881632 d and e = 0.0840. The nearest edge-on conjunction is offset by +0.0447 d (+0.0101 phase) at the measured reference epoch. Full source-specific NSS covariance gives a descriptive linear timing scale of 0.1250 d. Approximate central duration 4.98 h versus observed median 4.68 h. Assumed TIC radius and minimum-mass companion make this a plausibility check, not a fitted binary model or sigma veto.

**Deciding interpretation and limitation:** Fourteen raw events span S13, S92 and S94 with multiple adjacent cycles. The S94 difference core lies near the target and about 20 arcsec from the only capable Gaia neighbor; that neighbor would need an approximately 80% intrinsic eclipse.

**Next check:** Optional resolved photometry.

Catalogue novelty: the central seven-group result in `../../shared-catalogues/coverage-matrix.csv` reports complete scoped checks with no identified prior EB match. It does not establish exhaustive literature priority or resolve embargoed identities.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt |
|---:|---:|---:|---:|---:|
| 13 | 1 | 1665.9831857 | 0.010417 | 149.68 |
| 13 | 2 | 1670.4154686 | 0.010417 | 155.48 |
| 13 | 3 | 1674.8520864 | 0.010417 | 152.99 |
| 92 | 483 | 3804.3384462 | 0.001157 | 162.28 |
| 92 | 484 | 3808.7745133 | 0.001157 | 162.52 |
| 92 | 486 | 3817.6473162 | 0.001157 | 161.61 |
| 92 | 487 | 3822.0834577 | 0.001157 | 161.63 |
| 92 | 488 | 3826.5201663 | 0.001157 | 160.54 |
| 94 | 495 | 3857.5750328 | 0.001157 | 142.98 |
| 94 | 496 | 3862.0116368 | 0.001157 | 139.06 |
| 94 | 497 | 3866.4480830 | 0.001157 | 138.32 |
| 94 | 498 | 3870.8844811 | 0.001157 | 141.72 |
| 94 | 499 | 3875.3211812 | 0.001157 | 140.58 |
| 94 | 500 | 3879.7571485 | 0.001157 | 141.77 |

Capable Gaia neighbors:

| Gaia DR3 source | Target separation arcsec | G | Required intrinsic eclipse fraction | Deficit separation arcsec |
|---|---:|---:|---:|---:|
| 6732864026841949952 | 15.82 | 13.858 | 0.797 | 19.9 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../download-receipts.json`, `../alias-audit.json`, `../gaia-geometry.json`, `historical/diff_s94.json`, `historical/diff_s94.png`, `historical/gaia.json`, original `[local path omitted], and `../helper-audit.md`. All file hashes are in `../SHA256SUMS.json`.


Stable review key: R536. Public evidence files: [diff_s94.json](../../evidence/277598042/historical/diff_s94.json), [diff_s94.png](../../evidence/277598042/historical/diff_s94.png), [gaia.json](../../evidence/277598042/historical/gaia.json), [measurements.json](../../evidence/277598042/measurements.json), [raw-events.png](../../evidence/277598042/raw-events.png), [raw-windows.csv](../../evidence/277598042/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch03/INDEX.md). 
