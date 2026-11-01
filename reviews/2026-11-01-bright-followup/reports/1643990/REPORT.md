# TIC 1643990: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are recorded separately. The historical screening label is not an admission verdict.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 6 timing-usable measured eclipses in representative sectors [8, 61, 99]. The raw plot and numeric windows retain the light-curve evidence. Local trapezoids have free centers, depths, durations and baselines. Historical predicted times guided windows only. Flagged or uncovered intervals are not null detections.
2. **Measured timing and alias: pass.** 6 actual midpoints yield P = 6.2251817590 ± 0.0000063922 d and reference epoch BTJD 1519.5838843 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind cycle counts, within-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive blind all-period search.
3. **Source attribution: favors target at TESS image resolution.** Historical S8 cutout puts the deficit 2.55 arcsec from the target coordinate; peak [7, 7] versus target pixel [7, 7]. Image-model fractional residual 0.046; this is not a calibrated localization error. Capable Gaia neighbors: none within 60 arcsec under the approximate G-band flux budget. The intrinsic requirement uses an approximate flux budget and is not compared directly with a blended pixel fractional loss.
4. **Alternative reduction: pass.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 267.11/268.43/270.89 ppt in 3 stacked events; median selected QLP raw fit depth 258.75 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and any mixed event kinds limit depth comparisons.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 5762102560669048704 has orbital P = 6.2252118769 d, e = 0.11362; closest edge-on conjunction offset at the measured epoch is -0.00339 d (-0.00055 phase), with 0.07702 d linearly propagated full-SB1-covariance timing error. The rough central duration is 4.43 h versus observed median 3.86 h; assumed TIC radius and minimum-mass companion are not a full fit. Geometry supports physical plausibility without an arbitrary sigma veto.

**Deciding interpretation and limitation:** Six deep raw eclipses in S8/61/99 give a long timing baseline. The cutout deficit lies on the target with low model residual and no capable Gaia neighbor under the brightness screen.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is in ../../shared-catalogues/coverage-matrix.csv. A cone-source entry alone does not establish an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 8 | 0 | 1519.5838814 | 0.010417 | 268.15 | used |
| 8 | 3 | 1538.2572047 | 0.010417 | 249.36 | used |
| 61 | 233 | 2970.0512579 | 0.001157 | 272.58 | used |
| 61 | 235 | 2982.5016384 | 0.001157 | 271.53 | used |
| 99 | 407 | 4053.2328119 | 0.001157 | 231.58 | used |
| 99 | 409 | 4065.6832351 | 0.001157 | 232.67 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s08.json, historical/diff_s08.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). Source code and all retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R497. Public evidence files: [diff_s08.json](../../evidence/1643990/historical/diff_s08.json), [diff_s08.png](../../evidence/1643990/historical/diff_s08.png), [gaia.json](../../evidence/1643990/historical/gaia.json), [measurements.json](../../evidence/1643990/measurements.json), [raw-events.png](../../evidence/1643990/raw-events.png), [raw-windows.csv](../../evidence/1643990/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch09/INDEX.md). 
