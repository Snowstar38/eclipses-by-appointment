# TIC 17926125: PROBABLE

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are recorded separately. The historical screening label is not an admission verdict.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 6 timing-usable measured eclipses in representative sectors [82, 83]. The raw plot and numeric windows retain the light-curve evidence. Local trapezoids have free centers, depths, durations and baselines. Historical predicted times guided windows only. Flagged or uncovered intervals are not null detections.
2. **Measured timing and alias: pass.** 6 actual midpoints yield P = 9.4207091616 ± 0.0002766705 d and reference epoch BTJD 3534.4228208 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind cycle counts, within-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive blind all-period search.
3. **Source attribution: unresolved after completed check.** Historical S56 cutout puts the deficit 4.79 arcsec from the target coordinate; peak [8, 8] versus target pixel [8, 8]. Image-model fractional residual 0.489; this is not a calibrated localization error. Capable Gaia neighbors: Gaia 1896543625318721280: 15.7 arcsec, G 16.363, approximate intrinsic eclipse requirement 0.866; Gaia 1896543659678461312: 53.7 arcsec, G 16.358, approximate intrinsic eclipse requirement 0.862. The intrinsic requirement uses an approximate flux budget and is not compared directly with a blended pixel fractional loss.
4. **Alternative reduction: pass.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 21.32/20.96/19.82 ppt in 3 stacked events; median selected QLP raw fit depth 20.43 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and any mixed event kinds limit depth comparisons.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 1896543621022178048 has orbital P = 9.4199419993 d, e = 0.02747; closest edge-on conjunction offset at the measured epoch is 0.06074 d (0.00645 phase), with 0.52723 d linearly propagated full-SB1-covariance timing error. The rough central duration is 6.60 h versus observed median 2.74 h; assumed TIC radius and minimum-mass companion are not a full fit. Geometry supports physical plausibility without an arbitrary sigma veto.

**Deciding interpretation and limitation:** Six consecutive raw eclipses in S82/83 support the measured recurrence. The deficit core favors the target, but a capable G16.36 neighbor 15.7 arcsec away shares the central TESS pixel and could in principle produce the loss through an extremely deep intrinsic eclipse. Attribution remains unresolved at this resolution.

**Next check:** Resolved eclipse photometry or multi-source PRF localization of the 15.7-arcsec pair.

Catalogue novelty: central seven-group result is in ../../shared-catalogues/coverage-matrix.csv. A cone-source entry alone does not establish an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 82 | 193 | 3534.4229057 | 0.001157 | 20.98 | used |
| 82 | 194 | 3543.8431342 | 0.001157 | 21.43 | used |
| 82 | 195 | 3553.2644488 | 0.001157 | 19.71 | used |
| 83 | 196 | 3562.6856663 | 0.001157 | 19.00 | used |
| 83 | 197 | 3572.1047515 | 0.001157 | 21.55 | used |
| 83 | 198 | 3581.5266560 | 0.001157 | 19.87 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s56.json, historical/diff_s56.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). Source code and all retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R494. Public evidence files: [diff_s56.json](../../evidence/17926125/historical/diff_s56.json), [diff_s56.png](../../evidence/17926125/historical/diff_s56.png), [gaia.json](../../evidence/17926125/historical/gaia.json), [measurements.json](../../evidence/17926125/measurements.json), [raw-events.png](../../evidence/17926125/raw-events.png), [raw-windows.csv](../../evidence/17926125/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch09/INDEX.md). 
