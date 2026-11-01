# TIC 283016810: PROBABLE

Full bounded review: **COMPLETE**. This physical outcome is separate from catalogue novelty and from the historical screening label.

1. **Raw repeat:** 13 measured same-kind eclipses in representative QLP SAP_FLUX sectors [17, 58, 85]; raw flux, quality filtering, fitted windows and plots are retained. Fitted periodic depressions alone would be insufficient: the inspected windows have recurring eclipse morphology. Predicted centers were search guides, never timing points. Flagged or unresolved windows are not clean nulls.
2. **Timing and aliases:** measured midpoints give P = 5.1642748232 ± 0.0000050389 d and reference BTJD 1770.9909383 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind within-sector counts and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check rather than a blind exhaustive search.
3. **Attribution:** historical S24 TESScut deficit lies 0.94 arcsec from the target coordinate; peak pixel [8, 8] and target pixel [8, 8]. Image-model fractional residual 0.808 is not a calibrated position error. Capable Gaia neighbors: Gaia 431751179422562816, 19.0 arcsec, G 15.24, approximate intrinsic requirement 0.95; Gaia 431751351221252480, 53.5 arcsec, G 12.36, approximate intrinsic requirement 0.12; Gaia 431751351221249280, 59.7 arcsec, G 15.23, approximate intrinsic requirement 0.95. The intrinsic neighbor requirement is not the same as the blended pixel loss.
4. **Alternative reduction:** independent target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture extraction gives 53.08/45.84/26.48 ppt in 5 stacked events; selected QLP raw depth is 54.70 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution, event-kind mixing and temporal changes limit a direct depth comparison.
5. **Gaia geometry:** matched DR3 source 431751175113711872 has SB1 period 5.1640736469 d, e = 0.06043. The closest edge-on conjunction differs from the measured eclipse epoch by -0.01453 d (-0.00281 phase); the linear propagated timing scale from source-specific full SB1 covariance is 0.09489 d. Rough central duration 10.99 h versus measured median 7.72 h uses TIC radius and a minimum-mass main-sequence companion; it is not a physical fit or a sigma veto.

**Deciding interpretation and limitations:** Thirteen raw eclipses across S17/58/85. Three capable Gaia neighbors include one about 19 arcsec away. The S24 deficit peak overlaps the target pixel, but TESS cannot resolve the nearby capable source within roughly one pixel. The image-model residual further limits attribution.

**Next check:** Resolved eclipse photometry or multi-source PRF localization of the capable nearby star.

Catalogue novelty: the central seven-group check in ../../shared-catalogues/coverage-matrix.csv reports complete scoped coverage and no identified prior eclipsing-binary match for this exact target. This is not exhaustive priority and does not resolve embargoed identities.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 17 | 0 | 1770.9892475 | 0.010417 | 54.33 | used |
| 17 | 2 | 1781.3168663 | 0.010417 | 54.90 | used |
| 17 | 3 | 1786.4833952 | 0.010417 | 54.95 | used |
| 58 | 216 | 2886.4738673 | 0.001157 | 54.70 | used |
| 58 | 217 | 2891.6383068 | 0.001157 | 55.10 | used |
| 58 | 218 | 2896.8035472 | 0.001157 | 54.15 | used |
| 58 | 219 | 2901.9670358 | 0.001157 | 54.24 | used |
| 58 | 220 | 2907.1316295 | 0.001157 | 55.27 | used |
| 85 | 357 | 3614.6371395 | 0.001157 | 54.53 | used |
| 85 | 358 | 3619.8021171 | 0.001157 | 54.99 | used |
| 85 | 359 | 3624.9653593 | 0.001157 | 55.97 | used |
| 85 | 360 | 3630.1301941 | 0.001157 | 54.64 | used |
| 85 | 361 | 3635.2931091 | 0.001157 | 54.34 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s24.json, historical/diff_s24.png and historical/gaia.json. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). Source code and retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R466. Public evidence files: [diff_s24.json](../../evidence/283016810/historical/diff_s24.json), [diff_s24.png](../../evidence/283016810/historical/diff_s24.png), [gaia.json](../../evidence/283016810/historical/gaia.json), [measurements.json](../../evidence/283016810/measurements.json), [raw-events.png](../../evidence/283016810/raw-events.png), [raw-windows.csv](../../evidence/283016810/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch06/INDEX.md). 
