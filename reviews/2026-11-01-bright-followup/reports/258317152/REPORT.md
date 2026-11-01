# TIC 258317152: CONFIRMED

Full bounded review: **COMPLETE**. This physical outcome is separate from catalogue novelty and from the historical screening label.

1. **Raw repeat:** 8 measured same-kind eclipses in representative QLP SAP_FLUX sectors [10, 99, 101]; raw flux, quality filtering, fitted windows and plots are retained. Fitted periodic depressions alone would be insufficient: the inspected windows have recurring eclipse morphology. Predicted centers were search guides, never timing points. Flagged or unresolved windows are not clean nulls.
2. **Timing and aliases:** measured midpoints give P = 6.2291664080 ± 0.0000148911 d and reference BTJD 1573.1699570 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind within-sector counts and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check rather than a blind exhaustive search.
3. **Attribution:** historical S64 TESScut deficit lies 1.37 arcsec from the target coordinate; peak pixel [8, 7] and target pixel [8, 7]. Image-model fractional residual 0.484 is not a calibrated position error. Capable Gaia neighbors: None within 60 arcsec under the approximate G-band flux budget. The intrinsic neighbor requirement is not the same as the blended pixel loss.
4. **Alternative reduction:** independent target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture extraction gives 117.22/108.87/83.39 ppt in 4 stacked events; selected QLP raw depth is 116.70 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution, event-kind mixing and temporal changes limit a direct depth comparison.
5. **Gaia geometry:** matched DR3 source 6143372790427445888 has SB1 period 6.2285564049 d, e = 0.07165. The closest edge-on conjunction differs from the measured eclipse epoch by 0.08404 d (0.01349 phase); the linear propagated timing scale from source-specific full SB1 covariance is 0.15193 d. Rough central duration 5.14 h versus measured median 3.97 h uses TIC radius and a minimum-mass main-sequence companion; it is not a physical fit or a sigma veto.

**Deciding interpretation and limitations:** Eight strong raw eclipses across S10/99/101. The historical S64 deficit peaks on the target, with no capable Gaia neighbor under the approximate flux budget; the image-model residual is large, so its centroid is only descriptive.

**Next check:** Optional resolved photometry or spectroscopy for precision binary parameters; no bounded admission check remains missing.

Catalogue novelty: the central seven-group check in ../../shared-catalogues/coverage-matrix.csv reports complete scoped coverage and no identified prior eclipsing-binary match for this exact target. This is not exhaustive priority and does not resolve embargoed identities.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 10 | 0 | 1573.1680904 | 0.010417 | 122.55 | used |
| 10 | 2 | 1585.6266461 | 0.010417 | 122.57 | used |
| 10 | 3 | 1591.8558908 | 0.010417 | 121.98 | used |
| 99 | 398 | 4052.3797987 | 0.001157 | 115.32 | used |
| 99 | 400 | 4064.8377476 | 0.001157 | 115.86 | used |
| 101 | 406 | 4102.2109375 | 0.001157 | 116.54 | used |
| 101 | 407 | 4108.4399395 | 0.001157 | 116.73 | used |
| 101 | 409 | 4120.8975692 | 0.001157 | 116.67 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s64.json, historical/diff_s64.png and historical/gaia.json. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). Source code and retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R460. Public evidence files: [diff_s64.json](../../evidence/258317152/historical/diff_s64.json), [diff_s64.png](../../evidence/258317152/historical/diff_s64.png), [gaia.json](../../evidence/258317152/historical/gaia.json), [measurements.json](../../evidence/258317152/measurements.json), [raw-events.png](../../evidence/258317152/raw-events.png), [raw-windows.csv](../../evidence/258317152/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch06/INDEX.md). 
