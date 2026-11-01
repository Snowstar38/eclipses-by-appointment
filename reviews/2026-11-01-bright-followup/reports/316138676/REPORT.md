# TIC 316138676: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are recorded separately. The historical screening label is not an admission verdict.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 5 timing-usable measured eclipses in representative sectors [18, 59, 86]. The raw plot and numeric windows retain the light-curve evidence. Local trapezoids have free centers, depths, durations and baselines. Historical predicted times guided windows only. Flagged or uncovered intervals are not null detections.
2. **Measured timing and alias: pass.** 5 actual midpoints yield P = 13.9528465175 ± 0.0000217006 d and reference epoch BTJD 1805.4162403 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind cycle counts, within-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive blind all-period search.
3. **Source attribution: favors target at TESS image resolution.** Historical S19 cutout puts the deficit 2.82 arcsec from the target coordinate; peak [7, 8] versus target pixel [7, 8]. Image-model fractional residual 0.050; this is not a calibrated localization error. Capable Gaia neighbors: none within 60 arcsec under the approximate G-band flux budget. The intrinsic requirement uses an approximate flux budget and is not compared directly with a blended pixel fractional loss.
4. **Alternative reduction: pass.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 143.67/145.57/144.91 ppt in 2 stacked events; median selected QLP raw fit depth 151.16 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and any mixed event kinds limit depth comparisons.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 450156999764024576 has orbital P = 13.9484101055 d, e = 0.12110; closest edge-on conjunction offset at the measured epoch is 0.36270 d (0.02600 phase), with 0.36683 d linearly propagated full-SB1-covariance timing error. The rough central duration is 27.72 h versus observed median 10.23 h; assumed TIC radius and minimum-mass companion are not a full fit. Geometry supports physical plausibility without an arbitrary sigma veto.

**Deciding interpretation and limitation:** Five deep raw eclipses across S18/59/86, including consecutive S59 and S86 cycles. The deficit core is centered on the target; no capable Gaia neighbor is present under the approximate brightness screen. The long fitted duration is geometry dependent.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is in ../../shared-catalogues/coverage-matrix.csv. A cone-source entry alone does not establish an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 18 | 0 | 1805.4159110 | 0.010417 | 151.16 | used |
| 59 | 80 | 2921.6441111 | 0.001157 | 153.19 | used |
| 59 | 81 | 2935.5966595 | 0.001157 | 151.93 | used |
| 86 | 132 | 3647.1923341 | 0.001157 | 150.47 | used |
| 86 | 133 | 3661.1444770 | 0.001157 | 151.00 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s19.json, historical/diff_s19.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). Source code and all retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R490. Public evidence files: [diff_s19.json](../../evidence/316138676/historical/diff_s19.json), [diff_s19.png](../../evidence/316138676/historical/diff_s19.png), [gaia.json](../../evidence/316138676/historical/gaia.json), [measurements.json](../../evidence/316138676/measurements.json), [raw-events.png](../../evidence/316138676/raw-events.png), [raw-windows.csv](../../evidence/316138676/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch09/INDEX.md). 
