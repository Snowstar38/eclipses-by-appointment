# TIC 261702897: CONFIRMED

Full bounded review: **COMPLETE**. This physical outcome is separate from catalogue novelty and from the historical screening label.

1. **Raw repeat:** 5 measured same-kind eclipses in representative QLP SAP_FLUX sectors [12, 99, 102]; raw flux, quality filtering, fitted windows and plots are retained. Fitted periodic depressions alone would be insufficient: the inspected windows have recurring eclipse morphology. Predicted centers were search guides, never timing points. Flagged or unresolved windows are not clean nulls.
2. **Timing and aliases:** measured midpoints give P = 6.9340108453 ± 0.0000376792 d and reference BTJD 1630.5145301 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind within-sector counts and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check rather than a blind exhaustive search.
3. **Attribution:** historical S38 TESScut deficit lies 3.09 arcsec from the target coordinate; peak pixel [7, 7] and target pixel [7, 7]. Image-model fractional residual 0.985 is not a calibrated position error. Capable Gaia neighbors: Gaia 5824727895463607808, 44.9 arcsec, G 10.06, approximate intrinsic requirement 0.09; Gaia 5824727517506486016, 55.3 arcsec, G 14.78, approximate intrinsic requirement 0.95. The intrinsic neighbor requirement is not the same as the blended pixel loss.
4. **Alternative reduction:** independent target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture extraction gives 41.85/21.50/8.76 ppt in 4 stacked events; selected QLP raw depth is 71.34 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution, event-kind mixing and temporal changes limit a direct depth comparison.
5. **Gaia geometry:** matched DR3 source 5824728342140218880 has SB1 period 6.9344260455 d, e = 0.04238. The closest edge-on conjunction differs from the measured eclipse epoch by -0.06187 d (-0.00892 phase); the linear propagated timing scale from source-specific full SB1 covariance is 0.09078 d. Rough central duration 4.51 h versus measured median 3.50 h uses TIC radius and a minimum-mass main-sequence companion; it is not a physical fit or a sigma veto.

**Deciding interpretation and limitations:** Five raw eclipses across S12/99/102. Two capable Gaia neighbors at about 45 and 55 arcsec require separate evaluation; the S38 deficit peak is at the target pixel, distinct from the bright southeast neighbor. The poor image-model fit limits centroid precision.

**Next check:** Optional resolved photometry or spectroscopy for precision binary parameters; no bounded admission check remains missing.

Catalogue novelty: the central seven-group check in ../../shared-catalogues/coverage-matrix.csv reports complete scoped coverage and no identified prior eclipsing-binary match for this exact target. This is not exhaustive priority and does not resolve embargoed identities.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 12 | 0 | 1630.5077983 | 0.010417 | 71.34 | used |
| 99 | 349 | 4050.4862110 | 0.001157 | 68.80 | used |
| 99 | 351 | 4064.3528726 | 0.001319 | 51.63 | used |
| 102 | 361 | 4133.6917844 | 0.001157 | 87.32 | used |
| 102 | 363 | 4147.5589027 | 0.001157 | 88.29 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s38.json, historical/diff_s38.png and historical/gaia.json. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). Source code and retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R462. Public evidence files: [diff_s38.json](../../evidence/261702897/historical/diff_s38.json), [diff_s38.png](../../evidence/261702897/historical/diff_s38.png), [gaia.json](../../evidence/261702897/historical/gaia.json), [measurements.json](../../evidence/261702897/measurements.json), [raw-events.png](../../evidence/261702897/raw-events.png), [raw-windows.csv](../../evidence/261702897/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch06/INDEX.md). 
