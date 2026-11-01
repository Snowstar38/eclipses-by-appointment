# TIC 440168538: CONFIRMED

**Full bounded review: COMPLETE.** Physical outcome, catalogue novelty and historical screening label are separate.

1. **Repeated raw morphology.** 4 timing-usable measured eclipses in quality-zero QLP SAP_FLUX across representative sectors [57, 84]. The local fit has a free center, depth, width and baseline. Predicted centers select inspection windows; flagged and uncovered windows are not clean nulls. Raw points are preserved in `raw-windows.csv` and `raw-events.png`.
2. **Measured timing and aliases.** P = 11.3630365737 ± 0.0000180823 d, reference BTJD 2861.0881487 (Selected repeating eclipse; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; deeper/secondary identity not independently established. Adjacent-cycle and parity summaries are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive all-period search.
3. **Pixel attribution.** The S57 TESScut deficit centroid is 2.24 arcsec from the target coordinate. Peak deficit pixel [8, 7]; target pixel [8, 7]. Image-model fractional residual 0.766 is not a calibrated centroid error. The table below lists every Gaia neighbor in the 60-arcsec screen that can supply the selected depth under an approximate flux-budget calculation. Required intrinsic eclipse depth is not a blended pixel loss.
4. **Alternative reduction.** Target-centered, background-subtracted cutout apertures combining 2 predicted event windows give 1x1/3x3/5x5 depths 58.62/56.89/53.38 ppt; median selected QLP raw fit depth is 59.24 ppt. The stack does not by itself prove each cutout window contains an eclipse. The cutout and selected QLP observations use the same TESS sector and share photons; this is an alternative reduction, not an independent observing occasion. Aperture dilution and selected-event differences limit depth equality.
5. **Gaia geometry.** Source 391817260687992960 has orbital P = 11.362526050 d and e = 0.0213. The nearest edge-on conjunction is offset by +0.2062 d (+0.0181 phase) at the measured reference epoch. Full source-specific NSS covariance gives a descriptive linear timing scale of 0.3661 d. Approximate central duration 7.55 h versus observed median 4.46 h. Assumed TIC radius and minimum-mass companion make this a plausibility check, not a fitted binary model or sigma veto.

**Deciding interpretation and limitation:** Two adjacent raw eclipses in each of S57 and S84 anchor the recurrence. The S57 deficit favors the target; no Gaia neighbor within 60 arcsec passes the flux-budget screen. The image-model residual (0.77) limits localization precision.

**Next check:** Optional resolved photometry.

Catalogue novelty: the central seven-group result in `../../shared-catalogues/coverage-matrix.csv` reports complete scoped checks with no identified prior EB match. It does not establish exhaustive literature priority or resolve embargoed identities.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt |
|---:|---:|---:|---:|---:|
| 57 | 0 | 2861.0883552 | 0.001157 | 59.10 |
| 57 | 1 | 2872.4509721 | 0.001157 | 59.19 |
| 84 | 64 | 3588.3227099 | 0.001157 | 59.28 |
| 84 | 65 | 3599.6853121 | 0.001157 | 61.14 |

Capable Gaia neighbors:

| Gaia DR3 source | Target separation arcsec | G | Required intrinsic eclipse fraction | Deficit separation arcsec |
|---|---:|---:|---:|---:|
| None | — | — | — | — |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../download-receipts.json`, `../alias-audit.json`, `../gaia-geometry.json`, `historical/diff_s57.json`, `historical/diff_s57.png`, `historical/gaia.json`, original `[local path omitted], and `../helper-audit.md`. All file hashes are in `../SHA256SUMS.json`.


Stable review key: R538. Public evidence files: [diff_s57.json](../../evidence/440168538/historical/diff_s57.json), [diff_s57.png](../../evidence/440168538/historical/diff_s57.png), [gaia.json](../../evidence/440168538/historical/gaia.json), [measurements.json](../../evidence/440168538/measurements.json), [raw-events.png](../../evidence/440168538/raw-events.png), [raw-windows.csv](../../evidence/440168538/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch03/INDEX.md). 
