# TIC 241089793: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are recorded separately. The historical screening label is not an admission verdict.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 5 timing-usable measured eclipses in representative sectors [18, 85]. The raw plot and numeric windows retain the light-curve evidence. Local trapezoids have free centers, depths, durations and baselines. Predicted times guided windows only. Flagged or uncovered intervals are not null detections.
2. **Measured timing and alias: pass.** 5 actual midpoints yield P = 5.6321610433 ± 0.0000186954 d and reference epoch BTJD 1792.3571061 (repeating eclipse; primary by convention). Same-kind cycle counts, within-sector repeats and parity are in ../alias-audit.json. Linear fit to independently measured raw S18 and S85 midpoints, with max(formal center covariance, half cadence) per event and scatter inflation; formal fit error, not total calibrated uncertainty. Historical period/cycle predictions guided extraction only. This is a bounded alias check, not an exhaustive blind all-period search.
3. **Source attribution: favors target at TESS image resolution.** Historical sector 85 cutout puts the deficit 3.60 arcsec from the target coordinate; peak [8, 8] versus target pixel [8, 8]. Image-model fractional residual 0.847; this is not a calibrated localization error. Capable Gaia neighbors: Gaia 408289628502534144: separation 36.59 arcsec, G 14.375, approximate intrinsic eclipse requirement 0.166; Gaia 408289727280756608: separation 39.76 arcsec, G 14.819, approximate intrinsic eclipse requirement 0.242. The intrinsic requirement uses an approximate flux budget and is not compared directly with a blended pixel fractional loss.
4. **Alternative reduction: pass.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 18.09/15.54/10.73 ppt in 3 stacked events; median selected QLP raw fit depth 17.95 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and any mixed event kinds limit depth comparisons.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 408289727280589312 has orbital P = 5.6321186642 d, e = 0.02967; closest edge-on conjunction offset at the measured epoch is -0.03436 d (-0.00610 phase), with 0.12821 d linearly propagated full-SB1-covariance timing error. The rough central duration is 4.30 h versus observed median 1.88 h; assumed TIC radius and minimum-mass companion are not a full fit. Geometry supports physical plausibility without an arbitrary sigma veto or proof of which unresolved neighbor eclipses.

**Deciding interpretation and limitation:** S18 clean raw eclipses at successive cycles -1 and 0 plus cycle 2 test the 5.632-day recurrence; measured S85 cycles 324/326 extend the timing baseline. S85 cycle 325 and S18 cycle 1 are flagged, not clean nulls. S18 partial cycle 3 is excluded from timing. The formal period error is not total calibrated uncertainty.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is in ../../shared-catalogues/coverage-matrix.csv. A cone-source entry alone does not establish an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 18 | -1 | 1792.3580780 | 0.010420 | 16.04 | used |
| 18 | 0 | 1797.9886680 | 0.010420 | 17.95 | used |
| 18 | 2 | 1809.2530956 | 0.010420 | 18.69 | used |
| 18 | 3 | 1814.8824888 | 0.010420 | 19.46 | excluded: Partial coverage; excluded from joint timing fit. |
| 85 | 324 | 3622.8096759 | 0.001157 | 19.54 | used |
| 85 | 326 | 3634.0735380 | 0.001157 | 16.56 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s85.json, historical/diff_s85.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). This target also has ../241089793-refined-timing.json, ../241089793-alias-coverage.json and s18-cycle-check.png. Source code and all retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R413. Public evidence files: [diff_s85.json](../../evidence/241089793/historical/diff_s85.json), [diff_s85.png](../../evidence/241089793/historical/diff_s85.png), [gaia.json](../../evidence/241089793/historical/gaia.json), [measurements.json](../../evidence/241089793/measurements.json), [raw-events.png](../../evidence/241089793/raw-events.png), [raw-windows.csv](../../evidence/241089793/raw-windows.csv), [s18-cycle-check.png](../../evidence/241089793/s18-cycle-check.png). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch01/INDEX.md). 
