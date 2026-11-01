# TIC 34014384: CONFIRMED

Full bounded review: **COMPLETE**. This physical outcome is separate from catalogue novelty and from the historical screening label.

1. **Raw repeat:** 6 measured same-kind eclipses in representative QLP SAP_FLUX sectors [2, 69, 96]; raw flux, quality filtering, fitted windows and plots are retained. Fitted periodic depressions alone would be insufficient: the inspected windows have recurring eclipse morphology. Predicted centers were search guides, never timing points. Flagged or unresolved windows are not clean nulls.
2. **Timing and aliases:** measured midpoints give P = 9.5949058113 ± 0.0000134136 d and reference BTJD 1363.9891996 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind within-sector counts and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check rather than a blind exhaustive search.
3. **Attribution:** historical S69 TESScut deficit lies 0.80 arcsec from the target coordinate; peak pixel [7, 8] and target pixel [7, 8]. Image-model fractional residual 0.224 is not a calibrated position error. Capable Gaia neighbors: None within 60 arcsec under the approximate G-band flux budget. The intrinsic neighbor requirement is not the same as the blended pixel loss.
4. **Alternative reduction:** independent target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture extraction gives 46.04/45.25/39.29 ppt in 3 stacked events; selected QLP raw depth is 45.36 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution, event-kind mixing and temporal changes limit a direct depth comparison.
5. **Gaia geometry:** matched DR3 source 2328077646884230912 has SB1 period 9.5946733453 d, e = 0.07996. The closest edge-on conjunction differs from the measured eclipse epoch by 0.19039 d (0.01984 phase); the linear propagated timing scale from source-specific full SB1 covariance is 0.52291 d. Rough central duration 7.88 h versus measured median 6.38 h uses TIC radius and a minimum-mass main-sequence companion; it is not a physical fit or a sigma veto.

**Deciding interpretation and limitations:** Six raw eclipses across S2/69/96, including three consecutive S69 cycles. The S69 deficit peaks at the target and the aperture reductions retain the eclipse.

**Next check:** Optional resolved photometry or spectroscopy for precision binary parameters; no bounded admission check remains missing.

Catalogue novelty: the central seven-group check in ../../shared-catalogues/coverage-matrix.csv reports complete scoped coverage and no identified prior eclipsing-binary match for this exact target. This is not exhaustive priority and does not resolve embargoed identities.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 2 | 0 | 1363.9921725 | 0.010417 | 46.31 | used |
| 69 | 190 | 3187.0212237 | 0.001157 | 47.53 | used |
| 69 | 191 | 3196.6163746 | 0.001157 | 45.66 | used |
| 69 | 192 | 3206.2109008 | 0.001157 | 45.06 | used |
| 96 | 266 | 3916.2340458 | 0.001157 | 41.66 | used |
| 96 | 267 | 3925.8292435 | 0.001157 | 41.44 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s69.json, historical/diff_s69.png and historical/gaia.json. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). Source code and retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R463. Public evidence files: [diff_s69.json](../../evidence/34014384/historical/diff_s69.json), [diff_s69.png](../../evidence/34014384/historical/diff_s69.png), [gaia.json](../../evidence/34014384/historical/gaia.json), [measurements.json](../../evidence/34014384/measurements.json), [raw-events.png](../../evidence/34014384/raw-events.png), [raw-windows.csv](../../evidence/34014384/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch06/INDEX.md). 
