# TIC 399293743: CONFIRMED

**Full bounded review: COMPLETE.** Physical outcome, catalogue novelty and historical screening label are separate.

1. **Repeated raw morphology.** 5 timing-usable measured eclipses in quality-zero QLP SAP_FLUX across representative sectors [54, 81]. The local fit has a free center, depth, width and baseline. Predicted centers select inspection windows; flagged and uncovered windows are not clean nulls. Raw points are preserved in `raw-windows.csv` and `raw-events.png`.
2. **Measured timing and aliases.** P = 6.7257610294 ± 0.0000449821 d, reference BTJD 2771.4721584 (Selected repeating eclipse; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; deeper/secondary identity not independently established. Adjacent-cycle and parity summaries are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive all-period search.
3. **Pixel attribution.** The S81 TESScut deficit centroid is 1.35 arcsec from the target coordinate. Peak deficit pixel [7, 7]; target pixel [7, 7]. Image-model fractional residual 0.663 is not a calibrated centroid error. The table below lists every Gaia neighbor in the 60-arcsec screen that can supply the selected depth under an approximate flux-budget calculation. Required intrinsic eclipse depth is not a blended pixel loss.
4. **Alternative reduction.** Target-centered, background-subtracted cutout apertures combining 4 predicted event windows give 1x1/3x3/5x5 depths 87.65/74.64/68.29 ppt; median selected QLP raw fit depth is 101.13 ppt. The stack does not by itself prove each cutout window contains an eclipse. The cutout and selected QLP observations use the same TESS sector and share photons; this is an alternative reduction, not an independent observing occasion. Aperture dilution and selected-event differences limit depth equality.
5. **Gaia geometry.** Source 4244542013422016256 has orbital P = 6.725623473 d and e = 0.0141. The nearest edge-on conjunction is offset by +0.1301 d (+0.0194 phase) at the measured reference epoch. Full source-specific NSS covariance gives a descriptive linear timing scale of 0.2912 d. Approximate central duration 5.87 h versus observed median 5.14 h. Assumed TIC radius and minimum-mass companion make this a plausibility check, not a fitted binary model or sigma veto.

**Deciding interpretation and limitation:** Five raw events span S54 and S81, including three adjacent S81 cycles. The S81 deficit lies near the target, about 17.5 arcsec from the only flux-capable Gaia neighbor; the source is favored at TESS resolution.

**Next check:** Optional resolved photometry and spectroscopy.

Catalogue novelty: the central seven-group result in `../../shared-catalogues/coverage-matrix.csv` reports complete scoped checks with no identified prior EB match. It does not establish exhaustive literature priority or resolve embargoed identities.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt |
|---:|---:|---:|---:|---:|
| 54 | 0 | 2771.4721285 | 0.006944 | 100.12 |
| 54 | 2 | 2784.9235520 | 0.006944 | 101.84 |
| 81 | 110 | 3511.3062759 | 0.001157 | 102.45 |
| 81 | 111 | 3518.0313096 | 0.001157 | 100.88 |
| 81 | 112 | 3524.7573169 | 0.001157 | 101.13 |

Capable Gaia neighbors:

| Gaia DR3 source | Target separation arcsec | G | Required intrinsic eclipse fraction | Deficit separation arcsec |
|---|---:|---:|---:|---:|
| 4244541940403576832 | 17.73 | 13.303 | 0.349 | 17.5 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../download-receipts.json`, `../alias-audit.json`, `../gaia-geometry.json`, `historical/diff_s81.json`, `historical/diff_s81.png`, `historical/gaia.json`, original `[local path omitted], and `../helper-audit.md`. All file hashes are in `../SHA256SUMS.json`.


Stable review key: R531. Public evidence files: [diff_s81.json](../../evidence/399293743/historical/diff_s81.json), [diff_s81.png](../../evidence/399293743/historical/diff_s81.png), [gaia.json](../../evidence/399293743/historical/gaia.json), [measurements.json](../../evidence/399293743/measurements.json), [raw-events.png](../../evidence/399293743/raw-events.png), [raw-windows.csv](../../evidence/399293743/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch03/INDEX.md). 
