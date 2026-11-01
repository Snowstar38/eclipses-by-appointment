# TIC 72733549: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are recorded separately. The historical screening label is not an admission verdict.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 3 timing-usable measured eclipses in representative sectors [52, 79]. The raw plot and numeric windows retain the light-curve evidence. Local trapezoids have free centers, depths, durations and baselines. Predicted times guided windows only. Flagged or uncovered intervals are not null detections.
2. **Measured timing and alias: pass.** 3 actual midpoints yield P = 10.0757543600 ± 0.0000962802 d and reference epoch BTJD 2728.5178240 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind cycle counts, within-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive blind all-period search.
3. **Source attribution: favors target at TESS image resolution.** Historical sector 79 cutout puts the deficit 2.70 arcsec from the target coordinate; peak [7, 7] versus target pixel [7, 7]. Image-model fractional residual 0.430; this is not a calibrated localization error. Capable Gaia neighbors: Gaia 1351135967600649984: separation 48.12 arcsec, G 12.966, approximate intrinsic eclipse requirement 0.312. The intrinsic requirement uses an approximate flux budget and is not compared directly with a blended pixel fractional loss.
4. **Alternative reduction: pass.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 90.72/83.62/69.70 ppt in 2 stacked events; median selected QLP raw fit depth 96.51 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and any mixed event kinds limit depth comparisons.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 1351133729921222400 has orbital P = 10.0743628417 d, e = 0.01363; closest edge-on conjunction offset at the measured epoch is 0.28926 d (0.02871 phase), with 0.46418 d linearly propagated full-SB1-covariance timing error. The rough central duration is 7.25 h versus observed median 5.01 h; assumed TIC radius and minimum-mass companion are not a full fit. Geometry supports physical plausibility without an arbitrary sigma veto or proof of which unresolved neighbor eclipses.

**Deciding interpretation and limitation:** Three deep raw eclipses S52/79, including successive S79 cycles. A capable neighbor 48.1 arcsec away is distinct from the target-centered deficit.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is in ../../shared-catalogues/coverage-matrix.csv. A cone-source entry alone does not establish an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 52 | 73 | 2728.5178238 | 0.006944 | 96.51 | used |
| 79 | 145 | 3453.9721385 | 0.001157 | 96.22 | used |
| 79 | 146 | 3464.0478918 | 0.001157 | 97.43 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s79.json, historical/diff_s79.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json).  Source code and all retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R414. Public evidence files: [diff_s79.json](../../evidence/72733549/historical/diff_s79.json), [diff_s79.png](../../evidence/72733549/historical/diff_s79.png), [gaia.json](../../evidence/72733549/historical/gaia.json), [measurements.json](../../evidence/72733549/measurements.json), [raw-events.png](../../evidence/72733549/raw-events.png), [raw-windows.csv](../../evidence/72733549/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch01/INDEX.md). 
