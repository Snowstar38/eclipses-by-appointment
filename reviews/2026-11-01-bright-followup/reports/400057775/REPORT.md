# TIC 400057775: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are recorded separately. The historical screening label is not an admission verdict.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 10 timing-usable measured eclipses in representative sectors [19, 60, 86]. The raw plot and numeric windows retain the light-curve evidence. Local trapezoids have free centers, depths, durations and baselines. Predicted times guided windows only. Flagged or uncovered intervals are not null detections.
2. **Measured timing and alias: pass.** 10 actual midpoints yield P = 4.8719600113 ± 0.0000070752 d and reference epoch BTJD 1820.7274949 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind cycle counts, within-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive blind all-period search.
3. **Source attribution: favors target at TESS image resolution.** Historical sector 59 cutout puts the deficit 1.73 arcsec from the target coordinate; peak [7, 7] versus target pixel [7, 7]. Image-model fractional residual 0.822; this is not a calibrated localization error. Capable Gaia neighbors: Gaia 480689479890567936: separation 29.38 arcsec, G 15.294, approximate intrinsic eclipse requirement 0.466. The intrinsic requirement uses an approximate flux budget and is not compared directly with a blended pixel fractional loss.
4. **Alternative reduction: pass.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 22.99/22.01/20.61 ppt in 4 stacked events; median selected QLP raw fit depth 21.93 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and any mixed event kinds limit depth comparisons.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 480689509953048960 has orbital P = 4.8719149116 d, e = 0.08656; closest edge-on conjunction offset at the measured epoch is -0.01917 d (-0.00393 phase), with 0.12594 d linearly propagated full-SB1-covariance timing error. The rough central duration is 8.83 h versus observed median 7.09 h; assumed TIC radius and minimum-mass companion are not a full fit. Geometry supports physical plausibility without an arbitrary sigma veto or proof of which unresolved neighbor eclipses.

**Deciding interpretation and limitation:** Ten repeated raw eclipses S19/60/86. A capable neighbor 29.4 arcsec away is distinct from the target-centered deficit; high image-model residual limits precision.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is in ../../shared-catalogues/coverage-matrix.csv. A cone-source entry alone does not establish an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 19 | 0 | 1820.7240571 | 0.010417 | 22.97 | used |
| 19 | 1 | 1825.5962845 | 0.010417 | 23.40 | used |
| 19 | 3 | 1835.3436536 | 0.010417 | 23.15 | used |
| 19 | 4 | 1840.2123729 | 0.010417 | 21.82 | used |
| 60 | 230 | 2941.2790493 | 0.001157 | 21.44 | used |
| 60 | 231 | 2946.1507725 | 0.001157 | 21.62 | used |
| 60 | 233 | 2955.8940093 | 0.001157 | 22.42 | used |
| 60 | 234 | 2960.7653054 | 0.001157 | 22.05 | used |
| 86 | 375 | 3647.7126339 | 0.001157 | 21.72 | used |
| 86 | 378 | 3662.3278567 | 0.001562 | 21.28 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s59.json, historical/diff_s59.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json).  Source code and all retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R412. Public evidence files: [diff_s59.json](../../evidence/400057775/historical/diff_s59.json), [diff_s59.png](../../evidence/400057775/historical/diff_s59.png), [gaia.json](../../evidence/400057775/historical/gaia.json), [measurements.json](../../evidence/400057775/measurements.json), [raw-events.png](../../evidence/400057775/raw-events.png), [raw-windows.csv](../../evidence/400057775/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch01/INDEX.md). 
