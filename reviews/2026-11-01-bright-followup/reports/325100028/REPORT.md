# TIC 325100028: PROBABLE

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 5 fitted representative eclipses in sectors [11, 38, 100]; 5 enter the reported timing fit. Local trapezoids have free centers, depths, durations and baselines. Predicted times guided windows only; flagged or uncovered intervals are not clean nulls. See raw-events.png, raw-windows.csv and measurements.json.
2. **Measured timing and aliases: pass.** 5 same-kind actual midpoints yield P = 13.9493523851 ± 0.0000240409 d and reference epoch BTJD 1614.7612349 (Selected repeating eclipse; primary by convention; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; representative parity shows no persistent unequal alternation. Same-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Half/double alias assessment is bounded by representative raw morphology, not an exhaustive blind period search.
3. **Source attribution: unresolved.** Historical sector 38 cutout places the deficit centroid 6.02 arcsec from the target; peak pixel [8, 8] versus target pixel [8, 8]. Image-model fractional residual 0.932 is not a calibrated localization error. Gaia neighbors capable under the approximate G-band flux budget: Gaia 5864512143196081408: 12.3 arcsec, G 13.418, approximate intrinsic eclipse requirement 0.602; Gaia 5866013285774822528: 29.1 arcsec, G 11.757, approximate intrinsic eclipse requirement 0.252; Gaia 5866013285781269376: 31.6 arcsec, G 10.036, approximate intrinsic eclipse requirement 0.175. The neighbor intrinsic eclipse requirement is not directly comparable to blended pixel fractional loss.
4. **Alternative reduction: supports recurring loss with unresolved host.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 63.30/23.38/19.85 ppt over 2 stacked events, compared with median selected QLP raw fit depth 170.08 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution or mixed eclipse kinds limit depth equality. and aperture dilution or mixed eclipse kinds limit depth equality.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 5866013354494300928 has P = 13.9475152836 d and e = 0.22338. The closest edge-on conjunction offset at the measured epoch is 0.13013 d (0.00933 phase), with 0.22414 d linearly propagated full-SB1-covariance timing error. A rough central duration is 7.05 h versus observed median 5.67 h; TIC radius and minimum-mass companion are approximations, and impact parameter is not fitted.

**Deciding interpretation and limitation:** Five raw eclipses, including S38 events coincident with the historical TESScut stack, recur at one period. The S38 cutout shows a central deficit but its 3x3 depths of about 23 ppt disagree substantially with QLP raw fits of 164-183 ppt; dilution is plausible but not quantitatively demonstrated. A capable 12.3-arcsec Gaia neighbor remains viable at TESS resolution, so the host is unresolved.

**Next check:** Resolved eclipse imaging and independent aperture/PRF characterization of the crowded field.

Catalogue novelty is in the central seven-group ../../shared-catalogues/coverage-matrix.csv receipt; physical classification does not assert exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Orbital timing status |
|---|---:|---:|---:|---:|---|
| 11 | 1 | 1614.7633607 | 0.010417 | 156.81 | used |
| 38 | 53 | 2340.1255290 | 0.003472 | 182.88 | used |
| 38 | 54 | 2354.0787364 | 0.003472 | 164.43 | used |
| 100 | 178 | 4083.7950061 | 0.001157 | 170.08 | used |
| 100 | 179 | 4097.7475570 | 0.001157 | 175.18 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s38.json, historical/diff_s38.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). All evidence and source files are in ../SHA256SUMS.json.


Stable review key: R506. Public evidence files: [diff_s38.json](../../evidence/325100028/historical/diff_s38.json), [diff_s38.png](../../evidence/325100028/historical/diff_s38.png), [gaia.json](../../evidence/325100028/historical/gaia.json), [measurements.json](../../evidence/325100028/measurements.json), [raw-events.png](../../evidence/325100028/raw-events.png), [raw-windows.csv](../../evidence/325100028/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch10/INDEX.md). 
