# TIC 77571117: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw evidence.** Quality-zero QLP SAP_FLUX contains 6 timing-usable measured centers in sectors [12, 38, 91]. Local trapezoids fit free centers, depths, durations and baselines. Raw plots and windows retain the evidence. Predicted centers guided extraction only; flagged or uncovered windows are not null detections. Representative morphology shows repeated eclipses.
2. **Timing and aliases.** Measured centers yield P = 6.7210082588 ± 0.0000112025 d and reference epoch BTJD 1648.3408444 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). There are 1 within-sector adjacent same-kind pairs (../alias-audit.json). Measured centers and same-kind pairs support the bounded period and alias check. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This formal error is not total calibrated uncertainty or an exhaustive alias search.
3. **Source attribution.** Historical sector 91 TESScut difference image puts the deficit 5.93 arcsec from the target coordinate; peak [7, 8] versus target pixel [7, 8]. Image-model fractional residual 0.176 is not a localization error. Capable Gaia neighbors within 60 arcsec: none under approximate G-band flux budget. Intrinsic-loss requirements use an approximate flux budget and cannot be equated to blended pixel loss.
4. **Alternative reduction.** Background-subtracted TESScut 1x1/3x3/5x5 target apertures yield 86.36/86.68/82.50 ppt in 3 stacked historical events; representative QLP raw median fit depth is 83.92 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and event choice limit depth comparisons.
5. **Gaia geometry.** Matched DR3 source 6041559422449793792 has SB1 P = 6.7218718431 d and e = 0.00991. Closest edge-on conjunction offset is -0.13771 d (-0.02049 phase), with 0.25422 d linearly propagated full source-specific SB1 covariance. Rough central duration 6.62 h versus observed median fit 5.26 h assumes TIC radius and a minimum-mass main-sequence companion, not a full binary model. Agreement is not source proof.

**Interpretation and limitation:** Six raw repeats span three sectors. The deficit is target-centered and no Gaia neighbor is capable under the approximate flux budget.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is ../../shared-catalogues/coverage-matrix.csv. A cone source alone is not an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 12 | 2 | 1648.3403506 | 0.010416 | 83.42 | used |
| 38 | 105 | 2340.6043885 | 0.003472 | 86.30 | used |
| 38 | 107 | 2354.0471022 | 0.003472 | 85.61 | used |
| 91 | 319 | 3778.9005767 | 0.001157 | 82.79 | used |
| 91 | 321 | 3792.3421496 | 0.001157 | 84.42 | used |
| 91 | 322 | 3799.0636992 | 0.001157 | 82.98 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s91.json, historical/diff_s91.png, historical/gaia.json and ../helper-audit.md. Original TESScut: [local path omitted] (SHA256 in ../source-hashes.json). Retained artifacts are in ../SHA256SUMS.json.


Stable review key: R433. Public evidence files: [diff_s91.json](../../evidence/77571117/historical/diff_s91.json), [diff_s91.png](../../evidence/77571117/historical/diff_s91.png), [gaia.json](../../evidence/77571117/historical/gaia.json), [measurements.json](../../evidence/77571117/measurements.json), [raw-events.png](../../evidence/77571117/raw-events.png), [raw-windows.csv](../../evidence/77571117/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch03/INDEX.md). 
