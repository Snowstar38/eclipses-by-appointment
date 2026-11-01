# TIC 700593737: PROBABLE

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw evidence.** Quality-zero QLP SAP_FLUX contains 3 timing-usable measured centers in sectors [19, 59]. Local trapezoids fit free centers, depths, durations and baselines. Raw plots and windows retain the evidence. Predicted centers guided extraction only; flagged or uncovered windows are not null detections. Representative morphology shows repeated eclipses.
2. **Timing and aliases.** Measured centers yield P = 14.0508013034 ± 0.0001326694 d and reference epoch BTJD 1824.4825619 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). There are 1 within-sector adjacent same-kind pairs (../alias-audit.json). Measured centers and same-kind pairs support the bounded period and alias check. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This formal error is not total calibrated uncertainty or an exhaustive alias search.
3. **Source attribution.** Historical sector 19 TESScut difference image puts the deficit 0.69 arcsec from the target coordinate; peak [8, 7] versus target pixel [8, 7]. Image-model fractional residual 0.866 is not a localization error. Capable Gaia neighbors within 60 arcsec: Gaia 190955384147342592 (2.80 arcsec, G 13.139, intrinsic loss approx. 0.301); Gaia 190955384151069696 (38.88 arcsec, G 14.451, intrinsic loss approx. 0.819); Gaia 190956857322461184 (47.10 arcsec, G 14.240, intrinsic loss approx. 0.688); Gaia 190956861618883840 (48.54 arcsec, G 14.129, intrinsic loss approx. 0.629); Gaia 190955349790083200 (58.08 arcsec, G 13.440, intrinsic loss approx. 0.371). Intrinsic-loss requirements use an approximate flux budget and cannot be equated to blended pixel loss.
4. **Alternative reduction.** Background-subtracted TESScut 1x1/3x3/5x5 target apertures yield 54.10/49.36/34.54 ppt in 2 stacked historical events; representative QLP raw median fit depth is 79.25 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and event choice limit depth comparisons.
5. **Gaia geometry.** Matched DR3 source 190955379851574912 has SB1 P = 14.0495286778 d and e = 0.40569. Closest edge-on conjunction offset is 0.01921 d (0.00137 phase), with 0.42354 d linearly propagated full source-specific SB1 covariance. Rough central duration 3.87 h versus observed median fit 4.16 h assumes TIC radius and a minimum-mass main-sequence companion, not a full binary model. Agreement is not source proof.

**Interpretation and limitation:** A raw S19 adjacent-cycle pair confirms repetition. A capable 2.8 arcsec Gaia companion shares the central TESS core; source attribution is unresolved.

**Next check:** Resolved eclipse photometry or multi-source PSF localization of the 2.8 arcsec pair.

Catalogue novelty: central seven-group result is ../../shared-catalogues/coverage-matrix.csv. A cone source alone is not an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 19 | 0 | 1824.4824625 | 0.010417 | 81.25 | used |
| 59 | 78 | 2920.4451605 | 0.001157 | 78.61 | used |
| 59 | 79 | 2934.4957691 | 0.001157 | 79.25 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s19.json, historical/diff_s19.png, historical/gaia.json and ../helper-audit.md. Original TESScut: [local path omitted] (SHA256 in ../source-hashes.json). Retained artifacts are in ../SHA256SUMS.json.


Stable review key: R432. Public evidence files: [diff_s19.json](../../evidence/700593737/historical/diff_s19.json), [diff_s19.png](../../evidence/700593737/historical/diff_s19.png), [gaia.json](../../evidence/700593737/historical/gaia.json), [measurements.json](../../evidence/700593737/measurements.json), [raw-events.png](../../evidence/700593737/raw-events.png), [raw-windows.csv](../../evidence/700593737/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch03/INDEX.md). 
