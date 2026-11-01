# TIC 305826287: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 8 fitted representative eclipses in sectors [58, 85]; 8 enter the reported timing fit. Local trapezoids have free centers, depths, durations and baselines. Predicted times guided windows only; flagged or uncovered intervals are not clean nulls. See raw-events.png, raw-windows.csv and measurements.json.
2. **Measured timing and aliases: pass.** 8 same-kind actual midpoints yield P = 5.9986588262 ± 0.0000069644 d and reference epoch BTJD 2883.0297295 (Selected repeating eclipse; primary by convention; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; representative parity shows no persistent unequal alternation. Same-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Half/double alias assessment is bounded by representative raw morphology, not an exhaustive blind period search.
3. **Source attribution: favors target at TESS pixel resolution.** Historical sector 58 cutout places the deficit centroid 3.93 arcsec from the target; peak pixel [7, 7] versus target pixel [7, 7]. Image-model fractional residual 0.454 is not a calibrated localization error. Gaia neighbors capable under the approximate G-band flux budget: Gaia 414950435582368640: 44.5 arcsec, G 13.760, approximate intrinsic eclipse requirement 0.186. The neighbor intrinsic eclipse requirement is not directly comparable to blended pixel fractional loss.
4. **Alternative reduction: pass.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 37.50/35.53/32.80 ppt over 5 stacked events, compared with median selected QLP raw fit depth 36.65 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution or mixed eclipse kinds limit depth equality. and aperture dilution or mixed eclipse kinds limit depth equality.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 414950435582368256 has P = 5.9989472733 d and e = 0.39238. The closest edge-on conjunction offset at the measured epoch is -0.14458 d (-0.02410 phase), with 0.64607 d linearly propagated full-SB1-covariance timing error. A rough central duration is 3.64 h versus observed median 2.88 h; TIC radius and minimum-mass companion are approximations, and impact parameter is not fitted.

**Deciding interpretation and limitation:** Eight raw events across S58/85 have stable depth and a target-centered difference core; the one capable listed neighbor is 44.5 arcsec away.

**Next check:** Optional precision binary characterization.

Catalogue novelty is in the central seven-group ../../shared-catalogues/coverage-matrix.csv receipt; physical classification does not assert exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Orbital timing status |
|---|---:|---:|---:|---:|---|
| 58 | 186 | 2883.0292527 | 0.001157 | 36.46 | used |
| 58 | 187 | 2889.0284961 | 0.001157 | 36.83 | used |
| 58 | 188 | 2895.0278311 | 0.001157 | 36.27 | used |
| 58 | 189 | 2901.0258443 | 0.001157 | 36.28 | used |
| 58 | 190 | 2907.0238045 | 0.001157 | 36.22 | used |
| 85 | 308 | 3614.8659518 | 0.001157 | 37.51 | used |
| 85 | 309 | 3620.8653653 | 0.001157 | 37.55 | used |
| 85 | 311 | 3632.8616442 | 0.001157 | 37.87 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s58.json, historical/diff_s58.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). All evidence and source files are in ../SHA256SUMS.json.


Stable review key: R505. Public evidence files: [diff_s58.json](../../evidence/305826287/historical/diff_s58.json), [diff_s58.png](../../evidence/305826287/historical/diff_s58.png), [gaia.json](../../evidence/305826287/historical/gaia.json), [measurements.json](../../evidence/305826287/measurements.json), [raw-events.png](../../evidence/305826287/raw-events.png), [raw-windows.csv](../../evidence/305826287/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch10/INDEX.md). 
