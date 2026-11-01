# TIC 63013423: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are recorded separately. The historical screening label is not an admission verdict.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 12 timing-usable measured eclipses in representative sectors [44, 46, 72]. The raw plot and numeric windows retain the light-curve evidence. Local trapezoids have free centers, depths, durations and baselines. Historical predicted times guided windows only. Flagged or uncovered intervals are not null detections.
2. **Measured timing and alias: pass.** 12 actual midpoints yield P = 5.5779862426 ± 0.0000103302 d and reference epoch BTJD 2505.4546770 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind cycle counts, within-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive blind all-period search.
3. **Source attribution: favors target at TESS image resolution.** Historical S44 cutout puts the deficit 2.57 arcsec from the target coordinate; peak [7, 7] versus target pixel [7, 7]. Image-model fractional residual 0.569; this is not a calibrated localization error. Capable Gaia neighbors: Gaia 675068326633876992: 49.1 arcsec, G 14.755, approximate intrinsic eclipse requirement 0.904. The intrinsic requirement uses an approximate flux budget and is not compared directly with a blended pixel fractional loss.
4. **Alternative reduction: pass.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 82.60/81.69/70.51 ppt in 4 stacked events; median selected QLP raw fit depth 87.58 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and any mixed event kinds limit depth comparisons.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 675068532792307456 has orbital P = 5.5777973688 d, e = 0.04208; closest edge-on conjunction offset at the measured epoch is 0.13397 d (0.02402 phase), with 0.20174 d linearly propagated full-SB1-covariance timing error. The rough central duration is 5.22 h versus observed median 3.72 h; assumed TIC radius and minimum-mass companion are not a full fit. Geometry supports physical plausibility without an arbitrary sigma veto.

**Deciding interpretation and limitation:** Twelve raw eclipses in S44/46/72 show stable recurrence. The capable neighbor 49.1 arcsec away is distinct from the target-centered deficit; aperture and model residuals limit exact intrinsic depth.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is in ../../shared-catalogues/coverage-matrix.csv. A cone-source entry alone does not establish an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 44 | 0 | 2505.4547268 | 0.003473 | 88.53 | used |
| 44 | 1 | 2511.0325313 | 0.003473 | 89.00 | used |
| 44 | 2 | 2516.6111421 | 0.003473 | 88.27 | used |
| 44 | 3 | 2522.1890296 | 0.003473 | 86.32 | used |
| 46 | 9 | 2555.6563082 | 0.003472 | 89.73 | used |
| 46 | 10 | 2561.2344079 | 0.003472 | 88.32 | used |
| 46 | 12 | 2572.3902221 | 0.003472 | 89.96 | used |
| 46 | 13 | 2577.9681930 | 0.003472 | 86.86 | used |
| 72 | 136 | 3264.0613877 | 0.001157 | 85.57 | used |
| 72 | 137 | 3269.6388279 | 0.001157 | 85.71 | used |
| 72 | 138 | 3275.2165537 | 0.001157 | 86.88 | used |
| 72 | 139 | 3280.7943908 | 0.001157 | 82.67 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s44.json, historical/diff_s44.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). Source code and all retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R495. Public evidence files: [diff_s44.json](../../evidence/63013423/historical/diff_s44.json), [diff_s44.png](../../evidence/63013423/historical/diff_s44.png), [gaia.json](../../evidence/63013423/historical/gaia.json), [measurements.json](../../evidence/63013423/measurements.json), [raw-events.png](../../evidence/63013423/raw-events.png), [raw-windows.csv](../../evidence/63013423/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch09/INDEX.md). 
