# TIC 335502443: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw evidence.** Quality-zero QLP SAP_FLUX contains 5 timing-usable measured centers in sectors [60, 74]. Local trapezoids fit free centers, depths, durations and baselines. Raw plots and windows retain the evidence. Predicted centers guided extraction only; flagged or uncovered windows are not null detections. Representative morphology shows repeated eclipses.
2. **Timing and aliases.** Measured centers yield P = 8.7702776381 ± 0.0000245490 d and reference epoch BTJD 2939.8641685 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). There are 2 within-sector adjacent same-kind pairs (../alias-audit.json). Measured centers and same-kind pairs support the bounded period and alias check. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This formal error is not total calibrated uncertainty or an exhaustive alias search.
3. **Source attribution.** Historical sector 60 TESScut difference image puts the deficit 1.55 arcsec from the target coordinate; peak [7, 8] versus target pixel [7, 8]. Image-model fractional residual 0.193 is not a localization error. Capable Gaia neighbors within 60 arcsec: Gaia 1088529297616817152 (16.22 arcsec, G 15.075, intrinsic loss approx. 0.704). Intrinsic-loss requirements use an approximate flux budget and cannot be equated to blended pixel loss.
4. **Alternative reduction.** Background-subtracted TESScut 1x1/3x3/5x5 target apertures yield 41.06/39.39/38.17 ppt in 3 stacked historical events; representative QLP raw median fit depth is 42.90 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and event choice limit depth comparisons.
5. **Gaia geometry.** Matched DR3 source 1088529293321259648 has SB1 P = 8.7704426450 d and e = 0.03074. Closest edge-on conjunction offset is -0.01668 d (-0.00190 phase), with 0.24762 d linearly propagated full source-specific SB1 covariance. Rough central duration 6.49 h versus observed median fit 3.45 h assumes TIC radius and a minimum-mass main-sequence companion, not a full binary model. Agreement is not source proof.

**Interpretation and limitation:** Five raw repeats include adjacent S60 cycles. A capable neighbor 16.2 arcsec away is distinct from the target-centered deficit core at TESS resolution.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is ../../shared-catalogues/coverage-matrix.csv. A cone source alone is not an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 60 | 0 | 2939.8637048 | 0.001157 | 42.74 | used |
| 60 | 1 | 2948.6343381 | 0.001157 | 42.90 | used |
| 60 | 2 | 2957.4053258 | 0.001157 | 44.07 | used |
| 74 | 43 | 3316.9859743 | 0.001157 | 41.95 | used |
| 74 | 45 | 3334.5267647 | 0.001157 | 43.96 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s60.json, historical/diff_s60.png, historical/gaia.json and ../helper-audit.md. Original TESScut: [local path omitted] (SHA256 in ../source-hashes.json). Retained artifacts are in ../SHA256SUMS.json.


Stable review key: R439. Public evidence files: [diff_s60.json](../../evidence/335502443/historical/diff_s60.json), [diff_s60.png](../../evidence/335502443/historical/diff_s60.png), [gaia.json](../../evidence/335502443/historical/gaia.json), [measurements.json](../../evidence/335502443/measurements.json), [raw-events.png](../../evidence/335502443/raw-events.png), [raw-windows.csv](../../evidence/335502443/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch03/INDEX.md). 
