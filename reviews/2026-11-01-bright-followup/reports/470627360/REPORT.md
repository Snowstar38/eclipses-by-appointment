# TIC 470627360: CONFIRMED

**Full bounded review: COMPLETE.** Physical outcome, catalogue novelty and historical screening label are separate.

1. **Repeated raw morphology.** 3 timing-usable measured eclipses in quality-zero QLP SAP_FLUX across representative sectors [59, 73]. The local fit has a free center, depth, width and baseline. Predicted centers select inspection windows; flagged and uncovered windows are not clean nulls. Raw points are preserved in `raw-windows.csv` and `raw-events.png`.
2. **Measured timing and aliases.** P = 14.4695399219 ± 0.0000555576 d, reference BTJD 2913.1456895 (Selected repeating eclipse; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; deeper/secondary identity not independently established. Adjacent-cycle and parity summaries are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive all-period search.
3. **Pixel attribution.** The S59 TESScut deficit centroid is 1.66 arcsec from the target coordinate. Peak deficit pixel [7, 7]; target pixel [7, 7]. Image-model fractional residual 0.330 is not a calibrated centroid error. The table below lists every Gaia neighbor in the 60-arcsec screen that can supply the selected depth under an approximate flux-budget calculation. Required intrinsic eclipse depth is not a blended pixel loss.
4. **Alternative reduction.** Target-centered, background-subtracted cutout apertures combining 2 predicted event windows give 1x1/3x3/5x5 depths 106.04/90.28/83.80 ppt; median selected QLP raw fit depth is 117.46 ppt. The stack does not by itself prove each cutout window contains an eclipse. The cutout and selected QLP observations use the same TESS sector and share photons; this is an alternative reduction, not an independent observing occasion. Aperture dilution and selected-event differences limit depth equality.
5. **Gaia geometry.** Source 197378967299172224 has orbital P = 14.476795633 d and e = 0.3774. The nearest edge-on conjunction is offset by -0.6255 d (-0.0432 phase) at the measured reference epoch. Full source-specific NSS covariance gives a descriptive linear timing scale of 1.0802 d. Approximate central duration 14.33 h versus observed median 11.41 h. Assumed TIC radius and minimum-mass companion make this a plausibility check, not a fitted binary model or sigma veto.

**Deciding interpretation and limitation:** S59 has two adjacent measured eclipses and S73 supplies a longer-baseline third. The S59 difference core is target-centered, about 35.5 arcsec from its only capable Gaia neighbor; the long event is also recovered by aperture extraction.

**Next check:** Further-sector timing would refine the modest three-event ephemeris.

Catalogue novelty: the central seven-group result in `../../shared-catalogues/coverage-matrix.csv` reports complete scoped checks with no identified prior EB match. It does not establish exhaustive literature priority or resolve embargoed identities.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt |
|---:|---:|---:|---:|---:|
| 59 | 75 | 2913.1457540 | 0.001157 | 117.52 |
| 59 | 76 | 2927.6151624 | 0.001157 | 117.46 |
| 73 | 101 | 3289.3537301 | 0.001157 | 116.97 |

Capable Gaia neighbors:

| Gaia DR3 source | Target separation arcsec | G | Required intrinsic eclipse fraction | Deficit separation arcsec |
|---|---:|---:|---:|---:|
| 197378971597385472 | 34.28 | 13.428 | 0.445 | 35.5 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../download-receipts.json`, `../alias-audit.json`, `../gaia-geometry.json`, `historical/diff_s59.json`, `historical/diff_s59.png`, `historical/gaia.json`, original `[local path omitted], and `../helper-audit.md`. All file hashes are in `../SHA256SUMS.json`.


Stable review key: R537. Public evidence files: [diff_s59.json](../../evidence/470627360/historical/diff_s59.json), [diff_s59.png](../../evidence/470627360/historical/diff_s59.png), [gaia.json](../../evidence/470627360/historical/gaia.json), [measurements.json](../../evidence/470627360/measurements.json), [raw-events.png](../../evidence/470627360/raw-events.png), [raw-windows.csv](../../evidence/470627360/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch03/INDEX.md). 
