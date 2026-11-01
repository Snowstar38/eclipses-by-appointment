# TIC 349749097: PROBABLE

Full bounded review: **COMPLETE**. This physical outcome is separate from catalogue novelty and from the historical screening label.

1. **Raw repeat:** 16 measured same-kind eclipses in representative QLP SAP_FLUX sectors [13, 93, 104]; raw flux, quality filtering, fitted windows and plots are retained. Fitted periodic depressions alone would be insufficient: the inspected windows have recurring eclipse morphology. Predicted centers were search guides, never timing points. Flagged or unresolved windows are not clean nulls.
2. **Timing and aliases:** measured midpoints give P = 3.7886980284 ± 0.0000059917 d and reference BTJD 1663.0043255 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind within-sector counts and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check rather than a blind exhaustive search.
3. **Attribution:** historical S13 TESScut deficit lies 2.47 arcsec from the target coordinate; peak pixel [7, 8] and target pixel [8, 8]. Image-model fractional residual 0.655 is not a calibrated position error. Capable Gaia neighbors: Gaia 6702211498076393216, 24.4 arcsec, G 14.21, approximate intrinsic requirement 0.41; Gaia 6702211601155599616, 33.4 arcsec, G 14.55, approximate intrinsic requirement 0.54. The intrinsic neighbor requirement is not the same as the blended pixel loss.
4. **Alternative reduction:** independent target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture extraction gives 54.70/49.79/41.74 ppt in 7 stacked events; selected QLP raw depth is 55.44 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution, event-kind mixing and temporal changes limit a direct depth comparison.
5. **Gaia geometry:** matched DR3 source 6702211493775030784 has SB1 period 3.7889568790 d, e = 0.03612. The closest edge-on conjunction differs from the measured eclipse epoch by -0.06788 d (-0.01791 phase); the linear propagated timing scale from source-specific full SB1 covariance is 0.05803 d. Rough central duration 6.91 h versus measured median 4.46 h uses TIC radius and a minimum-mass main-sequence companion; it is not a physical fit or a sigma veto.

**Deciding interpretation and limitations:** Sixteen raw eclipses across S13/93/104. Two capable Gaia neighbors about 24 and 33 arcsec away lie in a crowded field. The S13 deficit core overlaps the target pixel, but the high image-model residual and roughly one-pixel separation leave source identity unresolved.

**Next check:** Resolved eclipse photometry or multi-source PRF localization of the capable nearby star.

Catalogue novelty: the central seven-group check in ../../shared-catalogues/coverage-matrix.csv reports complete scoped coverage and no identified prior eclipsing-binary match for this exact target. This is not exhaustive priority and does not resolve embargoed identities.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 13 | 1 | 1662.9913433 | 0.010416 | 58.81 | used |
| 13 | 2 | 1666.7774115 | 0.010416 | 53.37 | used |
| 13 | 3 | 1670.5687257 | 0.010416 | 53.30 | used |
| 13 | 4 | 1674.3590344 | 0.010416 | 51.69 | used |
| 13 | 5 | 1678.1464556 | 0.010416 | 58.45 | used |
| 93 | 574 | 3833.9294581 | 0.001157 | 59.72 | used |
| 93 | 575 | 3837.7180765 | 0.001157 | 59.41 | used |
| 93 | 577 | 3845.2955559 | 0.001157 | 58.11 | used |
| 93 | 578 | 3849.0842975 | 0.001157 | 58.79 | used |
| 93 | 579 | 3852.8730619 | 0.001157 | 59.25 | used |
| 104 | 666 | 4182.4872216 | 0.001157 | 55.37 | used |
| 104 | 667 | 4186.2759269 | 0.001157 | 55.51 | used |
| 104 | 668 | 4190.0651155 | 0.001157 | 54.59 | used |
| 104 | 669 | 4193.8542070 | 0.001157 | 54.46 | used |
| 104 | 670 | 4197.6433183 | 0.001157 | 55.06 | used |
| 104 | 671 | 4201.4306811 | 0.001157 | 53.92 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s13.json, historical/diff_s13.png and historical/gaia.json. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). Source code and retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R469. Public evidence files: [diff_s13.json](../../evidence/349749097/historical/diff_s13.json), [diff_s13.png](../../evidence/349749097/historical/diff_s13.png), [gaia.json](../../evidence/349749097/historical/gaia.json), [measurements.json](../../evidence/349749097/measurements.json), [raw-events.png](../../evidence/349749097/raw-events.png), [raw-windows.csv](../../evidence/349749097/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch06/INDEX.md). 
