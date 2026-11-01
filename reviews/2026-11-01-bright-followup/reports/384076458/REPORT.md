# TIC 384076458: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw evidence.** Quality-zero QLP SAP_FLUX gives 16 timing-selected measured centers in sectors [66, 102]. Local trapezoids fit free centers, depths, durations and baselines. Raw plots and windows retain the evidence. Predicted centers guided extraction only; flagged or uncovered windows are not null detections. Representative raw morphology shows repeated eclipses.
2. **Timing and aliases.** Selected centers yield P = 2.7847243427 ± 0.0000015681 d and reference epoch BTJD 3100.5639723 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). There are 12 within-sector same-kind adjacent pairs after the specified parity selection. The historical search branch is 2.78472813 d. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This conditional formal error is not total calibrated uncertainty or an exhaustive alias search.
3. **Source attribution.** Historical sector 65 TESScut difference image puts the deficit 3.54 arcsec from the target coordinate; peak [8, 8] versus target pixel [8, 8]. Image-model fractional residual 0.204 is not a localization error. Capable Gaia neighbors within 60 arcsec: Gaia 5778272945037909632 (46.63 arcsec, G 15.372, intrinsic required loss about 0.728). Intrinsic required losses use an approximate flux budget and cannot be equated to blended pixel loss.
4. **Alternative reduction.** Background-subtracted TESScut target 1x1/3x3/5x5 apertures yield 36.20/35.87/33.61 ppt in 10 stacked historical events; representative QLP raw median selected depth is 35.73 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. aperture dilution and event choice limit direct depth comparison.
5. **Gaia geometry.** Matched DR3 source 5778272841958695040 has SB1 P = 2.7847986876 d and e = 0.02887. Closest edge-on conjunction offset is -0.05097 d (-0.01830 phase), with 0.08625 d linearly propagated full source-specific SB1 covariance. Rough central duration 4.37 h versus observed median fit 2.49 h assumes TIC radius and a minimum-mass main-sequence companion, not a complete binary model. Agreement does not prove source identity.

**Interpretation and limitation:** Sixteen measured raw eclipses span sectors 66 and 102 with twelve adjacent-cycle pairs. The only approximately capable Gaia neighbor is 46.6 arcsec away from the target-centered deficit.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is ../../shared-catalogues/coverage-matrix.csv. A cone source alone is not an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 66 | 529 | 3100.5639140 | 0.001157 | 39.84 | used |
| 66 | 530 | 3103.3478225 | 0.001157 | 38.49 | used |
| 66 | 531 | 3106.1333249 | 0.001157 | 39.70 | used |
| 66 | 532 | 3108.9189679 | 0.001157 | 39.74 | used |
| 66 | 534 | 3114.4877752 | 0.001157 | 39.69 | used |
| 66 | 535 | 3117.2728831 | 0.001157 | 39.11 | used |
| 66 | 536 | 3120.0566188 | 0.001157 | 40.71 | used |
| 66 | 537 | 3122.8416413 | 0.001157 | 38.09 | used |
| 102 | 898 | 4128.1276997 | 0.001157 | 32.10 | used |
| 102 | 899 | 4130.9119539 | 0.001157 | 32.48 | used |
| 102 | 900 | 4133.6967499 | 0.001157 | 32.44 | used |
| 102 | 901 | 4136.4814578 | 0.001157 | 32.36 | used |
| 102 | 903 | 4142.0514537 | 0.001157 | 31.56 | used |
| 102 | 904 | 4144.8357621 | 0.001157 | 33.36 | used |
| 102 | 905 | 4147.6196430 | 0.001157 | 33.10 | used |
| 102 | 906 | 4150.4045059 | 0.001157 | 30.63 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s65.json, historical/diff_s65.png, historical/gaia.json and ../helper-audit.md. Original TESScut: [local path omitted] (SHA256 in ../source-hashes.json). Retained artifacts are in ../SHA256SUMS.json.


Stable review key: R450. Public evidence files: [diff_s65.json](../../evidence/384076458/historical/diff_s65.json), [diff_s65.png](../../evidence/384076458/historical/diff_s65.png), [gaia.json](../../evidence/384076458/historical/gaia.json), [measurements.json](../../evidence/384076458/measurements.json), [raw-events.png](../../evidence/384076458/raw-events.png), [raw-windows.csv](../../evidence/384076458/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch05/INDEX.md). 
