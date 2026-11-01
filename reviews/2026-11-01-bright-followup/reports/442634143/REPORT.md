# TIC 442634143: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are recorded separately. The historical screening label is not an admission verdict.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 3 timing-usable measured eclipses in representative sectors [12, 65]. The raw plot and numeric windows retain the light-curve evidence. Local trapezoids have free centers, depths, durations and baselines. Predicted times guided windows only. Flagged or uncovered intervals are not null detections.
2. **Measured timing and alias: pass.** 3 actual midpoints yield P = 14.1800335439 ± 0.0000734560 d and reference epoch BTJD 1633.9533458 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind cycle counts, within-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive blind all-period search.
3. **Source attribution: favors target at TESS image resolution.** Historical sector 12 cutout puts the deficit 4.58 arcsec from the target coordinate; peak [7, 7] versus target pixel [7, 7]. Image-model fractional residual 0.123; this is not a calibrated localization error. Capable Gaia neighbors: None within 60 arcsec under the approximate G-band flux budget. The intrinsic requirement uses an approximate flux budget and is not compared directly with a blended pixel fractional loss.
4. **Alternative reduction: pass.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 78.72/77.08/75.71 ppt in 2 stacked events; median selected QLP raw fit depth 74.53 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and any mixed event kinds limit depth comparisons.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 6040478190203632640 has orbital P = 14.1830337728 d, e = 0.14754; closest edge-on conjunction offset at the measured epoch is -0.20084 d (-0.01416 phase), with 0.38892 d linearly propagated full-SB1-covariance timing error. The rough central duration is 6.68 h versus observed median 8.78 h; assumed TIC radius and minimum-mass companion are not a full fit. Geometry supports physical plausibility without an arbitrary sigma veto or proof of which unresolved neighbor eclipses.

**Deciding interpretation and limitation:** Three deep raw eclipses in S12/65. Observed duration exceeds a rough central radius/minimum-mass estimate; the estimate is model dependent and does not resolve detailed binary geometry.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is in ../../shared-catalogues/coverage-matrix.csv. A cone-source entry alone does not establish an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 12 | 0 | 1633.9533229 | 0.010416 | 73.58 | used |
| 12 | 1 | 1648.1334025 | 0.010416 | 74.53 | used |
| 65 | 102 | 3080.3167673 | 0.001157 | 77.74 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s12.json, historical/diff_s12.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json).  Source code and all retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R411. Public evidence files: [diff_s12.json](../../evidence/442634143/historical/diff_s12.json), [diff_s12.png](../../evidence/442634143/historical/diff_s12.png), [gaia.json](../../evidence/442634143/historical/gaia.json), [measurements.json](../../evidence/442634143/measurements.json), [raw-events.png](../../evidence/442634143/raw-events.png), [raw-windows.csv](../../evidence/442634143/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch01/INDEX.md). 
