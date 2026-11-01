# TIC 436762701: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate. This report reviews the frozen batch04 target; historical screening is not an admission verdict.

1. **Raw events.** Quality-zero QLP SAP_FLUX shows 7 timing-selected measured eclipses in sectors [56, 83]. Local trapezoid fits allow free centers and baseline. Predicted windows are search guides only; flagged or sparsely sampled windows are not null detections. Numeric windows and the raw plot retain the evidence.
2. **Timing and aliases.** Measured same-kind centers give P=7.5061902904 d, fit error=0.0000090645 d, epoch BTJD 2832.3413064 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). There are 5 consecutive within-sector same-kind cycle pairs. The inventory period was 7.50619 d and the historical SAP search branch was 7.5061923952 d. All selected historical photometric cycles used; no systematic alternating depth pattern requiring a double-period fit in representative data. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. The fit error is not calibrated total uncertainty. This bounded alias check is not an exhaustive blind period search.
3. **Pixel attribution: favors target at TESS resolution.** Historical S83 TESScut deficit core is 3.16 arcsec from the target coordinate; peak pixel [8, 7] and target pixel [8, 7]. Fractional PSF model residual is 0.667, not a localization uncertainty. Capable Gaia neighbors: none under the approximate G-band flux budget. The full list and flux-budget calculation are in historical/diff_s83.json; the original cutout and stacked image are retained and hashed.
4. **Alternative reduction.** A target-centered, background-subtracted TESScut extraction gives 1x1/3x3/5x5 stacked depths 117.56/115.42/108.68 ppt from 4 selected windows. Median selected QLP raw fit depth is 122.69 ppt. Aperture dilution, event-kind mixing and model residuals limit direct depth comparisons. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument.
5. **Gaia orbit.** The matched DR3 NSS source 1885079155014227584 has P=7.5069767062 d and e=0.18531. Closest edge-on conjunction differs from the measured epoch by -0.02604 in phase (-0.19548 d); linear propagation of the source-specific full SB1 covariance gives 0.13174 d as a descriptive timing scale. The rough central-duration estimate is 9.36 h versus trapezoid median 6.11 h; these assume a TIC radius and minimum-mass main-sequence companion and are not a full geometry fit or a sigma gate.

**Deciding interpretation and limitation.** Seven deep raw events across S56 and S83 include consecutive cycles, with consistent depths and a target-centered deficit.

**Next check.** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty is evaluated centrally against seven scoped groups in ../../shared-catalogues/coverage-matrix.csv. This physical review does not assert exhaustive literature priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 56 | 0 | 2832.3415322 | 0.001157 | 122.89 | used |
| 56 | 1 | 2839.8472492 | 0.001157 | 122.69 | used |
| 56 | 2 | 2847.3537074 | 0.001157 | 123.96 | used |
| 83 | 97 | 3560.4416157 | 0.001157 | 122.32 | used |
| 83 | 98 | 3567.9480430 | 0.001157 | 121.48 | used |
| 83 | 99 | 3575.4543530 | 0.001157 | 121.25 | used |
| 83 | 100 | 3582.9601899 | 0.001157 | 122.98 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s83.json, historical/diff_s83.png, historical/gaia.json, original TESScut [local path omitted] and ../helper-audit.md. The original cutout and source files are SHA-256 recorded in ../source-hashes.json and ../SHA256SUMS.json.


Stable review key: R443. Public evidence files: [diff_s83.json](../../evidence/436762701/historical/diff_s83.json), [diff_s83.png](../../evidence/436762701/historical/diff_s83.png), [gaia.json](../../evidence/436762701/historical/gaia.json), [measurements.json](../../evidence/436762701/measurements.json), [raw-events.png](../../evidence/436762701/raw-events.png), [raw-windows.csv](../../evidence/436762701/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch04/INDEX.md). 
