# TIC 51564054: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 20 fitted representative eclipses in sectors [54, 55, 81]; 20 enter the reported timing fit. Local trapezoids have free centers, depths, durations and baselines. Predicted times guided windows only; flagged or uncovered intervals are not clean nulls. See raw-events.png, raw-windows.csv and measurements.json.
2. **Measured timing and aliases: pass.** 20 same-kind actual midpoints yield P = 3.6820558498 ± 0.0000053792 d and reference epoch BTJD 2770.7791920 (Selected repeating eclipse; primary by convention; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; representative parity shows no persistent unequal alternation. Same-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Half/double alias assessment is bounded by representative raw morphology, not an exhaustive blind period search.
3. **Source attribution: favors target at TESS pixel resolution.** Historical sector 55 cutout places the deficit centroid 6.58 arcsec from the target; peak pixel [8, 8] versus target pixel [8, 8]. Image-model fractional residual 0.567 is not a calibrated localization error. Gaia neighbors capable under the approximate G-band flux budget: None within 60 arcsec under the approximate G-band flux budget. The neighbor intrinsic eclipse requirement is not directly comparable to blended pixel fractional loss.
4. **Alternative reduction: pass.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 81.07/80.04/77.97 ppt over 7 stacked events, compared with median selected QLP raw fit depth 83.28 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution or mixed eclipse kinds limit depth equality. and aperture dilution or mixed eclipse kinds limit depth equality.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 1805030134371636352 has P = 3.6821627017 d and e = 0.03959. The closest edge-on conjunction offset at the measured epoch is -0.09878 d (-0.02683 phase), with 0.16553 d linearly propagated full-SB1-covariance timing error. A rough central duration is 5.75 h versus observed median 3.39 h; TIC radius and minimum-mass companion are approximations, and impact parameter is not fitted.

**Deciding interpretation and limitation:** Twenty raw events across S54/55/81 recur at the measured period; the difference core lies on the target and no Gaia neighbor passes the approximate brightness screen.

**Next check:** Optional precision binary characterization.

Catalogue novelty is in the central seven-group ../../shared-catalogues/coverage-matrix.csv receipt; physical classification does not assert exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Orbital timing status |
|---|---:|---:|---:|---:|---|
| 54 | 0 | 2770.7802194 | 0.003472 | 83.73 | used |
| 54 | 1 | 2774.4612189 | 0.003472 | 85.99 | used |
| 54 | 2 | 2778.1427547 | 0.003472 | 81.18 | used |
| 54 | 3 | 2781.8245378 | 0.003472 | 84.16 | used |
| 54 | 5 | 2789.1901975 | 0.003472 | 86.15 | used |
| 54 | 6 | 2792.8708408 | 0.003472 | 84.37 | used |
| 55 | 8 | 2800.2352509 | 0.003472 | 85.90 | used |
| 55 | 9 | 2803.9173093 | 0.003472 | 82.30 | used |
| 55 | 10 | 2807.5993533 | 0.003472 | 77.57 | used |
| 55 | 11 | 2811.2822047 | 0.003472 | 79.44 | used |
| 55 | 12 | 2814.9647274 | 0.003472 | 80.90 | used |
| 55 | 13 | 2818.6460093 | 0.003472 | 83.01 | used |
| 55 | 14 | 2822.3280330 | 0.003472 | 82.75 | used |
| 81 | 200 | 3507.1912335 | 0.001157 | 81.01 | used |
| 81 | 201 | 3510.8728408 | 0.001157 | 83.73 | used |
| 81 | 203 | 3518.2358094 | 0.001157 | 83.78 | used |
| 81 | 204 | 3521.9174461 | 0.001157 | 83.15 | used |
| 81 | 205 | 3525.6004124 | 0.001157 | 81.48 | used |
| 81 | 206 | 3529.2831125 | 0.001157 | 83.40 | used |
| 81 | 207 | 3532.9651413 | 0.001157 | 87.14 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s55.json, historical/diff_s55.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). All evidence and source files are in ../SHA256SUMS.json.


Stable review key: R502. Public evidence files: [diff_s55.json](../../evidence/51564054/historical/diff_s55.json), [diff_s55.png](../../evidence/51564054/historical/diff_s55.png), [gaia.json](../../evidence/51564054/historical/gaia.json), [measurements.json](../../evidence/51564054/measurements.json), [raw-events.png](../../evidence/51564054/raw-events.png), [raw-windows.csv](../../evidence/51564054/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch10/INDEX.md). 
