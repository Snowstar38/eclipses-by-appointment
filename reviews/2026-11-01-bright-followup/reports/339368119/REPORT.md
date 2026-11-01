# TIC 339368119: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw evidence.** Quality-zero QLP SAP_FLUX gives 9 timing-selected measured centers in sectors [19, 59, 86]. Local trapezoids fit free centers, depths, durations and baselines. Raw plots and windows retain the evidence. Predicted centers guided extraction only; flagged or uncovered windows are not null detections. Representative raw morphology shows repeated eclipses.
2. **Timing and aliases.** Selected centers yield P = 4.8123646667 ± 0.0000062908 d and reference epoch BTJD 1819.6071844 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). There are 5 within-sector same-kind adjacent pairs after the specified parity selection. The historical search branch is 4.81237757 d. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This conditional formal error is not total calibrated uncertainty or an exhaustive alias search.
3. **Source attribution.** Historical sector 59 TESScut difference image puts the deficit 2.41 arcsec from the target coordinate; peak [8, 7] versus target pixel [8, 7]. Image-model fractional residual 0.110 is not a localization error. Capable Gaia neighbors within 60 arcsec: none under the approximate G-band flux budget. Intrinsic required losses use an approximate flux budget and cannot be equated to blended pixel loss.
4. **Alternative reduction.** Background-subtracted TESScut target 1x1/3x3/5x5 apertures yield 144.77/145.89/142.74 ppt in 5 stacked historical events; representative QLP raw median selected depth is 152.15 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. aperture dilution and event choice limit direct depth comparison.
5. **Gaia geometry.** Matched DR3 source 287971617259251968 has SB1 P = 4.8121222282 d and e = 0.04395. Closest edge-on conjunction offset is 0.04761 d (0.00989 phase), with 0.06365 d linearly propagated full source-specific SB1 covariance. Rough central duration 4.47 h versus observed median fit 3.92 h assumes TIC radius and a minimum-mass main-sequence companion, not a complete binary model. Agreement does not prove source identity.

**Interpretation and limitation:** Nine deep measured eclipses in sectors 19, 59 and 86 include five adjacent-cycle pairs. No Gaia neighbor within 60 arcsec meets the approximate flux budget.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is ../../shared-catalogues/coverage-matrix.csv. A cone source alone is not an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 19 | 0 | 1819.6069525 | 0.010417 | 152.48 | used |
| 19 | 1 | 1824.4193945 | 0.010417 | 152.71 | used |
| 59 | 227 | 2912.0141496 | 0.001157 | 152.95 | used |
| 59 | 229 | 2921.6385015 | 0.001157 | 153.00 | used |
| 59 | 230 | 2926.4510671 | 0.001157 | 152.15 | used |
| 59 | 231 | 2931.2634482 | 0.001157 | 151.22 | used |
| 59 | 232 | 2936.0757667 | 0.001157 | 150.22 | used |
| 86 | 379 | 3643.4934662 | 0.001157 | 148.42 | used |
| 86 | 380 | 3648.3056804 | 0.001157 | 147.80 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s59.json, historical/diff_s59.png, historical/gaia.json and ../helper-audit.md. Original TESScut: [local path omitted] (SHA256 in ../source-hashes.json). Retained artifacts are in ../SHA256SUMS.json.


Stable review key: R455. Public evidence files: [diff_s59.json](../../evidence/339368119/historical/diff_s59.json), [diff_s59.png](../../evidence/339368119/historical/diff_s59.png), [gaia.json](../../evidence/339368119/historical/gaia.json), [measurements.json](../../evidence/339368119/measurements.json), [raw-events.png](../../evidence/339368119/raw-events.png), [raw-windows.csv](../../evidence/339368119/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch05/INDEX.md). 
