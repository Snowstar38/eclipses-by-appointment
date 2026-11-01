# TIC 61260847: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are recorded separately. The historical screening label is not an admission verdict.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 15 timing-usable measured eclipses in representative sectors [43, 70, 71]. The raw plot and numeric windows retain the light-curve evidence. Local trapezoids have free centers, depths, durations and baselines. Historical predicted times guided windows only. Flagged or uncovered intervals are not null detections.
2. **Measured timing and alias: pass.** 15 actual midpoints yield P = 3.7642439801 ± 0.0000080184 d and reference epoch BTJD 2477.9961067 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind cycle counts, within-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive blind all-period search.
3. **Source attribution: favors target at TESS image resolution.** Historical S43 cutout puts the deficit 2.54 arcsec from the target coordinate; peak [7, 8] versus target pixel [7, 7]. Image-model fractional residual 0.322; this is not a calibrated localization error. Capable Gaia neighbors: none within 60 arcsec under the approximate G-band flux budget. The intrinsic requirement uses an approximate flux budget and is not compared directly with a blended pixel fractional loss.
4. **Alternative reduction: pass.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 155.96/155.42/145.63 ppt in 5 stacked events; median selected QLP raw fit depth 160.34 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and any mixed event kinds limit depth comparisons.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 3410845980312983680 has orbital P = 3.7643570975 d, e = 0.01600; closest edge-on conjunction offset at the measured epoch is -0.07963 d (-0.02115 phase), with 0.21627 d linearly propagated full-SB1-covariance timing error. The rough central duration is 5.75 h versus observed median 4.35 h; assumed TIC radius and minimum-mass companion are not a full fit. Geometry supports physical plausibility without an arbitrary sigma veto.

**Deciding interpretation and limitation:** Fifteen deep raw eclipses in S43/70/71 establish recurrence and a measured period. The cutout core favors the target with no capable Gaia neighbor; local image residuals limit precise centroid claims.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is in ../../shared-catalogues/coverage-matrix.csv. A cone-source entry alone does not establish an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 43 | 0 | 2477.9961490 | 0.003473 | 160.95 | used |
| 43 | 1 | 2481.7601478 | 0.003473 | 159.16 | used |
| 43 | 3 | 2489.2890959 | 0.003473 | 160.84 | used |
| 43 | 4 | 2493.0530729 | 0.003473 | 159.18 | used |
| 43 | 5 | 2496.8173050 | 0.003473 | 160.37 | used |
| 70 | 195 | 3212.0234621 | 0.001158 | 161.16 | used |
| 70 | 196 | 3215.7881033 | 0.001158 | 160.34 | used |
| 70 | 198 | 3223.3164704 | 0.001158 | 161.07 | used |
| 70 | 199 | 3227.0805055 | 0.001158 | 160.97 | used |
| 70 | 200 | 3230.8449305 | 0.001158 | 161.27 | used |
| 71 | 202 | 3238.3734637 | 0.001157 | 156.10 | used |
| 71 | 203 | 3242.1373914 | 0.001157 | 156.13 | used |
| 71 | 204 | 3245.9020319 | 0.001157 | 155.95 | used |
| 71 | 205 | 3249.6660910 | 0.001157 | 156.03 | used |
| 71 | 207 | 3257.1947663 | 0.001157 | 156.21 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s43.json, historical/diff_s43.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). Source code and all retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R492. Public evidence files: [diff_s43.json](../../evidence/61260847/historical/diff_s43.json), [diff_s43.png](../../evidence/61260847/historical/diff_s43.png), [gaia.json](../../evidence/61260847/historical/gaia.json), [measurements.json](../../evidence/61260847/measurements.json), [raw-events.png](../../evidence/61260847/raw-events.png), [raw-windows.csv](../../evidence/61260847/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch09/INDEX.md). 
