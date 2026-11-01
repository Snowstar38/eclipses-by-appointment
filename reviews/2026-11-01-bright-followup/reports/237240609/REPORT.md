# TIC 237240609: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw evidence.** Quality-zero QLP SAP_FLUX gives 5 timing-selected measured centers in sectors [54, 81]. Local trapezoids fit free centers, depths, durations and baselines. Raw plots and windows retain the evidence. Predicted centers guided extraction only; flagged or uncovered windows are not null detections. Representative raw morphology shows repeated eclipses.
2. **Timing and aliases.** Selected centers yield P = 5.0155864471 ± 0.0000333988 d and reference epoch BTJD 2772.5784287 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). There are 1 within-sector same-kind adjacent pairs after the specified parity selection. The historical search branch is 5.01554178 d. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This conditional formal error is not total calibrated uncertainty or an exhaustive alias search.
3. **Source attribution.** Historical sector 81 TESScut difference image puts the deficit 3.87 arcsec from the target coordinate; peak [8, 7] versus target pixel [8, 7]. Image-model fractional residual 0.262 is not a localization error. Capable Gaia neighbors within 60 arcsec: none under the approximate G-band flux budget. Intrinsic required losses use an approximate flux budget and cannot be equated to blended pixel loss.
4. **Alternative reduction.** Background-subtracted TESScut target 1x1/3x3/5x5 apertures yield 42.53/43.97/44.53 ppt in 3 stacked historical events; representative QLP raw median selected depth is 40.70 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. aperture dilution and event choice limit direct depth comparison.
5. **Gaia geometry.** Matched DR3 source 4196687071198155520 has SB1 P = 5.0156410953 d and e = 0.01696. Closest edge-on conjunction offset is -0.03987 d (-0.00795 phase), with 0.31438 d linearly propagated full source-specific SB1 covariance. Rough central duration 6.29 h versus observed median fit 4.47 h assumes TIC radius and a minimum-mass main-sequence companion, not a complete binary model. Agreement does not prove source identity.

**Interpretation and limitation:** Five measured eclipses in sectors 54 and 81 include a sector-81 adjacent pair. No Gaia neighbor within 60 arcsec meets the approximate flux budget.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is ../../shared-catalogues/coverage-matrix.csv. A cone source alone is not an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 54 | 0 | 2772.5785995 | 0.006944 | 41.53 | used |
| 54 | 3 | 2787.6248058 | 0.006944 | 40.63 | used |
| 81 | 147 | 3509.8699618 | 0.001157 | 41.78 | used |
| 81 | 150 | 3524.9159492 | 0.001157 | 40.65 | used |
| 81 | 151 | 3529.9321092 | 0.001157 | 40.70 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s81.json, historical/diff_s81.png, historical/gaia.json and ../helper-audit.md. Original TESScut: [local path omitted] (SHA256 in ../source-hashes.json). Retained artifacts are in ../SHA256SUMS.json.


Stable review key: R453. Public evidence files: [diff_s81.json](../../evidence/237240609/historical/diff_s81.json), [diff_s81.png](../../evidence/237240609/historical/diff_s81.png), [gaia.json](../../evidence/237240609/historical/gaia.json), [measurements.json](../../evidence/237240609/measurements.json), [raw-events.png](../../evidence/237240609/raw-events.png), [raw-windows.csv](../../evidence/237240609/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch05/INDEX.md). 
