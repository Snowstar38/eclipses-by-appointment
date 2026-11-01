# TIC 401917014: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are recorded separately. The historical screening label is not an admission verdict.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 8 timing-usable measured eclipses in representative sectors [12, 93, 102]. The raw plot and numeric windows retain the light-curve evidence. Local trapezoids have free centers, depths, durations and baselines. Predicted times guided windows only. Flagged or uncovered intervals are not null detections.
2. **Measured timing and alias: pass.** 8 actual midpoints yield P = 7.8018659062 ± 0.0000181348 d and reference epoch BTJD 1630.8460077 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind cycle counts, within-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive blind all-period search.
3. **Source attribution: favors target at TESS image resolution.** Historical sector 93 cutout puts the deficit 4.91 arcsec from the target coordinate; peak [7, 7] versus target pixel [7, 7]. Image-model fractional residual 0.577; this is not a calibrated localization error. Capable Gaia neighbors: Gaia 5796293562665379456: separation 46.11 arcsec, G 13.487, approximate intrinsic eclipse requirement 0.923. The intrinsic requirement uses an approximate flux budget and is not compared directly with a blended pixel fractional loss.
4. **Alternative reduction: pass.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 196.20/192.24/161.00 ppt in 4 stacked events; median selected QLP raw fit depth 191.97 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and any mixed event kinds limit depth comparisons.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 5796293459586158976 has orbital P = 7.8019703401 d, e = 0.02120; closest edge-on conjunction offset at the measured epoch is -0.02604 d (-0.00334 phase), with 0.13110 d linearly propagated full-SB1-covariance timing error. The rough central duration is 5.66 h versus observed median 4.41 h; assumed TIC radius and minimum-mass companion are not a full fit. Geometry supports physical plausibility without an arbitrary sigma veto or proof of which unresolved neighbor eclipses.

**Deciding interpretation and limitation:** Eight deep raw eclipses across S12/93/102; capable G-band neighbor 46.1 arcsec away requires an extreme intrinsic loss, while the deficit core is target-centered. Pixel residual limits subpixel claims.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is in ../../shared-catalogues/coverage-matrix.csv. A cone-source entry alone does not establish an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 12 | 0 | 1630.8377438 | 0.010417 | 177.06 | used |
| 12 | 2 | 1646.4416770 | 0.010417 | 178.42 | used |
| 93 | 282 | 3830.9725084 | 0.001157 | 202.74 | used |
| 93 | 283 | 3838.7746987 | 0.001157 | 205.41 | used |
| 93 | 284 | 3846.5763723 | 0.001157 | 203.50 | used |
| 93 | 285 | 3854.3780807 | 0.001157 | 204.23 | used |
| 102 | 321 | 4135.2443979 | 0.001157 | 180.80 | used |
| 102 | 322 | 4143.0459048 | 0.001157 | 181.20 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s93.json, historical/diff_s93.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json).  Source code and all retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R410. Public evidence files: [diff_s93.json](../../evidence/401917014/historical/diff_s93.json), [diff_s93.png](../../evidence/401917014/historical/diff_s93.png), [gaia.json](../../evidence/401917014/historical/gaia.json), [measurements.json](../../evidence/401917014/measurements.json), [raw-events.png](../../evidence/401917014/raw-events.png), [raw-windows.csv](../../evidence/401917014/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch01/INDEX.md). 
