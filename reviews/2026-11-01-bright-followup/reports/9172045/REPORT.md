# TIC 9172045: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are recorded separately. The historical screening label is not an admission verdict.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 5 timing-usable measured eclipses in representative sectors [47, 60]. The raw plot and numeric windows retain the light-curve evidence. Local trapezoids have free centers, depths, durations and baselines. Predicted times guided windows only. Flagged or uncovered intervals are not null detections.
2. **Measured timing and alias: pass.** 5 actual midpoints yield P = 7.6743519360 ± 0.0000459896 d and reference epoch BTJD 2584.2044385 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind cycle counts, within-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive blind all-period search.
3. **Source attribution: favors target at TESS image resolution.** Historical sector 47 cutout puts the deficit 0.24 arcsec from the target coordinate; peak [7, 7] versus target pixel [8, 7]. Image-model fractional residual 0.213; this is not a calibrated localization error. Capable Gaia neighbors: Gaia 919146748219604736: separation 18.80 arcsec, G 13.721, approximate intrinsic eclipse requirement 0.139. The intrinsic requirement uses an approximate flux budget and is not compared directly with a blended pixel fractional loss.
4. **Alternative reduction: pass.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 23.77/21.23/20.42 ppt in 3 stacked events; median selected QLP raw fit depth 25.38 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and any mixed event kinds limit depth comparisons.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 919146679500127616 has orbital P = 7.6744160954 d, e = 0.24606; closest edge-on conjunction offset at the measured epoch is -0.07616 d (-0.00992 phase), with 0.15053 d linearly propagated full-SB1-covariance timing error. The rough central duration is 6.62 h versus observed median 3.04 h; assumed TIC radius and minimum-mass companion are not a full fit. Geometry supports physical plausibility without an arbitrary sigma veto or proof of which unresolved neighbor eclipses.

**Deciding interpretation and limitation:** Five repeated raw eclipses S47/60. A capable neighbor 18.8 arcsec away can in principle produce the blended loss, but the inspected deficit core falls on the target and shows no distinct neighbor peak; attribution is favored at TESS resolution, not proven subpixel.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is in ../../shared-catalogues/coverage-matrix.csv. A cone-source entry alone does not establish an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 47 | 96 | 2584.2038405 | 0.003472 | 24.64 | used |
| 47 | 97 | 2591.8791377 | 0.003472 | 27.68 | used |
| 47 | 98 | 2599.5533210 | 0.003472 | 25.38 | used |
| 60 | 143 | 2944.8992147 | 0.001157 | 25.04 | used |
| 60 | 145 | 2960.2474561 | 0.001157 | 26.21 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s47.json, historical/diff_s47.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json).  Source code and all retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R415. Public evidence files: [diff_s47.json](../../evidence/9172045/historical/diff_s47.json), [diff_s47.png](../../evidence/9172045/historical/diff_s47.png), [gaia.json](../../evidence/9172045/historical/gaia.json), [measurements.json](../../evidence/9172045/measurements.json), [raw-events.png](../../evidence/9172045/raw-events.png), [raw-windows.csv](../../evidence/9172045/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch01/INDEX.md). 
