# TIC 57047535: PROBABLE

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are recorded separately. The historical screening label is not an admission verdict.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 7 timing-usable measured eclipses in representative sectors [34, 35, 61, 62, 88, 89]. The raw plot and numeric windows retain the light-curve evidence. Local trapezoids have free centers, depths, durations and baselines. Historical predicted times guided windows only. Flagged or uncovered intervals are not null detections.
2. **Measured timing and alias: pass.** 7 actual midpoints yield P = 18.6882586301 ± 0.0000306738 d and reference epoch BTJD 2244.7878116 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind cycle counts, within-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive blind all-period search.
3. **Source attribution: unresolved after completed check.** Historical S62 cutout puts the deficit 4.30 arcsec from the target coordinate; peak [7, 8] versus target pixel [7, 8]. Image-model fractional residual 0.674; this is not a calibrated localization error. Capable Gaia neighbors: Gaia 5542738205536780288: 22.6 arcsec, G 12.965, approximate intrinsic eclipse requirement 0.031; Gaia 5542738205536774656: 33.5 arcsec, G 13.358, approximate intrinsic eclipse requirement 0.040; Gaia 5542738278564942848: 41.5 arcsec, G 16.683, approximate intrinsic eclipse requirement 0.647; Gaia 5542738209845466752: 44.2 arcsec, G 16.489, approximate intrinsic eclipse requirement 0.543; Gaia 5542737557010422784: 45.6 arcsec, G 16.553, approximate intrinsic eclipse requirement 0.576; Gaia 5542737453931213312: 46.2 arcsec, G 16.445, approximate intrinsic eclipse requirement 0.522; Gaia 5542738278566462336: 47.7 arcsec, G 15.131, approximate intrinsic eclipse requirement 0.163. The intrinsic requirement uses an approximate flux budget and is not compared directly with a blended pixel fractional loss.
4. **Alternative reduction: pass.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 8.93/7.09/5.36 ppt in 2 stacked events; median selected QLP raw fit depth 10.59 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and any mixed event kinds limit depth comparisons.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 5542738205536698240 has orbital P = 18.6663627993 d, e = 0.42196; closest edge-on conjunction offset at the measured epoch is 0.38371 d (0.02056 phase), with 1.66506 d linearly propagated full-SB1-covariance timing error. The rough central duration is 5.38 h versus observed median 4.22 h; assumed TIC radius and minimum-mass companion are not a full fit. Geometry supports physical plausibility without an arbitrary sigma veto.

**Deciding interpretation and limitation:** Seven raw eclipses across S34/35/61/62/88/89, including consecutive cycles 38/39, 77/78/79 and 116/117, resolve the initially sparse timing. Several capable neighbors make this a crowded field. The deficit core favors the target, but the closest capable Gaia source is only about 1.1 TESS pixels away and the image-model residual is large; attribution remains unresolved.

**Next check:** Resolved eclipse photometry or multi-source PRF localization of the crowded field.

Catalogue novelty: central seven-group result is in ../../shared-catalogues/coverage-matrix.csv. A cone-source entry alone does not establish an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 34 | 38 | 2244.7848021 | 0.003472 | 11.30 | used |
| 35 | 39 | 2263.4744847 | 0.003472 | 12.12 | used |
| 61 | 77 | 2973.6309138 | 0.001361 | 10.89 | used |
| 62 | 78 | 2992.3200617 | 0.001447 | 10.59 | used |
| 62 | 79 | 3011.0043901 | 0.001679 | 10.09 | used |
| 88 | 116 | 3702.4716187 | 0.001641 | 10.01 | used |
| 89 | 117 | 3721.1594292 | 0.001913 | 10.25 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s62.json, historical/diff_s62.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). Source code and all retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R493. Public evidence files: [diff_s62.json](../../evidence/57047535/historical/diff_s62.json), [diff_s62.png](../../evidence/57047535/historical/diff_s62.png), [gaia.json](../../evidence/57047535/historical/gaia.json), [measurements.json](../../evidence/57047535/measurements.json), [raw-events.png](../../evidence/57047535/raw-events.png), [raw-windows.csv](../../evidence/57047535/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch09/INDEX.md). [57047535-availability.json](../../analysis/original/batch09/helper/57047535-availability.json)
