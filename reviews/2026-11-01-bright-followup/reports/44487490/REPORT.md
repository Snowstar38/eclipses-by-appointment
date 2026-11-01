# TIC 44487490: CONFIRMED

**Full bounded review: COMPLETE.** Physical outcome, catalogue novelty and historical screening label are separate.

1. **Repeated raw morphology.** 5 timing-usable measured eclipses in quality-zero QLP SAP_FLUX across representative sectors [17, 84]. The local fit has a free center, depth, width and baseline. Predicted centers select inspection windows; flagged and uncovered windows are not clean nulls. Raw points are preserved in `raw-windows.csv` and `raw-events.png`.
2. **Measured timing and aliases.** P = 6.8939207479 ± 0.0000281001 d, reference BTJD 1780.3799981 (Odd-cycle, slightly deeper eclipse of the full orbit). Odd historical half-period cycles; the adjacent even events are a distinct eclipse kind with alternating timing offsets. Adjacent-cycle and parity summaries are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive all-period search.
3. **Pixel attribution.** The S84 TESScut deficit centroid is 2.39 arcsec from the target coordinate. Peak deficit pixel [8, 8]; target pixel [7, 8]. Image-model fractional residual 0.236 is not a calibrated centroid error. The table below lists every Gaia neighbor in the 60-arcsec screen that can supply the selected depth under an approximate flux-budget calculation. Required intrinsic eclipse depth is not a blended pixel loss.
4. **Alternative reduction.** Target-centered, background-subtracted cutout apertures combining 4 predicted event windows give 1x1/3x3/5x5 depths 68.92/66.68/60.44 ppt; median selected QLP raw fit depth is 75.15 ppt. The stack does not by itself prove each cutout window contains an eclipse. The cutout and selected QLP observations use the same TESS sector and share photons; this is an alternative reduction, not an independent observing occasion. Aperture dilution and selected-event differences limit depth equality.
5. **Gaia geometry.** Source 2863142675459097216 has orbital P = 6.893921667 d and e = 0.0556. The nearest edge-on conjunction is offset by -0.0401 d (-0.0058 phase) at the measured reference epoch. Full source-specific NSS covariance gives a descriptive linear timing scale of 0.1483 d. Approximate central duration 8.28 h versus observed median 5.56 h. Assumed TIC radius and minimum-mass companion make this a plausibility check, not a fitted binary model or sigma veto.

**Deciding interpretation and limitation:** Adjacent S17 and S84 dips alternate timing around the 3.44695-day photometric search clock. Odd cycles define the same-kind 6.89392-day orbit, matching Gaia; the even events are the other eclipse kind. The S84 image is target-centered, with the sole capable neighbor about 54 arcsec away.

**Next check:** Optional characterization of both eclipse kinds.

Catalogue novelty: the central seven-group result in `../../shared-catalogues/coverage-matrix.csv` reports complete scoped checks with no identified prior EB match. It does not establish exhaustive literature priority or resolve embargoed identities.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt |
|---:|---:|---:|---:|---:|
| 17 | 3 | 1780.3797789 | 0.010416 | 71.42 |
| 17 | 5 | 1787.2742324 | 0.010416 | 76.09 |
| 84 | 527 | 3586.5868457 | 0.001157 | 74.59 |
| 84 | 529 | 3593.4815850 | 0.001157 | 75.44 |
| 84 | 533 | 3607.2689533 | 0.001157 | 75.15 |

Capable Gaia neighbors:

| Gaia DR3 source | Target separation arcsec | G | Required intrinsic eclipse fraction | Deficit separation arcsec |
|---|---:|---:|---:|---:|
| 2863142885913312128 | 53.96 | 13.988 | 0.382 | 57.0 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../download-receipts.json`, `../alias-audit.json`, `../gaia-geometry.json`, `historical/diff_s84.json`, `historical/diff_s84.png`, `historical/gaia.json`, original `[local path omitted], and `../helper-audit.md`. All file hashes are in `../SHA256SUMS.json`.


Stable review key: R532. Public evidence files: [diff_s84.json](../../evidence/44487490/historical/diff_s84.json), [diff_s84.png](../../evidence/44487490/historical/diff_s84.png), [gaia.json](../../evidence/44487490/historical/gaia.json), [measurements.json](../../evidence/44487490/measurements.json), [raw-events.png](../../evidence/44487490/raw-events.png), [raw-windows.csv](../../evidence/44487490/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch03/INDEX.md). 
