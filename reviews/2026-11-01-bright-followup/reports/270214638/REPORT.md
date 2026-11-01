# TIC 270214638: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw evidence.** Quality-zero QLP SAP_FLUX contains 6 timing-usable measured centers in sectors [25, 52, 80]. Local trapezoids fit free centers, depths, durations and baselines. Raw plots and windows retain the evidence. Predicted centers guided extraction only; flagged or uncovered windows are not null detections. Representative morphology shows repeated eclipses.
2. **Timing and aliases.** Measured centers yield P = 6.3519439147 ± 0.0000246588 d and reference epoch BTJD 2006.5507448 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). There are 2 within-sector adjacent same-kind pairs (../alias-audit.json). Measured centers and same-kind pairs support the bounded period and alias check. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This formal error is not total calibrated uncertainty or an exhaustive alias search.
3. **Source attribution.** Historical sector 40 TESScut difference image puts the deficit 4.28 arcsec from the target coordinate; peak [7, 8] versus target pixel [7, 8]. Image-model fractional residual 0.143 is not a localization error. Capable Gaia neighbors within 60 arcsec: none under approximate G-band flux budget. Intrinsic-loss requirements use an approximate flux budget and cannot be equated to blended pixel loss.
4. **Alternative reduction.** Background-subtracted TESScut 1x1/3x3/5x5 target apertures yield 152.27/151.57/149.77 ppt in 4 stacked historical events; representative QLP raw median fit depth is 150.54 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and event choice limit depth comparisons.
5. **Gaia geometry.** Matched DR3 source 1360991195262446720 has SB1 P = 6.3527030171 d and e = 0.00643. Closest edge-on conjunction offset is -0.19216 d (-0.03025 phase), with 0.19511 d linearly propagated full source-specific SB1 covariance. Rough central duration 4.95 h versus observed median fit 4.28 h assumes TIC radius and a minimum-mass main-sequence companion, not a full binary model. Agreement is not source proof.

**Interpretation and limitation:** Six deep raw repeats span three sectors. The deficit is target-centered and no Gaia neighbor is capable under the approximate flux budget.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is ../../shared-catalogues/coverage-matrix.csv. A cone source alone is not an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 25 | 3 | 2006.5555644 | 0.010417 | 154.48 | used |
| 52 | 116 | 2724.3167245 | 166474.921768 | 149.71 | excluded: Singular or unidentifiable center covariance: formal timing uncertainty exceeds search duration; excluded from ephemeris. |
| 52 | 118 | 2737.0231476 | 0.003472 | 151.12 | used |
| 80 | 235 | 3480.2020761 | 0.001157 | 149.79 | used |
| 80 | 237 | 3492.9056726 | 0.001157 | 150.37 | used |
| 80 | 238 | 3499.2574710 | 0.001157 | 150.70 | used |
| 80 | 239 | 3505.6092753 | 0.001157 | 150.02 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s40.json, historical/diff_s40.png, historical/gaia.json and ../helper-audit.md. Original TESScut: [local path omitted] (SHA256 in ../source-hashes.json). Retained artifacts are in ../SHA256SUMS.json.


Stable review key: R435. Public evidence files: [diff_s40.json](../../evidence/270214638/historical/diff_s40.json), [diff_s40.png](../../evidence/270214638/historical/diff_s40.png), [gaia.json](../../evidence/270214638/historical/gaia.json), [measurements.json](../../evidence/270214638/measurements.json), [raw-events.png](../../evidence/270214638/raw-events.png), [raw-windows.csv](../../evidence/270214638/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch03/INDEX.md). 
