# TIC 270478197: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw evidence.** Quality-zero QLP SAP_FLUX gives 4 timing-selected measured centers in sectors [70, 71]. Local trapezoids fit free centers, depths, durations and baselines. Raw plots and windows retain the evidence. Predicted centers guided extraction only; flagged or uncovered windows are not null detections. Representative raw morphology shows repeated eclipses.
2. **Timing and aliases.** Selected centers yield P = 10.5462440932 ± 0.0003912788 d and reference epoch BTJD 3215.9948789 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). There are 1 within-sector same-kind adjacent pairs after the specified parity selection. The historical search branch is 10.54632873 d. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This conditional formal error is not total calibrated uncertainty or an exhaustive alias search.
3. **Source attribution.** Historical sector 31 TESScut difference image puts the deficit 5.02 arcsec from the target coordinate; peak [7, 8] versus target pixel [7, 8]. Image-model fractional residual 0.036 is not a localization error. Capable Gaia neighbors within 60 arcsec: none under the approximate G-band flux budget. Intrinsic required losses use an approximate flux budget and cannot be equated to blended pixel loss.
4. **Alternative reduction.** Background-subtracted TESScut target 1x1/3x3/5x5 apertures yield 172.94/172.35/172.38 ppt in 2 stacked historical events; representative QLP raw median selected depth is 171.57 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. aperture dilution and event choice limit direct depth comparison.
5. **Gaia geometry.** Matched DR3 source 2513059066528401664 has SB1 P = 10.5462213303 d and e = 0.09909. Closest edge-on conjunction offset is 0.19326 d (0.01833 phase), with 0.54444 d linearly propagated full source-specific SB1 covariance. Rough central duration 6.32 h versus observed median fit 5.12 h assumes TIC radius and a minimum-mass main-sequence companion, not a complete binary model. Agreement does not prove source identity.

**Interpretation and limitation:** Four deep measured eclipses include an adjacent sector-70 pair and a sector-71 repeat. No Gaia neighbor within 60 arcsec meets the approximate flux budget.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is ../../shared-catalogues/coverage-matrix.csv. A cone source alone is not an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 70 | 171 | 3215.9949044 | 0.001157 | 171.99 | used |
| 70 | 172 | 3226.5410800 | 0.001157 | 172.66 | used |
| 71 | 173 | 3237.0873804 | 0.001157 | 170.66 | used |
| 71 | 175 | 3258.1798593 | 0.001157 | 171.16 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s31.json, historical/diff_s31.png, historical/gaia.json and ../helper-audit.md. Original TESScut: [local path omitted] (SHA256 in ../source-hashes.json). Retained artifacts are in ../SHA256SUMS.json.


Stable review key: R456. Public evidence files: [diff_s31.json](../../evidence/270478197/historical/diff_s31.json), [diff_s31.png](../../evidence/270478197/historical/diff_s31.png), [gaia.json](../../evidence/270478197/historical/gaia.json), [measurements.json](../../evidence/270478197/measurements.json), [raw-events.png](../../evidence/270478197/raw-events.png), [raw-windows.csv](../../evidence/270478197/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch05/INDEX.md). 
