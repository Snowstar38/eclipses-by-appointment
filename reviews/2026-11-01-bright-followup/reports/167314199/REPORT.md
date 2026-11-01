# TIC 167314199: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are recorded separately. The historical screening label is not an admission verdict.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 8 timing-usable measured eclipses in representative sectors [15, 75, 83]. The raw plot and numeric windows retain the light-curve evidence. Local trapezoids have free centers, depths, durations and baselines. Historical predicted times guided windows only. Flagged or uncovered intervals are not null detections.
2. **Measured timing and alias: pass.** 8 actual midpoints yield P = 9.4293015589 ± 0.0000286278 d and reference epoch BTJD 1711.9085480 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind cycle counts, within-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive blind all-period search.
3. **Source attribution: favors target at TESS image resolution.** Historical S56 cutout puts the deficit 5.06 arcsec from the target coordinate; peak [7, 8] versus target pixel [7, 8]. Image-model fractional residual 0.880; this is not a calibrated localization error. Capable Gaia neighbors: Gaia 1964832780702837248: 35.7 arcsec, G 13.368, approximate intrinsic eclipse requirement 0.909. The intrinsic requirement uses an approximate flux budget and is not compared directly with a blended pixel fractional loss.
4. **Alternative reduction: pass.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 259.06/230.88/191.58 ppt in 3 stacked events; median selected QLP raw fit depth 272.15 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and any mixed event kinds limit depth comparisons.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 1964832776395084288 has orbital P = 9.4286060079 d, e = 0.02722; closest edge-on conjunction offset at the measured epoch is 0.14149 d (0.01501 phase), with 0.14582 d linearly propagated full-SB1-covariance timing error. The rough central duration is 7.89 h versus observed median 5.97 h; assumed TIC radius and minimum-mass companion are not a full fit. Geometry supports physical plausibility without an arbitrary sigma veto.

**Deciding interpretation and limitation:** Eight deep raw eclipses in S15/75/83 recur on the Gaia timescale. A capable 35.7-arcsec neighbor requires an extreme intrinsic eclipse and is distinct from the target-favored core; the image-model residual is high.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is in ../../shared-catalogues/coverage-matrix.csv. A cone-source entry alone does not establish an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 15 | 0 | 1711.9051662 | 0.010417 | 278.47 | used |
| 15 | 2 | 1730.7647966 | 0.010417 | 279.91 | used |
| 75 | 173 | 3343.1779004 | 0.001157 | 271.76 | used |
| 75 | 174 | 3352.6073018 | 0.001157 | 272.54 | used |
| 75 | 175 | 3362.0364531 | 0.001157 | 273.03 | used |
| 83 | 196 | 3560.0515342 | 0.001157 | 259.26 | used |
| 83 | 197 | 3569.4807627 | 0.001157 | 256.44 | used |
| 83 | 198 | 3578.9100415 | 0.001157 | 258.54 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s56.json, historical/diff_s56.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). Source code and all retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R496. Public evidence files: [diff_s56.json](../../evidence/167314199/historical/diff_s56.json), [diff_s56.png](../../evidence/167314199/historical/diff_s56.png), [gaia.json](../../evidence/167314199/historical/gaia.json), [measurements.json](../../evidence/167314199/measurements.json), [raw-events.png](../../evidence/167314199/raw-events.png), [raw-windows.csv](../../evidence/167314199/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch09/INDEX.md). 
