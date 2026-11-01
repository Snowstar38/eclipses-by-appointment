# TIC 156976058: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw evidence.** Quality-zero QLP SAP_FLUX contains 14 timing-usable measured centers in sectors [26, 53, 80]. Local trapezoids fit free centers, depths, durations and baselines. Raw plots and windows retain the evidence. Predicted centers guided extraction only; flagged or uncovered windows are not null detections. Representative morphology shows repeated eclipses.
2. **Timing and aliases.** Measured centers yield P = 3.4336457438 ± 0.0000062829 d and reference epoch BTJD 2018.9522980 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). There are 10 within-sector adjacent same-kind pairs (../alias-audit.json). Measured centers and same-kind pairs support the bounded period and alias check. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This formal error is not total calibrated uncertainty or an exhaustive alias search.
3. **Source attribution.** Historical sector 40 TESScut difference image puts the deficit 1.65 arcsec from the target coordinate; peak [8, 7] versus target pixel [8, 7]. Image-model fractional residual 0.465 is not a localization error. Capable Gaia neighbors within 60 arcsec: Gaia 4523316211621183872 (55.81 arcsec, G 13.768, intrinsic loss approx. 0.794). Intrinsic-loss requirements use an approximate flux budget and cannot be equated to blended pixel loss.
4. **Alternative reduction.** Background-subtracted TESScut 1x1/3x3/5x5 target apertures yield 132.09/118.89/100.11 ppt in 5 stacked historical events; representative QLP raw median fit depth is 138.82 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and event choice limit depth comparisons.
5. **Gaia geometry.** Matched DR3 source 4523316314700411136 has SB1 P = 3.4333917898 d and e = 0.03177. Closest edge-on conjunction offset is 0.07574 d (0.02206 phase), with 0.08230 d linearly propagated full source-specific SB1 covariance. Rough central duration 4.49 h versus observed median fit 3.61 h assumes TIC radius and a minimum-mass main-sequence companion, not a full binary model. Agreement is not source proof.

**Interpretation and limitation:** Fourteen deep raw repeats include adjacent cycles in S53 and S80. The only nominally capable neighbor is 55.8 arcsec away, distinct from the target-centered deficit.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is ../../shared-catalogues/coverage-matrix.csv. A cone source alone is not an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 26 | 2 | 2018.9536896 | 0.010417 | 131.25 | used |
| 53 | 214 | 2746.8856511 | 0.003472 | 136.41 | used |
| 53 | 215 | 2750.3189356 | 0.003472 | 139.38 | used |
| 53 | 216 | 2753.7522898 | 0.003472 | 138.79 | used |
| 53 | 217 | 2757.1857718 | 0.003472 | 137.72 | used |
| 53 | 218 | 2760.6195976 | 0.003472 | 138.43 | used |
| 53 | 219 | 2764.0532691 | 0.003472 | 137.64 | used |
| 53 | 220 | 2767.4871060 | 0.003472 | 137.42 | used |
| 80 | 428 | 3481.6852727 | 0.001157 | 138.85 | used |
| 80 | 431 | 3491.9865294 | 0.001157 | 140.49 | used |
| 80 | 432 | 3495.4197879 | 0.001157 | 140.30 | used |
| 80 | 433 | 3498.8537895 | 0.001157 | 139.67 | used |
| 80 | 434 | 3502.2872671 | 0.001157 | 139.86 | used |
| 80 | 435 | 3505.7208234 | 0.001157 | 141.64 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s40.json, historical/diff_s40.png, historical/gaia.json and ../helper-audit.md. Original TESScut: [local path omitted] (SHA256 in ../source-hashes.json). Retained artifacts are in ../SHA256SUMS.json.


Stable review key: R438. Public evidence files: [diff_s40.json](../../evidence/156976058/historical/diff_s40.json), [diff_s40.png](../../evidence/156976058/historical/diff_s40.png), [gaia.json](../../evidence/156976058/historical/gaia.json), [measurements.json](../../evidence/156976058/measurements.json), [raw-events.png](../../evidence/156976058/raw-events.png), [raw-windows.csv](../../evidence/156976058/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch03/INDEX.md). 
