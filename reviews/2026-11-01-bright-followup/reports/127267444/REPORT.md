# TIC 127267444: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are recorded separately. The historical screening label is not an admission verdict.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 3 timing-usable measured eclipses in representative sectors [92]. The raw plot and numeric windows retain the light-curve evidence. Local trapezoids have free centers, depths, durations and baselines. Historical predicted times guided windows only. Flagged or uncovered intervals are not null detections.
2. **Measured timing and alias: pass.** 3 actual midpoints yield P = 8.2997438847 ± 0.0008290274 d and reference epoch BTJD 3803.8082712 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind cycle counts, within-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive blind all-period search.
3. **Source attribution: favors target at TESS image resolution.** Historical S92 cutout puts the deficit 1.73 arcsec from the target coordinate; peak [8, 8] versus target pixel [8, 8]. Image-model fractional residual 0.388; this is not a calibrated localization error. Capable Gaia neighbors: Gaia 6771875970694979712: 27.8 arcsec, G 12.830, approximate intrinsic eclipse requirement 0.066; Gaia 6771878959992220544: 49.5 arcsec, G 14.954, approximate intrinsic eclipse requirement 0.322. The intrinsic requirement uses an approximate flux budget and is not compared directly with a blended pixel fractional loss.
4. **Alternative reduction: pass.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 22.88/17.92/15.43 ppt in 4 stacked events; median selected QLP raw fit depth 25.90 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and any mixed event kinds limit depth comparisons.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 6771876000757078144 has orbital P = 8.2991638272 d, e = 0.08323; closest edge-on conjunction offset at the measured epoch is 0.15077 d (0.01817 phase), with 0.61378 d linearly propagated full-SB1-covariance timing error. The rough central duration is 7.80 h versus observed median 3.33 h; assumed TIC radius and minimum-mass companion are not a full fit. Geometry supports physical plausibility without an arbitrary sigma veto.

**Deciding interpretation and limitation:** Three consecutive raw eclipses in S92 give a measured 8.299744-day period, close to the Gaia 8.299164-day orbit; the historical 8.29212-day screening estimate was inaccurate. Two capable neighbors at 27.8 and 49.5 arcsec are spatially distinct from the target-centered deficit. The pixel-model residual is substantial.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is in ../../shared-catalogues/coverage-matrix.csv. A cone-source entry alone does not establish an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 92 | 0 | 3803.8078822 | 0.001187 | 26.60 | used |
| 92 | 1 | 3812.1087545 | 0.001157 | 25.90 | used |
| 92 | 2 | 3820.4073893 | 0.001157 | 25.61 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s92.json, historical/diff_s92.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). Source code and all retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R491. Public evidence files: [diff_s92.json](../../evidence/127267444/historical/diff_s92.json), [diff_s92.png](../../evidence/127267444/historical/diff_s92.png), [gaia.json](../../evidence/127267444/historical/gaia.json), [measurements.json](../../evidence/127267444/measurements.json), [raw-events.png](../../evidence/127267444/raw-events.png), [raw-windows.csv](../../evidence/127267444/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch09/INDEX.md). 
