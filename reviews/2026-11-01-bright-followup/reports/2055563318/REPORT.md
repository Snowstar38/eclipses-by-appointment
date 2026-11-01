# TIC 2055563318: PROBABLE

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are recorded separately. The historical screening label is not an admission verdict.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 8 timing-usable measured eclipses in representative sectors [29, 95, 104]. The raw plot and numeric windows retain the light-curve evidence. Local trapezoids have free centers, depths, durations and baselines. Predicted times guided windows only. Flagged or uncovered intervals are not null detections.
2. **Measured timing and alias: pass.** 8 actual midpoints yield P = 6.0552614725 ± 0.0000071310 d and reference epoch BTJD 2093.8367290 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind cycle counts, within-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive blind all-period search.
3. **Source attribution: unresolved after completed check.** Historical sector 68 cutout puts the deficit 5.79 arcsec from the target coordinate; peak [8, 7] versus target pixel [8, 7]. Image-model fractional residual 0.044; this is not a calibrated localization error. Capable Gaia neighbors: Gaia 6524911983920449664: separation 1.11 arcsec, G 11.971, approximate intrinsic eclipse requirement 0.059. The intrinsic requirement uses an approximate flux budget and is not compared directly with a blended pixel fractional loss.
4. **Alternative reduction: pass.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 19.01/19.01/19.12 ppt in 4 stacked events; median selected QLP raw fit depth 30.23 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and any mixed event kinds limit depth comparisons.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 6524911983916150016 has orbital P = 6.0544220136 d, e = 0.14861; closest edge-on conjunction offset at the measured epoch is 0.12018 d (0.01985 phase), with 0.29407 d linearly propagated full-SB1-covariance timing error. The rough central duration is 3.87 h versus observed median 5.59 h; assumed TIC radius and minimum-mass companion are not a full fit. Geometry supports physical plausibility without an arbitrary sigma veto or proof of which unresolved neighbor eclipses.

**Deciding interpretation and limitation:** Eight repeated raw eclipses S29/95/104 show a real recurring signal, but a capable Gaia neighbor only 1.1 arcsec away shares the central TESS pixel. The image cannot uniquely identify the eclipsing star; geometry agrees with the selected Gaia orbit but does not cure this attribution limit.

**Next check:** Resolved eclipse photometry or multi-source PRF localization of the 1.1-arcsec pair.

Catalogue novelty: central seven-group result is in ../../shared-catalogues/coverage-matrix.csv. A cone-source entry alone does not establish an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 29 | 0 | 2093.8354098 | 0.003472 | 39.13 | used |
| 29 | 2 | 2105.9473696 | 0.003472 | 39.07 | used |
| 95 | 298 | 3898.3047275 | 0.001157 | 25.55 | used |
| 95 | 299 | 3904.3607308 | 0.001157 | 25.95 | used |
| 104 | 345 | 4182.9025932 | 0.001157 | 30.08 | used |
| 104 | 346 | 4188.9574118 | 0.001157 | 29.83 | used |
| 104 | 347 | 4195.0123085 | 0.001157 | 30.38 | used |
| 104 | 348 | 4201.0662356 | 0.001157 | 30.63 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s68.json, historical/diff_s68.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json).  Source code and all retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R419. Public evidence files: [diff_s68.json](../../evidence/2055563318/historical/diff_s68.json), [diff_s68.png](../../evidence/2055563318/historical/diff_s68.png), [gaia.json](../../evidence/2055563318/historical/gaia.json), [measurements.json](../../evidence/2055563318/measurements.json), [raw-events.png](../../evidence/2055563318/raw-events.png), [raw-windows.csv](../../evidence/2055563318/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch01/INDEX.md). 
