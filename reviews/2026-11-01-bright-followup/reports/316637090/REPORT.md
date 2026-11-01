# TIC 316637090: CONFIRMED

**Full bounded review: COMPLETE.** Physical outcome, catalogue novelty and historical screening label are separate.

1. **Repeated raw morphology.** 10 timing-usable measured eclipses in quality-zero QLP SAP_FLUX across representative sectors [53, 80]. The local fit has a free center, depth, width and baseline. Predicted centers select inspection windows; flagged and uncovered windows are not clean nulls. Raw points are preserved in `raw-windows.csv` and `raw-events.png`.
2. **Measured timing and aliases.** P = 3.8636264942 ± 0.0000122316 d, reference BTJD 2746.3243407 (Selected repeating eclipse; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; deeper/secondary identity not independently established. Adjacent-cycle and parity summaries are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive all-period search.
3. **Pixel attribution.** The S80 TESScut deficit centroid is 3.12 arcsec from the target coordinate. Peak deficit pixel [7, 7]; target pixel [7, 7]. Image-model fractional residual 0.179 is not a calibrated centroid error. The table below lists every Gaia neighbor in the 60-arcsec screen that can supply the selected depth under an approximate flux-budget calculation. Required intrinsic eclipse depth is not a blended pixel loss.
4. **Alternative reduction.** Target-centered, background-subtracted cutout apertures combining 6 predicted event windows give 1x1/3x3/5x5 depths 13.58/13.92/13.64 ppt; median selected QLP raw fit depth is 15.34 ppt. The stack does not by itself prove each cutout window contains an eclipse. The cutout and selected QLP observations use the same TESS sector and share photons; this is an alternative reduction, not an independent observing occasion. Aperture dilution and selected-event differences limit depth equality.
5. **Gaia geometry.** Source 4595458674208503424 has orbital P = 3.862983602 d and e = 0.1667. The nearest edge-on conjunction is offset by +0.2349 d (+0.0608 phase) at the measured reference epoch. Full source-specific NSS covariance gives a descriptive linear timing scale of 0.1301 d. Approximate central duration 4.61 h versus observed median 2.18 h. Assumed TIC radius and minimum-mass companion make this a plausibility check, not a fitted binary model or sigma veto.

**Deciding interpretation and limitation:** Ten shallow raw events in S53 and S80 repeat; the S80 aperture extraction recovers six. The target-near deficit is roughly 31 arcsec from the only capable Gaia neighbor. The Gaia conjunction offset is descriptive and is not used as a significance veto.

**Next check:** Additional resolved photometry would strengthen this shallow attribution.

Catalogue novelty: the central seven-group result in `../../shared-catalogues/coverage-matrix.csv` reports complete scoped checks with no identified prior EB match. It does not establish exhaustive literature priority or resolve embargoed identities.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt |
|---:|---:|---:|---:|---:|
| 53 | 195 | 2746.3247811 | 0.003472 | 12.98 |
| 53 | 197 | 2754.0513492 | 0.006473 | 12.57 |
| 53 | 198 | 2757.9189913 | 0.005698 | 14.81 |
| 53 | 200 | 2765.6405893 | 0.004227 | 16.53 |
| 80 | 385 | 3480.4125219 | 0.001253 | 16.41 |
| 80 | 386 | 3484.2757810 | 0.001157 | 15.45 |
| 80 | 388 | 3491.9986733 | 0.004023 | 10.24 |
| 80 | 389 | 3495.8677415 | 0.001157 | 15.22 |
| 80 | 390 | 3499.7325144 | 0.001157 | 16.71 |
| 80 | 391 | 3503.5977894 | 0.001547 | 15.71 |

Capable Gaia neighbors:

| Gaia DR3 source | Target separation arcsec | G | Required intrinsic eclipse fraction | Deficit separation arcsec |
|---|---:|---:|---:|---:|
| 4595458605489025280 | 29.26 | 15.390 | 0.246 | 30.8 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../download-receipts.json`, `../alias-audit.json`, `../gaia-geometry.json`, `historical/diff_s80.json`, `historical/diff_s80.png`, `historical/gaia.json`, original `[local path omitted], and `../helper-audit.md`. All file hashes are in `../SHA256SUMS.json`.


Stable review key: R534. Public evidence files: [diff_s80.json](../../evidence/316637090/historical/diff_s80.json), [diff_s80.png](../../evidence/316637090/historical/diff_s80.png), [gaia.json](../../evidence/316637090/historical/gaia.json), [measurements.json](../../evidence/316637090/measurements.json), [raw-events.png](../../evidence/316637090/raw-events.png), [raw-windows.csv](../../evidence/316637090/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch03/INDEX.md). 
