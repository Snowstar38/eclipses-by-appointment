# TIC 248688713: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw evidence.** Quality-zero QLP SAP_FLUX contains 6 timing-usable measured centers in sectors [32, 98]. Local trapezoids fit free centers, depths, durations and baselines. Raw plots and windows retain the evidence. Predicted centers guided extraction only; flagged or uncovered windows are not null detections. Representative morphology shows repeated eclipses.
2. **Timing and aliases.** Measured centers yield P = 10.2703783974 ± 0.0000121037 d and reference epoch BTJD 2178.2697573 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). There are 3 within-sector adjacent same-kind pairs (../alias-audit.json). Measured centers and same-kind pairs support the bounded period and alias check. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This formal error is not total calibrated uncertainty or an exhaustive alias search.
3. **Source attribution.** Historical sector 32 TESScut difference image puts the deficit 3.00 arcsec from the target coordinate; peak [7, 8] versus target pixel [7, 8]. Image-model fractional residual 0.867 is not a localization error. Capable Gaia neighbors within 60 arcsec: Gaia 3205176248663357440 (31.57 arcsec, G 10.569, intrinsic loss approx. 0.054). Intrinsic-loss requirements use an approximate flux budget and cannot be equated to blended pixel loss.
4. **Alternative reduction.** Background-subtracted TESScut 1x1/3x3/5x5 target apertures yield 22.05/10.14/8.07 ppt in 3 stacked historical events; representative QLP raw median fit depth is 43.88 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and event choice limit depth comparisons.
5. **Gaia geometry.** Matched DR3 source 3205176283023095424 has SB1 P = 10.2702471905 d and e = 0.09526. Closest edge-on conjunction offset is -0.01040 d (-0.00101 phase), with 0.82596 d linearly propagated full source-specific SB1 covariance. Rough central duration 5.62 h versus observed median fit 4.08 h assumes TIC radius and a minimum-mass main-sequence companion, not a full binary model. Agreement is not source proof.

**Interpretation and limitation:** Adjacent S32 cycles and S98 repeats establish recurrence. The brighter capable neighbor at 31.6 arcsec is distinct from the target-centered deficit; high image-model residual limits precision.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is ../../shared-catalogues/coverage-matrix.csv. A cone source alone is not an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 32 | 0 | 2178.2702044 | 0.003472 | 49.46 | used |
| 32 | 1 | 2188.5407239 | 0.003472 | 42.73 | used |
| 32 | 2 | 2198.8094783 | 0.003472 | 46.97 | used |
| 98 | 177 | 3996.1259138 | 0.001736 | 42.68 | used |
| 98 | 179 | 4016.6684904 | 0.001197 | 43.72 | used |
| 98 | 180 | 4026.9371326 | 0.001314 | 44.03 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s32.json, historical/diff_s32.png, historical/gaia.json and ../helper-audit.md. Original TESScut: [local path omitted] (SHA256 in ../source-hashes.json). Retained artifacts are in ../SHA256SUMS.json.


Stable review key: R430. Public evidence files: [diff_s32.json](../../evidence/248688713/historical/diff_s32.json), [diff_s32.png](../../evidence/248688713/historical/diff_s32.png), [gaia.json](../../evidence/248688713/historical/gaia.json), [measurements.json](../../evidence/248688713/measurements.json), [raw-events.png](../../evidence/248688713/raw-events.png), [raw-windows.csv](../../evidence/248688713/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch03/INDEX.md). 
