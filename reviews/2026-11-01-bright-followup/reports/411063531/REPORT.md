# TIC 411063531: CONFIRMED

**Full bounded review: COMPLETE.** Physical outcome, catalogue novelty and historical screening label are separate.

1. **Repeated raw morphology.** 6 timing-usable measured eclipses in quality-zero QLP SAP_FLUX across representative sectors [10, 64, 100]. The local fit has a free center, depth, width and baseline. Predicted centers select inspection windows; flagged and uncovered windows are not clean nulls. Raw points are preserved in `raw-windows.csv` and `raw-events.png`.
2. **Measured timing and aliases.** P = 9.9939890066 ± 0.0000106933 d, reference BTJD 1573.2390596 (Selected repeating eclipse; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; deeper/secondary identity not independently established. Adjacent-cycle and parity summaries are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive all-period search.
3. **Pixel attribution.** The S90 TESScut deficit centroid is 3.14 arcsec from the target coordinate. Peak deficit pixel [8, 7]; target pixel [8, 7]. Image-model fractional residual 0.859 is not a calibrated centroid error. The table below lists every Gaia neighbor in the 60-arcsec screen that can supply the selected depth under an approximate flux-budget calculation. Required intrinsic eclipse depth is not a blended pixel loss.
4. **Alternative reduction.** Target-centered, background-subtracted cutout apertures combining 3 predicted event windows give 1x1/3x3/5x5 depths 28.30/18.60/12.01 ppt; median selected QLP raw fit depth is 37.27 ppt. The stack does not by itself prove each cutout window contains an eclipse. The cutout sector is a separate TESS observing occasion from the selected QLP sectors; it is the same instrument with an alternative reduction, not independent-instrument confirmation. Aperture dilution and selected-event differences limit depth equality.
5. **Gaia geometry.** Source 5354251091852534016 has orbital P = 9.994640884 d and e = 0.0745. The nearest edge-on conjunction is offset by +0.2248 d (+0.0225 phase) at the measured reference epoch. Full source-specific NSS covariance gives a descriptive linear timing scale of 0.4266 d. Approximate central duration 5.40 h versus observed median 4.48 h. Assumed TIC radius and minimum-mass companion make this a plausibility check, not a fitted binary model or sigma veto.

**Deciding interpretation and limitation:** Six raw events span S10, S64 and S100, with adjacent pairs in both later sectors. The crowded S90 deficit centroid is 3.1 arcsec from the target while the light centroid is displaced 26.3 arcsec; four flux-capable catalogued neighbors are 44–47 arcsec from the deficit. The target is favored, but the image-model residual (0.86) limits localization precision.

**Next check:** Resolved eclipse imaging would strengthen attribution in this crowded field.

Catalogue novelty: the central seven-group result in `../../shared-catalogues/coverage-matrix.csv` reports complete scoped checks with no identified prior EB match. It does not establish exhaustive literature priority or resolve embargoed identities.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt |
|---:|---:|---:|---:|---:|
| 10 | 0 | 1573.2357051 | 0.010417 | 37.26 |
| 10 | 2 | 1593.2255969 | 0.010417 | 37.73 |
| 64 | 147 | 3042.3543805 | 0.001173 | 37.29 |
| 64 | 148 | 3052.3506213 | 0.001157 | 37.93 |
| 100 | 251 | 4081.7302680 | 0.001157 | 35.90 |
| 100 | 252 | 4091.7242273 | 0.001157 | 34.01 |

Capable Gaia neighbors:

| Gaia DR3 source | Target separation arcsec | G | Required intrinsic eclipse fraction | Deficit separation arcsec |
|---|---:|---:|---:|---:|
| 5354250374612876928 | 44.15 | 15.755 | 0.934 | 47.0 |
| 5354250374612874496 | 44.88 | 15.020 | 0.493 | 48.3 |
| 5354249618698621696 | 45.66 | 11.275 | 0.052 | 51.3 |
| 5354249687418099072 | 46.48 | 13.728 | 0.176 | 46.7 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../download-receipts.json`, `../alias-audit.json`, `../gaia-geometry.json`, `historical/diff_s90.json`, `historical/diff_s90.png`, `historical/gaia.json`, original `[local path omitted], and `../helper-audit.md`. All file hashes are in `../SHA256SUMS.json`.


Stable review key: R530. Public evidence files: [diff_s90.json](../../evidence/411063531/historical/diff_s90.json), [diff_s90.png](../../evidence/411063531/historical/diff_s90.png), [gaia.json](../../evidence/411063531/historical/gaia.json), [measurements.json](../../evidence/411063531/measurements.json), [raw-events.png](../../evidence/411063531/raw-events.png), [raw-windows.csv](../../evidence/411063531/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch03/INDEX.md). 
