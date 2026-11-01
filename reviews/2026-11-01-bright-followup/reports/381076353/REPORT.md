# TIC 381076353: PLAUSIBLE

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate. This report reviews the frozen batch04 target; historical screening is not an admission verdict.

1. **Raw events.** Quality-zero QLP SAP_FLUX shows 12 timing-selected candidate depressions in sectors [11, 99, 102]. Local trapezoid fits allow free centers and baseline. Predicted windows are search guides only; flagged or sparsely sampled windows are not null detections. Numeric windows and the raw plot retain the evidence.
2. **Timing and aliases.** Measured repeating depression centers give P=3.6112653345 d, fit error=0.0000376302 d, epoch BTJD 1603.6849541 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). There are 5 consecutive within-sector same-kind cycle pairs. The inventory period was 3.61123 d and the historical SAP search branch was 3.6112336247 d. All selected historical photometric cycles used; no systematic alternating depth pattern requiring a double-period fit in representative data. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. The fit error is not calibrated total uncertainty. This bounded alias check is not an exhaustive blind period search.
3. **Pixel attribution: unresolved at TESS resolution.** Historical S65 TESScut deficit core is 3.71 arcsec from the target coordinate; peak pixel [8, 8] and target pixel [8, 8]. Fractional PSF model residual is 0.909, not a localization uncertainty. Capable Gaia neighbors: 1.9 arcsec, G=17.55, intrinsic-loss requirement ~0.48; 5.8 arcsec, G=16.08, intrinsic-loss requirement ~0.13; 6.8 arcsec, G=18.17, intrinsic-loss requirement ~0.85; 7.8 arcsec, G=15.47, intrinsic-loss requirement ~0.07; 9.2 arcsec, G=17.17, intrinsic-loss requirement ~0.34; 45 further capable sources in the 60 arcsec list. The full list and flux-budget calculation are in historical/diff_s65.json; the original cutout and stacked image are retained and hashed.
4. **Alternative reduction.** A target-centered, background-subtracted TESScut extraction gives 1x1/3x3/5x5 stacked depths 3.60/3.63/2.38 ppt from 8 selected windows. Median selected QLP raw fit depth is 3.05 ppt. Aperture dilution, event-kind mixing and model residuals limit direct depth comparisons. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument.
5. **Gaia orbit.** The matched DR3 NSS source 5864386386590001024 has P=3.6112336247 d and e=0.38173. Closest edge-on conjunction differs from the measured epoch by 0.00267 in phase (0.00964 d); linear propagation of the source-specific full SB1 covariance gives 0.07820 d as a descriptive timing scale. The rough central-duration estimate is 3.02 h versus trapezoid median 12.16 h; these assume a TIC radius and minimum-mass main-sequence companion and are not a full geometry fit or a sigma gate.

**Deciding interpretation and limitation.** Recurrent ~3 ppt depressions are comparable to local scatter. Folded S11 and S102 show localized troughs and recovery, but S99 is rounded and broad variability is not decisively excluded; eclipse morphology remains uncertain. Fifty capable Gaia sources within 60 arcsec include several within 8 arcsec; the target-centered core has 0.909 image-model fractional residual, leaving attribution unresolved. Trapezoid durations and timing are shape-sensitive (up to 113 min timing residual).

**Next check.** Higher-resolution time-series photometry to test eclipse morphology and source attribution.

Catalogue novelty is evaluated centrally against seven scoped groups in ../../shared-catalogues/coverage-matrix.csv. This physical review does not assert exhaustive literature priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 11 | 0 | 1603.6846601 | 0.023909 | 3.34 | used |
| 11 | 1 | 1607.2888763 | 0.013657 | 3.93 | used |
| 11 | 4 | 1618.1752398 | 0.033312 | 2.81 | used |
| 11 | 5 | 1621.7413685 | 0.022295 | 2.20 | used |
| 99 | 677 | 4048.5136194 | 0.016278 | 3.02 | used |
| 99 | 678 | 4052.0649452 | 0.015813 | 3.08 | used |
| 99 | 682 | 4066.5666518 | 0.013352 | 3.02 | used |
| 99 | 683 | 4070.2579081 | 0.018299 | 5.10 | used |
| 102 | 700 | 4131.5997979 | 0.009527 | 2.80 | used |
| 102 | 701 | 4135.1379910 | 0.012265 | 4.25 | used |
| 102 | 703 | 4142.4034336 | 0.010024 | 2.88 | used |
| 102 | 705 | 4149.6213680 | 0.015593 | 3.55 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s65.json, historical/diff_s65.png, historical/gaia.json, original TESScut [local path omitted] and ../helper-audit.md. The original cutout and source files are SHA-256 recorded in ../source-hashes.json and ../SHA256SUMS.json.


Stable review key: R440. Public evidence files: [diff_s65.json](../../evidence/381076353/historical/diff_s65.json), [diff_s65.png](../../evidence/381076353/historical/diff_s65.png), [gaia.json](../../evidence/381076353/historical/gaia.json), [measurements.json](../../evidence/381076353/measurements.json), [raw-events.png](../../evidence/381076353/raw-events.png), [raw-windows.csv](../../evidence/381076353/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch04/INDEX.md). 
