# TIC 285232364: CONFIRMED

Full bounded review: **COMPLETE**. This physical outcome is separate from catalogue novelty and from the historical screening label.

1. **Raw repeat:** 4 measured same-kind eclipses in representative QLP SAP_FLUX sectors [58, 85]; raw flux, quality filtering, fitted windows and plots are retained. Fitted periodic depressions alone would be insufficient: the inspected windows have recurring eclipse morphology. Predicted centers were search guides, never timing points. Flagged or unresolved windows are not clean nulls.
2. **Timing and aliases:** measured midpoints give P = 12.6226616088 ± 0.0000199522 d and reference BTJD 2886.7012424 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind within-sector counts and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check rather than a blind exhaustive search.
3. **Attribution:** historical S18 TESScut deficit lies 4.06 arcsec from the target coordinate; peak pixel [8, 8] and target pixel [8, 8]. Image-model fractional residual 0.758 is not a calibrated position error. Capable Gaia neighbors: Gaia 427362616196340608, 56.1 arcsec, G 13.35, approximate intrinsic requirement 0.61. The intrinsic neighbor requirement is not the same as the blended pixel loss.
4. **Alternative reduction:** independent target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture extraction gives 134.81/117.84/92.18 ppt in 2 stacked events; selected QLP raw depth is 156.49 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution, event-kind mixing and temporal changes limit a direct depth comparison.
5. **Gaia geometry:** matched DR3 source 427362714972324736 has SB1 period 12.6184477876 d, e = 0.26083. The closest edge-on conjunction differs from the measured eclipse epoch by 0.63322 d (0.05018 phase); the linear propagated timing scale from source-specific full SB1 covariance is 0.33878 d. Rough central duration 6.67 h versus measured median 4.98 h uses TIC radius and a minimum-mass main-sequence companion; it is not a physical fit or a sigma veto.

**Deciding interpretation and limitations:** Four broad raw eclipses in S58/85, two adjacent cycles per sector. A capable neighbor about 56 arcsec away is spatially distinct from the S18 target-centered deficit. The image fit is imperfect and aperture depths are diluted.

**Next check:** Optional resolved photometry or spectroscopy for precision binary parameters; no bounded admission check remains missing.

Catalogue novelty: the central seven-group check in ../../shared-catalogues/coverage-matrix.csv reports complete scoped coverage and no identified prior eclipsing-binary match for this exact target. This is not exhaustive priority and does not resolve embargoed identities.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 58 | 88 | 2886.7011554 | 0.001157 | 157.10 | used |
| 58 | 89 | 2899.3239805 | 0.001157 | 156.71 | used |
| 85 | 146 | 3618.8163095 | 0.001157 | 156.05 | used |
| 85 | 147 | 3631.4375941 | 0.001157 | 156.27 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s18.json, historical/diff_s18.png and historical/gaia.json. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). Source code and retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R465. Public evidence files: [diff_s18.json](../../evidence/285232364/historical/diff_s18.json), [diff_s18.png](../../evidence/285232364/historical/diff_s18.png), [gaia.json](../../evidence/285232364/historical/gaia.json), [measurements.json](../../evidence/285232364/measurements.json), [raw-events.png](../../evidence/285232364/raw-events.png), [raw-windows.csv](../../evidence/285232364/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch06/INDEX.md). 
