# TIC 446159745: CONFIRMED

**Full bounded review: COMPLETE.** Physical outcome, catalogue novelty and historical screening label are separate.

1. **Repeated raw morphology.** 7 timing-usable measured eclipses in quality-zero QLP SAP_FLUX across representative sectors [19, 53, 74]. The local fit has a free center, depth, width and baseline. Predicted centers select inspection windows; flagged and uncovered windows are not clean nulls. Raw points are preserved in `raw-windows.csv` and `raw-events.png`.
2. **Measured timing and aliases.** P = 8.3371405920 ± 0.0000254401 d, reference BTJD 1819.7081287 (Selected repeating eclipse; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; deeper/secondary identity not independently established. Adjacent-cycle and parity summaries are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive all-period search.
3. **Pixel attribution.** The S20 TESScut deficit centroid is 0.30 arcsec from the target coordinate. Peak deficit pixel [8, 7]; target pixel [8, 7]. Image-model fractional residual 0.023 is not a calibrated centroid error. The table below lists every Gaia neighbor in the 60-arcsec screen that can supply the selected depth under an approximate flux-budget calculation. Required intrinsic eclipse depth is not a blended pixel loss.
4. **Alternative reduction.** Target-centered, background-subtracted cutout apertures combining 3 predicted event windows give 1x1/3x3/5x5 depths 128.37/128.36/127.20 ppt; median selected QLP raw fit depth is 132.96 ppt. The stack does not by itself prove each cutout window contains an eclipse. The cutout sector is a separate TESS observing occasion from the selected QLP sectors; it is the same instrument with an alternative reduction, not independent-instrument confirmation. Aperture dilution and selected-event differences limit depth equality.
5. **Gaia geometry.** Source 1139354875446856704 has orbital P = 8.337129275 d and e = 0.0553. The nearest edge-on conjunction is offset by -0.0237 d (-0.0028 phase) at the measured reference epoch. Full source-specific NSS covariance gives a descriptive linear timing scale of 0.2423 d. Approximate central duration 7.25 h versus observed median 5.94 h. Assumed TIC radius and minimum-mass companion make this a plausibility check, not a fitted binary model or sigma veto.

**Deciding interpretation and limitation:** Seven raw eclipses span S19, S53 and S74, with an adjacent S53 triplet. The S20 alternative extraction is a separate observing occasion with three events; its deficit is sharply target-centered and no capable Gaia neighbor is listed.

**Next check:** Optional precision characterization.

Catalogue novelty: the central seven-group result in `../../shared-catalogues/coverage-matrix.csv` reports complete scoped checks with no identified prior EB match. It does not establish exhaustive literature priority or resolve embargoed identities.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt |
|---:|---:|---:|---:|---:|
| 19 | 0 | 1819.7086587 | 0.010417 | 133.18 |
| 19 | 2 | 1836.3824472 | 0.010417 | 134.82 |
| 53 | 111 | 2745.1322540 | 0.003472 | 126.89 |
| 53 | 112 | 2753.4673157 | 0.003472 | 134.89 |
| 53 | 113 | 2761.8037927 | 0.003472 | 131.43 |
| 74 | 180 | 3320.3936679 | 0.001157 | 132.55 |
| 74 | 182 | 3337.0675061 | 0.001157 | 132.96 |

Capable Gaia neighbors:

| Gaia DR3 source | Target separation arcsec | G | Required intrinsic eclipse fraction | Deficit separation arcsec |
|---|---:|---:|---:|---:|
| None | — | — | — | — |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../download-receipts.json`, `../alias-audit.json`, `../gaia-geometry.json`, `historical/diff_s20.json`, `historical/diff_s20.png`, `historical/gaia.json`, original `[local path omitted], and `../helper-audit.md`. All file hashes are in `../SHA256SUMS.json`.


Stable review key: R539. Public evidence files: [diff_s20.json](../../evidence/446159745/historical/diff_s20.json), [diff_s20.png](../../evidence/446159745/historical/diff_s20.png), [gaia.json](../../evidence/446159745/historical/gaia.json), [measurements.json](../../evidence/446159745/measurements.json), [raw-events.png](../../evidence/446159745/raw-events.png), [raw-windows.csv](../../evidence/446159745/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch03/INDEX.md). 
