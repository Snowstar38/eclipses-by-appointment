# TIC 370829832: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 4 fitted representative eclipses in sectors [37, 90]; 4 enter the reported timing fit. Local trapezoids have free centers, depths, durations and baselines. Predicted times guided windows only; flagged or uncovered intervals are not clean nulls. See raw-events.png, raw-windows.csv and measurements.json.
2. **Measured timing and aliases: pass.** 4 same-kind actual midpoints yield P = 9.2465432321 ± 0.0000330778 d and reference epoch BTJD 2317.6240607 (Selected repeating eclipse; primary by convention; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; representative parity shows no persistent unequal alternation. Same-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Half/double alias assessment is bounded by representative raw morphology, not an exhaustive blind period search.
3. **Source attribution: favors target at TESS pixel resolution.** Historical sector 63 cutout places the deficit centroid 1.79 arcsec from the target; peak pixel [7, 14] versus target pixel [7, 8]. Image-model fractional residual 0.949 is not a calibrated localization error. Gaia neighbors capable under the approximate G-band flux budget: Gaia 5249020789631628928: 37.8 arcsec, G 16.212, approximate intrinsic eclipse requirement 0.537; Gaia 5249020720912155520: 38.7 arcsec, G 14.177, approximate intrinsic eclipse requirement 0.094; Gaia 5249020858351113472: 44.5 arcsec, G 14.172, approximate intrinsic eclipse requirement 0.094; Gaia 5249020927070584832: 46.6 arcsec, G 16.304, approximate intrinsic eclipse requirement 0.583; Gaia 5249020858351116032: 49.0 arcsec, G 14.187, approximate intrinsic eclipse requirement 0.095; Gaia 5249020927070586112: 49.2 arcsec, G 15.096, approximate intrinsic eclipse requirement 0.201; Gaia 5249020789631629440: 52.4 arcsec, G 14.216, approximate intrinsic eclipse requirement 0.097; Gaia 5249020927070587392: 53.9 arcsec, G 16.631, approximate intrinsic eclipse requirement 0.783; Gaia 5249020789631627776: 58.8 arcsec, G 16.523, approximate intrinsic eclipse requirement 0.710. The neighbor intrinsic eclipse requirement is not directly comparable to blended pixel fractional loss.
4. **Alternative reduction: pass.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 13.79/12.50/9.08 ppt over 3 stacked events, compared with median selected QLP raw fit depth 14.77 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution or mixed eclipse kinds limit depth equality. and aperture dilution or mixed eclipse kinds limit depth equality.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 5249020892710847488 has P = 9.2458347321 d and e = 0.18138. The closest edge-on conjunction offset at the measured epoch is -0.03335 d (-0.00361 phase), with 0.38441 d linearly propagated full-SB1-covariance timing error. A rough central duration is 6.19 h versus observed median 2.69 h; TIC radius and minimum-mass companion are approximations, and impact parameter is not fitted.

**Deciding interpretation and limitation:** The S63 difference image has a remote single-pixel maximum at [7,14] coincident with a bright field source; its origin is uncertain. The multi-pixel eclipse deficit and centroid lie near the target [7,8]. The remote maximum and large image-model residual limit precision localization.

**Next check:** Optional higher-resolution eclipse imaging and binary characterization.

Catalogue novelty is in the central seven-group ../../shared-catalogues/coverage-matrix.csv receipt; physical classification does not assert exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Orbital timing status |
|---|---:|---:|---:|---:|---|
| 37 | 83 | 2317.6218651 | 0.003472 | 15.04 | used |
| 37 | 84 | 2326.8729892 | 0.003472 | 16.52 | used |
| 90 | 238 | 3750.8350612 | 0.001678 | 14.12 | used |
| 90 | 240 | 3769.3338324 | 0.001489 | 14.50 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s63.json, historical/diff_s63.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). All evidence and source files are in ../SHA256SUMS.json.


Stable review key: R501. Public evidence files: [diff_s63.json](../../evidence/370829832/historical/diff_s63.json), [diff_s63.png](../../evidence/370829832/historical/diff_s63.png), [gaia.json](../../evidence/370829832/historical/gaia.json), [measurements.json](../../evidence/370829832/measurements.json), [raw-events.png](../../evidence/370829832/raw-events.png), [raw-windows.csv](../../evidence/370829832/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch10/INDEX.md). 
