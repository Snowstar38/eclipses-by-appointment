# TIC 131731452: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are recorded separately. The historical screening label is not an admission verdict.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 5 timing-usable measured eclipses in representative sectors [9, 63, 99]. The raw plot and numeric windows retain the light-curve evidence. Local trapezoids have free centers, depths, durations and baselines. Predicted times guided windows only. Flagged or uncovered intervals are not null detections.
2. **Measured timing and alias: pass.** 5 actual midpoints yield P = 13.0337190439 ± 0.0000167190 d and reference epoch BTJD 1554.9336392 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind cycle counts, within-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive blind all-period search.
3. **Source attribution: favors target at TESS image resolution.** Historical sector 89 cutout puts the deficit 3.67 arcsec from the target coordinate; peak [8, 8] versus target pixel [8, 8]. Image-model fractional residual 0.764; this is not a calibrated localization error. Capable Gaia neighbors: Gaia 5406501911631243520: separation 32.41 arcsec, G 12.282, approximate intrinsic eclipse requirement 0.553. The intrinsic requirement uses an approximate flux budget and is not compared directly with a blended pixel fractional loss.
4. **Alternative reduction: pass.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 210.62/164.58/119.31 ppt in 3 stacked events; median selected QLP raw fit depth 269.31 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and any mixed event kinds limit depth comparisons.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 5406501915941740928 has orbital P = 13.0317563802 d, e = 0.15286; closest edge-on conjunction offset at the measured epoch is -0.06192 d (-0.00475 phase), with 0.15776 d linearly propagated full-SB1-covariance timing error. The rough central duration is 7.22 h versus observed median 6.44 h; assumed TIC radius and minimum-mass companion are not a full fit. Geometry supports physical plausibility without an arbitrary sigma veto or proof of which unresolved neighbor eclipses.

**Deciding interpretation and limitation:** Five deep raw eclipses S9/63/99. A capable neighbor 32.4 arcsec away is distinct from the target-centered core; high pixel-model residual and changing aperture dilution limit intrinsic depth interpretation.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is in ../../shared-catalogues/coverage-matrix.csv. A cone-source entry alone does not establish an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 9 | 0 | 1554.9337346 | 0.010417 | 281.02 | used |
| 9 | 1 | 1567.9669072 | 0.010417 | 275.45 | used |
| 63 | 112 | 3014.7102093 | 0.001157 | 265.82 | used |
| 63 | 113 | 3027.7438640 | 0.001157 | 269.31 | used |
| 99 | 193 | 4070.4414090 | 0.001157 | 186.64 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s89.json, historical/diff_s89.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json).  Source code and all retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R417. Public evidence files: [diff_s89.json](../../evidence/131731452/historical/diff_s89.json), [diff_s89.png](../../evidence/131731452/historical/diff_s89.png), [gaia.json](../../evidence/131731452/historical/gaia.json), [measurements.json](../../evidence/131731452/measurements.json), [raw-events.png](../../evidence/131731452/raw-events.png), [raw-windows.csv](../../evidence/131731452/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch01/INDEX.md). 
