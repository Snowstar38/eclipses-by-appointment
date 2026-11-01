# TIC 428703516: PROBABLE

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are recorded separately. The historical screening label is not an admission verdict.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 4 timing-usable measured eclipses in representative sectors [19, 59, 86]. The raw plot and numeric windows retain the light-curve evidence. Local trapezoids have free centers, depths, durations and baselines. Historical predicted times guided windows only. Flagged or uncovered intervals are not null detections.
2. **Measured timing and alias: pass.** 4 actual midpoints yield P = 19.5422216389 ± 0.0001299315 d and reference epoch BTJD 1823.3679179 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind cycle counts, within-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive blind all-period search.
3. **Source attribution: unresolved after completed check.** Historical S52 cutout puts the deficit 2.07 arcsec from the target coordinate; peak [7, 7] versus target pixel [7, 7]. Image-model fractional residual 0.488; this is not a calibrated localization error. Capable Gaia neighbors: Gaia 548058855130833792: 11.2 arcsec, G 18.035, approximate intrinsic eclipse requirement 0.888; Gaia 548058859427261184: 21.5 arcsec, G 13.709, approximate intrinsic eclipse requirement 0.021; Gaia 548047104100306688: 51.4 arcsec, G 17.903, approximate intrinsic eclipse requirement 0.787; Gaia 548058859427256832: 52.1 arcsec, G 15.785, approximate intrinsic eclipse requirement 0.116. The intrinsic requirement uses an approximate flux budget and is not compared directly with a blended pixel fractional loss.
4. **Alternative reduction: pass.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 4.24/3.46/3.72 ppt in 2 stacked events; median selected QLP raw fit depth 4.41 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and any mixed event kinds limit depth comparisons.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 548058859427458688 has orbital P = 19.5459437733 d, e = 0.02433; closest edge-on conjunction offset at the measured epoch is -0.18196 d (-0.00931 phase), with 0.29026 d linearly propagated full-SB1-covariance timing error. The rough central duration is 5.97 h versus observed median 3.86 h; assumed TIC radius and minimum-mass companion are not a full fit. Geometry supports physical plausibility without an arbitrary sigma veto.

**Deciding interpretation and limitation:** Four shallow raw eclipses in S19/59/86, including consecutive S86 cycles, support recurrence. The deficit favors the target over the capable 21.5-arcsec neighbor, but a capable Gaia source 11.2 arcsec away is inside one TESS pixel and could in principle produce the 4-ppt loss with a deep intrinsic eclipse. Attribution remains unresolved at this resolution.

**Next check:** Resolved eclipse photometry or multi-source PRF localization of the 11.2-arcsec pair.

Catalogue novelty: central seven-group result is in ../../shared-catalogues/coverage-matrix.csv. A cone-source entry alone does not establish an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 19 | 0 | 1823.3699499 | 0.010417 | 4.80 | used |
| 59 | 56 | 2917.7318282 | 0.003696 | 4.19 | used |
| 86 | 93 | 3640.7902858 | 0.003409 | 4.51 | used |
| 86 | 94 | 3660.3435838 | 0.004222 | 4.31 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s52.json, historical/diff_s52.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). Source code and all retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R499. Public evidence files: [diff_s52.json](../../evidence/428703516/historical/diff_s52.json), [diff_s52.png](../../evidence/428703516/historical/diff_s52.png), [gaia.json](../../evidence/428703516/historical/gaia.json), [measurements.json](../../evidence/428703516/measurements.json), [raw-events.png](../../evidence/428703516/raw-events.png), [raw-windows.csv](../../evidence/428703516/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch09/INDEX.md). 
