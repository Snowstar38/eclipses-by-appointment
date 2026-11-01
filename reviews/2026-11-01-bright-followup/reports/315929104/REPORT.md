# TIC 315929104: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 4 fitted representative eclipses in sectors [18, 59, 86]; 4 enter the reported timing fit. Local trapezoids have free centers, depths, durations and baselines. Predicted times guided windows only; flagged or uncovered intervals are not clean nulls. See raw-events.png, raw-windows.csv and measurements.json.
2. **Measured timing and aliases: pass.** 4 same-kind actual midpoints yield P = 10.1370634374 ± 0.0000192086 d and reference epoch BTJD 1801.1719141 (Selected repeating eclipse; primary by convention; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; representative parity shows no persistent unequal alternation. Same-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Half/double alias assessment is bounded by representative raw morphology, not an exhaustive blind period search.
3. **Source attribution: favors target at TESS pixel resolution.** Historical sector 18 cutout places the deficit centroid 1.70 arcsec from the target; peak pixel [8, 8] versus target pixel [8, 8]. Image-model fractional residual 0.460 is not a calibrated localization error. Gaia neighbors capable under the approximate G-band flux budget: Gaia 449247978525955200: 43.0 arcsec, G 13.261, approximate intrinsic eclipse requirement 0.088; Gaia 449244959165948032: 46.1 arcsec, G 16.177, approximate intrinsic eclipse requirement 0.951. The neighbor intrinsic eclipse requirement is not directly comparable to blended pixel fractional loss.
4. **Alternative reduction: pass.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 27.55/24.62/18.58 ppt over 2 stacked events, compared with median selected QLP raw fit depth 27.28 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution or mixed eclipse kinds limit depth equality. and aperture dilution or mixed eclipse kinds limit depth equality.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 449245027885422592 has P = 10.1358765398 d and e = 0.08420. The closest edge-on conjunction offset at the measured epoch is 0.13186 d (0.01301 phase), with 0.16823 d linearly propagated full-SB1-covariance timing error. A rough central duration is 8.05 h versus observed median 3.60 h; TIC radius and minimum-mass companion are approximations, and impact parameter is not fitted.

**Deciding interpretation and limitation:** Representative raw eclipses in S18/59/86 and a target-centered S18 difference core support the target; capable neighbors are tens of arcsec away.

**Next check:** Optional precision binary characterization.

Catalogue novelty is in the central seven-group ../../shared-catalogues/coverage-matrix.csv receipt; physical classification does not assert exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Orbital timing status |
|---|---:|---:|---:|---:|---|
| 18 | 0 | 1801.1711761 | 0.010417 | 24.56 | used |
| 59 | 110 | 2916.2480272 | 0.001157 | 27.72 | used |
| 59 | 111 | 2926.3868563 | 0.001157 | 27.42 | used |
| 86 | 182 | 3646.1174333 | 0.001157 | 27.15 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s18.json, historical/diff_s18.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). All evidence and source files are in ../SHA256SUMS.json.


Stable review key: R503. Public evidence files: [diff_s18.json](../../evidence/315929104/historical/diff_s18.json), [diff_s18.png](../../evidence/315929104/historical/diff_s18.png), [gaia.json](../../evidence/315929104/historical/gaia.json), [measurements.json](../../evidence/315929104/measurements.json), [raw-events.png](../../evidence/315929104/raw-events.png), [raw-windows.csv](../../evidence/315929104/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch10/INDEX.md). 
