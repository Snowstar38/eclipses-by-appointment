# TIC 462538667: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate. This report reviews the frozen batch04 target; historical screening is not an admission verdict.

1. **Raw events.** Quality-zero QLP SAP_FLUX shows 8 timing-selected measured eclipses in sectors [41, 75]. Local trapezoid fits allow free centers and baseline. Predicted windows are search guides only; flagged or sparsely sampled windows are not null detections. Numeric windows and the raw plot retain the evidence.
2. **Timing and aliases.** Measured same-kind centers give P=5.0931372216 d, fit error=0.0000093209 d, epoch BTJD 2421.1146206 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). There are 5 consecutive within-sector same-kind cycle pairs. The inventory period was 5.09313 d and the historical SAP search branch was 5.0931300597 d. All selected historical photometric cycles used; no systematic alternating depth pattern requiring a double-period fit in representative data. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. The fit error is not calibrated total uncertainty. This bounded alias check is not an exhaustive blind period search.
3. **Pixel attribution: favors target at TESS resolution.** Historical S40 TESScut deficit core is 2.62 arcsec from the target coordinate; peak pixel [7, 7] and target pixel [7, 7]. Fractional PSF model residual is 0.021, not a localization uncertainty. Capable Gaia neighbors: none under the approximate G-band flux budget. The full list and flux-budget calculation are in historical/diff_s40.json; the original cutout and stacked image are retained and hashed.
4. **Alternative reduction.** A target-centered, background-subtracted TESScut extraction gives 1x1/3x3/5x5 stacked depths 111.52/110.09/109.81 ppt from 5 selected windows. Median selected QLP raw fit depth is 112.46 ppt. Aperture dilution, event-kind mixing and model residuals limit direct depth comparisons. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument.
5. **Gaia orbit.** The matched DR3 NSS source 1688501177639000320 has P=5.0931642420 d and e=0.03904. Closest edge-on conjunction differs from the measured epoch by 0.02129 in phase (0.10842 d); linear propagation of the source-specific full SB1 covariance gives 0.13996 d as a descriptive timing scale. The rough central-duration estimate is 4.85 h versus trapezoid median 3.46 h; these assume a TIC radius and minimum-mass main-sequence companion and are not a full geometry fit or a sigma gate.

**Deciding interpretation and limitation.** Eight deep raw events across S41 and S75 include consecutive cycles, with a well-centered pixel deficit and stable depths.

**Next check.** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty is evaluated centrally against seven scoped groups in ../../shared-catalogues/coverage-matrix.csv. This physical review does not assert exhaustive literature priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 41 | 144 | 2421.1148783 | 0.003472 | 112.60 | used |
| 41 | 145 | 2426.2062636 | 0.003472 | 112.33 | used |
| 41 | 146 | 2431.3012696 | 0.003472 | 110.92 | used |
| 41 | 147 | 2436.3942317 | 0.003472 | 113.62 | used |
| 41 | 148 | 2441.4878561 | 0.003472 | 111.19 | used |
| 75 | 326 | 3348.0656501 | 0.001157 | 113.20 | used |
| 75 | 327 | 3353.1585480 | 0.001157 | 113.04 | used |
| 75 | 329 | 3363.3451330 | 0.001157 | 112.02 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s40.json, historical/diff_s40.png, historical/gaia.json, original TESScut [local path omitted] and ../helper-audit.md. The original cutout and source files are SHA-256 recorded in ../source-hashes.json and ../SHA256SUMS.json.


Stable review key: R444. Public evidence files: [diff_s40.json](../../evidence/462538667/historical/diff_s40.json), [diff_s40.png](../../evidence/462538667/historical/diff_s40.png), [gaia.json](../../evidence/462538667/historical/gaia.json), [measurements.json](../../evidence/462538667/measurements.json), [raw-events.png](../../evidence/462538667/raw-events.png), [raw-windows.csv](../../evidence/462538667/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch04/INDEX.md). 
