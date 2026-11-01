# TIC 87159646: PROBABLE

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 3 fitted representative eclipses in sectors [59, 86]; 3 enter the reported timing fit. Local trapezoids have free centers, depths, durations and baselines. Predicted times guided windows only; flagged or uncovered intervals are not clean nulls. See raw-events.png, raw-windows.csv and measurements.json.
2. **Measured timing and aliases: pass.** 3 same-kind actual midpoints yield P = 11.2803975769 ± 0.0000584060 d and reference epoch BTJD 2922.0658972 (Selected repeating eclipse; primary by convention; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; representative parity shows no persistent unequal alternation. Same-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Half/double alias assessment is bounded by representative raw morphology, not an exhaustive blind period search.
3. **Source attribution: unresolved.** Historical sector 59 cutout places the deficit centroid 1.83 arcsec from the target; peak pixel [7, 8] versus target pixel [7, 8]. Image-model fractional residual 0.861 is not a calibrated localization error. Gaia neighbors capable under the approximate G-band flux budget: Gaia 469818814585955328: 3.0 arcsec, G 16.593, approximate intrinsic eclipse requirement 0.873; Gaia 469818810292668416: 4.9 arcsec, G 16.391, approximate intrinsic eclipse requirement 0.728; Gaia 469820223341588480: 32.6 arcsec, G 16.069, approximate intrinsic eclipse requirement 0.545; Gaia 469820223341588864: 40.8 arcsec, G 15.394, approximate intrinsic eclipse requirement 0.300; Gaia 469818745872854528: 49.1 arcsec, G 12.762, approximate intrinsic eclipse requirement 0.041; Gaia 469819020750741888: 54.5 arcsec, G 13.609, approximate intrinsic eclipse requirement 0.071; Gaia 469820223341582208: 59.6 arcsec, G 16.350, approximate intrinsic eclipse requirement 0.702. The neighbor intrinsic eclipse requirement is not directly comparable to blended pixel fractional loss.
4. **Alternative reduction: supports recurring loss with unresolved host.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 13.67/12.75/8.71 ppt over 3 stacked events, compared with median selected QLP raw fit depth 15.82 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution or mixed eclipse kinds limit depth equality. and aperture dilution or mixed eclipse kinds limit depth equality.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 469818814592320896 has P = 11.2828845399 d and e = 0.14903. The closest edge-on conjunction offset at the measured epoch is -0.57231 d (-0.05072 phase), with 0.55955 d linearly propagated full-SB1-covariance timing error. A rough central duration is 8.87 h versus observed median 3.56 h; TIC radius and minimum-mass companion are approximations, and impact parameter is not fitted.

**Deciding interpretation and limitation:** Three raw eclipses repeat in S59/86, but two capable Gaia neighbors at 3.0 and 4.9 arcsec share the central TESS pixel with the target. The S59 deficit cannot resolve the host.

**Next check:** Resolved eclipse photometry of the close Gaia sources.

Catalogue novelty is in the central seven-group ../../shared-catalogues/coverage-matrix.csv receipt; physical classification does not assert exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Orbital timing status |
|---|---:|---:|---:|---:|---|
| 59 | 97 | 2922.0674903 | 0.001435 | 15.82 | used |
| 59 | 98 | 2933.3445278 | 0.001500 | 16.19 | used |
| 86 | 161 | 3644.0113934 | 0.002044 | 13.33 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s59.json, historical/diff_s59.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). All evidence and source files are in ../SHA256SUMS.json.


Stable review key: R508. Public evidence files: [diff_s59.json](../../evidence/87159646/historical/diff_s59.json), [diff_s59.png](../../evidence/87159646/historical/diff_s59.png), [gaia.json](../../evidence/87159646/historical/gaia.json), [measurements.json](../../evidence/87159646/measurements.json), [raw-events.png](../../evidence/87159646/raw-events.png), [raw-windows.csv](../../evidence/87159646/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch10/INDEX.md). 
