# TIC 294082465: CONFIRMED

Full bounded review: **COMPLETE**. This physical outcome is separate from catalogue novelty and from the historical screening label.

1. **Raw repeat:** 3 measured same-kind eclipses in representative QLP SAP_FLUX sectors [8, 99]; raw flux, quality filtering, fitted windows and plots are retained. Fitted periodic depressions alone would be insufficient: the inspected windows have recurring eclipse morphology. Predicted centers were search guides, never timing points. Flagged or unresolved windows are not clean nulls.
2. **Timing and aliases:** measured midpoints give P = 17.3495287874 ± 0.0000712547 d and reference BTJD 1519.4094810 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind within-sector counts and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check rather than a blind exhaustive search.
3. **Attribution:** historical S99 TESScut deficit lies 1.70 arcsec from the target coordinate; peak pixel [8, 7] and target pixel [8, 7]. Image-model fractional residual 0.296 is not a calibrated position error. Capable Gaia neighbors: None within 60 arcsec under the approximate G-band flux budget. The intrinsic neighbor requirement is not the same as the blended pixel loss.
4. **Alternative reduction:** independent target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture extraction gives 212.51/210.43/203.81 ppt in 1 stacked events; selected QLP raw depth is 200.11 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution, event-kind mixing and temporal changes limit a direct depth comparison.
5. **Gaia geometry:** matched DR3 source 5705460089589085952 has SB1 period 17.3434002638 d, e = 0.43675. The closest edge-on conjunction differs from the measured eclipse epoch by 0.50447 d (0.02909 phase); the linear propagated timing scale from source-specific full SB1 covariance is 0.51559 d. Rough central duration 9.27 h versus measured median 7.07 h uses TIC radius and a minimum-mass main-sequence companion; it is not a physical fit or a sigma veto.

**Deciding interpretation and limitations:** Three broad deep raw events in S8/99, including consecutive S99 cycles. The S99 target-centered deficit is supported by all three apertures, though that historical image stack contains one event only.

**Next check:** Optional resolved photometry or spectroscopy for precision binary parameters; no bounded admission check remains missing.

Catalogue novelty: the central seven-group check in ../../shared-catalogues/coverage-matrix.csv reports complete scoped coverage and no identified prior eclipsing-binary match for this exact target. This is not exhaustive priority and does not resolve embargoed identities.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 8 | 0 | 1519.4094921 | 0.010417 | 203.51 | used |
| 99 | 146 | 4052.4406638 | 0.001157 | 200.11 | used |
| 99 | 147 | 4069.7902328 | 0.001157 | 199.95 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s99.json, historical/diff_s99.png and historical/gaia.json. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). Source code and retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R468. Public evidence files: [diff_s99.json](../../evidence/294082465/historical/diff_s99.json), [diff_s99.png](../../evidence/294082465/historical/diff_s99.png), [gaia.json](../../evidence/294082465/historical/gaia.json), [measurements.json](../../evidence/294082465/measurements.json), [raw-events.png](../../evidence/294082465/raw-events.png), [raw-windows.csv](../../evidence/294082465/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch06/INDEX.md). 
