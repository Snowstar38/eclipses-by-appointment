# TIC 382581210: CONFIRMED

**Full bounded review: COMPLETE.** Physical outcome, catalogue novelty and historical screening label are separate.

1. **Repeated raw morphology.** 10 timing-usable measured eclipses in quality-zero QLP SAP_FLUX across representative sectors [2, 3, 29, 68, 69, 95]. The local fit has a free center, depth, width and baseline. Predicted centers select inspection windows; flagged and uncovered windows are not clean nulls. Raw points are preserved in `raw-windows.csv` and `raw-events.png`.
2. **Measured timing and aliases.** P = 15.6625230978 ± 0.0000195721 d, reference BTJD 1354.4142823 (Selected repeating eclipse; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; deeper/secondary identity not independently established. Adjacent-cycle and parity summaries are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive all-period search.
3. **Pixel attribution.** The S2 TESScut deficit centroid is 0.97 arcsec from the target coordinate. Peak deficit pixel [7, 8]; target pixel [7, 8]. Image-model fractional residual 0.415 is not a calibrated centroid error. The table below lists every Gaia neighbor in the 60-arcsec screen that can supply the selected depth under an approximate flux-budget calculation. Required intrinsic eclipse depth is not a blended pixel loss.
4. **Alternative reduction.** Target-centered, background-subtracted cutout apertures combining 2 predicted event windows give 1x1/3x3/5x5 depths 72.76/56.61/50.49 ppt; median selected QLP raw fit depth is 78.95 ppt. The stack does not by itself prove each cutout window contains an eclipse. The cutout and selected QLP observations use the same TESS sector and share photons; this is an alternative reduction, not an independent observing occasion. Aperture dilution and selected-event differences limit depth equality.
5. **Gaia geometry.** Source 4699704947887847296 has orbital P = 15.665541787 d and e = 0.2966. The nearest edge-on conjunction is offset by -0.2056 d (-0.0131 phase) at the measured reference epoch. Full source-specific NSS covariance gives a descriptive linear timing scale of 0.5483 d. Approximate central duration 7.01 h versus observed median 4.68 h. Assumed TIC radius and minimum-mass companion make this a plausibility check, not a fitted binary model or sigma veto.

**Deciding interpretation and limitation:** The current MAST QLP availability record lists nine sectors; all nine files were retrieved and checked. Ten measured quality-zero raw eclipses in S2, S3, S29, S68, S69 and S95 now span the long baseline, including adjacent S29 and S68 pairs. The S29 clean intermediate windows reject equal-kind half, third and quarter-period submultiples; flagged windows were not used as nulls. The historical S2 cutout separately stacks two sparse predicted windows into one target-centered deficit, which alone would not establish each window as an eclipse. Its capable Gaia neighbor is 33 arcsec from the target and 32.5 arcsec from the deficit.

**Next check:** Optional later-sector timing and resolved photometry.

Catalogue novelty: the central seven-group result in `../../shared-catalogues/coverage-matrix.csv` reports complete scoped checks with no identified prior EB match. It does not establish exhaustive literature priority or resolve embargoed identities.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt |
|---:|---:|---:|---:|---:|
| 29 | 48 | 2090.5534699 | 0.003472 | 82.14 |
| 29 | 49 | 2106.2157431 | 0.003472 | 81.59 |
| 2 | 1 | 1354.4178976 | 0.010417 | 69.70 |
| 2 | 2 | 1370.0766181 | 0.010417 | 73.58 |
| 3 | 4 | 1401.4020768 | 0.010416 | 74.99 |
| 68 | 116 | 3155.6049624 | 0.001157 | 80.26 |
| 68 | 117 | 3171.2668610 | 0.001157 | 78.70 |
| 69 | 118 | 3186.9293125 | 0.001157 | 79.20 |
| 69 | 119 | 3202.5912876 | 0.001157 | 80.78 |
| 95 | 163 | 3891.7433424 | 0.001157 | 70.73 |

Capable Gaia neighbors:

| Gaia DR3 source | Target separation arcsec | G | Required intrinsic eclipse fraction | Deficit separation arcsec |
|---|---:|---:|---:|---:|
| 4699704986543565824 | 32.97 | 13.094 | 0.226 | 32.5 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../download-receipts.json`, `../alias-audit.json`, `../gaia-geometry.json`, `historical/diff_s02.json`, `historical/diff_s02.png`, `historical/gaia.json`, original `[local path omitted], and `../helper-audit.md`. All file hashes are in `../SHA256SUMS.json`.


Stable review key: R535. Public evidence files: [diff_s02.json](../../evidence/382581210/historical/diff_s02.json), [diff_s02.png](../../evidence/382581210/historical/diff_s02.png), [gaia.json](../../evidence/382581210/historical/gaia.json), [measurements.json](../../evidence/382581210/measurements.json), [raw-events.png](../../evidence/382581210/raw-events.png), [raw-windows.csv](../../evidence/382581210/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch03/INDEX.md). [382581210-coverage.csv](../../analysis/continuation/batch03/helper/382581210-coverage.csv) [382581210-coverage.py](../../analysis/continuation/batch03/helper/382581210-coverage.py) [382581210-downloads.json](../../analysis/continuation/batch03/helper/382581210-downloads.json) [382581210-recurrence.csv](../../analysis/continuation/batch03/helper/382581210-recurrence.csv) [382581210-recurrence.py](../../analysis/continuation/batch03/helper/382581210-recurrence.py)
