# TIC 233199615: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 13 fitted representative eclipses in sectors [14, 53, 86]; 13 enter the reported timing fit. Local trapezoids have free centers, depths, durations and baselines. Predicted times guided windows only; flagged or uncovered intervals are not clean nulls. See raw-events.png, raw-windows.csv and measurements.json.
2. **Measured timing and aliases: pass.** 13 same-kind actual midpoints yield P = 4.3672327612 ± 0.0000067972 d and reference epoch BTJD 1685.2243747 (Selected repeating eclipse; primary by convention; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; representative parity shows no persistent unequal alternation. Same-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Half/double alias assessment is bounded by representative raw morphology, not an exhaustive blind period search.
3. **Source attribution: favors target at TESS pixel resolution.** Historical sector 75 cutout places the deficit centroid 3.05 arcsec from the target; peak pixel [7, 8] versus target pixel [7, 8]. Image-model fractional residual 0.884 is not a calibrated localization error. Gaia neighbors capable under the approximate G-band flux budget: None within 60 arcsec under the approximate G-band flux budget. The neighbor intrinsic eclipse requirement is not directly comparable to blended pixel fractional loss.
4. **Alternative reduction: pass.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 109.47/108.17/97.70 ppt over 6 stacked events, compared with median selected QLP raw fit depth 107.83 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution or mixed eclipse kinds limit depth equality. and aperture dilution or mixed eclipse kinds limit depth equality.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 1638829129242739968 has P = 4.3672040925 d and e = 0.09279. The closest edge-on conjunction offset at the measured epoch is 0.05811 d (0.01331 phase), with 0.12907 d linearly propagated full-SB1-covariance timing error. A rough central duration is 4.84 h versus observed median 3.99 h; TIC radius and minimum-mass companion are approximations, and impact parameter is not fitted.

**Deciding interpretation and limitation:** Thirteen representative raw events across S14/53/86 repeat at the same period; the difference core is target-centered and no listed Gaia neighbor passes the approximate brightness screen.

**Next check:** Optional precision binary characterization.

Catalogue novelty is in the central seven-group ../../shared-catalogues/coverage-matrix.csv receipt; physical classification does not assert exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Orbital timing status |
|---|---:|---:|---:|---:|---|
| 14 | 0 | 1685.2271693 | 0.010417 | 108.74 | used |
| 14 | 3 | 1698.3305035 | 0.010417 | 106.48 | used |
| 53 | 243 | 2746.4615423 | 0.003472 | 110.72 | used |
| 53 | 244 | 2750.8292655 | 0.003472 | 111.05 | used |
| 53 | 245 | 2755.1959690 | 0.003472 | 110.40 | used |
| 53 | 246 | 2759.5631421 | 0.003472 | 109.28 | used |
| 53 | 247 | 2763.9305927 | 0.003472 | 108.97 | used |
| 53 | 248 | 2768.2977583 | 0.003472 | 107.83 | used |
| 86 | 447 | 3637.3775447 | 0.001157 | 104.42 | used |
| 86 | 449 | 3646.1118101 | 0.001157 | 105.91 | used |
| 86 | 450 | 3650.4798914 | 0.001157 | 106.67 | used |
| 86 | 451 | 3654.8463029 | 0.001157 | 105.04 | used |
| 86 | 452 | 3659.2129190 | 0.001157 | 104.29 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s75.json, historical/diff_s75.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). All evidence and source files are in ../SHA256SUMS.json.


Stable review key: R507. Public evidence files: [diff_s75.json](../../evidence/233199615/historical/diff_s75.json), [diff_s75.png](../../evidence/233199615/historical/diff_s75.png), [gaia.json](../../evidence/233199615/historical/gaia.json), [measurements.json](../../evidence/233199615/measurements.json), [raw-events.png](../../evidence/233199615/raw-events.png), [raw-windows.csv](../../evidence/233199615/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch10/INDEX.md). 
