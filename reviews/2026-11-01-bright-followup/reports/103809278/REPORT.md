# TIC 103809278: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are recorded separately. The historical screening label is not an admission verdict.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 9 timing-usable measured eclipses in representative sectors [14, 47, 75]. The raw plot and numeric windows retain the light-curve evidence. Local trapezoids have free centers, depths, durations and baselines. Predicted times guided windows only. Flagged or uncovered intervals are not null detections.
2. **Measured timing and alias: pass.** 9 actual midpoints yield P = 5.6815171354 ± 0.0000120548 d and reference epoch BTJD 1685.4540122 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind cycle counts, within-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive blind all-period search.
3. **Source attribution: favors target at TESS image resolution.** Historical sector 14 cutout puts the deficit 3.79 arcsec from the target coordinate; peak [7, 8] versus target pixel [7, 8]. Image-model fractional residual 0.023; this is not a calibrated localization error. Capable Gaia neighbors: None within 60 arcsec under the approximate G-band flux budget. The intrinsic requirement uses an approximate flux budget and is not compared directly with a blended pixel fractional loss.
4. **Alternative reduction: pass.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 147.02/147.02/146.82 ppt in 4 stacked events; median selected QLP raw fit depth 146.26 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and any mixed event kinds limit depth comparisons.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 1059801184791364480 has orbital P = 5.6814017817 d, e = 0.08033; closest edge-on conjunction offset at the measured epoch is 0.13967 d (0.02458 phase), with 0.10317 d linearly propagated full-SB1-covariance timing error. The rough central duration is 4.38 h versus observed median 4.14 h; assumed TIC radius and minimum-mass companion are not a full fit. Geometry supports physical plausibility without an arbitrary sigma veto or proof of which unresolved neighbor eclipses.

**Deciding interpretation and limitation:** Nine deep raw eclipses across S14/47/75; target-centered difference core and no capable Gaia neighbor under the brightness screen.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is in ../../shared-catalogues/coverage-matrix.csv. A cone-source entry alone does not establish an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 14 | 0 | 1685.4583462 | 0.010416 | 146.33 | used |
| 14 | 1 | 1691.1393536 | 0.010416 | 148.37 | used |
| 14 | 3 | 1702.5021041 | 0.010416 | 141.24 | used |
| 47 | 158 | 2583.1329651 | 0.003472 | 146.03 | used |
| 47 | 159 | 2588.8143143 | 0.003472 | 146.26 | used |
| 47 | 161 | 2600.1777778 | 0.003472 | 146.26 | used |
| 47 | 162 | 2605.8591093 | 0.003472 | 146.04 | used |
| 75 | 293 | 3350.1387125 | 0.001157 | 147.35 | used |
| 75 | 296 | 3367.1830767 | 0.001157 | 147.00 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s14.json, historical/diff_s14.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json).  Source code and all retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R416. Public evidence files: [diff_s14.json](../../evidence/103809278/historical/diff_s14.json), [diff_s14.png](../../evidence/103809278/historical/diff_s14.png), [gaia.json](../../evidence/103809278/historical/gaia.json), [measurements.json](../../evidence/103809278/measurements.json), [raw-events.png](../../evidence/103809278/raw-events.png), [raw-windows.csv](../../evidence/103809278/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch01/INDEX.md). 
