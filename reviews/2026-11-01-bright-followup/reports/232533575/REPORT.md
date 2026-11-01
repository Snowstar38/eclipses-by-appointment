# TIC 232533575: PLAUSIBLE

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw evidence.** Quality-zero QLP SAP_FLUX gives 2 timing-selected measured centers in sectors [77]. Local trapezoids fit free centers, depths, durations and baselines. Raw plots and windows retain the evidence. Predicted centers guided extraction only; flagged or uncovered windows are not null detections. Two observed eclipse-shaped events do not test the integer-cycle period.
2. **Timing and aliases.** Selected centers yield P = 5.0840126999 ± 0.0005456124 d and reference epoch BTJD 3405.0730806 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). There are 0 within-sector same-kind adjacent pairs after the specified parity selection. The historical search branch is 5.08450258 d. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This conditional formal error is not total calibrated uncertainty or an exhaustive alias search. Live MAST timeseries availability query is retained in ../232533575-availability.json; availability is not an eclipse detection. The two intervening predicted cycles have no quality-zero or flagged QLP cadences within 0.25 d, so neither is a clean null.
3. **Source attribution.** Historical sector 77 TESScut difference image puts the deficit 0.98 arcsec from the target coordinate; peak [8, 7] versus target pixel [8, 8]. Image-model fractional residual 0.154 is not a localization error. Capable Gaia neighbors within 60 arcsec: none under the approximate G-band flux budget. Intrinsic required losses use an approximate flux budget and cannot be equated to blended pixel loss.
4. **Alternative reduction.** Background-subtracted TESScut target 1x1/3x3/5x5 apertures yield 24.67/25.12/24.73 ppt in 2 stacked historical events; representative QLP raw median selected depth is 27.78 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. aperture dilution and event choice limit direct depth comparison.
5. **Gaia geometry.** Matched DR3 source 1285502678268839680 has SB1 P = 5.0852473937 d and e = 0.04997. Closest edge-on conjunction offset is -0.35556 d (-0.06992 phase), with 0.18332 d linearly propagated full source-specific SB1 covariance. Rough central duration 4.50 h versus observed median fit 2.15 h assumes TIC radius and a minimum-mass main-sequence companion, not a complete binary model. Agreement does not prove source identity.

**Interpretation and limitation:** Two target-centered eclipses in sector 77 are separated by 15.252 d. The Gaia-like 5.084-d period assigns three cycles, but cycles 291 and 292 fall in an observation gap. Sector 23 has no usable repeated center and current MAST lists only sectors 23 and 77. Thus the integer-cycle alias is untested by a third eclipse; the reported period is conditional on the Gaia-supported three-cycle assignment.

**Next check:** A third measured eclipse in future coverage to distinguish 15.252 d divided by three from other integer-cycle aliases.

Catalogue novelty: central seven-group result is ../../shared-catalogues/coverage-matrix.csv. A cone source alone is not an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 77 | 290 | 3405.0730806 | 0.001157 | 27.08 | used |
| 77 | 293 | 3420.3251187 | 0.001157 | 28.48 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s77.json, historical/diff_s77.png, historical/gaia.json and ../helper-audit.md. Original TESScut: [local path omitted] (SHA256 in ../source-hashes.json). Retained artifacts are in ../SHA256SUMS.json.


Stable review key: R454. Public evidence files: [diff_s77.json](../../evidence/232533575/historical/diff_s77.json), [diff_s77.png](../../evidence/232533575/historical/diff_s77.png), [gaia.json](../../evidence/232533575/historical/gaia.json), [measurements.json](../../evidence/232533575/measurements.json), [raw-events.png](../../evidence/232533575/raw-events.png), [raw-windows.csv](../../evidence/232533575/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch05/INDEX.md). 
