# TIC 3942765: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw evidence.** Quality-zero QLP SAP_FLUX gives 3 timing-selected measured centers in sectors [48]. Local trapezoids fit free centers, depths, durations and baselines. Raw plots and windows retain the evidence. Predicted centers guided extraction only; flagged or uncovered windows are not null detections. Representative raw morphology shows repeated eclipses.
2. **Timing and aliases.** Selected centers yield P = 5.5687926067 ± 0.0016073409 d and reference epoch BTJD 2611.6125011 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). There are 1 within-sector same-kind adjacent pairs after the specified parity selection. The historical search branch is 5.56862471 d. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This conditional formal error is not total calibrated uncertainty or an exhaustive alias search.
3. **Source attribution.** Historical sector 48 TESScut difference image puts the deficit 1.56 arcsec from the target coordinate; peak [7, 7] versus target pixel [7, 7]. Image-model fractional residual 0.063 is not a localization error. Capable Gaia neighbors within 60 arcsec: none under the approximate G-band flux budget. Intrinsic required losses use an approximate flux budget and cannot be equated to blended pixel loss.
4. **Alternative reduction.** Background-subtracted TESScut target 1x1/3x3/5x5 apertures yield 125.29/124.28/120.53 ppt in 4 stacked historical events; representative QLP raw median selected depth is 137.63 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. aperture dilution and event choice limit direct depth comparison.
5. **Gaia geometry.** Matched DR3 source 740708994716293120 has SB1 P = 5.5682939164 d and e = 0.01875. Closest edge-on conjunction offset is 0.12378 d (0.02223 phase), with 0.32903 d linearly propagated full source-specific SB1 covariance. Rough central duration 5.06 h versus observed median fit 3.70 h assumes TIC radius and a minimum-mass main-sequence companion, not a complete binary model. Agreement does not prove source identity.

**Interpretation and limitation:** Four eclipse-shaped events occur in sector 48; three centers give the ephemeris. Cycle 136 has a positive pre-ingress excursion that biases its fitted baseline and midpoint, so it is retained as morphology and excluded from timing. The remaining adjacent pair tests recurrence; no capable Gaia neighbor lies within 60 arcsec.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is ../../shared-catalogues/coverage-matrix.csv. A cone source alone is not an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 48 | 132 | 2611.6122989 | 0.003472 | 137.63 | used |
| 48 | 133 | 2617.1815969 | 0.003472 | 135.93 | used |
| 48 | 135 | 2628.3187778 | 0.003472 | 137.92 | used |
| 48 | 136 | 2633.8955128 | 0.003472 | 134.10 | excluded: Pre-ingress positive flux excursion biases the local linear baseline and center; retained as eclipse morphology, excluded from timing fit. |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s48.json, historical/diff_s48.png, historical/gaia.json and ../helper-audit.md. Original TESScut: [local path omitted] (SHA256 in ../source-hashes.json). Retained artifacts are in ../SHA256SUMS.json.


Stable review key: R458. Public evidence files: [diff_s48.json](../../evidence/3942765/historical/diff_s48.json), [diff_s48.png](../../evidence/3942765/historical/diff_s48.png), [gaia.json](../../evidence/3942765/historical/gaia.json), [measurements.json](../../evidence/3942765/measurements.json), [raw-events.png](../../evidence/3942765/raw-events.png), [raw-windows.csv](../../evidence/3942765/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch05/INDEX.md). 
