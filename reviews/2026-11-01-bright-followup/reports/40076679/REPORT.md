# TIC 40076679: PROBABLE

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw evidence.** Quality-zero QLP SAP_FLUX gives 7 timing-selected measured centers in sectors [39, 66, 103]. Local trapezoids fit free centers, depths, durations and baselines. Raw plots and windows retain the evidence. Predicted centers guided extraction only; flagged or uncovered windows are not null detections. Representative raw morphology shows repeated eclipses.
2. **Timing and aliases.** Selected centers yield P = 8.7425051500 ± 0.0000139891 d and reference epoch BTJD 2365.0791284 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). There are 2 within-sector same-kind adjacent pairs after the specified parity selection. The historical search branch is 8.74245731 d. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This conditional formal error is not total calibrated uncertainty or an exhaustive alias search.
3. **Source attribution.** Historical sector 39 TESScut difference image puts the deficit 5.05 arcsec from the target coordinate; peak [7, 7] versus target pixel [7, 7]. Image-model fractional residual 0.856 is not a localization error. Capable Gaia neighbors within 60 arcsec: Gaia 5937789026883670528 (25.82 arcsec, G 14.049, intrinsic required loss about 0.062); Gaia 5937789026883674624 (29.68 arcsec, G 15.869, intrinsic required loss about 0.291); Gaia 5937788270969425664 (32.98 arcsec, G 16.761, intrinsic required loss about 0.649); Gaia 5937794146484859520 (35.77 arcsec, G 16.205, intrinsic required loss about 0.393); Gaia 5937788270969425408 (43.72 arcsec, G 15.946, intrinsic required loss about 0.311); Gaia 5937794902399104128 (43.96 arcsec, G 16.674, intrinsic required loss about 0.600); Gaia 5937788270969424256 (44.85 arcsec, G 16.253, intrinsic required loss about 0.410); Gaia 5937788236609685632 (46.54 arcsec, G 16.804, intrinsic required loss about 0.675); Gaia 5937788270969423744 (51.00 arcsec, G 15.052, intrinsic required loss about 0.142); Gaia 5937788270969470208 (57.24 arcsec, G 15.251, intrinsic required loss about 0.168). Intrinsic required losses use an approximate flux budget and cannot be equated to blended pixel loss. A fresh sector-66 TESScut stack of two actual measured windows gives a 7.48-arcsec target offset, target-core peak, 1x1/3x3/5x5 depths 8.10/6.43/3.15 ppt and image-model residual 0.999; see historical/diff_s66.json and .png. These residuals prevent unique source attribution.
4. **Alternative reduction.** Background-subtracted TESScut target 1x1/3x3/5x5 apertures yield 8.97/5.31/3.45 ppt in 3 stacked historical events; representative QLP raw median selected depth is 9.64 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. aperture dilution and event choice limit direct depth comparison.
5. **Gaia geometry.** Matched DR3 source 5937789022547559296 has SB1 P = 8.7431794619 d and e = 0.06793. Closest edge-on conjunction offset is -0.13259 d (-0.01516 phase), with 0.31187 d linearly propagated full source-specific SB1 covariance. Rough central duration 8.16 h versus observed median fit 3.01 h assumes TIC radius and a minimum-mass main-sequence companion, not a complete binary model. Agreement does not prove source identity.

**Interpretation and limitation:** Seven shallow raw eclipses recur in sectors 39, 66 and 103; three adjacent sector-39 cycles directly test the period. Both sector-39 and newly measured sector-66 difference images have strong structured residuals in a crowded field. Ten Gaia neighbors within 60 arcsec can in principle produce the blended depth. The sector-66 deficit core is near the target, yet the pixel data cannot uniquely assign the signal.

**Next check:** Resolved time-series photometry or multi-source pixel modeling during an eclipse to identify the variable source.

Catalogue novelty: central seven-group result is ../../shared-catalogues/coverage-matrix.csv. A cone source alone is not an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 39 | 84 | 2365.0775254 | 0.004904 | 7.83 | used |
| 39 | 85 | 2373.8221439 | 0.003974 | 9.41 | used |
| 39 | 86 | 2382.5642846 | 0.003740 | 12.93 | used |
| 66 | 168 | 3099.4483213 | 0.003055 | 13.23 | used |
| 66 | 170 | 3116.9368236 | 0.003608 | 9.89 | used |
| 103 | 289 | 4157.2935634 | 0.002077 | 7.92 | used |
| 103 | 291 | 4174.7753719 | 0.003248 | 9.64 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s39.json, historical/diff_s39.png, historical/gaia.json and ../helper-audit.md. Original TESScut: [local path omitted] (SHA256 in ../source-hashes.json). Retained artifacts are in ../SHA256SUMS.json.


Stable review key: R459. Public evidence files: [diff_s39.json](../../evidence/40076679/historical/diff_s39.json), [diff_s39.png](../../evidence/40076679/historical/diff_s39.png), [diff_s66.json](../../evidence/40076679/historical/diff_s66.json), [diff_s66.png](../../evidence/40076679/historical/diff_s66.png), [gaia.json](../../evidence/40076679/historical/gaia.json), [measurements.json](../../evidence/40076679/measurements.json), [raw-events.png](../../evidence/40076679/raw-events.png), [raw-windows.csv](../../evidence/40076679/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch05/INDEX.md). 
