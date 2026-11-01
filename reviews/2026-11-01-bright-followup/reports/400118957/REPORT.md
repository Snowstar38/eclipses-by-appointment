# TIC 400118957: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 9 fitted representative eclipses in sectors [10, 38, 65]; 9 enter the reported timing fit. Local trapezoids have free centers, depths, durations and baselines. Predicted times guided windows only; flagged or uncovered intervals are not clean nulls. See raw-events.png, raw-windows.csv and measurements.json.
2. **Measured timing and aliases: pass.** 9 same-kind actual midpoints yield P = 9.1411474439 ± 0.0000216391 d and reference epoch BTJD 1576.1920454 (Selected repeating eclipse; primary by convention; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; representative parity shows no persistent unequal alternation. Same-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Half/double alias assessment is bounded by representative raw morphology, not an exhaustive blind period search.
3. **Source attribution: favors target at TESS pixel resolution.** Historical sector 10 cutout places the deficit centroid 2.32 arcsec from the target; peak pixel [8, 7] versus target pixel [8, 7]. Image-model fractional residual 0.514 is not a calibrated localization error. Gaia neighbors capable under the approximate G-band flux budget: Gaia 5231653797315230336: 15.3 arcsec, G 12.789, approximate intrinsic eclipse requirement 0.188; Gaia 5231653969118047488: 50.8 arcsec, G 14.684, approximate intrinsic eclipse requirement 0.740; Gaia 5231653758651818240: 58.6 arcsec, G 13.675, approximate intrinsic eclipse requirement 0.336; Gaia 5231653969113936384: 59.0 arcsec, G 14.499, approximate intrinsic eclipse requirement 0.635. The neighbor intrinsic eclipse requirement is not directly comparable to blended pixel fractional loss.
4. **Alternative reduction: pass.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 55.89/47.10/41.16 ppt over 3 stacked events, compared with median selected QLP raw fit depth 79.08 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution or mixed eclipse kinds limit depth equality. and aperture dilution or mixed eclipse kinds limit depth equality.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 5231653793011555840 has P = 9.1418612161 d and e = 0.18822. The closest edge-on conjunction offset at the measured epoch is -0.06312 d (-0.00690 phase), with 0.11125 d linearly propagated full-SB1-covariance timing error. A rough central duration is 7.25 h versus observed median 5.27 h; TIC radius and minimum-mass companion are approximations, and impact parameter is not fitted.

**Deciding interpretation and limitation:** Raw depths change with sector aperture, while nine measured midpoints retain one recurrence. A capable neighbor 15.3 arcsec away is distinct from the target-centered difference core; crowding limits intrinsic depth claims.

**Next check:** Optional precision binary characterization.

Catalogue novelty is in the central seven-group ../../shared-catalogues/coverage-matrix.csv receipt; physical classification does not assert exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Orbital timing status |
|---|---:|---:|---:|---:|---|
| 10 | 0 | 1576.1911659 | 0.010417 | 63.19 | used |
| 10 | 1 | 1585.3330745 | 0.010417 | 70.26 | used |
| 10 | 2 | 1594.4736317 | 0.010417 | 71.75 | used |
| 38 | 83 | 2334.9068107 | 0.003472 | 78.45 | used |
| 38 | 84 | 2344.0487326 | 0.003472 | 81.09 | used |
| 38 | 85 | 2353.1901072 | 0.003472 | 80.81 | used |
| 65 | 164 | 3075.3402986 | 0.001157 | 79.26 | used |
| 65 | 165 | 3084.4815508 | 0.001157 | 80.15 | used |
| 65 | 166 | 3093.6222526 | 0.001157 | 79.08 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s10.json, historical/diff_s10.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). All evidence and source files are in ../SHA256SUMS.json.


Stable review key: R504. Public evidence files: [diff_s10.json](../../evidence/400118957/historical/diff_s10.json), [diff_s10.png](../../evidence/400118957/historical/diff_s10.png), [gaia.json](../../evidence/400118957/historical/gaia.json), [measurements.json](../../evidence/400118957/measurements.json), [raw-events.png](../../evidence/400118957/raw-events.png), [raw-windows.csv](../../evidence/400118957/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch10/INDEX.md). 
