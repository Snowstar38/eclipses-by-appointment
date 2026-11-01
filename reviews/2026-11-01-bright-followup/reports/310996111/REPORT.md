# TIC 310996111: CONFIRMED

Full bounded review: **COMPLETE**. This physical outcome is separate from catalogue novelty and from the historical screening label.

1. **Raw repeat:** 4 measured same-kind eclipses in representative QLP SAP_FLUX sectors [76]; raw flux, quality filtering, fitted windows and plots are retained. Fitted periodic depressions alone would be insufficient: the inspected windows have recurring eclipse morphology. Predicted centers were search guides, never timing points. Flagged or unresolved windows are not clean nulls.
2. **Timing and aliases:** measured midpoints give P = 2.9826325236 ± 0.0003163772 d and reference BTJD 3376.1140790 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind within-sector counts and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check rather than a blind exhaustive search.
3. **Attribution:** historical S49 TESScut deficit lies 2.75 arcsec from the target coordinate; peak pixel [7, 8] and target pixel [7, 8]. Image-model fractional residual 0.424 is not a calibrated position error. Capable Gaia neighbors: Gaia 1559248294394682112, 52.0 arcsec, G 18.35, approximate intrinsic requirement 0.84; Gaia 1559154737124070528, 55.3 arcsec, G 14.06, approximate intrinsic requirement 0.02. The intrinsic neighbor requirement is not the same as the blended pixel loss.
4. **Alternative reduction:** independent target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture extraction gives 3.06/3.09/3.02 ppt in 8 stacked events; selected QLP raw depth is 3.80 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution, event-kind mixing and temporal changes limit a direct depth comparison.
5. **Gaia geometry:** matched DR3 source 1559154664107634560 has SB1 period 2.9825457445 d, e = 0.07326. The closest edge-on conjunction differs from the measured eclipse epoch by -0.07548 d (-0.02531 phase); the linear propagated timing scale from source-specific full SB1 covariance is 0.11227 d. Rough central duration 2.56 h versus measured median 0.72 h uses TIC radius and a minimum-mass main-sequence companion; it is not a physical fit or a sigma veto.

**Deciding interpretation and limitations:** Four shallow S76 raw events recur at the predicted phase, and the historical S49 aperture extraction retains a roughly 3 ppt target-pixel loss. S15/23 are 30-minute cadence: each predicted short event has at most one central sample, so their apparent weak or absent dips are not clean nulls. Capable neighbors about 52 and 55 arcsec away are distinct from the target-centered S49 deficit; the morphology and attribution remain limited by shallow depth.

**Next check:** Optional resolved photometry or spectroscopy for precision binary parameters; no bounded admission check remains missing.

Catalogue novelty: the central seven-group check in ../../shared-catalogues/coverage-matrix.csv reports complete scoped coverage and no identified prior eclipsing-binary match for this exact target. This is not exhaustive priority and does not resolve embargoed identities.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 76 | 557 | 3376.1143874 | 0.001284 | 5.78 | used |
| 76 | 558 | 3379.0956038 | 0.001653 | 3.70 | used |
| 76 | 559 | 3382.0799617 | 0.001651 | 3.89 | used |
| 76 | 563 | 3394.0098566 | 0.001488 | 2.78 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s49.json, historical/diff_s49.png and historical/gaia.json. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). Source code and retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R467. Public evidence files: [diff_s49.json](../../evidence/310996111/historical/diff_s49.json), [diff_s49.png](../../evidence/310996111/historical/diff_s49.png), [gaia.json](../../evidence/310996111/historical/gaia.json), [measurements.json](../../evidence/310996111/measurements.json), [raw-events.png](../../evidence/310996111/raw-events.png), [raw-windows.csv](../../evidence/310996111/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch06/INDEX.md). 
