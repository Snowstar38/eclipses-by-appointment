# TIC 309253911: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw evidence.** Quality-zero QLP SAP_FLUX gives 9 timing-selected measured centers in sectors [1, 38, 96]. Local trapezoids fit free centers, depths, durations and baselines. Raw plots and windows retain the evidence. Predicted centers guided extraction only; flagged or uncovered windows are not null detections. Representative raw morphology shows repeated eclipses.
2. **Timing and aliases.** Selected centers yield P = 5.6751203957 ± 0.0000063088 d and reference epoch BTJD 1328.2070579 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). There are 5 within-sector same-kind adjacent pairs after the specified parity selection. The historical search branch is 5.67511914 d. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This conditional formal error is not total calibrated uncertainty or an exhaustive alias search.
3. **Source attribution.** Historical sector 64 TESScut difference image puts the deficit 2.46 arcsec from the target coordinate; peak [7, 7] versus target pixel [7, 7]. Image-model fractional residual 0.179 is not a localization error. Capable Gaia neighbors within 60 arcsec: none under the approximate G-band flux budget. Intrinsic required losses use an approximate flux budget and cannot be equated to blended pixel loss.
4. **Alternative reduction.** Background-subtracted TESScut target 1x1/3x3/5x5 apertures yield 75.40/74.07/69.71 ppt in 5 stacked historical events; representative QLP raw median selected depth is 68.35 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. aperture dilution and event choice limit direct depth comparison.
5. **Gaia geometry.** Matched DR3 source 5276097362970850432 has SB1 P = 5.6754892774 d and e = 0.03670. Closest edge-on conjunction offset is -0.05998 d (-0.01057 phase), with 0.04432 d linearly propagated full source-specific SB1 covariance. Rough central duration 7.71 h versus observed median fit 4.98 h assumes TIC radius and a minimum-mass main-sequence companion, not a complete binary model. Agreement does not prove source identity.

**Interpretation and limitation:** Nine measured eclipses in sectors 1, 38 and 96 include five adjacent-cycle pairs. No Gaia neighbor within 60 arcsec meets the approximate flux budget.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is ../../shared-catalogues/coverage-matrix.csv. A cone source alone is not an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 1 | 0 | 1328.2081849 | 0.010416 | 66.69 | used |
| 1 | 1 | 1333.8846253 | 0.010416 | 68.35 | used |
| 1 | 3 | 1345.2296355 | 0.010416 | 66.37 | used |
| 38 | 178 | 2338.3785526 | 0.003472 | 77.00 | used |
| 38 | 179 | 2344.0532360 | 0.003472 | 76.55 | used |
| 38 | 180 | 2349.7283396 | 0.003472 | 77.20 | used |
| 38 | 181 | 2355.4044016 | 0.003472 | 76.78 | used |
| 96 | 455 | 3910.3868805 | 0.001157 | 65.77 | used |
| 96 | 456 | 3916.0619223 | 0.001157 | 66.56 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s64.json, historical/diff_s64.png, historical/gaia.json and ../helper-audit.md. Original TESScut: [local path omitted] (SHA256 in ../source-hashes.json). Retained artifacts are in ../SHA256SUMS.json.


Stable review key: R452. Public evidence files: [diff_s64.json](../../evidence/309253911/historical/diff_s64.json), [diff_s64.png](../../evidence/309253911/historical/diff_s64.png), [gaia.json](../../evidence/309253911/historical/gaia.json), [measurements.json](../../evidence/309253911/measurements.json), [raw-events.png](../../evidence/309253911/raw-events.png), [raw-windows.csv](../../evidence/309253911/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch05/INDEX.md). 
