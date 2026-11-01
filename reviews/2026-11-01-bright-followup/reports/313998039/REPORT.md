# TIC 313998039: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are recorded separately. The historical screening label is not an admission verdict.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 4 timing-usable measured eclipses in representative sectors [76, 83]. The raw plot and numeric windows retain the light-curve evidence. Local trapezoids have free centers, depths, durations and baselines. Historical predicted times guided windows only. Flagged or uncovered intervals are not null detections.
2. **Measured timing and alias: pass.** 4 actual midpoints yield P = 11.9746788325 ± 0.0000721956 d and reference epoch BTJD 3378.4872332 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind cycle counts, within-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive blind all-period search.
3. **Source attribution: favors target at TESS image resolution.** Historical S56 cutout puts the deficit 2.09 arcsec from the target coordinate; peak [7, 7] versus target pixel [7, 7]. Image-model fractional residual 0.874; this is not a calibrated localization error. Capable Gaia neighbors: Gaia 2189517466440845568: 29.6 arcsec, G 10.549, approximate intrinsic eclipse requirement 0.405; Gaia 2189505711103804288: 39.1 arcsec, G 11.912, approximate intrinsic eclipse requirement 0.581. The intrinsic requirement uses an approximate flux budget and is not compared directly with a blended pixel fractional loss.
4. **Alternative reduction: pass.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 178.81/65.00/32.94 ppt in 3 stacked events; median selected QLP raw fit depth 355.60 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and any mixed event kinds limit depth comparisons.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 2189517466440848256 has orbital P = 11.9737068648 d, e = 0.06505; closest edge-on conjunction offset at the measured epoch is 0.48689 d (0.04066 phase), with 0.44849 d linearly propagated full-SB1-covariance timing error. The rough central duration is 5.44 h versus observed median 4.47 h; assumed TIC radius and minimum-mass companion are not a full fit. Geometry supports physical plausibility without an arbitrary sigma veto.

**Deciding interpretation and limitation:** Four deep raw eclipses in S76/83 repeat consistently. Bright capable neighbors at 29.6 and 39.1 arcsec cause severe aperture dilution, but the deficit core favors the target location; high image residual prevents precise localization.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is in ../../shared-catalogues/coverage-matrix.csv. A cone-source entry alone does not establish an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 76 | 138 | 3378.4870523 | 0.001157 | 354.55 | used |
| 76 | 139 | 3390.4621157 | 0.001157 | 347.14 | used |
| 83 | 154 | 3570.0819122 | 0.001157 | 370.01 | used |
| 83 | 155 | 3582.0569331 | 0.001157 | 356.65 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s56.json, historical/diff_s56.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). Source code and all retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R498. Public evidence files: [diff_s56.json](../../evidence/313998039/historical/diff_s56.json), [diff_s56.png](../../evidence/313998039/historical/diff_s56.png), [gaia.json](../../evidence/313998039/historical/gaia.json), [measurements.json](../../evidence/313998039/measurements.json), [raw-events.png](../../evidence/313998039/raw-events.png), [raw-windows.csv](../../evidence/313998039/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch09/INDEX.md). 
