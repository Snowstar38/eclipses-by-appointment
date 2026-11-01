# TIC 233095433: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw evidence.** Quality-zero QLP SAP_FLUX gives 5 timing-selected measured centers in sectors [14, 53, 86]. Local trapezoids fit free centers, depths, durations and baselines. Raw plots and windows retain the evidence. Predicted centers guided extraction only; flagged or uncovered windows are not null detections. Representative raw morphology shows repeated eclipses.
2. **Timing and aliases.** Selected centers yield P = 12.7774965312 ± 0.0000311255 d and reference epoch BTJD 1686.6231819 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). There are 2 within-sector same-kind adjacent pairs after the specified parity selection. The historical search branch is 12.77746923 d. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This conditional formal error is not total calibrated uncertainty or an exhaustive alias search.
3. **Source attribution.** Historical sector 14 TESScut difference image puts the deficit 2.97 arcsec from the target coordinate; peak [8, 7] versus target pixel [7, 7]. Image-model fractional residual 0.067 is not a localization error. Capable Gaia neighbors within 60 arcsec: none under the approximate G-band flux budget. Intrinsic required losses use an approximate flux budget and cannot be equated to blended pixel loss.
4. **Alternative reduction.** Background-subtracted TESScut target 1x1/3x3/5x5 apertures yield 139.98/137.52/132.99 ppt in 2 stacked historical events; representative QLP raw median selected depth is 137.59 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. aperture dilution and event choice limit direct depth comparison.
5. **Gaia geometry.** Matched DR3 source 2160869549233604608 has SB1 P = 12.7774692281 d and e = 0.04193. Closest edge-on conjunction offset is 0.24719 d (0.01935 phase), with 0.26052 d linearly propagated full source-specific SB1 covariance. Rough central duration 7.34 h versus observed median fit 6.05 h assumes TIC radius and a minimum-mass main-sequence companion, not a complete binary model. Agreement does not prove source identity.

**Interpretation and limitation:** Five deep measured eclipses include adjacent pairs in sectors 14 and 53 and a sector-86 repeat. No Gaia neighbor within 60 arcsec meets the approximate flux budget.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is ../../shared-catalogues/coverage-matrix.csv. A cone source alone is not an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 14 | 0 | 1686.6233507 | 0.010417 | 137.59 | used |
| 14 | 1 | 1699.4004320 | 0.010417 | 138.12 | used |
| 53 | 83 | 2747.1553542 | 0.003472 | 137.56 | used |
| 53 | 84 | 2759.9329495 | 0.003472 | 137.20 | used |
| 86 | 154 | 3654.3576465 | 0.001157 | 138.73 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s14.json, historical/diff_s14.png, historical/gaia.json and ../helper-audit.md. Original TESScut: [local path omitted] (SHA256 in ../source-hashes.json). Retained artifacts are in ../SHA256SUMS.json.


Stable review key: R457. Public evidence files: [diff_s14.json](../../evidence/233095433/historical/diff_s14.json), [diff_s14.png](../../evidence/233095433/historical/diff_s14.png), [gaia.json](../../evidence/233095433/historical/gaia.json), [measurements.json](../../evidence/233095433/measurements.json), [raw-events.png](../../evidence/233095433/raw-events.png), [raw-windows.csv](../../evidence/233095433/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch05/INDEX.md). 
